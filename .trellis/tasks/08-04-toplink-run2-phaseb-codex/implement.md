# Implementation plan

1. Re-run N0 immediately before implementation; acquire the exact Phase B lease.
2. Load `trellis-before-dev` package/spec guidance and only the canonical source windows required for the audit.
3. Execute N2 across all eight axes and mandatory reference-integrity scans; persist the blind audit.
4. Execute N3: hash/freeze audit with ICT timestamp and checkpoint the digest.
5. Execute N4–N5: gated Claude read, independent lock cross-check, merged stable-ID ledger.
6. Execute N6: resolve majors first, then minors/advisories; record minimal diffs and new digests after each repair.
7. Execute N7–N9: gate integrity, Run 2 manifest build, paired-manifest/path/hash/stable-ID validation.
8. Execute N10 only if exact signed Sheet approval exists; otherwise record `SYNC_PENDING_TARGET` and keep `external_writes=0`.
9. Run full scoped QA: JSON parse, digest/read-back, reference/orphan/duplicate IDs, UTF-8/newline, placeholder/secret/PII/isolation, prohibited claim/approval/publish states, and `git diff --check`.
10. Execute N11–N12: checkpoint evidence, release lease, update sprint fact, and report the single truthful terminal verdict.

## Rollback points

- After each canonical repair, revert only that finding's patch if its postcondition fails.
- Stop immediately on lock mismatch, temporal-cut breach, overlapping lease, unsafe claim drift, or missing evidence for a required mutation.
