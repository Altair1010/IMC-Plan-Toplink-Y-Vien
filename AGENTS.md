<!-- TRELLIS:START -->
# Trellis Instructions

These instructions are for AI assistants working in this project.

This project is managed by Trellis. The working knowledge you need lives under `.trellis/`:

- `.trellis/workflow.md` — development phases, when to create tasks, skill routing
- `.trellis/spec/` — package- and layer-scoped coding guidelines (read before writing code in a given layer)
- `.trellis/workspace/` — per-developer journals and session traces
- `.trellis/tasks/` — active and archived tasks (PRDs, research, jsonl context)

If a Trellis command is available on your platform (e.g. `/trellis:finish-work`, `/trellis:continue`), prefer it over manual steps. Not every platform exposes every command.

If you're using Codex or another agent-capable tool, additional project-scoped helpers may live in:
- `.agents/skills/` — reusable Trellis skills
- `.codex/agents/` — optional custom subagents

Managed by Trellis. Edits outside this block are preserved; edits inside may be overwritten by a future `trellis update`.

<!-- TRELLIS:END -->

## Toplink operating context

Read `STATE.md`, `RULES.md`, `task.md`, and `spec.md` at the beginning of work. For any
strategy, milestone, or content question, read `docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md` and
`docs Toplink/TOPLINK_PAGE_MILESTONES.md` first; they are the canonical strategy and execution
owners respectively.

### Orchestration

- Digital Marketing Pro v3.15.1 is the primary draft-generation workflow. Use the active brand
  slug `toplink-y-vien` and record a real invocation trace for every deliverable-producing run.
- The six `marketing-*.md` Agency Agents are reviewers/specialists. Use no more than three on a
  workstream and never allow two agents to create competing versions of one artifact.
- Agency reviewers can return `DRAFT`, `REVIEWED`, `VERIFIED`, `PASS`, `FAIL`, or
  `NEEDS_HUMAN_REVIEW`; they cannot grant human `APPROVED`.
- Follow `docs/system/capability-routing-matrix.md` and use the Toplink-specific skills in
  `.agents/skills/` for source grounding, delivery, safety, and milestone governance.

### Toplink boundaries

- Facebook Page is primary; Reels support discovery; TikTok is mechanics-only unless a future
  canonical decision says otherwise.
- Hanoi is the local awareness/service-discovery lane when verified. National activity is
  education/awareness by default. Do not reuse any Thảo Tây channel, Sheet, external identifier,
  credential, baseline, or milestone.
- No health diagnosis/treatment/cure/prevention/guarantee claim, medical replacement claim, or
  unsupported product/service/franchise/legal fact. Sensitive material is fail-closed and routes
  to human/professional review.
- Google Sheets is `BLOCKED_TARGET_INPUT` until the user provides an exact approved target; any
  future write must be bounded, stable-identity based, and exact-read-back verified.

### Shared-write protocol

Before editing shared project artifacts, take a scoped lease in `task.md`. Leave a checkpoint
with evidence after each meaningful step, then release the lease at completion. Do not erase
unresolved blockers or claim a milestone has advanced without the canonical Done gate.
