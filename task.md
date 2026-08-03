# task.md — active execution only

## Status

`BLOCKED_PRE_TL_M5 · RUN1_NOT_COMPLETE`

## Current work

No active writer. Codex worktree/status reconciliation is checkpointed. TL-M5 Phase A is blocked
pending MCBAu P1 worktree disposition, production capacity/start date, and asset-rights boundary.

## 🔒 Lease — Claude Code ↔ Codex CLI

> Add one scoped row before a shared write. Read-only work may run in parallel. A handoff requires
> stop writing → checkpoint → release old lease → acquire new lease.

| Agent/runtime | File set | Started (ICT) | Purpose |
|---|---|---|---|

_Codex pre-TL-M5 reconciliation lease released 2026-08-03T17:19:25+07:00. Checkpoint: classified
all tracked/untracked changes; preserved the MCBAu-owned P1 bootstrap task and unverified
`docs Toplink/11_Product_Yvien.md`; independently validated and committed the generic multi-agent
contract (`3fab204`) and archived its Trellis task (`e04ac6e`); committed nine digest-verified
TL-M2–TL-M4 local artifacts (`468dee1`) and Sheet-governance alignment (`3840115`). Reconciled
`TOPLINK_PAGE_MILESTONES.md` v0.1.3 without milestone advance. Profile
`a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349`, source
`3ba91761612ca482471dc1c071bd7e9d82e5708a3bb13ceb630fed476541fe76`, DMP `3.15.1`, active brand
`toplink-y-vien`, and manifest `48955606d3b2e91c9a5d984c7dc5ec22dcc4f895479a96a069ef372c3ac26427`
all read back exact. Readiness report: `docs Toplink/staging/run1/codex-to-claude-tl-m5-readiness.md`.
Verdict `BLOCKED_PRE_TL_M5`: `BLOCKED_WORKTREE_OWNERSHIP`, `TL-GAP-006`,
`TL-M5-ASSET-RIGHTS-001`, and frozen-source metadata drift `TL-SOURCE-LOCK-STATUS-001`.
`external_writes=0`; no Sheet/Page/publish, no `APPROVED`, no milestone
advance, no Run 1 close, no Run 2/Run 3._

_Fresh Codex final-QA lease released 2026-08-01T13:41:46+07:00. Resolved
`TL-R1-ISSUE-QA-001`. Verified JSON/schema, 9/9 output digests, profile/source locks, DMP 3.15.1,
active brand `toplink-y-vien`, trace/review/handoff/Phase-B digests, stable-ID uniqueness,
dispositions, reference integrity, orphan/path checks, five pillars=100%, reviewer count=3,
UTF-8/final newline, placeholders, secret/PII, isolation and whitespace. Found and repaired one
trailing space at the prior checkpoint; final `git diff --check` exit 0 (non-failing CRLF
normalization warnings only). Updated `70-run1-checks.md` and `run1-manifest.json`; manifest
SHA-256 `48955606d3b2e91c9a5d984c7dc5ec22dcc4f895479a96a069ef372c3ac26427`.
Verdict: `RUN1 · LOCAL_VERIFIED · PHASE_B_RECONCILED · NOT_COMPLETE`.
`external_writes=0`; `milestone_advance=false`; no COMPLETE/APPROVED, Sheet/Page/publish,
Run 2 or Run 3._

_Codex Run 1 Phase B lease released 2026-08-01T13:04:40+07:00. Checkpoint: preflight verified
Phase A marker, 9/9 output digests, G5 profile digest
`a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349`, source digest
`3ba91761612ca482471dc1c071bd7e9d82e5708a3bb13ceb630fed476541fe76` with 5/5 members,
DMP `3.15.1`, and active brand `toplink-y-vien`. Updated
`docs Toplink/staging/run1/{10-evidence-profile-map.md,20-runtime-compatibility.md,30-delta-ledger.json,
40-workstream-reconciliation.md,50-pillar-decision.md,60-agency-review-register.md,
70-run1-checks.md,handoff-claude-to-codex.md,run1-manifest.json}`. The manifest SHA-256 is
`15bbe5bf09da1712cf06050d9c66780e924c8a8dac92d59bfe2d283238cad4b4`.
Preliminary JSON/output-row/UTF-8/placeholder/secret-PII/isolation checks passed, but the final
aggregate QA wrapper repeated `SyntaxError: Unexpected identifier 'n'` before PowerShell execution.
Per stop rule, `TL-R1-ISSUE-QA-001` owner = Codex CLI; no third retry in this turn. Verdict:
`PHASE_B_RECONCILIATION_WRITTEN · QA_BLOCKED · RUN1_NOT_PASS`; health TL-P2/TL-P4+W2, public
positioning, franchise/legal, TL-M5, SheetTargetApproval/read-back and Run 2 remain open.
`external_writes=0`; `milestone_advance=false`; no COMPLETE/APPROVED._

