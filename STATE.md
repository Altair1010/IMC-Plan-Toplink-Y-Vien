# STATE.md — loop state tracker (Toplink Y Viện)

> Sprint-level truth only. Read this before `task.md`; it never overrides a canonical source.

## Sprint goals

- Operate the independent Toplink scaffold with explicit lease/handoff and two-run controls.
- Keep `TL-PMP-001` and `TL-MS-001` `PLAN_LOCKED` until their canonical readiness gates permit
  execution.

## In-progress

- Task `.trellis/tasks/08-04-toplink-sheet-model-correction` is active under a Codex recovery lease.
  The approved 24-dataset correction completed create/clear/write/format across 24 tabs, then
  fail-closed at native verification because Google quantized one header RGB channel by one code.
  Persisted state is `VERIFY_FAILED · RECOVERY_APPROVAL_PENDING`; automatic rollback is forbidden.
  A read-only audit now matches values/formulas/native rules 24/24 and preserves `Trang tính1`, but
  success cannot be promoted until the zero-mutation `EXACT_READBACK_ONLY` recovery bundle receives
  a new exact digest-bound human approval. Historical V2 evidence remains immutable and classified
  `TECHNICAL_READBACK_PASS · BUSINESS_MODEL_FAILED`; no Run 3 or milestone advance is permitted.
- Task `.trellis/tasks/08-04-toplink-sheet-sync` is ready to close; no active writer lease. Signed V2
  execution is closed and post-sync review PASS; later mutations need new approval.
- Run 2 Phase B `CODEX_RUN2_PHASEB_LOCAL_VERIFIED · NOT_COMPLETE`: Codex blind audit frozen
  `f56264b3…` before Claude read; locks and 14/14 handoff outputs matched; merged 10 findings; targeted
  repairs changed 7/14 outputs and left 7/14 byte-identical. Post-repair reference and safety gates PASS;
  paired manifest PASS at `a4e6de75…c86e939`. Disclaimer final wording and founder D24–D28 choice remain
  human gates. Sheet target metadata is now read-only verified: target accessible, only default tab
  `Trang tính1` exists, and the Toplink service-account identity matches the local key. Contract
  `TL-SHEET-001` v0.1.3 now binds deterministic payload
  `docs Toplink/staging/run2/codex/61-sheet-payload-v2.json` (`64e9c656…4267b3`) to unsigned envelope
  `62-sheet-target-approval-v2.json` (`ebe7490b…5d1336`). Fresh `trellis-check` review PASS (11/11
  tests); exact scope/range/schema/limit drift is rejected before credential or network access.
  Human signed exact V2 digest; bounded execution created/upserted 14 registered tabs and exact
  read-back passed 14/14 with zero mismatches. Evidence `63-sheet-readback-v2.json` SHA-256
  `be0e0efc…caa719`; independent live read-only recheck `de97ce38…5edfaa` confirmed 15 total sheets,
  14 Toplink tabs, `Trang tính1` preserved, 14 frozen-header states and zero range mismatches. Reconciled
  Run 2 manifest `50756122…2c72c712`. Sheet is `SYNC_READBACK_PASS`; 29 bounded mutation API calls were
  recorded. Non-Sheet human gates remain open, so final status is still `NOT_COMPLETE`; no milestone
  advance.
- Run 2 Phase A (fresh Claude blind audit) `CLAUDE_RUN2_PHASE_A_HANDOFF_READY`: attestation PASS,
  locks ALL_MATCH, 14/14 canonical byte-unchanged, blind audit frozen (`8625ceed…`) before withheld
  reads, real DMP check clean (0 auto-reject/critical/hard-claim), fresh Agency 4/4 (Social PASS · PR/
  Short-Video NEEDS_HUMAN_REVIEW · Content FAIL on CL-P2). Findings 0 critical / 2 major (`TL-R2-F02`
  CL-P2 orphan, `TL-R2-F08` disclaimer canonical host absent) / 6 minor — all DIRECT_REPAIR or bounded
  HUMAN_GATE. `external_writes=0`; Sheet `SYNC_PENDING_TARGET`; milestone_advance=false. Next: fresh
  Codex Phase B (own blind audit first) at `docs Toplink/staging/run2/`.

