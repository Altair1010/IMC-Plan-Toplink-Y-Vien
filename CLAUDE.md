# Working conventions — IMC Toplink Y Viện

Read `AGENTS.md`, `STATE.md`, `RULES.md`, `task.md`, and `spec.md` before changing
project artifacts. For strategy or milestone work, also read the two canonical files
under `docs Toplink/` before proposing a deliverable.

## Roles

- DMP produces a traceable local draft.
- Agency Agents review only their routed specialty; use no more than three per workstream.
- The human owner remains the only authority that can mark a public health, legal, or
  publication item `APPROVED`.
- Codex maintains repository plumbing, evidence maps, validation, and bounded automation;
  it must not invent brand, medical, legal, product, or founder facts.

## Model discipline

Use a lower-cost model for bounded source reading, extraction, and planning. Use a stronger
model for editing, reconciliation, validation, and skill authoring. Keep source extraction
separate from final strategic judgment.

## External-state rule

Never use a Thảo Tây Page, Sheet, identifier, credential, or analytics baseline. The Toplink
Sheet target is `BLOCKED_TARGET_INPUT` until the user supplies the exact destination and write
approval.

Use `docs/system/toplink-google-sheets-operational-contract.md` for the Toplink-only tab registry,
mapping, approval payload, and read-back. It plans local architecture only until an exact target is
approved.

## Prime directives

1. Follow the user, `RULES.md`, `GOVERNANCE.md §1`, and Toplink canonical owners in that order.
2. Treat missing, unverified, health-sensitive, legal, privacy, and external-target inputs as
   fail-closed. Record the blocker; never fill it with plausible content.
3. `LOCAL_VERIFIED`, Agency `PASS`, and a DMP trace are not human `APPROVED` and do not authorize
   publishing, Page mutation, Sheet mutation, or external-runtime mutation.
4. Keep Toplink independent: a Thảo Tây pattern can inform process only, never facts, targets,
   credentials, output, or baseline.

## Session and context discipline

Read in this order before shared work: `AGENTS.md` → `STATE.md` → `RULES.md` → `task.md` →
`GOVERNANCE.md §1 + §3` → `spec.md` → the active Toplink milestone and its exact evidence inputs.
Read the minimum relevant source subset; use `docs/system/toplink-knowledge-brief.md` only as a
compact aid, never as a replacement for the canonical plan or milestone contract.

At a material pause, persist paths, evidence/digests, verdicts, blockers, and the next safe
action before context is lost. Do not load broad unrelated corpora merely to continue a nearly
complete task.

## Cross-runtime discipline

Follow `docs/system/claude-codex-operating-contract.md`. Before any shared write, acquire the
`task.md` lease. For `TL-M1`–`TL-M5`, keep the exact two-run model and use the committed handoff
and manifest templates. A runtime must stop writing and release its lease before the other one
starts an overlapping file set.

## Completion and communication

Close a work item only after the canonical Done gate, required trace/reviews, local validation,
human gates, and—when an external destination is required—approved bounded write/read-back have
passed. Final updates state files changed, checks/verdicts, unresolved gates, external ranges
changed (if any), and the next safe action. Respond to the user in Vietnamese with diacritics.
