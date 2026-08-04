# Implementation plan

## N0 — Governance correction

- [x] Expand the scoped lease to exact shared files.
- [x] Replace one-file/one-tab language with 24 domain datasets in canonical owners and `TL-SHEET-001`.
- [x] Record V2 as `TECHNICAL_READBACK_PASS · BUSINESS_MODEL_FAILED` without editing historical JSON.
- [x] Add immutable Run 1 addendum and Run 2 correction manifest; keep `NOT_COMPLETE`, no Run 3.
- [x] Gate: targeted canonical/status scan and `git diff --check` pass.

## N1 — Registry, compiler, and tests

- [x] Load `trellis-before-dev` and scoped specs before code edits.
- [x] RED: replace prose-centric tests with dataset, PK/FK, enum, digest, approval, bounded-range,
      partial-write, Unicode/formula/validation, and recovery tests.
- [x] GREEN: implement the versioned 24-tab registry and seven requested CLI commands.
- [x] Keep all pure validation/dry-run paths offline and fail before network on drift.
- [x] Gate: unit tests, `py_compile`, CLI dry-run, and determinism checks pass.

## N2 — Reconciliation and sidecars

- [x] Map all 14 manifest outputs into the 24 datasets; preserve verified semantics.
- [x] Create explicit gaps/actions instead of filling absent inputs.
- [x] If a material content semantic changes, stop and route repair through existing Run 1 DMP and
      existing Run 2 fresh-audit correction lane; never create Run 3.
- [x] Generate 24 deterministic sidecars, output index, FK graph, digests, report, and owner actions.
- [x] Gate: coverage 14/14; PK/FK/dedup/cardinality/enum/Unicode/source-digest checks pass.

## N3 — Independent review

- [x] Run source grounding then communication safety for public/health-sensitive records.
- [x] Run milestone governance then IMC delivery checks.
- [x] Dispatch one fresh-context read-only reviewer after schema freeze; review governance,
      isolation, safety, data integrity, coverage, and destructive-range safety.
- [x] Resolve all Critical/Major findings; disposition Minor findings with evidence.
- [x] Run `trellis-check` and full repository checks.

## N4 — Approval bundle and gated migration

- [x] Capture a read-only live snapshot and compare with V2 read-back; unexpected drift hard-stops.
- [x] Build unsigned `TL-SHEET-RUN2-CORRECTION-01` with 10 creates, 24 bounded replacements,
      formatting/validation, exact ranges/limits, digests, expiry, and read-back ranges.
- [ ] Commit the unsigned bundle and stop with `external_writes=0`.
- [ ] Only after fresh exact digest-bound `APPROVED`: revalidate lease/target/identity/hashes,
      mutate minimally, and exact-read-back 24/24 plus `Trang tính1` integrity.
- [ ] On partial write: persist `VERIFY_FAILED`, capture state, require new recovery approval.

## N5 — Closure

- [ ] Reconcile correction evidence and mutation accounting into output index/manifest/status files.
- [ ] Keep TL-M1–TL-M5 `NOT_COMPLETE` while non-Sheet human gates remain open.
- [ ] Run full-scope checks, update Trellis spec if warranted, commit by verified gate, checkpoint,
      release lease, and archive only when the applicable approval state is honestly complete.

## Validation commands

```text
python -m unittest .trellis.scripts.tests.test_toplink_sheet_sync
python -m py_compile .trellis/scripts/toplink_sheet_sync.py
python .trellis/scripts/toplink_sheet_sync.py validate-datasets
python .trellis/scripts/toplink_sheet_sync.py compile-datasets --check-determinism
python .trellis/scripts/toplink_sheet_sync.py build-correction-bundle --dry-run
git diff --check
python ./.trellis/scripts/get_context.py --mode packages
```

## Rollback points

- Before approval: discard only newly generated correction artifacts; never alter historical V2 files.
- After any external write begins: no automatic rollback. Persist current state and prepare a newly
  approved recovery bundle.
