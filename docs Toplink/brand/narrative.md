# TL-M3 — Cách kể chuyện Toplink Y Viện

> **Run 1 Phase A · chỉ chạy nội bộ · `external_writes=0`.** Xương sống kể chuyện, giọng thương hiệu
> và ranh giới cho founder, tất cả bị chặn bởi mức bằng chứng hiện có.
> `HYPOTHESIS · NOT_PUBLIC_APPROVED`.

## 0. Khối định danh

| Trường | Giá trị |
|---|---|
| Milestone | `TL-M3` |
| Stable ID | `TL-NARRATIVE-001` |
| Tab đích | `YV_04_narrative` |
| Schema | `YV-SHEET-001/1.0.0` |
| Trạng thái | `HYPOTHESIS · NOT_PUBLIC_APPROVED` |
| Nguồn sự thật | master plan §9 · `profile.json` `brand_voice` · taxonomy §1–3 |
| Ghi ra ngoài | `0` |

## 1. Xương sống kể chuyện

```text
Tín hiệu đời thường (đau mỏi, căng cứng, mệt mỏi)
một khoảng dừng để chăm sóc
lắng nghe và giải thích — KHÔNG chẩn đoán
lựa chọn hỗ trợ có giới hạn (đúng người, đúng cách, đúng thời điểm)
thói quen nhỏ, đều đặn
bước tiếp theo phù hợp, không gây áp lực
```

**Cấm lấp chỗ trống:** lịch sử nhượng quyền, thành tích hệ thống, chuẩn hay chứng nhận, và chuyên môn
của founder **không** được đưa vào mạch kể nếu chưa có nguồn kèm quyền nói công khai.

## 2. Bảng dữ liệu — `YV_04_narrative`

Quy ước bảng theo `dmp-profile.md §1`.

