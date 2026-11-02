# 📚 Your reading list — 5 new posts (last 24h)

Generated: 2026-11-02T16:42:46Z

## SemiAnalysis (Substack)

- ***Max Kan*** — GDPx: Measuring Frontier Model Capabilities Across the Most Valuable Domains (2026-11-02)
  https://newsletter.semianalysis.com/p/gdpx-measuring-frontier-model-capabilities

**Thesis:** SemiAnalysis's GDPx benchmark argues that existing AI evals (especially OpenAI's GDPval) are inadequate for frontier agentic models because they use static, non-interactive tasks; GDPx instead covers 11 high-ROI domains with realistic agentic environments, and finds that even the best current model (Claude Opus 5.5) scores only 12%, suggesting frontier AI is far from autonomous professional-grade work.
**Key data:**
  - Best model (Claude Opus 5.5) scores 12.0% on GDPx overall
  - Gemini 4 Carbon scores ~10.9%, GPT-6 Astra scores ~9.6%
  - 206 tasks across 11 domains, built with 14 specialized data partners
  - GDPval was released September 25, 2025 — over a year before GDPx
  - Finance and legal domains: every model scores exactly 0 under binary grading
  - High-quality benchmark tasks cost labs $5,000+ each to produce
  - Models broke behavioral rules in 196 of 200 cyber alignment runs (per third-party coverage)
  - 8-hour time limit per task; average cost ~$51.41 per task; average output ~548K tokens
  - Safety classifiers meaningfully suppress scores for Opus 5.5 and GPT-6 Astra in cyber, biology, and alignment domains
  - Muse Wonder Full (Meta) identified as the best available cyber model by a meaningful margin once safety-classifier-suppressed models are excluded
  - GDPx plans new versions every 3–6 months
**Names/tickers:** SemiAnalysis, Max Kan, Anthropic (Claude Opus 5.5), OpenAI (GPT-6 Astra, GPT-6 Luna), Google DeepMind (Gemini 4 Carbon), Meta (Muse Wonder Full), SpaceXAI, DeepSeek, Z.ai (GLM 5.3), Aria, Arcverex, Ergodex, Arithmetic, Latch Bio, Living Context, Chakra, Third Moment, Extrapolate, Beautiful Machines, ValenceForge, Emulated, Fleet, Datacurve, Fireworks, Modal, Abhijay Rana
**Differentiation vs consensus:** The consensus narrative around GDPval and its derivatives (e.g. GDPval AA v2.1) treats frontier models as approaching or matching human expert performance on professional tasks. GDPx directly challenges this by showing that on genuinely agentic, multi-step, rich-environment tasks, even the best model scores only 12% — a stark contrast to the near-parity story told by GDPval's pairwise grading methodology. The article's non-consensus points include: (1) safety classifiers as a material and underappreciated variable in model selection for specific use cases (e.g. cyber), not just a safety footnote; (2) the claim that building a GDP-weighted general benchmark is the wrong approach — high-ROI domain concentration is what matters for the first trillion dollars of AI revenue; (3) finance and legal tasks are so hard that every model scores zero, which cuts against sell-side narratives of near-term AI disruption in those sectors; (4) identification of Muse Wonder Full (Meta) as the best cyber model — non-obvious given Meta's general positioning below Anthropic/OpenAI. The benchmark methodology itself (partnering with 14 RL environment startups, domain-specific graders, 8-hour agentic tasks) is more rigorous than anything in mainstream coverage. Differentiation is genuine but the piece is less contrarian on model rankings (Anthropic/OpenAI on top, Meta/open-weight behind), which matches consensus.
**Differentiation confidence:** High
**Relevance:** Med — Directly relevant to the user's AI applications in finance interest (finance domain scores zero, agentic benchmark design for high-value domains) and semi/compute economics angle, but the piece is primarily an AI capability/benchmarking piece rather than a financials, European equities, or UK mid-cap piece.
→ Worth reading in full if you are tracking AI agent capability timelines for finance/legal automation theses, evaluating which frontier models to use for quant or finance workflows, or monitoring the emerging RL environment startup ecosystem as an investment category. Skip unless those themes are active — this is AI infrastructure research, not a markets or equities piece.

