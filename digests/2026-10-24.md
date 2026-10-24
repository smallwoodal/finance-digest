# 📚 Your reading list — 4 new posts (last 24h)

Generated: 2026-10-24T11:43:51Z

## SemiAnalysis (Substack)

- ***Kimbo Chen*** — Amazon’s Trainium Takes a Strike at the Training King (2026-10-23)
  https://newsletter.semianalysis.com/p/amazons-trainium-takes-a-strike-at

**Thesis:** Amazon's TorchNeuron represents a genuine software strategy inflection for Trainium, shifting from a painful XLA-based approach to a first-class native PyTorch training experience, potentially making Trainium3 a credible competitor to CUDA for research-grade training — not just inference.
**Key data:**
  - Trainium uses up to 80,000 physical cores allocated toward automated quality control (CI)
  - SemiAnalysis engineering team tested Trainium3 racks for ~2 weeks
  - Qwen3-32B trained on 16 Trainium2 chips (64 LNC=2 logical cores) and on a rack-scale Trainium3 UltraServer with 64 physical chips
  - AWS hired the lead of Google's native Torch on TPU effort (formerly TPU SW lead including XLA, xprof, Cloud TPU) to work on TorchNeuron
  - TorchNeuron now supports native torch.distributed.*, DTensor, SimpleFSDP, DDP — previously unavailable
  - MXFP8 training not supported on day 0; BF16 is the training baseline priority
  - Trainium Neuron Explorer profiler described as better than both Nvidia's and AMD's profilers
  - TorchTitan (popular open-source pre-training framework) is fully supported on Trainium
  - Hugging Face Accelerate, PEFT, diffusers, TRL supported in Trainium Torch ecosystem
  - 30+ early TorchNeuron customers across robotics, voice AI, and LLM development (per mainstream sources)
  - TorchNeuron entered public beta October 20, 2026, released under Apache 2.0
**Names/tickers:** Amazon (AMZN), AWS, Anthropic, Nvidia (NVDA), AMD, Google / Alphabet (GOOGL), Hugging Face, Cartesia, Deepgram, Nafea Bshara (VP at AWS), Inferact/RadixArk, Meta (META), Qwen3, TorchTitan, vLLM / SGLang, SemiAnalysis, Kimbo Chen
**Differentiation vs consensus:** Consensus coverage of TorchNeuron (TechCrunch, AboutAmazon, CryptoBriefing, etc.) focuses on the 'one-line code change' marketing narrative and lists ecosystem integrations. What SemiAnalysis adds that is genuinely non-consensus: (1) First-person, hands-on engineering validation of Trainium3 TorchTitan/TorchNeuron stack — including specific bugs encountered — giving a practitioner credibility that press releases and AWS blog posts lack. (2) The claim that Trainium's Neuron Explorer profiler is materially superior to both Nvidia's and AMD's profilers ('GPU Impossible') is a strong, differentiated, and verifiable assertion not made in any mainstream coverage found. (3) The specific talent signal — AWS hiring the former Google TPU SW lead who built XLA, xprof, and Cloud TPU from the start — is not widely cited and is a meaningful leading indicator of software quality trajectory. (4) The article contextualises the vLLM/SGLang Trainium integration as strategically analogous to Google's TPU playbook (via Inferact/RadixArk), which is a forward-looking framework mainstream media has not articulated. (5) The 80,000-core CI fleet claim, framed as superior to other accelerator vendors, is a specific and differentiated quality-infrastructure data point. However, no performance benchmarks (throughput, MFU, cost-per-token) are published in this article or by AWS, which limits the ability to assess whether the software improvements actually close the gap with CUDA on training workloads.
**Differentiation confidence:** Med
**Relevance:** Med — Directly relevant to the user's 'Semis / compute economics' and 'AI applications in finance' interest areas — specifically the competitive dynamics between Nvidia CUDA and alternative training accelerators — but contains no UK/European equities, banks, or mid-cap content.
→ Worth reading in full if you are tracking the Nvidia competitive moat thesis and want first-person practitioner signal on whether TorchNeuron genuinely de-risks Trainium3 adoption for research training; skip unless you want engineering-level detail on PyTorch backends — no performance benchmarks are provided.

## Net Interest

- ***Marc Rubinstein*** — Capital Wars (2026-10-23)
  https://www.netinterest.co/p/capital-wars

