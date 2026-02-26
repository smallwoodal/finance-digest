# 📚 Your reading list — 4 new posts (last 24h)

Generated: 2026-02-26T18:12:28Z

## SemiAnalysis (Substack)

- ***Wega Chu*** — Vera Rubin – Extreme Co-Design: An Evolution from Grace Blackwell Oberon (2026-02-25)
  https://newsletter.semianalysis.com/p/vera-rubin-extreme-co-design-an-evolution

**Thesis:** Nvidia's Vera Rubin (VR NVL72) represents an 'extreme co-design' evolution from Grace Blackwell, turning the full rack into a single distributed accelerator via six proprietary silicon products — a moat that deepens as rack-scale integration complexity rises. The article provides granular silicon-level, BoM, and supply-chain intelligence that goes substantially beyond public CES disclosures.
**Key data:**
  - Rubin FP4/FP8 FLOPs ~3.5x vs GB200; FP16/BF16 only ~1.6x — architectural bet on low-precision dominance
  - HBM4 bandwidth target: 22 TB/s (2.75x Blackwell), up from 13 TB/s originally advertised at GTC 2025
  - Initial HBM4 shipments expected at ~20 TB/s, below Nvidia's 22 TB/s spec, due to supplier qualification challenges
  - Micron 'effectively out of the picture' for Rubin HBM4; SK Hynix ~60% share, Samsung ~30% projected for first 12 months
  - Nvidia demanded HBM4 pin speeds well above JEDEC spec, forcing all three DRAM suppliers to redesign
  - Rubin GPU transistor count: 336 billion (60% increase vs Blackwell)
  - SM count rises from 160 to 224; Tensor Core width doubled to 32,768 FP4 MACs/clock; clock speed up 25% to 2.38 GHz
  - NVLink-C2C bandwidth doubled to 1.8 TB/s for Vera CPU connection
  - Adaptive compression engine in 3rd-gen Transformer Engine replaces rigid 2:4 structured sparsity, enabling up to 50 PFLOPS effective FP4 without accuracy loss
  - Hyperscaler customisation of rack design is now significantly more limited than with Grace Blackwell
  - VR NVL72 BoM model launched covering compute trays, NVLink system, liquid cooling, PCB/substrate, connectors, power delivery, mechanical structure, management modules, and networking
  - Rubin GPU moves to 3nm process; I/O disaggregated into chiplets while retaining 2 reticle-sized dies + 8 HBM stacks
**Names/tickers:** Nvidia (NVDA), Micron (MU), SK Hynix (000660.KS), Samsung (005930.KS), AMD (AMD), Google (GOOGL), Amazon (AMZN), TSMC (TSM), Groq, SemiAnalysis, Wega Chu
**Differentiation vs consensus:** Mainstream sell-side and financial media coverage of Vera Rubin is almost entirely limited to Nvidia's own CES 2026 marketing claims: 3.5x FP4 compute, 22 TB/s HBM4, 2H26 delivery, and narrative around 'extreme co-design.' What SemiAnalysis adds that is non-consensus or proprietary: (1) Micron is 'effectively out of the picture' for Rubin HBM4 — a specific supply-chain call that was first reported by SemiAnalysis in January 2026 and has since become somewhat circulated but is not yet baked into most Micron bull cases; the article reaffirms it with pin-speed detail (Samsung and SK Hynix samples at ~10 Gbps vs Micron 'much lower'). (2) Initial HBM4 shipments will likely come in at ~20 TB/s, not the 22 TB/s spec — a concrete downside qualification-risk flag absent from consensus. (3) The architectural decision to double Tensor Core width ONLY for FP4/FP8 (BF16/TF32 remain Blackwell-equivalent at 1.6x) is underappreciated by generalist coverage that leads with '3.5x' headline numbers. (4) Sparse FLOPs have been abandoned across the industry (AMD MI355X dropped them; Nvidia replaced with adaptive compression) — this is a regime change that generalist coverage ignores. (5) Hyperscaler customisation of rack design is now 'much more limited' under VR NVL72 than GB200 — a structural shift in Nvidia's supply chain control with direct component vendor implications. (6) The full BoM model launch is proprietary primary research unavailable elsewhere. Differentiation is partially diluted by the Micron/HBM4 story having circulated since late January 2026.
**Differentiation confidence:** Med
**Relevance:** Med — Highly relevant to the 'Semis / compute economics' and 'AI applications in finance' interests given the granular BoM, supply-chain, and TCO analysis for a $500B build cycle, but the article has no UK/European equities angle and is deep semiconductor engineering — best suited for analysts with a semis sub-sector mandate or those evaluating Nvidia, HBM suppliers, or AI infrastructure supply chains.
→ Worth reading in full if you are actively trading or researching Nvidia, SK Hynix, Samsung, or Micron around Rubin ramp timing, or need granular BoM/TCO intelligence for AI infrastructure cost modelling. Skip unless your mandate covers semis or compute-infrastructure supply chains — the article is highly technical and the highest-signal items (Micron HBM4 exclusion, 20 TB/s vs 22 TB/s gap, hyperscaler customisation restriction) can be extracted from the free-tier summary without the full paywalled BoM model.

## The MacroTourist

- ***Kevin Muir*** — M'tourist Private Feed Recap (2026-02-26)
  https://posts.themacrotourist.com/p/mtourist-private-feed-recap-85e

**Thesis:** Article content is not accessible — the article body is paywalled and contains no substantive text beyond a subscription prompt.
**Names/tickers:** Kevin Muir
**Differentiation vs consensus:** Cannot assess — the article is behind a paywall and no content was provided beyond the title and a subscription gate. No thesis, data, or argument is visible to evaluate against consensus.
**Differentiation confidence:** Low
**Relevance:** Low — No content is available to assess relevance against the user's stated interests in UK mid-caps, European equities, banks, AI in finance, or semis/compute economics.
→ Skip unless — you are already a paid MacroTourist subscriber and can access the full content directly; no assessment is possible from the text provided.

