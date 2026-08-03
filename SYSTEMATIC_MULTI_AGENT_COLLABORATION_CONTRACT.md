# HỢP ĐỒNG CỘNG TÁC ĐA TÁC NHÂN CÓ HỆ THỐNG

## 0. Kiểm soát tài liệu

| Trường | Giá trị |
|---|---|
| Phiên bản giao thức | 1.0.0 |
| Trạng thái | Chuẩn tắc, có thể sao chép và tùy biến |
| Đối tượng | Nhóm người, tác nhân AI và hệ thống tự động cùng tạo, kiểm tra, phê duyệt hoặc chuyển giao công việc |
| Phạm vi | Điều phối công việc, bằng chứng, quyền ghi, bàn giao, kiểm toán và thay đổi bên ngoài |
| Không bao gồm | Cài đặt công cụ, chính sách ngành cụ thể, hoặc triển khai dịch vụ điều phối |

Tài liệu này là một hợp đồng vận hành độc lập. Bên áp dụng **MUST** xác định các giá trị trong dấu `<...>` trước khi bắt đầu; không được suy diễn giá trị thiếu. Các tên nhãn mặc định như “Claude” và “Codex” chỉ là ví dụ thay thế được cho hai vai trò; giao thức không phụ thuộc vào một sản phẩm, ngôn ngữ, kho mã, hệ quản trị phiên bản hay bố cục thư mục nào.

### 0.1 Ngôn ngữ chuẩn tắc

- **MUST / MUST NOT**: bắt buộc / bị cấm; vi phạm làm kết quả không phù hợp giao thức.
- **SHOULD / SHOULD NOT**: mặc định phải làm / không nên làm; ngoại lệ phải được ghi trong `DecisionRecord`, nêu lý do, chủ sở hữu và thời hạn.
- **MAY**: tùy chọn, không tạo quyền ngầm định.

### 0.2 Giả định và thuật ngữ

`Actor` là người, runtime hoặc tiến trình có định danh ổn định. `Runtime` là tác nhân thực thi. `Scope` là tập đối tượng có thể đọc/ghi được mô tả chính xác. `Artifact` là đầu ra có ID ổn định. `Evidence` là tham chiếu có thể kiểm tra tới nguồn, nhật ký, digest, kết quả kiểm tra hoặc phê duyệt. `Digest` là băm của dạng chuẩn hóa đã công bố. `Custody` là trách nhiệm giữ và chuyển giao hiện trạng, không phải thẩm quyền. `Adapter` là cách cài đặt có thể thay thế (tệp, cơ sở dữ liệu, công cụ kiểm tra, hệ thống ngoài). `External mutation` là thay đổi trạng thái ngoài vùng kiểm soát cục bộ.

## 1. Thẩm quyền, bất biến và chính sách

### 1.1 Thứ tự ưu tiên

Khi mâu thuẫn, áp dụng theo thứ tự: (1) luật, hợp đồng và chỉ thị an toàn có thẩm quyền; (2) phê duyệt người hợp lệ, chưa hết hạn và đúng phạm vi; (3) tài liệu quyền hạn đã được kiểm soát phiên bản; (4) hợp đồng này; (5) quyết định đã ghi; (6) kế hoạch/mốc; (7) đầu ra tác nhân. Mâu thuẫn cùng cấp **MUST** chuyển `BLOCKED_AUTHORITY`; không được chọn nguồn thuận tiện hơn.

### 1.2 Bất biến giao thức

1. Mỗi phạm vi ghi chỉ có một writer lease `ACTIVE` tại một thời điểm.
2. Không trạng thái nào được nâng cấp nếu thiếu bằng chứng nhập trạng thái.
3. Bàn giao chỉ chuyển custody khi được chấp nhận; không chuyển thẩm quyền, không mở rộng scope.
4. Không tác nhân AI, bộ kiểm tra tự động hay reviewer tự cấp phê duyệt của con người về pháp lý, an toàn, riêng tư, xuất bản, tài chính hoặc sản xuất.
5. Thay đổi ngoài hệ thống **MUST** có target chính xác, hành động bị chặn biên, bằng chứng phê duyệt, và read-back chính xác.
6. Run 2 phải là kiểm toán độc lập với ngữ cảnh mới; không phải phần nối tiếp mơ hồ của Run 1.
7. Không chắc chắn, drift, ghi một phần hoặc thiếu bằng chứng phải fail closed cho phạm vi ảnh hưởng.

Các bất biến không được “tùy biến”. Việc bỏ một bất biến tạo giao thức khác và **MUST NOT** được tuyên bố phù hợp hợp đồng này.

### 1.3 Bề mặt chính sách được tùy biến

Bên áp dụng **MUST** công bố: `<CONTROL_ROOT>`, nơi lưu ledger; tên/định danh role; chu kỳ lease và ngưỡng stale; hàm chuẩn hóa/digest; loại review; danh mục tier phê duyệt; hệ status bổ sung; miền rủi ro; target adapter; và tiêu chí Done. Các lựa chọn này **MUST NOT** làm yếu các bất biến ở 1.2.

## 2. Vai trò và phân tách nhiệm vụ

| Vai trò | Trách nhiệm | Có thể | Không được |
|---|---|---|---|
| `AUTHORING_RUNTIME` | Tạo/sửa bản nháp, tổng hợp đầu vào, đề xuất | Có lease đúng scope, tạo Artifact và Run 1 | Tự phê duyệt người hoặc tự xác nhận độc lập sản phẩm của mình |
| `CONTROL_RUNTIME` | Đối soát bằng chứng, manifest, phạm vi, trạng thái | Kiểm tra, lập issue, Run 1 reconciliation, Run 2 finalize | Ghi chồng lên lease khác, biến review thành approval |
| `REVIEWER` | Đánh giá chuyên môn theo rubric | Trả verdict và issue có căn cứ | Mở rộng scope hoặc cấp human approval nếu không được ủy quyền |
| `HUMAN_APPROVER` | Cấp/thu hồi quyết định thuộc tier được ủy quyền | Ký approval đúng target, action, hạn dùng | Phê duyệt mù hoặc ngoài thẩm quyền |
| `CUSTODIAN` | Duy trì ledger, phục hồi lease bỏ quên | Xác thực record và tiến hành recovery | Tự thay thế evidence thiếu |

