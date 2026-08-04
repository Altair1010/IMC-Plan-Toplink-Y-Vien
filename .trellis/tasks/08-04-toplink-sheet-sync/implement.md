# Implementation order

1. RED: add offline tests for Markdown compilation, deterministic hashes, fail-closed approval validation, and exact read-back comparison.
2. GREEN: implement pure compiler/validator functions and CLI dry-run output.
3. Generate and validate the 14-tab V2 payload and unsigned approval envelope; update the Sheet contract/status checkpoint.
4. Run full local checks and a fresh `trellis-check` review; repair and re-run until PASS.
5. Present the exact approval statement. Stop with zero external writes until the user signs it.
6. After signature, revalidate all locks, execute `CREATE_TAB → UPSERT → READBACK` sequentially, persist evidence, run post-sync review, and commit the verified record.
