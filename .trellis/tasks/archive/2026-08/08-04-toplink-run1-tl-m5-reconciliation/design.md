# Design — Toplink Run 1 TL-M5 reconciliation

## Boundaries

- Canonical plan and milestone contracts are read-only.
- Claude Phase A content, raw invocation evidence, markers, reviews, and handoffs are verified inputs; Codex owns reconciliation artifacts and manifests.
- External systems, DMP runtime state, Page, Sheet, publishing, and Run 2 remain untouched.

## Reconciliation model

1. Accept the released handoff only after exact lock and digest read-back.
2. Extend the existing Phase B ledger and manifest rather than create competing artifacts.
3. Represent every output by immutable stable ID, exact path/hash, evidence status, disposition, and retained gate.
4. Treat Agency `PASS` as structural/local review only; human-sensitive items remain `NEEDS_HUMAN_REVIEW`.
5. Derive the Run 1 verdict from executable integrity checks and canonical gates.

## Integrity and closeout

- The manifest records member artifact hashes; its own SHA-256 is recorded in `STATE.md` and `task.md` after final serialization.
- Commits use exact path lists. Unrelated P1/bootstrap changes are never staged, reset, restored, or stashed.
- A non-empty final worktree caused solely by excluded owner files is reported as `BLOCKED_WORKTREE_OWNERSHIP`, not hidden.
