# Design — Toplink 24-dataset Sheet correction

## Architecture

The pipeline is `canonical Markdown + frozen ledgers → normalized records → registry validation →
deterministic dataset bundle → approval-bound correction → exact read-back`. Markdown remains the
human canonical layer; one canonical artifact may feed several datasets and one dataset may cite
several artifacts.

The schema registry is the single machine contract. Each dataset defines tab identity, ordered
columns, PK, typed FKs, enums, cardinality, validation, formatting, and read-back shape. Every record
includes `stable_row_key`, `record_id`, `source_path`, `source_location`, `source_id`,
`evidence_status`, `allowed_use`, `revision`, `source_digest`, `owner`, and `updated_at_ict`.

## Dataset groups

- Human/report: `TL_REPORT`, `TL_OWNER_ACTIONS`.
- Control/evidence: `TL_CONTROL`, `TL_SOURCE_INVENTORY`, `TL_INPUT_GAPS`, `TL_OUTPUT_INDEX`,
  `TL_DECISIONS`.
- Safety/measurement: `TL_KPI_DICTIONARY`, `TL_COMPLIANCE_RULES`.
- Brand/runtime: `TL_BRAND_PROFILE`, `TL_RUNTIME_COMPATIBILITY`, `TL_PAGE_BENCHMARK`.
- Strategy: `TL_AUDIENCE_HYPOTHESES`, `TL_POSITIONING`, `TL_NARRATIVE`, `TL_CONTENT_PILLARS`,
  `TL_FACEBOOK_STRATEGY`.
- Campaign/learning: `TL_CAMPAIGN`, `TL_EXPERIMENTS`.
- Execution: `TL_CONTENT_CALENDAR`, `TL_ASSET_BATCH_PLAN`, `TL_REELS_BRIEFS`,
  `TL_PRODUCTION_BRIEFS`.
- Approval: `TL_WORKFLOW_APPROVAL`.

## Compatibility and history

The prior payload, approval, read-back, and manifest digests are immutable. New Run 1/Run 2
correction addenda link those digests and explain why the prior technical read-back is not a valid
business-model delivery. Correction is a lane inside the existing two-run package, not a third run.

## Migration state machine

`LOCAL_COMPILED → LOCAL_VALIDATED → INDEPENDENT_REVIEW_PASS → BUNDLE_UNSIGNED → HUMAN_APPROVED →
TARGET_REVALIDATED → MUTATING → READBACK_PASS`.

Any pre-network mismatch is a hard stop. A partial mutation becomes `VERIFY_FAILED`; the executor
captures current state and never rolls back automatically. Recovery is a new bundle and approval.
Ten new tabs use `CREATE_TAB`; fourteen existing tabs use their exact live sheet IDs. All 24 tabs use
bounded `REPLACE_RANGE`, including a bounded stale-tail clear within the union of old/new used range.

## Security and approval

The bundle contains only the service-account email, never a key or credential path. Execution binds
the spreadsheet ID, email, operator, expiry, lease, target snapshot, tab IDs/titles, ranges, action
limits, and all content/schema/source/manifest digests. Agency or runtime verdicts cannot become
human `APPROVED`; material content edits reset approval.

## Operational trade-offs

Sidecars duplicate structured data intentionally so machines do not parse prose during operations.
The cost is more generated files, controlled by deterministic compilation and registry validation.
In-place replacement preserves workbook identity and existing tab IDs, while exact bounded ranges
avoid destructive workbook-wide operations.
