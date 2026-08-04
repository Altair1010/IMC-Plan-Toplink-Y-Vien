# RAW — TL-M5 content-engine (production-briefs + workflow-approval-measurement) · digital-marketing-pro:content-creator

> Native invocation raw capture. LOCAL-ONLY. Verdict: KEEP both (zero delta). No item APPROVED.

## RAW OUTPUT — production-briefs (captured)
Stable ID TL-M5-PRODBRIEF-001. Run 1 Phase A, local-only, external_writes=0, no item APPROVED/publish-ready.
- §0 legend: claim source register, R1/R2/R3 review routes, KPI dict, approval states (DRAFT/NEEDS_HUMAN_REVIEW only), CTA = follow/save/share only.
- §1 master table 28 items D01–D28: each row hook · shot · on-screen text · CTA · claim ID · source · review · approval · KPI. CTA column only "Theo dõi/Lưu/Chia sẻ".
- §2 caption skeletons, 6 pillar groups. Health groups (TL-P2 D08/D10/D11/D13/D23/D27; TL-P4 D09/D12/D26) + product-adjacent (CL-CX1 D14/D26) carry Disclaimer §3.3 verbatim (mandatory, end of post).
- §3 measurement mapping per-item → KPI; Reels rate N/A tới ≥100 starts; health items add KPI-10; KPI-09 gated.
- §4 VERIFY 6/6.
Safety: support-language (§3.1 preferred) throughout; zero forbidden §3.2 term; boundaries "không thay thế y khoa/không cam kết chữa khỏi" + nhóm thận trọng; product customer-experience only (D14/D26, TL-GAP-010 fail-closed, 11_Product_Yvien UNVERIFIED); founder allowed-use gated + consent.

## RAW OUTPUT — workflow-approval-measurement (captured)
Stable ID TL-M5-WORKFLOW-001. external_writes=0, no self-APPROVED/publish-ready.
- §1 workflow fail-closed: Ý tưởng → Draft → DMP check → R1 → [video]R2 → [health/founder/product]R3 → HUMAN APPROVE (chỉ người sở hữu, gate duy nhất) → Publish + log. Reviewer max verdict = REVIEWED/NEEDS_HUMAN_REVIEW/PASS/FAIL; commercial CTA locked.
- §2 approval states: DRAFT/REVIEWED/NEEDS_HUMAN_REVIEW/PASS/FAIL/HUMAN_APPROVED/PUBLISHED; only human owner sets HUMAN_APPROVED; none at HUMAN_APPROVED/PUBLISHED.
- §3 approval ledger: SHA-256 content hash per revision; material edit resets → DRAFT/NEEDS_HUMAN_REVIEW; 14-col schema (TL_WORKFLOW_APPROVAL). 28 rows revision=1, human_gate=PENDING, publish_state=NOT_PUBLISHED; 10 health + 6 founder/product = NEEDS_HUMAN_REVIEW.
- §4 health/legal/privacy: disclaimer §3.3 mandatory 10 health items; no franchise/legal wording; testimonial/UGC only consent_state=OBTAINED; product UNVERIFIED; founder gated; bounded write only with signed SheetTargetApproval (out of Phase A scope).
- §5 DMP check gate 8 dimensions (forbidden terms, mandatory disclaimer, no before/after/testimonial, CTA restriction, franchise/legal, product/efficacy, self-APPROVED) all PASS (deterministic scan); eval-runner quick-mode SKIPPED with documented reason.
- §6 measurement: no %-from-zero; rate N/A till min sample; 1 variable/experiment; Stop on KPI-10 rise; KPI-09 gated.
- §7 VERIFY 6/6.

## RECONCILIATION
- production-briefs.md → KEEP, zero delta. All 28 items full fields; CTA follow/save/share only; 10 health + 6 founder/product = NEEDS_HUMAN_REVIEW; §3.3 disclaimer on all health caption groups; support-language only; no forbidden §3.2 term; no invented N% (rates N/A); no superlative brand claim. Canonical passes check (composite 80, auto_reject=false, 0 critical).
- workflow-approval-measurement.md → KEEP, zero delta. Fail-closed single human gate; ledger content-hash + material-edit reset; consent gate; product UNVERIFIED; measurement no %-from-zero; no item HUMAN_APPROVED/PUBLISHED. Canonical passes check (composite 80, auto_reject=false, 0 critical).
Note: hallucination-detector "exclusive_claim/only" flags = Vietnamese governance phrases ("GATE DUY NHẤT", "chỉ human owner", "chỉ follow/save/share") = fail-closed authority statements, NOT public brand superlatives → documented false-positive; 0 critical.
Confirmation: support-language + disclaimer; no medical/franchise/efficacy claim; CTA follow/save/share; no APPROVED; external_writes=0.
