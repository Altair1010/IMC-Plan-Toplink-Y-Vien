# TL-M5 Run 1 Phase A — DMP invocation trace + source ledger (Toplink Y Viện)

> **Local-only · `external_writes=0`.** Claude Code raw authoring. DMP `3.15.1`, active brand
> `toplink-y-vien` (read-back `_active-brand.json` → `active_slug=toplink-y-vien`), profile digest
> `a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349` (G5 lock held). Frozen source set
> `3ba91761…541fe76` 5/5 exact. No Sheet/Page/publish; no milestone advance; no Run 1 close; no Run 2.
>
> **Invocation-mode (repaired 2026-08-04, real authoring).** Replaces the earlier version that recorded
> `scripts/eval-runner.py` (the `check` capability) as content-calendar/content-engine/video-script
> authoring. Under the governed definition (human owner, 2026-08-03): **DMP authoring-subagent dispatch
> via the Agent tool = real native authoring invocation.** Each authoring capability is recorded against
> a real subagent dispatch that returned generated raw output, captured to `raw-repair/<trace>.md` with a
> SHA-256 and `<trace>.invocation.json`. Evaluator scripts are a separate `check` (§3). No authoring row
> misattributes eval-runner.

## 0. Runtime preflight (read-back)

| Check | Read-back | Verdict |
|---|---|---|
| Active brand | `toplink-y-vien` (`_active-brand.json`) | PASS |
| Profile digest | `a45e4ae4…c8cbe349` (`sha256sum profile.json`) | PASS (unchanged) |
| DMP version | `3.15.1` (plugin cache) | PASS |
| Frozen sources | 5/5 exact (`3ba91761…`) | PASS |
| TL-M5 human-input block | `809a94dd…83c4274`, 6/6 | PASS |
| Lease | Claude Phase A repair lease (this file set), no competing writer | PASS |

## 1. Source ledger (inputs used to author)

| Statement / input | Source path | Digest | Evidence status | Allowed use |
|---|---|---|---|---|
| Voice/định vị/messaging | `docs Toplink/brand/positioning.md` | `7c216e38…` | `TOPLINK_CONFIRMED` (hypothesis, non-public) | positioning claim |
| Narrative spine + founder guardrail | `docs Toplink/brand/narrative.md` | `02a6f6be…` | `TOPLINK_CONFIRMED` | narrative/founder allowed-use |
| 5 pillars + slot allocation | `docs Toplink/brand/content-pillars.md` | `b0790e2d…` (repaired) | `TOPLINK_CONFIRMED` | pillar mapping 6/6/8/4/4 |
| 4-week arc / cadence | `docs Toplink/brand/campaign-architecture.md` | `c1fda749…` | `TOPLINK_CONFIRMED` | calendar structure |
| Channel roles / CTA policy | `docs Toplink/brand/facebook-page-strategy.md` | `cdd1f786…` | `TOPLINK_CONFIRMED` | FB-first, CTA gate |
| KPI dictionary | `docs Toplink/brand/kpi-experiment-plan.md` | `40a528c6…` | `TOPLINK_CONFIRMED` | measurement mapping |
| Personas TL-A01..A04 | `docs Toplink/research/audience-hypotheses.md` | `4a32da6b…` | `HYPOTHESIS` | audience job framing |
| Preferred/forbidden phrasing + disclaimer §3.3 | `docs Toplink/02_communication_safety.md` | `94a9c5ea…` | `TOPLINK_CONFIRMED` | support phrasing + mandatory disclaimer |
| 4-floor space / 8-step process | `docs Toplink/Ho-so-…-2026.md` | `645b1ad2…` (frozen) | `TOPLINK_CONFIRMED` | operational proof |
| Product/dưỡng liệu | `docs Toplink/11_Product_Yvien.md` | `df367e1b…` | `UNVERIFIED` (`TL-GAP-010` fail-closed) | **customer-experience framing only** |
| Capacity/start/asset/scope | `00-input-lock.json` block `809a94dd…` | — | `LOCKED` (human 2026-08-03) | capacity/relative-date/placeholder-asset bounds |

**Không tự invent:** product/price/booking/qualification/legal/franchise/health-outcome/asset-rights/
reviewer-credential/performance. Missing = `MISSING_INPUT`.

## 2. Real authoring invocations (subagent dispatch; raw output + metadata captured)

