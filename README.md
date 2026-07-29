# IMC Plan — Toplink Y Viện

Operational repository for the Facebook Page IMC track of Nhất Liệu Y Viện Toplink.
The canonical strategy and milestone contracts live in `docs Toplink/`; all other
documents must preserve their evidence, safety, and approval gates.

## Read first

1. `AGENTS.md`
2. `STATE.md`
3. `RULES.md`
4. `spec.md`
5. `docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md`
6. `docs Toplink/TOPLINK_PAGE_MILESTONES.md`

## Working model

- Digital Marketing Pro is the primary draft-generation workflow.
- The six Agency Agents are bounded specialists/reviewers, not competing writers.
- Health-sensitive, legal, privacy, publication, Page, and Sheets actions require the
  applicable human approval and exact read-back.
- Local documents are staging until their canonical promotion gate passes.

## Repository layout

- `docs Toplink/` — canonical Toplink evidence, plan, and milestone contract.
- `docs/system/` — capability routing, source grounding, setup, and migration records.
- `docs/brand/`, `docs/content/`, `docs/research/` — milestone outputs only.
- `.trellis/` — task lifecycle, working specs, and session records.
- `.claude/`, `.cursor/`, `.agents/` — project-local agents and skills.

## Operational control plane

Before shared work, read `task.md` and `GOVERNANCE.md §1 + §3` after the root read-first files.
Before a Claude/Codex handoff, also read
`docs/system/claude-codex-operating-contract.md`. The committed templates under
`docs/system/templates/` and the two-run prompts under `docs/prompts/` support execution but never
override Toplink canonical evidence, milestone gates, or human approval.

The runtime contract is local-only: no Page, Sheet, publishing, or external-runtime mutation is
authorized by this repository documentation.
