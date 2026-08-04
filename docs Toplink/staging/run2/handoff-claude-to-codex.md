# Handoff — Claude → Codex

## Envelope

- **Run/stage:** `TOPLINK_RUN2_FRESH_AUDIT_FINALIZE` · `claude_to_codex`
- **Prepared by / timestamp (ICT):** `Claude Code (claude-opus-4-8) · 2026-08-04T17:05:00+07:00`
- **Recipient:** `Codex CLI` (fresh context)
- **Lease:** `RELEASED` (after the release checkpoint below)
- **Read timing:** `after independent audit` — the fresh Codex MUST perform and persist its own blind
  audit BEFORE reading these Claude findings.

## Scope and provenance

- **Canonical inputs:** `docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md`, `docs Toplink/TOPLINK_PAGE_MILESTONES.md`,
  `docs/system/claude-codex-operating-contract.md`, `docs Toplink/staging/run1/00-input-lock.json`,
  `docs Toplink/staging/run1/run1-manifest.json`, the 5 frozen `source_digest` members,
  `staging/toplink-reconciled/TL-M1-evidence/entity-franchise-allowed-use-map.md`.
- **Locks recomputed (independent):** manifest `99227153…` · profile `a45e4ae4…` · source `3ba91761…`
  (5-member SHA LF-join + trailing LF) · DMP `3.15.1` · brand `toplink-y-vien` — ALL MATCH; 5/5 sources
  and 14/14 generated outputs byte-unchanged.
- **DMP check trace:** `TL-R2-DMP-CHECK-001` · DMP `3.15.1` · active-brand read-back `toplink-y-vien` ·
  `logged=false` · `external_writes=0` (`docs Toplink/staging/run2/claude/30-dmp-check-trace.md`).
- **Claude Phase A outputs (this run) + SHA-256:**

| Path | SHA-256 |
|---|---|
| `docs Toplink/staging/run2/claude/00-fresh-context-attestation.json` | see envelope JSON |
| `docs Toplink/staging/run2/claude/10-source-ledger.md` | see envelope JSON |
| `docs Toplink/staging/run2/claude/20-blind-audit.md` | `8625ceed415ae60bcc0202fa718608a73814693990389a196052518b1648ccaa` (frozen before withheld reads) |
| `docs Toplink/staging/run2/claude/30-dmp-check-trace.md` | see envelope JSON |
| `docs Toplink/staging/run2/claude/40-agency-review.md` | see envelope JSON |
| `docs Toplink/staging/run2/claude/50-post-blind-reconciliation.md` | see envelope JSON |

- **Stable IDs affected:** the 14 canonical outputs (unchanged this phase); findings reference
  `CL-P2`, `TL-D16`, `TL_PAGE_STRATEGY`, disclaimer `§3.3`.
- **Sheet delivery plan:** `BLOCKED_TARGET_INPUT` — no `SheetTargetApproval`; `SYNC_PENDING_TARGET`;
  no write performed.

## Reviewer and check results

| Reviewer/check | Verdict | Evidence/location | Required repair or gate |
|---|---|---|---|
| Real DMP `check` (`eval-runner`/`hallucination-detector`/`claim-verifier`) | `PASS` (all `auto_rejected=false`, 0 critical flags, 0 hard claims) | `30-dmp-check-trace.md` | content_quality/brand_voice/readability/output_structure/claim SKIPPED (no textstat/nltk/schema; 0 hard claims) — SKIPPED ≠ PASS |
| PR & Communications Manager | `NEEDS_HUMAN_REVIEW` | `40-agency-review.md` | disclaimer canonical host (`TL-R2-F08`); TL-D16 pointer; D26 tag |
| Social Media Strategist | `PASS` | `40-agency-review.md` | ID-namespace reconcile (`TL-R2-F07`) |
| Content Creator | `FAIL` | `40-agency-review.md` | `CL-P2` orphan (`TL-R2-F02`) — blocking on reference integrity |
| Short-Video Editing Coach | `NEEDS_HUMAN_REVIEW` | `40-agency-review.md` | reels count 5 (`TL-R2-F03`); `CL-P2` |

## Issue and repair ledger

| ID | Severity | Classification | Evidence | Allowed repair route | Status |
|---|---|---|---|---|---|
| `TL-R2-F02` | major | schema | month-calendar §3 + production-briefs §1 (`CL-P2` undefined, 12 refs) | DIRECT_REPAIR | open |
| `TL-R2-F08` | major | evidence | disclaimer §3.3 anchors to UNVERIFIED source; `system/health-compliance.md` absent | DIRECT_REPAIR + HUMAN_GATE | open |
| `TL-R2-F01` | minor | schema | `TL-D16` real (STATE.md L109 / task.md) but not in master §3 register | DIRECT_REPAIR | open |
| `TL-R2-F03` | minor | schema | reels VERIFY "6" vs actual 5 health Reels | DIRECT_REPAIR | open |
| `TL-R2-F04` | minor | schema | workflow §3 "10+6" double-counts D14/D26 (14 distinct) | DIRECT_REPAIR | open |
| `TL-R2-F05` | minor | schema | `TL_PAGE_STRATEGY` dataset double-assigned | DIRECT_REPAIR | open |
| `TL-R2-F06` | minor | strategy | founder-led D24 & D28 in one 5-window (global ratio OK) | DIRECT_REPAIR / HUMAN_GATE | open |
| `TL-R2-F07` | minor | schema | stable-ID namespace drift vs milestones §2.6 | DIRECT_REPAIR | open |

No `DMP_SKILL_REAUTHOR`, no `FAIL_BACK_TO_RUN1`. Reconciliation vs Run 1: all 8 are NEW or CONTRADICT
Run 1 (which reported them clean); Run 1's own orphan check ran at output-ID granularity and missed the
claim-ID level. See `50-post-blind-reconciliation.md`.

## Human gates, recipient constraints, and release

- **Human gate/blocker:** health per-item professional review (`TL-D13`/`TL-GAP-007`); public
  franchise/legal wording (`TL-GAP-002/009`); product dossier/efficacy (`TL-GAP-004/010`); offer/CTA
  (`TL-GAP-005`); founder/BTS/UGC consent; public positioning approval; final disclaimer wording
  (`TL-R2-F08`); Sheet target approval (`TL-GAP-008`). Owner = human owner; none is agent-approvable.
  Provenance `TL-GAP-012–014` remain fail-closed (`RUN1_ONLY_REVALIDATED`).
- **Allowed next action:** fresh Codex Phase B — persist its own blind audit first, then merge ledgers,
  repair the 8 defects in place (evidence-grounded, no new fact/claim/pillar/ID), update the Run 2
  manifest + re-verify digests, validate gate integrity, then paired-manifest validation. Sheet only on
  a separate exact `SheetTargetApproval` → bounded upsert → exact read-back.
- **Forbidden:** any external write / Page / Sheet / profile mutation without approval; new marketing
  version / `_v2` / third macro-run; milestone `COMPLETE`; human `APPROVED`; importing any Thảo Tây
  fact/target/credential/baseline.
- **Stop if:** profile/source/DMP/brand digest drift (`FAIL_BACK_TO_RUN1`), competing writer/lease,
  fake/skipped trace presented as PASS, prohibited claim, or secret/PII leak.

I stopped writing the leased file set, persisted this handoff, and released the lease above. This
handoff does not grant human approval. Maximum Claude Phase A verdict = `CLAUDE_RUN2_PHASE_A_HANDOFF_READY`.
