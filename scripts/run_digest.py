#!/usr/bin/env python3
"""
Finance Reading Digest Generator

Fetches RSS feeds, extracts full article text, summarises each piece using
Claude with the web_search built-in tool (for "reading around"), and outputs
a daily Markdown digest committed back to the repo.

Usage:
    ANTHROPIC_API_KEY=sk-ant-... ANTHROPIC_MODEL=claude-sonnet-4-6 \\
        python scripts/run_digest.py

Environment variables:
    ANTHROPIC_API_KEY       Required. Your Anthropic API key.
    ANTHROPIC_MODEL         Optional. Default: claude-sonnet-4-6
    LOOKBACK_HOURS          Optional. Hours to look back for new articles. Default: 24
    WEB_SEARCH_TOOL_TYPE    Optional. Anthropic tool type. Default: web_search_20250305
    SLACK_WEBHOOK_URL       Optional. If set, posts a condensed digest to Slack.
"""

import os
import json
import re
import sys
import time
import logging
import datetime
from pathlib import Path
from typing import Any, Optional

import yaml
import feedparser
import requests
import anthropic
import trafilatura

# Optional richer text extractors
try:
    from readability import Document as ReadabilityDoc
    HAS_READABILITY = True
except ImportError:
    HAS_READABILITY = False
    ReadabilityDoc = None  # type: ignore[assignment,misc]

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False
    BeautifulSoup = None  # type: ignore[assignment,misc]

# ── Logging ────────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-7s  %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)

# ── Paths ──────────────────────────────────────────────────────────────────────
REPO_ROOT       = Path(__file__).resolve().parent.parent
FEEDS_FILE      = REPO_ROOT / "feeds.yaml"
INTERESTS_FILE  = REPO_ROOT / "interests.yaml"
STATE_FILE      = REPO_ROOT / "state.json"
DIGESTS_DIR     = REPO_ROOT / "digests"
PROMPTS_DIR     = REPO_ROOT / "prompts"

DIGESTS_DIR.mkdir(parents=True, exist_ok=True)

# ── Constants (overridable via env) ───────────────────────────────────────────
LOOKBACK_HOURS       = int(os.environ.get("LOOKBACK_HOURS", "24"))
WEB_SEARCH_TOOL_TYPE = os.environ.get("WEB_SEARCH_TOOL_TYPE", "web_search_20250305")
SLACK_WEBHOOK_URL    = os.environ.get("SLACK_WEBHOOK_URL", "")
MAX_ARTICLE_CHARS    = 10_000   # chars sent to Claude per article
REQUEST_TIMEOUT      = 20       # seconds for outbound HTTP
INTER_ARTICLE_SLEEP  = 1.5      # polite pacing (seconds) between article API calls
STATE_RETENTION_DAYS = 30       # days before pruning seen-entry records


# ── YAML / state helpers ───────────────────────────────────────────────────────

def load_yaml(path: Path) -> Any:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_state() -> dict:
    if STATE_FILE.exists():
        with open(STATE_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {"seen": {}}


def save_state(state: dict) -> None:
    """Persist state to disk, pruning entries older than STATE_RETENTION_DAYS."""
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(
        days=STATE_RETENTION_DAYS
    )
    seen = state.get("seen", {})
    pruned: dict[str, str] = {}
    for uid, ts in seen.items():
        try:
            dt = datetime.datetime.fromisoformat(ts.rstrip("Z")).replace(
                tzinfo=datetime.timezone.utc
            )
            if dt > cutoff:
                pruned[uid] = ts
        except Exception:
            pruned[uid] = ts  # keep on parse error
    state["seen"] = pruned
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, default=str)


# ── Feed helpers ───────────────────────────────────────────────────────────────

def entry_uid(entry) -> str:
    """Return a stable unique ID for a feed entry."""
    return (
        getattr(entry, "id", None)
        or getattr(entry, "link", None)
        or getattr(entry, "title", None)
        or ""
    )


def parse_pub_dt(entry) -> Optional[datetime.datetime]:
    """Return a timezone-aware UTC datetime for when the entry was published."""
    for attr in ("published_parsed", "updated_parsed", "created_parsed"):
        val = getattr(entry, attr, None)
        if val:
            try:
                return datetime.datetime(*val[:6], tzinfo=datetime.timezone.utc)
            except Exception:
                pass
    return None


def is_recent(entry, hours: int = LOOKBACK_HOURS) -> bool:
    """True if the entry was published within the last N hours."""
    pub = parse_pub_dt(entry)
    if pub is None:
        return True  # include if we can't determine age
    now = datetime.datetime.now(datetime.timezone.utc)
    return (now - pub).total_seconds() <= hours * 3600


