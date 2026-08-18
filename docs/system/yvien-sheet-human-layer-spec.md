# Y Viện — Sheet human-layer specification

- **ID:** `YV-HUMAN-LAYER-001`
- **Version:** 1.0.0
- **State:** `DRAFT_UNSIGNED · LOCAL_ONLY`
- **Schema this spec defines:** `YV-SHEET-001/1.0.0`
- **Supersedes (as display model only):** `TL-SHEET-001/0.2.0` — 24 dataset `TL_*`, phân loại
  `TECHNICAL_READBACK_PASS · BUSINESS_MODEL_FAILED` trong
  `docs/system/toplink-google-sheets-operational-contract.md`.
- **Target:** `1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms`
- **Người viết lớp người:** Claude (Phase 1, `external_writes=0`).
  **Người ghi Sheet:** Codex (Phase 2, chỉ sau ba approval ký tay).
- **Voice binding:** `docs/system/yvien-brand-voice-pack.md` (`YV-VOICE-001` v0.1.0, `APPROVED` 2026-08-05).

---

## Vấn đề bản đặc tả này giải

Workbook cũ đúng về dữ liệu và sai về mô hình. Mỗi tab mở ra là 11 cột provenance máy
(`stable_row_key … updated_at_ict`) đứng trước nội dung; người mở sheet không đọc được kế hoạch,
chỉ đọc được payload. Read-back 14/14 PASS mà mô hình vận hành vẫn hỏng.

Bản này tách workbook làm ba lớp:

| Lớp | Ai đọc | Ở đâu |
|---|---|---|
| **Mặt trước** — nội dung và quyết định | người | 21 tab, cột tiếng Việt, thứ tự đọc của người |
| **Mặt sau** — provenance đầy đủ | máy / audit | JSON sidecar trong `staging/`, + 2 cột ẩn `_key`/`_audit` trong chính tab |
| **Cầu nối** — tái tạo xác định | pipeline | generator thuần → `report-plan.json` → apply → exact read-back (value + format) |

---

# SPEC-A — Schema 21 tab

## Quy ước chung

- Tên tab hệ thống: `NN_UPPER_SNAKE`. Tên tab nội dung: `YV_NN_slug_thường`.
- Tab mặc định `Trang tính1` (`sheetId = 0`) **giữ nguyên**, không đọc ghi. Không tab nào có hậu tố `_v2`.
- Header **tiếng Việt**, hàng 1, `frozenRowCount = 1`, `basicFilter` bật.
- Hai cột cuối mọi tab: `_key`, `_audit`, `hiddenByUser = true`.
  - `_key` = stable identity (bằng `stable_row_key` của dataset tương ứng).
  - `_audit` = chuỗi nối bằng ` · `:
    `record_id · source_path#source_location · source_id · evidence_status · allowed_use · revision · source_digest · owner · updated_at_ict`.
- 11 cột common **không bao giờ** xuất hiện ở mặt trước. Bản đầy đủ nằm trong JSON sidecar.
- `wrapStrategy = WRAP`, `verticalAlignment = TOP` cho toàn vùng dữ liệu. Không merge cell trong vùng dữ liệu.
- Hàng 2 của mỗi tab là **legend vàng** (một hàng, ô A2 merge-free, nền `#f6f4df`):
  `Ô nền vàng = còn một việc của người thật chưa làm. Nội dung ô bắt đầu bằng "CHƯA CHỐT — ".`
  Dữ liệu bắt đầu từ hàng 3. `frozenRowCount = 2`.
- Nhãn ngày là **tương đối**: `D-1` … `D-28` (không pad). Không ngày tuyệt đối
  (`TOPLINK_CONTENT_START_DATE = UNSET`, gate `TL-M6` / `TL-GAP-006`).
- Cột `Chu kỳ` giá trị `C1`, `C2`, … (mặc định `C1`).

## Whitelist ID được phép hiển thị ở mặt trước

Tab nội dung (`report`, `00_Y_VIEN_CAN_CHOT`, `YV_01`…`YV_12`) **cấm** mọi ID kỹ thuật.
Ngoại lệ duy nhất, vì ngắn và người thật dùng để đối chiếu:

```
D-1 … D-28        nhãn ngày tương đối
C1, C2, …         mã chu kỳ
CL-*              mã câu claim, phải resolve về 06_COMPLIANCE_RULES
A / B / C         mã hướng option
```

Cấm tuyệt đối ở mặt trước tab nội dung: `TL-*`, `YV-*`, chuỗi hex ≥ 16 ký tự, `sha256`, `revision`,
`record_id`, `stable_row_key`, `source_digest`.

