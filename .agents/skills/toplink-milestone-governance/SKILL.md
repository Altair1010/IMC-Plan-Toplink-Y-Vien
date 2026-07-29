---
name: toplink-milestone-governance
description: Assess and operate Toplink Y Viện milestones with source precedence, leases, DMP traces, two-run controls, stable identity, and external-write gates. Use when selecting the next action, updating milestone state, preparing a handoff, or deciding whether work may advance.
---

# Toplink Milestone Governance

## Determine the owner and gate

Read `STATE.md`, `task.md`, `GOVERNANCE.md`, `spec.md`, then the exact section of `docs Toplink/TOPLINK_PAGE_MILESTONES.md`. Treat the master plan as the decision owner and the milestones file as the delivery/Done owner. A summary cannot override either.

Check scope, predecessor status, input availability, canonical artifact paths, reviewer requirements, human gates, DMP trace requirement, and external-state requirements before writing.

## Apply the state machine

1. Acquire a scoped lease in `task.md` before shared writes.
2. Keep work local/staging until all required evidence and reviews pass.
3. For TL-M1–TL-M5, maintain Run 1 build/reconciliation and fresh Run 2 audit/finalize only.
4. Use stable IDs; never create `_v2` tabs or broad Sheet replacements.
5. Treat absent Page/Sheet target, input, or approval as `BLOCKED_INPUT` / `SYNC_PENDING_TARGET`.
6. Release the lease and record evidence-backed checkpoint, blockers, and next safe action.

## External write gate

Do not write to a Page or Sheet unless the user has supplied the exact destination and approval. For an approved Sheet write, use the smallest bounded upsert and exact-range read-back. A write acknowledgment without read-back is failed verification.

## Output

State the current milestone, allowed action, blocked dependencies, required reviewers, required human input, trace/manifest state, and a precise next safe action. Never mark `APPROVED` or milestone completion without its canonical Done gate.