# ── Text extraction ────────────────────────────────────────────────────────────

def strip_html(html: str) -> str:
    """Strip HTML tags; prefers BeautifulSoup if available."""
    if HAS_BS4 and BeautifulSoup is not None:
        try:
            return BeautifulSoup(html, "lxml").get_text(separator="\n").strip()
        except Exception:
            pass
    return re.sub(r"<[^>]+>", " ", html).strip()


def fetch_article_text(entry, link: str) -> str:
    """
    Try to retrieve readable article text via multiple strategies.

    Priority:
      1. RSS full content field (if >= 500 chars after stripping HTML)
      2. trafilatura (fetch + extract)
      3. readability-lxml (if installed)
      4. RSS summary fallback
    """
    # 1. RSS full content
    content = getattr(entry, "content", None)
    if content and isinstance(content, list) and content:
        raw = content[0].get("value", "")
        if raw:
            cleaned = strip_html(raw)
            if len(cleaned) > 500:
                return cleaned[:MAX_ARTICLE_CHARS]

    # 2. trafilatura
    try:
        downloaded = trafilatura.fetch_url(link)
        if downloaded:
            extracted = trafilatura.extract(
                downloaded,
                include_comments=False,
                include_tables=True,
                no_fallback=False,
            )
            if extracted and len(extracted) > 200:
                return extracted[:MAX_ARTICLE_CHARS]
    except Exception as exc:
        logger.debug(f"trafilatura failed ({link}): {exc}")

    # 3. readability-lxml
    if HAS_READABILITY and ReadabilityDoc is not None:
        try:
            resp = requests.get(
                link,
                timeout=REQUEST_TIMEOUT,
                headers={"User-Agent": "Mozilla/5.0 (finance-digest/1.0; +https://github.com)"},
            )
            resp.raise_for_status()
            doc = ReadabilityDoc(resp.text)
            text = strip_html(doc.summary())
            if text and len(text) > 200:
                return text[:MAX_ARTICLE_CHARS]
        except Exception as exc:
            logger.debug(f"readability failed ({link}): {exc}")

    # 4. RSS summary
    summary = getattr(entry, "summary", "")
    if summary:
        return strip_html(summary)[:MAX_ARTICLE_CHARS]

    return "(full text unavailable)"


# ── JSON parsing ───────────────────────────────────────────────────────────────

def parse_json_from_text(text: str) -> Optional[dict]:
    """Extract a JSON object from text that may be wrapped in prose or fences."""
    stripped = text.strip()

    # Direct parse
    try:
        obj = json.loads(stripped)
        if isinstance(obj, dict):
            return obj
    except json.JSONDecodeError:
        pass

    # Fenced code block (```json or ```)
    for pat in (r"```json\s*([\s\S]+?)\s*```", r"```\s*([\s\S]+?)\s*```"):
        m = re.search(pat, stripped)
        if m:
            try:
                obj = json.loads(m.group(1).strip())
                if isinstance(obj, dict):
                    return obj
            except json.JSONDecodeError:
                pass

    # Bare JSON object (first { ... })
    m = re.search(r"(\{[\s\S]+\})", stripped)
    if m:
        try:
            obj = json.loads(m.group(1))
            if isinstance(obj, dict):
                return obj
        except json.JSONDecodeError:
            pass

    return None


def error_summary(msg: str) -> dict:
    return {
        "thesis": f"Processing error: {msg[:200]}",
        "key_data": [],
        "names_tickers": [],
        "differentiation_vs_consensus": "Unable to assess — processing error.",
        "differentiation_confidence": "Low",
        "relevance": "Low",
        "relevance_reason": "Processing error — see the Errors section of this digest.",
        "verdict": "Unable to process — check run logs.",
    }


# ── Summarisation ──────────────────────────────────────────────────────────────

def _collect_tool_events(content: list) -> list[dict]:
    """Pull web_search tool_use events from a response content list for logging."""
    events: list[dict] = []
    for block in content:
        if getattr(block, "type", None) == "tool_use":
            if getattr(block, "name", None) == "web_search":
                inp = getattr(block, "input", {}) or {}
                events.append(
                    {
                        "query": inp.get("query", "") if isinstance(inp, dict) else "",
                        "tool_use_id": getattr(block, "id", ""),
                    }
                )
    return events


