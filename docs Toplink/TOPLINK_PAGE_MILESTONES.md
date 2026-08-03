# Toplink Facebook Page — Milestones

## 1. Document control

| Trường | Giá trị |
|---|---|
| Document ID | `TL-MS-001` |
| Plan owner | `TOPLINK_PAGE_MASTER_PLAN.md` |
| Version | `0.1.3` |
| Ngày | 2026-07-29 |
| Sửa đổi | 2026-08-03 — reconcile TL-M0/Run 1 evidence and blocker statuses; no milestone advancement |
| Trạng thái | `RUN1 · LOCAL_VERIFIED · PHASE_B_RECONCILED · TL-M5_PENDING · NOT_COMPLETE` |
| DMP | Digital Marketing Pro `3.15.1` — real invocation bắt buộc |
| Sheet | `TARGET_AND_SA_READY · SHEET_TARGET_APPROVAL_PENDING · NO_WRITE` |

File này là execution contract duy nhất của Toplink Page brand-track. Root `task.md` vẫn là live
checklist/lease ledger; root `STATE.md` là sprint summary. Không tạo plan/todo/milestone cạnh tranh.

## 2. Global execution contract

### 2.1. Read order

```text
AGENTS.md
→ STATE.md
→ RULES.md
→ task.md
→ GOVERNANCE.md §1 + §3
→ TOPLINK_PAGE_MASTER_PLAN.md
→ milestone đang active trong file này
→ exact source/evidence refs của milestone
```

### 2.2. DMP is the blocking core

Mọi milestone sinh deliverable phải có `REAL_DMP_INVOCATION`. Review thủ công hoặc
`SKILL_CONTRACT_REVIEW` không thay thế:

```text
trace_id
timestamp
DMP_version
active_brand_readback = toplink-y-vien
skill
exact_input_paths
input_digest
output_path
output_digest
status
skipped_dimensions
```

- `NO_TRACE = NOT_DONE`.
- DMP không chạy được → `BLOCKED_DMP_RUNTIME`.
- Active brand/version/profile/digest mismatch → không generate.
- DMP output chỉ là staging; cần Agency/compliance/human gate tương ứng.
- Không tạo thêm slug cho cùng entity; dùng `toplink-y-vien`.

### 2.3. Status state machine

```text
PLANNED
→ DMP_GENERATED
→ AGENCY_REVIEWED
→ LOCAL_VERIFIED
→ SYNC_PENDING_TARGET
→ SYNC_READY_APPROVAL
→ SYNC_WRITTEN_UNVERIFIED
→ SYNC_READBACK_PASS
→ COMPLETE
```

`LOCAL_VERIFIED` không đồng nghĩa `APPROVED`, published hoặc operationally complete.
Milestone cần Sheet chỉ `COMPLETE` sau exact-range read-back. Target chưa có thì dừng ở
`SYNC_PENDING_TARGET`.

### 2.4. Common Done gates

Mỗi milestone PASS khi:

- exact DMP trace tồn tại và output digest khớp;
- Agency review đúng routing, tối đa 3 reviewer/workstream;
- evidence/status/allowed-use rõ, không fact hoặc claim tự sinh;
- health/legal/privacy item giữ human gate;
- stable ID unique, reference integrity PASS;
- local schema/Unicode/secret/PII/diff checks PASS;
- Sheet target/range được duyệt, bounded upsert + exact read-back PASS khi required;
- checkpoint ghi vào root `task.md` và lease đã release.

### 2.5. Stop conditions

- Canonical/entity/digest conflict.
- DMP version/profile/active brand không khớp.
- Thiếu evidence bắt buộc hoặc human authority.
- Cùng bounded step fail hai lần.
- External target/action khác approval.
- Sheet write không read-back được.
- Agent tự nâng `APPROVED`.
- Có competing writer/lease.

### 2.6. Stable identity namespace