Một runtime có thể mang nhiều vai trò chỉ khi `Policy` ghi rõ xung đột đã được giảm thiểu. Với nội dung rủi ro cao, người/role thực hiện Run 2 **SHOULD NOT** là người duy nhất thực hiện Run 1. Ví dụ adapter có thể gán `AUTHORING_RUNTIME=Claude`, `CONTROL_RUNTIME=Codex`; các tên này hoàn toàn có thể đổi.

### 2.1 Định tuyến theo năng lực và preflight

`AUTHORING_RUNTIME=Claude` và `CONTROL_RUNTIME=Codex` là **nhãn adapter mặc định, có thể thay thế**, không phải tuyên bố phụ thuộc sản phẩm hay bảo đảm năng lực. Theo policy mặc định, Authoring Runtime mạnh hơn ở việc tạo bản nháp có ngữ cảnh, tổng hợp ý nghĩa, diễn đạt, và sửa nội dung có thực chất; rủi ro chính là tự củng cố cách diễn giải hoặc bỏ sót sai lệch cấu trúc/evidence của chính bản nháp. Control Runtime mạnh hơn ở đối soát scope, cấu trúc, schema, manifest, digest, truy vết thay đổi và kiểm tra lặp lại; rủi ro chính là sửa máy móc nhưng làm sai ý nghĩa, hoặc coi kiểm tra cấu trúc là xác nhận nội dung. Mỗi adopter **MUST** xác nhận các giả định này bằng capability preflight cho runtime thực tế; nếu không đạt, phải gán lại vai trò hoặc `BLOCKED_CAPABILITY`.

Capability preflight **MUST** ghi: `<RUNTIME_ID>`, phiên bản/cấu hình adapter nếu có, task class, quyền đọc/ghi thực tế, khả năng tạo và kiểm tra artifact, hạn chế đã biết, dữ liệu thử tối thiểu, kết quả `PASS|FAIL|LIMITED`, người/chủ policy xác nhận và thời hạn hiệu lực. Preflight không cấp approval, không mở rộng quyền ghi, và phải chạy lại khi runtime, adapter, quyền hoặc task class thay đổi material.

| Task class | Primary mặc định | Verifier bắt buộc | Vì sao/phù hợp năng lực | Hành động bị cấm | Handoff trigger | Escalation |
|---|---|---|---|---|---|---|
| Tổng hợp nguồn, lập luận, viết hoặc sửa nội dung thực chất | `AUTHORING_RUNTIME` | `CONTROL_RUNTIME` + reviewer phù hợp khi policy yêu cầu | Cần hiểu ngữ nghĩa, mục tiêu và tác động của thay đổi | Control Runtime tự viết lại nội dung thực chất chỉ từ kiểm tra cấu trúc | Bản nháp, input digest và scope đã checkpoint | `BLOCKED_CAPABILITY` hoặc human/reviewer nếu không có người kiểm semantic |
| Structural audit: schema, ID, digest, liên kết, trạng thái, scope, manifest | `CONTROL_RUNTIME` | Runtime khác hoặc kiểm tra xác định được theo policy | Cần tái lập, đối soát và evidence có thể truy vết | Gọi PASS cấu trúc là đúng ngữ nghĩa hoặc approval | Trước Run 1 pass, external mutation, hoặc Run 2 | `BLOCKED_EVIDENCE` khi không tái lập được kiểm tra |
| Semantic audit: đúng nghĩa nguồn, logic, yêu cầu, rủi ro, mức đầy đủ | `CONTROL_RUNTIME` hoặc reviewer độc lập có năng lực domain | Role/human độc lập theo tier rủi ro | Cần đánh giá ý nghĩa, không chỉ parse/so khớp | Dùng một structural audit để thay semantic audit | Khi có claim, quyết định, thay đổi policy hoặc rủi ro material | Human/domain review; `BLOCKED_CAPABILITY` nếu auditor không đủ năng lực |
| Mechanical evidence-preserving repair: định dạng, liên kết, ID, trường thiếu, manifest, lỗi parse | `CONTROL_RUNTIME` | Chủ artifact hoặc kiểm tra xác định | Sửa có thể chứng minh không đổi meaning, scope, allowed action hay digest input | Đổi yêu cầu, claim, lập luận, approval, target hoặc policy dưới nhãn “mechanical” | Sau repair phải checkpoint và nêu proof preservation | Reset Run 1 nếu không chứng minh được preservation |
| Re-authoring thực chất: đổi meaning, lập luận, claim, quyết định, target, scope hoặc Done gate | `AUTHORING_RUNTIME` hoặc owner được policy chỉ định | `CONTROL_RUNTIME` + reviewer/human gate phù hợp | Đây là thay đổi ngữ nghĩa cần chịu trách nhiệm tác giả | Control Runtime tự thực hiện trong pha audit/finalize mà không reset | Ngay khi phát hiện thay đổi material | `RESET_TO_RUN1`; xin authority/approval mới nếu cần |
| External mutation và exact read-back | Executor được policy ủy quyền, mặc định `CONTROL_RUNTIME` | `CONTROL_RUNTIME` độc lập hoặc người/adapter khác theo policy | Cần preflight, bounds, receipt và read-back chính xác | Authoring Runtime suy diễn thành công từ acknowledgement; bất kỳ runtime nào tự cấp approval | Sau approval còn hiệu lực và trước/ sau write | `BLOCKED_AUTHORITY`, `PARTIAL_WRITE` hoặc `VERIFY_FAILED` |

Structural audit trả lời “record có đúng shape, liên kết và evidence kỹ thuật không”; semantic audit trả lời “nội dung có đúng nghĩa, đủ, hợp lệ và an toàn trong authority/rubric không”. Cả hai **MUST** có verdict và evidence riêng; không verdict nào thay thế verdict kia khi task class yêu cầu cả hai.

Role swap chỉ **MAY** xảy ra trước acquisition hoặc sau release/handoff `ACCEPTED`, khi capability preflight mới chứng minh runtime nhận vai trò đáp ứng task class và policy ghi `DecisionRecord` nêu lý do, scope, thời hạn, verifier độc lập và biện pháp giảm xung đột. Swap **MUST NOT** làm một runtime vừa là người duy nhất re-author nội dung material vừa tự xác nhận semantic audit độc lập trong cùng package; không được swap để né human gate, lease conflict, Run 2 fresh-context hay `RESET_TO_RUN1`. Khi primary không sẵn sàng hoặc preflight `FAIL|LIMITED`, Custodian phải giữ scope `BLOCKED_CAPABILITY`, chọn runtime thay thế qua DecisionRecord hoặc chia task thành phần semantic/structural không giao nhau; không được hạ chuẩn audit để tiếp tục.

