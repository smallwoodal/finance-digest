# Finance Reading Digest

> A daily Markdown digest of high-signal financial articles, summarised by Claude with a hedge-fund-analyst lens.

## Why / how it works

This is a data pipeline with three stages:

1. **Ingest** — fetch new items from a curated list of RSS feeds (last 24 hours only)
2. **Process** — extract full article text, then produce genuinely useful, differentiated summaries using Claude's `web_search` tool to "read around" each piece and assess whether it's consensus or non-consensus
3. **Output** — one Markdown file (`digests/YYYY-MM-DD.md`) committed back to the repo each morning

The key decision is the **processing spec**: how summaries should be written, what "good" looks like, and how to score relevance. **This is intentionally easy to edit** — see `prompts/`.

### What "differentiated" means

The summariser roleplays as a hedge fund analyst whose job is to surface:
- What the author argues that mainstream sell-side or financial media does **not** say
- Unique data or proprietary analysis not widely cited elsewhere
- A framework that is genuinely novel or underused
- A conclusion that contradicts recent market consensus

It **never fabricates**. If it can't confidently judge consensus vs differentiated, it says so and sets `Differentiation confidence: Low`.

---

## Setup

### 1. Fork or clone this repo

### 2. Add your Anthropic API key as a GitHub Secret

Go to your repo → **Settings → Secrets and variables → Actions → New repository secret**:

| Name | Value |
|------|-------|
| `ANTHROPIC_API_KEY` | Your key from [console.anthropic.com](https://console.anthropic.com) |

### 3. (Optional) Set the model

Go to **Settings → Secrets and variables → Actions → Variables → New repository variable**:

| Name | Example value | Notes |
|------|---------------|-------|
| `ANTHROPIC_MODEL` | `claude-opus-4-6` | Default: `claude-sonnet-4-6` |

Sonnet 4.6 is the recommended default — fast, capable, and cost-effective for daily batch jobs. Use Opus 4.6 for deeper analysis at higher cost.

### 4. Enable GitHub Actions

The workflow (`.github/workflows/digest.yml`) runs automatically at **07:00 UTC daily**. You can also trigger it manually:

> Actions → **Daily Finance Digest** → **Run workflow**

---

## Running locally

```bash
pip install -r requirements.txt

ANTHROPIC_API_KEY=sk-ant-... \
ANTHROPIC_MODEL=claude-sonnet-4-6 \
python scripts/run_digest.py
```

The digest is written to `digests/YYYY-MM-DD.md` and `digests/latest.md`.

**Optional environment variables:**

| Variable | Default | Description |
|----------|---------|-------------|
| `ANTHROPIC_MODEL` | `claude-sonnet-4-6` | Claude model to use |
| `LOOKBACK_HOURS` | `24` | Hours to look back for new articles |
| `WEB_SEARCH_TOOL_TYPE` | `web_search_20250305` | Anthropic tool type name |

---

## Configuration

### `feeds.yaml`

The list of RSS sources to monitor. Each entry:

```yaml
feeds:
  - name: "Source Name"          # display name in digest
    url: "https://source.com/"   # canonical URL (for reference)
    rss_url: "https://source.com/feed"   # actual RSS/Atom feed URL
```

### `interests.yaml`

Your coverage lens — topics, regions, sectors. Claude uses this to judge relevance and write the `Relevance` and `Verdict` fields. Edit freely.

### `prompts/`

| File | Purpose |
|------|---------|
| `prompts/system.txt` | System prompt: analyst persona, strict "no hallucination" rules, output schema |
| `prompts/user_template.txt` | Per-article user prompt with placeholders |

**Edit these to change how summaries are written.** The model is instructed to return only valid JSON — the output schema is defined in `system.txt`.

---

## How to add more feeds

### Substack publications

The RSS URL is almost always:
```
https://<publication>.substack.com/feed
```

### Beehiiv newsletters

Look for the feed URL in the publication's settings or use the pattern:
```
https://rss.beehiiv.com/feeds/<FEED_ID>.xml
```

### General

1. Use a browser extension like "RSS Feed Finder" or "Feedly" to discover a site's feed
2. Add an entry to `feeds.yaml`:

```yaml
  - name: "New Source"
    url: "https://newsource.com/"
    rss_url: "https://newsource.com/feed"
```

3. Test locally:

```bash
ANTHROPIC_API_KEY=sk-ant-... python scripts/run_digest.py
```

---

## Output format

`digests/YYYY-MM-DD.md` — one file per day, committed automatically. Always also copied to `digests/latest.md`.

Each article block:

```
## Source Name

- ***Author*** — Title (YYYY-MM-DD)
  https://article-link

**Thesis:** Core argument in 1-2 sentences
**Key data:**
  - Specific data point or statistic cited
**Names/tickers:** AAPL, MSFT, or —
**Differentiation vs consensus:** What's non-consensus or uniquely evidenced
**Differentiation confidence:** High|Med|Low
**Relevance:** High|Med|Low — one-sentence explanation tied to interests.yaml
→ Worth reading in full if ... | Skip unless ...
```

At the bottom of each digest, an `## Errors` section lists any feeds or articles that failed to process.

---

## State management

`state.json` tracks seen article IDs/links so articles are never re-processed. It is committed back to the repo on each workflow run. Entries older than 30 days are automatically pruned.

To force re-processing of all articles, delete `state.json` (or reset `"seen": {}`) and re-run.

---

## Architecture

```
feeds.yaml          → feedparser → entries (last 24h, de-duped via state.json)
                                        ↓
                        fetch_article_text()
                          trafilatura → readability-lxml → RSS summary
                                        ↓
                        summarise_article()
                          Claude (model configurable)
                            + web_search_20250305 tool (max 2× per article)
                              → searches to assess consensus framing
                            → returns JSON summary
                                        ↓
                        render_digest() → digests/YYYY-MM-DD.md
                                        → digests/latest.md
                                        → state.json (updated)
```

Text extraction priority:
1. **trafilatura** — fetches URL and extracts readable text (best for full articles)
2. **readability-lxml** — fallback HTML parser
3. **RSS summary** — last resort (often truncated on Substack etc.)

Summarisation uses Anthropic's `web_search_20250305` built-in tool (server-executed). Claude performs up to 2 web searches per article to understand mainstream framing before assessing differentiation.
