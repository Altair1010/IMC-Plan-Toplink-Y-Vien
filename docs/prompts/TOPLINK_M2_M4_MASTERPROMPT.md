# TOPLINK_M2_M4_MASTERPROMPT — Run 1 Phase A (Claude DMP build, local-only)

> Paste this into a fresh Claude Code session opened at repo root `F:\Codex\IMC Plan - Toplink Y Viện`.
> Scope: build **TL-M2 → TL-M3 → TL-M4** as Run 1 Phase A. Local-only, `external_writes=0`. This prompt
> cannot authorize any Page/Sheet/publish/external mutation and cannot replace a real DMP invocation.
> It complements — does not override — `docs/prompts/TOPLINK_RUN1_MASTERPROMPT.md`.

---

## 0. Read order before any write (scaffold)

Read the minimum relevant subset, in this order; do not load unrelated corpora (token policy):
`AGENTS.md` (incl. **§ Token optimization policy**) → `STATE.md` → `RULES.md` → `task.md` →
`GOVERNANCE.md §1 + §3` → `spec.md` → `docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md` →
`docs Toplink/TOPLINK_PAGE_MILESTONES.md` (sections **TL-M2, TL-M3, TL-M4** + PHẦN C two-run) →
`docs/system/claude-codex-operating-contract.md` →
`docs/system/toplink-google-sheets-operational-contract.md` (tab registry + field rules).

Evidence already produced by TL-M1 (read, do not redo):
`staging/toplink-reconciled/TL-M1-evidence/` — `source-inventory.md`, `entity-franchise-allowed-use-map.md`,
`health-compliance-claim-taxonomy.md`, `page-identity-baseline-gate.md`, `input-gap-register.md`,
`tl-m1-dmp-trace.md`, `root-provenance-map.md`, `tl-m1-closure-readiness.md`,
`agency-review-pr-manager.md` (Review 2). Profile repair: `docs/system/tl-m2-profile-repair-spec.md`
(APPROVED) + `staging/toplink-reconciled/TL-M2-profile/tl-m2-profile-repair-trace.md`.
Digest lock: `docs Toplink/staging/run1/00-input-lock.json`. Use `docs/system/toplink-knowledge-brief.md`
only as a compact aid, never as a substitute for canon.

## 1. Current state you inherit (do not re-derive)

- **TL-M1** = `LOCAL_EVIDENCE_PASS`; PR verdict Review 2 `NEEDS_HUMAN_REVIEW` (human gates open, expected).
- **Profile G5 LOCK**: `toplink-y-vien/profile.json` digest `a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349`
  (`source_digest 3ba91761…`). Facebook Page primary; goal independent (0 Thảo Tây/supporting);
  competitors `[]`; `_franchise_internal` INTERNAL-only. Guidelines = 5 categories / 52 rules.
- **DMP active brand** may be `toplink-y-vien` or `thao-tay` — you MUST verify + `switch-brand toplink-y-vien`
  and read back before any DMP call. (`_active-brand.json` is shared global state.)
- **Decisions:** TL-D16 franchise/legal **KEEP LOCKED** (no public wording); TL-D17 health reviewers =
  Thảo Tây (teacher, person) + Guru (user), **user-attested**, per-item publish gate stays; TL-D18 dossier
  pending (claims stay `UNVERIFIED` + "hỗ trợ"); TL-D19 Sheet SA infra ready but **write still gated**;
  TL-D20 root provenance located.

## 2. Hard guardrails (fail-closed)

1. **Isolation.** Never use a Thảo Tây Page, Sheet, credential, analytics baseline, audience number, or
   brand fact. The origin repo `F:\Codex\IMC Plan - Thảo Tây` may inform **structure/process/skeleton only**
   (milestone doc shapes, sheet schema, section layout) — never Toplink brand facts, targets, goals,
   audience data, or KPIs. **Never open the actual Thảo Tây Google Sheet.**
