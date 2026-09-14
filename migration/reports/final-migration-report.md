# KTD Great Migration — Final Report

- Run ID: `KTD-GM-20260914-201546-f9ea6b6`
- Program version: `1.0`
- Start: `2026-09-14T20:15:46+07:00`
- Cutover completion: `2026-09-14T21:20:26+07:00`
- Terminal state: `DONE`
- Canonical brand: `KHIẾT TÂM ĐƯỜNG` (`KTD`)
- Current business phase: `DRY_RUN`
- Canonical repository branch: `main`
- Promotion payload revision: `393dba937acf87bbe48a5b9304ac5b49e2c18ba4`
- Verified runtime revision: `d95397b`
- Canonical workbook: `1v2bk-MOrYyDybgfAh1sYnOZ8D-Rw0bE9VO2HLG-t794`
- Target fingerprint: `627ab66d724c2e5017a3ee613433d65ba11048233c42b523bf288ee71e043c30`
- Legacy/rollback workbook: `1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms`
- AMH evidence: `F:\tmp\evidence AMH v0.3\runs\2026-09\KTD-GM-20260914-201546-f9ea6b6`

## Verdict

GM-0 through GM-9 PASS. KTD is current canonical. Toplink / Y Viện is historical/reference.
The exact verified human-first workbook was promoted without changing its cell content. Repository
`main` was advanced by fast-forward only.

## Final verification

- Package checksum: 16/16 PASS.
- Migration ledger: 50/50 active objects classified.
- Workbook topology: four human tabs plus `_CONTROL_PLANE`.
- Workbook content readback: 5/5 exact ranges.
- Active KTD tests: 9/9 PASS; compile PASS.
- Repository suite: 70/74 PASS; the same four archived approval-expiry tests remain disclosed.
- Acceptance matrix: 43 PASS, 3 PASS_WITH_NOTE, 0 FAIL, 0 BLOCKED, 0 NOT_TESTED.
- Legacy workbook: accessible with 22 tabs.
- Canonical and rollback pointers: singular and explicit.

The three notes preserve known evidence limitations: structural operator walkthrough rather than
an independent usability study, a metadata-only derived view, and capture-needs rather than
fabricated current events/assets. Eight current business fact families remain explicit UNKNOWN.

## Authority and method

The owner supplied the GM-9 cutover authorization. M0 was used; M1 was unnecessary. One UTF-8
transport repair and one transient multi-read connector anomaly were isolated without changing
the verified workbook. No public Page publication, force push, history rewrite, legacy deletion,
or permission change occurred.
