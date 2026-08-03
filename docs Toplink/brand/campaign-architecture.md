# TL-M4 — Trust-led campaign architecture (Toplink Y Viện)

> **Run 1 Phase A · local-only · `external_writes=0`.** DMP `campaign-plan` + `social-strategy` +
> `content-engine` (v3.15.1). **Relative D-1 … D-28** (no absolute dates; `TOPLINK_CONTENT_START_DATE`
> unbound). Cadence 1–2 posts/day. **Skeleton/framework only** — user shoots/edits media + finalizes
> caption; this is not finished creative. Full 28-day calendar + briefs = `TL-M5` (not started).
> Stable ID `TL-CAMPAIGN-001`. Logical Sheet dataset: `TL_CAMPAIGN_KPI`.

## 1. Four-week arc (each week traces to pillar + audience job)

| Week | Days | Role | Pillars | Audience job | Hard gate | Default CTA class |
|---|---|---|---|---|---|---|
| **W1** | D-1…D-7 | Toplink là gì / không phải gì; identity & giới hạn | `TL-P1` (+`TL-P3` teaser) | `TL-A01/A02` hiểu định vị | Page identity + **no public franchise/legal wording** (TL-D16) | Follow / save |
| **W2** | D-8…D-14 | Tín hiệu đời thường, thói quen, body literacy | `TL-P2` (+`TL-P4`) | `TL-A01/A02a/A02b` an tâm, hiểu cơ thể | Claim inventory + DMP `check` + **professional review per item** | Save / share |
| **W3** | D-15…D-21 | Không gian, quy trình, vệ sinh, đội ngũ | `TL-P3` | `TL-A01/A03` tin sự chỉn chu | **Operational proof only**; qualification/outcome/testimonial consent gate | Follow / save |
| **W4** | D-22…D-28 | `EVIDENCE-CLEARED SOLUTION` **hoặc** `SAFE FALLBACK` | conditional | `TL-A01/A03` next-step phù hợp | Per-SKU/service dossier PASS → cleared; else fallback | Non-commercial (see §3) |

## 2. Weekly skeleton (structure · hook · angle · claim-ID · CTA class — no finished copy)

### W1 — Identity & limits (`TL-P1`)
- **Angle:** ai là Toplink, phạm vi chăm sóc chủ động, và giới hạn rõ ràng (không bệnh viện, không chữa khỏi).
- **Skeleton per item:** hook (câu hỏi đời thường) → 1 ý định vị → 1 ý giới hạn → CTA follow/save.
- **Claim IDs allowed:** M1, M3 (positioning §4). **Forbidden:** franchise/legal/efficacy.
- **Slots:** D-1 intro Page · D-3 "Toplink không phải gì" · D-5 không gian teaser (`TL-P3`) · D-7 giá trị Thân–Tâm–Trí.

### W2 — Body literacy (`TL-P2`, `TL-P4`) — HEALTH-SENSITIVE
- **Angle:** lắng nghe tín hiệu cơ thể; thói quen nhỏ; hệ Lý–Dược–Dưỡng "đúng người/cách/thời điểm".
- **Skeleton per item:** hook (tín hiệu quen thuộc) → giải thích **không chẩn đoán** → support-level framing → **disclaimer bắt buộc** + individual-variation caveat → CTA save.
- **Every item:** claim-ID tagged, DMP `check`, **professional/human review before publish** (`TL-D13`, item-level).
- **Forbidden:** causal/diagnostic wording, efficacy claim, outcome, "chữa khỏi".

### W3 — Operational proof (`TL-P3`)
- **Angle:** không gian 4 tầng, quy trình 8 bước, vệ sinh, con người — minh bạch, real imagery.
- **Skeleton per item:** hook (chi tiết không gian/quy trình) → fact vận hành → CTA follow/save.
- **Allowed:** operational fact only. **Gated:** staff qualification, outcome, testimonial (consent).

### W4 — Conditional close
- **Branch A — `EVIDENCE-CLEARED SOLUTION`:** only if a specific SKU/service dossier PASSes (label,
  hồ sơ, phạm vi pháp lý, IFU, chống chỉ định) **and** an offer gate exists. Then bounded, claim-ID'd,
  disclaimer'd content — still **non-commercial CTA** unless the offer gate (does not yet exist) opens.
- **Branch B — `SAFE FALLBACK` (default, complete):** brand/process/community content recap
  (`TL-P1`/`TL-P3`/`TL-P5`), body-literacy reinforcement, invite to follow/save. This fallback is a
  **complete week**, not a disclaimer-bypassed version of Branch A. No calendar/disclaimer trick may
  substitute a missing dossier.
- **Current state:** no dossier PASS, no offer gate → **W4 = Branch B (SAFE FALLBACK)** by default.

## 3. CTA governance

- Default across W1–W4: **theo dõi Page · lưu · chia sẻ.**
- Commercial CTA (booking/tư vấn/mua) requires an offer gate that **does not yet exist**
  (exact offer, eligibility, location, availability, contact ownership, SLA, privacy, compliance).
- Founder-led ≤ 1 per 5 items; no two consecutive founder-led commercial CTAs (none commercial anyway).

## 4. Experiment design (one variable at a time)

| Experiment | Variable | Continue / Repair / Stop signal |
|---|---|---|
| Hook style | câu hỏi vs chi tiết không gian | Continue if save/share ≥ baseline sau đủ mẫu; Repair if flat; Stop if misread comments ↑ |
| Format | static vs Reel | Continue on completion/retention; else Repair format |
| Pillar mix | educational vs operational-proof share | Rebalance weights only after minimum sample |

Change **one** variable per test; never bind an experiment to a health claim. Minimum sample defined
in the KPI plan; no decision on `% from zero`.

## 5. VERIFY (TL-M4 campaign)

- [x] 4 weeks each trace to pillar + audience job.
- [x] W2 claim/professional gate item-level; W3 operational-only; W4 fallback complete (not bypassed).
- [x] Relative D-1…D-28; no absolute date; `TOPLINK_CONTENT_START_DATE` unbound.
- [x] Non-commercial CTA default; commercial gated behind non-existent offer gate.
- [x] Skeleton-only (no finished creative); media/caption owned by user.
- [x] `external_writes=0`; W4 currently = SAFE FALLBACK.
