# Correct Toplink operational Sheet model

## Goal

Replace the technically successful but operationally invalid “14 Markdown files → 14 prose tabs”
delivery with a deterministic 24-dataset IMC operating workbook. Preserve canonical Markdown,
historical Run 1/Run 2 evidence, stable identities, human gates, and exact read-back controls.

## Background and confirmed facts

- Target is the existing Toplink-only spreadsheet
  `1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms`.
- Live read-only metadata on 2026-08-04 shows preserved `Trang tính1` plus 14 existing Toplink tabs
  with the sheet IDs recorded by V2 read-back.
- V2 delivery is immutable historical evidence and is classified
  `TECHNICAL_READBACK_PASS · BUSINESS_MODEL_FAILED` for this correction.
- The 14 canonical Markdown artifacts remain the human-readable source; normalized JSON sidecars
  are the machine interface.
- The user approved the 24-tab architecture and in-place correction, but no new Sheet mutation is
  approved. The consumed V2 approval cannot authorize this migration.

## Requirements

1. Reconcile `RULES.md`, `STATE.md`, `task.md`, `spec.md`, the master plan, milestones, and
   `TL-SHEET-001` so domain datasets replace one-file/one-tab prose mapping without claiming a
   milestone advance or creating Run 3.
2. Define a versioned registry for exactly 24 tabs with ordered columns, common provenance fields,
   enums, PK/FK rules, validation, formatting, and cardinality.
3. Compile canonical Markdown plus ledgers into deterministic normalized dataset JSON; reject prose
   dumps, duplicate PKs, orphan FKs, invalid enums, false blanks, digest drift, and unsafe approval
   promotion.
4. Preserve all verified strategy/content semantics. Missing facts become explicit input gaps and
   owner actions; no brand, founder, product, health, legal, franchise, availability, performance,
   or approval fact may be invented.
5. Support local commands `compile-datasets`, `validate-datasets`, `snapshot-target`,
   `build-correction-bundle`, `validate-approval`, `execute-correction`, and `verify-readback`.
6. Correction execution must bind target, service-account identity, exact existing/new tab set,
   exact ranges, limits, schema/source/payload/manifest digests, operator, expiry, formatting,
   validation, and read-back. It must stop before network on any drift.
7. Existing tab IDs are retained; ten tabs are created only after new digest-bound human approval.
   All writes and stale-tail clears are bounded to the approved union of old/new used ranges.
8. Partial write never triggers automatic rollback. Record `VERIFY_FAILED`, snapshot current state,
   and require a new approval for recovery.
9. `Trang tính1` and all cells outside approved ranges remain unchanged.
10. Independent review must find zero unresolved Critical/Major findings before generating the
    unsigned approval bundle.

## Acceptance criteria

- [ ] Canonical owners consistently specify 24 domain datasets and classify V2 honestly; Run count
      remains exactly two and TL-M1–TL-M5 remain `NOT_COMPLETE` while human gates are open.
- [ ] Registry contains the exact 24 tab keys approved by the user and mandatory common record fields.
- [ ] Compiler creates byte-identical output and SHA-256 digests for identical inputs.
- [ ] Twenty-four sidecars validate with unique immutable PKs, complete typed FKs, allowed enums,
      valid Unicode, source digests, and no `PROSE`/`section-text` rows.
- [ ] All 14 canonical outputs map many-to-many through `TL_OUTPUT_INDEX`; missing inputs appear in
      `TL_INPUT_GAPS` and `TL_OWNER_ACTIONS`.
- [ ] Unit/integration tests cover all minimum cases in the approved plan, including approval reset,
      bounded stale-tail clearing, partial writes, reordered rows, Unicode/formula/validation loss,
      wrong sheet ID, and mandatory re-approval for recovery.
- [ ] `py_compile`, JSON/schema validation, determinism check, link/reference scan,
      `git diff --check`, Trellis checks, safety review, and independent review pass.
- [ ] An unsigned `TL-SHEET-RUN2-CORRECTION-01` bundle is committed with exact path and SHA-256;
      `external_writes=0` until a later user statement approves that exact digest.
- [ ] After a valid later approval only: bounded mutation and 24/24 exact read-back pass, with a
      read-only integrity proof for `Trang tính1`; otherwise the task stops honestly at approval gate.

## Out of scope

- Run 3, competing artifact versions, `_v2` tabs, broad clears, renames, or deletion of historical
  evidence.
- New DMP authoring unless reconciliation changes material strategy/content semantics.
- Publishing, Page mutation, milestone completion, human `APPROVED`, or resolution of open health,
  legal, franchise, product, privacy, consent, capacity, or asset-rights gates.
- Any Thảo Tây data, identifier, credential, target, baseline, deliverable, or milestone.

## Deferred gate

External migration is deferred until the user provides a fresh statement bound to the exact
correction-bundle repository path and SHA-256. Credential identity is read back only inside the
approved execution process.