_Claude Run 1 Phase A (TL-M2→TL-M4) lease released 2026-08-01T05:35 ICT. Built 9 deliverables via DMP
raw-authoring (local-only, `external_writes=0`): TL-M2 `docs Toplink/brand/dmp-profile.md` (`2a151493…`) +
`docs Toplink/system/runtime-compatibility.md` (`e38846fb…`); TL-M3 `research/audience-hypotheses.md`
(`4a32da6b…`), `brand/{positioning `7c216e38…`, narrative `02a6f6be…`, content-pillars `451425c1…`
(5 pillars=100%), facebook-page-strategy `cdd1f786…`}`; TL-M4 `brand/{campaign-architecture `c1fda749…`
(relative D-1..D-28, W4=SAFE FALLBACK), kpi-experiment-plan `40a528c6…` (counts=0/rates=N/A)}`. Trace +
agency-review + Phase A marker + handoff addendum in `staging/toplink-reconciled/TL-M2-M4-run1/`. DMP
3.15.1, active brand `toplink-y-vien`, 4 skills invoked (audience-intelligence/campaign-plan/social-strategy/
content-engine, skill-scaffold mode). Verify: G5 profile lock HELD (`a45e4ae4…` unchanged), 5/5 source
digests MATCH, isolation scan 0 external-brand refs, secret/PII 0, `git diff --check` PASS. Codex Phase B
files (`docs Toplink/staging/run1/10..70`, `run1-manifest.json`) NOT touched. `external_writes=0`; no
milestone COMPLETE/APPROVED; human gates open (health TL-P2/P4+W2, public positioning, franchise/legal).
Next actor: Codex Run 1 Phase B reconciliation._

_Claude handoff-refresh lease released 2026-08-01T10:55 ICT. Brought `handoff-claude-to-codex.md` current
to post-18:05 work: added `root-provenance-map.md` (`7962fed2…`) to digest table, updated `input-gap-register.md`
digest (`2e8db2…`→`b12d5b78…`), added Part 2 user decisions TL-D16–D20 (franchise LOCKED, health reviewers,
dossier pending, SA email provided, provenance located), updated issue ledger + closure marker (012–014
PROVENANCE_LOCATED, SA_INFRA_READY, Run 1 still NOT_PASS pending Phase A M2–M5). Verify: 2 changed digests
MATCH actual; `git diff --check` PASS; 0 private-key/Thảo-Tây-workbook-owner leak; `external_writes=0`; no milestone advanced._

_Claude M2→M4 masterprompt lease released 2026-08-01T10:20 ICT. Authored `docs/prompts/TOPLINK_M2_M4_MASTERPROMPT.md`
(Run 1 Phase A build prompt for M2→M4: scaffold read order, token policy ref AGENTS.md, Claude-Codex contract,
G5 lock, isolation, D-1..D-28 relative + 1-2/day skeleton-only, logical Sheet datasets no-write, handoff marker).
Also read Thảo Tây sheet architecture (local schema only, no external Sheet access) to confirm Toplink tab
registry already mirrors it. Verify: `git diff --check` PASS; 0 Thảo Tây workbook-id/owner-email/SA in prompt;
secret scan clean; `external_writes=0`; no DMP/runtime/Sheet action; no milestone advanced._

_Claude #7 provenance-extract lease released 2026-07-30T23:15 ICT. Bounded provenance-only extract from origin
`IMC Plan - Thảo Tây` (read-only, not mutated): TL-GAP-012 (root source-inventory `146140bf…`), TL-GAP-013
(origin profile §2 `c453cee9…` label SUPPORTING + pre-repair backup `09885c2a…`), TL-GAP-014 (origin
STATE/task/GOVERNANCE pointers) → all `PROVENANCE_LOCATED`. Wrote `root-provenance-map.md`; updated
input-gap-register (also TL-GAP-011→RESOLVED). Key finding: repaired drift = original SUPPORTING design,
re-scoped by user §6. Verify: `git diff --check` PASS; 0 secret/Thảo-Tây Sheet-id/credential in new artifact;
`external_writes=0`; no milestone advanced._