## A Wealth of Common Sense

- ***Ben Carlson*** — Can You Live Off Your Dividends? (2026-02-26)
  https://awealthofcommonsense.com/2026/02/can-you-live-off-your-dividends/

**Thesis:** High-yielding covered call ETFs (e.g. SPYI at 12%, YieldMax single-stock funds at 37-43%) are not a shortcut past the 4% rule because price returns are near zero, leaving retirees fully exposed to inflation erosion and income variability in downturns.
**Key data:**
  - $1.6M taxable brokerage + $250k 401k + $150k cash = ~$2M net worth
  - $170k annual income target implies 8.5% withdrawal rate on $2M portfolio
  - 4% rule would require $4.25M to support $170k spending
  - SPYI covered call ETF quoted yield: 12%
  - $1.4M invested at 12% yield = $170k/year income
  - YieldMax Amazon covered call ETF yield: 43%
  - YieldMax Google covered call ETF yield: 39%
  - YieldMax Apple covered call ETF yield: 37%
  - Price returns on major covered call funds: essentially flat over recent years
  - During 'Liberation Day' sell-off, covered call funds fell 16-22%
  - 3% inflation rate makes $1 today worth ~$0.40 in 30 years
**Names/tickers:** SPYI, YieldMax, Amazon, Google, Apple, Ben Carlson, Bill Sweet, A Wealth of Common Sense
**Differentiation vs consensus:** The article's core point — that covered call ETF 'yield' is largely a return-of-capital illusion masking near-zero price appreciation, not genuine income generation — is not contrarian; it is well-covered in mainstream ETF commentary and widely flagged by Morningstar, Bloomberg, and financial advisors. The Liberation Day drawdown data (16-22% for covered call funds) is a useful concrete reference but not proprietary. The YieldMax single-stock yield figures (37-43%) are striking but widely cited in retail financial media. No novel framework, proprietary data, or non-consensus conclusion is present. This is competent consumer financial education, not differentiated institutional analysis.
**Differentiation confidence:** Low
**Relevance:** Low — This is generic personal finance and retirement planning content with no connection to the user's stated interests in UK mid-caps, European equities, AI in finance, banks, market structure, alternative data, or semis/compute economics.
→ Skip unless you need plain-English covered call explainer content for client communication purposes — no institutional or analytical value for a hedge fund analyst.

## Statecraft

- ***Santi Ruiz*** — When FAFSA Broke, They Called This Guy (2026-02-26)
  https://www.statecraft.pub/p/when-fafsa-broke-they-called-this

**Thesis:** A Q&A with College Board President Jeremy Singer about his six-month salvage operation at the Department of Education following the botched 2023 FAFSA redesign rollout, exploring what went wrong with the federal software project and how it was stabilised.
**Key data:**
  - Roughly 17 million people access FAFSA annually (students and families combined)
  - At least 6 million students fill out FAFSA per year
  - FAFSA was redesigned to reduce questions from ~100 to 36
  - New system was supposed to launch October 2023; it launched late December 2023 in pieces
  - 1.7 million students were eligible for maximum Pell Grants in the 2025-26 application cycle post-fix
  - Singer spent six months (from ~June 2024) at the Department of Education leading the cleanup
  - IRS data integration was the core technical innovation — reducing completion time from hours to under 10 minutes for some applicants
  - The fix was modelled on the Obama-era ACA exchange rescue, which brought in private-sector software talent
**Names/tickers:** Jeremy Singer, College Board, Kaplan, McGraw Hill Education, Department of Education, Lamar Alexander, Raj Chetty, Harvard, IRS, Louisiana State
**Differentiation vs consensus:** Mainstream coverage (NPR, Inside Higher Ed, GAO) focused on the failures: 55 technical defects, 9% drop in applicants, $1.8B mistake in aid calculations, and management dysfunction. This article offers something mainstream coverage largely lacks: a first-person insider account of the salvage operation itself — specifically the decision to model the fix on the ACA exchange rescue and the role of private-sector software talent. Singer's framing that Congress's precise statutory drafting (not just DoE management failures) was a root cause is a differentiated angle not prominently featured in GAO or media post-mortems. However, the article is cut off before Singer elaborates on this mechanism, limiting the depth of differentiated insight that can be confirmed.
**Differentiation confidence:** Low
**Relevance:** Low — The article covers US federal education policy and a government software project failure — entirely outside the user's stated interest areas of UK/European equities, financials, AI in finance, semis/compute, and alternative data.
→ Skip unless you are specifically interested in US government technology project management or federal education policy; no relevance to the stated investment coverage universe.

## Errors

- Cassandra Unchained (Michael Burry): empty feed — <unknown>:2:751: not well-formed (invalid token)
- The Bear Cave: empty feed — <unknown>:2:751: not well-formed (invalid token)
- Kyla's Newsletter: empty feed — <unknown>:2:751: not well-formed (invalid token)
- Stay-At-Home Macro (SAHM): empty feed — <unknown>:2:751: not well-formed (invalid token)
- While Stocks Last: empty feed — <unknown>:2:751: not well-formed (invalid token)
- Capital Wars: empty feed — <unknown>:2:751: not well-formed (invalid token)
- The Sleepwell Strategy: empty feed — <unknown>:2:751: not well-formed (invalid token)
- Behind the Balance Sheet: empty feed — <unknown>:2:751: not well-formed (invalid token)