**Thesis:** AI is now as much a financing story as a technology story; CoreWeave, framed as a non-bank financial rather than a tech company, is the most sensitive barometer of AI credit conditions, and its rising cost of capital (15%+ unsecured yields, falling stock) signals systemic stress in the AI infrastructure funding model.
**Key data:**
  - Meta admitted it will need to raise 'hundreds of billions of dollars of equity over several years beginning as early as fall 2026'
  - SpaceX IPO raised $85.7 billion of equity in June 2026
  - SpaceX subsequently tapped the bond market for a further $25 billion after achieving investment-grade ratings
  - CoreWeave operates 51 data centers drawing 1.5 gigawatts of power
  - CoreWeave contracted capacity expanded from 2.9 gigawatts (Nov 2025) to 4.2 gigawatts
  - CoreWeave 2026 capex guidance: $35–39 billion
  - CoreWeave unsecured debt yields: ~15%
  - CoreWeave stock down materially; ~$4 billion of debt trading at distressed levels below 80 cents on the dollar (per Forbes)
  - CoreWeave total debt ~$35 billion principal, ~$52 billion including lease liabilities at end of Q2 2026
  - CoreWeave Q2 2026 revenue: $2.575 billion (+112% YoY); backlog: ~$104 billion
  - Meta 2026 capex raised to $135–145 billion (Q3 earnings), third raise of the year
  - Goldman Sachs upgraded CoreWeave to Buy on October 19, 2026
**Names/tickers:** CoreWeave (CRWV), Mike Intrator (CoreWeave CEO), Brian Venturo (CoreWeave CSO), Brannin McBee (CoreWeave CDO), Meta Platforms (META), SpaceX, Elon Musk, Ted Pick (Morgan Stanley CEO), Morgan Stanley (MS), Microsoft (MSFT), OpenAI, Goldman Sachs (GS), Nvidia (NVDA), Marc Rubinstein
**Differentiation vs consensus:** The mainstream framing of CoreWeave centres on the backlog-vs-debt binary (bulls cite $100B+ backlog; bears cite $50B+ debt load). Rubinstein's differentiation is the reframing of CoreWeave not as a tech or cloud company but explicitly as a non-bank financial — an entity whose viability is entirely contingent on spread compression between borrowing costs and lease yields, analogous to classic leveraged finance vehicles. This non-bank financial lens is not how sell-side (Goldman upgraded to Buy on demand narrative) or financial media typically frame it. The second differentiated claim is that CoreWeave's credit spreads function as a real-time leading indicator for the broader AI financing complex — ahead of, not coincident with, stress in the wider AI complex. The Musk/SpaceX comparison as a case study in superior capital markets execution is also a non-consensus framing. However, the broad observation that 'AI is a financing story' is now widely echoed (Forbes, CryptoBriefing, Yahoo Finance all use near-identical language), so that top-line framing is increasingly consensus. The structural non-bank-financial analogy and spread-as-barometer angle remain the genuinely differentiated elements.
**Differentiation confidence:** Med
**Relevance:** High — Directly relevant to banks/financials (non-bank financial structure analysis), market structure (AI credit markets as a new asset class), and AI applications in finance (compute economics, infrastructure financing dynamics) — all core to the stated coverage interests.
→ Worth reading in full if you are actively tracking AI infrastructure credit risk, non-bank financial analogues in tech, or need a framework for using CoreWeave's spread as a macro indicator for the AI capex cycle — the non-bank financial lens is actionable and underused by sell-side.

## A Wealth of Common Sense

- ***Ben Carlson*** — Markets Are Always Different This Time (2026-10-23)
  https://awealthofcommonsense.com/2026/10/markets-are-always-different-this-time/

**Thesis:** Markets have structurally changed so much — in sector composition, transaction costs, information access, and regulatory environment — that historical return comparisons are misleading; but on a net-of-cost basis, today's investors are better off than any prior era.
**Key data:**
  - S&P 500 in 1960: 425 industrials, 25 rail companies, 50 utilities
  - S&P 500 today: 83 industrials, 76 financials, 75 IT, 60 health care, 47 consumer discretionary, 34 consumer staples, 31 utilities, 30 real estate, 24 materials, 21 energy, 22 communication services
  - Historical brokerage costs: 2%+ for retail, 1%+ for institutions
  - Mutual fund sales loads historically 5–8% upfront, plus 0.5–2% annual management fee
  - Vanguard's first index fund had an 8.5% sales load
  - Pre-decimalization stock spreads were 1/8th ($0.125); a $1 stock implied 12.5% bid-ask bounce
  - Andrew Ang estimated federal taxes reduced 10%+ long-run annualized equity returns to ~7%
  - Reg FD imposed by SEC in 2000, ending selective corporate disclosure
  - Michael Milken built junk bond market partly from a 1943 Hickman study on corporate bond returns 1900–1943; 'maybe 2,000 people read Hickman's book, and 1,999 ignored it'
