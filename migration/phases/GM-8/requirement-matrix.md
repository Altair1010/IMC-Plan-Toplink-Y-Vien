# GM-8 Requirement-to-Evidence Matrix

Revision under test: plan fingerprint `627ab66d724c2e5017a3ee613433d65ba11048233c42b523bf288ee71e043c30`.

| Requirement | Acceptance condition | Evidence | Verdict |
|---|---|---|---|
| Individual acceptance rows | Every pre-cutover blocking row has evidence and passes | `migration/verification/acceptance-matrix.md` | PASS |
| Unknown integrity | Unknown facts remain explicit and are not counted as current facts | truth bundle; target readback | PASS |
| Target behavior | Target plan validates, resolves, and enforces authority | 9/9 KTD tests | PASS |
| Live workbook | Five-sheet target values/topology read back from staging | staging readback | PASS |
| Legacy preservation | Original workbook still has 22 tabs; legacy code has no diff | live metadata; Git diff | PASS |
| Regression disclosure | Four time-expired legacy approval tests are not hidden | defect register; 68/72 repository tests PASS | PASS_WITH_NOTE |
| Cutover readiness | Exact target revision and rollback pointer exist | fingerprint; source/staging IDs | PASS |

Hard fails: none. The historical approval-expiry errors are non-blocking because the KTD route
does not import that runtime and repairing them would reinstate retired governance.

Promotion allowed: NO. State must move to `PROMOTION_PENDING` because GM-9 authorization is NO.
