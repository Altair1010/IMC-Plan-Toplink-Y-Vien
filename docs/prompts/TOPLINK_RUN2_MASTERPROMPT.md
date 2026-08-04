# TOPLINK_RUN2_FRESH_AUDIT_FINALIZE — fresh Claude master prompt

Execute this prompt in one genuinely fresh Claude Code context from the repository root. You are
the Claude Phase A auditor for `TOPLINK_RUN2_FRESH_AUDIT_FINALIZE`, covering the single
`TL-M1`–`TL-M5` package. Run 1 authoring is closed. Your job is an independent audit, real DMP
`check`, fresh Agency review, and a released handoff to a fresh Codex auditor. Do not create a new
marketing version, start TL-M6, or perform any external action.

## 1. Authority and fixed entry facts

Apply this precedence:

1. Current explicit user instruction and platform safety rules.
2. `AGENTS.md`, `RULES.md`, and `GOVERNANCE.md`.
3. `docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md` for strategy and scope.
4. `docs Toplink/TOPLINK_PAGE_MILESTONES.md` for sequence and Done gates.
5. `docs/system/claude-codex-operating-contract.md` for runtime ownership and handoff.
6. This prompt. If it conflicts with an authority above, stop only the affected action and record
   the conflict; do not silently reinterpret the contract.

Expected Run 1 lock:

```text
run_id         = TOPLINK_RUN1_BUILD
status         = RUN1_PASS · LOCAL_VERIFIED · PHASE_B_RECONCILED · NOT_MILESTONE_COMPLETE
manifest       = docs Toplink/staging/run1/run1-manifest.json
manifest_sha256= 99227153de577887966ae09124fdabcb2b3bf8ff23d838503531be507c2f4d2d
profile_digest = a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349
source_digest  = 3ba91761612ca482471dc1c071bd7e9d82e5708a3bb13ceb630fed476541fe76
DMP_version    = 3.15.1
active_brand   = toplink-y-vien
lease_released = true
external_writes= 0
```

Recompute and verify these values. Do not trust this prompt as proof. Any mismatch in manifest,
profile digest, source digest, DMP version, active brand, scope, or released lease means:

```text
FAIL_BACK_TO_RUN1
RUN2_NOT_STARTED
RUN3_FORBIDDEN
```

Persist the mismatch evidence, release any lease you acquired, and stop. Do not repair a lock
mismatch inside Run 2.

## 2. Fresh-context and blind-audit boundary

Before persisting the blind audit, read only what is needed to establish authority, the active
lease, the frozen inputs, and the artifact contract:

- `AGENTS.md`.
- `RULES.md`, `GOVERNANCE.md`, and `spec.md`.
- Only the current status and live lease sections of `STATE.md` and `task.md`; do not consume their
  historical Run 1 reasoning as audit guidance.
- `docs/system/toplink-knowledge-brief.md`.
- `docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md`.
- `docs Toplink/TOPLINK_PAGE_MILESTONES.md`, especially the common Done gates and Run 2 section.
- `docs/system/claude-codex-operating-contract.md`.
- `docs/system/capability-routing-matrix.md`.
- `docs Toplink/staging/run1/00-input-lock.json` and the exact frozen evidence paths it authorizes.
- From `docs Toplink/staging/run1/run1-manifest.json`, initially use only identity/lock fields and
  `generated_outputs[].{milestone,stable_id,path,sha256}` as the artifact contract. Do not use its
  review conclusions, dispositions, issue conclusions, or check verdicts to seed your audit.
- The 14 current generated artifacts named by that artifact contract.

Until `docs Toplink/staging/run2/claude/20-blind-audit.md` is written, do not read:

- `docs Toplink/staging/run1/30-delta-ledger.json`.
- `docs Toplink/staging/run1/40-workstream-reconciliation.md`.
- `docs Toplink/staging/run1/50-pillar-decision.md`.
- `docs Toplink/staging/run1/60-agency-review-register.md`.
- `docs Toplink/staging/run1/70-run1-checks.md`.
- Any Run 1 Claude/Codex handoff, Agency-review finding, closure reasoning, or detailed historical
  checkpoint under `staging/toplink-reconciled/**`, `task.md`, or `STATE.md`.

If this fresh context has already consumed those detailed findings, record
`FRESH_CONTEXT_ATTESTATION_FAIL` and stop. Do not pretend the audit is blind.

## 3. Scope, lease, and writable paths

After the entry locks pass, acquire the only active scoped lease in `task.md` with runtime,
concrete file set, ICT start time, and purpose. Hard-stop on an overlapping writer.

Claude Phase A may write only:

```text
docs Toplink/staging/run2/claude/00-fresh-context-attestation.json
docs Toplink/staging/run2/claude/10-source-ledger.md
docs Toplink/staging/run2/claude/20-blind-audit.md
docs Toplink/staging/run2/claude/30-dmp-check-trace.md
docs Toplink/staging/run2/claude/40-agency-review.md
docs Toplink/staging/run2/claude/50-post-blind-reconciliation.md
docs Toplink/staging/run2/claude/CLAUDE_TOPLINK_RUN2_PHASE_A_COMPLETE.json
docs Toplink/staging/run2/handoff-claude-to-codex.md
docs Toplink/staging/run2/handoff-envelope.json
task.md
STATE.md  # concise sprint mirror only when needed
```

