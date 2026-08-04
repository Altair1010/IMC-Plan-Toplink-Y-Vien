# TOPLINK Run 2 Phase B — Codex independent blind audit

## Audit control

- Runtime: Codex CLI (`root`)
- Run: `TOPLINK_RUN2_FRESH_AUDIT_FINALIZE`
- Audit mode: independent canonical/Run 1 inspection before any read of `docs Toplink/staging/run2/claude/**`, `handoff-claude-to-codex.md`, or `handoff-envelope.json`
- Scope: the 14 `generated_outputs[]` in `docs Toplink/staging/run1/run1-manifest.json`
- External writes: `0`
- Human approvals granted by this audit: `0`

## Entry-lock evidence

Independent disk read-back immediately before N2:

| Invariant | Actual | Result |
|---|---|---|
| Run 1 manifest SHA-256 | `99227153de577887966ae09124fdabcb2b3bf8ff23d838503531be507c2f4d2d` | MATCH |
| Profile SHA-256 | `a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349` | MATCH |
| Five-member source aggregate | `3ba91761612ca482471dc1c071bd7e9d82e5708a3bb13ceb630fed476541fe76` | MATCH; 5/5 members |
| Generated outputs | 14/14 | BYTE_MATCH |
| DMP package / active brand | `3.15.1` / `toplink-y-vien` | MATCH |
| Run 1 status | `RUN1_PASS · LOCAL_VERIFIED · PHASE_B_RECONCILED · NOT_MILESTONE_COMPLETE` | MATCH |
| Competing writer at N0 | 0 | PASS |

## Eight-axis blind audit

| Axis | Evidence and result |
|---|---|
| Evidence/entity | Brand profile and positioning retain public franchise/legal `PENDING_DOCUMENT`; product experience remains `UNVERIFIED`; no public franchise claim found. One decision-reference gap is recorded as `TL-R2-C04`. |
| Audience/positioning | Audience hypotheses remain hypotheses and preserve Hanoi local / national awareness-only boundaries. One sentence can imply facility/professional avoidance and is `TL-R2-C02`. |
| Pillars/Facebook | Five pillars total 28 slots and Facebook Page/Reels roles remain primary/supporting. Dataset collision, founder-window ambiguity, and namespace drift are `TL-R2-C07..C09`. |
| Campaign/KPI | Relative D-1..D-28 architecture, safe W4 fallback, counts-from-zero / rate=`N/A`, and non-commercial CTA gate are intact. Namespace mapping remains unresolved under `TL-R2-C09`. |
| Calendar/production | 28 unique calendar rows, 12 Reels, 28 production rows, placeholder-only assets, consent gates, and capacity bounds are intact. Claim orphan, Reels count, and approval-ledger count are `TL-R2-C01`, `C05`, `C06`. |
| Claim safety | Bounded support language, professional escalation, customer-experience-only product framing, and follow/save/share CTA pass. `TL-R2-C01..C03` require repair or fail-closed handling. |
| Privacy/approvals | All current items remain `DRAFT` or `NEEDS_HUMAN_REVIEW`; human gate is the only route to `HUMAN_APPROVED`; publish state remains `NOT_PUBLISHED`; founder/BTS/UGC consent gates are preserved; no null→approved default observed. |
| Integrity/isolation | Entry hashes pass; no Thảo Tây/thao tay match occurs in the 14 outputs; no secret/credential target is introduced. Stable-ID/reference issues are limited to `C01`, `C04`, `C07`, `C09`. |

## Mandatory reference-integrity scan

| Reference class | Scope | Result |
|---|---|---|
| Claim IDs | `month-calendar.md` §3 + `production-briefs.md` §1 → `month-calendar.md` §1 | FAIL: `CL-P2` absent; 6 calendar + 6 production occurrences. All other 10 distinct used claim IDs resolve. |
| Asset IDs | production table and batch usage → `asset-and-batch-plan.md` §2 | PASS: 0 unresolved asset IDs. |
| Decision IDs | cited `TL-D*` → canonical decision surface | FAIL: `TL-D16` cited at `month-calendar.md:34`; master register ends at `TL-D15`. The decision text exists only in current state/task records and needs a canonical status pointer. |
| Disclaimer anchors | every `§3.3` reference → required canonical host | FAIL-CLOSED: the wording exists at `docs Toplink/02_communication_safety.md:35-39`, but the TL-M1 canonical deliverable `docs Toplink/system/health-compliance.md` is absent. Textual resolution therefore does not satisfy the canonical-host contract. |

