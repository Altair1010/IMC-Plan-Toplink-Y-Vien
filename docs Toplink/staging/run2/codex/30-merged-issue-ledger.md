# TOPLINK Run 2 — merged Claude/Codex issue ledger

## N4 handoff cross-check

- Codex temporal cut: `f56264b3a95d799b41313eee63a25a63bf90eb94627dbabaf4374005b0f82720` frozen before handoff read.
- Claude blind audit: envelope/actual SHA-256 `8625ceed415ae60bcc0202fa718608a73814693990389a196052518b1648ccaa` — MATCH.
- Seven envelope-listed Claude artifacts: 7/7 SHA-256 MATCH.
- Run locks: manifest `99227153…`, profile `a45e4ae4…`, source `3ba91761…`, DMP `3.15.1`, active brand `toplink-y-vien` — all match Codex N0.
- Canonical outputs at N4: 14/14 byte-match Run 1.
- Claude DMP check: `TL-R2-DMP-CHECK-001`, check-only, `logged=false`, all auto-rejected=false, 0 critical flags, 0 hard claims. Skipped dimensions remain SKIPPED, not PASS.
- Agency: Social `PASS`; PR and Short-Video `NEEDS_HUMAN_REVIEW`; Content `FAIL` on claim-reference integrity.

## Merged ledger

| Merged ID | Claude provenance | Codex provenance | Relation | Severity | Class | Route | Status |
|---|---|---|---|---|---|---|---|
| `TL-R2-M01` | `TL-R2-F02` | `TL-R2-C01` | AGREES | major | claim reference integrity (`CL-P2`) | `DIRECT_REPAIR` | RESOLVED_ZERO_ORPHAN |
| `TL-R2-M02` | `TL-R2-F08` | `TL-R2-C03` | AGREES | major | canonical disclaimer host | `HUMAN_GATE` + bounded interim annotation | INTERIM_ANNOTATED_FINAL_WORDING_PENDING_HUMAN |
| `TL-R2-M03` | — | `TL-R2-C02` | NEW | major | audience wording / professional-escalation safety | `DIRECT_REPAIR` | RESOLVED_SAFE_NARROWING |
| `TL-R2-M04` | `TL-R2-F01` | `TL-R2-C04` | AGREES | minor | `TL-D16..D20` canonical pointer | `DIRECT_REPAIR` | RESOLVED_CANONICAL_POINTER |
| `TL-R2-M05` | `TL-R2-F03` | `TL-R2-C05` | AGREES | minor | health-Reels count | `DIRECT_REPAIR` | RESOLVED_COUNT_5 |
| `TL-R2-M06` | `TL-R2-F04` | `TL-R2-C06` | AGREES | minor | distinct approval-ledger count / D26 binding | `DIRECT_REPAIR` | RESOLVED_14_DISTINCT_D26_BOUND |
| `TL-R2-M07` | `TL-R2-F05` | `TL-R2-C07` | AGREES | minor | logical Sheet dataset collision | `DIRECT_REPAIR` | RESOLVED_TL_CONTENT_PILLARS |
| `TL-R2-M08` | `TL-R2-F06` | `TL-R2-C08` | AGREES | minor | founder five-item window interpretation | `DIRECT_REPAIR` for explicit global-ratio QA note; content reassignment remains `HUMAN_GATE` | GLOBAL_RATIO_PASS_SLIDING_WINDOW_HUMAN_GATE |
| `TL-R2-M09` | `TL-R2-F07` | `TL-R2-C09` | AGREES | minor | emitted-ID namespace drift | `DIRECT_REPAIR` non-breaking family crosswalk | RESOLVED_NON_BREAKING_CROSSWALK |
| `TL-R2-M10` | `50-post-blind-reconciliation.md` omits F07/F08 while envelope/handoff/marker declare eight findings | N4 envelope read-back | CONTRADICTS | minor | Phase A reconciliation-count integrity | `DIRECT_REPAIR` in recipient ledger — retain all F01..F08 provenance; do not rewrite released Claude artifacts | RESOLVED_BY_MERGE |

## Run 1 blockers retained / revalidated

`TL-GAP-002`, `004`, `005`, `007`, `008`, `009`, `010`, `012`, `013`, `014`, public-positioning approval, final-disclaimer wording, founder/BTS/UGC consent, and asset rights remain fail-closed. They are `RUN1_ONLY_REVALIDATED` where the fresh audits did not independently create a new defect. No fresh result erases them.

## N5 verdict

`MERGED_LEDGER_COMPLETE · 10 ITEMS · 0 FAIL_BACK_TO_RUN1 · 0 DMP_SKILL_REAUTHOR`
