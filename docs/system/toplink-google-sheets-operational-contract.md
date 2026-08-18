# Toplink Google Sheets operational contract

## Status, authority, and scope

- **Contract ID:** TL-SHEET-001 · **Version:** 0.3.0 · **Status:**
  `HUMAN_LAYER_LOCAL_BUILD · BOUNDED_APPROVAL_PENDING · HUMAN_GATES_PENDING`.
- **0.3.0 changes:** the delivered surface is now the 21-tab `YV_` human layer, not the 24-tab `TL_`
  dataset layer (§3); read-back is mandatory for **format as well as value** (§4, §7); the default tab
  `Trang tính1` (sheetId 0) is a preserved object; ACTION_REQUIRED colour uses direct format only and
  the post-write conditional-format rule count must be 0.
- **Decision owner:** docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md; **execution/Done owner:**
  docs Toplink/TOPLINK_PAGE_MILESTONES.md; **safety owner:** RULES.md.
- **Scope:** the provided Toplink-only operational workbook with functional parity to the approved
  DMP-to-Sheet workflow: control, evidence, output, compliance, planning, production, approval,
  measurement, stable identity, and exact read-back.
- **Out of scope:** creating a workbook; creating a tab or writing without an exact signed approval; using any Thảo Tây workbook, sheet ID, tab,
  row, formula, output, baseline, credential, or identifier; copying external data; publishing;
  changing the DMP runtime/profile; granting human approval.

This contract defines the required architecture after the target and dedicated SA were supplied. It
is not an external-write approval. Until the user signs the exact bounded action payload, every record
stays LOCAL_VERIFIED or STAGING with SYNC_PENDING_APPROVAL.

The Run 2 V2 payload and unsigned approval envelope are respectively
`docs Toplink/staging/run2/codex/61-sheet-payload-v2.json` and
`docs Toplink/staging/run2/codex/62-sheet-target-approval-v2.json`. The approval envelope binds the
payload file digest plus each tab's title, range, schema, dimensions, and payload digest; its V2 suffix
is an envelope revision only and never authorizes a `_v2` tab. A human's exact digest-bound approval
statement remains required before any Google API call.

The human owner signed that exact V2 envelope digest on 2026-08-04. Codex executed only its three
bound phases and recorded 14/14 exact tab read-backs at
`docs Toplink/staging/run2/codex/63-sheet-readback-v2.json` (SHA-256
`be0e0efca02f3a7d5cba09cc404d3dba02ecc77a268d57de8b4d43d824caa719`). This closes only the signed
V2 delivery. It is immutable historical `TECHNICAL_READBACK_PASS · BUSINESS_MODEL_FAILED`: the
cells matched the approved prose payload, but the payload was not an operational data model. Any
correction mutation requires a new current digest-bound approval.

The human owner then deleted all 24 `TL_*` tabs from the target workbook. The workbook is near-empty
again and holds only `Trang tính1`, so the next delivery is a fresh `CREATE_TAB`, not a repair of
live rows. The replacement surface is the 21-tab `YV_` human layer specified in
`docs/system/yvien-sheet-human-layer-spec.md` and enumerated by
`docs/system/yvien-sheet-dataset-registry.json` (`YV-SHEET-001`). Its deterministic build contract is
`staging/yv-humanize/report-plan.json` (`YV-REPORT-PLAN-001`), `state: DRAFT_UNSIGNED · LOCAL_ONLY`,
`write_executed: false`, `external_writes: 0`, `workbook_content_hash`
`8cbb4e12ff6c8054b969e4c44ab4432bd4b2def3303ba03697c1aceec84e338b`. That file is the instruction, not
a suggestion: the executor writes the `values` matrix it declares and nothing else.

No dataset was dropped. The 24 machine datasets survive in full as JSON sidecars under `staging/`;
only the display surface changed.

## 0. Provided target and auth plan (2026-07-30)

The user supplied an exact Toplink-only target and dedicated auth identity. This section records
the infrastructure that was later bound by the signed V2 `SheetTargetApproval`; it does not authorize
any future mutation.

