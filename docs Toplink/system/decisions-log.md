# Sổ quyết định

- **Mã tài liệu:** `TL-DECISIONS-001`
- **Tab đích:** `04_DECISIONS` (registry `YV-SHEET-001/1.0.0`, index 6)
- **Trạng thái:** `DRAFT · LOCAL_ONLY` — dòng ở đây ghi lại một quyết định đã xảy ra, không tự nâng
  bất kỳ hạng mục nào lên `APPROVED`
- **Nguồn:** `STATE.md` §quyết định · `task.md` §sổ lease · `docs Toplink/system/owner-decisions.md`
  · `docs/system/yvien-brand-voice-pack.md`

---

## 1. Quy ước bảng

Theo `docs Toplink/brand/dmp-profile.md §1`. Riêng tab này thêm bốn luật:

1. **Một dòng = một quyết định đã xảy ra.** Việc còn treo không viết vào đây; nó thuộc
   `00_Y_VIEN_CAN_CHOT`. Sổ này là quá khứ, sổ kia là tương lai.
2. **`Ngày` là ngày tuyệt đối, dạng `YYYY-MM-DD`.** Cấm ngày tuyệt đối chỉ áp dụng cho lịch nội
   dung; sổ quyết định phải tra được theo thời gian thật. Không biết chính xác thì ghi `—`, không
   đoán.
3. **`Điều kiện xem lại` viết bằng lời người, không viết mã cổng.** Tên cổng tiếng Việt tra từ
   `display_label_map.milestone_gate`; trong sổ này chỉ ghi điều kiện đọc hiểu được.
4. **Quyết định giữ khoá cũng là quyết định.** `Trạng thái = DECIDED` với nội dung "giữ khoá" khác
   hoàn toàn `BLOCKED`. `BLOCKED` nghĩa là chưa quyết được vì thiếu điều kiện ngoài tầm.

Số dòng: **17**. Trong đó **10 dòng chủ Y Viện quyết**, **7 dòng thuộc thiết kế workbook** do bên
làm kế hoạch quyết trong phạm vi đã được giao.

---

## 2. Bảng chính

