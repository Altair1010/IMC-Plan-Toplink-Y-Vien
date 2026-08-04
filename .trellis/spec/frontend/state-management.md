# Artifact and Workflow State

## State has named owners

This project does not have browser-local, global, URL, or server-cache state.
Its reader-facing state is stored in files with strict ownership:

| State | Owner | Rule |
|---|---|---|
| Active work and writer lock | `task.md` | one scoped lease; checkpoint and release on handoff |
| Sprint summary and blockers | `STATE.md` | concise facts only; never overrides canonical sources |
| Durable verified lessons | `MEMORY.md` | no temporary, speculative, secret, or unverified content |
| Strategy and scope | `docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md` | canonical strategy owner |
| Milestone gate and status | `docs Toplink/TOPLINK_PAGE_MILESTONES.md` | canonical execution owner |
| Session/task metadata | `.trellis/` JSON and JSONL | local automation state, validated by its readers |

## Update rules

- Change the source of truth once, then update only the allowed derived views.
  A `STATE.md` summary cannot advance a milestone or erase a `task.md` blocker.
- Before a shared document mutation, acquire the exact `task.md` lease. On a
  handoff: stop writing, record paths/digests/verdicts/blockers, release the
  lease, then let the next runtime acquire a new one.
- Preserve the status vocabulary and human-approval boundary. `LOCAL_VERIFIED`
  or an Agency `PASS` does not mean `APPROVED`, published, or externally
  delivered.
- Keep Google Sheets `BLOCKED_TARGET_INPUT` unless the user supplies an exact
  approved target and bounded write authorization. No document or hook may
  infer the target.

## Avoid

- Do not introduce a Redux, Zustand, React Query, or similar state library.
- Do not duplicate the same live status independently across several plans.
- Do not treat transient tool output as canonical state without recording the
  required trace, source path, and verdict.