Raw output + `.invocation.json` under `staging/toplink-reconciled/TL-M5-run1/raw-repair/`.
`native_skill_invoked=true`; `external_writes=0` every row.

| trace_id | capability | native subagent | raw output (sha256) | selected output(s) | disposition |
|---|---|---|---|---|---|
| `TL-M5-DMP-CAL-002` | content-calendar | `digital-marketing-pro:content-creator` | `TL-M5-DMP-CAL-002.md` `cceb73ba…` | `month-calendar.md` `0d2d2d16…`, `asset-and-batch-plan.md` `435969cf…` (unchanged) | KEEP |
| `TL-M5-DMP-ENG-002` | content-engine | `digital-marketing-pro:content-creator` | `TL-M5-DMP-ENG-002.md` `2f5d5218…` | `production-briefs.md` `42cb8e7d…`, `workflow-approval-measurement.md` `651dff61…` (unchanged) | KEEP |
| `TL-M5-DMP-VID-002` | video-script | `Short-Video Editing Coach` | `TL-M5-DMP-VID-002.md` `c97345a0…` | `reels-briefs.md` `51b18d91…` (unchanged) | KEEP |

- content-calendar independently re-verified pillar 6/6/8/4/4=28, 12 Reels, A/B/C daily, CTA follow/save/share,
  10 health + 4 founder = `NEEDS_HUMAN_REVIEW`, placeholder assets (direction B), relative D-1..D-28.
- content-engine confirmed support-language + mandatory §3.3 disclaimer on health items, fail-closed single
  human gate, product customer-experience-only/UNVERIFIED, no item `APPROVED`.
- video-script confirmed 12 Reels FB-first, TikTok mechanics-only, timestamps/safe-zone are in-file production
  mechanics, disclaimer on health Reels, no `APPROVED`.
- 5 canonical M5 deliverables **byte-unchanged** (disposition KEEP); real invocation supplies trace integrity.

## 3. DMP check (separate; evaluator scripts only)

`digital-marketing-pro:check` = `eval-runner.py --action run-full` + `hallucination-detector.py --action
detect`, `logged=false` ⇒ `external_writes=0`. Raw JSON under `raw-repair/check/`.

| Deliverable | composite | auto_rejected | halluc | critical |
|---|---:|---|---:|---:|
| month-calendar.md | 72 | false | 72 | 0 |
| asset-and-batch-plan.md | 80 | false | 80 | 0 |
| reels-briefs.md | 44 | false | 44 | 0 |
| production-briefs.md | 80 | false | 80 | 0 |
| workflow-approval-measurement.md | 80 | false | 80 | 0 |

**All 5 M5 deliverables: `auto_rejected=false`, 0 critical.** `reels-briefs` 44 = generic scorer flagging
in-file Reels timestamps / safe-zone mechanics (0–3s hook, 14%/20% safe-zone) — design values with in-file
provenance, not external performance stats. `production-briefs`/`workflow` "exclusive_claim/only" flags =
Vietnamese governance phrases ("GATE DUY NHẤT", "chỉ human owner") = fail-closed authority statements, not
brand superlatives. `claim-verifier extract-claims` = `total_claims=0` on public/health deliverables. No
fabricated fact. Deterministic check = PASS; agency/human layer stays `NEEDS_HUMAN_REVIEW` on
health/founder/product/public-positioning. No `APPROVED`.

## 4. Output hash re-confirmation (unchanged)

```text
0d2d2d1609910f7f5784ea98cd9e0820cda9d267314d9418e2e3b2f5b47ccb36  docs Toplink/content/month-calendar.md
435969cf0ae9e8badccb22451b7d4704b5733afa70ca43aac7aef9f324bc0acd  docs Toplink/content/asset-and-batch-plan.md
51b18d91f1d5dea5391192700260273c3e891ac9cfb9e95f59c0917dfdb60fd4  docs Toplink/content/reels-briefs.md
42cb8e7d916b1cbe8e48d7f2ac624ea9e83ce49c3420cb2da55814b48d00d429  docs Toplink/content/production-briefs.md
651dff61991fdc9c5669635cfacabebb4c006b4aa9b558739ce897fe80f109ed  docs Toplink/content/workflow-approval-measurement.md
```

All five byte-unchanged; real invocations did not mutate any deliverable. `external_writes=0`;
`milestone_advanced=false`; no `APPROVED`; Run 1 open; no Run 2.