_Claude SA-secure + decision-record lease released 2026-07-30T22:45 ICT. Moved SA private key
`imcforyvien-de7e7ee958f4.json` out of `docs Toplink/` into gitignored `.secrets/` (untracked, key never
committed); added SA-key `.gitignore` patterns; repo-wide scan = 0 private_key in tracked tree. Recorded
TL-D19 (SA email `yvien-sheet-writer@imcforyvien…`, write still gated) + TL-D20 (#7 source = sibling
`IMC Plan - Thảo Tây`, extraction pending bounded/isolation-guarded scope). `external_writes=0`; no milestone advanced._

_Claude decision-record lease released 2026-07-30T22:15 ICT. Recorded TL-D16 (franchise/legal KEEP LOCKED),
TL-D17 (health reviewers Thảo Tây-person + Guru, user-attested, per-item gate stays), TL-D18 (dossier to
come with legal certs/kiểm định) in STATE.md Resolved-by-user. `external_writes=0`; no milestone advanced._

_Codex Run 1 Phase B lease released 2026-07-30T21:51+07:00. Checkpoint: verified refreshed Claude
handoff (9/9 artifact digests), input lock (5/5 sources + profile), and DMP runtime outputs; created
the required `docs Toplink/staging/run1/` receipt/index plus `10`–`70` reconciliation artifacts and
`run1-manifest.json` (SHA-256 `0f7c930ef78213e87427a9ee4daf4359a4b2ef7ed07f85c3e59e6f1ba286e98e`).
JSON/schema, stable-ID/disposition, required-path, generated-output digest, UTF-8/placeholder,
secret/PII, whitespace, and `git diff --check` checks PASS. Final status remains
`BLOCKED_INCOMPLETE_PHASE_A · RUN1_NOT_PASS`: TL-M2–TL-M5 deliverable traces/outputs/reviews were
not supplied; human gates remain open; `external_writes=0`; no canonical/runtime/Sheet/Page
mutation and no milestone advanced. Next safe action stays in Run 1: Claude supplies the missing
Phase A package and refreshed handoff. Run 2 was not called._

_Claude TL-M1 handoff-resync lease released 2026-07-30T18:15 ICT. Checkpoint: brought
`handoff-claude-to-codex.md` current after Codex fail-closed digest-conflict stop. Fixed 2 stale
declared digests (`dmp-invocation-block.md` 906568b1→c85865e6 SUPERSEDED, `agency-review-pr-manager.md`
09b64b83→0225c77f Review 2); added 2 files to digest table (`tl-m1-dmp-trace.md` b0272f66,
`tl-m1-closure-readiness.md` bf10341f); DMP trace NOT_AVAILABLE→`VERIFIED_REAL_INVOKE`; profile digest
NOT_AVAILABLE→`a45e4ae4…c8cbe349` (G5 lock); PR verdict→Review 2 `NEEDS_HUMAN_REVIEW`; TL-ISSUE-001 &
profile-drift→RESOLVED; status token BLOCKED→`LOCAL_EVIDENCE_PASS · READY_FOR_CODEX_RECONCILIATION`.
Verify: all 9 declared digests == actual; no `NOT_AVAILABLE`/`dmp_trace=NONE` remain (only 1
SUPERSEDED-tagged historical `BLOCKED_DMP` reference). No fact invented; `external_writes=0`; no
milestone advanced. Codex may re-audit and proceed to Run 1 Phase B._