| Mã | Chu kỳ | Ngày | Ai quyết | Quyết định gì | Phạm vi áp dụng | Căn cứ | Điều kiện xem lại | Trạng thái | Chủ sở hữu |
|---|---|---|---|---|---|---|---|---|---|
| TL-D16 | C1 | 2026-07-30 | Chủ Y Viện | Giữ khoá mọi cách nói công khai về quan hệ nhượng quyền và về phạm vi pháp lý cho tới khi có văn bản thật đã kiểm chứng | Hồ sơ thương hiệu, Định vị, Chiến lược Page, Luật phát ngôn | `STATE.md` §quyết định | Khi chủ Y Viện nộp văn bản nhượng quyền hoặc giấy phép hoạt động và bên rà soát xác nhận | DECIDED | Cổng pháp lý |
| TL-D17 | C1 | 2026-07-30 | Chủ Y Viện | Nêu tên hai người chịu trách nhiệm chuyên môn cho từng bài sức khoẻ, ở mức tự khai; mỗi bài vẫn phải duyệt riêng trước khi đăng | Sổ duyệt và đăng, Luật phát ngôn, Lịch 28 ngày | `STATE.md` §quyết định | Khi có hồ sơ chuyên môn nộp thật, hoặc khi đổi người chịu trách nhiệm | DECIDED | Cổng sức khoẻ |
| TL-D18 | C1 | 2026-07-30 | Chủ Y Viện | Hồ sơ sản phẩm và dịch vụ sẽ nộp sau, kèm giấy tờ pháp lý và kết quả kiểm định đầy đủ; tới lúc đó mọi lời về công dụng giữ mức chưa kiểm chứng và chỉ dùng khung hỗ trợ | Chiến dịch 28 ngày, Luật phát ngôn, Brief sản xuất | `STATE.md` §quyết định | Khi hồ sơ sản phẩm được nộp và kiểm chứng | DECIDED | Chủ Y Viện |
| TL-D19 | C1 | 2026-07-30 | Chủ Y Viện | Cấp địa chỉ tài khoản dịch vụ ghi Sheet và cất tệp khoá ở thư mục bí mật không theo dõi bởi kho mã | Kiểm soát và runtime, Mục lục sản phẩm | `STATE.md` §quyết định | Khi đổi tài khoản dịch vụ hoặc xoay khoá | DECIDED | Chủ Y Viện |
| TL-D20 | C1 | 2026-07-30 | Chủ Y Viện | Cho phép trích xuất giới hạn phần nguồn gốc dữ liệu từ dự án gốc; kết quả đã khoá bằng digest, phần lịch sử còn thiếu đóng theo thiết kế | Kho nguồn, Sổ quyết định, Hồ sơ thương hiệu | `STATE.md` §quyết định | Không xem lại; đóng theo thiết kế | DECIDED | Codex |
| TL-D21 | C1 | 2026-07-30 | Chủ Y Viện | Cấp danh tính Page thật và chốt mốc xuất phát bằng 0 người theo dõi, coi Page là mới hoàn toàn | Từ điển chỉ số, Chiến lược Page, Kiểm soát và runtime | `STATE.md` §quyết định | Khi Page đổi định danh hoặc gộp với Page khác | DECIDED | Chủ Y Viện |
| TL-D22 | C1 | 2026-08-03 | Chủ Y Viện | Giới hạn phạm vi lịch nội dung và quyền dùng tư liệu cho một giai đoạn làm việc, không mở rộng ra ngoài | Lịch 28 ngày, Kế hoạch tư liệu và mẻ quay | `STATE.md` §trạng thái milestone | Khi mở giai đoạn làm việc kế tiếp | DECIDED | Chủ Y Viện |
| TL-D23 | C1 | 2026-08-05 | Chủ Y Viện | Dựng lại workbook theo hướng người đọc trước, máy kiểm chứng sau: 21 tab, tiền tố tab nội dung đổi sang dạng ngắn của Y Viện, gộp 24 bộ dữ liệu cũ xuống 21 tab | Toàn workbook | Bản kế hoạch tái thiết kế đã duyệt | Khi thêm chu kỳ mới cần thêm tab, hoặc khi một tab vượt trần số dòng | DECIDED | Chủ Y Viện |
| TL-D24 | C1 | 2026-08-05 | Chủ Y Viện | Duyệt bộ giọng thương hiệu Y Viện làm chuẩn ngôn từ cho mọi ô hiển thị, gồm xưng hô, danh sách từ cấm và bảng màu | Toàn workbook, mọi tệp nguồn | `docs/system/yvien-brand-voice-pack.md` | Khi thương hiệu đổi định vị hoặc đổi bảng màu | DECIDED | Chủ Y Viện |
| TL-D25 | C1 | 2026-08-05 | Chủ Y Viện | Chỉ Codex được ghi vào Sheet; bên soạn nội dung làm việc hoàn toàn tại chỗ, không chạm giao diện lập trình của Google | Kiểm soát và runtime, Mục lục sản phẩm | Bản kế hoạch tái thiết kế đã duyệt | Không xem lại trong chu kỳ này | DECIDED | Chủ Y Viện |
| TL-D26 | C1 | 2026-08-05 | Bên làm kế hoạch | Ghi 11 cột nguồn gốc dữ liệu vào hai cột ẩn cuối mỗi tab thay vì bày ra mặt trước; bản đầy đủ nằm ở tệp kèm dạng máy đọc | Toàn workbook | `docs/system/yvien-sheet-human-layer-spec.md` §SPEC-A | Khi cần thêm trường nguồn gốc mới | DECIDED | Bên làm kế hoạch |
| TL-D27 | C1 | 2026-08-05 | Bên làm kế hoạch | Tô vàng bằng định dạng trực tiếp trên từng ô, cấm dùng quy tắc định dạng theo điều kiện; sau khi ghi, số quy tắc định dạng theo điều kiện phải bằng 0 | Toàn workbook | `docs/system/yvien-sheet-human-layer-spec.md` §SPEC-D | Nếu Google đổi hành vi giao diện lập trình | DECIDED | Codex |
| TL-D28 | C1 | 2026-08-05 | Bên làm kế hoạch | Hợp đồng ô vàng cần đồng thời hai điều kiện: trạng thái còn mở và một hành động của người thật còn treo. Trạng thái kỹ thuật đơn thuần không đủ để tô vàng | Toàn workbook | `docs/system/yvien-sheet-human-layer-spec.md` §SPEC-C | Khi đổi bộ trạng thái | DECIDED | Bên làm kế hoạch |
| TL-D29 | C1 | 2026-08-05 | Bên làm kế hoạch | Tab báo cáo tổng hợp và tab thiếu đầu vào không tô ô vàng nào; mọi việc treo đã có ô vàng ở tab gốc và một dòng ở sổ việc, tô lại làm hỏng luật đối xứng một-đổi-một | Báo cáo tổng hợp, Thiếu đầu vào | `docs Toplink/system/report-human-layer.md` §1 · `docs Toplink/system/input-gaps.md` §1 | Khi luật đối xứng ô vàng đổi | DECIDED | Bên làm kế hoạch |
| TL-D30 | C1 | 2026-08-05 | Bên làm kế hoạch | Lịch chạy theo chu kỳ 28 ngày với nhãn tương đối, lặp lại bằng cột chu kỳ thay vì tạo tab mới; hết một chu kỳ thì ghi một dòng chốt vào sổ này rồi mở chu kỳ kế | Lịch 28 ngày, Chiến dịch, Thử nghiệm, Brief sản xuất, Sổ duyệt và đăng | Bản kế hoạch tái thiết kế đã duyệt | Cuối mỗi chu kỳ | DECIDED | Bên làm kế hoạch |
| TL-D31 | C1 | — | Chủ Y Viện | Ba phê duyệt ghi Sheet phải ký riêng biệt và tách rời: tạo tab, ghi dữ liệu, đọc lại. Chưa ký thì không được chạm Sheet | Mục lục sản phẩm, Sổ quyết định | `docs/system/toplink-google-sheets-operational-contract.md` §2 | Mỗi lần ghi Sheet đều cần bộ chữ ký mới | BLOCKED | Chủ Y Viện |
| TL-D32 | C1 | — | Chủ Y Viện | Chọn cách xử lý trụ nội dung đang thiếu câu phát ngôn được duyệt: viết câu mới, hay dùng ranh giới của một câu đã có | Luật phát ngôn, Trụ nội dung, Brief sản xuất | `docs Toplink/system/owner-decisions.md` | Trước khi lên brief tuần 2 | BLOCKED | Chủ Y Viện |

