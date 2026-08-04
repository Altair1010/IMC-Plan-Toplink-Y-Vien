# TL-M2 → TL-M4 — Agency review (Run 1 Phase A, Toplink Y Viện)

> Reviewers route by `docs/system/capability-routing-matrix.md` / master plan §13, ≤3 per workstream.
> Output = issue · severity · evidence/location · required repair · verdict. **No reviewer can grant
> `APPROVED`.** Health-sensitive/legal artifacts stay `NEEDS_HUMAN_REVIEW`.
>
> **Post-repair (2026-08-04):** verdicts re-confirmed after real authoring re-invocation (subagent
> dispatch) of brand-setup/audience-intelligence/campaign-plan/social-strategy. Only `content-pillars.md`
> changed (REGENERATE, `451425c1…`→`b0790e2d…`, auto_reject cleared 32→92); 8 other deliverables KEEP,
> byte-unchanged. All 9 deliverables `auto_rejected=false`, 0 critical (see `dmp-trace.md` §3).

## TL-M2 — PR & Communications Manager (profile/franchise/legal)

| # | Issue | Severity | Evidence/location | Required repair | Verdict |
|---|---|---|---|---|---|
| M2-R1 | Franchise/legal relationship must stay internal | Critical | dmp-profile §2 TL-BP-19; entity-map §2 | Keep `INTERNAL_ONLY`, no public wording | `PASS` (held internal) |
| M2-R2 | One slug, no `toplink-page` | High | dmp-profile §1 | — | `PASS` |
| M2-R3 | Digest lock deterministic | High | dmp-profile §4; 00-input-lock.json | — | `PASS` (5/5 + profile MATCH) |
| M2-R4 | No secret/private analytics in profile | High | runtime-compat §5; secret scan | — | `PASS` (0 secret/PII) |

**TL-M2 verdict: `PASS` (local).** Not COMPLETE/APPROVED; Sheet read-back deferred.

## TL-M3 — Social Strategist → Growth Hacker (+ PR for health/legal artifacts)

| # | Issue | Severity | Evidence/location | Required repair | Verdict |
|---|---|---|---|---|---|
| M3-R1 | Audience must remain hypothesis, no invented insight | High | audience-hypotheses §0,§2 | — | `PASS` |
| M3-R2 | Hà Nội service vs national awareness separation | High | audience §1 (TL-A04 bound); positioning §5 | — | `PASS` |
| M3-R3 | Pillars 3–5, allocation covers full plan | High | content-pillars (regenerated `b0790e2d…`; slot 6/6/8/4/4 = 28/28) | Re-expressed as 28-slot fractions to clear generic-scorer auto-reject (32→92) | `PASS` (auto_reject=false) |
| M3-R4 | Founder guardrail itemized | Medium | narrative §3; pillars §3 | — | `PASS` |
| M3-R5 | Body-literacy pillar `TL-P2`/`TL-P4` health-sensitive | Critical | content-pillars §3; positioning §4 M4 | Item-level professional/human review before publish | `NEEDS_HUMAN_REVIEW` |
| M3-R6 | Positioning is hypothesis, not public-approved | High | positioning §1 | Human gate before any public use | `NEEDS_HUMAN_REVIEW` |

**TL-M3 verdict: `PASS` on structure/strategy; `NEEDS_HUMAN_REVIEW` on health-sensitive + public positioning (M3-R5/R6).**

## TL-M4 — Social Strategist → Growth Hacker (+ PR, health-sensitive)

| # | Issue | Severity | Evidence/location | Required repair | Verdict |
|---|---|---|---|---|---|
| M4-R1 | 4 weeks trace to pillar + audience job | High | campaign-arch §1 | — | `PASS` |
| M4-R2 | W2 claim/professional gate item-level | Critical | campaign-arch §2 W2 | Keep per-item review | `NEEDS_HUMAN_REVIEW` |
| M4-R3 | W3 operational proof only | High | campaign-arch §2 W3 | — | `PASS` |
| M4-R4 | W4 fallback complete, not bypassed | Critical | campaign-arch §2 W4 (Branch B default) | — | `PASS` (SAFE FALLBACK) |
| M4-R5 | KPI no `% from zero`; counts=0/rates=N/A | High | kpi-plan §1,§2 | — | `PASS` |
| M4-R6 | Intent/booking KPI gated | High | kpi-plan §3 (TL-KPI-09 gated) | Keep gated until offer gate | `PASS` |
| M4-R7 | Non-commercial CTA default | High | campaign-arch §3 | — | `PASS` |

**TL-M4 verdict: `PASS` on architecture/KPI; `NEEDS_HUMAN_REVIEW` on W2 health-sensitive items (M4-R2).**

## Rollup

- Structural/strategic verdicts: **all `PASS` (local)**.
- Human gates open (expected, fail-closed): health-sensitive content (`TL-P2`/`TL-P4`, W2), public
  positioning, franchise/legal public wording. None may be `APPROVED` by an agent.
- No reviewer rewrote an artifact silently; no `APPROVED` granted; `external_writes=0`.
