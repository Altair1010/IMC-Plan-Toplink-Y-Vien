# Toplink Facebook Page — Product Master Plan

## 1. Document control

| Trường | Giá trị |
|---|---|
| Document ID | `TL-PMP-001` |
| Brand track | Toplink Facebook Page |
| Version | `0.1.1` |
| Ngày khóa plan | 2026-07-29 |
| Sửa đổi | 2026-07-30 — thêm `TL-D12`–`TL-D15` (Page ID, health reviewer, Sheet target, SA Toplink mới); no milestone advancement |
| Trạng thái | `PLAN_LOCKED · EXECUTION_NOT_STARTED` |
| Canonical scope | Chiến lược, kiến trúc và quyết định riêng của Toplink Page |
| Execution owner | `TOPLINK_PAGE_MILESTONES.md` |
| DMP | Digital Marketing Pro `3.15.1` — core bắt buộc |
| DMP real invocation của plan này | `0` — chỉ có `SKILL_CONTRACT_REVIEW` |
| Google Sheets | Target verified; V2 consumed; 24-dataset correction `BOUNDED_APPROVAL_PENDING` |
| External writes | `0` |

Tài liệu này là brand-track được ủy quyền bởi `GOVERNANCE.md §1`, subordinate với
`docs/product-master-plan.md`, `RULES.md` và các canonical root. Nó không thay thế chiến lược
thương hiệu cá nhân Thảo Tây và không tự mở M6 của Thảo Tây.

## 2. Canonical ownership và precedence

| Câu hỏi | Owner |
|---|---|
| Scope, hard stop, cross-brand policy | Root `RULES.md`, `GOVERNANCE.md`, `AGENTS.md` |
| Chiến lược/kiến trúc/quyết định Toplink Page | File này |
| Trình tự, deliverable, Done gate `TL-M0`–`TL-M9` | `TOPLINK_PAGE_MILESTONES.md` |
| Live checklist, lease, checkpoint | Root `task.md` |
| Sprint summary/blocker | Root `STATE.md` |
| Brand/product evidence | `00_INDEX.md`, `01`–`10`, hồ sơ thương hiệu và evidence map được tạo ở `TL-M1` |
| DMP output | Staging có trace; không tự trở thành canonical |
| Operational destination | Google Sheets target do user duyệt, sau exact read-back; shape/mapping tại `docs/system/toplink-google-sheets-operational-contract.md` |

Các file nguồn hiện hữu trong `docs Toplink/` là evidence input, không phải decision owner. Không
di chuyển, đổi tên hoặc xóa chúng vì còn tham chiếu provenance/hydration. Khi owner mâu thuẫn,
dừng phần mutation bị ảnh hưởng và sửa đúng owner; không giải bằng cách chọn file thuận tiện hơn.

## 3. User-confirmed decision register

