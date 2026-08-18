# Hướng dẫn đọc workbook Y Viện

Workbook đã lên Sheet ngày `2026-08-05`. 21 tab nội dung, `Trang tính1` cũ giữ nguyên không đụng.
Tài liệu này để mở ra dùng được ngay, không cần đọc hợp đồng kỹ thuật.

Spreadsheet: `1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms`

## Mở theo thứ tự này

**1. `00_Y_VIEN_CAN_CHOT`** — mở đầu tiên. 23 dòng, mỗi dòng là một việc cần người quyết.
18 dòng `OPEN` (chờ chủ Y Viện), 5 dòng `BLOCKED` (chờ điều kiện ngoài tầm).

**2. `report`** — bảng đọc. Nền tảng chiến lược, 84 dòng lựa chọn nội dung theo ngày, hướng ghép flow.
Mỗi ngày có một khuyến nghị và hai dự phòng.

**3. Còn lại** — tra khi cần, không phải đọc tuần tự.

## Ô vàng nghĩa là gì

Vàng `#f7e8c2` = **có người thật cần làm một việc**, không phải lỗi, không phải bị từ chối.
Nội dung ô luôn mở đầu `CHƯA CHỐT — ` và nêu rõ ai + chốt điều gì. Toàn bảng có đúng **27 ô vàng**.

Dòng mở đầu `DỰ PHÒNG — ` là hướng thay thế, **không tô vàng**, không cần quyết gì.

Không ô vàng nào nghĩa là `APPROVED`. Chỉ người mới đặt được `APPROVED`.

## 18 việc đang chờ chủ Y Viện chốt

| # | Mức | Nhóm | Chốt điều gì |
|---|---|---|---|
| 1 | CHẶN NGAY | Chuyên môn sức khoẻ | Chỉ định người có chuyên môn rà từng bài tuần 2 |
| 2 | CHẶN NGAY | Đồng ý hình ảnh | Ai được lên hình tuần 3, đã có đồng ý văn bản chưa |
| 7 | CHẶN NGAY | Đồng ý hình ảnh | Đồng ý văn bản của từng người trong video hậu trường |
| 8 | CHẶN NGAY | Đồng ý hình ảnh | Phạm vi được nói của founder, ký đồng ý |
| 10 | CHẶN NGAY | Chuyên môn sức khoẻ | Bằng chứng chuyên môn của người rà nội dung sức khoẻ |
| 11 | CHẶN NGAY | Ghi Sheet | Ký ba phê duyệt ghi Sheet — **đã ký `2026-08-05`**, xem ghi chú dưới |
| 12 | CHẶN NGAY | Quyền tư liệu | Chính sách quyền dùng tư liệu cả chu kỳ |
| 13 | CHẶN NGAY | Nội dung | Nơi đặt câu miễn trừ sức khoẻ |
| 3 | CAO | Hồ sơ sản phẩm | Nhánh tuần 4: nộp hồ sơ sản phẩm/dịch vụ hay không |
| 6 | CAO | Kênh liên hệ | Số điện thoại, Zalo, điểm Google Maps chính thức |
| 9 | CAO | Sản xuất | Ai quay, ai dựng, ai duyệt |
| 14 | CAO | Nội dung | Câu claim cho trụ "Hiểu và lắng nghe tín hiệu" |
| 15 | CAO | Sản xuất | Ngày bắt đầu đăng thật + số bài một tuần |
| 16 | CAO | Hồ sơ sản phẩm | Hồ sơ nguồn gốc, kiểm định, cơ sở từng câu nói về sản phẩm |
| 4 | TRUNG BÌNH | Đo lường | Mở cổng chào bán: dịch vụ, điều kiện, đầu mối, thời gian |
| 5 | TRUNG BÌNH | Đo lường | Cách đo mức nhận biết thương hiệu |
| 17 | TRUNG BÌNH | Hồ sơ sản phẩm | Hồ sơ mô tả từng sản phẩm và dịch vụ đang cung cấp thật |
| 18 | TRUNG BÌNH | Kênh liên hệ | Cách đặt lịch, cách liên hệ, thời gian phản hồi cam kết |

Bốn dòng `CHẶN NGAY` về đồng ý hình ảnh và chuyên môn sức khoẻ chặn thẳng việc sản xuất tuần 2-3.
Chốt trước những dòng đó thì phần còn lại chạy được.