_Claude TL-M1 closure lease released 2026-07-30T17:55 ICT. Checkpoint: superseded `dmp-invocation-block.md`;
re-ran PR Manager (Review 2 in `agency-review-pr-manager.md`, verdict `NEEDS_HUMAN_REVIEW`, TL-REV-004/005→PASS,
new TL-REV-008/009/010); wrote `tl-m1-closure-readiness.md` (10/12 VERIFY PASS, #7 DEFERRED, #12 HELD, 0 FAIL).
TL-M1 = `LOCAL_EVIDENCE_PASS · READY_FOR_CODEX_RECONCILIATION`, NOT COMPLETE. `git diff --check` PASS; secret
scan clean; `external_writes=0`; no milestone advanced._

_Claude TL-M1 DMP lease released 2026-07-30T17:20 ICT. Checkpoint: 2 real DMP invocations
(`switch-brand toplink-y-vien` + `import-guidelines`), scope import-guidelines only (user choice; brand-setup
skipped to hold G5 profile lock). Added guidelines `voice-and-tone/messaging/visual-identity/channel-styles`
merged with `restrictions` ⇒ 5 cat/52 rules, summary read-back MATCH. Profile.json untouched (digest
`a45e4ae4…` unchanged); 0 "Thảo Tây" in guidelines; `_active-brand.json`→`toplink-y-vien` (backup saved).
Trace `staging/toplink-reconciled/TL-M1-evidence/tl-m1-dmp-trace.md`; `git diff --check` PASS; secret scan
clean; `external_writes=0`; no milestone advanced._

_Claude TL-M2 profile-repair lease released 2026-07-30T16:45 ICT. Checkpoint: user signed §6
(`APPROVED 2026-07-30`); ran bounded field correction on DMP `profile.json` (channel→Facebook Page,
goal→độc lập 0 Thảo Tây, competitors→[], `_franchise_internal` INTERNAL/public gated). Backup
`profile.2026-07-30T19-26-29.json`, trace `staging/toplink-reconciled/TL-M2-profile/tl-m2-profile-repair-trace.md`,
digest-lock `docs Toplink/staging/run1/00-input-lock.json` (`profile_digest=a45e4ae4…`,
`source_digest=3ba91761…`). Read-back G1–G7 PASS; `git diff --check` PASS; secret/PII clean;
`external_writes=0`; `TL-GAP-011` RESOLVED; no milestone advanced._

_Extension review lease released 2026-07-30T18:50+07:00. Checkpoint: independent review aligned
ledger custody with `ACTIVE -> CHECKPOINTED -> ACTIVE` and made `ACTIVE|CHECKPOINTED` block
overlapping writers. Final parent checks: capability/live-ledger required content PASS; 10 JSON
blocks parse; 26 fences balanced; leakage and whitespace scans PASS. File is 424 lines._

_Extension implementation lease released 2026-07-30T18:34+07:00. Checkpoint: added §2.1
capability-aware routing and §5.0 copyable `🔒 Lock/Lease Ledger`; updated conformance checklist and
neutral example. Author checks: 10 JSON blocks parse, 26 fences balanced, required terms present,
portability leakage scan PASS. Custody transferred to independent review._

_Independent review lease released 2026-07-30T18:10+07:00. Checkpoint: reviewer fixed universal
record-field omissions, incomplete/contradictory state transitions, handoff acceptance/rejection
evidence, and the state-machine count. Final parent verification: 10 JSON blocks parse, 24 fences
balanced, required-section scan PASS, prohibited-term leakage scan PASS, two Claude/Codex mentions
are explicitly replaceable labels, whitespace/final-newline PASS. File is 373 lines / 32,868 bytes.
No existing operating contract was edited by this deliverable._

_Implementation lease released 2026-07-30T17:49+07:00. Checkpoint: standalone contract authored;
author checks report 9 JSON blocks parse, 22 fences balanced, terminology leakage scan PASS, and
`git diff --check` PASS. Custody transferred to independent review; no existing contract changed._

_Codex planning lease released 2026-07-30T17:20+07:00. Checkpoint: requirements converged in
`prd.md`; architecture and protocol boundaries recorded in `design.md`; ordered creation and
validation gates recorded in `implement.md`. Output file not created; implementation awaits the
user's explicit approval of the planning summary._

_Claude TL-M1 unblock Part 1 lease released 2026-07-30T16:05 ICT. Checkpoint: authored profile-repair
spec `docs/system/tl-m2-profile-repair-spec.md` (`TL-M2-PROFILE-REPAIR-001`, awaiting user sign-off);
recorded `TL-D12`–`TL-D15`; updated staging (page-identity/entity-franchise/health-compliance/input-gap
+ handoff hashes recomputed, all 5 MATCH); operational contract v0.1.1 (target `1s-Pm5f…8hms` + new-Toplink-SA
plan, no Thảo Tây credential); master plan v0.1.1; milestones v0.1.2. Verification: `git diff --check` PASS,
Page ID consistent across 7 files, secret/PII scan PASS (no SA key/JSON). No DMP profile mutation; DMP
trace `NONE`; `external_writes=0`; no milestone advancement._

_Claude TL-M1 input-contract repair lease released 2026-07-30T15:20 ICT (`TL-ISSUE-006`). Checkpoint:
bound every TL-M1 prerequisite to an exact path or `TL-GAP-*`; added `TL-GAP-010`–`TL-GAP-014`
(`012`–`014` = absent pre-migration/root artifacts, `MISSING_INPUT`, `NOT_MIGRATED_BY_DESIGN`);
milestones bumped to `0.1.1`; staging `source-inventory.md`/`input-gap-register.md` hashes recomputed
in the handoff. Verification: `rg` PASS (no unbound "root inventory/profile/history" prerequisite,
no "resolves to brand dossier"), `git diff --check` PASS, secret/PII scan PASS. DMP trace `NONE`;
`external_writes=0`; no milestone advancement._

_Claude TL-M1 evidence-staging lease released 2026-07-30T14:40 ICT; Codex Sheet-contract lease
released 2026-07-30T02:35:59+07:00. Relevant evidence/checkpoints are retained in `STATE.md` and
their staged artifact paths._

_Codex Trellis-spec bootstrap lease released 2026-07-30T03:55:43+07:00. Checkpoint: replaced all
templates in `.trellis/spec/{guides,backend,frontend}/` with source-backed project guidance and
checked all three bootstrap boxes in `.trellis/tasks/00-bootstrap-guidelines/prd.md`; no DMP or
external action, digest N/A. Verification: no placeholder matches; spec-index links resolve;
`task.py validate 00-bootstrap-guidelines` PASS (no JSONL files); `git diff --check` PASS._

## Next safe action

Gated next steps, in order:

1. ~~User signs §6 → Claude runs bounded DMP profile repair~~ **DONE 2026-07-30** (`TL-GAP-011` RESOLVED;
   trace `staging/toplink-reconciled/TL-M2-profile/tl-m2-profile-repair-trace.md`; digest-lock in
   `docs Toplink/staging/run1/00-input-lock.json`).
2. ~~Run TL-M1 DMP + PR verdict re-run~~ **DONE 2026-07-30.** 2 real DMP invocations
   (`switch-brand`+`import-guidelines`, 5 cat/52 rules, G5 lock held); PR Manager Review 2 verdict
   `NEEDS_HUMAN_REVIEW` (TL-REV-004/005→PASS). TL-M1 = `LOCAL_EVIDENCE_PASS · READY_FOR_CODEX_RECONCILIATION`
   (10/12 VERIFY PASS, #7 DEFERRED, #12 HELD) — see `staging/toplink-reconciled/TL-M1-evidence/tl-m1-closure-readiness.md`.
   TL-M1 **cannot be agent-closed**; remaining gates are Codex/user/human below.
3. ~~**Fresh Codex — final Phase B QA**~~ **DONE 2026-08-01.** Manifest SHA-256
   `48955606d3b2e91c9a5d984c7dc5ec22dcc4f895479a96a069ef372c3ac26427`.
4. **User (human owner) — APPROVE per-item legal/franchise/health gates:** franchise/legal proof
   (TL-GAP-002/009), health reviewer credential (TL-GAP-007), product dossier (TL-GAP-004), `11_Product_Yvien.md`
   (TL-GAP-010).
5. **User → Codex — Sheet:** SA infrastructure is ready; user supplies the exact signed
   `SheetTargetApproval` → Codex bounded upsert + exact read-back (TL-GAP-008).
6. Two-run Run 1/Run 2 package → only then TL-M1–M5 close together. TL-GAP-012–014 stay fail-closed.

Pre-migration/root artifacts stay fail-closed at `TL-GAP-012`–`TL-GAP-014`. Do not mark any milestone
`COMPLETE`/`APPROVED`. No mutation until the corresponding approval is signed.

## Carry-forward blockers

- Google Sheets target and Toplink SA infrastructure are ready, but write remains blocked pending
  a full signed `SheetTargetApproval` + bounded upsert + exact read-back.
  `TL-OUT-TL-M0-001` stays logical (`SYNC_PENDING_TARGET`). `TL-SHEET-001` v0.1.1 records the target,
  not a write approval.
- ~~DMP profile drift~~ **RESOLVED 2026-07-30** (`TL-GAP-011`): `toplink-y-vien` now reads back
  `Facebook Page` primary + independent Toplink goal (0 Thảo Tây/supporting), `competitors=[]`,
  franchisor relation INTERNAL-only. Digest-locked (`profile_digest=a45e4ae4…`). Profile usable for
  the next gated TL-M1 DMP run.
- Pre-migration/root source inventory, DMP profile snapshot, and decision/change history are absent
  from the standalone repo (`TL-GAP-012`–`TL-GAP-014`, `MISSING_INPUT`). No historical equivalence,
  full legacy reconciliation, or exact before/after profile claim until user/migration authority
  supplies them; reconstructed current-repo inventory is not a root/pre-migration inventory.
