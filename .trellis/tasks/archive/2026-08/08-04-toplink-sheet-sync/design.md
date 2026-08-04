# Design — deterministic Toplink Sheet sync

## Components

- `.trellis/scripts/toplink_sheet_sync.py`: CLI for `compile`, `validate-approval`, and `execute`; dry-run by default.
- `docs Toplink/staging/run2/codex/61-sheet-payload-v2.json`: exact cells, ranges, stable keys, formatting requests, and per-tab digests.
- `docs Toplink/staging/run2/codex/62-sheet-target-approval-v2.json`: unsigned envelope binding the payload and three sequential actions.
- `docs Toplink/staging/run2/codex/63-sheet-readback-v2.json`: post-write metadata and per-tab exact comparisons without credentials.

## Payload model

Each tab contains a metadata block followed by named Markdown table blocks and prose-section rows. Existing explicit IDs are retained. Missing row IDs are deterministically derived from artifact stable ID, section slug, and row ordinal. All source content is sent as literal strings. The payload stores the exact A1 used range and SHA-256 over canonical UTF-8 JSON for every tab.

## External state machine

`COMPILED → LOCAL_VALIDATED → REVIEW_PASS → APPROVED → TABS_CREATED → WRITTEN_UNVERIFIED → READBACK_PASS`.

Every transition checks the signed envelope, current target metadata, lease, source/payload digests, action limit, and predecessor postcondition. An unexpected existing tab, target drift, partial response, or cell mismatch terminates with a blocked/failed record. No broad retry or cleanup mutation is automatic.

## Authentication

The executor loads the service-account file only from `GOOGLE_APPLICATION_CREDENTIALS`, verifies its `client_email`, requests the Sheets scope, and redacts all credential paths and values. Google client libraries are runtime dependencies checked before execution; compilation and unit tests remain offline.