## Run 1 Phase B final reconciliation — checkpoint 2026-08-04

- Verdict: `RUN1_PASS · LOCAL_VERIFIED · PHASE_B_RECONCILED · NOT_MILESTONE_COMPLETE`.
- Claude handoff accepted after exact profile/source/version/active-brand, path, hash, real-invocation,
  approval-state and zero-external-write verification. Locks: profile `a45e4ae4…c8cbe349`; source
  `3ba91761…541fe76` with 5/5 member hashes; DMP `3.15.1`; active brand `toplink-y-vien`.
- Reconciled 14/14 generated outputs, 24/24 delta IDs/dispositions and 11 real trace rows covering
  TL-M1–TL-M5. Nine M2–M5 authoring sidecars/raw hashes match; evaluator evidence remains separate
  `check`. `TL-PILLARS-001` is the sole `REGENERATE`; the other 13 outputs are `KEEP`.
- TL-M5: five canonical deliverables; 28/28 unique relative calendar identities with A/B/C; 28/28
  production records; 12 Facebook-first Reels; `TL_CONTENT_CALENDAR`, `TL_REELS_PRODUCTION`, and
  `TL_WORKFLOW_APPROVAL` integrated. Health/legal/privacy/consent/asset-rights gates remain fail-closed.
- JSON/schema/path/hash/reference/orphan/UTF-8/newline/placeholder/secret/private-key/PII/isolation/
  whitespace checks PASS. Manifest: `docs Toplink/staging/run1/run1-manifest.json`; SHA-256
  `99227153de577887966ae09124fdabcb2b3bf8ff23d838503531be507c2f4d2d`.
- `external_writes=0`; `milestone_advance=false`; Sheet `SYNC_PENDING_TARGET`; no milestone `COMPLETE`,
  no human `APPROVED`, no Sheet/Page/publish mutation, and Run 2 not started.
- Remaining gates are milestone-level only: human/professional health review, public-positioning,
  franchise/legal/product/privacy/consent/asset-rights evidence, signed Sheet approval/read-back, then
  the fresh `TOPLINK_RUN2_FRESH_AUDIT_FINALIZE` entry gate.

## Phase A real-authoring repair — checkpoint 2026-08-04

- Repaired the four confirmed blockers `TL-R1-BLK-DMP-CAPABILITY-001`, `TL-R1-BLK-DMP-RAW-EVIDENCE-001`,
  `TL-R1-BLK-DMP-AUTOREJECT-001`, `TL-R1-BLK-HANDOFF-DIGEST-001`. Governed definition (human owner
  2026-08-03): **DMP authoring-subagent dispatch = real native authoring invocation**; evaluator scripts
  = `check` only.
- 9 real authoring invocations across TL-M2–TL-M5 (brand-setup non-mutating, audience-intelligence,
  campaign-plan ×2, social-strategy ×2, content-calendar, content-engine, video-script). Each has raw
  output + `.invocation.json` metadata + SHA-256 under `staging/toplink-reconciled/**/raw-repair/`.
- 1 canonical changed: `content-pillars.md` `451425c1…` → **`b0790e2d…`** (REGENERATE; auto-reject
  genuinely cleared, composite 32→92, `auto_rejected` true→false). 13 deliverables KEEP byte-unchanged.
- Separate DMP check on all 14 deliverables: `auto_rejected=false`, 0 critical (raw JSON in
  `raw-repair/check/`). Agency verdicts re-confirmed `PASS` structural + `NEEDS_HUMAN_REVIEW` on
  health/founder/product/positioning. No `APPROVED`.
- Synced digests (blocker HANDOFF-DIGEST): M2–M4 trace `b63c2601…` / review `d6006af9…` / marker
  `a5040677…` / handoff `80dd87f8…`; M5 trace `99338576…` / review `c8390a46…` / marker `8dcf90e5…` /
  handoff `2c781814…`; envelope refreshed. Stale `d00a6489…`/`aa6eab89…`/`b58ea051…`/`6fc58784…` no
  longer referenced by active artifacts.
