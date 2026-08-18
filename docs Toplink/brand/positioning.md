# TL-M3 — Định vị Toplink Y Viện

> **Run 1 Phase A · chỉ chạy nội bộ · `external_writes=0`.** Định vị đang ở mức **giả thuyết**, chưa
> được duyệt để nói công khai, cho tới khi có bằng chứng từ chu kỳ chạy thử và cổng người duyệt.
> Không khẳng định bất kỳ dữ kiện nhượng quyền, pháp lý hay công dụng nào.

## 0. Khối định danh

| Trường | Giá trị |
|---|---|
| Milestone | `TL-M3` |
| Stable ID | `TL-POSITIONING-001` |
| Tab đích | `YV_03_positioning` |
| Schema | `YV-SHEET-001/1.0.0` |
| Trạng thái | `HYPOTHESIS · NOT_PUBLIC_APPROVED` — chưa `APPROVED`, chưa ghi Sheet |
| Nguồn sự thật | brief §Confirmed foundation · taxonomy §1–2 · master plan §9, §16 · `profile.json` `identity.positioning_statement` |
| Ghi ra ngoài | `0` |

## 1. Câu định vị nội bộ

> Toplink hướng tới trở thành một **điểm chạm dưỡng thân – tỉnh thức** cho người muốn chăm sóc cơ thể
> đều đặn, kết hợp trải nghiệm chỉn chu với hệ **Lý – Dược – Dưỡng** được dùng **đúng nhu cầu, đúng
> người, đúng thời điểm và đúng giới hạn**.

Ranh giới chứng minh: không nói chữa khỏi, không nói điều trị, không nói thay thế y khoa, không dựng
khung bệnh viện. Công dụng sản phẩm vẫn `UNVERIFIED`.

## 2. Bảng dữ liệu — `YV_03_positioning`

Quy ước bảng theo `dmp-profile.md §1`. Cột `Mã` và `Chủ sở hữu` là cột máy, không hiển thị.

