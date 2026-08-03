# TL-M3 — Content pillars (Toplink Y Viện)

> **Run 1 Phase A · local-only · `external_writes=0`.** DMP `social-strategy` + `content-engine`
> (v3.15.1) converged candidate territories `TL-PC1`–`TL-PC5` (master plan §10) into **5 pillars
> totaling 100%**. Weights are launch hypotheses, re-weighted after pilot signal (`TL-M4`). Stable ID
> `TL-PILLARS-001`. Logical Sheet dataset: `TL_PAGE_STRATEGY`.

## 1. Pillar set (total = 100%)

| Pillar | ID | Weight | Audience job | Right-to-document / evidence | Format & funnel | Health/reputation risk | Weight rationale |
|---|---|---:|---|---|---|---|---|
| **Toplink là ai — phạm vi & giới hạn** | `TL-P1` (←PC1) | 20% | `TL-A01/A02` hiểu Toplink là gì, không phải gì | Positioning + space + brand descriptor `TOPLINK_CONFIRMED`; franchise/legal **gated** | FB post + Reel intro; TOFU awareness/trust | Medium — tick xanh ≠ proof; no franchise/legal wording | Foundational; must precede claims — moderate share |
| **Hiểu & lắng nghe tín hiệu cơ thể** | `TL-P2` (←PC2) | 20% | `TL-A01/A02a/A02b` body literacy, an tâm | Support language `TOPLINK_CONFIRMED` (taxonomy §1); efficacy `UNVERIFIED` | Educational carousel/Reel; TOFU→MOFU | **High** — cấm causal/diagnostic; disclaimer + professional review per item | Core value but capped by health gate — not the largest |
| **Bằng chứng vận hành: không gian, quy trình, con người** | `TL-P3` (←PC3) | 30% | `TL-A01/A03` tin vào sự chỉn chu, minh bạch | 4-floor space + 8-step process `TOPLINK_CONFIRMED`; **strongest asset** | Photo/video tour, Reel behind-the-scenes; MOFU trust | Low — fact vận hành; qualification/outcome/testimonial gated | Strongest verifiable asset, lowest risk → largest share |
| **Lý – Dược – Dưỡng dễ hiểu** | `TL-P4` (←PC4) | 15% | `TL-A02/A04` hiểu hệ giải pháp | Naming `TOPLINK_CONFIRMED`; per-SKU efficacy `UNVERIFIED` (dossier gate TL-GAP-004) | Explainer post/Reel; MOFU | Medium-High — cấm efficacy claim tới khi có dossier | Held lower until product dossiers PASS |
| **Hành trình Toplink, founder & cộng đồng** | `TL-P5` (←PC5) | 15% | `TL-A03/A04` kết nối giá trị, cộng đồng | Founder allowed-use gated; consent required | Story/Reel; TOFU→retention | Medium — founder cap ≤1/5 item; no mechanism/diagnosis | Capped by founder guardrail (≤20%) |

**Total: 20 + 20 + 30 + 15 + 15 = 100%.**

## 2. Funnel coverage

- **TOFU (awareness):** `TL-P1`, `TL-P2`, `TL-P5` — reach, save/share, follow.
- **MOFU (consideration/trust):** `TL-P3`, `TL-P4` — question-asking, repeat interaction.
- **BOFU (conversion):** none by default — commercial CTA disabled until offer gate (`TL-M4`/§11).

## 3. Per-pillar guardrails

- `TL-P2` / `TL-P4`: every item carries the mandatory disclaimer + individual-variation caveat and
  routes to professional/human review before publish (`TL-D13`; item-level, not batch).
- `TL-P3`: operational fact only; no staff qualification claim, no outcome, no testimonial without
  documented consent.
- `TL-P5`: founder-led ≤ 1 per 5 planned items; no two consecutive founder-led commercial CTAs.
- `TL-P1`: no public franchise/legal wording (`TL-D16`); tick xanh = `PLATFORM_IDENTITY_SIGNAL` only.

## 4. VERIFY (TL-M3 pillars)

- [x] 5 pillars, weights total exactly 100%.
- [x] Each pillar has audience job + evidence + format/funnel + risk + weight rationale.
- [x] Health-sensitive pillars item-gated; founder guardrail itemized.
- [x] No BOFU/commercial default; no invented efficacy.
- [x] `external_writes=0`.