Do not edit the 14 canonical Run 1 outputs during Claude Phase A. Findings and proposed repair
routes belong in Run 2 staging. Do not write to a Google Sheet, Facebook Page, DMP profile, public
channel, message endpoint, or any other external target. Do not create `_v2`, a competing plan, a
third run, or a Thảo Tây-linked artifact.

## 4. Record the fresh-context attestation

Create `00-fresh-context-attestation.json` before auditing content. Record at minimum:

- run ID and phase: `TOPLINK_RUN2_FRESH_AUDIT_FINALIZE` / `CLAUDE_PHASE_A`;
- timestamp in ICT and runtime identity;
- exact files read before the blind audit;
- explicit list of prohibited Run 1 reasoning files not yet read;
- manifest/profile/source/DMP/active-brand read-backs and verification results;
- active lease result;
- `external_writes=0`;
- attestation verdict: `PASS` or `FAIL`.

## 5. Build the source ledger

Write `10-source-ledger.md`. For every material fact or claim used by the artifacts, record:

| Statement or claim ID | Source path/location | Evidence status | Allowed use | Missing proof or human gate |
|---|---|---|---|---|

Use only:

- `TOPLINK_CONFIRMED` for the source's exact meaning;
- `INFERENCE` for bounded reasoning with a validation path;
- `HYPOTHESIS` for unmeasured audience, positioning, pillar, KPI, or performance proposals;
- `MISSING_INPUT`, `UNVERIFIED`, or `DO_NOT_USE` when public support is absent.

Keep Page identity, offer readiness, public franchise/legal wording, product/service facts,
qualification, price, availability, booking/contact, testimonial/UGC consent, asset rights, and
Sheet permission fail-closed unless the frozen source set directly verifies them. Never import a
Thảo Tây brand fact, identifier, credential, target, baseline, deliverable, or milestone.

## 6. Perform and persist the independent blind audit

Audit the 14 artifacts directly against the canonical contract and frozen evidence. Persist all
findings to `20-blind-audit.md` before reading any prohibited Run 1 reasoning.

Audit at least these axes:

1. **Evidence and entity:** source status, allowed use, Toplink-only isolation, entity/franchise
   boundaries, Page identity, founder role, and no invented facts.
2. **Audience and positioning:** hypotheses remain labelled; Hanoi service-discovery versus
   nationwide education boundary; no unsupported persona or measured-insight claim.
3. **Pillars and Facebook strategy:** 3–5 pillars total 100%; Facebook Page remains primary;
   Reels support discovery; TikTok is mechanics-only.
4. **Campaign and KPI:** relative four-week architecture, greenfield logic, no percentage growth
   from zero, explicit metric/formula/source/owner/cadence, and held offer/scale gates.
5. **Calendar and production:** 28 unique D1–D28 identities, A/B/C options for each day, capacity
   fit, 28 production records, Facebook-first Reels, stable references, asset/consent states, and
   no fabricated hard date.
6. **Claim safety:** no diagnosis, treatment, cure, prevention, guarantee, medical replacement,
   universal result, unsupported efficacy, or disclaimer-laundered claim. Classify every material
   public claim as `ALLOWABLE_WITH_SOURCE`, `REWRITE_REQUIRED`, `NEEDS_HUMAN_REVIEW`, or `BLOCKED`.
7. **Privacy and approvals:** consent, PII minimization, content hash/revision reset, no
   null-to-approved default, no agent-created `APPROVED`, and no publish-ready state without the
   item-level gate.
8. **Integrity:** stable IDs, cross-file references, Unicode, placeholders, secrets/private keys,
   unnecessary PII, and scope drift.

For each finding record:

```text
finding_id
severity = minor | major | critical
classification = evidence | entity | strategy | claim | privacy | schema | runtime
artifact_path + exact location
evidence_path + exact location
observed problem
required result
allowed route = DIRECT_REPAIR | DMP_SKILL_REAUTHOR | HUMAN_GATE | FAIL_BACK_TO_RUN1
status = OPEN | NO_FINDING
```

Do not repair or reauthor the canonical artifacts in this phase. A lack of findings must be an
evidence-backed result, not an assumed PASS.

## 7. Run real DMP checks

After the blind audit is persisted, run the actual installed DMP `check` capability on every
health-sensitive/public-facing artifact and any additional file implicated by a finding. This is
a check run, not a substitute for an authoring invocation and not permission to mutate the active
brand profile.

At minimum capture in `30-dmp-check-trace.md`:

- trace ID and ICT timestamp;
- DMP version and active-brand read-back;
- exact input paths and SHA-256 digests;
- exact raw output paths and SHA-256 digests;
- check dimensions and any legitimately skipped dimension with a reason;
- exit status and finding IDs;
- `external_writes=0`.

`NO_TRACE = NOT_DONE`. `SKIPPED` is never `PASS`. A required reauthoring recommendation must name
the correct DMP capability, but Claude Phase A must not silently generate a competing artifact.