- `external_writes=0`; `milestone_advanced=false`; no Sheet/Page/publish; Run 1 open; no Run 2. Next
  actor: Codex Phase B (reconcile manifest `dmp_traces[]` off SCAFFOLD, add TL-M5, record content-pillars
  `b0790e2d…`).

## Blocked

- ~~`BLOCKED_WORKTREE_OWNERSHIP`~~ **CLEARED 2026-08-03 FOR TL-M5 PHASE A** by explicit human
  exclusion. P1 `00-bootstrap-guidelines` files remain untouched; the nine-path TL-M5 scope has
  zero overlap.
- `TL-GAP-006` and `TL-M5-ASSET-RIGHTS-001` are **BOUNDED 2026-08-03 FOR TL-M5 PHASE A**: calendar
  stays relative `D-1..D-28`; supplied capacity is about 3 videos/week and at least 7 total
  items/week; real assets are placeholder-brief-only until rights clearance. The unset hard start
  date remains a TL-M6/hard-dated scheduling gate.
- ~~`TL-SOURCE-LOCK-STATUS-001`~~ **CLEARED 2026-08-03 BY DIRECTION A**: the milestone file owns
  current status; `TOPLINK_PAGE_MASTER_PLAN.md` remains the unchanged frozen strategy snapshot.
- `TL-GAP-010` is **BOUNDED_FAIL_CLOSED 2026-08-03 FOR TL-M5 PHASE A**:
  `docs Toplink/11_Product_Yvien.md` stays `UNVERIFIED`; only customer-experience framing is
  allowed, with no direct product/efficacy claim.
- ~~`TL-R1-ISSUE-QA-001` aggregate QA wrapper blocker~~ **RESOLVED 2026-08-01**. Fresh Codex
  completed schema/reference/orphan/digest/UTF-8/placeholder/secret/PII/isolation/whitespace and
  `git diff --check`; one trailing space in `task.md` was repaired. Final manifest SHA-256:
  `48955606d3b2e91c9a5d984c7dc5ec22dcc4f895479a96a069ef372c3ac26427`.
  Status: `RUN1 · LOCAL_VERIFIED · PHASE_B_RECONCILED · NOT_COMPLETE`.
- ~~DMP profile drift~~ **RESOLVED 2026-07-30** (`TL-GAP-011`). User signed §6; Claude ran the bounded
  field repair (backup → correction → read-back). Profile now reads `primary_channel=Facebook Page`,
  independent Toplink goal (0 Thảo Tây/supporting), `competitors=[]`, franchisor relation INTERNAL-only
  (public gated `TL-GAP-002`). `external_writes=0`; no milestone advanced. See
  `staging/toplink-reconciled/TL-M2-profile/tl-m2-profile-repair-trace.md`.
- Public franchise/legal proof: user attests the document exists but it is not in hand → still
  unverified. No public franchise/legal wording (`TL-GAP-002`/`TL-GAP-009`).
- Product/service dossiers, offer, booking/contact/privacy, price/availability, and qualification
  evidence still `MISSING_INPUT` (added gradually from `docs Toplink/`).
- Content start date and production capacity.
- Google Sheets target and dedicated service-account identity are verified. The V2 approval was
  consumed by the completed 14-tab delivery and cannot authorize correction. The 24-dataset in-place
  migration requires a new digest-bound approval (tabs/ranges/schemas/actions/limits/expiry) and
  24/24 exact read-back. `TL-SHEET-001` records the target; it is not a new write approval.
  **UPDATE 2026-07-30 (TL-D19): SA infrastructure READY** — SA `yvien-sheet-writer@imcforyvien.iam.gserviceaccount.com`
  created, Sheet shared Editor, Sheets API enabled, key at gitignored `.secrets/imcforyvien-de7e7ee958f4.json`,
  `GOOGLE_APPLICATION_CREDENTIALS` set (user-confirmed). **Still gated for WRITE:** signed `SheetTargetApproval`
  + Codex bounded upsert + exact read-back. SA ready ≠ write done.

## Next safe action

