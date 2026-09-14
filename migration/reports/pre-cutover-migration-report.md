# KTD Great Migration — Pre-Cutover Report

- Run ID: `KTD-GM-20260914-201546-f9ea6b6`
- Start: `2026-09-14T20:15:46+07:00`
- Verification checkpoint: `2026-09-14T20:44:07+07:00`
- Terminal state: `PROMOTION_PENDING`
- Source repository baseline: commit `f9ea6b61941dd46872acc39d180b8d847ceb1ec7`
- Observed source drift: no Git commit drift; package label called a commit a tree SHA
- Verified runtime commit: `d95397b`
- Target workbook fingerprint: `627ab66d724c2e5017a3ee613433d65ba11048233c42b523bf288ee71e043c30`
- Staging workbook: `1v2bk-MOrYyDybgfAh1sYnOZ8D-Rw0bE9VO2HLG-t794`
- Legacy/rollback workbook: `1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms`
- AMH evidence: `F:\tmp\evidence AMH v0.3\runs\2026-09\KTD-GM-20260914-201546-f9ea6b6`

## Phase verdicts

GM-0 through GM-8: PASS. GM-9: PROMOTION_PENDING because the invocation explicitly set
cutover authorization to NO.

## Verification summary

- Package checksums: 16/16 PASS.
- Migration-ledger coverage: 50/50 active semantic objects classified.
- Target workbook: exact four Vietnamese human tabs plus `_CONTROL_PLANE`.
- Live populated ranges: 5/5 exact readback matches.
- Active KTD tests: 9/9 PASS; Python compile PASS.
- Repository suite: 68/72 PASS; four historical tests error only because their legacy approval
  fixtures have expired. No legacy implementation or fixture was changed.
- Pre-cutover acceptance: 42 PASS, 3 PASS_WITH_NOTE, 1 GM-9-only NOT_TESTED, 0 FAIL.

## Evidence boundaries

Eight current business fact families remain explicit UNKNOWN because no authoritative current
KTD source was available. The workbook surfaces those gaps and never fills them from Toplink
history. Campaign seed rows are capture needs, not claims that events/assets already exist.

## Method and gates

M0 was used throughout; M1 was not needed. One UTF-8 transport defect was repaired. No
regression occurred in the active KTD route. The owner cutover gate remains pending.

No public Page publication, legacy deletion, force-push, canonical promotion, or permission
change was performed.
