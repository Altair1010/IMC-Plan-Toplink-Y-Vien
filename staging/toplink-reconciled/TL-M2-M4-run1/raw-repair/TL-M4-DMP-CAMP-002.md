# RAW — TL-M4 campaign-plan (campaign-architecture + kpi-experiment-plan) · digital-marketing-pro:marketing-strategist

> Native invocation raw capture. LOCAL-ONLY. Verdict: KEEP both (semantic parity; optional expression deltas).

## RAW OUTPUT — campaign-architecture (captured)
TL-M4 trust-led campaign architecture. Relative D-1..D-28 (no absolute dates; start unset; no holiday bound). 1–2 posts/day. Skeleton-only (user shoots media + finalizes caption). Greenfield count=0/rate=N/A. No paid/budget. Stable ID TL-CAMPAIGN-001; dataset TL_CAMPAIGN_KPI.
- W1 (D-1..7) nhận diện & giới hạn TL-P1(+P3 teaser); gate no franchise/legal public wording (TL-D16); CTA follow/save.
- W2 (D-8..14) hiểu cơ thể HEALTH-SENSITIVE TL-P2(+P4); claim inventory + DMP check + per-item professional/human review (TL-D13); CTA save/share; cấm nhân-quả/chẩn đoán/efficacy/hứa kết quả.
- W3 (D-15..21) bằng chứng vận hành TL-P3; operational fact only; consent gate cho chứng chỉ/kết quả/testimonial; CTA follow/save.
- W4 (D-22..28) EVIDENCE-CLEARED SOLUTION (chỉ khi SKU/dịch vụ có dossier PASS + offer gate) HOẶC SAFE FALLBACK (mặc định hoàn chỉnh, không phải A bị lược disclaimer). Hiện: no dossier PASS/offer gate → W4 = SAFE FALLBACK.
- CTA governance: default follow/save/share; commercial CTA cần offer gate chưa tồn tại; founder-led ≤1/5, no consecutive commercial.
- Experiment §4: one variable per test (hook/format/pillar weight); Continue/Repair/Stop; never bind test to health claim; no decision on growth-from-zero.
- VERIFY: 4 tuần trace pillar+audience; W2 per-item gate; W3 operational-only; W4 fallback complete; relative D-1..28; greenfield count=0/rate=N/A no %-from-zero; non-commercial CTA default; skeleton-only; no paid; external_writes=0.

## RAW OUTPUT — kpi-experiment-plan (captured)
TL-M4 KPI & experiment plan. Greenfield dictionary. count=0 only post-measurement; rate/history=N/A tới mẫu tối thiểu; never %-from-zero. Tick xanh ≠ trust KPI; awareness=NO_MEASUREMENT. No paid/budget. Stable ID TL-KPI-001; dataset TL_CAMPAIGN_KPI.
- Baseline rules §1 (follower 0 post-snapshot TL-D12; awareness NO_MEASUREMENT; rate N/A; no %-growth-from-zero; tick xanh = PLATFORM_IDENTITY_SIGNAL).
- KPI dictionary §2: TL-KPI-01..11 (reach, impressions, reel starts, save/share, completion/retention, on-topic questions, new followers, repeat interaction, qualified inquiry [gated post offer gate], risk signals, ops adherence) — each with metric/def/formula/source/owner/cadence/min-sample/launch value. Groups map master plan §17.
- Guardrails §3: no intent KPI (TL-KPI-09) tới offer/CTA gate PASS; utility signals = learning not trust-achieved; rate N/A tới min sample; health-sensitive posts log content hash/claim IDs/risk class/DMP check/reviewer/publish status; no null→approved default.
- Experiment loop §4: one variable; decision only after min sample; Continue/Repair/Stop.
- VERIFY: each KPI defined; count 0 post-measurement/rate N/A/no %-from-zero; intent gated; awareness NO_MEASUREMENT; no overclaim; no paid; external_writes=0.

## RECONCILIATION
- campaign-architecture.md — KEEP. Semantic parity; optional expression deltas (HEALTH-SENSITIVE label into §1 table; header echo of no-paid + count=0/rate=N/A). Canonical passes check (composite 64, auto_reject=false, 0 critical).
- kpi-experiment-plan.md — KEEP. Semantic parity; all 11 KPIs/formulas/min-samples/launch values preserved; optional header clarifications only. Canonical passes check (composite 68, auto_reject=false, 0 critical).
- Hard constraints confirmed: relative D-1..D-28; greenfield counts=0/rates=N/A (numbers like "≥30 posts","≥100 starts","≤1/5" are min-sample/frequency rules from source, not result percentages); no paid; W2 health human gate; W4 = SAFE FALLBACK; external_writes=0. No invented fact/metric. Sheet target = BLOCKED_TARGET_INPUT.
