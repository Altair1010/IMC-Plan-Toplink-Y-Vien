# Staging Workbook Readback

- Run: `KTD-GM-20260914-201546-f9ea6b6`
- Source workbook: `1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms` (legacy/reference; unchanged)
- Target workbook: `1v2bk-MOrYyDybgfAh1sYnOZ8D-Rw0bE9VO2HLG-t794` (staging; non-canonical)
- Target plan fingerprint: `627ab66d724c2e5017a3ee613433d65ba11048233c42b523bf288ee71e043c30`

## Value readback

Each populated target range was read from Google Sheets after the write and compared with the
deterministic plan after normalizing omitted trailing empty cells.

| Sheet | Range | Shape | Exact match |
|---|---|---:|---|
| `YV_01_BRAND` | `A1:C30` | 30 x 3 | PASS |
| `YV_02_AUDIENCE_PAGE` | `A1:F20` | 20 x 6 | PASS |
| `YV_03_CONTENT_SYSTEM` | `A1:I24` | 24 x 9 | PASS |
| `YV_04_CAMPAIGN_CALENDAR` | `A1:S19` | 19 x 19 | PASS |
| `_CONTROL_PLANE` | `A1:O20` | 20 x 15 | PASS |

CellData readback also found 9 validated cells in the bounded Content System range and 6
validated cells in the bounded Campaign range. Header/background/wrap formatting was returned
for the populated cells.

## Topology readback

After the exact-value readback passed, the 22 copied legacy tabs were deleted from the staging
workbook only. Metadata readback returned exactly these five active sheets, in order:

1. `YV_01_BRAND` (`1230273866`)
2. `YV_02_AUDIENCE_PAGE` (`874501956`)
3. `YV_03_CONTENT_SYSTEM` (`849632411`)
4. `YV_04_CAMPAIGN_CALENDAR` (`727506307`)
5. `_CONTROL_PLANE` (`1505896630`)

The source workbook remains the rollback and legacy lineage pointer.
