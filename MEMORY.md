# MEMORY.md — durable decisions and verified patterns (Toplink Y Viện)

Only compact, verified, reusable knowledge belongs here. `task.md` owns active detail; Git history
owns complete history; this file never stores a secret, unnecessary PII, temporary hypothesis, or
unverified conclusion.

## Architecture decisions

- [2026-07-29] Toplink is an independent repository. `docs Toplink/` is the evidence/plan source;
  `TOPLINK_PAGE_MASTER_PLAN.md` owns strategy and `TOPLINK_PAGE_MILESTONES.md` owns execution.
- [2026-07-29] The only DMP brand slug is `toplink-y-vien`; never create or route to
  `toplink-page`.
- [2026-07-29] Use a file-ledger coordination model, not a service: the accepted contract is
  `docs/system/claude-codex-operating-contract.md`; `task.md` is the only live lease ledger.
- [2026-07-29] `TL-M1`–`TL-M5` use exactly Run 1 build/reconciliation plus fresh-context Run 2
  audit/finalize. Digest/profile/active-brand drift returns the affected work to Run 1; no Run 3.
- [2026-07-29] Google Sheets is `BLOCKED_TARGET_INPUT` until exact user target and approval exist.
  Any future write is stable-identity based, bounded, and exact-read-back verified.

## Safety and evidence conventions

- Local output remains staging until required DMP trace, Agency review, human/professional gates,
  and—where applicable—approved external read-back pass. `LOCAL_VERIFIED` is never `APPROVED`.
- Never infer or reuse a Thảo Tây credential, Page/Sheet target, baseline, deliverable, milestone,
  or brand fact. Its process pattern is not Toplink evidence.
- Four Toplink-specific skills enforce source grounding, IMC routing, communication safety, and
  milestone governance. Their verified smoke test blocks unsupported nationwide booking, fixed-time
  cure, before/after testimonial, and unapproved publishing claims.

## Working conventions

- Start sessions with `AGENTS.md → STATE.md → RULES.md → task.md`, then load only the active
  milestone and its exact evidence. At a material pause, checkpoint before context is lost.
- One artifact has one writer. Handoff means stop writing, persist paths/digests/verdicts/gates,
  release the lease, then let the next runtime acquire a new scoped lease.
- Store actual run handoffs and manifests from the committed templates; never promote an empty
  template or a mock invocation as a completed deliverable.

## Verified migration record

- [2026-07-29] The 14-file Toplink source set moved with zero SHA-256 mismatch. Unrelated dirty
  files in the source repository were deliberately untouched.