**Names/tickers:** Ben Carlson, Jason Zweig, Andrew Ang, Robin Wigglesworth, Michael Milken, Walter Braddock Hickman, Drexel, Vanguard, SEC
**Differentiation vs consensus:** The Reg FD point is the most interesting element, but it is not truly non-consensus: academic literature and practitioner commentary (e.g. Charley Ellis, Will Danoff at Fidelity) have discussed Reg FD as a structural shift in active management for years. The historical cost-of-investing framing (loads, spreads, taxes) is well-trodden in passive-investing advocacy. The Milken/Hickman anecdote is colourful but drawn from Robin Wigglesworth's new book, not proprietary research. The article's core observation — that net-of-cost investor outcomes are better today despite potentially lower gross returns — is a standard passive investing argument. Nothing here is genuinely contrarian or ahead of consensus. Differentiation confidence is Low.
**Differentiation confidence:** Low
**Relevance:** Low — This is a retail-oriented, US-centric personal finance/market history essay with no actionable content for UK mid-cap, European equity, bank, semis, or alternative data analysis.
→ Skip unless you want accessible background colour on long-run US market structure evolution for a client-facing piece; no actionable signal for a hedge fund analyst.

## Commodity Context

- ***Rory Johnston*** — Oil Context Weekly (W43) (2026-10-23)
  https://www.commoditycontext.com/p/ocw43w26

**Thesis:** Brent crude has surged to ~$117/bbl as markets begin pricing in a post-US-midterm re-escalation of the Iran War, with physical tightness confirmed across all major inventory hubs and timespreads steepening sharply, suggesting the 'new normal' of elevated geopolitical risk premium is becoming structurally embedded in the barrel.
**Key data:**
  - Brent crude rose ~$7/bbl on the week to ~$117/bbl — higher than all but two daily closes in March/April
  - Brent and Dubai prompt backwardation rose by two-thirds to ~$5/bbl
  - Brent DFLs (dated-to-frontline spreads) nearly doubled to ~$10/bbl
  - WTI prompt backwardation rose ~50c to $2.50/bbl, after WTI November contract briefly spiked to $9/bbl on Tuesday
  - US, Singapore, and ARA Europe inventories all showing major product categories at or below trailing 5-year seasonal lows
  - US Northeast heating oil reserve release announced; US weekly diesel stocks showed a build
  - Gasoline crack spreads fell to lowest level since the start of the Iran War, within a few dollars of seasonal average
  - Speculators were modest net crude buyers over the week-through-Tuesday, driven mainly by short-covering (gross short capitulation)
  - Chinese crude oil imports tentatively recovering to 2025 levels
**Names/tickers:** Brent crude, WTI, Dubai crude, Rory Johnston, Commodity Context, War on the Rocks, Financial Times, Soumaya Keynes, Real Vision
**Differentiation vs consensus:** The mainstream financial media (Yahoo Finance, CNBC, NPR) is covering the post-midterm Iran escalation risk as breaking news, so the geopolitical angle is NOT differentiated. However, Johnston's specific framing adds several non-consensus layers: (1) he labels current conditions a 'new normal' for elevated geopolitical risk premium — implying the market should not expect a reversion to pre-war pricing even if escalation pauses; (2) the WTI November contract briefly spiking to $9/bbl backwardation before settling at $2.50/bbl is a notable physical dislocation not widely surfaced in mainstream coverage; (3) the across-the-board inventory draw reaching 5-year seasonal lows across all three major hubs simultaneously is a supply-side signal beyond what sell-side consensus ($100–107 Q4 EIA/Morgan Stanley/BMI) appears to fully reflect, given Brent spot is already at $117; (4) the Saudi-Houthi war worsening and Chinese import recovery to 2025 levels are cited as concurrent demand support factors not prominently featured in consensus framing. The $117/bbl spot price is already well above the mainstream Q4 consensus of $100–107, suggesting the market has moved faster than sell-side models. Johnston's positioning data (short capitulation driving net length) implies the move is not yet heavily driven by speculative long-building, which is a structural nuance.
**Differentiation confidence:** Med
**Relevance:** Low — The article is a commodity oil market weekly focused on crude prices, spreads, and Middle East geopolitics — none of which fall within the user's stated coverage areas of UK mid-caps, European equities, banks/financials, AI in finance, market structure, alternative data, or semis/compute.
→ Skip unless the fund has direct commodity or energy sector exposure, or needs to assess oil-price pass-through effects on European industrials or consumer names.

## Errors

- Cassandra Unchained (Michael Burry): empty feed — <unknown>:2:1326: not well-formed (invalid token)
- The Bear Cave: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- Kyla's Newsletter: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- Stay-At-Home Macro (SAHM): empty feed — <unknown>:2:1326: not well-formed (invalid token)
- While Stocks Last: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- Capital Wars: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- The Sleepwell Strategy: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- Behind the Balance Sheet: empty feed — <unknown>:2:1326: not well-formed (invalid token)
