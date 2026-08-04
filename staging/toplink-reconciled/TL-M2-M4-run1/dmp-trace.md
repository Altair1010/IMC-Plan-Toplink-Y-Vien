# TL-M2 → TL-M4 — DMP invocation trace (Run 1 Phase A, Toplink Y Viện)

> Scope: Claude DMP authoring for `TL-M2`–`TL-M4`, local-only, `external_writes=0`. `NO_TRACE = NOT_DONE`.
> DMP version `3.15.1`; active brand read-back `toplink-y-vien` for every row.
>
> **Invocation-mode (repaired 2026-08-04, real authoring).** This trace replaces the earlier version
> that misattributed `scripts/eval-runner.py` (the `check` capability) as authoring capabilities. Under
> the governed definition (human owner, 2026-08-03): **DMP authoring-subagent dispatch via the Agent
> tool = real native authoring invocation.** Each authoring capability below is now recorded against a
> real subagent dispatch that returned a generated raw result, captured to `raw-repair/<trace>.md` with
> a SHA-256 and an `<trace>.invocation.json` metadata sidecar. Evaluator scripts are recorded separately
> in §3 as `check` only. Labels `VERIFIED_REAL_INVOKE_SCAFFOLD`, `skill-scaffold`, `planned`,
> `manual-only`, and read-back-only are **not** used for authoring rows.

## Common inputs (G5-locked, verified this run)

```text
profile.json   a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349  [MATCH, G5 held]
source_digest  3ba91761612ca482471dc1c071bd7e9d82e5708a3bb13ceb630fed476541fe76  [locked 5/5 exact]
active brand   toplink-y-vien (_active-brand.json)                               [read-back]
DMP version    3.15.1 (plugins/cache/neels-plugins/digital-marketing-pro/3.15.1) [verified]
```

## 1. Real authoring invocations (subagent dispatch; raw output + metadata captured)

Every row: `native_skill_invoked=true`; raw output + `.invocation.json` under
`staging/toplink-reconciled/TL-M2-M4-run1/raw-repair/`; `external_writes=0`.

| trace_id | milestone | capability | native subagent | raw output (sha256) | selected output | disposition |
|---|---|---|---|---|---|---|
| `TL-M2-DMP-BRAND-002` | TL-M2 | brand-setup (non-mutating proposal) | `digital-marketing-pro:marketing-strategist` | `TL-M2-DMP-BRAND-002.md` `1a91b07d…` | `docs Toplink/brand/dmp-profile.md` `2a151493…` (unchanged) | KEEP |
| `TL-M3-DMP-AUD-002` | TL-M3 | audience-intelligence | `digital-marketing-pro:marketing-strategist` | `TL-M3-DMP-AUD-002.md` `efa54ffb…` | `docs Toplink/research/audience-hypotheses.md` `4a32da6b…` (unchanged) | KEEP |
| `TL-M3-DMP-CAMP-002` | TL-M3 | campaign-plan (positioning+narrative) | `digital-marketing-pro:marketing-strategist` | `TL-M3-DMP-CAMP-002.md` `6cc1f5a2…` | `positioning.md` `7c216e38…`, `narrative.md` `02a6f6be…` (unchanged) | KEEP |
| `TL-M3-DMP-SOC-002` | TL-M3 | social-strategy (content-pillars) | `digital-marketing-pro:social-media-manager` | `TL-M3-DMP-SOC-002.md` `b0790e2d…` | `docs Toplink/brand/content-pillars.md` `b0790e2d…` (**REGENERATED**) | REGENERATE |
| `TL-M3-DMP-SOC-003` | TL-M3 | social-strategy (facebook-page-strategy) | `digital-marketing-pro:social-media-manager` | `TL-M3-DMP-SOC-003.md` `95645fa6…` | `docs Toplink/brand/facebook-page-strategy.md` `cdd1f786…` (unchanged) | KEEP |
| `TL-M4-DMP-CAMP-002` | TL-M4 | campaign-plan (campaign-architecture+kpi) | `digital-marketing-pro:marketing-strategist` | `TL-M4-DMP-CAMP-002.md` `833f63a5…` | `campaign-architecture.md` `c1fda749…`, `kpi-experiment-plan.md` `40a528c6…` (unchanged) | KEEP |

### TL-M3-DMP-SOC-002 — content-pillars REGENERATE (auto-reject repair)

The only canonical change this run. Native `social-strategy` regeneration re-expressed pillar weights as
28-slot fractions (6/6/8/4/4) instead of bare percentages, and neutralized superlative/exclusive language,
preserving every pillar/ID/audience/evidence/funnel/risk/guardrail. Machine check result:

```text
pre-regeneration : composite 32 / grade F / auto_rejected=TRUE  / halluc 32 / 15 flags / 0 critical
post-regeneration: composite 92 / grade A / auto_rejected=FALSE / halluc 92 /  1 flag  / 0 critical
```

`auto_reject` was genuinely cleared by regeneration (machine output, threshold composite<40), **not** by
prose override. Prior canonical `451425c1…` → new canonical `b0790e2d…`.

