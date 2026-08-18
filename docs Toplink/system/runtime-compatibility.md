# TL-M2 — Bảng điều khiển và tương thích runtime (Toplink Y Viện)

> **Run 1 Phase A · chỉ chạy nội bộ · `external_writes=0`.** Tệp này ghi lại đúng bề mặt runtime mà
> các milestone `TL-M3` và `TL-M4` dựa vào, để một lần kiểm độc lập ở Run 2 xác nhận được cùng một môi
> trường đã sinh ra gói này.

## 0. Khối định danh

| Trường | Giá trị |
|---|---|
| Milestone | `TL-M2` |
| Stable ID | `TL-RUNTIME-COMPAT-001` |
| Tab đích | `00_CONTROL` |
| Schema | `YV-SHEET-001/1.0.0` |
| Trạng thái | `LOCAL_VERIFIED` — chưa `APPROVED`, chưa ghi Sheet |
| Nguồn sự thật | `_active-brand.json` · `profile.json` · `guidelines/_manifest.json` · `RULES.md` |
| Ghi ra ngoài | `0` |

## 1. Quy ước bảng

Theo `dmp-profile.md §1`, với **một ngoại lệ đã ghi rõ**: `00_CONTROL` là tab kiểm soát, nên cột `Mã`
vừa là khoá dòng cho máy vừa là **cột hiển thị** — người vận hành cần đọc được mã để đối chiếu. Đây là
tab duy nhất cùng với `01_SOURCE_INVENTORY` và `03_OUTPUT_INDEX` được phép bày mã kỹ thuật ra mặt
trước. Các tab nội dung `YV_*` tuyệt đối không được.

Ô nền vàng nghĩa là còn một việc của người thật chưa làm.

## 2. Bảng dữ liệu — `00_CONTROL`

