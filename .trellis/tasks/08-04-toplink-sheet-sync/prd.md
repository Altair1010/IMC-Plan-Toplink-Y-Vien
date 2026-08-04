# Toplink deterministic Google Sheet sync

## Goal

Build deterministic 14-tab payload and fail-closed sync tooling, obtain digest-bound approval, then exact read-back with independent review.

## Requirements

- Compile the 14 Run 2 canonical Markdown artifacts into deterministic, per-tab cell payloads.
- Preserve one artifact per registered Toplink tab, stable identity, UTF-8 Vietnamese, evidence status, allowed-use, and unresolved human gates.
- Produce an unsigned digest-bound V2 approval envelope containing exact target, tab titles, used ranges, payload digests, action limits, service-account identity, expiry, and three explicit actions: `CREATE_TAB`, `UPSERT`, `READBACK`.
- Default to dry-run. Refuse every external mutation without an exact, unexpired approval statement matching the envelope path and SHA-256.
- Use the Toplink service account only from `GOOGLE_APPLICATION_CREDENTIALS`; never persist or log credential material.
- On approved execution, create only missing registered tabs, write only exact approved rectangles, preserve `Trang tính1`, and verify exact cell read-back before reporting success.
- Record delivery/read-back evidence without granting human `APPROVED` or milestone completion.
- Obtain an independent fresh-context review before requesting approval and again before closing an external sync.

## Acceptance Criteria

- [ ] Unit tests prove deterministic parsing, stable-key generation, Unicode preservation, formula-injection safety, duplicate rejection, approval validation, and read-back comparison.
- [ ] Dry-run compiles 14 unique tabs and passes schema, range, digest, secret, cross-brand, and Run 2 lock checks.
- [ ] V1 remains historical and unsigned; V2 explicitly supersedes it without creating `_v2` Sheet tabs.
- [ ] No connector/API mutation occurs before the exact V2 approval is received.
- [ ] An approved run cannot proceed from one phase to the next unless the previous phase's exact postcondition passes.
- [ ] Any target drift, lease conflict, expired approval, partial write, or read-back mismatch fails closed with an evidence-backed status.
- [ ] Reviewer findings are repaired and rechecked; local quality gates and secret scan pass before commit.

## Notes

- Target spreadsheet: `1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms`.
- External execution is intentionally a separate gated increment after the V2 digest is signed.
