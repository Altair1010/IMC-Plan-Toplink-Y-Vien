# Toplink Google Sheets operational contract

## Status, authority, and scope

- **Contract ID:** TL-SHEET-001 · **Version:** 0.1.1 · **Status:** TARGET_PROVIDED · PENDING_SA_AND_BOUNDED_APPROVAL.
- **Decision owner:** docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md; **execution/Done owner:**
  docs Toplink/TOPLINK_PAGE_MILESTONES.md; **safety owner:** RULES.md.
- **Scope:** a future Toplink-only operational workbook with functional parity to the approved
  DMP-to-Sheet workflow: control, evidence, output, compliance, planning, production, approval,
  measurement, stable identity, and exact read-back.
- **Out of scope:** creating a workbook or tab now; using any Thảo Tây workbook, sheet ID, tab,
  row, formula, output, baseline, credential, or identifier; copying external data; publishing;
  changing the DMP runtime/profile; granting human approval.

This contract defines the required architecture before a target exists. It is not an external-write
approval. Until the user supplies a new Toplink spreadsheet plus bounded authorization, every
record stays LOCAL_VERIFIED or STAGING with SYNC_PENDING_TARGET.

## 0. Provided target and auth plan (2026-07-30)

The user supplied an exact Toplink-only target and chose an isolation-clean auth path. This section
records the target; it is **not yet** a complete `SheetTargetApproval` (SA + bounded fields + read-back
still pending), so no write may occur.

| Field | Value | Status |
|---|---|---|
| `spreadsheet_id` | `1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms` | `USER_PROVIDED` (Toplink-only workbook) |
| Auth mechanism | **New dedicated Toplink service account** | `USER_DECISION` — no Thảo Tây credential reuse |
| SA email | — | `PENDING_USER` (user creates SA in GCP, grants Editor on the sheet) |
| SA key | local gitignored `GOOGLE_APPLICATION_CREDENTIALS` path | `PENDING_USER` — never committed, never in chat |
| Write operator | Codex CLI | per DMP-to-Sheet sequence §4 |
| `TL_PAGE_BENCHMARK` seed | Page ID `61591880797654` (baseline task start 2026-07-30, follower 0) | `LOCAL_VERIFIED · SYNC_PENDING` |

**Isolation guard:** the SA must be a new Toplink-only identity. Reusing the Thảo Tây service account
or any Thảo Tây credential is forbidden (`CLAUDE.md` external-state rule). Claude does not source,
handle, or expose any SA key; Codex performs SA wiring and the bounded write through the approved flow.

**Still required before any write** (§1 entry condition, §2 `SheetTargetApproval`): SA email + Editor
grant confirmed, tab_keys, ranges/schemas, action, limits, authorized_agent, expiry, and read-back.
Missing any field ⇒ `BLOCKED_TARGET_INPUT`; retain local staging.

## 1. Scope / trigger

**Trigger:** The user requires the same operational mechanism used for the other brand, but with an
independent Toplink profile and output set.

**Decision:** Preserve functional parity, not identity parity. Toplink uses TL_ stable keys and
Toplink-only source/output records. A referenced Thảo Tây workbook may explain the desired class of
workflow, but cannot be a template, destination, baseline, or source of values.

**Entry condition for external delivery:** all of the following must be explicit in one user
authorization: spreadsheet ID/URL, intended tab key(s), range/schema, exact action, record limits,
agent/operator, expiry, and read-back requirement.

## 2. Signatures and delivery contracts

### SheetTargetApproval

~~~text
spreadsheet_id: string                 # new Toplink-only workbook
tab_keys: string[]                     # keys from the registry below
ranges: { tab_key: A1-range }          # bounded per tab
schemas: { tab_key: schema_version }
action: CREATE_TAB | UPSERT | READBACK
limits: { max_tabs, max_rows_per_tab }
authorized_agent: Codex CLI | named operator
expires_at_ict: ISO-8601
~~~