| Mã | Nhóm | Mục | Giá trị hiện tại | Trạng thái | Nghĩa là gì | Vai trò giữ | Chủ sở hữu |
|---|---|---|---|---|---|---|---|
| TL-CTL-01 | Nhận dạng runtime | Bộ công cụ tiếp thị | Digital Marketing Pro | Đang dùng | Bộ công cụ sinh ra toàn bộ bản kế hoạch này | Codex | Codex |
| TL-CTL-02 | Nhận dạng runtime | Phiên bản bộ công cụ | 3.15.1 | Đã khoá | Đổi phiên bản là phải chạy lại từ đầu, không vá giữa chừng | Codex | Codex |
| TL-CTL-03 | Nhận dạng runtime | Thương hiệu đang hoạt động | toplink-y-vien | Đã khoá | Trạng thái toàn cục dùng chung; làm việc thương hiệu khác phải chuyển đi rồi chuyển về | Codex | Codex |
| TL-CTL-04 | Nhận dạng runtime | Tên đọc lại của thương hiệu | Toplink Y Viện | Đã xác nhận | Đọc lại đúng tên nghĩa là không nhầm sang hồ sơ thương hiệu khác | Codex | Codex |
| TL-CTL-05 | Nhận dạng runtime | Phiên bản hồ sơ thương hiệu | 1.0.0 | Đã khoá | Hồ sơ gốc của Y Viện, mọi tệp khác đọc từ đây | Chủ Y Viện | Chủ Y Viện |
| TL-CTL-06 | Nhận dạng runtime | Bộ hướng dẫn | 5 nhóm, 52 luật | Đã khoá | Số này đổi là môi trường đã đổi, phải chạy lại | Codex | Codex |
| TL-CTL-07 | Nhận dạng runtime | Ngôn ngữ và định dạng | Tiếng Việt, ngày dạng ngày/tháng/năm, hệ mét | Đã khoá | Mọi con số và ngày trong workbook theo đúng quy ước này | Codex | Codex |
| TL-CTL-08 | Lớp hướng dẫn | Nhóm luật cấm | 18 luật | Cao nhất, không được đè | Danh mục từ cấm và câu miễn trừ bắt buộc; không kênh nào ghi đè được | Cổng sức khoẻ | Cổng sức khoẻ |
| TL-CTL-09 | Lớp hướng dẫn | Nhóm giọng và cách nói | 11 luật | Đang áp dụng | Chi tiết giọng nằm ngoài bốn thang điểm số | Hướng dẫn thương hiệu | Hướng dẫn thương hiệu |
| TL-CTL-10 | Lớp hướng dẫn | Nhóm thông điệp | 9 luật | Đang áp dụng | Bộ thông điệp và cách nói định vị đã được duyệt | Hướng dẫn thương hiệu | Hướng dẫn thương hiệu |
| TL-CTL-11 | Lớp hướng dẫn | Nhóm nhận diện thị giác | 8 luật | Đang áp dụng | Màu, phông chữ và chuyển động | Hướng dẫn thương hiệu | Hướng dẫn thương hiệu |
| TL-CTL-12 | Lớp hướng dẫn | Nhóm phong cách theo kênh | 6 luật | Đè lên giọng nền | Khi nhắm một kênh cụ thể thì luật kênh thắng giọng nền, trừ nhóm luật cấm | Hướng dẫn thương hiệu | Hướng dẫn thương hiệu |
| TL-CTL-13 | Vai trò kênh | Facebook Page | Kênh chính | Đang chạy | Danh tính, giáo dục, bằng chứng vận hành, tín hiệu cộng đồng | Chủ Y Viện | Chủ Y Viện |
| TL-CTL-14 | Vai trò kênh | Reels trên Facebook | Kênh hỗ trợ | Đang chạy | Giúp người lạ tìm thấy và giữ chân | Chủ Y Viện | Chủ Y Viện |
| TL-CTL-15 | Vai trò kênh | Zalo, điện thoại, Google Maps | Chưa đấu nối | Thiếu đầu vào | CHƯA CHỐT — chủ Y Viện cần cấp số điện thoại, tài khoản Zalo và điểm Google Maps chính thức kèm người giữ đầu mối; chưa có thì cả ba kênh này không được xuất hiện trong bất kỳ lời kêu gọi nào | Chủ Y Viện | Chủ Y Viện |
| TL-CTL-16 | Vai trò kênh | Website | Nằm trong lộ trình | Chưa đấu nối | Lớp số dài hạn, không phải kênh chính của chu kỳ này | Chủ Y Viện | Chủ Y Viện |
| TL-CTL-17 | Vai trò kênh | TikTok | Chỉ để tham khảo | Không mở | Chỉ tham chiếu cơ chế, không mở kênh trong chu kỳ này | Chủ Y Viện | Chủ Y Viện |
| TL-CTL-18 | Vai trò kênh | Facebook cá nhân của founder | Đăng lại có chọn lọc | Duyệt theo từng bài | Mỗi lần đăng lại là một hành động ngoài phạm vi, cần duyệt riêng | Cổng pháp lý | Cổng pháp lý |
| TL-CTL-19 | Bất biến hai lần chạy | Dấu vân hồ sơ thương hiệu | a45e4ae4 | Đã ghim | Lệch dấu vân là lùi về lần chạy trước, không đi tiếp | Codex | Codex |
| TL-CTL-20 | Bất biến hai lần chạy | Dấu vân nguồn | 3ba91761 | Đã ghim | Lệch dấu vân là lùi về lần chạy trước, không đi tiếp | Codex | Codex |
| TL-CTL-21 | Bất biến hai lần chạy | Bộ hướng dẫn không đổi | 5 nhóm, 52 luật | Đã ghim | Thay đổi bất kỳ mục nào ở trên đều buộc quay lại lần chạy trước | Codex | Codex |
| TL-CTL-22 | Bất biến hai lần chạy | Trạng thái thương hiệu dùng chung | Đã sao lưu giá trị trước đó | Đã ghim | Việc chuyển thương hiệu qua lại phải để lại bản sao lưu, không ghi đè mù | Codex | Codex |
| TL-CTL-23 | Điều runtime không được làm | Ghi ra ngoài | 0 lần | Chặn cứng | Không ghi Sheet, không đụng Page, không đăng, không nhắn tin | Codex | Codex |
| TL-CTL-24 | Điều runtime không được làm | Dựng lại hồ sơ thương hiệu | Không được phép | Chặn cứng | Không tạo thực thể thương hiệu mới, không dựng lại toàn bộ hồ sơ đã khoá | Codex | Codex |
| TL-CTL-25 | Điều runtime không được làm | Nâng dữ kiện thiếu bằng chứng thành sự thật | Không được phép | Chặn cứng | Giá, công dụng sản phẩm, cách nói công khai về nhượng quyền và pháp lý đều không được lên hàng sự thật | Cổng pháp lý | Cổng pháp lý |
| TL-CTL-26 | Điều runtime không được làm | Ghi khoá bí mật hay đường dẫn máy cá nhân | Không được phép | Chặn cứng | Không sản phẩm bàn giao nào được chứa khoá, mật khẩu hay đường dẫn máy cá nhân | Codex | Codex |
| TL-CTL-27 | Bảng quy chiếu mã | Mã nhóm khách | TL-A01, TL-A02a, TL-A02b, TL-A03, TL-A04 | Giữ nguyên | Mã đã phát ra ở lần chạy trước, giữ làm bí danh, không tự đánh số lại | Codex | Codex |
| TL-CTL-28 | Bảng quy chiếu mã | Mã trụ nội dung | TL-P1 tới TL-P5 | Giữ nguyên | Mã đã phát ra ở lần chạy trước, giữ làm bí danh, không tự đánh số lại | Codex | Codex |
| TL-CTL-29 | Bảng quy chiếu mã | Mã chỉ số | TL-KPI-01 tới TL-KPI-12 | Giữ nguyên | Thêm số 0 ở đầu không phải là đổi danh tính | Codex | Codex |
| TL-CTL-30 | Bảng quy chiếu mã | Mã câu claim | CL-* | Giữ nguyên | Đổi sang một hệ mã khác cần một lần chuyển đổi riêng, có đọc lại đủ tham chiếu | Cổng pháp lý | Cổng pháp lý |

