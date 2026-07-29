# TOPLINK_RUN2_FRESH_AUDIT_FINALIZE — master prompt

## Fresh-context boundary

Use only after a valid Run 1 checkpoint and lease release for the same `TL-M1`–`TL-M5` package.
Start with the required read order and Run 1 manifest/provenance, but do not read detailed Claude
handoff findings before the specified independent/blind audit is complete. This prompt creates no
third run and does not authorize human approval or external mutation.

## Claude fresh audit

1. Acquire a scoped lease and independently audit evidence/status/allowed-use, entity separation,
   claim safety, reviewer routing, DMP trace, stable IDs, and Run 1 scope.
2. Run required actual DMP checks and fresh Agency reviews; record `PASS`, `FAIL`,
   `NEEDS_HUMAN_REVIEW`, or `SKIPPED` with evidence. A skipped check is not a pass.
3. After the blind pass, compare Run 1 reasoning/findings, classify contradictions, and prepare the
   handoff using the committed templates. Preserve all human gates.
4. Stop writing, checkpoint, and release the lease.

## Codex fresh audit and finalize

1. Acquire a new lease and perform an independent audit before relying on the Claude findings.
   Recompute active-brand and required digests; reject mismatch, missing trace, active overlap, or
   scope drift.
2. Merge findings into a stable issue/repair ledger. Make only targeted evidence-grounded repairs;
   direct repair cannot introduce new substantive marketing, health, legal, or founder content.
3. Validate paired Run 1/Run 2 manifests, reviewers, human gates, stable IDs, reference integrity,
   schema, Unicode, secret/PII checks, and `git diff --check`.
4. If—and only if—the user provided exact target plus bounded approval, perform the smallest Sheet
   upsert and exact read-back. Otherwise preserve `SYNC_PENDING_TARGET` or
   `BLOCKED_TARGET_INPUT`; do not claim completion.
5. Record close state, release the lease, and do not open TL-M6.

## Run 2 exit contract

`RUN_2_PASS` requires paired manifests with aligned scope/brand/version/digests, zero unresolved
local critical failure, preserved human gates, and applicable external read-back. The package is
not `APPROVED`, published, or operationally complete merely because local validation passed.