| ID | Quyết định/fact | Status và allowed use |
|---|---|---|
| `TL-D01` | Facebook Page Toplink đã có tick xanh | `USER_CONFIRMED_PLATFORM_SIGNAL`; chỉ là tín hiệu xác thực danh tính trên nền tảng, không chứng minh chất lượng, pháp lý, công dụng hoặc quyền nhượng quyền |
| `TL-D02` | Follower hiện tại = 0 | `USER_REPORTED_COUNT`; phải khóa Page ID/URL + timestamp/snapshot tại `TL-M1` trước khi thành measured baseline |
| `TL-D03` | Chưa có độ nhận diện | `USER_CONFIRMED_GREENFIELD_ASSUMPTION`; không gọi là measured zero khi chưa có phương pháp đo |
| `TL-D04` | Toplink là đơn vị nhượng quyền từ Nhất Liệu Y Viện | `USER_CONFIRMED_INTERNAL`; public attribution = `NEEDS_LEGAL_DOC`; legal scope = `MISSING_INPUT` |
| `TL-D05` | Trust-led local launch là hướng lõi | `DECIDED` |
| `TL-D06` | Founder thỉnh thoảng xuất hiện; Page dùng tiếng nói doanh nghiệp | `DECIDED`; founder allowed-use vẫn confirmed-only |
| `TL-D07` | Offer-led acquisition hoãn tới khi offer/compliance đủ | `DECIDED` |
| `TL-D08` | Hà Nội là trọng tâm; toàn quốc là phạm vi awareness | `DECIDED_WITH_BOUNDARY`; không suy diễn năng lực phục vụ toàn quốc |
| `TL-D09` | Codex làm phần lớn reconciliation/finalization do session Claude ngắn | `USER_APPROVED_BOUNDED_EXCEPTION`; theo `AGENTS.md` |
| `TL-D10` | Mọi milestone phải qua DMP thật; output operational vào Google Sheets | `DECIDED`; `NO_DMP_TRACE = NOT_DONE`, `NO_SHEET_READBACK = NOT_OPERATIONALLY_COMPLETE` |
| `TL-D11` | Toplink dùng kiến trúc Sheet có functional parity với workflow đã duyệt, nhưng profile/schema/output/identifier độc lập | `USER_APPROVED_BOUNDED_DECISION`; theo `docs/system/toplink-google-sheets-operational-contract.md`; không cấp target hoặc quyền ghi |
| `TL-D12` | FB Page ID `61591880797654`; baseline = mốc bắt đầu task (2026-07-30), follower 0, greenfield | `USER_CONFIRMED_IDENTITY`; provenance user-provided (không tool-observed); badge chỉ `PLATFORM_IDENTITY_SIGNAL`; measured awareness vẫn `NO_MEASUREMENT` |
| `TL-D13` | Người review sức khỏe = user + một người thầy lành nghề | `USER_ATTESTED_AUTHORITY`; duyệt từng health-sensitive item lúc publish là bắt buộc; credential chính thức `MISSING_INPUT` |
| `TL-D14` | Google Sheet target = `1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms` (workbook Toplink-only) | `USER_PROVIDED_TARGET`; chưa phải write approval; cần SA + bounded fields + exact read-back trước khi ghi |
| `TL-D15` | Sheet auth = Service Account Toplink **mới**, không dùng credential Thảo Tây | `USER_DECISION`; SA email `PENDING_USER`; key local gitignored; Codex thực thi wiring + bounded write |

### Conflict cần giải tại `TL-M1`

Canonical cũ từng gắn `Nhất Liệu Y Viện`/một source website là `COMPETITOR`. Quyết định mới của
user xác định quan hệ entity là franchisor → franchise unit. `TL-M1` phải tách:

1. entity `Nhất Liệu Y Viện`;
2. quan hệ thương hiệu/quyền nhượng quyền;
3. source artifact/domain đã crawl;
4. allowed-use cho tài sản, benchmark, thông điệp và thành tích.

Không xóa provenance cũ. Gắn classification cũ là `SUPERSEDED_PENDING_RECONCILIATION` ở đúng
record; không biến tài sản của franchisor thành tài sản được Toplink tự do sử dụng.

## 4. Business problem

Toplink bắt đầu truyền thông Page từ greenfield audience. Tick xanh có thể giảm nghi ngờ về danh
tính Page nhưng không tạo reach, nhận diện, niềm tin, local relevance hoặc demand. Nếu đi thẳng
vào sản phẩm/ưu đãi khi evidence, offer và compliance chưa đủ, Page dễ bị đọc như một kênh bán
hàng sức khỏe thiếu proof.

Bài toán:

> Xây Facebook Page Toplink từ số 0 thành điểm chạm doanh nghiệp đáng tin: giúp đúng người hiểu
> Toplink là ai, phạm vi chăm sóc là gì, giới hạn ở đâu và vì sao trải nghiệm vận hành đáng được
> tìm hiểu — trước khi tăng áp lực chuyển đổi.

## 5. Objectives

### 5.1. 30 ngày đầu

- Thiết lập baseline Page có stable identity.
- Xây nhận diện ban đầu bằng nội dung trust-led, không hù dọa hoặc chẩn đoán.
- Tạo signal học hỏi về audience, format, câu hỏi và nhu cầu.
- Hình thành workflow DMP → Agency → compliance/human → Sheet → read-back.
- Chỉ bật commercial CTA khi offer, capacity, privacy và compliance cùng PASS.