| Artifact | Pattern |
|---|---|
| Source/evidence | `TL-EV-{NNN}` |
| Gap/gate | `TL-GAP-{NNN}` |
| Audience | `TL-AUD-{NNN}` |
| Positioning/narrative | `TL-STR-{NNN}` |
| Pillar | `TL-PIL-{NNN}` |
| Campaign/KPI | `TL-CAM-{NNN}`, `TL-KPI-{NNN}` |
| Content | `TL-CONTENT-D{01..28}-{A\|B\|C}` |
| Claim | `TL-CLAIM-{NNN}` |
| Approval | `TL-APPROVAL-{CONTENT_ID}-{REVISION}` |
| Output index | `TL-OUT-{MILESTONE}-{NNN}` |

ID immutable; wording/revision không đổi identity.

## 3. DMP và reviewer routing theo milestone

| Milestone | DMP real invocation bắt buộc | Reviewer |
|---|---|---|
| `TL-M0` | `doctor`, `status`, `output-folder`/readiness path | PR/ops review khi cần |
| `TL-M1` | `import-guidelines`, `brand-setup` | PR Manager |
| `TL-M2` | `brand-setup`, `switch-brand`, `import-guidelines`, `status` | PR Manager |
| `TL-M3` | `audience-intelligence`, `campaign-plan`, `social-strategy`, `content-engine` | Social Strategist → Growth Hacker; Content Creator/PR theo artifact |
| `TL-M4` | `campaign-plan`, `social-strategy`, `content-engine` | Social Strategist → Growth Hacker; PR khi sensitive |
| `TL-M5` | `content-calendar`, `content-engine`, `video-script`, `check` | Content Creator → PR; Short-Video Coach → TikTok Strategist |
| `TL-M6` | `resume`, `status`, `check` + generator skill khi repair | Growth Hacker + content/PR theo item |
| `TL-M7` | `campaign-plan`, `status` | Growth Hacker → PR |
| `TL-M8` | `campaign-plan`, `resume`, `status`, `check` | Growth Hacker → PR |
| `TL-M9` | `status`, `output-folder`, `integrations` | PR Manager + operator |

Command-only/skill availability phải được xác minh ở runtime. Không ghi `REAL_INVOKE` khi chỉ đọc
contract hoặc chạy mock.

## 4. Top-level dependency graph

```text
TL-M0 scope/readiness
  → TOPLINK_RUN1_BUILD
       TL-M1 evidence/entity/compliance
       → TL-M2 DMP profile/digests
       → TL-M3 audience/positioning/Page/pillars
       → TL-M4 campaign/KPI
       → TL-M5 production/approval
       → Claude handoff/release
       → Codex reconciliation/Run 1 manifest
  → TOPLINK_RUN2_FRESH_AUDIT_FINALIZE
       fresh Claude audit/DMP check/Agency review
       → handoff/release
       → fresh Codex blind audit/repair/promotion
       → Sheet sync/read-back
       → paired manifests PASS
  → TL-M6 30-day pilot
  → TL-M7 three-month roadmap
  → TL-M8 gated scale
  → TL-M9 handoff
```

`TL-M1`–`TL-M5` là một package chạy đúng hai macro-run. Không promote sớm từng milestone, không
Run 3. Mỗi milestone có local checkpoint nhưng chỉ `COMPLETE` sau Run 2 + Sheet read-back.

# PHẦN A — Foundation

## TL-M0 — Scope, canonical delegation và DMP readiness

### Goal

Khóa brand-track, canonical owner, write-role exception, read order, DMP availability và target
gate trước khi tạo bất kỳ strategy/content deliverable.

### Inputs

- User decisions `TL-D01`–`TL-D10`.
- Root governance/rules/agents.
- Hai planning docs Toplink.
- DMP health check hiện có.

### Work