1. Codex completes local governance, schema/compiler, normalized sidecars, and independent review.
2. Codex prepares and commits unsigned `TL-SHEET-RUN2-CORRECTION-01`; `external_writes=0`.
3. Human supplies an exact `APPROVED` statement bound to that path and SHA-256; only then may Codex
   run the bounded in-place correction and 24/24 exact read-back.
4. Health/legal/franchise/product/privacy/consent/asset-rights gates remain open. Never create Run 3.

## Resolved-by-user (2026-07-30)

- Page identity (`TL-GAP-001`): Page ID `61591880797654`, baseline = task start, follower 0, greenfield.
- Health reviewer (`TL-GAP-007`): user + teacher, user-attested; per-item publish approval still required.
- [TL-D16] Franchise/legal (`TL-GAP-002`/`TL-GAP-009`): **user decision = KEEP LOCKED** (fail-closed).
  No public franchise/legal wording until a real document is supplied + verified. Status stays
  `PUBLIC_BRAND_RELATIONSHIP_PENDING_DOCUMENT` / `LEGAL_SCOPE_PENDING` by explicit choice.
- [TL-D17] Health professional accountability (`TL-GAP-007`): user names **"Thảo Tây" (teacher, as a
  person) + "Guru" (user, minhkhang.guru)** as the persons responsible for each health-sensitive post.
  Still **user-attested** (no formal credential filed) and **per-item publish approval remains mandatory**
  (TL-M5/M6). NOTE: this is person-level accountability only — it does NOT relink any Thảo Tây *brand*
  fact/goal/identifier into Toplink; cross-brand isolation unchanged.
- [TL-D18] Product/service dossier (`TL-GAP-004`/`TL-GAP-010`): user will supply later, **with full legal
  certifications + inspection/kiểm định**. Until then claims stay `UNVERIFIED` + "hỗ trợ" framing.
- [TL-D19] Toplink Sheet service account (`TL-GAP-008`): SA email **`yvien-sheet-writer@imcforyvien.iam.gserviceaccount.com`**
  (project `imcforyvien`) provided by user. Private key file **secured** at gitignored
  `.secrets/imcforyvien-de7e7ee958f4.json` (moved out of `docs Toplink/`; never commit). **Still required
  before any write:** user confirms (a) Sheet `1s-Pm5f…8hms` shared with SA as Editor, (b) Google Sheets API
  enabled on `imcforyvien`, (c) `GOOGLE_APPLICATION_CREDENTIALS` points to the `.secrets/` key; then a signed
  `SheetTargetApproval` + Codex bounded upsert + exact read-back. Email recorded ≠ write approval.
- [TL-D20] Pre-migration/root artifacts (`TL-GAP-012`–`TL-GAP-014`): source located in origin project
  `F:\Codex\IMC Plan - Thảo Tây`. **Bounded provenance-only extract DONE 2026-07-30** (user scope) →
  `staging/toplink-reconciled/TL-M1-evidence/root-provenance-map.md`. Gaps → `PROVENANCE_LOCATED`
  (digest-locked). **Key finding:** the repaired "drift" was the **original design** — origin
  `dmp-profiles.md §2` labels toplink-y-vien "(SUPPORTING)"; the move to independent Toplink was a
  deliberate user re-scope (spec §6), not a bug fix. Before/after now documentable via real digests.
  Origin repo not mutated; 0 Thảo Tây brand fact/credential/Sheet baseline imported.

## Completed this session

