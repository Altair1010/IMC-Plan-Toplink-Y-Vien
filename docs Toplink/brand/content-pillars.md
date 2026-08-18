# TL-M3 — Trụ nội dung Toplink Y Viện

> **Run 1 Phase A · chỉ chạy nội bộ · `external_writes=0`.** Năm trụ nội dung hội tụ từ năm vùng đề
> tài ứng viên (master plan §10). Phân bổ biểu diễn bằng số slot trên kế hoạch 28 slot; đây là giả
> thuyết khởi động, sẽ cân chỉnh lại sau tín hiệu của chu kỳ chạy thử.

## 0. Khối định danh

| Trường | Giá trị |
|---|---|
| Milestone | `TL-M3` |
| Stable ID | `TL-PILLARS-001` |
| Tab đích | `YV_05_content_pillars` |
| Schema | `YV-SHEET-001/1.0.0` |
| Trạng thái | `HYPOTHESIS` — giả thuyết khởi động, chưa `APPROVED` |
| Số dòng | **đúng 5**, không hơn không kém (sửa lỗi mô hình #9: registry cũ cho `min_records = 3`) |
| Nguồn sự thật | master plan §10 · taxonomy §1–2 · `positioning.md §2` |
| Ghi ra ngoài | `0` |

## 1. Quy tắc quy đổi slot sang tỷ trọng %

Slot là sự thật gốc: **6 / 6 / 8 / 4 / 4 = 28**. Tỷ trọng % là số nguyên, tổng **đúng 100**, quy đổi
bằng phương pháp phần dư lớn nhất:

- Lấy phần nguyên: 21 · 21 · 28 · 14 · 14 = 98.
- Còn dư 2 điểm phần trăm, chia cho hai phần dư lớn nhất: `TL-P3` (0,5714) rồi `TL-P1` (0,4286 —
  hoà với `TL-P2`, phá hoà theo thứ tự trụ).
- Kết quả: **22 · 21 · 29 · 14 · 14 = 100**.

Quy tắc này là tất định; chạy lại cho ra đúng bộ số này.

## 2. Bảng dữ liệu — `YV_05_content_pillars`

Quy ước bảng theo `dmp-profile.md §1`. Cột `Slot` là cột máy phục vụ ánh xạ lịch, không hiển thị.

| Mã | Trụ nội dung | Tỷ trọng % | Số ngày trong chu kỳ | Giải quyết việc gì cho khách | Định dạng hay dùng | Vai trò trong phễu | Rủi ro / cổng | Vì sao có trụ này | Chủ sở hữu |
|---|---|---|---|---|---|---|---|---|---|
| TL-P1 | Y Viện là ai — phạm vi và giới hạn | 22 | 6 | Giúp người mới hiểu Y Viện là gì và không phải là gì trước khi tin bất cứ điều gì khác | Bài Facebook và Reel giới thiệu | TOFU | Trung bình — cấm ngôn từ nhượng quyền và pháp lý công khai; tick xanh chỉ là tín hiệu định danh nền tảng, không phải bằng chứng năng lực | Đây là nền móng; mọi khẳng định khác chỉ đứng được khi người đọc đã biết phạm vi của Y Viện | Hướng dẫn thương hiệu |
| TL-P2 | Hiểu và lắng nghe tín hiệu cơ thể | 21 | 6 | Giúp người đọc đọc được tín hiệu cơ thể mình và bớt lo lắng | Carousel và Reel giáo dục | TOFU | Cao — cấm ngôn từ nhân quả và chẩn đoán; bắt buộc câu miễn trừ, lưu ý khác biệt cá nhân, và người có chuyên môn rà từng bài chứ không rà theo lô | Đây là giá trị lõi nhưng bị chặn bởi cổng sức khoẻ, nên giữ nguyên 6 trên 28 slot | Cổng sức khoẻ |
| TL-P3 | Bằng chứng vận hành: không gian, quy trình, con người | 29 | 8 | Cho người đang cân nhắc thấy sự chỉn chu và minh bạch bằng thứ kiểm chứng được | Ảnh và video tham quan, Reel hậu trường | MOFU | Thấp — chỉ nói dữ kiện vận hành; không gắn bằng cấp nhân sự, không nói kết quả, không dùng lời khách khi chưa có đồng ý | Đây là tài sản kiểm chứng được và rủi ro thấp nhất, nên nhận phần lớn nhất trong 28 slot | Chủ Y Viện |
| TL-P4 | Lý – Dược – Dưỡng dễ hiểu | 14 | 4 | Giúp người đọc hiểu hệ giải pháp trước khi chọn | Bài giải thích và Reel giải thích | MOFU | Trung bình cao — cấm mọi khẳng định công dụng cho tới khi có hồ sơ sản phẩm; bắt buộc câu miễn trừ, lưu ý khác biệt cá nhân và rà soát từng bài | Giữ ở mức thấp cho tới khi hồ sơ sản phẩm đạt, vì công dụng theo từng sản phẩm vẫn chưa kiểm chứng | Cổng sức khoẻ |
| TL-P5 | Hành trình Y Viện, founder và cộng đồng | 14 | 4 | Cho người đã biết Y Viện một lý do để ở lại và quay lại | Story và Reel kể chuyện | TOFU | Trung bình — trần founder tối đa 1 trên mỗi 5 bài; không đặt hai lời kêu gọi thương mại do founder dẫn liền kề; không nói cơ chế, không chẩn đoán; cần đồng ý của người xuất hiện | Bị giới hạn bởi ranh giới founder, nên giữ ở 4 trên 28 slot | Cổng pháp lý |

**Tổng: 100% · 28/28 slot.** Cơ chế lịch phản chiếu 6/6/8/4/4.

## 3. Vai trò trong phễu

- **TOFU (nhận biết):** `TL-P1` · `TL-P2` · `TL-P5`
- **MOFU (cân nhắc):** `TL-P3` · `TL-P4`
- **BOFU (ra quyết định):** *không có trụ nào* — lời kêu gọi thương mại đang tắt cho tới khi cổng
  chào bán được mở.

Mặc định: không BOFU, không lời kêu gọi thương mại. Bài chạm sức khoẻ bị chặn theo từng bài. Ranh giới
founder áp theo từng bài.

## 4. Kiểm trần founder

Tỷ trọng founder hiện tại = 4/28 = **14,3%**, dưới trần 20%, và chưa có lời kêu gọi thương mại nào do
founder dẫn. Cửa sổ trượt `D-24`…`D-28` vẫn chứa `D-24` và `D-28`. Việc giữ hay đổi `D-28` trước khi
có lịch đăng thật là **cổng người**; đồng ý của người xuất hiện và duyệt theo từng bài vẫn bắt buộc.

## 5. VERIFY (TL-M3)

- [x] Đúng 5 trụ, giữ nguyên mã, việc cần giải, mức bằng chứng, vai trò phễu, rủi ro và thứ tự nhấn.
- [x] Phân bổ 6/6/8/4/4 phủ đủ 28 slot; tỷ trọng % tổng đúng 100 theo quy tắc tất định ở §1.
- [x] Trụ chạm sức khoẻ (`TL-P2`, `TL-P4`) bị chặn theo từng bài.
- [x] Ranh giới founder (`TL-P5`) tách thành điều kiện kiểm được.
- [x] Giữ mặc định không BOFU, không lời kêu gọi thương mại.
- [x] Không phát sinh khẳng định công dụng mới; giữ nguyên mọi nhãn bằng chứng.
- [x] Chuyển từ dạng bullet sang bảng để `parse_markdown_tables()` đọc được.
- [x] `external_writes=0`.
