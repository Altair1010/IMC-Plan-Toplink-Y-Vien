# 10 — Evidence and profile map

Status: `RUN1_PASS · LOCAL_VERIFIED · PHASE_B_RECONCILED · NOT_MILESTONE_COMPLETE`

## Locked provenance

| Control | Read-back | Verdict |
|---|---|---|
| Profile | `a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349` | `PASS` |
| Frozen source set | `3ba91761612ca482471dc1c071bd7e9d82e5708a3bb13ceb630fed476541fe76`; 5/5 member hashes match | `PASS` |
| DMP / active brand | `3.15.1` / `toplink-y-vien` | `PASS` |
| Handoff | M2–M4 and M5 markers, reviews, traces and handoffs match all eight envelope hashes | `PASS` |
| External state | `external_writes=0`; `milestone_advance=false` | `PASS_ZERO` |

## Deliverable-to-evidence ledger

| Stable ID | Milestone | Path | Evidence status | Disposition | Retained gate |
|---|---|---|---|---|---|
| `TL-BRAND-PROFILE-001` | TL-M2 | `docs Toplink/brand/dmp-profile.md` | local profile structure verified | `KEEP` | public franchise/legal/product facts held |
| `TL-RUNTIME-COMPAT-001` | TL-M2 | `docs Toplink/system/runtime-compatibility.md` | runtime read-back verified | `KEEP` | same lock required in Run 2 |
| `TL-AUDIENCE-001` | TL-M3 | `docs Toplink/research/audience-hypotheses.md` | `HYPOTHESIS` | `KEEP` | pilot validation |
| `TL-POSITIONING-001` | TL-M3 | `docs Toplink/brand/positioning.md` | `HYPOTHESIS · NOT_PUBLIC_APPROVED` | `KEEP` | human public-use gate |
| `TL-NARRATIVE-001` | TL-M3 | `docs Toplink/brand/narrative.md` | gated hypothesis | `KEEP` | founder/privacy/consent |
| `TL-PILLARS-001` | TL-M3 | `docs Toplink/brand/content-pillars.md` | five-pillar 28-slot hypothesis | `REGENERATE` | TL-P2/TL-P4 item review |
| `TL-PAGE-STRATEGY-001` | TL-M3 | `docs Toplink/brand/facebook-page-strategy.md` | Facebook-primary hypothesis | `KEEP` | offer/commercial CTA held |
| `TL-CAMPAIGN-001` | TL-M4 | `docs Toplink/brand/campaign-architecture.md` | relative four-week structure | `KEEP` | W2 health review; W4 safe fallback |
| `TL-KPI-001` | TL-M4 | `docs Toplink/brand/kpi-experiment-plan.md` | greenfield measurement definitions | `KEEP` | baseline/capacity/offer gates |
| `TL-M5-CALENDAR-001` | TL-M5 | `docs Toplink/content/month-calendar.md` | 28 relative identities, A/B/C complete | `KEEP` | health/founder/product item gates |
| `TL-M5-ASSET-001` | TL-M5 | `docs Toplink/content/asset-and-batch-plan.md` | bounded capacity; placeholder assets only | `KEEP` | rights and consent uncleared |
| `TL-M5-REELS-001` | TL-M5 | `docs Toplink/content/reels-briefs.md` | 12 Facebook-first Reels | `KEEP` | health and asset gates |
| `TL-M5-PRODBRIEF-001` | TL-M5 | `docs Toplink/content/production-briefs.md` | 28 production records complete | `KEEP` | per-item claim/reviewer/consent gates |
| `TL-M5-WORKFLOW-001` | TL-M5 | `docs Toplink/content/workflow-approval-measurement.md` | approval/measurement workflow fail-closed | `KEEP` | human approval and publish held |

## Allowed-use rollup

- Usable now: local runtime identity, source-bound architecture, stable IDs, relative production plan.
- Conditional: audience, positioning, narrative, pillars, campaign, calendar and production hypotheses with their recorded gates.
- Blocked: unsupported health efficacy, public franchise/legal facts, commercial offer/booking claims, testimonials without consent, and publication.
- Human owners: professional health review; public-positioning/legal/privacy/consent decisions; asset rights; offer and Sheet approval.

No row promotes `HYPOTHESIS`, `UNVERIFIED`, Agency `PASS`, or `LOCAL_VERIFIED` to human `APPROVED`.
