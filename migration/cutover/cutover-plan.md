# GM-9 Cutover Plan

Status: `DONE`

## Locked inputs

- Verified runtime commit: `d95397b`
- Verified workbook plan fingerprint: `627ab66d724c2e5017a3ee613433d65ba11048233c42b523bf288ee71e043c30`
- Verified staging workbook: `1v2bk-MOrYyDybgfAh1sYnOZ8D-Rw0bE9VO2HLG-t794`
- Legacy rollback/reference workbook: `1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms`
- Acceptance matrix: `migration/verification/acceptance-matrix.md`

## Gate result

The owner supplied `AUTHORIZE_GM0_TO_GM9_CUTOVER = YES` in the GM-9 invocation.

This gate does not authorize public publication, force-push, legacy deletion, or irreversible
permission changes.

## Completed bounded execution

1. Source and staging workbook identities and exact five-tab topology were re-read.
2. The deterministic fingerprint remained exact.
3. KTD tests passed; no affected GM-0 through GM-8 row reopened.
4. The 22-tab legacy workbook remained accessible as rollback/reference.
5. The exact workbook was renamed to CURRENT CANONICAL without rebuilding its cells.
6. Repository `main` was fast-forwarded without force or history rewrite.
7. Canonical workbook, runtime mapping, repository ref, and legacy accessibility were read back.