## 3. Định danh, phạm vi và ledger

Mọi record **MUST** có `schema_version`, `id`, `created_at`, `updated_at`, `actor_id`, `status`, và `evidence_refs` (mảng rỗng chỉ hợp lệ nếu trạng thái chưa đòi evidence). ID phải ổn định, không tái sử dụng, ví dụ `<WORK_ID>`, `<MILESTONE_ID>`, `<ARTIFACT_ID>`, `<RUN_ID>`. Đổi tên hiển thị không đổi ID.

`Scope` **MUST** liệt kê đối tượng logic cụ thể, quyền (`read|write`), và ranh giới loại trừ. Các scope giao nhau về đối tượng ghi là chồng lấn kể cả khi đường dẫn/vị trí adapter khác nhau. Ledger là nguồn trạng thái sống duy nhất; adapter **MUST** hỗ trợ cập nhật nguyên tử hoặc cơ chế tương đương để phát hiện cạnh tranh.

### 3.1 Schema nền và record bắt buộc

`StableIdentity` gồm `namespace`, `kind`, `key`, `value`, và `immutable=true`; key/value phải đủ để đọc lại đúng một đối tượng ở adapter mục tiêu. `DigestRecord` gồm `algorithm`, `canonicalization`, `value`, `subject_ref`, `computed_at`, `computed_by`. Không được dùng digest rút gọn thay bằng chứng đầy đủ.

```json
{
 "stable_identity":{"namespace":"docs","kind":"guide","key":"record_id","value":"GUIDE-01","immutable":true},
 "digest":{"algorithm":"sha256","canonicalization":"UTF-8 LF, no trailing whitespace","value":"sha256:...","subject_ref":"logical://artifact/A-17","computed_at":"2026-01-01T00:00:00Z","computed_by":"control-01"}
}
```

`LeaseRecord` phải thêm `holder`, `scope`, `requested_at`, `activated_at`, `expires_at`, `checkpoint_refs`, `conflict_check_ref`, `release_reason`. `CheckpointRecord` phải thêm `lease_id`, `artifacts`, `checks`, `issues_open`, `blockers`, `approval_refs`, `next_safe_action`.

```json
{
 "schema_version":"1.0", "id":"L-21", "status":"ACTIVE", "actor_id":"author-01", "holder":"author-01",
 "scope":{"write_objects":["artifact:A-17"],"excluded":["external:*"]}, "requested_at":"2026-01-01T00:00:00Z",
 "activated_at":"2026-01-01T00:01:00Z", "expires_at":"2026-01-01T01:01:00Z", "checkpoint_refs":[],
 "conflict_check_ref":"CC-21", "release_reason":null, "created_at":"2026-01-01T00:00:00Z", "updated_at":"2026-01-01T00:01:00Z", "evidence_refs":["CC-21"]
}
```

```json
{
 "schema_version":"1.0", "id":"CP-88", "status":"CHECKPOINTED", "actor_id":"author-01", "lease_id":"L-21",
 "artifacts":[{"id":"A-17","digest":"sha256:...","status":"GENERATED"}], "checks":[{"id":"C-1","verdict":"PASS"}],
 "issues_open":["I-09"], "blockers":[], "approval_refs":[], "next_safe_action":"offer H-042",
 "created_at":"2026-01-01T00:02:00Z", "updated_at":"2026-01-01T00:02:00Z", "evidence_refs":["LOG-01"]
}
```

`ArtifactRecord` phải có `stable_identity`, producer, input digests, location-adapter reference, trạng thái và promotion/external-write references. `IssueRecord` phải có `severity`, `detected_by`, `affected_scope`, `closure_criteria`, `owner`, `status`; `DecisionRecord` phải có `alternatives`, `rationale`, `authority_ref`, `impact`, `review_at`.

```json
{
 "schema_version":"1.0", "id":"A-17", "status":"LOCALLY_VERIFIED", "actor_id":"author-01",
 "stable_identity":{"namespace":"docs","kind":"guide","key":"record_id","value":"GUIDE-01","immutable":true},
 "producer":"author-01", "input_digests":["sha256:..."], "location_ref":"logical://artifact/A-17",
 "promotion_refs":[], "external_write_refs":[], "created_at":"2026-01-01T00:01:00Z",
 "updated_at":"2026-01-01T00:05:00Z", "evidence_refs":["RM-R1-017"]
}
```

```json
{
 "issue":{"schema_version":"1.0","id":"I-09","status":"OPEN","actor_id":"control-01","severity":"HIGH","detected_by":"C-1","affected_scope":"artifact:A-17","owner":"author-01","closure_criteria":"digest and citation corrected","created_at":"2026-01-01T00:03:00Z","updated_at":"2026-01-01T00:03:00Z","evidence_refs":["C-1"]},
 "decision":{"schema_version":"1.0","id":"D-01","status":"APPROVED","actor_id":"human-07","alternatives":["defer","revise"],"rationale":"scope remains bounded","authority_ref":"AUTH-02","impact":"replace A-17","review_at":"2026-02-01T00:00:00Z","created_at":"2026-01-01T00:04:00Z","updated_at":"2026-01-01T00:04:00Z","evidence_refs":["SIG-01"]}
}
```

## 4. Máy trạng thái

Ký hiệu `A -> B [evidence]` là chuyển tiếp được phép. Mọi chuyển tiếp không liệt kê đều bị cấm. “Terminal” không có chuyển tiếp thường; mở lại chỉ qua record quyết định mới.

Mỗi state machine trong mục này có record ID ổn định. Trạng thái khởi tạo chỉ được nhập khi có evidence tạo record; mọi transition không phải khởi tạo **MUST** mang evidence trong guard `[...]`. Mọi transition không được liệt kê đều bị cấm; terminal state không có outbound transition, trừ khi machine nêu rõ việc tạo record hoặc instance mới cho recovery.

### 4.1 Work item

`PROPOSED -> PLANNED [authority, scope, owner] -> READY [dependencies, plan] -> IN_PROGRESS [active lease] -> VERIFYING [artifact+manifest] -> COMPLETE [Done gate]`.