## 8. Coordinate fresh Agency reviews

Record fresh reviews in `40-agency-review.md`; do not reuse a Run 1 verdict as a Run 2 verdict.
Route by workstream:

| Workstream | Review route |
|---|---|
| Evidence/entity/public reputation | PR Manager |
| Audience/positioning/campaign/KPI | Social Strategist → Growth Hacker |
| Pillars/calendar/production/copy | Content Creator → PR Manager |
| Reels mechanics | Short-Video Coach → TikTok Strategist |
| Health/legal/privacy/approval | PR Manager → named human/professional gate |

Use no more than three Agency reviewers on one workstream. Reviewers audit; they do not create
competing versions. Record `PASS`, `FAIL`, `NEEDS_HUMAN_REVIEW`, or `SKIPPED` with evidence and
required action. The highest agent state is `REVIEWED` or `NEEDS_HUMAN_REVIEW`; no agent may grant
human `APPROVED`.

## 9. Reconcile only after the blind pass is frozen

Once `20-blind-audit.md` is persisted with its digest, you may read the withheld Run 1 reasoning,
review registers, checks, and handoffs. Write `50-post-blind-reconciliation.md` containing:

- the pre-read blind-audit SHA-256;
- each Claude Run 2 finding matched to Run 1 as `AGREES`, `NEW`, `CONTRADICTS`, or
  `RUN1_ONLY_REVALIDATED`;
- evidence deciding each contradiction;
- a stable merged issue ID and allowed repair route;
- unresolved human gates and their owner;
- exact constraints for the fresh Codex recipient.

Do not erase a Run 1 blocker merely because the new audit did not rediscover it. Do not upgrade a
finding on model confidence alone.

## 10. Handoff to fresh Codex

Instantiate:

- `docs/system/templates/handoff-claude-to-codex.template.md` as
  `docs Toplink/staging/run2/handoff-claude-to-codex.md`;
- `docs/system/templates/handoff-envelope.template.json` as
  `docs Toplink/staging/run2/handoff-envelope.json`.

The JSON envelope must set:

```text
project                      = toplink-y-vien
run                          = TOPLINK_RUN2_FRESH_AUDIT_FINALIZE
stage                        = claude_to_codex
prepared_by                  = Claude Code
recipient                    = Codex CLI
lease_status                 = RELEASED  # only after the release checkpoint
read_after_independent_audit = true
sheet target/action          = no write unless a separate exact SheetTargetApproval exists
```

Prepare the final handoff, completion marker, checkpoint, and `task.md` lease release, then apply
them as one final atomic local change. After that change succeeds, perform no further write to the
released file set. This is the evidence basis for `lease_status=RELEASED` in the envelope.

Include exact paths/digests, DMP trace, reviewer results, stable finding IDs, human gates, allowed
next action, and forbidden actions. The next actor is a **fresh Codex context** that must perform
and persist its own blind audit before reading Claude findings.

Create `CLAUDE_TOPLINK_RUN2_PHASE_A_COMPLETE.json` only when the attestation, blind audit, real DMP
check, fresh Agency review, post-blind reconciliation, handoff files, digests, and local QA all
exist. Its maximum verdict is:

```text
CLAUDE_RUN2_PHASE_A_HANDOFF_READY
```

It must never say `RUN2_PASS`, milestone `COMPLETE`, human `APPROVED`, published, or synced.

## 11. Verification and stop conditions

Before handoff, verify:

- JSON parses; every declared path exists; every declared SHA-256 reads back exactly.
- The Run 1 lock values still match.
- Blind-audit digest predates access to detailed Run 1 reasoning.
- Required DMP check trace and fresh review evidence exist.
- All finding IDs and references resolve; no orphan or duplicate stable ID exists.
- UTF-8, final newlines, placeholders, secrets/private keys, unnecessary PII, isolation, and
  `git diff --check` pass.
- Canonical Run 1 outputs are byte-unchanged by Claude Phase A.
- `external_writes=0`; no Page/Sheet/publish/profile mutation occurred.

Stop with an evidence-backed blocker if there is an overlapping lease, lock drift, source conflict,
missing required check, fake/skipped trace presented as PASS, prohibited claim, secret/PII leak, or
unclear authority. A third macro-run is forbidden.

## 12. Checkpoint, release, and final report

At each meaningful step, checkpoint evidence in `task.md`. At completion:

1. Stop writing the leased file set.
2. Record paths, digests, verdicts, open findings, human gates, Sheet state, `external_writes=0`, and
   the fresh Codex next action.
3. Release the lease in `task.md`; mirror only the concise sprint fact in `STATE.md` if needed.
4. Report one of:

```text
CLAUDE_RUN2_PHASE_A_HANDOFF_READY
BLOCKED_ENTRY_GATE
FAIL_BACK_TO_RUN1
```

Report artifacts, provenance status, DMP trace state, Agency verdicts, open human gates, and Sheet
state. Do not open TL-M6. Do not claim the TL-M1–TL-M5 package is complete: fresh Codex Phase B,
paired-manifest validation, and the applicable exact Sheet read-back remain separate gates.