### TL-M2 brand-setup fail-closed note

Native `brand-setup` mutates the live `profile.json`, which is G5 digest-locked (`a45e4ae4…`) and has no
dry-run. The mutating path was **not invoked**. A non-mutating proposal was authored and reconciled to
`dmp-profile.md` (KEEP). `sha256sum profile.json` = `a45e4ae4…` unchanged. `TL-R1-BLK-DMP-M2-001`: repaired
via non-mutating proposal; live-profile mutation remains a documented human/runtime action, not agent-run.

## 2. Reconciliation summary

- 1 canonical changed: `content-pillars.md` (`451425c1…` → `b0790e2d…`, disposition REGENERATE).
- 8 canonical unchanged (KEEP): dmp-profile, audience-hypotheses, positioning, narrative,
  facebook-page-strategy, campaign-architecture, kpi-experiment-plan, runtime-compatibility.
- Subagent-proposed optional refinements on positioning/narrative (neutralize "mạnh nhất"; add explicit
  NEEDS_HUMAN_REVIEW labels) are logged in `TL-M3-DMP-CAMP-002.invocation.json` as human-review
  recommendations, **not applied** (files already pass; minimize digest churn).
- No invented brand/product/legal/franchise/health/founder/performance fact. Missing = `MISSING_INPUT`/`UNVERIFIED`.

## 3. DMP check (separate; evaluator scripts only)

`digital-marketing-pro:check` = `scripts/eval-runner.py --action run-full` + `hallucination-detector.py
--action detect` (+ `claim-verifier.py` where applicable), `logged=false` ⇒ `external_writes=0`. Raw JSON
saved under `raw-repair/check/`. Script-reported skipped dimensions every run: `content_quality`+`readability`
(textstat absent, fallback), `brand_voice` (nltk absent, fallback), `claim_verification` (no `--evidence`),
`output_structure` (no `--schema`).

| Deliverable | composite | auto_rejected | halluc | critical |
|---|---:|---|---:|---:|
| dmp-profile.md | 60 | false | 60 | 0 |
| runtime-compatibility.md | 84 | false | 84 | 0 |
| audience-hypotheses.md | 68 | false | 68 | 0 |
| positioning.md | 76 | false | 76 | 0 |
| narrative.md | 88 | false | 88 | 0 |
| **content-pillars.md** (repaired) | **92** | **false** | **92** | **0** |
| facebook-page-strategy.md | 52 | false | 52 | 0 |
| campaign-architecture.md | 64 | false | 64 | 0 |
| kpi-experiment-plan.md | 68 | false | 68 | 0 |

**All 9 M2–M4 deliverables: `auto_rejected=false`, 0 critical.** Low composites on some files are the
generic scorer flagging in-file design numerics / governed support-language already labeled
`HYPOTHESIS`/`NEEDS_HUMAN_REVIEW`; no fabricated fact. Deterministic check = PASS; agency/human layer stays
`NEEDS_HUMAN_REVIEW` on health/founder/public-positioning. No `APPROVED`.

## 4. Output digest re-confirmation

```text
2a15149302a1fc69e772fde035b16666a5be7f5a76fd5aeb3182dabb0df47bc4  docs Toplink/brand/dmp-profile.md
e38846fb51853d2e82eadab8f882ec1ecc4d5a01256b8f99685ab508f07425c7  docs Toplink/system/runtime-compatibility.md
4a32da6bdcbbbaa99db5618b052c809f579b8415497070d60b1f91fc3469c881  docs Toplink/research/audience-hypotheses.md
7c216e38fafeb46a6bcf40f0d4aa0b8dc872b060dbcb75e290da7e6b99729ce6  docs Toplink/brand/positioning.md
02a6f6be10b5c363a10e1ee1d6843ba913e17c9d56cb748ad24b2283aa5ae2c6  docs Toplink/brand/narrative.md
b0790e2d83aa456eb09a318e1306953ceab54cc68b6c68079fa218477fb3a2a6  docs Toplink/brand/content-pillars.md   [REGENERATED, was 451425c1…]
cdd1f786ff2222923bfd558f39f8f425a1004750d6e9e915ca27708e8e71e075  docs Toplink/brand/facebook-page-strategy.md
c1fda749f256dc420d7818143267c9036948ddfd812191c8f3d88cb5aa76c6c0  docs Toplink/brand/campaign-architecture.md
40a528c67c904789d07d2ca8395befc3a9a8a78bc24cef56ccd0a3cc9a06523d  docs Toplink/brand/kpi-experiment-plan.md
```

- [x] G5 profile lock held (`a45e4ae4…`); 5/5 source digests MATCH.
- [x] Active brand `toplink-y-vien` read-back every invocation.
- [x] Real authoring = subagent dispatch; each has raw output + metadata + SHA-256.
- [x] Evaluator = separate `check` only; no authoring row misattributes eval-runner.
- [x] content-pillars `auto_rejected` cleared by regeneration (32→92, machine).
- [x] `external_writes=0`; no Sheet/Page/publish; no milestone COMPLETE/APPROVED; Run 1 open; no Run 2.
