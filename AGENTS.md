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

## Token optimization policy

Applies to every runtime in this repo (Claude Code and Codex CLI). The goal is to spend the
fewest tokens that still reach a correct, traceable result. Reducing tokens must never lower
verification rigor: fail-closed gates, evidence, and human `APPROVED` still stand.

### Model tiering

- Use a low-cost model for bounded, mechanical work: search, reading, keyword extraction, file
  location, structure mapping, and first-pass planning. Pick the tier by how much has to be read:
  - Claude Code: Haiku for light search/read; Sonnet (medium) when the volume is larger.
  - Codex CLI: 5.4 for light search/read; 5.5 when the volume is larger.
- Use a stronger model only for editing, reconciliation, validation, judgment, and skill
  authoring. Keep raw source extraction separate from final strategic decisions.
- When a step is pure search or "where is X", route it to a cheap read-only agent
  (`Explore`, `cavecrew-investigator`, `trellis-research`) and consume its compressed result
  instead of reading the corpus yourself.

### Search before read

- Locate first, read second. Run `grep` for a keyword — a single word or an exact phrase — to
  find the file and line, then open only that region. Do not open a whole file to find one symbol.
- Prefer content search with line numbers (`Grep output_mode=content -n`) so you can jump to an
  exact `offset`/`limit` window.
- Read the minimum relevant subset. For a large file, read the ranges the grep hits point to, not
  the entire file. Re-grep to widen only when a hit proves insufficient.
- Use `count` mode to size a footprint, but switch to `content -n` before drawing a verdict — a
  raw hit count cannot tell an allowed guardrail mention apart from a real leak.
- Anchor a probe on a distinctive literal (a URL, a known prefix) before reaching for a generic
  regex, and exclude generated artifacts (`.template-hashes.json`, lock files) so wide patterns do
  not match hashes or build noise.
- Consult indexes before full documents: `.trellis/spec/*/index.md`,
  `docs/system/toplink-knowledge-brief.md`, and section headers of the canonical plans. Open the
  full file only when the index is not enough. The brief is a compact aid, never a replacement for
  the canonical plan or milestone contract.

### Read discipline

- Never re-read a file you just edited to "verify"; the edit tool already confirms success and the
  harness tracks file state.
- Do not reload broad unrelated corpora to continue a nearly complete task. Cache a fact once, then
  reference it by `path:line` rather than re-quoting it.
- Persist paths, digests, verdicts, and blockers at a material pause (journal / `task.md`
  checkpoint) so the next turn resumes without re-reading everything.
- Compress or summarize large tool outputs before reasoning over them; keep only the decisive lines.

### Execution efficiency

- Batch independent tool calls in one turn (parallel reads/greps) instead of serial round-trips.
- Quote the shortest decisive line of an error or log, not the full dump, unless the full text is
  requested.
- Scope every request: state the exact files or ranges to touch so a delegated agent does not sweep
  the repo. Refuse or narrow any task that would require reading far more than the change needs.

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
- The Toplink-only tab registry, approval payload, mapping, validation, and read-back contract is
  `docs/system/toplink-google-sheets-operational-contract.md`; it never authorizes reuse of a Thảo
  Tây workbook or creation of an external target.

### Shared-write protocol

Before editing shared project artifacts, take a scoped lease in `task.md`. Leave a checkpoint
with evidence after each meaningful step, then release the lease at completion. Do not erase
unresolved blockers or claim a milestone has advanced without the canonical Done gate.

### Claude ↔ Codex coordination

The detailed, Toplink-only contract is
`docs/system/claude-codex-operating-contract.md`. It is authoritative for runtime ownership,
handoff, approval tiers, two-run collaboration, and file-ledger behaviour.

- Claude Code owns DMP raw authoring, creative/strategy drafts, and Agency-review coordination.
- Codex CLI owns repository plumbing, evidence/status/allowed-use reconciliation, schemas,
  manifests, QA, bounded automation, and exact read-back verification.
- Neither runtime may invent brand, founder, product, legal/franchise, health, availability, or
  performance facts, nor grant a human `APPROVED` state.
- `TL-M1`–`TL-M5` are one two-run package: `TOPLINK_RUN1_BUILD`, then
  `TOPLINK_RUN2_FRESH_AUDIT_FINALIZE`. A third run is forbidden.

#### File lease and explicit handoff

- The single live lock is `task.md → 🔒 Lease`: runtime, concrete file set, ICT start time, and
  purpose. An overlapping writer is a hard stop; read-only work may run in parallel.
- A handoff is always: stop writing → checkpoint paths/digests/verdicts/blockers → release the
  old lease → recipient acquires a new lease. There is no implicit role switch.
- Use `docs/system/templates/handoff-claude-to-codex.template.md` and
  `handoff-envelope.template.json` for cross-runtime transfer. In Run 2, the recipient completes
  the required independent audit before relying on the handoff findings.
- Never deploy a coordination service or reuse a Thảo Tây identifier, credential, Sheet, Page,
  baseline, deliverable, or milestone.
