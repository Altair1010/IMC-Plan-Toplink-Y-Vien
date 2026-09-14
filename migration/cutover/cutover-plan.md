# GM-9 Cutover Plan

Status: `PROMOTION_PENDING`

## Locked inputs

- Verified runtime commit: `d95397b`
- Verified workbook plan fingerprint: `627ab66d724c2e5017a3ee613433d65ba11048233c42b523bf288ee71e043c30`
- Verified staging workbook: `1v2bk-MOrYyDybgfAh1sYnOZ8D-Rw0bE9VO2HLG-t794`
- Legacy rollback/reference workbook: `1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms`
- Acceptance matrix: `migration/verification/acceptance-matrix.md`

## Gate

Do not promote until the owner supplies exactly:

`AUTHORIZE_GM0_TO_GM9_CUTOVER = YES`

This gate does not authorize public publication, force-push, legacy deletion, or irreversible
permission changes.

## Bounded execution after authorization

1. Re-read source and staging workbook identities and exact five-tab topology.
2. Recompute the deterministic plan fingerprint and verify it remains exact.
3. Re-run the KTD tests and reopen only affected acceptance rows if drift exists.
4. Confirm the legacy workbook remains the rollback/reference object.
5. Promote the exact verified KTD pointers without rebuilding the workbook.
6. Read back canonical workbook, runtime mapping, and legacy accessibility.
7. Write the cutover record, finalize AMH state as DONE, and stop.