`PROPOSED|PLANNED|READY|IN_PROGRESS|VERIFYING -> BLOCKED [blocker record]`; `PROPOSED|PLANNED|READY -> CANCELLED [authorized cancellation]`; mọi trạng thái chưa terminal `-> SUPERSEDED [replacement ID, authority]`. `COMPLETE`, `CANCELLED`, `SUPERSEDED` là terminal. `BLOCKED ->` trạng thái trước đó chỉ khi blocker được đóng với evidence. Cấm `READY -> COMPLETE`, `BLOCKED -> COMPLETE`.

### 4.2 Lease

`ABSENT -> REQUESTED [scope, holder, duration] -> ACTIVE [conflict check pass, acquisition evidence] -> CHECKPOINTED [checkpoint] -> RELEASED [release record]`.

`ACTIVE -> CHECKPOINTED [checkpoint record] -> ACTIVE [checkpoint accepted, lease unexpired, scope/holder unchanged]`; `ACTIVE|CHECKPOINTED -> RELEASED [release record]`; `ACTIVE|CHECKPOINTED -> EXPIRED [clock evidence]`; `ACTIVE|CHECKPOINTED -> ABANDONED [interruption evidence]`; `EXPIRED|ABANDONED -> REQUESTED [recovery record]`. `RELEASED` là terminal của một lease instance. Cấm sửa scope/holder của `ACTIVE|CHECKPOINTED`, và cấm `EXPIRED -> ACTIVE` không qua acquisition mới.

### 4.3 Artifact

`PLANNED -> GENERATED [producer, input digest] -> REVIEWED [review record] -> LOCALLY_VERIFIED [verification manifest] -> PROMOTION_READY [all gates] -> PROMOTED [promotion evidence]`. Nếu cần đồng bộ ngoài: `PROMOTION_READY -> SYNC_READY [approval+write plan] -> WRITTEN_UNVERIFIED [write receipt] -> READBACK_PASS [exact read-back]`; `READBACK_PASS` mới là terminal delivery. `PROMOTED` là terminal khi artifact không cần external delivery; `REJECTED`, `INVALIDATED` là terminal khi có authority/evidence. Cấm `WRITTEN_UNVERIFIED -> PROMOTED`, hoặc coi acknowledgement là `READBACK_PASS`.

### 4.4 Handoff

`DRAFT -> SEALED [all required fields, digests] -> OFFERED [recipient] -> VALIDATING [recipient validation] -> ACCEPTED [acceptance record] | REJECTED [rejection issues]`. `ACCEPTED` và `REJECTED` là terminal. Custody chỉ chuyển tại `ACCEPTED`. Cấm sửa envelope đã `SEALED`; thay đổi tạo envelope mới và liên kết `supersedes`.

### 4.5 Approval

`REQUESTED -> VALIDATING [authority/scope check] -> APPROVED [human signature] | REJECTED [reason] | EXPIRED [clock]`; `APPROVED -> EXPIRED [clock] | REVOKED [authorized revocation evidence]`. `REJECTED`, `EXPIRED`, `REVOKED` là terminal; `APPROVED` chỉ còn hiệu lực đến khi bị thu hồi hoặc hết hạn. Cấm runtime/reviewer tạo `APPROVED`, và cấm dùng approval hết hạn/khác target.

### 4.6 External write

`NOT_REQUESTED -> PLANNED [exact target, stable identity, bounded action] -> AUTHORIZED [valid approval] -> EXECUTING [active lease, baseline và preflight] -> WRITTEN_UNVERIFIED [write receipt] -> READBACK_PASS [exact comparison]`. `NOT_REQUESTED -> CANCELLED [authorized cancellation]`; `PLANNED|AUTHORIZED -> CANCELLED [authorized cancellation]`. Nhánh lỗi: `EXECUTING|WRITTEN_UNVERIFIED -> PARTIAL_WRITE [observed delta] -> RECOVERY_REQUIRED [approved bounded recovery plan] -> READBACK_PASS|VERIFY_FAILED [exact comparison]`. `READBACK_PASS`, `VERIFY_FAILED` và `CANCELLED` là terminal; `NOT_REQUESTED` chỉ là terminal khi không có external mutation trong milestone. Cấm `AUTHORIZED -> READBACK_PASS`, `PARTIAL_WRITE -> EXECUTING` không có recovery plan, và retry mở rộng target/scope.

### 4.7 Milestone và package hai run

Milestone: `NOT_READY -> READY [dependencies, inputs, scope và owner] -> RUNNING [active lease, run manifest] -> VERIFYING [all outputs và review evidence] -> DONE [mọi Done gate, approval và read-back bắt buộc]`. `NOT_READY|READY|RUNNING|VERIFYING -> BLOCKED [blocker record]`; `NOT_READY|READY -> CANCELLED [authorized cancellation]`; mọi trạng thái chưa terminal `-> SUPERSEDED [replacement ID, authority]`; `BLOCKED ->` trạng thái trước chỉ khi blocker được đóng với evidence. `DONE`, `CANCELLED`, `SUPERSEDED` là terminal. Cấm `READY -> DONE`, `BLOCKED -> DONE`, và `DONE` khi external requirement còn `WRITTEN_UNVERIFIED` hoặc approval bắt buộc thiếu/hết hạn.

Package: `RUN1_READY -> RUN1_AUTHORING [Run 1 lease+scope] -> RUN1_RECONCILING [Run 1 manifest, outputs, issues] -> RUN1_PASS [local verification và issue disposition] -> RUN2_BLIND_AUDIT [sealed Run 1 handoff, fresh-context attestation] -> RUN2_FINALIZING [audit manifest, blocking issues closed] -> PACKAGE_PASS [all package gates]`. Mismatch material đi `RESET_TO_RUN1 [material-change record] -> RUN1_READY`. `PACKAGE_PASS` là terminal; `RESET_TO_RUN1` chỉ là trạng thái chuyển tiếp. Cấm `RUN1_PASS -> RUN2_FINALIZING`, `RUN2_BLIND_AUDIT -> PACKAGE_PASS`, `PACKAGE_PASS ->` trạng thái khác, và dùng “RUN3” như continuation. Bất cứ thay đổi material nào sau Run 2 phải reset Run 1 với `<NEW_RUN_ID>`; thay đổi không material chỉ được ghi trong closeout nếu policy cho phép.

## 5. Lease, checkpoint và concurrency

### 5.0 🔒 Lock/Lease Ledger (mẫu Markdown sống)