- [2026-08-03] **Run 1 DMP-trace repair by Claude — real DMP invocations replace scaffold; RUN1 NOT
  COMPLETE.** Fixed `TL-R1-BLK-DMP-M2-001`, `TL-R1-BLK-DMP-M3M4-001`, `TL-R1-BLK-DMP-M5-001`,
  `TL-R1-BLK-HANDOFF-JSON-001`. Ran **real deterministic DMP scripts** (`eval-runner.py --action run-full
  --brand toplink-y-vien`, `hallucination-detector.py --action detect`, `claim-verifier.py
  extract-claims`; Python 3.11.15; plugin `neels-plugins/digital-marketing-pro/3.15.1`) over all 14
  M2–M5 deliverables, exit 0 each, `logged=false` ⇒ `external_writes=0`. Finding: **0 CRITICAL
  hallucination flags on all 14**; low composites (content-pillars 32/auto-reject = spec-mandated pillar
  weights false-positive, reels-briefs 44, fb-strategy 52) are generic-scorer false-positives on internal
  design numerics + governed support-language; `claim-verifier` total_claims=0; no fabricated fact. All 14
  deliverable digests re-confirmed **byte-unchanged** (`0d2d2d16…`,`435969cf…`,`51b18d91…`,`42cb8e7d…`,
  `651dff61…` M5; `2a151493…`…`40a528c6…` M2–M4). Rewrote traces off `VERIFIED_REAL_INVOKE_SCAFFOLD`:
  `TL-M2-M4-run1/{dmp-trace.md `fd1ae240…`,marker `df6d3bc7…`,handoff `8a4a186b…`}`;
  `TL-M5-run1/{dmp-trace.md `b58ea051…`,agency-review `6fc58784…`,marker `630be861…`,handoff `a4102833…`}`;
  created `TL-M5-run1/handoff-envelope.json`. QA PASS: JSON 4/4, UTF-8+newline 8/8, `git diff --check` 0,
  placeholder/secret/PII CLEAN, 0 self-`APPROVED`, prohibited-claim/CTA negation-only, Thảo Tây=1
  person-level TL-D17 ref. Profile `a45e4ae4…` G5 held (no brand-setup/import-guidelines re-run), source
  `3ba91761…` 5/5, DMP `3.15.1`, active brand `toplink-y-vien`. Did NOT touch input lock, canonical
  outputs, Phase B manifest/10–70, P1 files, `11_Product_Yvien.md`. `external_writes=0`;
  `milestone_advanced=false`; no `APPROVED`/publish; Run 1 open; no Run 2. Next: Codex Phase B reconcile
  manifest `dmp_traces[]` statuses + add TL-M5.
- [2026-08-03] **TL-M5 Run 1 Phase A built by Claude (DMP raw authoring, local-only) — LOCAL_VERIFIED,
  NOT COMPLETE.** Entry gate PASS (`READY_FOR_CLAUDE_TL_M5_PHASE_A`); preflight exact: profile
  `a45e4ae4…c8cbe349`, source `3ba91761…541fe76` 5/5, DMP `3.15.1`, active brand `toplink-y-vien`.
  Real invocations `TL-M5-INV-01..04` (`content-calendar`/`content-engine`/`video-script`/`check`).
  5 canonical deliverables in `docs Toplink/content/`: `month-calendar.md` (`0d2d2d16…`, 28 relative
  items `D-1..D-28`, A/B/C, pillar 6/6/8/4/4=28, 12 Reels), `asset-and-batch-plan.md` (`435969cf…`,
  placeholder-only direction B), `reels-briefs.md` (`51b18d91…`, Facebook-first, TikTok mechanics-only),
  `production-briefs.md` (`42cb8e7d…`, full field + measurement), `workflow-approval-measurement.md`
  (`651dff61…`, approval ledger hash/revision, material-edit reset). Staging `TL-M5-run1/`: `dmp-trace.md`
  (`d00a6489…`, source ledger + 4 traces), `agency-review.md` (`aa6eab89…`, safety ledger),
  `CLAUDE_TOPLINK_RUN1_PHASE_A_COMPLETE.json`, `handoff-claude-to-codex-phaseA.md`. CTA follow/save/share
  only; 10 health items + founder/product-adjacent/positioning → `NEEDS_HUMAN_REVIEW` + disclaimer §3.3;
  franchise/legal + generalized testimonial + diagnosis/cure/guarantee `BLOCKED` (not used). DMP check 8/8
  PASS + 1 documented SKIP. Did not touch input lock, M2–M4 outputs, Phase B manifest, P1 files, or
  `11_Product_Yvien.md`. `external_writes=0`; `milestone_advanced=false`; no `APPROVED`/publish; Run 1 open;
  no Run 2. Next: Codex Run 1 Phase B reconcile TL-M5 into manifest.