### 5.2. Ba tháng

- Dùng pilot evidence để chọn pillar, cadence, format và local growth loop.
- Tăng operational proof có consent thay vì dựa vào claim kết quả.
- Xác định mức đóng góp phù hợp của founder mà không làm Page phụ thuộc vào personal authority.

### 5.3. Sáu tháng

- Mở rộng organic awareness toàn quốc theo evidence.
- Chỉ mở national conversion, paid media, kênh mới hoặc ecosystem module qua scope/budget/capacity
  gate riêng.

## 6. Scope

### IN

- Facebook Page Toplink là kênh chính của brand-track.
- Reels/short-form hỗ trợ Page; mechanics TikTok chỉ dùng làm tham chiếu.
- Corporate voice là mặc định; founder xuất hiện có chọn lọc.
- Hà Nội: awareness + service/conversion khi từng offer được verify.
- Toàn quốc: education/brand awareness; product/service availability phải có evidence riêng.
- Evidence mapping, DMP profile, audience/positioning, content pillars, campaign, KPI,
  production/approval, pilot, roadmap và handoff.
- Google Sheets stable-identity upsert + exact read-back sau khi user cấp target.

### OUT hoặc DEFERRED

- Chẩn đoán, điều trị, cam kết kết quả hoặc ngôn ngữ gây sợ hãi.
- Dùng tick xanh như proof chất lượng/pháp lý/công dụng.
- Public franchise wording trước legal/brand-right gate.
- Tuyên bố dịch vụ, giao hàng, bảo hành hoặc chuỗi cơ sở toàn quốc khi chưa xác minh.
- Offer-led acquisition, promotion, booking pressure khi offer/CTA chưa đủ gate.
- Paid ads scale, TikTok là kênh chính, national conversion và kênh mới trước `TL-M8`.
- Full overwrite Sheet, tab `_v2`, tái dùng workbook Thảo Tây hoặc tự tạo target.
- Tự mở hoặc thay đổi milestone của Thảo Tây.

## 7. Geographic architecture

| Lane | Vai trò | CTA được phép | Điều kiện |
|---|---|---|---|
| Hà Nội | Local awareness, operational proof, service discovery | Theo dõi/lưu bài; booking chỉ khi offer PASS | Địa chỉ, service menu, availability, contact owner, response SLA, privacy, compliance |
| Ngoài Hà Nội | Education và brand awareness | Theo dõi/lưu/chia sẻ nội dung | Không ngụ ý có cơ sở hoặc dịch vụ tại địa phương |
| Toàn quốc — sản phẩm | `DEFERRED_HYPOTHESIS` | Không commercial CTA mặc định | SKU, vùng bán, logistics, giá, bảo hành, nhãn/công bố và claim đều verify |
| Mở rộng cơ sở/chuỗi | `OUT_UNTIL_TL-M8_GATE` | Không | Evidence vận hành + user scope approval |

## 8. Audience hypotheses

Các nhóm dưới đây là `LAUNCH_AUDIENCE_HYPOTHESIS`, không phải insight đã quan sát:

| ID | Nhóm giả thuyết | Audience job | Validation signal |
|---|---|---|---|
| `TL-A01` | Người bận rộn/văn phòng 28–55 tại Hà Nội | Tìm một cách chăm sóc dễ hiểu, không bị ép bán | Save/share, câu hỏi về quy trình, qualified inquiry |
| `TL-A02` | Người trung niên/lớn tuổi và người chăm sóc cha mẹ | Muốn an tâm về phạm vi, mức tác động và hướng dẫn | Câu hỏi phù hợp/an toàn, repeat interaction |
| `TL-A03` | Phụ nữ quan tâm sức khỏe chủ động | Muốn trải nghiệm tinh tế, riêng tư, minh bạch | Engagement với proof không gian/quy trình |
| `TL-A04` | Người quan tâm dưỡng sinh trên toàn quốc | Muốn kiến thức và thói quen dễ áp dụng | Completion, save/share; không coi là service demand |