1. Verify canonical paths, no competing plan/milestones.
2. Verify root `GOVERNANCE §1`, `RULES §0/§2`, `AGENTS` Toplink exception.
3. Chạy DMP readiness path thật: version/capabilities/status/output-folder.
4. Ghi rõ active brand hiện tại; không switch ngầm.
5. Khóa logical Sheet architecture theo `docs/system/toplink-google-sheets-operational-contract.md`;
   giữ `BLOCKED_TARGET_INPUT` và không tạo target/tab.
6. Khóa future directory tree, không tạo toàn bộ trước hạn.

### Deliverables

- `TOPLINK_PAGE_MASTER_PLAN.md`.
- `TOPLINK_PAGE_MILESTONES.md`.
- DMP readiness trace.
- `TL-OUT-TL-M0-001` logical output-index record.

### VERIFY

- Hai file tồn tại, basename không collision root.
- Scope/canonical/exception được root files ủy quyền.
- DMP readiness là `REAL_INVOKE`; nếu chưa có, status = `PLANNED` hoặc `BLOCKED_DMP_RUNTIME`.
- External writes = 0.
- Khi Sheet target có: output-index upsert + read-back.

### Current status

`READINESS_EVIDENCE_PASS · VERIFIED_REAL_INVOKE · PROFILE_DRIFT_REPAIRED · NOT_MILESTONE_COMPLETE`.

Evidence: `staging/toplink-reconciled/TL-M0-readiness/dmp-readiness-trace.md`,
`staging/toplink-reconciled/TL-M0-readiness/codex-tl-m0-verification.md`, and
`staging/toplink-reconciled/TL-M2-profile/tl-m2-profile-repair-trace.md`. The original TL-M0
control-plane finding is retained as historical evidence; the later signed repair/read-back closes
that readiness blocker without promoting TL-M0 or any package milestone.

## TL-M1 — Evidence, entity/franchise, Page identity và compliance

### Goal

Tạo frozen evidence foundation đủ để downstream không đọc lại toàn corpus và không biến
competitor/franchisor, tick xanh hoặc product wording thành fact sai.

### Inputs

- Evidence corpus hiện hữu: `docs Toplink/00_INDEX.md`, `01`–`10` và
  `Ho-so-thuong-hieu-Y-Vien-Toplink-Cai-tien-2026.md`.
- Standalone-repository migration provenance:
  `docs/reports/migration-report.md` và
  `docs/reports/toplink-source-manifest.sha256`.
- TL-M0 runtime/profile metadata read-back:
  `staging/toplink-reconciled/TL-M0-readiness/dmp-readiness-trace.md` và
  `staging/toplink-reconciled/TL-M0-readiness/raw/02-status.json`.
  Metadata này chỉ chứng minh trạng thái/drift hiện tại; không phải nguồn brand fact.
- User decisions trong canonical master plan.
- Official Page URL/Page ID/snapshot khi user cung cấp.
- Franchise/legal documents khi user cung cấp.
- Pre-migration/root source inventory, profile artifact và decision/change history hiện không có
  trong standalone repo; giữ fail-closed theo `TL-GAP-012`–`TL-GAP-014`. Không được thay chúng
  bằng brand dossier, governance file, memory suy diễn hoặc artifact Thảo Tây.

### DMP

`import-guidelines` + `brand-setup` ở evidence/profile mode, có trace thật.

### Work

0. Resolve mọi prerequisite thành một exact repository path hoặc một `TL-GAP-*` stable ID.
   Không để prerequisite dạng tên mô tả tự do, không map artifact thiếu sang một file có vai trò
   khác và không dựng lại lịch sử rồi trình bày như lịch sử gốc.
1. Tạo source manifest: relative path, UTF-8 policy, SHA-256, exclusions.
2. Tách entity `Nhất Liệu Y Viện`, franchise relationship, source artifact/domain và allowed-use.
3. Reconcile classification cũ; không xóa provenance.
4. Tách status:
   `USER_CONFIRMED_INTERNAL` · `PUBLIC_BRAND_RELATIONSHIP_PENDING_DOCUMENT` ·
   `LEGAL_SCOPE_PENDING`.