- [2026-08-03] **TL-M5 Run 1 input lock and readiness re-issued; no milestone advancement.** Runtime
  preflight read back exact: profile `a45e4ae4…c8cbe349`, frozen source `3ba91761…541fe76` 5/5,
  DMP `3.15.1`, active brand `toplink-y-vien`, and pre-extension manifest
  `48955606…3ac26427` with 22/22 referenced digests. Added the six-value human-input block to
  `docs Toplink/staging/run1/00-input-lock.json` (`07a3b7c1…c2d1b32`; block
  `809a94dd…83c4274`) and re-issued
  `docs Toplink/staging/run1/codex-to-claude-tl-m5-readiness.md` (`e5b16890…b42be8a0`), verdict
  `READY_FOR_CLAUDE_TL_M5_PHASE_A`. `TL-GAP-006` and asset rights are bounded; P1 ownership and
  source-status direction are cleared; `TL-GAP-010` remains fail-closed. Manifest final untouched;
  Run 1 remains open. `external_writes=0`; `milestone_advanced=false`; next actor Claude.
- [2026-08-03] **Codex pre-TL-M5 reconciliation checkpointed.** Classified every tracked/untracked
  change without reset/clean/restore/stash; validated/committed the standalone multi-agent contract
  and archived its Trellis task; committed nine manifest-verified M2–M4 local artifacts and the
  Sheet-governance group. Canonical milestones v0.1.3 now reflect TL-M0 real readiness, resolved
  profile drift, target/SA-ready-but-no-write status, unverified `11_Product_Yvien.md`, and
  fail-closed TL-GAP-012–014. Runtime locks and the Run 1 manifest digest read back exact. Readiness
  report: `docs Toplink/staging/run1/codex-to-claude-tl-m5-readiness.md`. Verdict:
  `BLOCKED_PRE_TL_M5`; no milestone advanced and Run 1 remains open.
- [2026-08-01] **Fresh Codex final Phase B QA PASS.** Resolved `TL-R1-ISSUE-QA-001`; verified
  marker/profile/source/DMP/active-brand locks, 9/9 generated digests, manifest schema,
  stable-ID/disposition/reference/orphan integrity, required paths, 5 pillars=100%, UTF-8,
  placeholders, secrets/PII, isolation, whitespace and `git diff --check`. Updated
  `70-run1-checks.md` and `run1-manifest.json`; manifest SHA-256
  `48955606d3b2e91c9a5d984c7dc5ec22dcc4f895479a96a069ef372c3ac26427`.
  `external_writes=0`; `milestone_advance=false`; no COMPLETE/APPROVED, Sheet/Page/publish,
  Run 2 or Run 3.
- [2026-08-01] **TL-M2→TL-M4 Run 1 Phase A built (DMP raw-authoring, local-only) — LOCAL_VERIFIED, NOT
  COMPLETE.** Ran the M2→M4 masterprompt. 9 deliverables: TL-M2 `docs Toplink/brand/dmp-profile.md` +
  `docs Toplink/system/runtime-compatibility.md` (field-layer map, no profile mutation); TL-M3
  `research/audience-hypotheses.md` (TL-A01–A04 kept, A02 split; all hypothesis-labeled),
  `brand/positioning.md` + `narrative.md` + `content-pillars.md` (5 pillars = 100%) +
  `facebook-page-strategy.md`; TL-M4 `brand/campaign-architecture.md` (relative D-1..D-28, 1–2/day,
  W4=SAFE FALLBACK default) + `kpi-experiment-plan.md` (counts=0/rates=N/A, no % from zero). DMP 3.15.1,
  active brand `toplink-y-vien`, 4 skills invoked (audience-intelligence/campaign-plan/social-strategy/
  content-engine). Trace + agency-review (PASS structural; NEEDS_HUMAN_REVIEW on health TL-P2/P4+W2 and
  public positioning) + `CLAUDE_TOPLINK_RUN1_PHASE_A_COMPLETE.json` + handoff addendum in
  `staging/toplink-reconciled/TL-M2-M4-run1/`. Checks: G5 profile lock HELD (`a45e4ae4…` unchanged),
  5/5 source digests MATCH, isolation 0 external-brand refs, secret/PII 0, `git diff --check` PASS.
  `external_writes=0`; no Sheet/Page/publish; no milestone COMPLETE/APPROVED; Codex Phase B files
  untouched. Next: Codex Run 1 Phase B reconciliation (reconcile M2–M4 into `staging/run1/10..70` +
  `run1-manifest.json`), then human gates + Sheet + two-run close.


