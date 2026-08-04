# Design

## Execution boundary

Implement the supplied DAG N0–N12 as a file-ledger workflow. Canonical authority remains the master plan/milestones, `RULES.md`, governance contract, and frozen Run 1 locks. Claude Phase A is a withheld input behind the N3 temporal cut.

## Data flow

1. Recompute locks and lease state.
2. Acquire scoped lease.
3. Read only canonical/Run 1 evidence and the 14 outputs; write blind audit.
4. Hash and freeze the blind audit in JSON plus `task.md` checkpoint.
5. Read Claude bundle/handoff; cross-check locks and output digests.
6. Build merged issue ledger, route each finding, and apply minimal in-place repairs.
7. Re-run integrity/safety/gate checks and build paired manifest.
8. Skip or execute the Sheet subgraph strictly from the signed-approval predicate.
9. Checkpoint, release lease, and emit one allowed verdict.

## Safety and rollback

- Capture pre-repair hashes and minimal diffs. A repair that weakens a gate or expands a claim is reverted at the finding node and routes to `STOP_HUMAN_GATE`.
- Any lock drift routes to `FAIL_BACK_TO_RUN1`; it is never repaired inside Run 2.
- No competing files or broad cleanup are touched; existing unrelated worktree changes are preserved.