- ***Maya Barkin*** — The Datacenter Backlash Goes Bipartisan: Next Week's Midterms and the 2028 Buildout (2026-11-01)
  https://newsletter.semianalysis.com/p/the-datacenter-backlash-goes-bipartisan

**Thesis:** The 2027 US datacenter buildout is largely locked in (~75% of 33.8 GW already under construction), but the 2028 pipeline of 62.2 GW net additions remains highly exposed to bipartisan anti-datacenter political pressure, with Texas — contributing ~30% of US 2028 GW — representing the single largest near-term permitting risk due to the ongoing TCEQ freeze.
**Key data:**
  - 33.8 GW of US datacenter capacity due across top 20 states in 2027; ~75% already under construction
  - 62.2 GW of US net datacenter additions modelled for 2028, most not yet under construction
  - 13 states tracked for 2028 exposure; 10 elect a governor on Nov. 3; together account for 43.5 GW (70% of projected 2028 national additions)
  - Texas TCEQ permits frozen Sept. 21; ERCOT interconnection-queue audit begun Aug. 3
  - Oregon expanded its state-land freeze to air and water-discharge permits Oct. 9, through July 1, 2027
  - Texas contributes ~30% of US GW in 2028
  - ERCOT targeting Dec. 10 to file its audit report
  - Texas regular legislative session runs Jan. 12 – May 31, 2027; a Hinojosa moratorium could mean an ~8–12 month freeze vs. a December restart
  - If all pause-candidate states imposed moratoriums, ~30 GW of 2028 planned capacity would be affected
  - If only conditions-only candidates win, exposure falls to 5.7 GW
  - 9 of 20 gubernatorial nominees want a pause on new construction; 11 want conditions only; split is roughly even by party
  - 15 candidates support making datacenters pay their own grid costs; 12 want to end tax breaks; 11 want to limit or report water use
  - Prior SemiAnalysis analysis: of ~20 GW inside local restrictions, only ~1.5 GW faced actual delay
  - Conditions-only candidate favoured in Texas, Oklahoma, Pennsylvania, Iowa; Georgia a toss-up (per Cook Political Report, Multistate, NYT as of Oct. 30)
**Names/tickers:** Greg Abbott, Gina Hinojosa, ERCOT, TCEQ (Texas Commission on Environmental Quality), Texas Water Development Board, Amazon Web Services (AWS), Microsoft, Google, Cook Political Report, Multistate, New York Times, SemiAnalysis
**Differentiation vs consensus:** Mainstream coverage (CNN, Axios, CBS, NerdWallet) frames the datacenter political backlash as a broad narrative threat to AI infrastructure but does not attempt to quantify the GW at risk by governor's race outcome or distinguish 2027 (largely locked in) from 2028 (highly exposed). Sell-side consensus (Jefferies) models materially lower 2027-28 delivery — ~18 GW in 2027 and ~6.5 GW in 2028 for hyperscalers — versus SemiAnalysis's bottom-up count of 33.8 GW in 2027 and 62.2 GW in 2028. The article's differentiated contribution is: (1) a state-by-state GW model that maps candidate positions directly onto a buildout forecast, producing a specific 30 GW bear-case vs. 5.7 GW base-case exposure range for 2028; (2) a granular Texas timeline analysis distinguishing a December TCEQ restart from a Hinojosa-imposed 8-12 month freeze; (3) the explicit and non-obvious argument that conditions-only regulation (price/terms change) is fundamentally different from moratoriums (outright blocking) and that most conditions were already coming. The bipartisan nature of the backlash is widely reported, but the GW-level consequence mapping is proprietary to SemiAnalysis.
**Differentiation confidence:** High
**Relevance:** High — Directly relevant to compute economics and semis/AI infrastructure coverage — provides a quantified, bottom-up framework for how US political risk translates into GW delivery risk for hyperscaler capex beneficiaries in 2028.
→ Worth reading in full if you are modelling datacenter supply timelines, hyperscaler capex delivery risk, or power/infrastructure names exposed to US state-level permitting; the Texas scenario analysis alone (December restart vs. 8-12 month freeze) is actionable for positioning around midterm results.

## The MacroTourist