`TL-M3` phải giữ, sửa hoặc loại từng hypothesis dựa trên DMP + signal; không chốt persona giả.

## 9. Positioning và narrative hypothesis

### Internal working positioning

> Toplink hướng tới trở thành một điểm chạm dưỡng thân – tỉnh thức cho người muốn chăm sóc cơ
> thể đều đặn, kết hợp trải nghiệm chỉn chu với hệ Lý – Dược – Dưỡng được sử dụng đúng nhu cầu
> và đúng giới hạn.

Status: `HYPOTHESIS · NOT_PUBLIC_APPROVED`.

### Narrative spine

```text
Tín hiệu đời thường
→ một khoảng dừng
→ lắng nghe và giải thích không chẩn đoán
→ lựa chọn hỗ trợ có giới hạn
→ thói quen nhỏ, đều đặn
→ next step phù hợp, không gây áp lực
```

Franchise history, system achievements, standard/certification hoặc founder expertise không được
điền vào narrative nếu thiếu source và public-use authority.

## 10. Candidate content architecture

`TL-M3` phải dùng DMP để hội tụ 3–5 pillar, tổng trọng số 100%. Mỗi pillar cần audience job,
right-to-document, evidence, format/funnel fit, health/reputation risk và rationale trọng số.

| Candidate ID | Territory | Evidence/risk boundary |
|---|---|---|
| `TL-PC1` | Toplink là ai, phạm vi và giới hạn | Franchise/legal wording gated; tick xanh không là proof chất lượng |
| `TL-PC2` | Hiểu và lắng nghe tín hiệu cơ thể | Health-sensitive; cấm causal/diagnostic wording; professional review theo item |
| `TL-PC3` | Operational proof: không gian, quy trình, vệ sinh, con người | Chỉ fact vận hành; qualification/outcome/testimonial có gate riêng |
| `TL-PC4` | Lý – Dược – Dưỡng dễ hiểu | Từng SKU/service phải có dossier và public naming registry |
| `TL-PC5` | Hành trình Toplink, founder và cộng đồng | Founder chỉ nói hành trình/triết lý/vận hành; privacy/consent bắt buộc |

### Founder guardrail

- Corporate voice là mặc định.
- Trước khi có pilot evidence, founder-led item không quá 1 trong mỗi 5 item planned và không
  dùng hai founder-led commercial CTA liên tiếp.
- Public role chỉ là `Founder/điều hành Toplink Y Viện` theo evidence hiện có.
- Không dùng founder để giải thích cơ chế, chỉ định sản phẩm, chẩn đoán hoặc nói thay chuyên gia.
- Cross-post sang Facebook cá nhân là external action riêng, cần item-level approval.

## 11. Facebook Page và 30-day campaign hypothesis

### Channel roles

| Channel | Vai trò |
|---|---|
| Facebook Page Toplink | Corporate identity, education, operational proof, community signal |
| Reels trên Facebook | Discovery, retention mechanics và diễn giải ngắn |
| Facebook cá nhân Thảo Tây | Selective founder context/cross-post; không phải distribution mặc định |
| Website/Zalo/phone/Maps | `PENDING_INPUT`; chỉ kích hoạt vai trò conversion khi identity/ownership/flow verify |
| TikTok | Mechanics review only; chưa là primary deliverable |

### Relative four-week arc

| Tuần | Vai trò | Hard gate |
|---|---|---|
| W1 | Toplink là gì/không phải gì; identity và giới hạn | Page identity + public brand/franchise wording gate |
| W2 | Tín hiệu đời thường, thói quen và body literacy | Claim inventory + DMP `check` + professional review |
| W3 | Không gian, quy trình, vệ sinh, đội ngũ | Operational proof only; qualification/outcome/consent gate |
| W4 | `EVIDENCE-CLEARED SOLUTION` hoặc `SAFE FALLBACK` | Từng SKU/service dossier PASS; thiếu thì dùng brand/process content |

