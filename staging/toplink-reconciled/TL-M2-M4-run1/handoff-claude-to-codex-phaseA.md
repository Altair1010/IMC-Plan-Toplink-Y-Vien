# Handoff — Claude → Codex (Run 1 Phase A, TL-M2 → TL-M4)

> Addendum to `staging/toplink-reconciled/TL-M1-evidence/handoff-claude-to-codex.md`. Machine marker:
> `CLAUDE_TOPLINK_RUN1_PHASE_A_COMPLETE.json` (same dir). Uses committed handoff/envelope shape.

## 1. What Claude produced (Phase A repair, local-only)

9 deliverables, 1 DMP trace, 1 agency review, 6 real-authoring raw-evidence sets under `raw-repair/`:

- **TL-M2:** `docs Toplink/brand/dmp-profile.md`, `docs Toplink/system/runtime-compatibility.md`.
- **TL-M3:** `docs Toplink/research/audience-hypotheses.md`, `docs Toplink/brand/{positioning,narrative,content-pillars,facebook-page-strategy}.md`.
- **TL-M4:** `docs Toplink/brand/{campaign-architecture,kpi-experiment-plan}.md`.
- **Trace:** `staging/toplink-reconciled/TL-M2-M4-run1/dmp-trace.md` `b63c2601…`.
- **Review:** `staging/toplink-reconciled/TL-M2-M4-run1/agency-review.md` `d6006af9…`.
- **Raw evidence:** `raw-repair/TL-M2-DMP-BRAND-002`, `TL-M3-DMP-AUD-002`, `TL-M3-DMP-CAMP-002`, `TL-M3-DMP-SOC-002`, `TL-M3-DMP-SOC-003`, `TL-M4-DMP-CAMP-002` (`.md` + `.invocation.json` each).

## 2. Locked inputs (must equal in Run 2)

```text
DMP 3.15.1 · active brand toplink-y-vien
profile_digest a45e4ae4…c8cbe349   [G5 HELD]
source_digest  3ba91761…6541fe76   [5/5 MATCH]
```

## 3. What changed vs prior (real-invocation repair, 2026-08-04)

- **Invocation mode fixed:** M2–M4 traces rebuilt from **eval-runner-misattribution** to **real
  authoring-subagent dispatch** (governed definition: subagent dispatch = real native authoring invocation,
  human owner 2026-08-03). Each authoring capability (brand-setup, audience-intelligence, campaign-plan,
  social-strategy) re-invoked via the Agent tool; raw output + `.invocation.json` metadata + SHA-256 captured
  under `raw-repair/`. Evaluator scripts are now recorded **separately** as `check` only.
- **1 canonical changed — content-pillars REGENERATE:** `451425c1…` → **`b0790e2d…`**. Native social-strategy
  regeneration re-expressed pillar weights as 28-slot fractions (6/6/8/4/4) and neutralized superlatives.
  Machine check: composite **32 → 92**, `auto_rejected` **true → false**, 0 critical. Auto-reject genuinely
  cleared by regeneration, not prose override.
- **8 canonical unchanged (KEEP)** — dmp-profile, runtime-compatibility, audience-hypotheses, positioning,
  narrative, facebook-page-strategy, campaign-architecture, kpi-experiment-plan (digests in marker).
- **Separate check result:** all 9 deliverables `auto_rejected=false`, 0 critical (raw JSON in `raw-repair/check/`).
- **G5 profile lock held** (`a45e4ae4…` unchanged); `brand-setup` mutating path NOT invoked (fail-closed
  non-mutating proposal reconciled KEEP). 5/5 source digests MATCH. Isolation scan = 0 external-brand refs.

## 4. Codex Phase B action required

- Reconcile `run1-manifest.json` `dmp_traces[]` statuses (currently `VERIFIED_REAL_INVOKE_SCAFFOLD`) to the
  real-invocation repair; refresh trace/marker digests (dmp-trace `b63c2601…`, marker rebuilt).
- Record content-pillars new digest **`b0790e2d…`** (was `451425c1…`) in the manifest/delta ledger.

## 5. Open gates (fail-closed, expected)

- Health-sensitive `TL-P2`/`TL-P4` + campaign W2 → `NEEDS_HUMAN_REVIEW` (item-level, per `TL-D13`).
- Public positioning → `HYPOTHESIS · NOT_PUBLIC_APPROVED`.
- Franchise/legal public wording → `PENDING_DOCUMENT` (`TL-D16`), internal-only.
- Product efficacy / price / offer / booking → `UNVERIFIED` / `MISSING_INPUT`.
- Sheet write → `BLOCKED_TARGET_INPUT`; `external_writes=0`. Logical datasets mapped only.

## 6. Allowed next action (Codex)

Run 1 **Phase B** reconciliation only: author `docs Toplink/staging/run1/10..70` + `run1-manifest.json`,
reconcile TL-M2–M4 outputs into the delta ledger/manifest, verify digests against the marker. Claude did
**not** author Phase B files (lease boundary honored).

## 7. Forbidden next

Sheet/Page/publish mutation; mark any milestone COMPLETE/APPROVED; Run 3; author health/legal/efficacy
facts; `brand-setup` live-profile mutation that would clobber the G5-locked profile.