Ba tab được **miễn trừ** vì bản chất là tab audit cho người soát: `01_SOURCE_INVENTORY`,
`03_OUTPUT_INDEX`, và cột `Mã` của `00_CONTROL`. Miễn trừ này phải khai trong registry
(`id_exposure: AUDIT_TAB`), không phải mặc định.

---

## A.0 `report` — index 0

Không phải một bảng phẳng. Ba bảng xếp dọc, mỗi bảng có một hàng tiêu đề mục
(nền `#f6f4df`, chữ `#95131f`, merge-free — dùng một ô A và pad phần còn lại bằng chuỗi rỗng).

### Bảng A — Nền tảng chiến lược

| # | Cột |
|---|---|
| 1 | Hạng mục |
| 2 | Cách hiểu đơn giản |
| 3 | Ý nghĩa với campaign / content |
| 4 | Điều đã chốt |
| 5 | Cần chốt / review |
| 6 | Người cần can thiệp |

Nguồn: tổng hợp từ `YV_01`…`YV_08` + `05_KPI_DICTIONARY` + `06_COMPLIANCE_RULES`.
Cột 2 là **bắt buộc dịch sang lời đời thường** — không lặp lại nguyên văn cột 1.

### Bảng B — 28 ngày × 3 hướng (84 dòng)

| # | Cột |
|---|---|
| 1 | Ngày |
| 2 | Hướng |
| 3 | Trụ nội dung |
| 4 | Định dạng |
| 5 | Nói gì |
| 6 | Vì sao chọn / đánh đổi |
| 7 | Kêu gọi |
| 8 | Ai duyệt |
| 9 | Trạng thái |

Hướng `A` = khuyến nghị. `B`, `C` = dự phòng, ô cột 6 mở đầu `DỰ PHÒNG — `, **không tô vàng**.

### Bảng C — Ghép luồng vận hành

| # | Cột |
|---|---|
| 1 | Bước |
| 2 | Việc cần làm |
| 3 | Đầu vào từ tab |
| 4 | Kết quả ra |
| 5 | Ai làm |
| 6 | Chặn bởi |

`report` là **lớp đọc**. Không dòng nào của `report` là nguồn sự thật; mọi ô truy về tab gốc qua `_key`.

## A.1 `00_Y_VIEN_CAN_CHOT` ← `TL_OWNER_ACTIONS`

| # | Cột | Ghi chú |
|---|---|---|
| 1 | STT | số thứ tự thuần (1, 2, 3…), **không** phải `action_id` |
| 2 | Mức ưu tiên | `CHẶN NGAY` / `CAO` / `TRUNG BÌNH` |
| 3 | Nhóm việc | |
| 4 | Cần chốt điều gì | ô vàng, mở đầu `CHƯA CHỐT — ` |
| 5 | Vì sao đang chặn | |
| 6 | Chặn cái gì | tab / milestone bị chặn |
| 7 | Ai quyết | vai trò người thật |
| 8 | Hạn / cổng | |
| 9 | Trạng thái | `decision_status` |
| 10 | Ngày quyết | |
| 11 | Nội dung quyết | |
| 12 | Ghi chú | |

**Luật đối xứng:** mỗi ô vàng ở bất kỳ tab nào phải có **đúng một** dòng ở đây, và ngược lại.
Validator kiểm hai chiều; lệch = `VALIDATION_FAILED`.

## A.2 `00_CONTROL` ← `TL_CONTROL` + `TL_RUNTIME_COMPATIBILITY`

| # | Cột |
|---|---|
| 1 | Nhóm (`Kiểm soát` / `Runtime`) |
| 2 | Mã |
| 3 | Mục |
| 4 | Giá trị hiện tại |
| 5 | Trạng thái |
| 6 | Nghĩa là gì |
| 7 | Vai trò giữ |

`external_writes` và `approval_bundle_id` là hai dòng `Kiểm soát` bình thường, không phải cột riêng.

## A.3 `01_SOURCE_INVENTORY` ← `TL_SOURCE_INVENTORY` *(audit tab)*

`Tệp nguồn · Nhóm · Mức nhạy cảm · Trạng thái · Lý do loại trừ · SHA-256`

## A.4 `02_INPUT_GAPS` ← `TL_INPUT_GAPS`

`Thiếu gì · Ai cấp được · Chặn milestone nào · Cách gỡ · Trạng thái`

## A.5 `03_OUTPUT_INDEX` ← `TL_OUTPUT_INDEX` *(audit tab)*

`Sản phẩm · Đường dẫn · Tab hiển thị · Trạng thái QA nội bộ · Trạng thái đưa lên Sheet · Trạng thái đọc lại · Digest`

Cột **Tab hiển thị** là cột mới. Mọi artifact phải trỏ tới ít nhất một tab `YV_*`/`NN_*`; orphan = fail.
Tab này là **mục lục**, tuyệt đối không chứa nội dung kế hoạch.