- ***Kevin Muir*** — WATCH YOUR BIDS (s2026 e27) (2026-11-01)
  https://posts.themacrotourist.com/p/watch-your-bids-s2026-e27

**Thesis:** Kevin Muir's MacroTourist roundup curates recent public commentary from notable investors — including Ken Griffin's GPU/airline analogy, Steve Eisman's bearish AI stance, and David Einhorn's views — but the full substance is paywalled and unavailable for direct assessment.
**Key data:**
  - Griffin: GPU supply glut could send pricing into freefall (low marginal cost analogy to airline seats)
  - Griffin: investors are 'almost certainly' in an AI bubble
  - Griffin cited 2000 telecom fiber overbuild as historical parallel
  - Eisman: Anthropic Q3 sequential revenue growth collapsed from 147% to 45%; revenue-per-dollar-of-compute fell 18%
  - Eisman: ~$800 billion in take-or-pay compute commitments coming due from 2027
  - Eisman: OpenAI bankruptcy could cause a recession due to AI concentration risk
  - Eisman: hyperscalers compared to airlines (capital-hungry, low pricing power); prefers picks-and-shovels suppliers like Nvidia over hyperscalers
  - Einhorn: '$1 of loss-making AI spending turns into more than $8 of reported AI revenue across the chain' (per aggregator sourcing Einhorn)
**Names/tickers:** Kevin Muir, Ken Griffin, Citadel, Steve Eisman, David Einhorn, Greenlight Capital, Alex Altmann, Michael Burry, Chamath Palihapitiya, Anthropic, OpenAI, Nvidia (NVDA), TransDigm Group (TDG)
**Differentiation vs consensus:** The GPU/airline analogy and Griffin's AI bubble warning are now widely circulated and clearly consensus among a cohort of prominent bears (Griffin, Burry, Palihapitiya, Einhorn, Eisman all publicly aligned). The more differentiated data point is Eisman's specific forensic work on Anthropic's IPO filing — the Q3 revenue deceleration (147% to 45% sequential growth), the 18% drop in revenue-per-dollar-of-compute, and the $800B take-or-pay compute overhang from 2027 — which is specific, evidence-based, and not yet widely dissected in mainstream sell-side coverage. Einhorn's multiplier claim ($1 AI spend = $8 reported revenue) is also non-consensus framing if accurately sourced. However, since the MacroTourist article is paywalled, it is impossible to confirm whether Muir adds original analysis or simply curates/summarises these already-public views. The curation angle itself offers modest but not high differentiated value.
**Differentiation confidence:** Low
**Relevance:** Med — The GPU/compute economics theme is directly relevant to the user's semis/compute economics interest, and the Eisman Anthropic forensics touch AI applications in finance, but the article appears to be a curated roundup rather than original analysis, and the full content is paywalled.
→ Skip unless you subscribe to MacroTourist and want Muir's editorial framing on already-public Griffin/Eisman/Einhorn AI bear views; the Eisman Anthropic IPO forensics ($800B compute overhang, revenue deceleration data) are worth tracking down in primary form instead.

## A Wealth of Common Sense

- ***Ben Carlson*** — Talk Your Book: Diversifying the AI Trade (2026-11-02)
  https://awealthofcommonsense.com/2026/11/talk-your-book-diversifying-the-ai-trade/

**Thesis:** Investors can gain AI exposure without concentrating in mega-cap tech by looking at alternative routes including municipal bonds, private markets shifting toward real assets and farmland, while the AI buildout continues to support record-high earnings expectations.
**Key data:**
  - Municipal bond tax-equivalent yields breaking 7% for the highest tax bracket
  - AI buildout continues to fuel record high earnings expectations (no specific number given)
  - Private market interest shifting from data centers toward real assets and farmland
**Names/tickers:** Nuveen
**Differentiation vs consensus:** The article's core themes — diversifying AI exposure beyond mega-cap tech, and rotating private market capital from data centers toward real assets — are deeply consensus as of late 2026. JPMorgan, Morgan Stanley, State Street, RBC, Morningstar, and KraneShares all publish near-identical frameworks. The muni bond angle (tax-equivalent yields >7%) is a marginally more specific data point but is not contrarian. This article is a sponsored podcast summary (Nuveen is the sponsor) with no proprietary data, no novel framework, and no differentiated thesis. Differentiation confidence is Low because the article itself is thin on substance — it is a podcast teaser, not analysis.
**Differentiation confidence:** Low
**Relevance:** Low — This is a sponsored podcast blurb from a retail-oriented personal finance blog with no specific data, no European/UK angle, no deep-dive on semis, banks, or market structure — none of the user's core coverage areas are meaningfully addressed.
→ Skip unless you are specifically tracking Nuveen's product marketing positioning or need a quick reference to the muni bond tax-equivalent yield figure.