| Mã | Loại tuyên bố | Câu tuyên bố | Mức chứng minh | Ranh giới được nói | Đường kiểm chứng | Chủ sở hữu |
|---|---|---|---|---|---|---|
| TL-POS-01 | Định vị lõi | Điểm chạm dưỡng thân – tỉnh thức cho người muốn chăm sóc cơ thể đều đặn, dùng hệ Lý – Dược – Dưỡng đúng nhu cầu, đúng người, đúng thời điểm và đúng giới hạn | HYPOTHESIS | Không chữa khỏi, không điều trị, không thay thế y khoa, không khung bệnh viện | Chạy 28 ngày nội dung, đo tín hiệu lưu bài và chia sẻ trên trụ trải nghiệm không gian | Chủ Y Viện |
| TL-POS-02 | Khung ngành | Y Viện là không gian chăm sóc sức khoẻ chủ động, đi đều đặn — không phải bệnh viện hay cơ sở khám chữa bệnh | TOPLINK_CONFIRMED | Cấm chữ "bệnh viện", cấm dấu thập tự, cấm mọi hình ảnh gợi cơ sở y tế | Rà soát ngôn từ theo bộ luật phát ngôn sức khoẻ trước khi đăng | Cổng sức khoẻ |
| TL-POS-03 | Khung ngành | Y Viện kết hợp Đông y dưỡng sinh với lý liệu và công nghệ cao — không phải nơi cam kết chữa khỏi hay điều trị dứt điểm | TOPLINK_CONFIRMED | Cấm mọi cam kết kết quả; thêm chữ "hỗ trợ" không hợp thức hoá một khẳng định thiếu bằng chứng | Rà soát ngôn từ theo bộ luật phát ngôn sức khoẻ trước khi đăng | Cổng sức khoẻ |
| TL-POS-04 | Khung ngành | Y Viện là trải nghiệm chỉn chu, riêng tư, minh bạch giới hạn — không phải spa đại trà và không phải nơi chỉ bán sản phẩm | TOPLINK_CONFIRMED | Không hạ xuống ngôn ngữ khuyến mãi; không đẩy sản phẩm khi chưa mở cổng chào bán | Đo tỷ lệ lưu bài trên trụ trải nghiệm và trụ quy trình | Chủ Y Viện |
| TL-POS-05 | Khung ngành | Y Viện hỗ trợ thư giãn, làm ấm, lưu thông và phục hồi — không phải sản phẩm thay thế thuốc hay thay thế bác sĩ | TOPLINK_CONFIRMED | Bắt buộc kèm câu miễn trừ; cấm suy ra kết quả điều trị | Rà soát từng bài theo tuyến duyệt R1+R2 | Cổng sức khoẻ |
| TL-POS-06 | Tài sản khác biệt | Không gian bốn tầng Tĩnh · Thông · Dưỡng · Tỉnh | TOPLINK_CONFIRMED | Chỉ mô tả không gian; cấm suy ra hiệu quả sức khoẻ từ không gian | Dùng ảnh thật của Y Viện; chờ bộ ảnh gốc được cấp | Chủ Y Viện |
| TL-POS-07 | Tài sản khác biệt | Quy trình tám bước từ tiếp nhận tới hẹn lịch | TOPLINK_CONFIRMED | Chỉ minh bạch quy trình; cấm suy ra kết quả từ quy trình | Đo lượng câu hỏi về quy trình trong bình luận | Chủ Y Viện |
| TL-POS-08 | Tài sản khác biệt | Hệ Lý – Dược – Dưỡng | TOPLINK_CONFIRMED ở mức tên gọi | Giải thích "đúng cách, đúng người, đúng thời điểm"; cấm mọi khẳng định công dụng | Cần người có chuyên môn rà từng bài trước khi đăng | Cổng sức khoẻ |
| TL-POS-09 | Tài sản khác biệt | Liệu trình cá nhân hoá theo thể trạng | TOPLINK_CONFIRMED ở mức mô hình | Chỉ nói về trải nghiệm và cách chọn; cấm cam kết kết quả | Đo lượng tin nhắn hỏi về liệu trình sau khi mở cổng chào bán | Chủ Y Viện |
| TL-POS-10 | Tài sản khác biệt | Hành trình và triết lý của founder | HYPOTHESIS | Chỉ hành trình, triết lý, cách vận hành; cấm cơ chế, cấm chỉ định sản phẩm | Duyệt từng bài; giới hạn tỷ trọng founder dưới 20% số bài | Cổng pháp lý |
| TL-POS-11 | Tài sản khác biệt | Quan hệ với hệ thống mẹ Nhất Liệu Y Viện | MISSING_INPUT | **Không** có cách nói công khai nào cho tới khi có văn bản; chỉ dùng nội bộ | Chờ văn bản pháp lý xác nhận quan hệ và phạm vi được nói | Cổng pháp lý |
| TL-POS-12 | Thông điệp lõi | Chăm sóc cơ thể bắt đầu từ việc lắng nghe | TOPLINK_CONFIRMED | Không cần cổng thêm; đây là câu định vị, không phải khẳng định sức khoẻ | Dùng làm câu mở cho trụ triết lý; đo tỷ lệ lưu bài | Hướng dẫn thương hiệu |
| TL-POS-13 | Thông điệp lõi | Hỗ trợ thư giãn, làm ấm, lưu thông, phục hồi — đúng người, đúng lúc | TOPLINK_CONFIRMED | Bắt buộc kèm câu miễn trừ ở mọi lần dùng | Rà soát theo bộ luật phát ngôn sức khoẻ | Cổng sức khoẻ |
| TL-POS-14 | Thông điệp lõi | Không gian và quy trình rõ ràng, minh bạch giới hạn | TOPLINK_CONFIRMED | Chỉ nói ở mức vận hành; cấm mở rộng sang kết quả | Đối chiếu với quy trình tám bước đã xác nhận | Chủ Y Viện |
| TL-POS-15 | Thông điệp lõi | Hiểu Lý – Dược – Dưỡng để chăm sóc chủ động | TOPLINK_CONFIRMED ở mức tên gọi | Công dụng vẫn chưa kiểm chứng; cấm mọi câu ngụ ý hiệu quả | Người có chuyên môn rà từng bài | Cổng sức khoẻ |
| TL-POS-16 | Địa bàn | Hà Nội — nhận biết tại chỗ, bằng chứng vận hành, khám phá dịch vụ | TOPLINK_CONFIRMED | Chỉ mở phần chuyển đổi khi bảng giá và điều khoản đã được xác nhận | Chờ chủ Y Viện cấp bảng giá và điều khoản | Chủ Y Viện |
| TL-POS-17 | Địa bàn | Toàn quốc — chỉ giáo dục và nhận biết thương hiệu | TOPLINK_CONFIRMED | **Cấm** mọi ngụ ý có cơ sở hoặc dịch vụ tại địa phương ngoài Hà Nội | Kiểm tra mọi bài toàn quốc không chứa lời mời tới cơ sở | Cổng pháp lý |

## 3. VERIFY (TL-M3)

- [x] Định vị dán nhãn `HYPOTHESIS`; ranh giới chứng minh ghi rõ từng dòng.
- [x] Không khẳng định dữ kiện nhượng quyền, pháp lý hay công dụng; quan hệ hệ thống mẹ giữ nội bộ.
- [x] Tách bạch Hà Nội và toàn quốc; không suy ra dịch vụ toàn quốc.
- [x] Header khai đúng tab `YV_03_positioning` (sửa lỗi mô hình #1: bản cũ khai
      `TL_AUDIENCE_POSITIONING`, một dataset không tồn tại trong registry).
- [x] `external_writes=0`.