## A.6 `04_DECISIONS` ← `TL_DECISIONS`

`Chu kỳ · Ngày · Ai quyết · Quyết định gì · Phạm vi áp dụng · Căn cứ · Điều kiện xem lại · Trạng thái`

Nhận thêm hai loại dòng: **revision event** (mỗi lần ghi Sheet) và **chốt cuối chu kỳ**
(mở `C(n+1)`).

## A.7 `05_KPI_DICTIONARY` ← `TL_KPI_DICTIONARY`

`Chỉ số · Nghĩa là gì · Tính thế nào · Đo ở đâu · Ai theo dõi · Nhịp đo · Cỡ mẫu tối thiểu ·
Mốc xuất phát · Ngưỡng Tiếp tục · Ngưỡng Sửa · Ngưỡng Dừng · Cửa sổ đo · Trạng thái mẫu số`

Năm cột `Mốc xuất phát`, `Ngưỡng Tiếp tục/Sửa/Dừng`, `Cửa sổ đo` là **mới** — đây là thứ biến workbook
thành vòng học. Baseline hiện tại: follower Page `61591880797654` = 0; awareness = `NO_MEASUREMENT`.
Ngưỡng chưa có = ô vàng, không được bịa số.

## A.8 `06_COMPLIANCE_RULES` ← `TL_COMPLIANCE_RULES` + claim register `CL-*`

`Nhóm (Luật / Câu claim) · Mã · Mức rủi ro · Loại phát ngôn · Được nói gì · Cấm nói gì · Ai duyệt · Cổng người`

Claim register `CL-*` (10 dòng, hiện nằm rải trong `month-calendar.md`) gộp về đây. Đây là **nơi duy nhất**
`CL-*` được định nghĩa. `TL-R2-F02` (`CL-P2` orphan) đóng tại tab này hoặc hiện thành ô vàng.

## A.9 `YV_01_brand_profile` ← `TL_BRAND_PROFILE`

`Nhóm · Hạng mục · Nội dung · Mức bằng chứng · Được dùng ở đâu · Khoá / mở`

## A.10 `YV_02_audience` ← `TL_AUDIENCE_HYPOTHESES`

`Nhóm khách · Giả định về họ · Mức bằng chứng · Kiểm chứng bằng cách nào · Cửa sổ quan sát ·
Kết luận hiện tại · Vì sao tin vậy`

Cột 1 hiển thị **tên nhóm khách bằng tiếng Việt**, không phải `TL-A01`. Mã thật nằm ở `_key`.

## A.11 `YV_03_positioning` ← `TL_POSITIONING`

`Loại tuyên bố · Câu tuyên bố · Mức chứng minh · Ranh giới được nói · Đường kiểm chứng`

## A.12 `YV_04_narrative` ← `TL_NARRATIVE`

`Luật kể chuyện · Ranh giới · Ai giữ giọng · Cổng founder`

## A.13 `YV_05_content_pillars` ← `TL_CONTENT_PILLARS` — **đúng 5 dòng**

`Trụ nội dung · Tỷ trọng % · Giải quyết việc gì cho khách · Định dạng hay dùng · Vai trò trong phễu ·
Rủi ro / cổng · Vì sao có trụ này`

Tổng `Tỷ trọng %` phải bằng 100. Validator kiểm.

## A.14 `YV_06_page_strategy` ← `TL_FACEBOOK_STRATEGY` + `TL_PAGE_BENCHMARK`

`Nhóm (Chiến lược / Mốc đo) · Hạng mục · Kênh · Vai trò · Tỷ trọng % · Trụ liên quan ·
Giá trị đo · Mẫu số · Thời điểm đo · Trạng thái`

Dòng `Chiến lược` để trống 4 cột đo; dòng `Mốc đo` để trống `Tỷ trọng %` và `Trụ liên quan`.
Ô trống ghi `—`, không để rỗng thật (read-back cần chuỗi xác định).

## A.15 `YV_07_campaign` ← `TL_CAMPAIGN`

`Chu kỳ · Tuần · Ngày · Vai trò giai đoạn · Trụ nội dung · Việc cần giải cho khách · Cổng cứng · Kêu gọi mặc định`

## A.16 `YV_08_experiments` ← `TL_EXPERIMENTS`

`Chu kỳ · Thuộc giai đoạn · Giả thuyết · Biến thay đổi · Mức bằng chứng · Đo bằng cách nào ·
Cửa sổ quan sát · Dấu hiệu Tiếp tục · Dấu hiệu Sửa · Dấu hiệu Dừng · Kết luận · Chốt ở quyết định nào`

Cột cuối là khoá ngoại mới trỏ `04_DECISIONS` — đóng vòng chu kỳ.

## A.17 `YV_09_content_calendar` ← `TL_CONTENT_CALENDAR` — **đúng 84 dòng**