| Mã | Luật kể chuyện | Ranh giới | Ai giữ giọng | Cổng founder | Chủ sở hữu |
|---|---|---|---|---|---|
| TL-NAR-01 | Mở bằng một tín hiệu đời thường của cơ thể — đau mỏi, căng cứng, mệt mỏi | Mô tả cảm giác, không đặt tên bệnh, không quy nguyên nhân | Giọng thương hiệu | — | Hướng dẫn thương hiệu |
| TL-NAR-02 | Dẫn tới một khoảng dừng để chăm sóc, không dẫn tới một lời chào bán | Không đặt lời mời mua ở nhịp này | Giọng thương hiệu | — | Hướng dẫn thương hiệu |
| TL-NAR-03 | Lắng nghe và giải thích, tuyệt đối không chẩn đoán | Cấm mọi câu định danh bệnh hay chỉ ra nguyên nhân bệnh lý | Cổng sức khoẻ | Founder không được đứng ở nhịp này | Cổng sức khoẻ |
| TL-NAR-04 | Đưa ra lựa chọn hỗ trợ có giới hạn — đúng người, đúng cách, đúng thời điểm | Luôn kèm câu miễn trừ và lưu ý khác biệt giữa từng người | Cổng sức khoẻ | Founder không được chỉ định sản phẩm | Cổng sức khoẻ |
| TL-NAR-05 | Kết bằng một thói quen nhỏ, làm được đều đặn | Không hứa kết quả sau một mốc thời gian nào | Giọng thương hiệu | — | Hướng dẫn thương hiệu |
| TL-NAR-06 | Bước tiếp theo phải nhẹ, không tạo áp lực | Trước khi mở cổng chào bán, lời kêu gọi chỉ được là theo dõi Page, lưu bài, chia sẻ | Giọng thương hiệu | Không đặt hai lời kêu gọi thương mại do founder dẫn liền nhau | Hướng dẫn thương hiệu |
| TL-NAR-07 | Không lấp chỗ trống bằng lịch sử nhượng quyền, thành tích hệ thống, chuẩn, chứng nhận hay chuyên môn founder | Mỗi mảnh nội dung loại này cần nguồn kèm quyền nói công khai; chưa có thì bỏ trống, không viết thay | Cổng pháp lý | Chuyên môn founder nằm trong danh mục bị chặn | Cổng pháp lý |
| TL-NAR-08 | Giữ thang giọng trang trọng 6, năng lượng 3, hài hước 2, uy tín 6 | Không hạ xuống giọng bán hàng, không đẩy lên giọng bệnh viện | Hướng dẫn thương hiệu | — | Hướng dẫn thương hiệu |
| TL-NAR-09 | Giữ nhóm từ lõi: dưỡng sinh, lắng nghe cơ thể, làm ấm, thư giãn, phục hồi, cân bằng thân – tâm – trí | Không thay bằng từ y khoa lâm sàng, không thay bằng từ khuyến mãi | Hướng dẫn thương hiệu | — | Hướng dẫn thương hiệu |
| TL-NAR-10 | Không dùng: chữa khỏi, điều trị dứt điểm, khỏi 100%, thay thế thuốc, cam kết khỏi sau X ngày, chống ung thư | Vi phạm một từ là chặn cả bài, không sửa cục bộ rồi đăng | Cổng sức khoẻ | Áp dụng cho cả nội dung do founder dẫn | Cổng sức khoẻ |
| TL-NAR-11 | Nên dùng: hỗ trợ thư giãn, hỗ trợ lưu thông khí huyết, hỗ trợ giảm đau mỏi, góp phần cân bằng | Thêm chữ "hỗ trợ" không hợp thức hoá một khẳng định thiếu bằng chứng | Cổng sức khoẻ | — | Cổng sức khoẻ |
| TL-NAR-12 | Giọng thương hiệu là mặc định; founder chỉ xuất hiện có chọn lọc | Không để founder trở thành gương mặt chính của Page | Hướng dẫn thương hiệu | Trần tỷ trọng founder | Cổng pháp lý |
| TL-NAR-13 | Trần founder: tối đa 1 bài do founder dẫn trên mỗi 5 bài đã hoạch định | Trước khi có bằng chứng từ chu kỳ chạy thử, trần này không được nới | Hướng dẫn thương hiệu | Trần cứng, kiểm bằng máy | Cổng pháp lý |
| TL-NAR-14 | Không đặt hai lời kêu gọi thương mại do founder dẫn liền kề nhau | Kiểm trên cửa sổ trượt của lịch 28 ngày | Hướng dẫn thương hiệu | Cửa sổ trượt D-24 tới D-28 | Cổng pháp lý |
| TL-NAR-15 | Vai trò công khai của founder chỉ là "Founder / điều hành Toplink Y Viện" | Không thêm học hàm, học vị, chuyên môn hay chức danh nào khác | Cổng pháp lý | Chờ văn bản nếu muốn mở rộng | Cổng pháp lý |
| TL-NAR-16 | Founder không giải thích cơ chế, không chỉ định sản phẩm, không chẩn đoán, không nói thay người có chuyên môn | Bốn điều cấm này không có ngoại lệ | Cổng sức khoẻ | Cấm tuyệt đối | Cổng sức khoẻ |
| TL-NAR-17 | Đăng lại sang Facebook cá nhân của founder là một hành động ngoài phạm vi kế hoạch này | Cần duyệt riêng cho từng bài, không duyệt theo lô | Cổng pháp lý | Duyệt theo từng bài | Cổng pháp lý |
| TL-NAR-18 | Mỗi nhịp chạm tới sức khoẻ phải kèm câu miễn trừ và lưu ý khác biệt giữa từng người | Thiếu một trong hai là bài chưa đủ điều kiện đăng | Cổng sức khoẻ | — | Cổng sức khoẻ |
| TL-NAR-19 | Triệu chứng cấp hoặc nặng thì chuyển hướng tới nơi có chuyên môn, không đưa vào đường chuyển đổi | Không giữ người có dấu hiệu nặng lại trong luồng nội dung thương mại | Cổng sức khoẻ | — | Cổng sức khoẻ |
| TL-NAR-20 | Câu chuyện khách và nội dung do người dùng làm ra chỉ dùng khi có đồng ý bằng văn bản | Không khái quát một trường hợp thành bằng chứng kết quả | Cổng pháp lý | — | Cổng pháp lý |

## 3. VERIFY (TL-M3)

- [x] Xương sống khớp master plan §9; luật cấm lấp chỗ trống ghi thành dòng dữ liệu.
- [x] Giọng khoá theo hồ sơ; danh sách từ cấm và từ nên dùng chuyển thành dòng kiểm được bằng máy.
- [x] Ranh giới founder tách thành sáu dòng riêng (trần, vai trò, bốn điều cấm, cổng đăng lại).
- [x] Header khai đúng tab `YV_04_narrative` (sửa lỗi mô hình #1: bản cũ khai
      `TL_AUDIENCE_POSITIONING`, một dataset không tồn tại).
- [x] `external_writes=0`; không viết sẵn câu nào để đăng công khai.