| Field | Value | Status |
|---|---|---|
| `spreadsheet_id` | `1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms` | `USER_PROVIDED` (Toplink-only workbook) |
| Auth mechanism | **New dedicated Toplink service account** | `USER_DECISION` — no Thảo Tây credential reuse |
| SA email | `yvien-sheet-writer@imcforyvien.iam.gserviceaccount.com` | `USER_CONFIRMED_READY`; local key `client_email` read-back MATCH |
| SA key | gitignored `.secrets/imcforyvien-de7e7ee958f4.json` | `LOCAL_KEY_PRESENT`; key material never committed or printed; process env binding required at execution |
| Editor grant / Sheets API | dedicated SA has Editor; API enabled | `USER_CONFIRMED_READY`; not a write approval |
| Write operator | Codex CLI | per DMP-to-Sheet sequence §4 |
| `TL_PAGE_BENCHMARK` seed | Page ID `61591880797654` (baseline task start 2026-07-30, follower 0) | `LOCAL_VERIFIED · SYNC_PENDING` |

**Isolation guard:** the SA must be a new Toplink-only identity. Reusing the Thảo Tây service account
or any Thảo Tây credential is forbidden (`CLAUDE.md` external-state rule). Claude does not source,
handle, or expose any SA key; Codex performs SA wiring and the bounded write through the approved flow.

**Required before every new write** (§1 entry condition, §2 `SheetTargetApproval`): signed tab_keys,
ranges/schemas, one exact action per approval record, limits, authorized_agent, expiry, and read-back.
The V2 approval satisfied these fields only for its completed run. Missing or changed fields in a later
correction ⇒ `BOUNDED_APPROVAL_PENDING`; retain local staging.

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
readback_required: true
write_executed: false                  # single-use; an approval already true is refused
plan_digest: sha256                    # binds staging/yv-humanize/report-plan.json
workbook_content_hash: sha256          # binds the exact content that may be written
signer: human owner
signed_at_ict: ISO-8601
~~~

Missing, mismatched, expired, or broad fields yield BLOCKED_TARGET_INPUT; they are never filled
from an old workbook or an agent guess.

A human may sign an exact local draft by citing its repository path plus SHA-256 and stating
`APPROVED`; the signed statement binds every field in that digest. A multi-step delivery uses one
approval record per action (`CREATE_TAB`, `UPSERT`, then `READBACK`); approval of one action never
implies the next.

### SheetDeliveryRecord

~~~text
record_id · artifact_path · artifact_digest · dmp_trace_id
dataset_key · tab_key · stable_row_key · schema_version
local_status · sheet_status · write_action · readback_digest
written_at_ict · verified_at_ict · blocker_ids
~~~

record_id is immutable. A material artifact change increments its revision/hash and requires the
applicable review/gate again; it does not create a _v2 tab or overwrite an unrelated record.

## 3. Toplink tab registry — 21 `YV_` tabs

Authoritative machine copy: `docs/system/yvien-sheet-dataset-registry.json` (`YV-SHEET-001`). The old
24-key `TL_*` registry is `SUPERSEDED`; it is retained for provenance and must not be used to plan a
write. None of these tabs exists in the target yet, so the first authorized mutation is `CREATE_TAB`.

Tab index is part of the contract: `report` is index 0, `00_Y_VIEN_CAN_CHOT` index 1. Those are the
two tabs a human opens first, so they lead.

