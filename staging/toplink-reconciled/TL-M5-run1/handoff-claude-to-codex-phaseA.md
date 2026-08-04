# Handoff — Claude → Codex (TL-M5 Run 1 Phase A)

## Envelope

- **Run/stage:** `TOPLINK_RUN1_BUILD` · Phase A (TL-M5)
- **Prepared by / timestamp (ICT):** `Claude Code · 2026-08-04T01:15:00+07:00`
- **Recipient:** `Codex CLI`
- **Lease:** released — `docs Toplink/content/{5 files}` + `staging/toplink-reconciled/TL-M5-run1/**`
- **Read timing:** before Codex Run 1 Phase B reconciliation of TL-M5

## Scope and provenance

- **Canonical inputs:** `00-input-lock.json` (block `809a94dd…`), M2–M4 outputs
  (`content-pillars b0790e2d…` [regenerated], `campaign-architecture c1fda749…`, `positioning 7c216e38…`,
  `narrative 02a6f6be…`, `kpi-experiment-plan 40a528c6…`, `facebook-page-strategy cdd1f786…`,
  `audience-hypotheses 4a32da6b…`), safety `02_communication_safety.md 94a9c5ea…`, frozen dossier
  `645b1ad2…`, product `11_Product_Yvien.md df367e1b…` (`UNVERIFIED`, customer-experience only).
- **DMP trace:** real authoring-subagent dispatch (governed 2026-08-03) — `TL-M5-DMP-CAL-002`
  (content-calendar), `TL-M5-DMP-ENG-002` (content-engine), `TL-M5-DMP-VID-002` (video-script), each with
  raw output + `.invocation.json` under `raw-repair/`; DMP `3.15.1`; active-brand read-back `toplink-y-vien`.
  Evaluator scripts recorded **separately** as `check` (raw JSON in `raw-repair/check/`). Trace rebuilt
  2026-08-04: `staging/toplink-reconciled/TL-M5-run1/dmp-trace.md` now **`99338576…`**; agency-review
  **`c8390a46…`**. Structured JSON envelope: `handoff-envelope.json`.
- **Input/profile digest:** profile `a45e4ae4…c8cbe349` (G5 held); source set `3ba91761…` 5/5.
- **Output paths/digests (all KEEP, byte-unchanged):**
  - `docs Toplink/content/month-calendar.md` `0d2d2d16…`
  - `docs Toplink/content/asset-and-batch-plan.md` `435969cf…`
  - `docs Toplink/content/reels-briefs.md` `51b18d91…`
  - `docs Toplink/content/production-briefs.md` `42cb8e7d…`
  - `docs Toplink/content/workflow-approval-measurement.md` `651dff61…`
  - `staging/.../TL-M5-run1/dmp-trace.md` **`99338576…`**
  - `staging/.../TL-M5-run1/agency-review.md` **`c8390a46…`**
  - `staging/.../TL-M5-run1/CLAUDE_TOPLINK_RUN1_PHASE_A_COMPLETE.json`
- **Stable IDs affected:** `TL-M5-CALENDAR-001`, `TL-M5-ASSET-001`, `TL-M5-REELS-001`,
  `TL-M5-PRODBRIEF-001`, `TL-M5-WORKFLOW-001`; items `TL-M5-CAL-D01..D28`.
- **Sheet delivery plan:** `TL-SHEET-001` logical datasets `TL_CONTENT_CALENDAR`, `TL_REELS_PRODUCTION`,
  `TL_WORKFLOW_APPROVAL` — local only; `target provided but write BLOCKED`. No write in this phase.

## Reviewer and check results

| Reviewer/check | Verdict | Evidence/location | Required repair or gate |
|---|---|---|---|
| Content Creator | `REVIEWED` (structural PASS) | agency-review §1 | — |
| PR Manager (copy+safety) | `PASS` + `NEEDS_HUMAN_REVIEW` | agency-review §1,§3 | human gate: health/positioning/founder/product |
| Short-Video Coach | `PASS` (mechanics) | agency-review §2 | — |
| TikTok Strategist | `REVIEWED` (mechanics-only) | agency-review §2 | no TikTok publish/cross-post |
| DMP check (separate `eval-runner.py`) | `PASS` (0 critical, 0 auto-reject) | dmp-trace §3; raw-repair/check/ | textstat/nltk dims fallback (script-reported) |
| Safety ledger | `NEEDS_HUMAN_REVIEW` overall | agency-review §3–§4 | human/professional for health/legal/privacy |

## Issue and repair ledger

| ID | Severity | Classification | Evidence | Allowed repair route | Status |
|---|---|---|---|---|---|
| `TL-M5-ISSUE-001` | major | claim | 10 health items need per-item human/professional approval | `HUMAN_GATE` | open |
| `TL-M5-ISSUE-002` | major | evidence | `11_Product_Yvien.md` UNVERIFIED (D14/D26 customer-exp only) | `HUMAN_GATE` (`TL-GAP-010`) | open |
| `TL-M5-ISSUE-003` | minor | runtime | team-role split `MISSING_INPUT` in asset/batch plan | `HUMAN_GATE` (`TL-GAP-006` at TL-M6) | open |
| `TL-R1-MANIFEST-DMPSTATUS-001` | minor | schema | manifest `dmp_traces[]` still `VERIFIED_REAL_INVOKE_SCAFFOLD`; add TL-M5 + content-pillars new digest | `CODEX_PHASE_B` | open |

## Human gates, recipient constraints, and release

- **Human gate/blocker:** per-item health approval (`TL-D13/TL-D17`), public positioning, franchise/legal
  (`TL-D16` KEEP LOCKED), product dossier (`TL-GAP-004/010`), founder allowed-use + consent, testimonial
  consent. None can be self-approved; agency verdict max = `NEEDS_HUMAN_REVIEW`.
- **Allowed next action:** Codex reconciles TL-M5 into the Run 1 manifest (add TL-M5 outputs + refresh
  input-lock reference) **without** closing Run 1. Verify 5 output + staging digests (dmp-trace
  `99338576…`, agency-review `c8390a46…`, envelope hash), stable-ID uniqueness, reference integrity,
  pillar allocation 6/6/8/4/4, forbidden-term/disclaimer/CTA/franchise scans. **Also reconcile manifest
  `dmp_traces[]` statuses** (currently `VERIFIED_REAL_INVOKE_SCAFFOLD`) to the real-authoring repair.
- **Forbidden:** Sheet/Page/publish mutation, `APPROVED`, milestone advancement, Run 1 close, Run 2/Run 3,
  editing input lock / P1 Trellis files / `11_Product_Yvien.md`, elevating UNVERIFIED product to claim.
- **Stop if:** profile digest ≠ `a45e4ae4…`, source set ≠ `3ba91761…` 5/5, active brand ≠ `toplink-y-vien`,
  DMP ≠ `3.15.1`, output digest mismatch, or overlapping lease.

I stopped writing the leased file set, persisted this handoff, and released the lease. This handoff does
not grant human approval. `external_writes=0`; `milestone_advanced=false`; `next_actor=Codex`.
