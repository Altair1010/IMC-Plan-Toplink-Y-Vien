# Implementation plan — Toplink Run 1 TL-M5 reconciliation

1. Verify released lease, locks, profile/source/DMP/brand state, handoff paths and hashes, real invocation sidecars, approval flags, and zero external writes.
2. Acquire the exact Phase B lease in `task.md`.
3. Reconcile repaired TL-M2–TL-M4 provenance and TL-M5 into `10`–`70`, delta ledger, reviewer register, and manifest without new facts.
4. Run canonical lock, DMP, TL-M5 structure, safety, JSON/schema, path/hash/reference/orphan, encoding/newline, placeholder, secret/PII, isolation, and whitespace gates.
5. Write the evidence-backed Run 1 verdict; compute final manifest SHA-256; checkpoint `STATE.md` and `task.md`; release the lease.
6. Run Trellis quality checks, stage exact owned/provenance sets, create logical commits, and run final verification.
7. Do not invoke Run 2 or any external mutation.