5. Khóa Page stable identity, platform-signal meaning và baseline timestamp.
6. Lập product/service claim registry, safe public naming, forbidden catalogue, disclaimer.
7. Lập privacy/consent/qualification/outcome proof taxonomy.
8. Ghi input-gap register.

### Deliverables

Future paths:

```text
docs Toplink/research/source-inventory.md
docs Toplink/research/input-gap-register.md
docs Toplink/research/entity-franchise-allowed-use-map.md
docs Toplink/system/health-compliance.md
```

Logical Sheet datasets:
`TL_SOURCE_INVENTORY`, `TL_INPUT_GAPS`, `TL_DECISIONS`.

### VERIFY

- Mọi material fact có exact source + status + allowed-use.
- Competitor/franchisor records không collision hoặc silent overwrite.
- Tick xanh chỉ `PLATFORM_IDENTITY_SIGNAL`.
- Follower count có Page identity + timestamp; awareness = `NO_MEASUREMENT`.
- Product benefit chưa đủ dossier giữ `UNVERIFIED`.
- DMP trace + PR verdict PASS/NEEDS gate.
- Sheet stable IDs + exact read-back PASS khi target có.
- Mọi input được resolve thành exact path hoặc gap ID; không còn prerequisite không ràng buộc.
- Migration provenance, current runtime metadata và historical evidence được phân biệt rõ.
- Reconstructed current-repo inventory không được gọi là root/pre-migration inventory.
- Thiếu legacy profile/history không được lấp bằng suy diễn hoặc dữ liệu Thảo Tây.
- Các claim về historical equivalence, full reconciliation hoặc exact before/after state vẫn
  bị chặn khi `TL-GAP-012`–`TL-GAP-014` chưa được giải.

## TL-M2 — DMP profile và brand architecture

### Goal

Cập nhật đúng một DMP brand entity `toplink-y-vien`, đặt Facebook Page là primary channel của
Toplink track, khóa profile/source digests và guidelines trước generation.

### Dependencies

`TL-M1` local evidence PASS. Runtime/profile mutation cần đúng approval tier.

### DMP

`brand-setup` → `import-guidelines` → `switch-brand toplink-y-vien` → `status/read-back`.

### Work

1. Map field vào DMP core/profile/guideline/staging-only.
2. Không tạo slug `toplink-page`.
3. Cập nhật competitor/franchisor relation sau `TL-M1` evidence decision.
4. Page primary channel; Website/Zalo/phone/Maps giữ `PENDING_INPUT` nếu chưa verify.
5. Map restrictions/disclaimer và founder allowed-use.
6. Tạo `profile_digest` + `source_digest`; read-back active brand/version.

### Deliverables

```text
docs Toplink/brand/dmp-profile.md
docs Toplink/system/runtime-compatibility.md
docs Toplink/staging/run1/00-input-lock.json
```

Logical Sheet dataset: `TL_BRAND_PROFILE`.

### VERIFY

- Một slug duy nhất; active read-back = `toplink-y-vien`.
- Không secret/path/private analytics.
- Mọi unsupported field không bị ép vào runtime.
- Digests deterministic và được khóa cho hai run.
- Runtime/Sheet exact read-back PASS khi mutation được duyệt.

# PHẦN B — Strategy và production package

## TL-M3 — Audience, positioning, Facebook Page strategy và pillar decision

### Goal

Hội tụ từ hypotheses sang launch strategy có thể kiểm thử, không giả audience insight.

### DMP

`audience-intelligence` → `campaign-plan` → `social-strategy` + `content-engine`.

### Work