Missing, mismatched, expired, or broad fields yield BLOCKED_TARGET_INPUT; they are never filled
from an old workbook or an agent guess.

### SheetDeliveryRecord

~~~text
record_id · artifact_path · artifact_digest · dmp_trace_id
dataset_key · tab_key · stable_row_key · schema_version
local_status · sheet_status · write_action · readback_digest
written_at_ict · verified_at_ict · blocker_ids
~~~

record_id is immutable. A material artifact change increments its revision/hash and requires the
applicable review/gate again; it does not create a _v2 tab or overwrite an unrelated record.

## 3. Toplink tab registry

The following are **proposed Toplink keys/titles**, not tabs that now exist. Each logical output is
mapped once through TL_OUTPUT_INDEX; a re-run upserts the same tab_key and stable row key.

| Tab key | Primary milestone | Local source class | Stable row key |
|---|---|---|---|
| TL_CONTROL | TL-M0–TL-M9 | target metadata, delivery state, revisions | control_key |
| TL_SOURCE_INVENTORY | TL-M1 | source manifest | source_id |
| TL_INPUT_GAPS | TL-M1 | input-gap register | gap_id |
| TL_OUTPUT_INDEX | TL-M0–TL-M9 | artifact/delivery index | record_id |
| TL_DECISIONS | TL-M0–TL-M9 | decision register | decision_id |
| TL_KPI_DICTIONARY | TL-M4 | KPI/experiment plan | kpi_id |
| TL_COMPLIANCE_RULES | TL-M1–TL-M5 | health/legal/privacy taxonomy | rule_id |
| TL_BRAND_PROFILE | TL-M2 | profile/source-digest map | profile_field_id |
| TL_PAGE_BENCHMARK | TL-M3 | Page identity/baseline only | page_snapshot_id |
| TL_AUDIENCE_HYPOTHESES | TL-M3 | audience hypotheses | audience_id |
| TL_POSITIONING | TL-M3 | positioning/narrative constraints | positioning_id |
| TL_CAMPAIGN | TL-M4 | relative campaign architecture | campaign_item_id |
| TL_CONTENT_PILLARS | TL-M3 | weighted pillar decision | pillar_id |
| TL_EXPERIMENTS | TL-M4–TL-M8 | experiment ledger | experiment_id |
| TL_CONTENT_CALENDAR | TL-M5 | relative calendar | content_id |
| TL_FACEBOOK_STRATEGY | TL-M3 | Facebook Page strategy | strategy_id |
| TL_ASSET_BATCH_PLAN | TL-M5 | asset and capacity plan | asset_batch_id |
| TL_REELS_BRIEFS | TL-M5 | Facebook-first Reels briefs | reel_id |
| TL_PRODUCTION_BRIEFS | TL-M5 | production briefs | production_id |
| TL_WORKFLOW_APPROVAL | TL-M5–TL-M6 | approval/measurement ledger | approval_id |

No title may use a Thảo Tây identifier. A tab only becomes real after an approved target and a
bounded CREATE_TAB action. It must then retain the listed tab_key; a revision changes rows, not
the tab title.

## 4. Data and mapping rules

### Common provenance fields

Every operational row carries its stable row key, record_id where an artifact exists,
source_path/source_id, evidence_status, allowed_use, revision_or_digest, owner, and updated_at_ict.
Unknown values are explicit (MISSING_INPUT, UNVERIFIED, or DO_NOT_USE), not blank values presented
as facts.

### Required dataset fields