CTA mặc định trước offer gate: theo dõi Page, lưu hoặc chia sẻ nội dung. Booking/tư vấn CTA chỉ
mở khi có exact offer/service, eligibility, location, availability, contact ownership, response
SLA, privacy notice, price/condition nếu nhắc và compliance verdict.

## 12. DMP architecture — bắt buộc

Brand slug duy nhất dự kiến: `toplink-y-vien`. Không tạo thêm profile `toplink-page` cho cùng
entity. `TL-M2` cập nhật profile này để Facebook Page là primary channel của Toplink track.

```text
active-brand/version/profile/source gate
→ import-guidelines + brand-setup
→ audience-intelligence
→ campaign-plan + social-strategy + content-engine
→ content-calendar + video-script
→ check
→ Agency review
→ human/professional gates
→ local canonical candidate
→ Google Sheets plan/approval/upsert/read-back
```

### Real invocation trace contract

Mỗi milestone sinh deliverable phải ghi:

```text
trace_id · timestamp · DMP_version · active_brand_readback
· skill · exact_input_paths · input_digest · invocation_mode
· output_path · output_digest · status · skipped_dimensions
```

- `NO_TRACE = NOT_DONE`.
- `SKILL_CONTRACT_REVIEW` không phải `REAL_DMP_INVOCATION`.
- Không switch brand hoặc sửa runtime ngầm.
- Nếu DMP runtime/skill không chạy được: `BLOCKED_DMP_RUNTIME`; manual draft không thay thế.
- Run 2 audit/repair; chỉ regenerate qua DMP khi finding yêu cầu và phải trace invocation mới.

## 13. Agency routing

| Workstream | DMP | Reviewer route | Gate |
|---|---|---|---|
| Evidence/profile/franchise map | `import-guidelines`, `brand-setup` | PR Manager | Entity/allowed-use/legal status |
| Audience/positioning | `audience-intelligence`, `campaign-plan` | Social Strategist → Growth Hacker | Hypothesis/provenance |
| Page/pillars/campaign | `social-strategy`, `campaign-plan`, `content-engine` | Social Strategist + Content Creator; Growth review khi KPI | 3–5 pillar/100%, geo/founder boundary |
| Calendar/copy | `content-calendar`, `content-engine` | Content Creator → PR Manager | Capacity/originality/claim gate |
| Reels | `video-script` | Short-Video Coach → TikTok Strategist | Facebook-first, anti-copy, accessibility |
| Health-sensitive | `check` | PR Manager → human professional | Agent không tự `APPROVED` |

Tối đa 3 Agency Agents/workstream. Artifact không đổi không review lại. Reviewer trả issue,
severity, evidence/location, required repair và verdict; không silently rewrite.

## 14. Claude ↔ Codex orchestration

### Ownership target

| Runtime | Khoảng tải | Sở hữu |
|---|---:|---|
| Claude Code | 20–25% | DMP raw-authoring, strategic/creative specialist review, fresh audit, handoff ngắn |
| Codex CLI | 75–80% | Evidence reconciliation, stable identity, schema/manifest, cross-workstream QA/repair có nguồn, local promotion, Sheet plumbing/read-back |

Tỷ lệ là design target, không phải token guarantee. Claude vẫn là bắt buộc cho DMP real
invocation. Codex exception bị giới hạn bởi `AGENTS.md`; không mở quyền thêm fact/claim.

### Lease/handoff invariant

```text
writer lấy exact file-set lease ở root task.md
→ generate/repair
→ ghi trace + digest + status + blocker + next actor
→ writer dừng ghi
→ release lease
→ next actor verify marker/digest
→ next actor mới lấy lease
```

Reviewer read-only không cần lease. Không hai writer trên cùng file set. Stale lease hoặc digest
drift = stop affected mutation và escalate.

## 15. Model và token policy