1. Đánh giá `TL-A01`–`TL-A04`; giữ/sửa/loại có rationale.
2. Tạo positioning/narrative hypothesis với proof boundary.
3. Tách Hà Nội service/conversion và national awareness.
4. Khóa corporate voice/founder allowed-use.
5. Hội tụ 3–5 pillar, tổng 100%; mỗi pillar có evidence/job/format/funnel/risk/rationale.
6. Facebook Page = primary; Reels support; Thảo Tây cross-post có item gate.

### Deliverables

```text
docs Toplink/research/audience-hypotheses.md
docs Toplink/brand/positioning.md
docs Toplink/brand/narrative.md
docs Toplink/brand/content-pillars.md
docs Toplink/brand/facebook-page-strategy.md
```

Logical Sheet dataset: `TL_AUDIENCE_POSITIONING`, `TL_PAGE_STRATEGY`.

### VERIFY

- Không audience fact thiếu source.
- 3–5 pillar, total 100%.
- Founder-led planning guardrail được item hóa.
- Không national service inference.
- Agency verdict theo artifact; human gate giữ nguyên.

## TL-M4 — Trust-led 30-day campaign và greenfield KPI

### Goal

Thiết kế campaign Tuần 1–4 tương đối, đo learning signal trước sales pressure.

### DMP

`campaign-plan` + `social-strategy` + `content-engine`.

### Work

1. W1 identity/limits; W2 health-sensitive education; W3 operational proof.
2. W4 conditional: `EVIDENCE-CLEARED SOLUTION` hoặc `SAFE FALLBACK`.
3. Không bind ngày trước `TOPLINK_CONTENT_START_DATE`.
4. CTA mặc định non-commercial; commercial CTA chỉ sau offer gate.
5. KPI dictionary: definition/formula/source/owner/cadence/minimum sample.
6. Counts = 0 khi measured; rates/history = `N/A`; cấm `% from zero`.
7. Experiment một biến/lần; Continue/Repair/Stop.

### Deliverables

```text
docs Toplink/brand/campaign-architecture.md
docs Toplink/brand/kpi-experiment-plan.md
```

Logical Sheet dataset: `TL_CAMPAIGN_KPI`.

### VERIFY

- Bốn tuần truy về pillar/audience job.
- W2 claim/professional gate item-level.
- W3 chỉ operational proof hoặc proof có hồ sơ/consent.
- W4 fallback đầy đủ, không bypass bằng lịch/disclaimer.
- KPI không overclaim trust/awareness.

## TL-M5 — Content, Reels, production, approval và measurement

### Goal

Biến strategy thành production system khả thi và fail-closed trước publish.

### Dependencies

- Production capacity, asset rights và reviewer route được user chốt.
- Public-ready offer/CTA chỉ khi corresponding gate PASS.

### DMP

`content-calendar` + `content-engine` + `video-script` + `check`.

### Work

1. Relative 28-day calendar, mỗi ngày A/B/C option; không bind ngày.
2. Asset/batch plan theo capacity thật.
3. Reels brief Facebook-first; TikTok mechanics review only.
4. Production brief: hook, shot, on-screen text, caption, CTA, claim IDs, source.
5. Approval ledger theo content hash/revision; material edit reset approval.
6. Accessibility: subtitle, safe zone, disclaimer đủ thời gian đọc.
7. Không before/after, medicalized fear visual hoặc generalized testimonial.

### Deliverables

```text
docs Toplink/content/month-calendar.md
docs Toplink/content/asset-and-batch-plan.md
docs Toplink/content/reels-briefs.md
docs Toplink/content/production-briefs.md
docs Toplink/content/workflow-approval-measurement.md
```

Logical Sheet datasets:
`TL_CONTENT_CALENDAR`, `TL_REELS_PRODUCTION`, `TL_WORKFLOW_APPROVAL`.

### VERIFY

- 28-day relative identities complete, reference integrity PASS.
- Capacity/reviewer/asset/claim fields không null giả.
- DMP `check` thật; skipped dimension ghi đúng.
- Health/legal/privacy state giữ nguyên trong Sheet schema.
- Không item nào tự `APPROVED` hoặc publish.