def summarise_article(
    article: dict,
    system_prompt: str,
    user_template: str,
    interests_yaml_str: str,
    client: anthropic.Anthropic,
) -> tuple[dict, list[dict]]:
    """
    Call Claude with the web_search built-in tool and return:
        (summary_dict, web_search_citations_list)

    The web_search_20250305 tool is server-executed by Anthropic's infrastructure.
    Claude can call it up to 2× per article to "read around" and assess consensus
    framing before producing the final JSON summary.

    Falls back to no-tools if the tool type is rejected (e.g. unsupported region).
    """
    user_message = (
        user_template.replace("{INTERESTS_YAML}", interests_yaml_str)
        .replace("{ARTICLE_TITLE}", article.get("title", "(no title)"))
        .replace("{ARTICLE_AUTHOR}", article.get("author", "Unknown"))
        .replace("{ARTICLE_SOURCE}", article.get("source", ""))
        .replace("{ARTICLE_PUBLISHED}", str(article.get("published", "")))
        .replace("{ARTICLE_URL}", article.get("link", ""))
        .replace("{ARTICLE_TEXT}", article.get("text", "")[:8000])
    )

    model = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")
    tools: list[dict] = [
        {
            "type": WEB_SEARCH_TOOL_TYPE,
            "name": "web_search",
            "max_uses": 2,
        }
    ]

    messages: list[dict] = [{"role": "user", "content": user_message}]
    web_search_citations: list[dict] = []
    use_tools = True

    for iteration in range(8):  # guard against run-away agentic loops
        try:
            response = client.messages.create(
                model=model,
                max_tokens=2048,
                system=system_prompt,
                messages=messages,
                tools=tools if use_tools else [],
            )
        except anthropic.BadRequestError as exc:
            # Tool type unsupported for this account/region — retry without tools
            if use_tools:
                logger.warning(
                    f"web_search tool rejected — retrying without it: {exc}"
                )
                use_tools = False
                messages = [{"role": "user", "content": user_message}]
                continue
            return error_summary(str(exc)), []
        except anthropic.APIError as exc:
            return error_summary(str(exc)), web_search_citations

        # Collect tool events for audit log
        new_events = _collect_tool_events(response.content)
        for ev in new_events:
            logger.info(f"    [web_search] {ev['query']!r}")
        web_search_citations.extend(new_events)

        # ── Case 1: done ──────────────────────────────────────────────────────
        if response.stop_reason == "end_turn":
            final_text = "".join(
                getattr(block, "text", "")
                for block in response.content
                if getattr(block, "type", None) == "text"
            )
            parsed = parse_json_from_text(final_text)
            if parsed:
                return parsed, web_search_citations
            logger.warning(
                f"JSON parse failed. Raw response (first 500 chars): {final_text[:500]}"
            )
            return (
                error_summary("Model did not return valid JSON"),
                web_search_citations,
            )

        # ── Case 2: tool_use stop (shouldn't happen for server-side tools, ──
        # ── but handle gracefully as a fallback) ─────────────────────────────
        elif response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            tool_results = [
                {
                    "type": "tool_result",
                    "tool_use_id": getattr(block, "id", ""),
                    "content": (
                        "Web search could not be executed client-side. "
                        "Please proceed with the article text only and set "
                        "differentiation_confidence to Low."
                    ),
                }
                for block in response.content
                if getattr(block, "type", None) == "tool_use"
            ]
            if tool_results:
                messages.append({"role": "user", "content": tool_results})
            else:
                break  # no tool_use blocks to respond to

        else:
            logger.warning(f"Unexpected stop_reason: {response.stop_reason!r}")
            break

    return (
        error_summary("Agentic loop did not terminate normally"),
        web_search_citations,
    )


# ── Markdown rendering ─────────────────────────────────────────────────────────

def render_summary(s: dict) -> str:
    """Render a summary dict as indented Markdown lines."""
    lines: list[str] = []

    thesis = str(s.get("thesis", "")).strip()
    if thesis:
        lines.append(f"**Thesis:** {thesis}")

    key_data = s.get("key_data") or []
    if key_data:
        lines.append("**Key data:**")
        for item in key_data:
            lines.append(f"  - {item}")

    tickers = s.get("names_tickers") or []
    lines.append(f"**Names/tickers:** {', '.join(tickers) if tickers else '—'}")

    diff = str(s.get("differentiation_vs_consensus", "")).strip()
    conf = s.get("differentiation_confidence", "Low")
    if diff:
        lines.append(f"**Differentiation vs consensus:** {diff}")
    lines.append(f"**Differentiation confidence:** {conf}")

    rel = s.get("relevance", "Low")
    rr  = str(s.get("relevance_reason", "")).strip()
    lines.append(f"**Relevance:** {rel}" + (f" — {rr}" if rr else ""))

    verdict = str(s.get("verdict", "")).strip()
    if verdict:
        lines.append(f"→ {verdict}")

    return "\n".join(lines)


