# GM-9 Requirement-to-Evidence Matrix

| Requirement | Acceptance condition | Evidence | Verdict |
|---|---|---|---|
| GM-8 readiness | All pre-cutover blocking rows pass | acceptance matrix | PASS |
| Exact target | Fingerprint and staging ID are locked | cutover plan | PASS |
| Rollback | Legacy source workbook is present and unchanged | live 22-tab metadata readback | PASS |
| Owner authorization | Exact cutover token is YES | invocation sets token to NO | BLOCKED |
| Canonical promotion | Verified KTD target is the current pointer | post-cutover evidence | NOT_TESTED |
| Post-cutover readback | Canonical, runtime, and legacy checks pass | post-cutover evidence | NOT_TESTED |
| Public publication | No public Page post occurs | final cutover record | NOT_TESTED |

Promotion allowed: NO. The program must remain `PROMOTION_PENDING`.