# PHẦN C — Two-run control

## TOPLINK_RUN1_BUILD — Claude DMP build → Codex reconciliation

### Entry

- `TL-M0` readiness PASS.
- Exact lease, no competing writer.
- `TL-M1` source set frozen.
- DMP `3.15.1`, active brand/profile gate.
- Sheet target có thể chưa có; Run 1 luôn local-only.

### Phase A — Claude 20–25%

1. Nhận lease chỉ cho input lock, `claude/` raw outputs và handoff.
2. Chạy DMP real invocation cho `TL-M1`–`TL-M5` theo dependency.
3. Ghi invocation trace với exact inputs/outputs/digests.
4. Coordinate Agency review theo workstream.
5. Ghi handoff marker:

```text
CLAUDE_TOPLINK_RUN1_PHASE_A_COMPLETE
profile_digest
source_digest
DMP_version
active_brand
generated_outputs
reviewers
check_results
external_writes=0
next_actor=Codex
```

6. Dừng ghi, checkpoint, release lease.

### Phase B — Codex 75–80%

1. Verify handoff/digests trước khi lấy lease.
2. Evidence/status/privacy/allowed-use reconciliation.
3. Stable identity + delta ledger:
   `KEEP | REVALIDATE | OPTIMIZE | REGENERATE | REJECT_DMP`.
4. Evidence-grounded cross-workstream repair theo ngoại lệ; không thêm fact/claim.
5. Schema/compliance/manifest QA.
6. Tạo `run1-manifest.json`; `external_writes=0`.
7. Release lease và STOP. Không gọi là Run 2.

### Required staging

```text
docs Toplink/staging/run1/
├── 00-input-lock.json
├── claude/
├── handoff-claude-to-codex.md
├── 10-evidence-profile-map.md
├── 20-runtime-compatibility.md
├── 30-delta-ledger.json
├── 40-workstream-reconciliation.md
├── 50-pillar-decision.md
├── 60-agency-review-register.md
├── 70-run1-checks.md
└── run1-manifest.json
```

### Run 1 PASS

- Real DMP traces đủ `TL-M1`–`TL-M5`.
- Mọi delta có stable ID/disposition.
- No canonical/runtime/Sheet/Page mutation.
- Human gates giữ nguyên.
- Manifest schema PASS.

## TOPLINK_RUN2_FRESH_AUDIT_FINALIZE — Fresh Claude → fresh Codex

### Entry

- Session/context fresh theo attestation.
- Chỉ đọc canonical contract, input lock, Run 1 manifest metadata và artifact contract trước blind pass.
- Digests/version/active brand match; mismatch = `FAIL_BACK_TO_RUN1`.
- Run 1 PASS; no competing writer.

### Phase A — fresh Claude

1. Blind audit evidence/voice/entity.
2. Blind audit audience/positioning/pillar.
3. Blind audit KPI/production/compliance.
4. Sau khi persist blind findings mới đọc Run 1 reasoning.
5. Chạy DMP `check` thật trên health-sensitive artifacts.
6. Fresh Agency review.
7. Ghi handoff envelope + findings; external writes = 0.
8. Dừng ghi và release lease.

### Phase B — fresh Codex

1. Independent blind audit trước khi đọc Claude findings.
2. Persist audit; sau đó merge Claude/Codex issue ledger.
3. Repair evidence-grounded; regenerate chỉ qua traced DMP invocation khi required.
4. Validate human/legal/privacy gate integrity.
5. Promote local canonical candidates in place, không `_v2`.
6. Chuẩn bị Sheet mapping theo `docs/system/toplink-google-sheets-operational-contract.md` và target
   user duyệt.
7. Exact approval → bounded upsert → exact-range read-back.
8. Paired-manifest validation, checkpoint, release lease.

### Run 2 Sheet gate

Nếu target chưa được cấp:

