# Google Sheets architecture

Authoritative contract: `docs/system/toplink-google-sheets-operational-contract.md` (TL-SHEET-001
v0.3.0). This file is the short orientation; where the two differ, the contract wins.

## Current state

The target workbook is supplied and read-only verified. The human owner deleted all 24 `TL_*` tabs,
so the workbook now holds only the default tab `Trang tính1` (sheetId 0). Write state is
`BOUNDED_APPROVAL_PENDING`: no script, connector, or agent may create a tab or write a cell until an
exact digest-bound approval is signed, and none may create, guess, or reuse a Thảo Tây spreadsheet,
tab, range, or schema.

## Three layers

- **Front** — 21 `YV_` tabs with Vietnamese headers in reading order. A human reads a plan here, not
  a data dump. `report` (index 0) and `00_Y_VIEN_CAN_CHOT` (index 1) lead.
- **Back** — JSON sidecars under `staging/` holding the full machine record, plus two hidden columns
  `_key` and `_audit` at the end of every tab, both `hiddenByUser = true`. The 11 common provenance
  fields never appear on the front.
- **Bridge** — a deterministic, network-free generator produces `staging/yv-humanize/report-plan.json`;
  the executor applies exactly that and reads back both value and format.

## Write contract

Before an external write, obtain the user-approved spreadsheet ID, tab, range, schema, stable
identity fields, source artifact, and write authorization. One approval per action — `CREATE_TAB`,
`UPSERT`, `READBACK` — each single-use and each carrying `write_executed: false`. Then:

1. Validate the local source artifact and DMP/review state; rebuild `report-plan.json` independently
   and match `workbook_content_hash` before touching the network.
2. Snapshot the `before` state of each range.
3. Upsert only the smallest approved range using stable identity. `valueInputOption = RAW`; a cell
   starting `+ = - @` is written as text.
4. Apply colour by direct format (`repeatCell.userEnteredFormat.backgroundColor`). Conditional
   formatting is forbidden; the rule count after the write must be 0.
5. Preserve unrelated formulas, formatting, protected cells, user data, and `Trang tính1`.
6. Read back the exact range and verify identity, row/column count, required values, Vietnamese
   Unicode, **and format**: freeze, filter, wrap, alignment, width, `hiddenByUser` on `_key`/`_audit`,
   and the exact set of ACTION_REQUIRED cells.
7. Record the revision and evidence in `03_OUTPUT_INDEX` and `04_DECISIONS`.

A response acknowledging a write is not verification. A mismatch restores the `before` snapshot and
stays `VERIFY_FAILED`; a failed or unreadable target is `VERIFY_FAILED` or `BLOCKED_AUTH`, and local
work stays staging. No status escalates on the way through — only the human owner sets `APPROVED`.