`Chu kỳ · Ngày · Hướng · Nhóm khách · Trụ nội dung · Định dạng · Vai trò phễu · Angle chính · Nói gì ·
Kêu gọi · Câu claim dùng · Thử nghiệm gắn kèm · Tuyến duyệt · Bản sửa · Trạng thái duyệt`

84 = 28 ngày × 3 hướng. Hướng `A` khuyến nghị; `B`/`C` dự phòng.
Cột `Angle chính` là góc chung của cả ngày; cột `Nói gì` là nội dung riêng của từng hướng A/B/C.

Sáu cột phải **có thật**, không suy diễn và không hardcode: `Nhóm khách` (#2) · `Thử nghiệm gắn kèm` (#3) ·
`Angle chính` + `Tuyến duyệt` (#4) · `Vai trò phễu` (#12) · `Bản sửa` (#13). Xem SPEC-B.

## A.18 `YV_10_production_briefs` ← `TL_PRODUCTION_BRIEFS` + `TL_REELS_BRIEFS`

`Chu kỳ · Ngày · Hướng · Loại brief (Bài / Reel) · Định dạng · Hook · Hình ảnh / shot · Chữ trên hình ·
Thời lượng · Tỷ lệ khung · Lời thoại · Phụ đề · Vùng an toàn · Kêu gọi · Câu claim dùng ·
Chỉ số theo dõi · Tiếp cận · Rủi ro / cổng · Trạng thái sản xuất`

Dòng `Bài` để `—` ở 5 cột riêng của reel. Dòng `Reel` để `—` ở `Chỉ số theo dõi` nếu chưa gắn.
Ngày nào chỉ có brief cho hướng `A`: hai dòng `B`/`C` vẫn tồn tại với
`Trạng thái sản xuất = CHƯA CÓ BRIEF` và ô mở đầu `DỰ PHÒNG — ` (defect #6).

## A.19 `YV_11_asset_batch_plan` ← `TL_ASSET_BATCH_PLAN`

`Chu kỳ · Mẻ sản xuất · Dùng cho ngày nào · Loại tài sản · Mô tả · Sức chứa mẻ · Quyền sử dụng ·
Đồng ý của người xuất hiện · Trạng thái`

## A.20 `YV_12_workflow_approval` ← `TL_WORKFLOW_APPROVAL`

`Chu kỳ · Ngày · Hướng · Người duyệt · Kết luận · Điều kiện kèm theo · Hết hạn (ICT) · Trạng thái đăng ·
Bản sửa · Sửa lớn có reset không · Tuyến duyệt · Mức rủi ro · DMP check · Trạng thái đồng ý ·
Giờ đăng · Tham chiếu đo · Ghi chú reset · Câu claim`

18 cột hiển thị — hợp nhất 10 cột registry cũ với 8 field ledger bị bỏ rơi trong
`workflow-approval-measurement.md:48-63` (defect #7).

---

# SPEC-B — Mapping và 11 lỗi mô hình

## B.1 Mapping 24 dataset → 21 tab

| Tab đích | Dataset nguồn |
|---|---|
| `report` | `TL_REPORT` |
| `00_Y_VIEN_CAN_CHOT` | `TL_OWNER_ACTIONS` |
| `00_CONTROL` | `TL_CONTROL` + `TL_RUNTIME_COMPATIBILITY` |
| `01_SOURCE_INVENTORY` | `TL_SOURCE_INVENTORY` |
| `02_INPUT_GAPS` | `TL_INPUT_GAPS` |
| `03_OUTPUT_INDEX` | `TL_OUTPUT_INDEX` |
| `04_DECISIONS` | `TL_DECISIONS` |
| `05_KPI_DICTIONARY` | `TL_KPI_DICTIONARY` |
| `06_COMPLIANCE_RULES` | `TL_COMPLIANCE_RULES` |
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

24 vào, 24 ra, 0 dataset mất. Ba lần gộp: `00_CONTROL`, `YV_06`, `YV_10` — mỗi tab gộp có một cột
`Nhóm` phân biệt nguồn.

## B.2 Mười ba lỗi mô hình và cách sửa

| # | Lỗi | Bằng chứng | Cách sửa |
|---|---|---|---|
| 1 | Header markdown khai dataset không tồn tại trong registry | `TL_CAMPAIGN_KPI` (`campaign-architecture.md:7`, `kpi-experiment-plan.md:6`) · `TL_AUDIENCE_POSITIONING` (`positioning.md:6`, `narrative.md:5`, `audience-hypotheses.md:7`) · `TL_PAGE_STRATEGY` (`facebook-page-strategy.md:5`) · `TL_REELS_PRODUCTION` (`production-briefs.md:6`, `reels-briefs.md:6`, `asset-and-batch-plan.md:7`). Cùng bốn tên này còn nằm ở `TOPLINK_PAGE_MILESTONES.md:368,405,451` | P1.4 viết lại header, khai đúng tên tab `YV_*`; sửa cả ba dòng ở `TOPLINK_PAGE_MILESTONES.md` |
| 2 | `audience_id` bịa theo số ngày | `toplink_sheet_sync.py:352` — `day≤7→TL-A01`, `≤14→TL-A02`, còn lại `TL-A03`; `TL-A04`, `TL-A02a`, `TL-A02b` không bao giờ xuất hiện | Thêm cột **Nhóm khách** thật vào bảng `month-calendar.md`, do người chọn; bỏ hoàn toàn suy diễn trong compiler |
| 3 | `experiment_ids` hardcode `NOT_AVAILABLE` cho cả 84 dòng | `toplink_sheet_sync.py:375` | Thêm cột **Thử nghiệm gắn kèm** vào markdown; khoá ngoại về `YV_08_experiments`; sentinel `NOT_AVAILABLE` chỉ dùng khi có lý do ghi ở `02_INPUT_GAPS` |
| 4 | Hai cột của bảng calendar bị compiler bỏ hoàn toàn | `_compile_calendar` (`toplink_sheet_sync.py:345-378`) chỉ đọc `values[0,1,2,4,5,6,8]`. Bỏ **`values[3]` = `Angle chính`** và **`values[7]` = `Review`** (`R1`/`R1+R2`/`R1+R2+R3`) — mất cả angle gốc lẫn route duyệt | Thêm `review_route` → cột **Tuyến duyệt** ở `YV_09` và `YV_12`; giữ `Angle chính` làm cột riêng, tách khỏi nội dung option A/B/C |
| 5 | `_split_options` degrade im lặng | `toplink_sheet_sync.py:329-336` — parse không ra 3 option thì `return [("A",value),("B",value),("C",value)]`, A=B=C | Fail closed: raise, kèm `content_id` và chuỗi gốc |
| 6 | B/C không có brief, reel, asset — chỉ A được materialize | `TL_PRODUCTION_BRIEFS` 28/28 trong khi calendar 84 | Sinh đủ 84 dòng ở `YV_10`; dòng B/C mang `Trạng thái sản xuất = CHƯA CÓ BRIEF` + `DỰ PHÒNG — `. Ghi rõ, không im lặng |
| 7 | Ledger 14 field vs registry 10 cột | `workflow-approval-measurement.md:48-63` khai `risk_class, dmp_check, review_route, consent_state, publish_ts, measurement_ref, edit_reset_note, claim_ids` — không có chỗ đáp | `YV_12` mở lên 18 cột hiển thị (A.20) |
| 8 | `relative_day` lệch format | markdown `D01` (pad) vs compiled `D-1` | Chuẩn hoá **`D-1` … `D-28`**, không pad, ở cả markdown lẫn dataset |
| 9 | `TL_CONTENT_PILLARS` cho `min_records: 3` trong khi mọi VERIFY yêu cầu 5 | registry | `min = max = 5`, cộng ràng buộc tổng tỷ trọng = 100 |
| 10 | `dmp-profile.md` có 21 dòng `TL-BP-*` nhưng compile ra 32 record | nguồn ≠ dataset | Đối chiếu từng dòng ở P1.4; chênh lệch nào không truy được nguồn thì xoá, không giữ |
| 11 | Gate treo không hiện ở đâu cả | `TL-R2-F02` (`CL-P2` orphan) · `TL-R2-F08` `DISCLAIMER_HOST_PENDING` hardcode ở `reels-briefs.md:18` và `workflow-approval-measurement.md:74` · founder D24–D28 sliding window | Mỗi cái một dòng ở `00_Y_VIEN_CAN_CHOT` + ô vàng tại tab liên quan |
| 12 | `funnel_role` suy diễn cứng từ pillar | `toplink_sheet_sync.py:353` — `"MOFU" if values[1] in {"TL-P3","TL-P4"} else "TOFU"`. Chỉ hai giá trị khả dĩ; `BOFU` không bao giờ xuất hiện dù phễu có giai đoạn đó | Thành cột thật **Vai trò phễu** trong `month-calendar.md`, do người đặt theo `YV_07_campaign` |
| 13 | `content_revision` hardcode `"1"` cho cả 84 dòng | `toplink_sheet_sync.py:376` | Nối với `YV_12.Bản sửa`; mỗi lần sửa lớn tăng revision và reset `approval_state` (`reset_approval_on_material_edit()` :821) |

---

# SPEC-C — Governance

## C.1 Bốn luật cứng

**Luật 1 — Status không bao giờ escalate.**
Không nâng `HYPOTHESIS → TOPLINK_CONFIRMED`, không nâng `DRAFT`/`NEEDS_HUMAN_REVIEW` → `APPROVED`.
Chỉ người đặt `APPROVED` (`RULES.md:53`, `RULES.md:129-130`). `LOCAL_VERIFIED` và Agency `PASS`
không phải `APPROVED`. Validator fail closed: so trạng thái nguồn với trạng thái đích, cao hơn = từ chối.

**Luật 2 — Vàng = ACTION_REQUIRED có hợp đồng.**
Tô vàng khi và chỉ khi **đồng thời**:
(a) trạng thái ∈ `{HYPOTHESIS, UNVERIFIED, MISSING_INPUT, NEEDS_HUMAN_REVIEW, lựa chọn còn mở}`, **và**
(b) còn một hành động của **người thật** chưa làm.
Trạng thái kỹ thuật đơn thuần không đủ. Nội dung ô mở đầu `CHƯA CHỐT — `, nêu **ai** + **chốt gì**.
Vàng ≠ `APPROVED`, ≠ bị từ chối. Dòng B/C mang `DỰ PHÒNG — `, **không vàng**.

**Luật 3 — Audit sống trong chính tab, ở hai cột ẩn cuối.**
`_key` + `_audit`, `hiddenByUser = true`. Không bao giờ bày 11 cột common ra mặt trước.

**Luật 4 — Humanize = dịch schema sang lời đời thường, không đổi meaning.**
Cấm đổi giá trị, cấm làm tròn trạng thái, cấm bỏ ràng buộc. Chỉ đổi **cách nói**.

## C.2 Một dòng = một ý nghĩ trọn vẹn

Mỗi dòng nội dung phải trả lời được: **tin gì · vì sao tin · bằng chứng mức nào · triển khai tới đâu ·
cấm hoặc thiếu gì · khi nào Tiếp tục/Sửa/Dừng · ai chịu trách nhiệm.**
Vì thế schema **không** đồng nhất giữa các tab — mỗi tab có bộ cột riêng của nó.

## C.3 Enum

Giữ nguyên 6 enum của `TL-SHEET-001/0.2.0`:
`evidence_status` · `allowed_use` · `decision_status` · `approval_state` · `publish_state` · `experiment_decision`.

Thêm hai enum:

```
review_route : R1 | R1+R2 | R1+R2+R3
cycle_id     : ^C[1-9][0-9]*$
```

Nhãn hiển thị tiếng Việt map 1:1 sang enum máy; bảng map nằm trong registry, không hardcode trong generator.

## C.4 Gate còn mở — không cái nào đóng trong lần này

`TL-GAP-002 / 004 / 005 / 006 / 007 / 009 / 010 / 012 / 013 / 014 / ASSET` vẫn mở.
`TL-M1`–`TL-M5` vẫn `NOT_COMPLETE`. Đây là repair **trong** package hai macro-run hiện có, **không mở Run 3**.

---

# SPEC-D — Pipeline tái tạo xác định

```
14 markdown canonical
        │  parse_markdown_tables()
        ▼
21 dataset (JSON sidecar, đủ 11 cột common)      ← staging/yv-humanize/datasets/
        │  validate-datasets   (schema · enum · FK · min/max · no-escalate)
        ▼
build-report-plan   (HÀM THUẦN — không mạng, không đọc Sheet)
        ▼
staging/yv-humanize/report-plan.json
        │  execute-human-layer  (chỉ Codex, chỉ sau 3 approval ký tay)
        ▼
CREATE_TAB → UPSERT (bounded) → batchUpdate format (direct)
        ▼
verify-readback   (value + format, exact)
```

## D.1 `report-plan.json` — hợp đồng, không phải gợi ý

Mỗi tab khai:

```json
{
  "tab": "YV_09_content_calendar",
  "title": "…",
  "header": ["…"],
  "used_range": "YV_09_content_calendar!A1:Q86",
  "values": [["…"]],
  "row_count": 86,
  "column_count": 17,
  "hidden_columns": ["P", "Q"],
  "yellow_cells": ["I15", "I24"],
  "expected_yellow_count": 2,
  "formatting": {
    "frozen_rows": 2,
    "basic_filter": true,
    "wrap": "WRAP",
    "vertical_alignment": "TOP",
    "column_widths": {"A": 60},
    "banding": false
  },
  "palette": {"header_bg": "#f6f4df", "header_fg": "#95131f", "action_required": "#f7e8c2"},
  "content_hash": "sha256(canonical values)"
}
```

`row_count` = 1 header + 1 legend + số dòng dữ liệu. Ví dụ trên: 1 + 1 + 84 = 86, cột A…Q (15 hiển thị + 2 ẩn).

`values` là **ma trận cố định chiều rộng** — mọi hàng cùng số cột, pad bằng chuỗi rỗng.
`content_hash` = SHA-256 của `values` canonical hoá (JSON `ensure_ascii=False`, `separators=(",",":")`).
Chạy generator hai lần liên tiếp phải ra **cùng một `content_hash`**.

Kế hoạch mang `write_executed: false`. Validator từ chối nếu đã `true` — approval dùng một lần.

## D.2 Chống Sheets hiểu nhầm

- Ô bắt đầu bằng `+`, `=`, `-`, `@` phải viết lại thành chữ (thêm tiền tố an toàn hoặc đổi ký tự đầu).
- `valueInputOption = RAW` cho mọi lần ghi.
- Ô trống có nghĩa ghi `—`, không để chuỗi rỗng, để read-back so được xác định.

## D.3 Tô màu

Tô vàng bằng **direct format**: `repeatCell` với `userEnteredFormat.backgroundColor`.
**Cấm** conditional formatting — Thảo Tây đã bị Google trả HTTP 400 rồi 500 với payload conditional-format.
Số conditional-format rule sau khi ghi phải bằng **0**; read-back kiểm.

Google lượng tử hoá RGB một mã (`0.4196` gửi đi, `0.41568628` đọc về). Giữ dung sai **một mã**
như bản vá hiện có; không nới rộng hơn.

## D.4 Apply và đường lùi

```
snapshot before (từng range)
  → batchUpdate format
  → values().batchUpdate(RAW)
  → đọc lại từng range
  → normalize_grid hai phía
  → lệch: ghi trả `before`, raise, KHÔNG retry rộng
```

Partial write = `VERIFY_FAILED`, giữ nguyên evidence.

## D.5 Read-back phải kiểm cả format

| Nhóm | Kiểm |
|---|---|
| Giá trị | value từng ô · sha256 · row/col count · stable key · dấu tiếng Việt |
| Cấu trúc | `frozenRowCount` · `basicFilter` · `wrapStrategy` · `verticalAlignment` · `columnWidth` |
| Ẩn | `hiddenByUser = true` cho `_key` và `_audit` ở cả 21 tab |
| Màu | `backgroundColor` đúng danh sách `yellow_cells` — đúng toạ độ, đúng số lượng |
| Sạch | conditional-format rule = 0 · `Trang tính1` còn nguyên · không tab `_v2` |
| Idempotency | chạy lại cùng payload lần hai cho **0 diff** |

---

# SPEC-E — Retrofit TL-M1…TL-M5 và gate mới

## E.1 14 markdown canonical viết lại tại chỗ

| Milestone | Tệp | Tab đích |
|---|---|---|
| TL-M1 | `docs Toplink/brand/dmp-profile.md` | `YV_01_brand_profile` |
| TL-M1 | `docs Toplink/system/runtime-compatibility.md` | `00_CONTROL` |
| TL-M2 | `docs Toplink/research/audience-hypotheses.md` | `YV_02_audience` |
| TL-M2 | `docs Toplink/brand/positioning.md` | `YV_03_positioning` |
| TL-M2 | `docs Toplink/brand/narrative.md` | `YV_04_narrative` |
| TL-M3 | `docs Toplink/brand/content-pillars.md` | `YV_05_content_pillars` |
| TL-M3 | `docs Toplink/brand/facebook-page-strategy.md` | `YV_06_page_strategy` |
| TL-M3 | `docs Toplink/brand/campaign-architecture.md` | `YV_07_campaign` |
| TL-M3 | `docs Toplink/brand/kpi-experiment-plan.md` | `YV_08_experiments` + `05_KPI_DICTIONARY` |
| TL-M4 | `docs Toplink/content/month-calendar.md` | `YV_09_content_calendar` + `06_COMPLIANCE_RULES` (`CL-*`) |
| TL-M4 | `docs Toplink/content/production-briefs.md` | `YV_10_production_briefs` |
| TL-M5 | `docs Toplink/content/reels-briefs.md` | `YV_10_production_briefs` |
| TL-M5 | `docs Toplink/content/asset-and-batch-plan.md` | `YV_11_asset_batch_plan` |
| TL-M5 | `docs Toplink/content/workflow-approval-measurement.md` | `YV_12_workflow_approval` |

Ghi đè **tại chỗ**, giữ nguyên đường dẫn. Bản nguyên trạng đã snapshot byte-exact tại
`staging/yv-humanize/00-baseline/` (manifest SHA-256 `e3227eb4e4c066a5ccc61e574a77f67bcc64905f2edc7383d89f687dbb3d50eb`).

Mỗi tệp sau khi viết lại có:

1. Khối header: stable ID · tab đích `YV_*` **đúng tên** · trạng thái · nguồn.
2. Bảng chính đúng thứ tự cột của SPEC-A.
3. Prose diễn giải nằm **trong ô của cột nội dung**, không dump thành đoạn văn ngoài bảng.

Ba tệp đang ở dạng bullet/H3 phải chuyển sang bảng để `parse_markdown_tables()` đọc được:
`audience-hypotheses.md §2` · `content-pillars.md` · `reels-briefs.md`.

## E.2 Gate mới `TL-M5H`

Milestone mới, **không** thay thế `TL-M1`…`TL-M5`, chỉ chồng lên:

| Điều kiện Done | Kiểm bằng |
|---|---|
| 21 dataset compile PASS | `compile-datasets` |
| `content_hash` ổn định qua 2 lần chạy | `build-report-plan` ×2 |
| Lint từ cấm 0 hit | lint §9 voice pack |
| Đối xứng ô vàng ↔ `00_Y_VIEN_CAN_CHOT` khớp hai chiều | validator |
| `03_OUTPUT_INDEX` phủ hết artifact, 0 orphan | validator |
| 21/21 tab read-back MATCH value + format | `verify-readback` |
| Chạy lại lần hai 0 diff | idempotency |
| `Trang tính1` còn nguyên, 0 tab `_v2` | `snapshot-target` |

`TL-M5H` **không** đóng bất kỳ gate người nào đang mở. Nó chỉ chứng minh workbook đúng mô hình.

## E.3 Growth — cơ chế lặp chu kỳ

- `cycle_id` (`C1`, `C2`, …) ở `YV_07`, `YV_08`, `YV_09`, `YV_10`, `YV_11`, `YV_12`.
- Ngày vẫn là nhãn tương đối `D-1`…`D-28`; không ngày tuyệt đối.
- Hết `D-28`: ghi **một dòng `04_DECISIONS`** chốt chu kỳ (kết luận Tiếp tục/Sửa/Dừng theo ngưỡng
  `05_KPI_DICTIONARY`), rồi mở `C2` bằng **cùng bộ 21 tab**.
- Không tạo tab mới cho chu kỳ mới. Không `_v2`. Số dòng `YV_09` thành 84 × số chu kỳ.
- `YV_08.Chốt ở quyết định nào` trỏ về dòng `04_DECISIONS` tương ứng — đó là khớp nối vòng học.

---

# SPEC-F — Visual system

Nguồn màu: `Yvien Hotlink Website/app-demo/styles/tokens.css:10-56`. Vai trò từng màu:
`docs/system/yvien-brand-voice-pack.md §7`.

| Vùng | Nền | Chữ |
|---|---|---|
| Header hàng 1 | `#f6f4df` cream | `#95131f` crimson-600, bold |
| Legend vàng hàng 2 | `#f6f4df` cream | `#4a4a4a` ink-soft, italic |
| Dữ liệu | `#fffcf7` ivory | `#1a1410` ink |
| Ô ACTION_REQUIRED | `#f7e8c2` gold-200 | `#1a1410` ink |
| Ô blocker cứng | `#fffcf7` ivory | `#c70002` accent-red, bold |
| Ô đã xác minh | `#fffcf7` ivory | `#2f5d50` jade-500 |
| Đường kẻ / viền | `#e7d6b4` sand | — |

Ràng buộc:

- Màu **phẳng**, không gradient, không blend (`tokens.css:6`).
- `gold-500 #d8aa4b` trên ivory ~2.1:1 — FAIL WCAG (`tokens.css:34-35`). Chỉ dùng cho viền.
  Ô vàng dùng `gold-200` làm **nền**, chữ giữ `ink`.
- Header cũ `#6B1F36` của `TL-SHEET-001` **bỏ** — không thuộc palette Y Viện.
- Không banding tự động, không merge cell trong vùng dữ liệu.
- Độ rộng cột khai tường minh trong `report-plan.json`; không auto-resize (auto-resize không tái tạo xác định).

---

## Ranh giới không được vượt

- Không gì trở thành `APPROVED` trong lần này. Không milestone nào `COMPLETE`.
- Không dùng bất kỳ identifier, workbook, credential, baseline hay nội dung nào của Thảo Tây.
- Claude không chạm Google API, không đọc key service account. Codex không tự sáng tác brand / medical /
  legal / product / founder fact.
- Dữ kiện từ repo website chỉ vào workbook với `UNVERIFIED` · `DO_NOT_USE` (voice pack §8).
- CTA trước khi gate offer mở: chỉ `theo dõi Page` · `lưu` · `chia sẻ`. Không `nhắn Zalo` —
  `facebook-page-strategy.md:44`, `campaign-architecture.md:49`, `month-calendar.md:16` đều giới hạn ba
  CTA này, và `runtime-compatibility.md:38` ghi kênh Zalo `PENDING_INPUT` (chưa đấu nối).
