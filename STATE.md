# STATE.md — loop state tracker (Toplink Y Viện)

> Sprint-level truth only. Read this before `task.md`; it never overrides a canonical source.

## Sprint goals

- Operate the independent Toplink scaffold with explicit lease/handoff and two-run controls.
- Keep `TL-PMP-001` and `TL-MS-001` `PLAN_LOCKED` until their canonical readiness gates permit
  execution.

## In-progress

- No active shared work item or writer lease.

## Blocked

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
- Google Sheets **target provided** (`1s-Pm5f…8hms`) but write still blocked: needs the new Toplink
  service account (email + Editor grant), then a full `SheetTargetApproval` (tab/range/schema/action/
  limits/expiry) and exact read-back. `TL-SHEET-001` v0.1.1 records the target; it is not a write approval.
  **UPDATE 2026-07-30 (TL-D19): SA infrastructure READY** — SA `yvien-sheet-writer@imcforyvien.iam.gserviceaccount.com`
  created, Sheet shared Editor, Sheets API enabled, key at gitignored `.secrets/imcforyvien-de7e7ee958f4.json`,
  `GOOGLE_APPLICATION_CREDENTIALS` set (user-confirmed). **Still gated for WRITE:** signed `SheetTargetApproval`
  + Codex bounded upsert + exact read-back. SA ready ≠ write done.

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
