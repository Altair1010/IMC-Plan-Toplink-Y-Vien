# Verify and reconcile Toplink Run 1 TL-M5

## Goal

Verify Claude TL-M5 Phase A handoff, reconcile Run 1 Phase B, execute TL-M1-TL-M5 gates, checkpoint and logical commits without Run 2 or external writes.

## Requirements

- Verify the released Claude TL-M5 Phase A handoff before acquiring a shared-file lease.
- Reconcile TL-M5 and repaired TL-M2–TL-M4 real DMP traces into the existing Run 1 Phase B artifacts.
- Preserve stable IDs and assign exactly one allowed disposition to every delta.
- Run all canonical Run 1 lock, DMP, TL-M5, safety, and QA gates.
- Set `RUN1_PASS · LOCAL_VERIFIED · PHASE_B_RECONCILED · NOT_MILESTONE_COMPLETE` only if every required Run 1 gate passes; otherwise record `RUN1_NOT_PASS` with exact blockers.
- Keep all human/professional/legal/privacy gates open and Sheet state `SYNC_PENDING_TARGET`.
- Do not start Run 2, mutate Sheet/Page/runtime/canonical contracts, publish, or create `APPROVED`/`COMPLETE` states.
- Preserve unrelated dirty work and report `BLOCKED_WORKTREE_OWNERSHIP` if a clean tree cannot be established without touching another owner's files.

## Acceptance Criteria

- [x] Handoff lock/profile/source/version/brand/path/hash/trace/approval/external-write preflight is evidence-backed.
- [x] Five TL-M5 deliverables and all TL-M1–TL-M5 real DMP evidence are represented in the Run 1 manifest.
- [x] Phase B files `10`–`70` and the manifest agree on statuses, stable IDs, dispositions, logical datasets, reviewer gates, and zero external writes.
- [x] JSON/schema, path/hash/reference/orphan/encoding/newline/placeholder/secret/PII/isolation/whitespace checks pass.
- [x] Manifest SHA-256 is computed after final content and recorded without creating a self-hash contradiction.
- [x] `STATE.md` and `task.md` checkpoint the exact verdict, evidence, blockers, `external_writes=0`, `milestone_advance=false`, no `APPROVED`/`COMPLETE`, and Run 2 not started.
- [x] Lease is released, exact owned file sets are committed logically, and final Git ownership/status is reported truthfully.

## Notes

- Keep `prd.md` focused on requirements, constraints, and acceptance criteria.
- Lightweight tasks can remain PRD-only.
- For complex tasks, add `design.md` for technical design and `implement.md` for execution planning before `task.py start`.