def render_digest(
    date_str: str,
    generated_at: str,
    articles_by_source: dict,
    errors: list[str],
) -> str:
    """Render the full daily digest as a Markdown string."""
    total = sum(len(v) for v in articles_by_source.values())
    lines: list[str] = [
        f"# 📚 Your reading list — {total} new post{'s' if total != 1 else ''} (last 24h)",
        "",
        f"Generated: {generated_at}",
        "",
    ]

    if not total:
        lines += ["_No new posts found in the last 24 hours._", ""]
    else:
        for source_name, items in articles_by_source.items():
            lines.append(f"## {source_name}")
            lines.append("")
            for item in items:
                author  = item.get("author", "")
                title   = item.get("title", "(no title)")
                pub     = item.get("published")
                link    = item.get("link", "")
                summary = item.get("summary", {})

                pub_str = pub.strftime("%Y-%m-%d") if isinstance(pub, datetime.datetime) else str(pub or "")

                if author:
                    lines.append(f"- ***{author}*** — {title} ({pub_str})")
                else:
                    lines.append(f"- {title} ({pub_str})")
                if link:
                    lines.append(f"  {link}")
                lines.append("")
                lines.append(render_summary(summary))
                lines.append("")

    if errors:
        lines += ["## Errors", ""]
        for err in errors:
            lines.append(f"- {err}")
        lines.append("")

    return "\n".join(lines)


# ── Slack notification ─────────────────────────────────────────────────────────

