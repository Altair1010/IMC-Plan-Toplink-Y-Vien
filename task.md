# task.md — active execution only

## Status

`IN_PROGRESS` — regenerate the Toplink operating scaffold from the approved plan. This is a
documentation/control-plane change only; no DMP deliverable invocation, Page mutation, Google
Sheets write, public publishing, or external-runtime mutation is authorized.

## Current work

- **Scope proof:** user approved the 2026-07-29 scaffold-regeneration plan.
- **Deliverables:** Toplink-specific Claude ↔ Codex protocol; expanded root control plane;
  lifecycle templates; two-run handoff/manifest templates; cross-link validation.
- **Non-goals:** importing Thảo Tây history, staging payloads, credentials, Page/Sheet IDs,
  analytics baselines, local tool caches, or its brand/content facts.
- **Next safe action:** update the root control-plane documents while this lease is active.

## Assumptions

- `docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md` and `TOPLINK_PAGE_MILESTONES.md` stay the only
  strategy and execution owners for Toplink.
- This repository remains independent. A source pattern may be adapted, but never becomes a
  source of Toplink facts or external targets.

## 🔒 Lease — Claude Code ↔ Codex CLI

> Before writing a shared file set, add one scoped row. Read-only work may run in parallel.
> A handoff requires the current writer to stop, checkpoint durable state, and release its row
> before the next writer acquires a new one.

| Agent/runtime | File set | Started (ICT) | Purpose |
|---|---|---|---|
| Codex CLI | root control plane; `docs/system/**`; `docs/prompts/**`; `README.md` | 2026-07-29 | Regenerate approved Toplink scaffold |

## Checklist

- [ ] Define the Toplink-specific Claude ↔ Codex contract and ownership boundaries.
- [ ] Regenerate root rules, governance, loop, state, memory, and read order.
- [ ] Add reusable handoff and two-run manifest templates.
- [ ] Validate references, prohibited cross-brand leakage, UTF-8 content, and diff hygiene.
- [ ] Record a checkpoint, release the lease, and reset this file to the idle template.

## Verification contract

- Every link/reference resolves to a tracked Toplink path.
- No document grants an agent human approval or permits an unapproved external mutation.
- `toplink-y-vien` remains the only DMP brand slug; Sheet status remains
  `BLOCKED_TARGET_INPUT`.
- No Thảo Tây credential, identifier, baseline, deliverable, or runtime configuration enters
  the repository.
- `git diff --check` and bounded content checks pass before close.

## Blockers

None for the documentation-only scaffold work. Existing Toplink execution inputs remain blocked
as recorded in `STATE.md` and `GOVERNANCE.md §3`.

## Recent checkpoints

- [2026-07-29] `STARTED` — user approved the scaffold-regeneration plan; Codex acquired the
  scoped documentation lease. External mutations remain zero.
