# GM-7 Requirement-to-Evidence Matrix

Revision under test: branch `program/ktd-great-migration`; plan fingerprint
`627ab66d724c2e5017a3ee613433d65ba11048233c42b523bf288ee71e043c30`.

| Requirement | Acceptance condition | Evidence | Verdict |
|---|---|---|---|
| Target runtime | Additive runtime consumes only the five-sheet target model | `ktd_migration.py`; tests | PASS |
| Archived context excluded | Runtime context has no legacy governance loader | runtime-context test | PASS |
| Stable mapping | Nodes resolve uniquely and invalid plans fail closed | validator/resolver tests | PASS |
| Write authority | Automation cannot write human canonical nodes | negative authority test | PASS |
| Canary write | Exact deterministic plan was written to staging and read back | staging readback | PASS |
| Source preservation | Legacy Sheet runtime and source workbook were not changed | Git diff and workbook IDs | PASS |
| Rollback | Original workbook remains the pre-migration reference | baseline/staging pointers | PASS |

The active migration runtime is additive; old implementation files remain historical reference
and are not imported by the new route.

Hard fails: none.

Promotion allowed: YES, to GM-8 verification only.
