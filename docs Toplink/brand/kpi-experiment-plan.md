# TL-M4 — KPI & experiment plan (Toplink Y Viện)

> **Run 1 Phase A · local-only · `external_writes=0`.** Greenfield KPI dictionary. **Counts = 0 only
> after measurement exists; rates/history = `N/A` until minimum sample; never `% from zero`.** Tick
> xanh is not a trust KPI; awareness = `NO_MEASUREMENT` until a method exists. Stable ID
> `TL-KPI-001`. Logical Sheet dataset: `TL_CAMPAIGN_KPI`.

## 1. Baseline rules (master plan §17)

- Follower count records `0` **only after** Page identity + timestamp snapshot (`TL-D12`).
- Awareness is `NO_MEASUREMENT`, not measured zero.
- Count metrics may start at 0; rate/history metrics = `N/A` until denominator sample reached.
- No `% growth from zero`. Tick xanh (`TL-D01`) = `PLATFORM_IDENTITY_SIGNAL`, not a KPI.

## 2. KPI dictionary

| KPI ID | Metric | Definition | Formula | Source | Owner | Cadence | Minimum sample | Launch value |
|---|---|---|---|---|---|---|---|---|
| `TL-KPI-01` | Reach | Unique accounts reached by a post | count (platform) | FB Page Insights | Page owner | Weekly | n/a (count) | `0` (pre-launch) |
| `TL-KPI-02` | Impressions | Total views | count | FB Page Insights | Page owner | Weekly | n/a | `0` |
| `TL-KPI-03` | Video/Reel starts | Reel play starts | count | FB Page Insights | Page owner | Weekly | n/a | `0` |
| `TL-KPI-04` | Save/share | Saves + shares per post | count | FB Page Insights | Page owner | Weekly | ≥ 30 posts for rate | `0` |
| `TL-KPI-05` | Completion/retention | Reel completion rate | completions ÷ starts | FB Page Insights | Page owner | Weekly | ≥ 100 starts | `N/A` |
| `TL-KPI-06` | On-topic questions | Comments/inbox asking about quy trình/phù hợp/an toàn | count (manual tag) | Page inbox/comments | Page owner | Weekly | n/a | `0` |
| `TL-KPI-07` | New followers | Net new Page follows | count | FB Page Insights | Page owner | Weekly | cohort/time window | `0` |
| `TL-KPI-08` | Repeat interaction | Accounts interacting ≥ 2 windows | count (cohort) | FB Page Insights | Page owner | Monthly | cohort defined | `N/A` |
| `TL-KPI-09` | Qualified inquiry | Inbox with genuine service interest | count | Page inbox (manual) | Page owner | Weekly | **only after CTA/offer gate** | `N/A` (gated) |
| `TL-KPI-10` | Risk signals | Misread comments, claim-escalation, approval turnaround | count + hours | Page + review log | Reviewer | Weekly | n/a | `0` |
| `TL-KPI-11` | Ops adherence | Posts on schedule, response SLA, review failures | count/ratio | Production log | Page owner | Weekly | ≥ 1 week | `0` / `N/A` |

Groups map to master plan §17: Distribution (01–03), Utility (04, 06), Attention (05), Relationship
(07–08), Intent (09, gated), Risk (10), Operations (11).

## 3. Metric guardrails

- No `TL-KPI-09` (intent/booking) measurement until the offer/CTA gate PASSes (currently absent).
- Utility signals (save/share, on-topic questions) are **learning signals**, not "trust achieved".
- Every rate metric shows `N/A` until its minimum sample; report the denominator with the rate.
- Health-sensitive posts also log content hash · claim IDs · risk class · DMP check · reviewer/conditions
  · publish status (approval ledger, master plan §16); no null→approved default.

## 4. Experiment loop (Continue / Repair / Stop)

- One variable per experiment (hook, format, or pillar share — see campaign-architecture §4).
- Decision only after minimum sample; never decide on `% from zero`.
- **Continue:** signal ≥ baseline band. **Repair:** flat/ambiguous → adjust one variable.
  **Stop:** risk signal (`TL-KPI-10`) rises or claim-misread emerges → pause + review.

## 5. VERIFY (TL-M4 KPI)

- [x] Each KPI has definition/formula/source/owner/cadence/minimum sample.
- [x] Counts start at 0 only post-measurement; rates/history = `N/A`; no `% from zero`.
- [x] Intent/booking KPI gated behind offer gate; awareness `NO_MEASUREMENT`.
- [x] KPI does not overclaim trust/awareness; tick xanh excluded.
- [x] `external_writes=0`.
