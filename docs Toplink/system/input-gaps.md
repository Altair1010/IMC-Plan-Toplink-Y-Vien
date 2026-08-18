# Sổ thiếu đầu vào

- **Mã tài liệu:** `TL-INPUT-GAPS-001`
- **Tab đích:** `02_INPUT_GAPS` (registry `YV-SHEET-001/1.0.0`, index 4)
- **Trạng thái:** `DRAFT · LOCAL_ONLY` — không dòng nào ở đây là `APPROVED`
- **Nguồn:** `docs Toplink/TOPLINK_PAGE_MILESTONES.md` §sổ thiếu đầu vào · `STATE.md` §quyết định
  · `docs Toplink/system/owner-decisions.md`

---

## 1. Quy ước bảng

Theo `docs Toplink/brand/dmp-profile.md §1`. Riêng tab này thêm ba luật:

1. **Không tô vàng.** Tab này là *sổ đăng ký*, không phải nơi giao việc. Mọi việc còn treo đã có
   đúng một dòng ở `00_Y_VIEN_CAN_CHOT`; tô vàng lại ở đây làm hỏng luật đối xứng một-đổi-một và
   làm loãng chính sổ việc. Cột `Trạng thái` đã nói đủ.
2. **`Chặn milestone nào` ghi mã cổng máy** (`TL-M1`…`TL-M8`); Sheet hiển thị tên tiếng Việt tra từ
   `display_label_map.milestone_gate`. Nhiều cổng thì ngăn bằng dấu phẩy.
3. **Thiếu đầu vào đã được quyết là "giữ khoá" vẫn nằm trong sổ.** Quyết định không xoá khoảng
   trống; nó chỉ đóng hành động. `Trạng thái` phân biệt bốn thể: `Đang mở` · `Đã cấp` ·
   `Giữ khoá theo quyết định` · `Đóng theo thiết kế`.

Số dòng: **13**. Trong đó **7 dòng `Đang mở`**, **2 dòng `Đã cấp`**, **1 dòng
`Giữ khoá theo quyết định`** (gộp hai mã khung nhượng quyền/pháp lý), **3 dòng
`Đóng theo thiết kế`**.

---

## 2. Bảng chính