| Work | Claude | Codex | Context rule |
|---|---|---|---|
| Bounded retrieval/source excerpt | Haiku nếu runtime có | Terra `medium` | Chỉ exact section/path |
| DMP raw draft/synthesis | Sonnet | Terra/Sol review | Không load lại full corpus |
| Strategy/creative conflict | Opus khi cần | Sol `high` | Một bounded package |
| Evidence/privacy/health conflict | Opus review | Sol `xhigh`; `max` chỉ escalation | Không nén mất claim/evidence |
| Schema/identity/manifest/Sheet | Claude review ngắn | Terra `high` hoặc Sol final | Machine-verifiable |

- `fork_turns=none` cho reviewer; truyền contract + path + excerpt tối thiểu.
- `TL-M1` tạo frozen source manifest/evidence map; downstream không đọc lại toàn bộ corpus.
- Context warning 55%; checkpoint/handoff 70%; không mở stage mới nếu dự kiến vượt 80%.
- Output reviewer dùng `issue · severity · evidence · repair · gate`.
- Không dùng model mạnh cho hash/inventory/mechanical formatting.

## 16. Evidence, health, legal và privacy

### Status vocabulary

| Status | Allowed use |
|---|---|
| `USER_CONFIRMED_INTERNAL` | Project planning; chưa tự thành public/legal wording |
| `PLATFORM_IDENTITY_SIGNAL` | Chỉ mô tả trạng thái nền tảng |
| `TOPLINK_CONFIRMED` | Dùng trong sourced meaning |
| `HYPOTHESIS` | Testable proposal |
| `MISSING_INPUT` / `BLOCKED_INPUT` | Không hỗ trợ claim hoặc Done |
| `NEEDS_LEGAL_DOC` | Không publish legal/franchise assertion |
| `NEEDS_HUMAN_REVIEW` | Không publish health-sensitive item |
| `APPROVED` | Chỉ human authority hợp lệ, gắn item/version |

### Claim and approval order

```text
evidence/permitted claim
→ bounded wording
→ disclaimer bổ sung
→ DMP check
→ professional/legal/privacy review theo risk
→ human publish approval
```

Thêm chữ “hỗ trợ” hoặc disclaimer không hợp pháp hóa claim thiếu nguồn. Material edit ở copy,
visual, SKU/model, source, disclaimer hoặc CTA làm approval cũ hết hiệu lực.

Approval ledger tối thiểu:

```text
content_id · revision/hash · claim_ids · SKU/model · source_set
· visual_ref · risk_class · DMP_check · reviewer_role/name
· gate_type · date · verdict · conditions/expiry · publish_status
```

Không lưu chi tiết sức khỏe/PII không cần thiết. Testimonial/UGC cần consent theo purpose,
channel, duration, withdrawal và redaction; không generalize thành outcome proof.

## 17. KPI và experimentation

### Baseline rules

- Follower count chỉ ghi `0` sau Page identity + timestamp snapshot.
- Awareness hiện là `NO_MEASUREMENT`, không phải measured zero.
- Count metrics có thể bắt đầu từ 0; rate/history metrics = `N/A` tới khi có mẫu.
- Không báo cáo `% growth from zero`.
- Tick xanh không phải trust KPI.

### Signal dictionary khởi tạo

| Nhóm | Signal | Cách dùng |
|---|---|---|
| Distribution | Reach, impressions, video starts | Absolute counts; source/time window bắt buộc |
| Attention | Completion/retention theo format | Chỉ sau khi denominator đủ |
| Utility | Save/share, câu hỏi đúng chủ đề | Learning signal, không gọi là trust achieved |
| Relationship | Follower mới, repeat interaction | Cohort/time window rõ |
| Intent | Qualified inbox, contact click, booking có source | Chỉ khi CTA/booking gate PASS |
| Risk | Comment hiểu sai, claim escalation, approval turnaround | Repair/compliance input |
| Operations | Output đúng lịch, response SLA, review failure | Capacity signal |

`TL-M4` định nghĩa metric/formula/source/owner/cadence; target số chỉ khóa sau baseline và capacity.

## 18. Google Sheets operational architecture

### Current gate