---

## 3. Ghi chú đọc bảng

Mười dòng đầu là quyết định của chủ Y Viện — chúng ràng buộc nội dung và không được sửa bởi bên làm
kế hoạch. Bảy dòng thiết kế workbook ràng buộc cách dựng bảng, không ràng buộc nội dung; đổi chúng
không cần chủ Y Viện, nhưng phải ghi thêm một dòng mới ở đây chứ không sửa dòng cũ.

Hai dòng cuối mang `Trạng thái = BLOCKED` vì điều kiện nằm ngoài tầm của bên làm kế hoạch: một cái
chờ chữ ký, một cái chờ chọn của chủ Y Viện. Chúng nằm ở đây để giữ vết; hành động tương ứng nằm ở
`00_Y_VIEN_CAN_CHOT`.

Sổ này chỉ tính từ mốc dự án trở thành độc lập. Lịch sử trước đó đóng theo thiết kế — xem dòng
`TL-GAP-014` ở sổ thiếu đầu vào.

---

## 4. VERIFY

- Đúng **17 dòng**, mã duy nhất, khớp `min_records: 1` · `max_records: 200`.
- `Chu kỳ` toàn bộ `C1`, khớp mẫu `^C[1-9][0-9]*$`.
- `Trạng thái` chỉ nhận giá trị thuộc `decision_status`: **15 `DECIDED`**, **2 `BLOCKED`**, không
  dòng nào `OPEN` (việc còn mở thuộc `00_Y_VIEN_CAN_CHOT`).
- **0 ô vàng** ở tab này (`expected_yellow_count: 0`): mọi dòng đã là quá khứ, không còn hành động
  treo; hai dòng `BLOCKED` có ô vàng của chúng ở sổ việc (`TL-OA-11`, `TL-OA-14`).
- `Ngày` dạng `YYYY-MM-DD` hoặc `—`; không đoán ngày.
- Cột hiển thị không chứa mã `TL-*` hay `YV-*`; mã nằm ở cột `Mã` (khoá máy, ẩn).
- Không ô nào bắt đầu bằng `+`, `=`, `-`, `@`.