| # | Tab key | Rows × cols | Bounded range | Evidence / allowed use | Yellow cells |
|---|---|---|---|---|---|
| 0 | `report` | 121 × 11 | `'report'!A1:K121` | INFERENCE / INTERNAL_ONLY | 0 |
| 1 | `00_Y_VIEN_CAN_CHOT` | 25 × 14 | `'00_Y_VIEN_CAN_CHOT'!A1:N25` | TOPLINK_CONFIRMED / OPERATIONAL_CONTROL | 18 |
| 2 | `00_CONTROL` | 32 × 9 | `'00_CONTROL'!A1:I32` | TOPLINK_CONFIRMED / OPERATIONAL_CONTROL | 1 |
| 3 | `01_SOURCE_INVENTORY` | 24 × 8 | `'01_SOURCE_INVENTORY'!A1:H24` | TOPLINK_CONFIRMED / OPERATIONAL_CONTROL | 0 |
| 4 | `02_INPUT_GAPS` | 15 × 7 | `'02_INPUT_GAPS'!A1:G15` | TOPLINK_CONFIRMED / OPERATIONAL_CONTROL | 0 |
| 5 | `03_OUTPUT_INDEX` | 21 × 9 | `'03_OUTPUT_INDEX'!A1:I21` | TOPLINK_CONFIRMED / OPERATIONAL_CONTROL | 0 |
| 6 | `04_DECISIONS` | 19 × 10 | `'04_DECISIONS'!A1:J19` | TOPLINK_CONFIRMED / OPERATIONAL_CONTROL | 0 |
| 7 | `05_KPI_DICTIONARY` | 14 × 15 | `'05_KPI_DICTIONARY'!A1:O14` | INFERENCE / INTERNAL_ONLY | 2 |
| 8 | `06_COMPLIANCE_RULES` | 27 × 10 | `'06_COMPLIANCE_RULES'!A1:J27` | TOPLINK_CONFIRMED / INTERNAL_ONLY | 0 |
| 9 | `YV_01_brand_profile` | 23 × 8 | `'YV_01_brand_profile'!A1:H23` | INFERENCE / INTERNAL_ONLY | 0 |
| 10 | `YV_02_audience` | 11 × 9 | `'YV_02_audience'!A1:I11` | HYPOTHESIS / HYPOTHESIS_VALIDATION_ONLY | 0 |
| 11 | `YV_03_positioning` | 19 × 7 | `'YV_03_positioning'!A1:G19` | HYPOTHESIS / HYPOTHESIS_VALIDATION_ONLY | 0 |
| 12 | `YV_04_narrative` | 22 × 6 | `'YV_04_narrative'!A1:F22` | HYPOTHESIS / HYPOTHESIS_VALIDATION_ONLY | 0 |
| 13 | `YV_05_content_pillars` | 7 × 10 | `'YV_05_content_pillars'!A1:J7` | HYPOTHESIS / HYPOTHESIS_VALIDATION_ONLY | 0 |
| 14 | `YV_06_page_strategy` | 27 × 12 | `'YV_06_page_strategy'!A1:L27` | INFERENCE / INTERNAL_ONLY | 0 |
| 15 | `YV_07_campaign` | 6 × 10 | `'YV_07_campaign'!A1:J6` | HYPOTHESIS / HYPOTHESIS_VALIDATION_ONLY | 3 |
| 16 | `YV_08_experiments` | 5 × 14 | `'YV_08_experiments'!A1:N5` | HYPOTHESIS / HYPOTHESIS_VALIDATION_ONLY | 0 |
| 17 | `YV_09_content_calendar` | 86 × 17 | `'YV_09_content_calendar'!A1:Q86` | HYPOTHESIS / HYPOTHESIS_VALIDATION_ONLY | 0 |
| 18 | `YV_10_production_briefs` | 86 × 21 | `'YV_10_production_briefs'!A1:U86` | HYPOTHESIS / HYPOTHESIS_VALIDATION_ONLY | 0 |
| 19 | `YV_11_asset_batch_plan` | 16 × 11 | `'YV_11_asset_batch_plan'!A1:K16` | HYPOTHESIS / HYPOTHESIS_VALIDATION_ONLY | 3 |
| 20 | `YV_12_workflow_approval` | 86 × 20 | `'YV_12_workflow_approval'!A1:T86` | INFERENCE / INTERNAL_ONLY | 0 |

Total 27 yellow cells. `report` stacks three tables in one grid (§A rows 4–22, §B rows 25–109,
§C rows 112–121); each section has its own header row, and the column count is the widest section.

`Trang tính1` (sheetId 0) is a **preserved object**: never renamed, never written, never deleted, and
its presence is re-verified after the write. No title may use a Thảo Tây identifier or a `_v2` suffix.
A revision changes rows, never the tab title.

### 24 datasets → 21 tabs

The merge is deliberate; it is not a 1:1 port.