## Independent finding ledger

| Codex ID | Severity | Class | Evidence | Route | Status |
|---|---|---|---|---|---|
| `TL-R2-C01` | major | reference integrity | `CL-P2` occurs in `month-calendar.md:65,67,68,70,90,94` and `production-briefs.md:31,33,34,36,46,50`; register is `month-calendar.md:23-32` and omits it. | `DIRECT_REPAIR` — replace with already co-tagged `CL-M2`; no new meaning | OPEN |
| `TL-R2-C02` | major | claim safety | `audience-hypotheses.md:63` says the national-awareness audience seeks proactive care “mà không cần đến cơ sở”, which can imply avoiding facility/professional care; conflicts with professional-escalation controls. | `DIRECT_REPAIR` — narrow to sourced learning/suitable-at-home-habit framing; preserve awareness-only boundary | OPEN |
| `TL-R2-C03` | major | health canonical host | `docs Toplink/system/health-compliance.md` is absent while health artifacts depend on disclaimer §3.3. Existing wording is in `02_communication_safety.md`, whose canonical TL-M1 host status is insufficient for final anchoring. | `HUMAN_GATE` — interim pending-host annotations only; no health wording creation | OPEN |
| `TL-R2-C04` | minor | decision reference | `month-calendar.md:34` cites `TL-D16`; master register `TOPLINK_PAGE_MASTER_PLAN.md:45-59` stops at D15; current D16-D20 facts are in `STATE.md:116-135` / `task.md`. | `DIRECT_REPAIR` — add a canonical milestone/status pointer without editing frozen master | OPEN |
| `TL-R2-C05` | minor | count integrity | Calendar has 5 health Reels: D08,D11,D14,D23,D27; `reels-briefs.md:131` says 6. | `DIRECT_REPAIR` — correct VERIFY count to `5 (4×TL-P2 + 1×TL-P4)` | OPEN |
| `TL-R2-C06` | minor | approval-ledger count | `workflow-approval-measurement.md:68-69` describes 10 health + 6 founder/product-adjacent, but D14 and D26 overlap health/product; distinct gated items are 14. | `DIRECT_REPAIR` — state 14 distinct, note overlap, bind D26 product-adjacent with inherited health gate | OPEN |
| `TL-R2-C07` | minor | Sheet mapping integrity | `content-pillars.md:3,56` and `facebook-page-strategy.md:5` both claim logical dataset `TL_PAGE_STRATEGY`; operational registry has distinct `TL_CONTENT_PILLARS` and `TL_FACEBOOK_STRATEGY`. | `DIRECT_REPAIR` — map pillars to `TL_CONTENT_PILLARS`; keep Facebook strategy mapping until the Run 2 mapping ledger resolves the registry key | OPEN |
| `TL-R2-C08` | minor | founder guardrail | Founder items D24 and D28 coexist within the sliding D24-D28 window while master plan says no more than 1 in every 5 planned items; global 4/28 remains within the approximate mix. | `HUMAN_GATE` unless canonical owner confirms a global/non-overlapping-batch interpretation; do not silently reassign content | OPEN |
| `TL-R2-C09` | minor | stable-ID namespace | Emitted IDs `TL-A0x`, `TL-P1..P5`, `TL-KPI-0x`, `CL-*` differ from milestones §2.6 `TL-AUD/TL-PIL/TL-KPI/TL-CLAIM-{NNN}`. | `DIRECT_REPAIR` — non-breaking crosswalk; do not rename emitted immutable IDs | OPEN |

## Advisories retained for hardening

- Health Reels at or below 20 seconds must hold the §3.3 disclaimer through the end, not merely state a generic five-second minimum.
- Approval ledger validation must explicitly reject `HUMAN_APPROVED` when `content_hash` is null or empty.

## Blind-audit verdict

`N2_COMPLETE · NEEDS_TARGETED_REPAIR · TEMPORAL_CUT_NOT_YET_FIRED`

No finding above is evidence of human approval, publication, Sheet synchronization, milestone completion, or authorization to create health-sensitive canonical wording.