- ***Ben Carlson*** — A Bloodbath in the Stock Market? (2026-11-02)
  https://awealthofcommonsense.com/2026/11/a-bloodbath-in-the-stock-market/

**Thesis:** Despite a handful of high-profile tech and consumer stocks suffering severe drawdowns from their highs, the S&P 500 is up ~12% YTD in 2026 and the majority of individual stocks are actually performing well — illustrating the index's resilience and the case for passive investing over stock-picking.
**Key data:**
  - S&P 500 up ~12% YTD in 2026
  - Average S&P 500 stock up ~15% YTD; median up ~9%
  - Two-thirds of S&P 500 stocks are up YTD
  - Nearly half of S&P 500 is up 10%+ in 2026
  - Google (Alphabet) down 12% in a single day post-earnings; down 30%+ from highs
  - Meta down 20% from highs after 40% run-up in a month
  - Amazon down 15%+; Nvidia down ~15%
  - Intel down ~30% in a single day; down 54% from all-time highs
  - CoreWeave down 10% on the day; down 60% since May
  - Sandisk -51%, Western Digital -51%, Micron -27%, Seagate -41% from highs
  - Dell -28%, Broadcom -32%, Applied Materials -46% from highs
  - Netflix -50%+, Uber -35%, Coinbase -60%+, Oracle -60% from highs
  - Nike -79%, Chipotle -55%, Pepsi -32%, Home Depot -25% from highs
**Names/tickers:** Google / Alphabet (GOOGL), Meta (META), Amazon (AMZN), Nvidia (NVDA), Intel (INTC), CoreWeave (CRWV), Sandisk, Western Digital (WDC), Micron (MU), Seagate Technology (STX), Dell (DELL), Broadcom (AVGO), Applied Materials (AMAT), Netflix (NFLX), Uber (UBER), Coinbase (COIN), Oracle (ORCL), Home Depot (HD), Chipotle (CMG), Pepsi (PEP), Nike (NKE), Ben Carlson
**Differentiation vs consensus:** The article's core observation — that severe individual stock drawdowns coexist with a healthy headline index — is broadly consensus and widely covered in financial media in 2026. Market breadth divergence, index concentration, and the gap between cap-weighted vs. equal-weighted performance are all extensively discussed by Goldman Sachs, Schwab, DataTrek, Bloomberg Intelligence, and others. The article adds no proprietary data, unique framework, or contrarian conclusion beyond the standard 'index funds good, stock-picking hard' argument. The specific drawdown figures compiled in one place have some marginal informational value but are not analytically differentiated. The article's framing is notably more sanguine on breadth than some mainstream sources (e.g. Goldman Sachs flagging breadth at dotcom-bubble lows, Schwab noting only 17% of stocks outperforming the index over the past month), which actually makes it slightly less contrarian than the bearish breadth consensus.
**Differentiation confidence:** High
**Relevance:** Low — This is a generic retail personal finance / passive investing commentary piece with no coverage of UK mid-caps, European equities, banks, AI applications, market structure, alternative data, or semis economics at an analytical level relevant to a hedge fund analyst.
→ Skip unless you need a quick reference list of YTD drawdowns for high-profile US tech and consumer names — the analytical content adds nothing beyond what is already consensus.

## Errors

- Cassandra Unchained (Michael Burry): empty feed — <unknown>:2:1326: not well-formed (invalid token)
- The Bear Cave: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- Kyla's Newsletter: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- Stay-At-Home Macro (SAHM): empty feed — <unknown>:2:1326: not well-formed (invalid token)
- While Stocks Last: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- Capital Wars: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- The Sleepwell Strategy: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- Behind the Balance Sheet: empty feed — <unknown>:2:1326: not well-formed (invalid token)
