# Toplink Run 2 Phase B Codex audit and finalize

## Goal

Execute `TOPLINK_RUN2_FRESH_AUDIT_FINALIZE` Phase B exactly once from the supplied master prompt: independently audit the 14 Run 1 outputs, freeze the audit before reading Claude Phase A, reconcile findings, make only evidence-grounded in-place repairs, validate gates and paired manifests, and stop at a truthful local-only verdict.

## Background and confirmed facts

- N0 was recomputed read-only on 2026-08-04: Run 1 manifest `99227153de577887966ae09124fdabcb2b3bf8ff23d838503531be507c2f4d2d`, profile `a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349`, source aggregate `3ba91761612ca482471dc1c071bd7e9d82e5708a3bb13ceb630fed476541fe76`, 5/5 source members, and 14/14 outputs all match.
- DMP read-back is 3.15.1 and active brand is `toplink-y-vien`.
- No competing writer lease existed at N0. A planning lease was acquired and will be released before the approval pause.
- Claude Phase A withheld files have not been opened in this Codex run.

## Requirements

- Preserve the N0 lock invariants, Toplink isolation, exactly-two-run architecture, stable IDs, fail-closed human gates, and `external_writes=0` unless an exact signed Sheet approval exists.
- Acquire exactly one scoped Codex lease before Phase B writes and release it after checkpointing.
- Persist `20-blind-audit-codex.md` and `25-blind-freeze.json` before reading `run2/claude/**` or the handoff files.
- Audit the required eight axes and run the claim, asset, decision, and disclaimer reference-integrity scans.
- Merge both provenance ledgers with stable `TL-R2-M##` IDs and explicit route/status fields.
- Repair only independently reproduced or explicitly revalidated findings, in place and idempotently; use traced DMP reauthoring if any finding requires it.
- Validate gate integrity, rebuild and verify the paired Run 2 manifest, checkpoint `task.md`/`STATE.md`, and report the exact terminal verdict.
- Skip Sheet mutation and retain `SYNC_PENDING_TARGET` unless the operational contract's exact signed approval predicate is proven.

## Acceptance criteria

- [x] Blind audit exists and its digest is frozen before any withheld Phase A read.
- [x] Claude lock/output cross-check matches independent N0 evidence.
- [x] Merged ledger covers all Claude and Codex findings without lost provenance.
- [x] Reference-integrity scans have zero unresolved orphan IDs, except an explicitly fail-closed human-owned disclaimer-host gate.
- [x] Every repair has a named finding, minimal byte scope, old/new digest evidence, and preserved human/legal/privacy/consent gates.
- [x] Run 2 manifest parses, every path/digest reads back, and its profile/source/DMP/brand fields pair exactly with Run 1.
- [x] No `_v2`, Run 3, milestone `COMPLETE`, agent `APPROVED`, publish/Page mutation, unapproved Sheet write, secret, PII, or cross-brand reuse is introduced.
- [x] Lease is released and final report includes nodes, proofs, ledger, repairs, gates, sheet state, external writes, manifest digest, verdict, and next safe action.

## Out of scope

- Human/professional approval, final health disclaimer authorship, legal/franchise verification, publication, Page mutation, TL-M6, new product/brand facts, and any unapproved external write.

## Open questions

- None. The master prompt and canonical repository owners resolve execution choices; remaining human gates are deliverable states, not planning ambiguities.
