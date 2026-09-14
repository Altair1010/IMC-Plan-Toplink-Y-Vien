# GM-1 Requirement-to-Evidence Matrix

- Revision under test: `e6f1e97` plus current GM-1 artifacts
- Input revisions: live owner instruction SHA-256 `53bd6b321bbf4f0970107c8c17dddfef1c182abb9dc8c31514e73140ed501068`; package v1.0

| REQ_ID | Requirement | Acceptance condition | Required evidence | Observed evidence | Verdict | Notes |
|---|---|---|---|---|---|---|
| GM1-01 | Current identity | KTD and legacy lineage are distinct and sourced | E1 | `current-truth/CURRENT_KTD_TRUTH.md`; `fact-provenance.csv` | PASS | No legacy continuity inference. |
| GM1-02 | Current phase | Dry Run is explicit and authoritative | E1 | KTD-F-003 | PASS | Owner instruction and package agree. |
| GM1-03 | Communication boundary | Removed and prohibited content categories are explicit | E1 | Current truth boundary set | PASS | Legacy gates are history only. |
| GM1-04 | Page and CTA boundary | Role, non-role, and conditional CTA classes are explicit | E1 | Current truth table | PASS_WITH_NOTE | Actual Page ID and operational booking readiness remain unknown. |
| GM1-05 | Current material facts | Every asserted fact has provenance | E2 | `fact-provenance.csv` provenance scan | PASS | Assertions are limited to supported boundaries. |
| GM1-06 | Unknowns explicit | Unsupported current facts are not inferred | E1 | `unknown-and-conflict-register.csv` | PASS | Eight current-truth gaps remain explicit. |
| GM1-07 | Conflicts reconciled | Source conflicts follow precedence and preserve lineage | E1 | KTD-C-001 and KTD-C-002 | PASS | Target is isolated; no legacy deletion. |
| GM1-08 | Bundle coherent | No confirmed fact contradicts another confirmed fact | E2 | consistency validation in GM-1 artifacts | PASS | Unknowns are not treated as PASS. |

- HARD_FAILS: none for GM-1 extraction
- OPEN_UNKNOWNS: KTD-U-001 through KTD-U-008; downstream blocking impact will be evaluated per claim
- CONVERGENCE: PROGRESSING
- NEXT_SIGNAL: classify every active legacy semantic object and runtime consumer
- PROMOTION_ALLOWED: YES