## 3. Điều kiện hỏng và cách xử lý

Bất kỳ mục nào ở nhóm **Bất biến hai lần chạy** lệch so với giá trị đã ghim đều dẫn tới một kết quả
duy nhất: **quay lại lần chạy trước**, không vá giữa chừng và không đi tiếp sang bước ghi Sheet.

Kênh mang trạng thái chưa đấu nối thì **không có đường chuyển đổi nào được bật**. Lời kêu gọi đặt lịch
hay liên hệ vẫn tắt cho tới khi cổng chào bán mở — cổng này hiện chưa tồn tại.

## 4. VERIFY (TL-M2)

- [x] Ghi lại và tái lập được phiên bản bộ công cụ, thương hiệu đang hoạt động và bộ hướng dẫn.
- [x] Vai trò kênh khớp hồ sơ thương hiệu và chính sách kênh trong `RULES.md`.
- [x] Bất biến hai lần chạy nêu rõ; lệch là quay lại lần chạy trước.
- [x] Chuyển toàn bộ nội dung sang một bảng dữ liệu duy nhất cho tab `00_CONTROL`.
- [x] Ngoại lệ bày mã kỹ thuật ở tab kiểm soát được ghi rõ tại §1, không lan sang tab `YV_*`.
- [x] Một ô vàng (`TL-CTL-15`) mở đầu bằng `CHƯA CHỐT — `, có đúng một dòng đối ứng ở
      `00_Y_VIEN_CAN_CHOT`.
- [x] `external_writes=0`; tệp này không làm biến đổi runtime.