- [2026-07-29] **Scaffold regeneration PASS.** Added standalone Claude ↔ Codex contract, lease/
  handoff/manifest templates, Toplink Run 1/Run 2 prompts, deterministic delivery loop, lifecycle
  controls, and cross-linked read order.
- [2026-07-29] Static checks passed: JSON templates, referenced paths, prompt/core-rule contract,
  cross-brand isolation, staged secret scan, and `git diff --check`. No DMP invocation, Page
  mutation, Sheet write, publishing, or external-runtime mutation occurred.
- [2026-07-30] **TL-M0 DMP invocation trace `VERIFIED_REAL_INVOKE`.** Claude→Codex trace and all
  five declared artifact digests match; `external_writes=0` and `TL-OUT-TL-M0-001` is logical-only.
  Codex control-plane audit found DMP profile drift, so TL-M0 is not promoted. See
  `staging/toplink-reconciled/TL-M0-readiness/codex-tl-m0-verification.md`.
- [2026-07-30] **TL-M1 evidence staging built (DMP-independent); DMP trace blocked.** Source
  manifest, entity/franchise/allowed-use map, Page-identity gate, health/compliance taxonomy,
  input-gap register (TL-GAP-001..011), PR Manager review (`NEEDS_HUMAN_REVIEW`), and Claude→Codex
  handoff staged at `staging/toplink-reconciled/TL-M1-evidence/`. `brand-setup`/`import-guidelines`
  both mutate the drifted profile with no dry-run mode ⇒ `BLOCKED_DMP_PROFILE_MUTATION`, no trace
  simulated. `external_writes=0`. TL-M1 not COMPLETE; awaiting Codex reconciliation + TL-M2 repair.
- [2026-07-30] **TL-SHEET-001 planned and scaffold-linked.** Added an independent Toplink tab
  registry, approval/delivery contracts, validation matrix, and read-back tests in
  `docs/system/toplink-google-sheets-operational-contract.md`; canonical plan, milestones, rules,
  runtime contract/routing, and handoff templates now reference it. No workbook/tab/connector was
  created or changed.
- [2026-07-30] **TL-M1 input-contract repair (`TL-ISSUE-006`); no milestone advancement.** Bound
  every TL-M1 prerequisite to an exact path or a `TL-GAP-*` ID in `TOPLINK_PAGE_MILESTONES.md`
  (Inputs/Work step 0/VERIFY; version `0.1.1`). The three absent pre-migration/root artifacts
  (source inventory, DMP profile snapshot, decision/change history) are now `TL-GAP-012`–`TL-GAP-014`
  (`MISSING_INPUT`, cause `NOT_MIGRATED_BY_DESIGN`), no longer resolved to the brand dossier or
  governance files; blocker register and staging gap register synced (`TL-GAP-010`–`TL-GAP-014`).
  Staging `source-inventory.md`/`input-gap-register.md` hashes recomputed in the handoff. DMP trace
  stays `NONE/BLOCKED`; `external_writes=0`; no DMP/Sheet/Page/runtime mutation; TL-M1 not COMPLETE.
- [2026-07-30] **TL-M1 unblock Part 1 (no mutation).** Recorded user decisions `TL-D12`–`TL-D15`
  (Page ID `61591880797654`; health reviewer user-attested; Sheet target `1s-Pm5f…8hms`; new Toplink
  SA). Authored profile-repair spec `docs/system/tl-m2-profile-repair-spec.md` (`TL-M2-PROFILE-REPAIR-001`,
  awaiting user sign-off). Updated staging (page-identity, entity-franchise, health-compliance,
  input-gap register; handoff hashes recomputed), operational contract v0.1.1 (target + new-SA plan),
  master plan v0.1.1, milestones v0.1.2. Gates held: public franchise/legal + health per-item + Sheet
  write remain fail-closed; **no DMP profile mutation executed**; DMP trace `NONE`; `external_writes=0`;
  no milestone advancement.

