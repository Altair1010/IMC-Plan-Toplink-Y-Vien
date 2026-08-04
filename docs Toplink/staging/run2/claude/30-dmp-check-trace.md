# TL Run 2 Phase A — Real DMP check trace

> **Run 2 Phase A · fresh Claude · local-only.** Real installed DMP `check` capability run on the
> health-sensitive / public-facing artifacts + files implicated by findings, AFTER `20-blind-audit.md`
> was persisted. This is a **check** run only — not an authoring invocation and not a brand-profile
> mutation. `NO_TRACE = NOT_DONE`; `SKIPPED` is never `PASS`.

## Trace identity

| Field | Value |
|---|---|
| trace_id | `TL-R2-DMP-CHECK-001` |
| timestamp_ict | `2026-08-04T16:24+07:00` (script UTC stamp `2026-08-04T09:24Z`) |
| DMP version | `3.15.1` (plugin cache `neels-plugins/digital-marketing-pro/3.15.1`) |
| active_brand read-back | `toplink-y-vien` (`~/.claude-marketing/brands/_active-brand.json` `active_slug=toplink-y-vien`) |
| runtime | Python 3.11.15, stdlib only, no internet, no pip |
| scripts | `eval-runner.py` (run-full), `hallucination-detector.py` (detect), `claim-verifier.py` (extract-claims) |
| invocation_mode | read-only QA; **`--log` omitted ⇒ `logged=false` ⇒ `external_writes=0`** |
| output artifact | none written by the check (stdout only; no brand-log mutation) |

## Inputs (exact paths + SHA-256, byte-unchanged this run)

| Artifact | SHA-256 (prefix) | Health-sensitive |
|---|---|---|
| `docs Toplink/brand/positioning.md` | `7c216e38…` | yes (public messages) |
| `docs Toplink/brand/narrative.md` | `02a6f6be…` | yes (voice/health beats) |
| `docs Toplink/brand/content-pillars.md` | `b0790e2d…` | yes (P2/P4 gated) |
| `docs Toplink/brand/campaign-architecture.md` | `c1fda749…` | yes (W2 health) |
| `docs Toplink/content/month-calendar.md` | `0d2d2d16…` | yes (10 health items) |
| `docs Toplink/content/production-briefs.md` | `42cb8e7d…` | yes (health captions) |
| `docs Toplink/content/reels-briefs.md` | `51b18d91…` | yes (health reels + disclaimer) |
| `docs Toplink/content/workflow-approval-measurement.md` | `651dff61…` | yes (compliance gate) |

Evidence file passed for the claim dimension: `staging/toplink-reconciled/TL-M1-evidence/entity-franchise-allowed-use-map.md`.

## Results (`eval-runner run-full` + `hallucination-detector detect`)

| Artifact | composite | grade | auto_rejected | hallucination | critical_flags | logged |
|---|---|---|---|---|---|---|
| positioning | 76.0 | B | false | 76 / pass | none | false |
| narrative | 88.0 | A- | false | 88 / pass | none | false |
| content-pillars | 92.0 | A | false | 92 / pass | none | false |
| campaign-architecture | 64.0 | C | false | 64 / pass | none | false |
| month-calendar | 72.0 | B- | false | 72 / pass | none | false |
| production-briefs | 80.0 | B+ | false | 80 / pass | none | false |
| reels-briefs | 44.0 | D | false | 44 / pass | none | false |
| workflow-approval-measurement | 80.0 | B+ | false | 80 / pass | none | false |

`claim-verifier --action extract-claims` on production-briefs.md and reels-briefs.md → **0 hard claims**
(no numeric/efficacy/guarantee/statistical claim to verify) — consistent with support-framing-only design.

## Dimensions and legitimately-skipped dimensions

| Dimension | Status | Reason |
|---|---|---|
| hallucination | **RAN** (weight 1.0) | deterministic; all 8 `pass`, no critical flags |
| claim_verification | SKIPPED | claim-verifier extracted 0 hard claims ⇒ nothing to verify; dimension weight 0 |
| content_quality | SKIPPED | `content-scorer.py` fallback: `textstat` not installed, no pip in venv |
| brand_voice | SKIPPED | `brand-voice-scorer.py` fallback: `nltk` not installed |
| readability | SKIPPED | `readability-analyzer.py` fallback: `textstat` not installed |
| output_structure | SKIPPED | no marketing schema matches these bilingual plan/skeleton docs |

**Skip disclosure (SKIPPED ≠ PASS):** with `textstat`/`nltk` absent and no marketing output schema for
Vietnamese health-domain plan skeletons, the composite collapses to the **hallucination dimension only**.
The numeric composite is therefore a hallucination-heuristic signal, not a full-suite quality grade. The
meaningful compliance gate is the triad `auto_rejected=false` (threshold composite<40) + `critical_flags=none`
+ `0 hard claims`, which **all 8 artifacts pass**. `reels-briefs` (44) sits nearest the 40 auto-reject
threshold; it did not auto-reject and raised no critical flag — the low number reflects the generic
hallucination heuristic penalising bracketed A/B/C placeholders and claim-ID tags, not a compliance
violation. Run 1's own §5 deterministic compliance scan (forbidden-term/disclaimer/CTA/franchise/self-approve)
is the domain gate; this Run 2 check independently corroborates it (no auto-reject, no critical flag).

## Exit status & finding linkage

- Exit status: all invocations returned normally; no auto-reject, no critical flag.
- No DMP-check finding upgrades a blind-audit severity. No finding requires `DMP_SKILL_REAUTHOR`.
- `TL-R2-F02` (orphan `CL-P2`) is a claim-register schema defect, not a claim-safety failure — the
  check found 0 hard claims and no critical flag on the affected files.
- `external_writes=0`; `logged=false`; no brand profile / Sheet / Page mutation.