2. **G5 lock.** Do not re-drift the profile. TL-M2 formalizes/locks the already-repaired profile. If
   `brand-setup` would clobber field-level, stop and use bounded correction on the exact declared fields
   (as in the signed repair) — never re-derive wholesale, never invent fields.
3. **Real trace or not done.** Every DMP invocation records `trace_id · timestamp · DMP_version ·
   active_brand_readback · skill · input_paths · input_digest · output_path · output_digest · status ·
   skipped_dimensions`. `NO_TRACE = NOT_DONE`. A skill-contract read is not an invocation.
4. **No invention.** Classify every material statement: confirmed / inference / hypothesis / missing /
   unverified / do-not-use. No franchise, legal, founder, product-efficacy, price, availability, booking,
   qualification, or nationwide-capacity fact invented.
5. **Human gates hold.** Health/legal/privacy/public-claim items stay `NEEDS_HUMAN_REVIEW`. No `APPROVED`,
   no publish, no Sheet/Page write, no milestone marked `COMPLETE`. `external_writes=0` throughout.
6. **Model discipline.** Cheaper model for source reading/extraction; stronger model for editing,
   reconciliation, validation. Keep extraction separate from final judgment.

## 3. Lease + cross-runtime

Before any shared write, acquire a scoped `task.md` lease row (file set, start ICT, purpose). This is
Run 1 **Phase A only** — do NOT author Codex Phase B files (`docs Toplink/staging/run1/10..70`,
`run1-manifest.json`); Codex owns those after your handoff. Stop writing → checkpoint → release lease
before Codex starts. Follow `docs/system/claude-codex-operating-contract.md`.

## 4. Milestone build — do in order, one lease/checkpoint each

### TL-M2 — DMP profile + brand architecture
- **DMP:** `switch-brand toplink-y-vien` → `status` read-back → (profile already repaired; only formalize).
- **Work:** map fields core/profile/guideline/staging-only; keep Facebook Page primary; Website/Zalo/phone/
  Maps `PENDING_INPUT`; competitor/franchisor per entity map (internal-only); recompute + lock
  `profile_digest`+`source_digest` (must equal the inherited G5/source digests — if they differ, STOP,
  investigate drift). No slug `toplink-page`.
- **Deliverables:** `docs Toplink/brand/dmp-profile.md`, `docs Toplink/system/runtime-compatibility.md`,
  confirm `docs Toplink/staging/run1/00-input-lock.json`.
- **VERIFY:** one slug, active read-back `toplink-y-vien`; no secret/path/private analytics; no unsupported
  field forced into runtime; digests deterministic + locked.

### TL-M3 — Audience, positioning, Facebook Page strategy, pillar decision
- **DMP:** `audience-intelligence` → `campaign-plan` → `social-strategy` + `content-engine`.
- **Work:** assess audience hypotheses `TL-A01`–`TL-A04` (keep/edit/drop with rationale, no invented
  insight); positioning/narrative hypotheses with proof boundary; separate Hà Nội service/conversion vs
  national awareness (no national-service inference); lock corporate voice + founder allowed-use; converge
  **3–5 pillars totaling 100%**, each with evidence/job/format/funnel/risk/rationale; Facebook Page primary,
  Reels support; any founder/teacher cross-post carries an item gate.
- **Deliverables:** `docs Toplink/research/audience-hypotheses.md`, `docs Toplink/brand/positioning.md`,
  `docs Toplink/brand/narrative.md`, `docs Toplink/brand/content-pillars.md`,
  `docs Toplink/brand/facebook-page-strategy.md`.
- **VERIFY:** no audience fact without source; 3–5 pillars = 100%; founder-led guardrail itemized; no
  national-service inference; agency verdict by artifact; human gates intact.

### TL-M4 — Trust-led relative campaign + greenfield KPI
- **DMP:** `campaign-plan` + `social-strategy` + `content-engine`.
- **Inputs (user-confirmed):** calendar is **relative D-1 … D-28** (no absolute dates; no `TOPLINK_CONTENT_START_DATE`
  binding); cadence **1–2 posts/day**; user shoots/edits media + finalizes caption later — **DMP produces only
  the skeleton/framework** (structure, hook, angle, claim IDs, CTA class), not finished creative.