Ledger này là adapter Markdown có thể sao chép trực tiếp vào `<WORK_LEDGER>`; nó bổ sung chứ không thay `LeaseRecord` JSON-compatible ở 3.1. Mỗi hàng `REQUESTED|ACTIVE|CHECKPOINTED` phải tương ứng chính xác với `LeaseRecord` cùng `Lease ID`; với một scope ghi, chỉ được có một hàng `ACTIVE|CHECKPOINTED`. `Released` và checkpoint được giữ dưới dạng prose có timestamp để bảo toàn custody; hàng trống chỉ là idle template, không phải lease.

```md
## 🔒 Lock/Lease Ledger

> Một scope ghi chỉ có một hàng `ACTIVE|CHECKPOINTED`; `CHECKPOINTED` vẫn giữ custody và không mở quyền cho writer khác. Read-only có thể song song. Handoff bắt buộc: dừng ghi → checkpoint → release lease cũ → acceptance → acquire lease mới.

| Lease ID | Agent/runtime | File set or logical write scope | Started (timezone) | Purpose | Status | Expires |
|---|---|---|---|---|---|---|
| L-042 | author-01 / AUTHORING_RUNTIME | `artifact:A-GUIDE-01`; exclude `external:*` | 2026-01-01T09:00:00+07:00 (ICT) | Re-author phần hướng dẫn theo scope M-GUIDE-01 | ACTIVE | 2026-01-01T10:00:00+07:00 |

_Checkpoint CP-042 — 2026-01-01T09:30:00+07:00 (ICT): `L-042 ACTIVE -> CHECKPOINTED -> ACTIVE`; scope/holder không đổi, lease chưa hết hạn; `A-GUIDE-01 sha256:...`; checks `C-01=PASS`; open `I-09`; blocker `NONE`; next safe action: seal H-042._

_Released L-041 — 2026-01-01T08:55:00+07:00 (ICT): holder `control-01`; reason: handoff H-041 offered; digest `sha256:...`; open issues `I-08`; next safe action: recipient validates H-041._

<!-- Idle template: copy one row only after conflict check PASS -->
| <LEASE_ID> | <ACTOR_ID> / <RUNTIME_ROLE> | `<EXACT_FILE_SET_OR_LOGICAL_WRITE_SCOPE>` | <ISO-8601 timestamp + timezone> | <bounded purpose> | REQUESTED\|ACTIVE\|CHECKPOINTED\|RELEASED\|EXPIRED\|ABANDONED | <ISO-8601 timestamp + timezone> |
```

Acquisition: holder **MUST** append `REQUESTED`, normalize scope, inspect every non-terminal row, record conflict-check evidence, then atomically change only its row to `ACTIVE` when no overlap exists. Update: holder **MUST** add a checkpoint prose row before material change, handoff, external action, or expiry; the row transitions `ACTIVE -> CHECKPOINTED`, and may return to `ACTIVE` only when scope/holder are unchanged and lease is unexpired. A renewal is a new checked acquisition with a new `Lease ID`, never a silent edit of `Expires`. Release: holder **MUST** stop writing, add a release prose row containing checkpoints/digests/open issues/next safe action, then set the active or checkpointed row `RELEASED`. Custodian alone may mark `EXPIRED` or `ABANDONED` with clock/interruption evidence; recovery requires the 5.2 procedure and a new row.

| Tình huống quan sát | Quyết định overlap | Hành động bắt buộc |
|---|---|---|
| `ACTIVE` trên cùng file/object hoặc scope cha-con giao nhau | Cấm | Không ghi; mở conflict issue hoặc chờ release/handoff |
| Hai scope tách rời, exclusions rõ và conflict check PASS | Cho phép song song | Mỗi writer giữ Lease ID/hàng/checkpoint riêng |
| Một scope dùng wildcard/mô tả mơ hồ | Coi là overlap | Chuẩn hóa thành object list rồi kiểm tra lại |
| Hàng `EXPIRED`/`ABANDONED` nhưng checkpoint chưa đối chiếu | Chưa được ghi | Recovery record, verify digest, acquisition mới |
| Một bên read-only đúng scope, một bên write `ACTIVE` | Cho phép đọc | Reader MUST NOT sửa, giữ kết quả như evidence không phải lock |

### 5.1 Acquisition

Holder **MUST** (a) chuẩn hóa scope, (b) kiểm tra toàn bộ lease `REQUESTED|ACTIVE|CHECKPOINTED`, (c) từ chối nếu giao nhau, (d) tạo `LeaseRecord` nguyên tử, (e) ghi thời điểm hết hạn. Không có phản hồi từ adapter không phải là quyền ghi. `ACTIVE` chỉ được cấp sau kiểm tra thành công được lưu làm evidence.

Lease **MUST** có TTL hữu hạn theo policy. Holder **SHOULD** checkpoint trước nửa TTL, trước thay đổi material, trước bàn giao và trước bất kỳ thao tác bên ngoài nào. Renewal là acquisition được kiểm tra lại; không được gia hạn mù. Release phải ghi công việc đã làm, digest hiện tại, issues mở và next safe action.

### 5.2 Checkpoint và lease bỏ quên

Checkpoint **MUST** chứa scope, artifacts/digests, trạng thái, kiểm tra đã chạy, lỗi, blockers, approval/gate còn thiếu, và next safe action. Khi TTL hết, Custodian đánh dấu `EXPIRED`; sau ngưỡng `abandon_after`, hoặc có bằng chứng runtime bị gián đoạn, đánh dấu `ABANDONED`. Người phục hồi **MUST** đọc checkpoint, đối chiếu digest, ghi `RecoveryRecord`, rồi xin lease mới. Không được xóa, ghi đè hay coi output của lease bỏ quên là đáng tin mà không đối chiếu.

### 5.3 Quy tắc đồng thời

Read-only có thể song song. Hai write chỉ song song nếu scopes không giao nhau theo danh sách đối tượng chuẩn hóa. Một writer được đọc scope khác nhưng **MUST NOT** suy ra quyền ghi. Chồng lấn, scope mơ hồ, lock adapter lỗi, hoặc digest thay đổi bất ngờ là hard stop cho phần giao nhau.

## 6. Bàn giao custody

Người gửi phải: dừng ghi; checkpoint; seal envelope; release lease cũ; offer recipient. Recipient phải: kiểm tra schema, authority, scope, digest, issue/gate, lease đã release và khả năng nhận. Recipient chỉ acquire lease sau `ACCEPTED`. `REJECTED` không chuyển custody và **MUST** chỉ ra ID issue có thể hành động.