| Mã | Thiếu gì | Ai cấp được | Chặn milestone nào | Cách gỡ | Trạng thái | Chủ sở hữu |
|---|---|---|---|---|---|---|
| TL-GAP-001 | Danh tính Page thật: mã Page, mốc xuất phát người theo dõi, Page mới hay Page đã chạy | Chủ Y Viện | TL-M1, TL-M6 | Chủ Y Viện đã cấp mã Page `61591880797654`, mốc xuất phát tính từ lúc bắt đầu việc, người theo dõi 0, Page mới hoàn toàn. Không cần làm gì thêm | Đã cấp | Chủ Y Viện |
| TL-GAP-002 | Văn bản chứng minh quan hệ nhượng quyền hoặc quan hệ thương hiệu giữa Y Viện và bên nhượng | Chủ Y Viện · bên nhượng quyền | TL-M1, TL-M2 | Chủ Y Viện đã quyết giữ khoá cho tới khi có văn bản thật và đã kiểm chứng. Trong lúc chờ, mọi cách nói công khai về quan hệ này bị cấm. Xem dòng `TL-OA-19` ở sổ việc | Giữ khoá theo quyết định | Cổng pháp lý |
| TL-GAP-004 | Hồ sơ mô tả từng sản phẩm và từng dịch vụ: tên, thành phần, công dụng nói được, chống chỉ định, giá | Chủ Y Viện | TL-M2, TL-M5 | Chủ Y Viện nộp hồ sơ kèm giấy tờ pháp lý và kết quả kiểm định. Chưa có thì mọi lời về sản phẩm giữ mức chưa kiểm chứng và chỉ dùng khung hỗ trợ. Xem `TL-OA-17` | Đang mở | Chủ Y Viện |
| TL-GAP-005 | Cách khách đặt lịch, đầu mối liên hệ, thời gian phản hồi cam kết, thông báo riêng tư khi nhận tin nhắn | Chủ Y Viện | TL-M3, TL-M6 | Chủ Y Viện chốt quy trình đặt lịch và câu thông báo riêng tư. Chưa chốt thì lời kêu gọi dừng ở theo dõi Page, lưu, chia sẻ. Xem `TL-OA-18` | Đang mở | Chủ Y Viện |
| TL-GAP-006 | Ngày bắt đầu đăng thật và số bài một tuần chịu được | Chủ Y Viện | TL-M5, TL-M6 | Chủ Y Viện chốt ngày mở chu kỳ trên Page. Trong lúc chờ, lịch dùng nhãn tương đối `D-1`…`D-28`, không ngày tuyệt đối. Xem `TL-OA-15` | Đang mở | Chủ Y Viện |
| TL-GAP-007 | Bằng chứng chuyên môn của người rà nội dung sức khoẻ | Chủ Y Viện | TL-M5, TL-M6 | Chủ Y Viện đã nêu tên hai người chịu trách nhiệm ở mức tự khai; vẫn cần hồ sơ chuyên môn nộp thật, và mỗi bài sức khoẻ vẫn phải duyệt riêng từng bài. Xem `TL-OA-10` | Đang mở | Cổng sức khoẻ |
| TL-GAP-008 | Quyền ghi vào Google Sheet đích: chia sẻ quyền Sửa cho tài khoản dịch vụ, bật API, trỏ đúng tệp khoá, và ba phê duyệt ghi đã ký | Chủ Y Viện | TL-M5H | Chủ Y Viện đã cấp địa chỉ tài khoản dịch vụ và tệp khoá đã cất nơi an toàn. Còn thiếu ba xác nhận và ba chữ ký phê duyệt cho tạo tab, ghi dữ liệu, đọc lại. Xem `TL-OA-11` | Đang mở | Chủ Y Viện |
| TL-GAP-009 | Tên pháp lý đầy đủ, giấy phép hoạt động, phạm vi hành nghề được đăng ký | Chủ Y Viện | TL-M1, TL-M2 | Chủ Y Viện đã quyết giữ khoá cùng lượt với `TL-GAP-002`. Không phát ngôn công khai về pháp lý cho tới khi có giấy tờ thật. Xem `TL-OA-20` | Giữ khoá theo quyết định | Cổng pháp lý |
| TL-GAP-010 | Cơ sở của từng công dụng được nói: nguồn gốc, kiểm định, tài liệu tham chiếu | Chủ Y Viện | TL-M2, TL-M5 | Chủ Y Viện nộp hồ sơ nguồn gốc và kiểm định cho từng công dụng định nói. Chưa có thì không nói công dụng nào, kể cả ở mức gợi ý. Xem `TL-OA-16` | Đang mở | Cổng sức khoẻ |
| TL-GAP-012 | Kho nguồn lịch sử đầy đủ trước lần chuyển dự án | Dự án gốc | TL-M1 | Đã định vị được nguồn và khoá bằng digest; phần còn thiếu đóng theo thiết kế. Không được tuyên bố kho nguồn hiện tại là đầy đủ. Xem `TL-OA-21` | Đóng theo thiết kế | Codex |
| TL-GAP-013 | Ảnh chụp hồ sơ thương hiệu tại thời điểm trước lần chuyển dự án | Dự án gốc | TL-M1, TL-M2 | Đã định vị và khoá bằng digest. Không suy rộng nguồn gốc trường dữ liệu ra ngoài phần có bằng chứng. Xem `TL-OA-22` | Đóng theo thiết kế | Codex |
| TL-GAP-014 | Lịch sử quyết định và đối chiếu thay đổi trước lần chuyển dự án | Dự án gốc | TL-M1 | Đã định vị và khoá bằng digest. Sổ quyết định hiện tại chỉ tính từ mốc dự án độc lập trở đi. Xem `TL-OA-23` | Đóng theo thiết kế | Codex |
| TL-GAP-ASSET | Chính sách quyền dùng tư liệu: ai giữ bản quyền ảnh và video, dùng được ở đâu, dùng được bao lâu, gỡ thế nào khi người trong hình rút đồng ý | Chủ Y Viện | TL-M5 | Chủ Y Viện chốt chính sách quyền dùng cho cả chu kỳ trước mẻ quay đầu tiên. Chưa chốt thì mọi tư liệu có người đứng ở mức chưa gỡ quyền. Xem `TL-OA-12` | Đang mở | Cổng pháp lý |

---

## 3. Ghi chú đọc bảng

Bảy dòng `Đang mở` là bảy việc thật đang chặn. Hai dòng `Giữ khoá theo quyết định` không phải việc
quên làm — chủ Y Viện đã cân nhắc và chọn khoá; sổ giữ lại để không ai lặng lẽ mở khoá sau này. Ba
dòng `Đóng theo thiết kế` là giới hạn của lịch sử dữ liệu, không phải lỗi: chúng chỉ cấm một kiểu
tuyên bố, không chặn việc chạy.

`TL-GAP-003` và `TL-GAP-011` không xuất hiện ở bảng này: cả hai đã đóng trọn vẹn trong các vòng
trước và không còn ràng buộc nào lên workbook. Đánh số giữ nguyên khoảng trống để mã cũ trong lịch
sử vẫn tra được.

---

## 4. VERIFY

- Đúng **13 dòng**, mã duy nhất, khớp `min_records: 1` · `max_records: 200`.
- **0 ô vàng** ở tab này (`expected_yellow_count: 0`).
- Mỗi dòng `Đang mở` trỏ đúng một mã `TL-OA-*` ở `00_Y_VIEN_CAN_CHOT`:
  `TL-GAP-004`→`TL-OA-17` · `005`→`TL-OA-18` · `006`→`TL-OA-15` · `007`→`TL-OA-10` ·
  `008`→`TL-OA-11` · `010`→`TL-OA-16` · `ASSET`→`TL-OA-12`.
- Mỗi dòng không mở cũng trỏ được: `002`→`TL-OA-19` · `009`→`TL-OA-20` · `012`→`TL-OA-21` ·
  `013`→`TL-OA-22` · `014`→`TL-OA-23`. `001` đã cấp, không cần dòng việc.
- `Chặn milestone nào` chỉ chứa mã thuộc `display_label_map.milestone_gate`.
- Không ô nào bắt đầu bằng `+`, `=`, `-`, `@`. Ô trống có nghĩa ghi `—`.