**Ghi chú dòng 11:** ba phê duyệt ghi Sheet đã được ký ngày `2026-08-05` và đã tiêu thụ xong. Dòng
trên bảng vẫn hiện `OPEN` vì trạng thái chỉ đổi khi có vòng sync mới — không có runtime nào tự nâng
trạng thái. Xem `staging/yv-humanize/approvals/SIGNATURES.md`.

## 5 việc đang khoá

| # | Nhóm | Khoá vì |
|---|---|---|
| 19 | Pháp lý | Chưa có giấy tờ nhượng quyền trong tay |
| 20 | Pháp lý | Chưa có tên pháp lý, giấy phép, phạm vi hoạt động |
| 21-23 | Nguồn gốc dữ liệu | Kho nguồn hiện tại không bằng kho lịch sử; đóng theo thiết kế |

Dòng 19-20 mở được khi có giấy tờ. Dòng 21-23 đóng vĩnh viễn theo ranh giới nguồn, không phải việc
cần làm.

## 21 tab

**Hai tab mở đầu:** `report` · `00_Y_VIEN_CAN_CHOT`

**Hệ thống (7):**

| Tab | Dùng để |
|---|---|
| `00_CONTROL` | Tham số điều khiển, tương thích runtime |
| `01_SOURCE_INVENTORY` | 22 tệp nguồn + SHA-256 từng tệp |
| `02_INPUT_GAPS` | Thiếu gì, ai cấp được, chặn milestone nào |
| `03_OUTPUT_INDEX` | Mục lục sản phẩm, trạng thái đưa lên Sheet |
| `04_DECISIONS` | Sổ quyết định — 17 dòng nguồn + vết thi hành |
| `05_KPI_DICTIONARY` | Chỉ số, mốc xuất phát, ngưỡng Tiếp tục / Sửa / Dừng |
| `06_COMPLIANCE_RULES` | Được nói gì, cấm nói gì, ai duyệt |

**Nội dung (12):**

| Tab | Dùng để |
|---|---|
| `YV_01_brand_profile` | Hồ sơ thương hiệu + mức bằng chứng từng mục |
| `YV_02_audience` | Nhóm khách, giả định, cách kiểm chứng |
| `YV_03_positioning` | Tuyên bố định vị + ranh giới được nói |
| `YV_04_narrative` | Luật kể chuyện, ai giữ giọng, cổng founder |
| `YV_05_content_pillars` | 5 trụ nội dung, tỷ trọng, vai trò phễu |
| `YV_06_page_strategy` | Chiến lược Page + mốc đối chiếu |
| `YV_07_campaign` | 4 giai đoạn chu kỳ, cổng cứng, kêu gọi mặc định |
| `YV_08_experiments` | Giả thuyết + dấu hiệu Tiếp tục / Sửa / Dừng |
| `YV_09_content_calendar` | 28 ngày × 3 hướng = 84 dòng |
| `YV_10_production_briefs` | Brief sản xuất từng dòng lịch |
| `YV_11_asset_batch_plan` | Mẻ sản xuất, quyền dùng, đồng ý người xuất hiện |
| `YV_12_workflow_approval` | Sổ duyệt, trạng thái đăng, tuyến duyệt |

## Vài quy ước để khỏi hiểu nhầm

**Ngày là nhãn tương đối `D-1`…`D-28`, không phải ngày thật.** Ngày bắt đầu đăng chưa chốt — đó là
việc số 15. Chốt xong mới quy được sang ngày dương lịch.

**Cột `_key` và `_audit` bị ẩn ở cả 21 tab.** Đó là lớp máy: mã dòng, đường dẫn nguồn, mức bằng chứng,
digest, chủ sở hữu, giờ cập nhật. Bỏ ẩn để tra nguồn, không cần cho việc đọc thường ngày.

**Hàng 1 là tiêu đề, hàng 2 là chú giải, dữ liệu từ hàng 3.** Hai hàng đầu đóng băng, có filter sẵn.

**Ô ghi `—` nghĩa là "trống có chủ ý"**, khác ô để trắng. Không đoán, không bịa số.

**Mốc xuất phát hiện tại:** follower `0`, mức nhận biết `NO_MEASUREMENT`. Đây là số thật, không phải
lỗi nhập.

## Chưa có gì được duyệt

Sync xong nghĩa là kế hoạch đã lên bảng để đọc và chốt — **không** nghĩa là đã duyệt đăng.
Không dòng nào ở trạng thái `APPROVED`. Không được đăng bài, không được chạm Page, không được mở cổng
chào bán trước khi chủ Y Viện chốt các dòng `CHẶN NGAY` tương ứng.