### 6.1 Mẫu Markdown

```md
# Handoff <HANDOFF_ID>
- from / to: <ACTOR_ID> / <ACTOR_ID>
- work, milestone, run: <WORK_ID> / <MILESTONE_ID> / <RUN_ID>
- custody scope: <EXACT_SCOPE>
- status: SEALED | OFFERED | VALIDATING | ACCEPTED | REJECTED
- provenance: <AUTHORITY_REFS>; input digests: <ID=digest>
- outputs: <ARTIFACT_ID, location-adapter-ref, digest, status>
- checks and verdicts: <CHECK_ID, result, evidence>
- open issues/blockers: <ISSUE_ID...>
- human gates: <APPROVAL_ID or MISSING>
- allowed next actions: <bounded list>
- forbidden actions: <bounded list>
- recipient acceptance criteria: <list>
- acceptance: <ACCEPTED_BY, timestamp, evidence | MISSING>
- rejection: <REJECTION_ISSUE_IDS | NONE>
- custody transfer: only on ACCEPTED; <new custodian or NONE>
- next safe action: <action>
```

### 6.2 Envelope JSON-compatible

```json
{
  "schema_version": "1.0", "id": "H-042", "status": "OFFERED",
  "from_actor": "author-01", "to_actor": "control-01",
  "work_id": "W-017", "milestone_id": "M-03", "run_id": "R1-017",
  "scope": {"write_objects": ["artifact:A-17"], "excluded": ["external:*"]},
  "provenance": [{"ref": "AUTH-02", "digest": "sha256:..."}],
  "artifacts": [{"id": "A-17", "ref": "logical://artifact/A-17", "digest": "sha256:...", "status": "LOCALLY_VERIFIED"}],
  "checks": [{"id":"C-1","verdict":"PASS","evidence":"LOG-01"}],
  "issues_open": ["I-09"], "human_gates": ["MISSING"], "approval_refs": [],
  "allowed_actions": ["independent audit"], "forbidden_actions": ["external mutation"],
  "acceptance_criteria": ["digest matches", "issue ledger parsed"],
  "custody_transfer": {"transfers_only_on":"ACCEPTED","accepted_by":null,"accepted_at":null},
  "rejection": null, "created_at": "2026-01-01T00:00:00Z", "updated_at":"2026-01-01T00:02:00Z",
  "sealed_at": "2026-01-01T00:02:00Z", "actor_id":"author-01", "evidence_refs": ["CP-88"]
}
```

## 7. Mốc, review, issue và quyết định

Mỗi milestone **MUST** chứa: ID, mục tiêu, owner, dependencies, inputs cùng digest/status allowed-use, work scope, outputs, reviewers, phương pháp verification, tier approval, status, blockers, Done gates, và external requirement. Done gate là mệnh đề AND rõ ràng; “đã cố gắng” không phải evidence.

```json
{
  "schema_version":"1.0", "id":"M-03", "status":"READY", "actor_id":"author-01", "owner":"author-01",
  "goal":"Tạo hướng dẫn trung lập", "dependencies":["M-02"],
  "inputs":[{"id":"SRC-01","digest":"sha256:...","allowed_use":"INTERNAL"}],
  "scope":{"include":["artifact:A-17"],"exclude":["external:*"]},
  "outputs":["A-17"], "reviewers":["control-01"],
  "verification":["schema-check","digest-check"], "approval_tier":"NONE",
  "blockers":[], "done_gates":["A-17=LOCALLY_VERIFIED","all issues resolved or accepted"],
  "created_at":"2026-01-01T00:00:00Z", "updated_at":"2026-01-01T00:00:00Z", "evidence_refs":["PLAN-03"]
}
```

`IssueRecord` phải có severity, phát hiện, phạm vi, evidence, owner, trạng thái (`OPEN|MITIGATED|RESOLVED|ACCEPTED_RISK`), tiêu chí đóng, và liên kết run. `DecisionRecord` phải có alternatives, authority, rationale, effect, expiry/review date. Không được đóng issue bằng lời khẳng định không evidence.

## 8. Run 1 và Run 2

**Run 1 — build/reconciliation.** `AUTHORING_RUNTIME` tạo đúng scope dưới lease, ghi manifest đầu vào/đầu ra/digest. `CONTROL_RUNTIME` đối soát authority, scope, schema, evidence, issues và không phê duyệt thay người. Run 1 pass khi outputs xác minh cục bộ và mọi sai lệch được giải quyết hoặc được risk acceptance hợp lệ.

**Run 2 — fresh-context audit/finalization.** Auditor **MUST** bắt đầu với context tối thiểu độc lập: authority hiện hành, scope, sealed Run 1 manifest, artifacts/digests, rubric và issue ledger; **MUST NOT** nhận tóm tắt đánh giá như bằng chứng duy nhất. Auditor tái kiểm digest, truy xuất đầu vào, kiểm transitions/gates, tìm vấn đề mới và lập audit manifest. Finalizer chỉ được hoàn tất sau audit pass và các issues blocking đã đóng.

Reset Run 1 khi input/authority/digest/scope/target/approval/rubric thay đổi material, audit phát hiện lỗi material, hoặc custody không chứng minh được. Policy **MUST** định nghĩa “material”; khi nghi ngờ coi là material. Không được sửa lặng lẽ sau Run 2 để gọi là finalization.

## 9. Phê duyệt và mutation bên ngoài

Tier tối thiểu: `NONE` (không cần người), `HUMAN_REVIEW`, `HUMAN_APPROVAL`, và các tier domain tùy biến (`LEGAL`, `SAFETY`, `PRIVACY`, `FINANCIAL`, `PUBLICATION`, `PRODUCTION`). Chỉ người được ủy quyền đúng tier mới ký. Một `ApprovalRecord` phải nêu target/action/scope, risk, artifact digest, điều kiện, thời hạn, signatory, authority ref và trạng thái.

```json
{
 "schema_version":"1.0", "id":"AP-12", "status":"APPROVED", "actor_id":"human-07", "tier":"HUMAN_APPROVAL",
 "signatory":"human-07", "authority_ref":"ROLE-MAP-2", "scope":"target:T-8/object:O-5", "risk":"bounded publication",
 "artifact_digest":"sha256:...", "allowed_action":"upsert exactly one record",
 "conditions":["read-back exact"], "expires_at":"2026-02-01T00:00:00Z", "created_at":"2026-01-01T00:00:00Z",
 "updated_at":"2026-01-01T00:00:00Z", "evidence_refs":["SIG-12"]
}
```