| `YV_` tab | Absorbed `TL_` datasets |
|---|---|
| `report` | `TL_REPORT` (rebuilt as three human tables) |
| `00_Y_VIEN_CAN_CHOT` | `TL_OWNER_ACTIONS` |
| `00_CONTROL` | `TL_CONTROL` + `TL_RUNTIME_COMPATIBILITY` |
| `01_SOURCE_INVENTORY` | `TL_SOURCE_INVENTORY` |
| `02_INPUT_GAPS` | `TL_INPUT_GAPS` |
| `03_OUTPUT_INDEX` | `TL_OUTPUT_INDEX` |
| `04_DECISIONS` | `TL_DECISIONS` |
| `05_KPI_DICTIONARY` | `TL_KPI_DICTIONARY` |
| `06_COMPLIANCE_RULES` | `TL_COMPLIANCE_RULES` + claim register `CL-*` |
| `YV_01_brand_profile` | `TL_BRAND_PROFILE` |
| `YV_02_audience` | `TL_AUDIENCE_HYPOTHESES` |
| `YV_03_positioning` | `TL_POSITIONING` |
| `YV_04_narrative` | `TL_NARRATIVE` |
| `YV_05_content_pillars` | `TL_CONTENT_PILLARS` |
| `YV_06_page_strategy` | `TL_FACEBOOK_STRATEGY` + `TL_PAGE_BENCHMARK` |
| `YV_07_campaign` | `TL_CAMPAIGN` |
| `YV_08_experiments` | `TL_EXPERIMENTS` |
| `YV_09_content_calendar` | `TL_CONTENT_CALENDAR` |
| `YV_10_production_briefs` | `TL_PRODUCTION_BRIEFS` + `TL_REELS_BRIEFS` |
| `YV_11_asset_batch_plan` | `TL_ASSET_BATCH_PLAN` |
| `YV_12_workflow_approval` | `TL_WORKFLOW_APPROVAL` |

`03_OUTPUT_INDEX` still maps every artifact to a tab with no orphan record, and it holds the index
only — never the content itself.

### Run 2 canonical 14-output mapping (historical, `SUPERSEDED`)

The tab column below records the tab keys of the deleted 24-tab delivery. Use §3 above for any write.

| Output stable ID | Artifact | Tab key |
|---|---|---|
| TL-BRAND-PROFILE-001 | `docs Toplink/brand/dmp-profile.md` | TL_BRAND_PROFILE |
| TL-RUNTIME-COMPAT-001 | `docs Toplink/system/runtime-compatibility.md` | TL_RUNTIME_COMPATIBILITY |
| TL-AUDIENCE-001 | `docs Toplink/research/audience-hypotheses.md` | TL_AUDIENCE_HYPOTHESES |
| TL-POSITIONING-001 | `docs Toplink/brand/positioning.md` | TL_POSITIONING |
| TL-NARRATIVE-001 | `docs Toplink/brand/narrative.md` | TL_NARRATIVE |
| TL-PILLARS-001 | `docs Toplink/brand/content-pillars.md` | TL_CONTENT_PILLARS |
| TL-PAGE-STRATEGY-001 | `docs Toplink/brand/facebook-page-strategy.md` | TL_FACEBOOK_STRATEGY |
| TL-CAMPAIGN-001 | `docs Toplink/brand/campaign-architecture.md` | TL_CAMPAIGN |
| TL-KPI-001 | `docs Toplink/brand/kpi-experiment-plan.md` | TL_KPI_DICTIONARY |
| TL-M5-CALENDAR-001 | `docs Toplink/content/month-calendar.md` | TL_CONTENT_CALENDAR |
| TL-M5-ASSET-001 | `docs Toplink/content/asset-and-batch-plan.md` | TL_ASSET_BATCH_PLAN |
| TL-M5-REELS-001 | `docs Toplink/content/reels-briefs.md` | TL_REELS_BRIEFS |
| TL-M5-PRODBRIEF-001 | `docs Toplink/content/production-briefs.md` | TL_PRODUCTION_BRIEFS |
| TL-M5-WORKFLOW-001 | `docs Toplink/content/workflow-approval-measurement.md` | TL_WORKFLOW_APPROVAL |

Every artifact receives one or more mapping records in `TL_OUTPUT_INDEX`. A dataset may aggregate
records from multiple artifacts, and an artifact may feed multiple datasets. There is no artifact
“primary tab” requirement and no `_v2` key.

## 4. Data and mapping rules

### Three layers

- **Front** — the visible columns, in reading order, headed in Vietnamese. A human reads a plan here.
- **Back** — the JSON sidecars under `staging/`, holding the full machine record.
- **Bridge** — two hidden columns in every tab, plus the deterministic generator that produces
  `report-plan.json`.

### Common provenance fields

Every operational row carries `stable_row_key`, `record_id`, `source_path`, `source_location`,
`source_id`, `evidence_status`, `allowed_use`, `revision`, `source_digest`, `owner`, and
`updated_at_ict`.
Unknown values are explicit (MISSING_INPUT, UNVERIFIED, or DO_NOT_USE), not blank values presented
as facts. A cell that is empty on purpose carries `—`, never `""`.

**These 11 fields never appear on the front.** They ride in the last two columns of every tab:

| Column | Position | Content |
|---|---|---|
| `_key` | second to last | `stable_row_key` |
| `_audit` | last | 9 fields joined by ` · `: `record_id · source_path#source_location · source_id · evidence_status · allowed_use · revision · source_digest · owner · updated_at_ict` |

Both carry `hiddenByUser = true` in all 21 tabs. A visible cell containing a machine field name or an
undeclared technical ID is a build failure, not a cosmetic issue; each tab declares its own
`visible_id_allowed` pattern and anything outside it fails closed.

### ACTION_REQUIRED (yellow) contract

A cell is yellow **iff** its text begins with `CHƯA CHỐT — `. There is no second rule and no
inference from status alone: a technical status is not by itself a reason to colour a cell. The text
must name a role and the action that role owes, in one sentence, at most 210 characters
(`docs/system/yvien-brand-voice-pack.md §6`). Fallback rows carry `DỰ PHÒNG — ` and are never yellow.
Yellow means neither `APPROVED` nor rejected — it means a human still owes a decision.

Every open `TL-GAP-*` has exactly one row in `00_Y_VIEN_CAN_CHOT` with exactly one yellow cell.

### Format contract

| Property | Required value |
|---|---|
| Header row | row 1 · legend row 2 · data from row 3 |
| `frozenRowCount` | 2 |
| `basicFilter` | present |
| `wrapStrategy` | `WRAP` |
| `verticalAlignment` | `TOP` |
| ACTION_REQUIRED colour | `#f7e8c2`, applied by `repeatCell.userEnteredFormat.backgroundColor` |
| Conditional formatting | **FORBIDDEN**; post-write rule count must be 0 |
| Banding, auto-resize, merged cells in the data area | none |
| RGB tolerance on read-back | one code (Google quantizes `0.4196` → `0.41568628`); never widened |

Conditional formatting is banned on evidence, not preference: Google returned HTTP 400 and then 500
for conditional-format payloads on this workbook class. Direct format is the only supported path.

Palette (`Yvien Hotlink Website/app-demo/styles/tokens.css:10-56`, role map in the voice pack §7):
sheet `#fffcf7` · header background `#f6f4df` · header foreground `#95131f` · border `#e7d6b4` ·
text `#1a1410` · soft text `#4a4a4a` · ACTION_REQUIRED `#f7e8c2` · blocker `#c70002` ·
verified `#2f5d50`. Flat only.

### Write mechanics

`valueInputOption = RAW`. A cell whose text begins with `+`, `=`, `-`, or `@` is rewritten as text so
Sheets cannot read it as a formula. Values come from the `values` matrix in `report-plan.json`
verbatim; the executor does not reformat, re-sort, re-wrap, or "improve" a cell.

`content_hash` per tab is SHA-256 over the canonical `values` (JSON, `ensure_ascii=False`,
`separators=(",",":")`); `workbook_content_hash` is SHA-256 over the ordered list of tab hashes. Two
consecutive builds from unchanged sources must produce identical hashes — a build that does not is
rejected before any network call.

### Required dataset fields

Minimum semantic content per dataset. The dataset names are the `TL_` machine keys; §3 maps each to
its `YV_` tab, and `docs/system/yvien-sheet-human-layer-spec.md` SPEC-A gives the exact visible column
order and Vietnamese header for each tab.

| Dataset | Minimum additional fields |
|---|---|
| TL_REPORT | report section, synthesis, source record IDs, status, blocker IDs |
| TL_OWNER_ACTIONS | priority, category, requested decision/input, deadline gate, blocked effect, live source reference, decision status, approver role/date/value, notes |
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

1. **Claude Code** writes wording and derived rows into the canonical markdown, runs the deterministic
   generator into `staging/yv-humanize/report-plan.json`, and records the trace. It does not read the
   SA key, call the Google API, or write a Sheet. Its runs are `external_writes = 0`.
2. **Codex CLI** validates the artifact digest, source/profile gate, registry mapping, schema, and
   stable row key, then rebuilds the plan itself and compares `workbook_content_hash` plus every tab
   `content_hash` against Claude's file and the committed fixtures. Any drift stops the lane before
   the network.
3. After explicit SheetTargetApproval, Codex performs the smallest allowed `CREATE_TAB` or bounded
   upsert, snapshotting the `before` state of each range first, then exact read-back of **value and
   format**: values, IDs, row/column count, required fields, Vietnamese Unicode, `frozenRowCount`,
   `basicFilter`, `wrapStrategy`, `verticalAlignment`, `columnWidth`, `hiddenByUser` on `_key`/`_audit`,
   the `backgroundColor` of exactly the declared yellow cells (right count, right coordinates), a
   conditional-format rule count of 0, and the survival of `Trang tính1`.