| Dataset | Minimum additional fields |
|---|---|
| TL_SOURCE_INVENTORY | relative path, SHA-256, UTF-8 policy, category, exclusion reason |
| TL_INPUT_GAPS | requested input, owner, blocked milestone, unblock action, status |
| TL_OUTPUT_INDEX | local path/digest, DMP trace, tab_key, delivery/read-back status |
| TL_DECISIONS | decision, authority, date, allowed effect, review condition |
| TL_COMPLIANCE_RULES | claim/risk class, source, permitted wording boundary, human gate |
| TL_BRAND_PROFILE | field name, source/allowed-use reference, profile digest, mutation gate |
| TL_PAGE_BENCHMARK | Page URL/ID, snapshot timestamp, platform-signal meaning, measured values |
| TL_CONTENT_CALENDAR | content ID, relative day, pillar, claim IDs, CTA class, revision, approval state |
| TL_WORKFLOW_APPROVAL | content hash, reviewer role, verdict, conditions/expiry, publish state |

Product/service, legal, qualification, pricing, availability, Page identity, and health fields may
only be written with their source/status/allowed-use. A sheet schema never upgrades evidence.

### DMP-to-Sheet sequence

1. **Claude Code** invokes DMP only into local staging and records the real trace; it does not run
   production connectors or write a Sheet.
2. **Codex CLI** validates the artifact digest, source/profile gate, registry mapping, schema, and
   stable row key.
3. After explicit SheetTargetApproval, Codex performs the smallest allowed CREATE_TAB or upsert,
   then exact read-back of values, IDs, row count, required fields, formulas/validation where
   applicable, and Vietnamese Unicode.
4. Codex records the read-back in the paired manifest and TL_OUTPUT_INDEX. Acknowledgment without
   read-back is VERIFY_FAILED.

## 5. Validation and error matrix

| Condition | Required status | Permitted response |
|---|---|---|
| Target, tab, range, schema, or expiry absent | BLOCKED_TARGET_INPUT | retain local staging; request exact approval |
| Target is not Toplink-only or matches Thảo Tây scope | REJECT_TARGET | no connector call; request a new target |
| Artifact lacks trace/digest/stable key | BLOCKED_SCHEMA | repair local artifact or return to originating run |
| Source/claim/Page/legal field lacks proof | MISSING_INPUT / DO_NOT_USE | retain a blocker; never invent a value |
| Wrong tab key, schema, or duplicate stable row | BLOCKED_SCHEMA | stop before write; repair map locally |
| Partial write, wrong row count, or mismatched read-back | VERIFY_FAILED | preserve evidence, do not retry broadly, escalate exact repair |
| Active lease, concurrent writer, or target changed | BLOCKED_LOCK / BLOCKED_AUTH | stop and reacquire/re-authorize |

## 6. Good, base, and bad cases

- **Good:** The user approves one new Toplink workbook, TL_SOURCE_INVENTORY, a bounded range and
  an upsert limit. Codex verifies the local source manifest, writes only those records, and reads
  back IDs, count, values, and Unicode.
- **Base:** The local artifact and registry mapping are ready but no target is approved. Its state is
  LOCAL_VERIFIED · SYNC_PENDING_TARGET; no tab is created.
- **Bad:** An agent copies a tab, formula, baseline, or output from the Thảo Tây workbook, guesses a
  target/range, creates a _v2 tab, or calls a connector without a read-back. Stop and record the
  applicable error status.

## 7. Tests and audit evidence

Before any external write, the operator must prove:

1. every requested tab_key is in this registry and maps to exactly one artifact/dataset;
2. artifact and DMP trace digests match the handoff/manifest;
3. no target/ID/tab/row comes from Thảo Tây scope;
4. exact approval fields and lease are current;
5. pre-write target/range/schema/validation read is captured; and
6. post-write read-back verifies stable IDs, row count, required fields, formulas/validation where
   relevant, and Vietnamese Unicode.

git diff --check, link validation, JSON-template parsing, and a contract-reference search are
required for changes to this contract or its scaffolds.

## 8. Wrong vs correct

**Wrong:** “DMP created a local file, therefore create a similar tab in the previous brand’s
workbook.”

**Correct:** “DMP created a traced Toplink artifact; Codex maps its Toplink stable ID to a registered
TL_ tab only after the user approves a new Toplink workbook, exact range/schema/action/limits, and
Codex can read the result back.”