```text
spreadsheet_id = 1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms · VERIFIED_TOPLINK_ONLY
approved_tabs  = 14-tab V2 delivery consumed; 24-tab correction pending
approved_range = CORRECTION_BUNDLE_PENDING
write_approval = NOT_GRANTED_FOR_CORRECTION
```

Không tái dùng workbook Thảo Tây, tự tạo workbook/tab hoặc suy diễn target. User có thể cấp target
mới hoặc target hiện hữu; chỉ exact target trong approval mới có hiệu lực.

### Logical dataset map

The operational model uses exactly 24 functional datasets/tabs:

```text
TL_REPORT
TL_OWNER_ACTIONS
TL_CONTROL
TL_SOURCE_INVENTORY
TL_INPUT_GAPS
TL_OUTPUT_INDEX
TL_DECISIONS
TL_KPI_DICTIONARY
TL_COMPLIANCE_RULES
TL_BRAND_PROFILE
TL_RUNTIME_COMPATIBILITY
TL_PAGE_BENCHMARK
TL_AUDIENCE_HYPOTHESES
TL_POSITIONING
TL_NARRATIVE
TL_CONTENT_PILLARS
TL_FACEBOOK_STRATEGY
TL_CAMPAIGN
TL_EXPERIMENTS
TL_CONTENT_CALENDAR
TL_ASSET_BATCH_PLAN
TL_REELS_BRIEFS
TL_PRODUCTION_BRIEFS
TL_WORKFLOW_APPROVAL
```

Canonical artifacts and datasets map many-to-many through `TL_OUTPUT_INDEX`. Canonical Markdown
remains human-readable source-of-truth; deterministic normalized JSON sidecars are the machine
interface. No `_v2`; update by stable identity.

### Stable identity

```text
TL-{ARTIFACT}-{NNN}
TL-CONTENT-D{01..28}-{A|B|C}
TL-CLAIM-{NNN}
TL-APPROVAL-{CONTENT_ID}-{REVISION}
```

ID immutable; wording edit không đổi ID. Validator phải kiểm uniqueness, reference integrity và
orphan. Source manifest dùng relative path, UTF-8, SHA-256; newline normalization phải được khóa
trước Run 1 và giữ tới hết Run 2.

### Sync state machine

```text
LOCAL_STAGING
→ LOCAL_VERIFIED
→ SYNC_PENDING_APPROVAL
→ SYNC_READY_APPROVAL
→ SYNC_WRITTEN_UNVERIFIED
→ SYNC_READBACK_PASS
→ OPERATIONALLY_COMPLETE
```

Read-back kiểm exact range, row/key, formula/value, Unicode, stable ID và mọi gate field. Write
acknowledgement không phải PASS. Health-sensitive row bắt buộc giữ content hash, claim IDs,
risk, DMP check, reviewer/conditions và publish status; không có null→approved default.

## 19. Two-run architecture

`TL-M1`–`TL-M5` chạy đúng hai macro-run:

1. `TOPLINK_RUN1_BUILD`: Claude DMP raw-authoring → handoff/release → Codex reconciliation.
   Local only; `external_writes=0`.
2. `TOPLINK_RUN2_FRESH_AUDIT_FINALIZE`: fresh Claude blind audit/DMP check/Agency review →
   handoff/release → fresh Codex independent audit/repair/local promotion/Sheet sync.

Hai run dùng cùng `profile_digest`, `source_digest`, DMP version và active brand. Drift:
`FAIL_BACK_TO_RUN1`; không tạo Run 3. `TL-M1`–`TL-M5` chỉ complete khi paired manifests PASS và
Sheet correction `SYNC_READBACK_PASS`. Until the new digest-bound correction approval and read-back,
the state is `LOCAL_VERIFIED · SYNC_PENDING_APPROVAL`; it is not operationally complete.

Canonical promotion, Sheet sync và Facebook Page mutation là ba action khác nhau. Page publish/
bio/CTA/cross-post luôn cần item/action approval riêng và không nằm mặc định trong Run 2.

## 20. Cây thư mục đích

Chỉ hai file chính được tạo trong work item này. Các thư mục còn lại được tạo theo milestone:

```text
docs Toplink/
├── 00_INDEX.md + 01…10 + hồ sơ hiện hữu
├── TOPLINK_PAGE_MASTER_PLAN.md
├── TOPLINK_PAGE_MILESTONES.md
├── research/
├── brand/
├── content/
├── system/
├── prompts/
└── staging/
    ├── run1/
    └── run2/
```

Không tạo `task.md`, `STATE.md`, `MEMORY.md`, `RULES.md` hoặc `GOVERNANCE.md` thứ hai trong cây.

## 21. Risks và mitigation

| Risk | Mức | Mitigation |
|---|---|---|
| Franchise/competitor canonical conflict | Critical | Entity/allowed-use reconciliation ở `TL-M1`; no public wording |
| Health claim laundering | Critical | Claim ledger → DMP check → professional/human gate |
| Tick xanh bị hiểu sai | High | `PLATFORM_IDENTITY_SIGNAL` + forbidden inference |
| National awareness thành national service claim | High | Geo lane matrix và item-level CTA gate |
| Greenfield KPI bị thổi phồng | High | Counts/rates rule; no `% from zero` |
| Offer/booking chưa sẵn sàng | High | Non-commercial CTA fallback |
| W4 thiếu dossier | High | `EVIDENCE-CLEARED` hoặc `SAFE FALLBACK`, không bypass lịch |
| Hai runtime ghi đè | High | Exact lease/handoff/digest |
| DMP trace giả | Critical | `NO_TRACE = NOT_DONE`; runtime blocker rõ |
| Sheet correction approval chưa có | Critical | `BOUNDED_APPROVAL_PENDING`; no invented/reused target or approval |
| Approval rơi khi sync/edit | Critical | Immutable gate fields + content hash/reset rule |
| Token/context waste | Medium | Frozen manifest + section-level routing + thresholds |

## 22. Open gates

1. Official Page URL/Page ID, display name, badge/follower snapshot và ngày.
2. Hồ sơ/quyền public attribution quan hệ nhượng quyền.
3. Legal name, license và phạm vi hoạt động.
4. Service menu, giá, availability, booking/contact ownership và response SLA.
5. Product dossiers: model/spec/IFU/label/công bố/chống chỉ định/bảo hành.
6. Asset, staff title, testimonial/UGC consent.
7. Google Sheets spreadsheet/tab/range/schema + approval.
8. `TOPLINK_CONTENT_START_DATE`, weekly production capacity và reviewer authority.

## 23. Plan review reconciliation

Plan này đã qua Codex skill review + fresh-context adversarial review và Claude Code
`SKILL_CONTRACT_REVIEW` DMP 3.15.1. Không review nào là real DMP invocation.

- Accepted: canonical delegation, scope amendment, entity/legal/health gates, same-slug profile,
  Page identity, greenfield KPI, geo boundary, founder boundary, W4 fallback, exact DMP trace,
  Codex exception, paired two-run, Sheet state machine và approval-field integrity.
- Rejected as overreach: bắt buộc workbook “mới”. User chỉ nói sẽ cung cấp target sau; plan cấm
  tự tái dùng và chấp nhận đúng target user duyệt, dù mới hay hiện hữu.
- Rejected: chuyển path sang `docs/toplink/`. User đã chỉ định `docs Toplink/`; nguồn hiện hữu có
  stable references tại path này.
- Repaired: không tạo profile `toplink-page`; dùng entity slug duy nhất `toplink-y-vien` và cập
  nhật channel role ở `TL-M2`.

## 24. Success contract

Brand-track chỉ được gọi hoàn thành khi:

- `TL-M0`–`TL-M9` đạt Done gate theo canonical milestones;
- mọi deliverable có DMP real invocation trace và Agency verdict;
- mọi public health/legal item có đúng human gate;
- paired Run 1/Run 2 manifests PASS, không Run 3;
- Google Sheets stable-identity upsert + exact read-back PASS;
- không có target/tab `_v2`, full overwrite, approval giả hoặc Page mutation ngoài authorization;
- Thảo Tây personal track và Toplink corporate track vẫn tách bạch.
