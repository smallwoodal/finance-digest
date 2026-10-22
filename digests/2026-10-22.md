# 📚 Your reading list — 1 new post (last 24h)

Generated: 2026-10-22T12:39:18Z

## SemiAnalysis (Substack)

- ***Bryan Shan*** — The Huawei-DeepSeek Symbiosis (2026-10-21)
  https://newsletter.semianalysis.com/p/huawei-deepseek

**Thesis:** Huawei and DeepSeek have formed a mutually dependent hardware-software symbiosis — Huawei supplies Ascend silicon and its CANN stack, DeepSeek supplies frontier model workloads and kernel engineering — and SemiAnalysis argues this partnership is sufficiently mature that DeepSeek will likely migrate primarily to Huawei's stack by 2027-2028, ahead of most mainstream timelines.
**Key data:**
  - Ascend 950PR_9579 test SKU: 28 cube cores, 128 GiB HBM, ~203W idle power
  - Huawei bins both compute AND memory into multiple SKUs (pairing weaker memory with weaker compute), unlike Nvidia which bins only compute
  - Huawei's stock torch.matmul kernels hit 99.7% of theoretical FLOPs ceiling across 1,055 BF16 GEMM shapes — matching DeepSeek's own 99%+ from DeepGEMM
  - On sub-ridge compute-bound shapes, 950PR median achieved/attainable fraction: 41.5% vs H100's 46.8%
  - Nvidia H100 results were power-limited: median ~690-698W vs 700W TDP, SM clocks 1335-1470 MHz vs 1830 MHz max
  - Huawei 950PR ran at 599-600W, 1500-1550 MHz vs 1650 MHz reference
  - 950PR absolute performance sits between A100 and MI300X
  - 950PR HBM bandwidth surpasses H100 at small message sizes; nearly matches H100 utilization at large message sizes
  - DeepSeek released Ascend support for TileLang, DeepGEMM, DeepEP, TileKernels, FlashMLA, and DeepSelect on September 30 (before China's national day holidays)
  - Each 950PR SKU contains variable Linx816 AArch64 AICPUs (same cores as Kirin 9000S/9010 middle cores); test SKU had 7 configured, 6 visible, 5 executing
  - SemiAnalysis projects DeepSeek will primarily use Huawei's stack by 2027-2028
**Names/tickers:** Huawei, DeepSeek, Nvidia, AMD, Ascend 950PR, Ascend 950DT, Ascend 910B, H100, MI300X, A100, TileLang, DeepGEMM, DeepEP, TileKernels, FlashMLA, DeepSelect, CANN, vLLM-ascend, Linx816, Kirin 9000S
**Differentiation vs consensus:** Mainstream coverage (Bloomberg, The Information, Reuters) frames the DeepSeek-Huawei relationship primarily as a procurement story (160,000-chip order) and a high-level co-design narrative. The consensus view is that Huawei's software ecosystem (CANN) remains a key bottleneck and that training on Ascend at scale is unproven. This SemiAnalysis piece is differentiated in several specific ways: (1) It provides the first publicly available microbenchmark data directly from 950PR hardware, placing it concretely between A100 and MI300X on absolute compute — a more precise calibration than most analyst commentary which vaguely compares it to H100. (2) It reveals Huawei's binning strategy (co-binning compute AND memory into multi-SKU tiers) which has not been widely reported and has implications for yield economics and supply forecasting. (3) It demonstrates empirically that Huawei's own stock CANN kernels already reach 99.7% FLOPs utilization — directly countering the consensus narrative that software maturity is the primary Ascend weakness. (4) The framing of the relationship as a mutual dependency (DeepSeek needs compute it can't buy; Huawei needs a frontier workload to validate its chip) is more structurally precise than the customer-vendor framing in mainstream press. (5) The 2027 migration timeline for DeepSeek moving primarily to Huawei's stack is more aggressive than consensus, which still treats Nvidia-trained models as the near-term baseline.
**Differentiation confidence:** High
**Relevance:** High — Directly relevant to the user's stated interest in semis/compute economics and AI applications in finance — this piece provides proprietary benchmark data and architectural analysis with direct implications for the Nvidia-vs-China-domestic compute thesis that is a live question for any semis-focused hedge fund analyst.
→ Worth reading in full if you have a position or view on Nvidia's China exposure, the trajectory of domestic Chinese AI compute, or want primary benchmark data rather than press-release comparisons; the kernel utilization data and binning strategy details are not available elsewhere in mainstream coverage.

## Errors

- Cassandra Unchained (Michael Burry): empty feed — <unknown>:2:1326: not well-formed (invalid token)
- The Bear Cave: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- Kyla's Newsletter: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- Stay-At-Home Macro (SAHM): empty feed — <unknown>:2:1326: not well-formed (invalid token)
- While Stocks Last: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- Capital Wars: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- The Sleepwell Strategy: empty feed — <unknown>:2:1326: not well-formed (invalid token)
- Behind the Balance Sheet: empty feed — <unknown>:2:1326: not well-formed (invalid token)