```text
local_status = LOCAL_VERIFIED
sheet_status = SYNC_PENDING_TARGET
final_status = NOT_COMPLETE
```

Không tái dùng workbook Thảo Tây hoặc tự tạo target. Khi target được cấp, approval phải nêu
agent · spreadsheet/tab/range · input · action · limits · expiry.
Registry tab, schema, mapping, validation error states, và bằng chứng read-back phải theo
`docs/system/toplink-google-sheets-operational-contract.md`.

### Paired manifest contract

```text
run_id
profile_digest
source_digest
DMP_version
active_brand
workstreams
dmp_traces
generated_outputs
reviewers
check_results
delta_ledger
human_gates
sheet_plan
readback
blockers
final_status
```

Hai manifest cùng digest/version/brand và cùng PASS; không Run 3.

# PHẦN D — Operation và growth

## TL-M6 — Controlled 30-day Page pilot

### Entry gate

- Paired manifests PASS + Sheet `SYNC_READBACK_PASS`.
- Official Page identity/access snapshot.
- `TOPLINK_CONTENT_START_DATE`.
- Weekly production capacity.
- Offer/CTA status rõ; non-commercial fallback tồn tại.
- Item-level publish approvals.
- Response/measurement owner.

### DMP

`resume` + `status` + `check`; generator skill được gọi lại khi repair có trace.

### Work

- Bind D1–D28 vào ngày thật.
- Publish chỉ item approved; Page mutation cần action approval.
- Daily/weekly measurement có source/time window.
- Continue/Repair/Stop review; không đổi nhiều biến một lúc.
- Sync observations/decisions/approval revisions và exact read-back.

### VERIFY

- Không skipped day bị backfill bằng content chưa duyệt.
- Mọi metric có source; no `% from zero`.
- Health/legal/privacy incidents được fail-closed.
- Pilot retrospective truy về stable IDs.

## TL-M7 — Evidence-led three-month roadmap

### Goal

Dùng pilot evidence để giữ/sửa/loại pillar, cadence, format, CTA và founder mix.

### DMP

`campaign-plan` + `status`.

### Deliverables

- Roadmap 3 tháng.
- Growth/experiment loop.
- Capacity plan.
- Decision ledger với pilot evidence.

### VERIFY

- Không quyết định nào chỉ dựa vào benchmark hoặc model confidence.
- Paid ads/kênh mới chưa tự mở.
- Sheet upsert/read-back PASS.

## TL-M8 — Gated national/ecosystem scale

### Goal

Mở rộng organic awareness và operational system sau signal/capacity; không tự đồng nghĩa national
service availability.

### DMP

`campaign-plan` + `resume` + `status` + `check`.

### Gate riêng

- Paid media: ngân sách + scope + measurement approval.
- New channel: pilot evidence + owner/capacity.
- National conversion/product sales: coverage/logistics/price/warranty/compliance.
- New location/chain/ecosystem: legal/operational evidence.

### VERIFY

- Geo/entity/channel boundary giữ nguyên.
- Mọi scale decision truy về M6/M7 evidence.
- Sheet stable identities/revisions/read-back PASS.

## TL-M9 — Operational handoff

### Goal

Người vận hành mới có thể chạy một bounded cycle mà không dựa vào conversation history.

### DMP

`status` + `output-folder` + `integrations`.

### Deliverables

- SOP/RACI.
- DMP invocation/handoff guide.
- Claim/approval/incident protocol.
- Sheet mapping, backup/recovery và exact read-back checklist.
- Page publishing checklist.
- Dry-run package.

### VERIFY

- Operator mới chạy dry-run local + Sheet read-back trên exact approved range.
- Không cần secret trong repo/docs.
- Human approvals và external mutation boundaries rõ.
- All leases released; unresolved gates được handoff.

## 5. Current blocker register