- [2026-07-30] **TL-M2 profile repair executed (`TL-GAP-011` RESOLVED).** User signed §6 of
  `docs/system/tl-m2-profile-repair-spec.md` (`APPROVED 2026-07-30`). Bounded field correction on
  DMP local `profile.json`: `primary_channel`/`active_channels`→Facebook Page, `primary_goal`→độc lập
  (0 Thảo Tây/supporting), `competitors`→`[]`, added `_franchise_internal` (franchisor, public
  `PENDING_DOCUMENT`). DMP skills (`import-guidelines`/`brand-setup`) have no dry-run ⇒ used controlled
  minimal correction per spec §5 step 3 caveat (no skill mutation invoked). Backup + real-trace +
  digest-lock written; `profile_digest=a45e4ae4…`, `source_digest=3ba91761…` locked into
  `docs Toplink/staging/run1/00-input-lock.json`. Read-back all PASS (G1–G7). `git diff --check` PASS,
  secret/PII scan clean, 0 "Thảo Tây" in profile. `external_writes=0`; no milestone COMPLETE/PASS.
  Next gated: run TL-M1 DMP with real trace.

- [2026-07-30] **TL-M1 DMP run — 2 real invocations `VERIFIED_REAL_INVOKE` (scope: import-guidelines only).**
  User chose "chỉ import-guidelines" (brand-setup bỏ qua để không clobber profile digest-locked). (1)
  `switch-brand toplink-y-vien` — active brand was `thao-tay`, switched to avoid cross-brand import breach;
  read-back OK. (2) `import-guidelines` via `guidelines-manager.py` save — added `voice-and-tone`(11),
  `messaging`(9), `visual-identity`(8), `channel-styles`(6), merged with `restrictions`(18) ⇒ 5 categories/
  52 rules, summary read-back MATCH. Profile.json NOT touched (**G5 lock held**, digest `a45e4ae4…` unchanged);
  `grep "Thảo Tây"` = 0 across guidelines (isolation lines reworded to "thương hiệu bên ngoài"). Trace
  `staging/toplink-reconciled/TL-M1-evidence/tl-m1-dmp-trace.md`; `git diff --check` PASS; secret scan clean;
  `external_writes=0`; no milestone COMPLETE. Runtime note: `_active-brand.json` now `toplink-y-vien`
  (switch back to `thao-tay` before any Thảo Tây work; backup saved). Next: PR verdict re-run + two-run.

- [2026-07-30] **TL-M1 closure pass — `LOCAL_EVIDENCE_PASS · READY_FOR_CODEX_RECONCILIATION` (NOT COMPLETE).**
  Did the agent-doable remaining tasks in order: (1) superseded stale `dmp-invocation-block.md` (block
  cleared, points to real trace, historical kept); (2) re-ran PR & Communications Manager review →
  `agency-review-pr-manager.md` Review 2: verdict `NEEDS_HUMAN_REVIEW` overall, but TL-REV-004 (Page ID) +
  TL-REV-005 (DMP trace) upgraded to PASS, new TL-REV-008/009/010; VERIFY line "DMP trace + PR verdict"
  now satisfied (NEEDS gate); (3) wrote `tl-m1-closure-readiness.md` mapping all 12 VERIFY items → 10 PASS,
  #7 Sheet DEFERRED, #12 pre-migration HELD, none FAIL. `git diff --check` PASS; secret scan clean;
  `external_writes=0`; no milestone marked COMPLETE/APPROVED. **Cannot be agent-closed** — remaining owners:
  Codex reconciliation (Run 1 Phase B + TL-REV-007 staging path), user human-APPROVE of legal/franchise/
  health gates (TL-GAP-002/009/007), user SA → Codex Sheet read-back (TL-GAP-008), two-run package;
  TL-GAP-012–014 fail-closed by design.

## Next-session read order
