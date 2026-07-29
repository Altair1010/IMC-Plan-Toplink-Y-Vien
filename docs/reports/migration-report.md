# Migration report — Toplink Y Viện

## Scope

On 2026-07-29, the user authorized moving `F:\Codex\IMC Plan - Thảo Tây\docs Toplink` into this
repository and creating an independent Toplink IMC scaffold.

## Data move verification

- Source files expected: 14.
- Target files found: 14.
- Missing files: 0.
- Unexpected files: 0.
- SHA-256 mismatches: 0.
- Source folder after move: absent.

The moved set includes `TOPLINK_PAGE_MASTER_PLAN.md` and `TOPLINK_PAGE_MILESTONES.md`, which were
untracked user work in the source repository. The source repository's other dirty root files were
not edited by this migration.

## Scaffold decisions

- Initialized a fresh Git repository and Trellis 0.6.8 project; no source Git history, Trellis
  task archive, workspace journal, or developer state was copied.
- Inherited the selected six Agency reviewers and the Trellis workflow layer.
- Recorded, rather than copied, the selected DMP capability map because DMP is a shared runtime.
- Added Toplink-specific control-plane documents, `spec.md`, knowledge brief, routing, safety,
  migration, and Sheets architecture records.
- Excluded secrets, credentials, caches, backups, staging data, vendor bulk content, and
  Thảo Tây deliverables/external identifiers.