| ID | Blocker | Chặn |
|---|---|---|
| `TL-GAP-001` | `RESOLVED_BY_USER`: Page ID `61591880797654`; baseline = task start, follower 0; awareness vẫn `NO_MEASUREMENT` | Dated image snapshot remains optional evidence; no measured-awareness claim |
| `TL-GAP-002` | Franchise public/legal evidence chưa có | Public identity/franchise content |
| `TL-GAP-003` | `RESOLVED_INTERNAL_CLASSIFICATION`: profile/entity map reconciled; public relationship wording vẫn gated bởi `TL-GAP-002`/`009` | Public narrative until legal gates pass |
| `TL-GAP-004` | Product/service dossiers còn thiếu | Product/service claim và W4 solution |
| `TL-GAP-005` | Offer/booking/contact/privacy/SLA chưa verify | Commercial CTA |
| `TL-GAP-006` | Production capacity/start date chưa chốt | TL-M5/TL-M6 |
| `TL-GAP-007` | `REVIEWER_DESIGNATED_USER_ATTESTED`; formal credential missing and item-level approval mandatory | Health-sensitive publish |
| `TL-GAP-008` | `TARGET_AND_SA_READY · SHEET_TARGET_APPROVAL_PENDING`; target/Editor/API/key wiring readiness is not write approval | Mọi operational completion |
| `TL-GAP-009` | Legal name / giấy phép / phạm vi hoạt động chưa có verified document in hand | Any public legal/scope claim |
| `TL-GAP-010` | `11_Product_Yvien.md` now exists as an unverified source candidate; provenance, certifications, inspection and claim dossiers have not passed | Full product-source provenance and every product/service claim |
| `TL-GAP-011` | `RESOLVED 2026-07-30`: signed bounded profile repair + G1–G7 read-back; digest locked | — |
| `TL-GAP-012` | `PROVENANCE_LOCATED_LIMITED · FAIL_CLOSED`: bounded origin inventory digest exists; full historical equivalence remains unverified | Claim that current inventory equals the full historical source set |
| `TL-GAP-013` | `PROVENANCE_LOCATED_LIMITED · FAIL_CLOSED`: origin profile pointer + pre-repair backup digest exist | Any broader legacy-field provenance or comparison beyond the bounded evidence |
| `TL-GAP-014` | `PROVENANCE_LOCATED_LIMITED · FAIL_CLOSED`: origin decision-file pointers are digest-recorded | Claim that full legacy decision/reconciliation history is complete |

`TL-GAP-012`–`TL-GAP-014` remain fail-closed. `PROVENANCE_LOCATED_LIMITED` records only the bounded
pointer/digest evidence in `root-provenance-map.md`; it does not resolve the missing authority or
permit historical-equivalence/full-reconciliation claims.

**Evidence reconciliation 2026-08-03; no milestone advancement:** TL-M0 real readiness trace,
TL-M2 signed profile repair/read-back, TL-M1 DMP trace, TL-M2–TL-M4 Phase A/Phase B and final QA are
locally verified. Run 1 still cannot PASS because TL-M5 is absent. Human health/legal/franchise/
public-positioning gates, `SheetTargetApproval`/read-back and Run 2 remain open; `external_writes=0`.

## 6. Next safe action

1. Human owner resolves `TL-GAP-006` (content start date + real weekly production capacity) and
   supplies the asset-rights/availability boundary required by TL-M5; designated health reviewers
   remain item-level gates, not blanket approval.
2. MCBAu finishes or explicitly hands off/excludes the non-overlapping P1
   `.trellis/tasks/00-bootstrap-guidelines` worktree changes.
3. Claude may then acquire an exact TL-M5 Run 1 Phase A lease and write only the five canonical
   TL-M5 deliverables plus its bounded trace/review/marker/handoff scope.
4. Codex reconciles TL-M5 into the existing Run 1 manifest. Do not close Run 1, start Run 2, write
   Sheet/Page state, publish, or mark any milestone `COMPLETE`/`APPROVED` in this step.