- **Work:** W1 identity/limits; W2 health-sensitive education (claim + professional gate item-level); W3
  operational proof only (or proof with dossier/consent); W4 conditional `EVIDENCE-CLEARED SOLUTION` or
  `SAFE FALLBACK` (fallback must be complete, not bypassed by calendar/disclaimer); default CTA
  non-commercial (commercial CTA only after an offer gate that does not yet exist); KPI dictionary
  (definition/formula/source/owner/cadence/minimum sample); **counts = 0 when measured, rates/history = `N/A`,
  never `% from zero`**; experiments one variable at a time (Continue/Repair/Stop).
- **Deliverables:** `docs Toplink/brand/campaign-architecture.md`, `docs Toplink/brand/kpi-experiment-plan.md`.
- **VERIFY:** 4 weeks trace back to pillar/audience job; W2 claim/professional gate item-level; W3 operational
  or documented proof only; W4 fallback complete; KPI does not overclaim trust/awareness.

> Note: full 28-day content calendar + production/reels briefs are **TL-M5** (blocked on dossier + per-item
> health gate + finalized capacity/reviewer route). M2→M4 sets the framework M5 will fill. Do not start M5.

## 5. Sheet targeting (logical only — no write)

Map every deliverable to the logical Toplink datasets in `docs/system/toplink-google-sheets-operational-contract.md §3`
(e.g. TL-M2 → `TL_BRAND_PROFILE`; TL-M3 → `TL_AUDIENCE_HYPOTHESES` / `TL_POSITIONING` / `TL_CONTENT_PILLARS` /
`TL_FACEBOOK_STRATEGY`; TL-M4 → `TL_CAMPAIGN` / `TL_KPI_DICTIONARY` / `TL_EXPERIMENTS`), plus the always-on
`TL_OUTPUT_INDEX` / `TL_DECISIONS` / `TL_COMPLIANCE_RULES`. Structure prose for Sheet as columns —
`Section | Subsection | Item ID | Content | Evidence/source | Assumption status | Owner | Review status | Last updated`
— so a later bounded sync maps cleanly. **Do not write to any Sheet.** The SA infra is ready but the write
needs a signed `SheetTargetApproval` + Codex bounded upsert + exact read-back (separate step). Keep
`external_write=false` in every Run 1 plan.

## 6. Agency review

For each milestone route ≤3 Agency reviewers by the routing matrix (`docs/system/capability-routing-matrix.md`).
Preserve issue / severity / evidence-location / repair request / verdict. Reviewers cannot grant `APPROVED`.

## 7. Handoff + exit

1. After M2→M4, refresh `staging/toplink-reconciled/TL-M1-evidence/handoff-claude-to-codex.md` +
   `handoff-envelope.json` from committed templates: exact paths/digests (all M2–M4 outputs), stable IDs,
   open issues, gates, allowed next action, forbidden actions.
2. Write the Phase A marker: `CLAUDE_TOPLINK_RUN1_PHASE_A_COMPLETE` with `profile_digest`, `source_digest`,
   `DMP_version`, `active_brand`, `generated_outputs`, `reviewers`, `check_results`, `external_writes=0`,
   `next_actor=Codex`.
3. Local checks before release: `git diff --check`; secret/PII scan; digest recomputation; `external_writes=0`;
   confirm profile digest still `a45e4ae4…` (G5 held). Stop writing, checkpoint, release lease.
4. Update `STATE.md` + `task.md` (status, files, verdicts, open gates, next safe action). Then Codex runs
   Run 1 Phase B (do not do it yourself).

## 8. Stop conditions (any → stop, not pass)

Brand/digest/scope conflict; active brand ≠ `toplink-y-vien`; a DMP skill would clobber the G5-locked profile;
missing required evidence; conflicting lease; second repeated bounded failure; any pressure to invent
health/legal/franchise/price/availability facts or to write externally. Record the exact blocker and the
owner; do not retry the same blocked action.