Trước write, executor **MUST** xác nhận target định danh chính xác, schema/identity, action/delta/giới hạn, approval còn hạn, lease, baseline read, và rollback/recovery plan. Sau write, phải read-back chính xác các trường identity, giá trị yêu cầu, số lượng, digest/phiên bản nếu có. Acknowledgement, HTTP success, hoặc receipt không phải verification.

```json
{
 "schema_version":"1.0", "id":"EW-31", "status":"READBACK_PASS", "actor_id":"control-01", "target":"target:T-8/object:O-5",
 "stable_identity":{"key":"record_id","value":"REC-14"}, "action":"upsert", "bounds":{"max_records":1,"fields":["title","state"]},
 "approval_ref":"AP-12", "preflight_digest":"sha256:...", "write_receipt":"receipt:...",
 "expected":{"title":"Hướng dẫn A","state":"active"}, "readback":{"title":"Hướng dẫn A","state":"active"},
 "verified_at":"2026-01-01T00:30:00Z", "created_at":"2026-01-01T00:20:00Z", "updated_at":"2026-01-01T00:30:00Z", "evidence_refs":["RB-31"]
}
```

Partial write, timeout sau gửi, hoặc read-back mismatch phải vào `PARTIAL_WRITE`/`VERIFY_FAILED`; giữ receipt và baseline, chặn promotion, thực hiện recovery plan trong bounds đã phê duyệt hoặc xin phê duyệt mới. Không retry “rộng hơn”, tạo bản sao lách giới hạn, hay xóa dữ liệu để che lỗi.

## 10. Manifest và bằng chứng

`RunManifest` liên kết toàn bộ custody: authority refs/digests, runtime/role, inputs, outputs, leases, handoffs, checks, issue/decision/approval IDs, external writes, timestamps và verdict. Digest **MUST** công bố thuật toán và canonicalization; không so sánh digest của hai dạng không cùng quy tắc.

```json
{
 "schema_version":"1.0", "id":"RM-R2-017", "run_id":"R2-017", "kind":"RUN2_AUDIT", "status":"PASS",
 "actor_id":"control-02", "fresh_context_attestation":true,
 "authority":[{"ref":"AUTH-02","digest":"sha256:..."}],
 "inputs":[{"id":"A-17","digest":"sha256:..."}], "outputs":["AUD-17"],
 "leases":["L-21"], "handoffs":["H-042"], "checks":[{"id":"C-1","verdict":"PASS","evidence":"LOG-1"}],
 "issues":{"opened":["I-10"],"resolved":["I-09"]}, "approvals":[], "external_writes":[],
 "started_at":"2026-01-01T00:10:00Z", "ended_at":"2026-01-01T00:40:00Z", "created_at":"2026-01-01T00:10:00Z",
 "updated_at":"2026-01-01T00:40:00Z", "evidence_refs":["AUD-17"]
}
```

Mọi JSON mẫu dùng giá trị hợp lệ; `<PLACEHOLDER>` nếu dùng trong mẫu phải được thay trước parse. Adapter có thể dùng YAML, bảng hay cơ sở dữ liệu, nhưng phải bảo toàn tất cả trường bắt buộc, history và khả năng truy xuất evidence.

## 11. Luồng bắt buộc end-to-end

```text
Intake -> resolve authority -> define stable IDs/scope -> plan milestone
 -> acquire lease -> Run 1 author -> reconcile/review -> Run 1 pass
 -> sealed handoff -> fresh Run 2 audit -> finalize -> approvals
 -> bounded external write (if required) -> exact read-back -> closeout
```

Ở mỗi mũi tên, thiếu evidence thì dừng tại trạng thái trước. Closeout **MUST** xác nhận Done gates, terminal states, issue disposition, digest/manifest, custody release, và next owner/retention theo policy.

## 12. Xử lý lỗi và hard stop

| Tình huống | Hành động bắt buộc |
|---|---|
| Authority xung đột/thiếu | `BLOCKED_AUTHORITY`; ghi nguồn và câu hỏi cần quyết |
| Scope drift | dừng write; lập issue; quyết định scope mới; xin lease mới nếu cần |
| Digest drift | invalidated artifact/run; xác định delta; reset Run 1 nếu material |
| Context stale | refresh từ authority + manifest sealed; không dựa vào memory tường thuật |
| Handoff gián đoạn | không transfer custody; giữ `OFFERED` hoặc `REJECTED`; renew/recover lease theo evidence |
| Lease hết/bỏ quên | Custodian thực hiện 5.2; không ghi chồng |
| Partial external write | `PARTIAL_WRITE`; read-back, recovery bounded, approval mới nếu vượt kế hoạch |
| Lỗi lặp lại | sau hai thất bại cùng loại/cùng bound, dừng; ghi error, owner, unblock condition, next safe action |

Không được làm yếu target, tăng quyền, mở rộng phạm vi, bỏ kiểm tra, hoặc bịa evidence để vượt stop condition.

## 13. Adapter và tùy biến

Quy trình adoption:

1. Chỉ định authority map và người có quyền từng approval tier.
2. Đặt `<CONTROL_ROOT>`, adapter atomic ledger, retention và timezone/timestamp chuẩn.
3. Đổi tên role/runtime, nhưng giữ accountabilities và separation of duties.
4. Định nghĩa stable-ID namespace, canonicalization/digest và scope grammar.
5. Chọn status bổ sung, TTL, stale threshold, material-change rubric và Done gates.
6. Ánh xạ storage, review, automation, version history và external system vào record logic; ghi mapping trong policy.
7. Chạy conformance check trước công việc thật; sửa adapter, không nới invariant.

Ví dụ adapter chỉ minh họa: ledger có thể là tệp, bảng, cơ sở dữ liệu hoặc dịch vụ; history có thể là snapshot hoặc hệ version; external target có thể là bất kỳ hệ thống được phê duyệt. Không adapter nào được giả định bắt buộc.

## 14. Conformance checklist

Một triển khai chỉ được tự tuyên bố `CONFORMANT` khi tất cả đúng:

- [ ] Có authority precedence, policy công bố và toàn bộ bất biến 1.2.
- [ ] Roles, scope grammar, stable IDs và ledger atomic quan sát được.
- [ ] Capability preflight xác nhận primary/verifier cho từng task class; semantic audit và structural audit có verdict/evidence tách biệt; role swap (nếu có) có `DecisionRecord` và không phá separation of duties.
- [ ] Bảy state machines và luồng package hai run có states, transition, evidence, terminal và transition cấm như mục 4.
- [ ] Lease có conflict check, TTL, checkpoint, release và abandoned recovery; `<WORK_LEDGER>` có section `🔒 Lock/Lease Ledger`, một hàng `ACTIVE`, prose checkpoint/release, và idle template đủ cột Lease ID, Agent/runtime, File set or logical write scope, Started (timezone), Purpose, Status, Expires.
- [ ] Handoff có Markdown/envelope, digest, issue/gate, acceptance/rejection và custody rule.
- [ ] Milestone, issue, decision, approval, external write và manifest giữ đủ trường bắt buộc.
- [ ] Run 1/Run 2 có fresh-context attestation, reset material và cấm Run 3; re-authoring thực chất sau audit reset Run 1, còn mechanical evidence-preserving repair có proof preservation.
- [ ] Không AI/reviewer tự cấp human/domain approval.
- [ ] External mutation có exact target, bound, approval, preflight và exact read-back.
- [ ] Failure/repeated-failure, drift và partial-write recovery đã được thử bằng tình huống mô phỏng.
- [ ] Thay đổi adapter không làm mất evidence, history, ID hay gates.

Kiểm tra tối thiểu: parse mọi envelope machine-readable; kiểm scope overlap bằng hai request cạnh tranh và bằng hàng `ACTIVE` trong Ledger Markdown; cố chuyển trạng thái cấm và mong đợi từ chối; cố handoff sai digest và mong đợi reject; mô phỏng một semantic finding mà structural audit không phát hiện, và ngược lại; mô phỏng mechanical repair có proof preservation; mô phỏng re-authoring material sau audit và mong đợi `RESET_TO_RUN1`; mô phỏng read-back mismatch; thay đổi input material sau Run 2 và mong đợi `RESET_TO_RUN1`.

## 15. Anti-patterns (không phù hợp)

| Sai | Vì sao sai | Thay thế |
|---|---|---|
| “Hai runtime cùng sửa vì tin nhau” | phá single writer | scope tách rời hoặc tuần tự handoff |
| “Review PASS nên coi như approved” | review không phải human authority | yêu cầu `ApprovalRecord` đúng tier |
| “Gửi thành công là hoàn tất” | không chứng minh trạng thái đích | exact read-back |
| “Sửa nhẹ sau audit rồi gọi là Run 3” | che correlated failure | đánh giá material, reset Run 1 nếu cần |
| “Lease hết thì người khác tự ghi” | phá custody | abandoned recovery và acquisition mới |
| “Thiếu authority thì chọn nguồn mới hơn” | không có precedence hợp lệ | `BLOCKED_AUTHORITY` |
| “Lỗi hai lần thì tăng quyền/rộng target” | vượt boundary | dừng và xin unblock có thẩm quyền |

## 16. Ví dụ hoàn chỉnh, trung lập

Nhóm cần phát hành một hướng dẫn nội bộ `A-GUIDE-01` vào một kho tài liệu đã xác định `T-DOC-01`.

1. Intake tạo `W-GUIDE-01`, authority `AUTH-01`, milestone `M-GUIDE-01`. Scope chỉ gồm `artifact:A-GUIDE-01`; external target bị loại trừ. Done gate: input digest khớp, review pass, human publication approval, read-back chính xác.
2. Policy map `AUTHORING_RUNTIME=Claude` và `CONTROL_RUNTIME=Codex` chỉ là nhãn thay thế. Capability preflight `PF-01` xác nhận `author-01` làm re-authoring, `control-01` làm structural audit, và `control-02` làm semantic audit fresh-context; nếu `control-02` không đủ năng lực semantic thì milestone sẽ là `BLOCKED_CAPABILITY`, không hạ chuẩn xuống structural-only. `author-01` yêu cầu `L-01`; trong `🔒 Lock/Lease Ledger`, một hàng `ACTIVE` ghi `L-01`, exact scope, ICT timestamp, purpose và expiry; ledger không có overlap nên lease hợp lệ. Nó tạo artifact từ `SRC-01 sha256:x`, checkpoint `CP-01`, rồi Run 1 manifest `RM-R1-01`.
3. `control-01` đối soát structural scope, digest, schema và rubric evidence; `control-02` đối soát semantic và mở `I-01` vì thiếu mục tiêu retention. `author-01` thực hiện re-authoring thực chất theo quyết định `D-01`, checkpoint digest mới và chuyển lại Run 1; control chỉ sửa cơ học một liên kết manifest với proof rằng meaning không đổi. Sau semantic re-check, `control-02` đóng `I-01` bằng evidence. Run 1 thành `RUN1_PASS`.
4. `author-01` seal `H-01`, release `L-01`, offer custody. `control-02` (auditor fresh context) kiểm schema/digest/issue, accept `H-01`, acquire `L-02`, attests `fresh_context_attestation=true`, phát hiện không có lỗi material và xuất `RM-R2-01 PASS`. Package `PACKAGE_PASS`.
5. Người có authority xuất bản ký `AP-01`, nêu đúng `T-DOC-01`, một object, artifact digest, hạn dùng và điều kiện read-back. Executor preflight target/identity/bounds; ghi đúng một object. Receipt tạo `EW-01 WRITTEN_UNVERIFIED`.
6. Control đọc lại object có `record_id=GUIDE-01`, tiêu đề và digest đúng expected; `EW-01 -> READBACK_PASS`. Mốc đạt `DONE`, issues không còn blocking, manifest/checkpoint lưu, `L-02` release. Nếu title khác expected ở bước 6, không được đánh dấu Done: phải `PARTIAL_WRITE`/`VERIFY_FAILED`, giữ receipt và thực hiện recovery được bound/phê duyệt.

## 17. Change control

Thay đổi hợp đồng **MUST** có đề xuất ID, lý do, impact lên invariants/schema/state/adapters, compatibility/migration plan, reviewer và human approval phù hợp. Thay đổi breaking tăng major version; thêm trường tùy chọn hoặc làm rõ không breaking tăng minor/patch theo policy. Bản record cũ phải còn đọc được hoặc có migration evidence. Không thay đổi hồi tố để biến một hành động trước đó thành hợp lệ.

Kết thúc hợp đồng.
