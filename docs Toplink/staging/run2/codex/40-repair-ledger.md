# TOPLINK Run 2 — targeted repair ledger

All repairs are in place, evidence-grounded, and limited to bytes named by the merged finding. No DMP reauthoring was required; no external write occurred.

| Merged ID | Repair | Digest transition / proof | Result |
|---|---|---|---|
| `TL-R2-M01` | Removed the undefined, co-tagged `CL-P2` token from six calendar and six production rows; retained existing `CL-M2`. | calendar `0d2d2d16…` → `c270bd4f…`; production `42cb8e7d…` → `2496aa3c…`; `CL-P2` occurrences in both files = 0 | `RESOLVED_ZERO_ORPHAN` |
| `TL-R2-M02` | Added `DISCLAIMER_HOST_PENDING (TL-M1: docs Toplink/system/health-compliance.md)` annotations only; did not create or revise health wording. | reels `51b18d91…` → `eaab023b…`; production `2496aa3c…` → `f36824b6…`; workflow `651dff61…` → `bdad718f…` | `INTERIM_ANNOTATED · FINAL_WORDING_PENDING_HUMAN` |
| `TL-R2-M03` | Narrowed the national-awareness emotional JTBD from facility-avoidance wording to learning/suitable-at-home-habit wording. | audience `4a32da6b…` → `25d3795c…`; one line replaced | `RESOLVED_SAFE_NARROWING` |
| `TL-R2-M04` | Added a milestone/status pointer resolving `TL-D16..D20` without editing frozen master plan. | milestone current SHA-256 `68258db164321a57c2ec57baa1fd5166fef077bc3e2905090b2317b80bd11143`; six inserted lines, no deletion | `RESOLVED_CANONICAL_POINTER` |
| `TL-R2-M05` | Corrected health-Reels VERIFY from 6 to 5 and listed D08,D11,D14,D23,D27. | reels `eaab023b…` → `51983b6f…`; one line replaced | `RESOLVED_COUNT_5` |
| `TL-R2-M06` | Replaced the additive 10+6 description with 14 distinct gated items; recorded D14/D26 overlap and D26 product-adjacent binding with inherited health gate. | workflow `bdad718f…` → `754af6cf…`; bounded ledger paragraph/binding only | `RESOLVED_14_DISTINCT_D26_BOUND` |
| `TL-R2-M07` | Changed the pillar logical dataset from the colliding `TL_PAGE_STRATEGY` to registry key `TL_CONTENT_PILLARS`. | pillars `b0790e2d…` → `eeed4593…`; two token replacements | `RESOLVED_DATASET_COLLISION` |
| `TL-R2-M08` | Recorded global founder ratio 4/28 (14.3%) and retained the D24–D28 sliding-window decision as a human gate; no item was reassigned. | pillars `eeed4593…` → `773a43d7…`; one bounded note added | `GLOBAL_RATIO_PASS · SLIDING_WINDOW_HUMAN_GATE` |
| `TL-R2-M09` | Added a family-level crosswalk for emitted Run 1 aliases; allocated no new ID and performed no breaking rename. | runtime `e38846fb…` → `5c6325aa…`; one subsection added | `RESOLVED_NON_BREAKING_CROSSWALK` |
| `TL-R2-M10` | Recipient ledger retains F01..F08 despite the released Claude post-blind file omitting F07/F08 from its six-item reconciliation count. Released Claude artifacts were not rewritten. | `30-merged-issue-ledger.md` records the contradiction | `RESOLVED_BY_MERGE` |

## Final canonical-output digest set after N6

Changed: 7/14 (`TL-RUNTIME-COMPAT-001`, `TL-AUDIENCE-001`, `TL-PILLARS-001`, `TL-M5-CALENDAR-001`, `TL-M5-REELS-001`, `TL-M5-PRODBRIEF-001`, `TL-M5-WORKFLOW-001`).

Unchanged: 7/14; each remains byte-identical to its Run 1 digest. All 14 current hashes match `run2-manifest.json`.