def send_to_slack(
    webhook_url: str,
    articles_by_source: dict,
    date_str: str,
    errors: list[str],
) -> None:
    """Post a condensed digest to a Slack incoming webhook using Block Kit."""
    total = sum(len(v) for v in articles_by_source.values())

    blocks: list[dict] = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": f"📚 Finance Digest — {date_str}"},
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"*{total} new article{'s' if total != 1 else ''}* in the last 24h"
                    if total
                    else "_No new articles in the last 24 hours._"
                ),
            },
        },
        {"type": "divider"},
    ]

    for source_name, items in articles_by_source.items():
        for item in items:
            title   = item.get("title", "(no title)")
            link    = item.get("link", "")
            author  = item.get("author", "")
            summary = item.get("summary", {})

            thesis    = str(summary.get("thesis", "")).strip()[:300]
            verdict   = str(summary.get("verdict", "")).strip()[:200]
            relevance = summary.get("relevance", "")
            diff_conf = summary.get("differentiation_confidence", "")

            title_link = f"<{link}|{title}>" if link else title
            byline = f" — _{author}_" if author else ""
            header_line = f"*{title_link}*{byline}  `{source_name}`"

            lines = [header_line]
            if thesis:
                lines.append(f"*Thesis:* {thesis}")
            if verdict:
                lines.append(f"→ {verdict}")
            meta: list[str] = []
            if relevance:
                meta.append(f"Relevance: {relevance}")
            if diff_conf:
                meta.append(f"Diff confidence: {diff_conf}")
            if meta:
                lines.append("  ".join(meta))

            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": "\n".join(lines)[:3000]},
            })
            blocks.append({"type": "divider"})

    if errors:
        err_lines = "\n".join(f"• {e[:200]}" for e in errors[:5])
        blocks.append({
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*⚠️ Errors:*\n{err_lines}"},
        })

    # Slack allows max 50 blocks per request — chunk if needed
    MAX_BLOCKS = 50
    for i in range(0, max(len(blocks), 1), MAX_BLOCKS):
        chunk = blocks[i : i + MAX_BLOCKS]
        try:
            resp = requests.post(
                webhook_url,
                json={"blocks": chunk},
                timeout=REQUEST_TIMEOUT,
                headers={"Content-Type": "application/json"},
            )
            resp.raise_for_status()
            logger.info(f"Slack notification sent (block chunk {i // MAX_BLOCKS + 1})")
        except Exception as exc:
            logger.error(f"Slack notification failed: {exc}")
        if i + MAX_BLOCKS < len(blocks):
            time.sleep(1)


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        logger.error("ANTHROPIC_API_KEY environment variable is not set")
        sys.exit(1)

    # Load config files
    feeds_cfg  = load_yaml(FEEDS_FILE)
    interests_cfg = load_yaml(INTERESTS_FILE)
    interests_yaml_str = yaml.dump(
        interests_cfg, allow_unicode=True, default_flow_style=False
    )

    system_prompt = (PROMPTS_DIR / "system.txt").read_text(encoding="utf-8")
    user_template = (PROMPTS_DIR / "user_template.txt").read_text(encoding="utf-8")

    state  = load_state()
    client = anthropic.Anthropic(api_key=api_key)

    now_utc  = datetime.datetime.now(datetime.timezone.utc)
    date_str = now_utc.strftime("%Y-%m-%d")
    gen_ts   = now_utc.strftime("%Y-%m-%dT%H:%M:%SZ")

    articles_by_source: dict[str, list[dict]] = {}
    errors: list[str] = []

    feeds = feeds_cfg.get("feeds", [])
    logger.info(
        f"Starting digest run — {len(feeds)} feed(s), lookback={LOOKBACK_HOURS}h, "
        f"model={os.environ.get('ANTHROPIC_MODEL', 'claude-sonnet-4-6')}"
    )

    for feed_cfg in feeds:
        feed_name = feed_cfg.get("name", "Unknown")
        rss_url   = feed_cfg.get("rss_url", "")

        logger.info(f"Fetching: {feed_name}")
        try:
            parsed  = feedparser.parse(rss_url)
            entries = parsed.entries or []
        except Exception as exc:
            msg = f"{feed_name}: RSS fetch/parse error — {exc}"
            logger.warning(msg)
            errors.append(msg)
            continue

        # bozo flag = malformed feed; warn but continue if we have entries
        if getattr(parsed, "bozo", False):
            bozo_exc = getattr(parsed, "bozo_exception", None)
            logger.debug(f"  Feed parse warning ({feed_name}): {bozo_exc}")
            if not entries:
                msg = f"{feed_name}: empty feed — {bozo_exc}"
                logger.warning(msg)
                errors.append(msg)
                continue

        new_entries = [
            e for e in entries
            if is_recent(e) and entry_uid(e) not in state["seen"]
        ]
        logger.info(f"  {len(new_entries)} new / {len(entries)} total entries")

        for entry in new_entries:
            uid    = entry_uid(entry)
            title  = getattr(entry, "title", "(no title)")
            link   = getattr(entry, "link", feed_cfg.get("url", ""))
            author = getattr(entry, "author", "") or ""
            pub_dt = parse_pub_dt(entry) or now_utc

            logger.info(f"  → {title[:80]}")

            # Text extraction
            try:
                text = fetch_article_text(entry, link)
            except Exception as exc:
                text = "(text extraction failed)"
                err_msg = f'{feed_name} / "{title[:60]}": text extraction — {exc}'
                logger.warning(err_msg)
                errors.append(err_msg)

            article: dict = {
                "title":     title,
                "author":    author,
                "source":    feed_name,
                "published": pub_dt,
                "link":      link,
                "text":      text,
            }

            # Summarise via Claude + web_search
            try:
                summary, citations = summarise_article(
                    article, system_prompt, user_template, interests_yaml_str, client
                )
                if citations:
                    logger.info(f"    {len(citations)} web search(es) performed")
            except Exception as exc:
                logger.error(f'  Summarisation failed for "{title[:60]}": {exc}')
                summary   = error_summary(str(exc))
                citations = []
                err_msg = f'{feed_name} / "{title[:60]}": summarisation — {exc}'
                errors.append(err_msg)

            article["summary"]   = summary
            article["citations"] = citations
            articles_by_source.setdefault(feed_name, []).append(article)

            # Mark as seen (persist even on partial failures)
            state["seen"][uid] = gen_ts

            time.sleep(INTER_ARTICLE_SLEEP)

    # Persist state
    save_state(state)

    # Render digest
    digest_md   = render_digest(date_str, gen_ts, articles_by_source, errors)
    digest_path = DIGESTS_DIR / f"{date_str}.md"
    latest_path = DIGESTS_DIR / "latest.md"

    digest_path.write_text(digest_md, encoding="utf-8")
    latest_path.write_text(digest_md, encoding="utf-8")

    total = sum(len(v) for v in articles_by_source.values())
    logger.info(f"Digest written: {digest_path}")
    logger.info(f"Run complete — {total} article(s) processed, {len(errors)} error(s)")

    if errors:
        logger.warning("Errors encountered (also listed in digest):")
        for err in errors:
            logger.warning(f"  {err}")

    if SLACK_WEBHOOK_URL:
        send_to_slack(SLACK_WEBHOOK_URL, articles_by_source, date_str, errors)
    else:
        logger.info("SLACK_WEBHOOK_URL not set — skipping Slack notification")


if __name__ == "__main__":
    main()