4. Codex records the read-back in the paired manifest and `03_OUTPUT_INDEX`, and appends a revision
   row to `04_DECISIONS`. Acknowledgment without read-back is VERIFY_FAILED. A mismatch writes the
   `before` snapshot back, marks VERIFY_FAILED, preserves the evidence, and forbids a broad retry.

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
| Read-back format differs (freeze, filter, wrap, alignment, width, `hiddenByUser`) | VERIFY_FAILED | restore the `before` snapshot for that range; no broad retry |
| Yellow-cell count or coordinates differ from `expected_yellow_count` | VERIFY_FAILED | restore `before`; do not repaint by hand |
| Any conditional-format rule present after the write | VERIFY_FAILED | restore `before`; the mechanism itself is wrong, not the colour |
| Two builds of `report-plan.json` disagree | BLOCKED_SCHEMA | repair the generator; never write a non-reproducible plan |
| `Trang tính1` renamed, written, or missing | VERIFY_FAILED | restore; it is a preserved object |
| A tab title carries a `_v2` suffix | BLOCKED_SCHEMA | stop before write; a revision changes rows, not titles |

## 6. Good, base, and bad cases

- **Good:** The user signs the `UPSERT` approval bound to the plan digest. Codex rebuilds
  `report-plan.json`, matches `workbook_content_hash`, snapshots each range, writes the declared
  `values` only, applies direct format, and reads back value and format — including the 27 yellow
  cells at their declared coordinates and zero conditional-format rules.
- **Base:** The plan and fixtures are ready but no approval is signed. State is
  `LOCAL_VERIFIED · SYNC_PENDING_APPROVAL`; `external_writes = 0`; no mutation occurs.
- **Bad:** An agent copies a tab, formula, baseline, or output from the Thảo Tây workbook, guesses a
  target/range, creates a `_v2` tab, paints a yellow cell by hand, reaches for conditional formatting
  after a colour mismatch, or calls a connector without a read-back. Stop and record the applicable
  error status.

## 7. Tests and audit evidence

Before any external write, the operator must prove:

1. every requested tab_key is in the 21-tab `YV_` registry of §3 and all artifact/dataset mappings
   resolve through `03_OUTPUT_INDEX` without orphan records;
2. artifact and DMP trace digests match the handoff/manifest, and an independent rebuild of
   `report-plan.json` reproduces `workbook_content_hash` exactly;
3. no target/ID/tab/row comes from Thảo Tây scope;
4. exact approval fields and lease are current, and the approval being consumed carries
   `write_executed: false`;
5. pre-write target/range/schema/validation read is captured, including a `before` snapshot per
   range and confirmation that `Trang tính1` exists and no `_v2` tab does; and
6. post-write read-back verifies stable IDs, row/column count, required fields, Vietnamese Unicode,
   **and the full format contract of §4** — freeze, filter, wrap, alignment, width, `hiddenByUser` on
   `_key`/`_audit`, the exact yellow-cell set, and zero conditional-format rules.

Local test suite: `python -B -m unittest discover -s .trellis/scripts/tests -p "test_yv_*.py"`
(21 checks over the human layer — fixtures, determinism, no-escalate, banned-word lint, claim
resolution, yellow contract, hidden columns, Unicode, secret scan). The unfiltered `discover` command
also loads `test_toplink_sheet_sync.py`, the superseded `TL_*` suite, which fails closed on source
digest drift until Codex completes the P2.1 refactor.

git diff --check, link validation, JSON-template parsing, and a contract-reference search are
required for changes to this contract or its scaffolds.

## 8. Wrong vs correct

**Wrong:** “DMP created a local file, therefore create a similar tab in the previous brand’s
workbook.”

**Correct:** “DMP created a traced Toplink artifact; Codex maps its Toplink stable ID to a registered
`YV_` tab only after the user approves a new Toplink workbook, exact range/schema/action/limits, and
Codex can read the result back.”

**Wrong:** “The read-back matched every cell, so the delivery passed.”

**Correct:** “The read-back matched every cell and every format property in §4, including the yellow
set and a conditional-format rule count of 0. A value-only match is `TECHNICAL_READBACK_PASS` — the
0.2.0 delivery already proved that is not the same as a workbook a human can use.”
