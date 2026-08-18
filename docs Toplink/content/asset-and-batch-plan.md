# TL-M5 — Kế hoạch tài sản và mẻ sản xuất (Toplink Y Viện)

> **Run 1 Phase A · chỉ chạy nội bộ · `external_writes=0`.** Phản ánh **năng lực sản xuất thật** đã
> chốt. **Toàn bộ tài sản ở đây là yêu cầu cần quay hoặc chuẩn bị mới** — không tệp nào trỏ tới thư
> viện có sẵn, không dòng nào ngụ ý đã có quyền sử dụng. Việc chọn và làm sạch quyền cho một tài sản
> thật là hành động diễn ra **sau** khi cổng quyền sử dụng đạt.

## 0. Khối định danh

| Trường | Giá trị |
|---|---|
| Milestone | `TL-M5` |
| Stable ID | `TL-M5-ASSET-001` |
| Tab đích | `YV_11_asset_batch_plan` |
| Schema | `YV-SHEET-001/1.0.0` |
| Trạng thái | `LOCAL_VERIFIED` — chưa `APPROVED`, chưa ghi Sheet |
| Chu kỳ hiện tại | `C1` |
| Năng lực đã chốt | Khoảng 3 video mỗi tuần · ít nhất 1 mục mỗi ngày · 28 mục trong 28 ngày · 12 Reel · 16 bài tĩnh hoặc carousel |
| Thời gian chuẩn bị video | 2 ngày, tính từ lúc quay tới lúc sẵn sàng đăng |
| Nguồn sự thật | Bản chốt năng lực sản xuất · `content-pillars.md §2` · `reels-briefs.md` |
| Ghi ra ngoài | `0` |

## 1. Quy ước bảng

Theo `dmp-profile.md §1`. Bảng ở §2 chứa **hai loại dòng** trong cùng một tab:

- Dòng **tài sản** để `—` ở cột `Sức chứa mẻ`.
- Dòng **mẻ sản xuất** để `—` ở các cột `Loại tài sản`, `Quyền sử dụng`, `Đồng ý của người xuất hiện`.

Ngày ghi theo dạng tương đối `D-1` … `D-28`, không zero-pad, đúng như lịch nội dung. Ô nền vàng nghĩa
là còn một việc của người thật chưa làm.

## 2. Bảng dữ liệu — `YV_11_asset_batch_plan`

| Mã | Chu kỳ | Mẻ sản xuất | Dùng cho ngày nào | Loại tài sản | Mô tả | Sức chứa mẻ | Quyền sử dụng | Đồng ý của người xuất hiện | Trạng thái | Chủ sở hữu |
|---|---|---|---|---|---|---|---|---|---|---|
| AST-SPACE-4F | C1 | Mẻ tuần 1 và mẻ tuần 3 | D-3, D-15, D-19 | Video và ảnh không gian | Cảnh cắt bốn tầng Tĩnh, Thông, Dưỡng, Tỉnh; quay hình thật của Y Viện | — | Chưa xác lập — phải quay mới, không dùng lại tư liệu cũ | Không có người xuất hiện | Chưa quay | Chủ Y Viện |
| AST-PROCESS-8S | C1 | Mẻ tuần 3 | D-6, D-16 | Video và ảnh quy trình | Minh hoạ tám bước tiếp nhận, có xin phép và giải thích tại chỗ | — | Chưa xác lập — phải quay mới | Cần đồng ý nếu có nhân viên trong khung hình | Chưa quay | Chủ Y Viện |
| AST-HYGIENE | C1 | Mẻ tuần 3 | D-17, D-21 | Ảnh và video vệ sinh | Quy chuẩn vệ sinh và các chi tiết cho thấy sự chỉn chu | — | Chưa xác lập — phải quay mới | Không có người xuất hiện | Chưa quay | Chủ Y Viện |
| AST-TEAM-BTS | C1 | Mẻ tuần 3 | D-18, D-20 | Video hậu trường | Đội ngũ chuẩn bị; tuyệt đối không nêu bằng cấp hay chuyên môn của ai | — | Chưa xác lập — phải quay mới | CHƯA CHỐT — chủ Y Viện cần lấy đồng ý bằng văn bản của từng người xuất hiện, nêu rõ mục đích, kênh đăng, thời hạn và cách rút lại. Chưa có thì bỏ hết phần con người, chỉ giữ không gian | Chặn bởi cổng đồng ý | Cổng pháp lý |
| AST-BODY-LIT | C1 | Mẻ tuần 2 và mẻ tuần 4 | D-8, D-10, D-11, D-13, D-23, D-27 | Video và đồ hoạ giải thích | Minh hoạ tín hiệu cơ thể; giải thích không doạ, không chẩn đoán | — | Chưa xác lập — phải dựng mới | Không có người xuất hiện | Chưa dựng | Cổng sức khoẻ |
| AST-LDD-EXPLAIN | C1 | Không thuộc mẻ quay | D-9, D-12, D-26 | Đồ hoạ và carousel | Giải thích Lý – Dược – Dưỡng ở mức trải nghiệm; cấm mọi khẳng định công dụng | — | Chưa xác lập — phải dựng mới | Không có người xuất hiện | Chưa dựng | Cổng sức khoẻ |
| AST-CX-DUONGLIEU | C1 | Mẻ tuần 2 | D-14 | Video trải nghiệm | Kể ở mức trải nghiệm khách hàng vì hồ sơ sản phẩm chưa kiểm chứng | — | Chưa xác lập — phải quay mới | Cần đồng ý nếu có khách trong khung hình | Chặn bởi cổng hồ sơ sản phẩm | Cổng sức khoẻ |
| AST-FOUNDER | C1 | Mẻ tuần 1 và mẻ tuần 4 | D-5, D-24 | Video và ảnh founder | Hành trình và triết lý của founder; cấm cơ chế, cấm chỉ định sản phẩm | — | Chưa xác lập — phải quay mới | CHƯA CHỐT — chủ Y Viện cần xác nhận phạm vi được nói của founder bằng văn bản và ký đồng ý cho hình ảnh. Chưa có thì hai ngày này chuyển sang nội dung không có founder | Chặn bởi cổng đồng ý | Cổng pháp lý |
| AST-BRAND-ID | C1 | Không thuộc mẻ quay | D-1, D-2, D-4, D-7, D-22, D-25, D-28 | Đồ hoạ nhận diện | Định vị và cặp "là gì, không phải gì"; dùng bảng màu ngà, rượu vang, đồng | — | Chưa xác lập — phải dựng mới | Không có người xuất hiện | Chưa dựng | Hướng dẫn thương hiệu |
| B-W1 | C1 | Mẻ tuần 1 | D-1, D-3, D-7 | — | Gom quay không gian và phần giới thiệu thương hiệu trong một buổi | 3 video, quay xong trước D-1 ít nhất 2 ngày | — | — | Chưa quay | Chủ Y Viện |
| B-W2 | C1 | Mẻ tuần 2 | D-8, D-11, D-14 | — | Gom quay phần đọc hiểu cơ thể và phần trải nghiệm trong một buổi | 3 video, quay xong trước D-8 ít nhất 2 ngày, và phải qua người có chuyên môn rà trước khi đăng | — | — | Chưa quay | Cổng sức khoẻ |
| B-W3 | C1 | Mẻ tuần 3 | D-15, D-18, D-21 | — | Gom quay không gian bốn tầng và hậu trường đội ngũ trong một buổi | 3 video, quay xong trước D-15 ít nhất 2 ngày, và phải có đồng ý của người xuất hiện | — | — | Chưa quay | Cổng pháp lý |
| B-W4 | C1 | Mẻ tuần 4 | D-23, D-25, D-27 | — | Gom quay phần khép chu kỳ; dùng lại khung cũ, chỉ quay mới phần thiếu | 3 video, quay xong trước D-22 ít nhất 2 ngày | — | — | Chưa quay | Chủ Y Viện |
| TL-BATCH-ROLE | C1 | Áp dụng cho cả bốn mẻ | D-1 … D-28 | — | Phân vai sản xuất: ai quay, ai dựng, ai duyệt | Mặc định một người làm hết cho tới khi có phân vai | — | — | CHƯA CHỐT — chủ Y Viện cần chốt ai quay, ai dựng và ai duyệt. Chưa chốt thì mặc định một người kiêm hết, và mọi cam kết về nhịp đăng chỉ là ước lượng | Chủ Y Viện |

**16 bài tĩnh và carousel** sản xuất trong ngày, dùng bộ đồ hoạ nhận diện và bộ đồ hoạ giải thích ở
trên, không cần mẻ quay riêng.

## 3. Ràng buộc khi dựng

- Ưu tiên cắt đơn giản, phụ đề rõ, vùng an toàn chuẩn khung dọc 9:16. Tránh hiệu ứng chuyển động nặng.
- Mọi Reel bắt buộc có phụ đề. Mục chạm sức khoẻ phải để câu miễn trừ đủ lâu để đọc hết.
- Không dùng tài sản do máy sinh ra trong chu kỳ này.
- Bất kỳ câu chuyện khách hàng, nội dung do người dùng làm ra, hay người thật xuất hiện đều cần đồng ý
  bằng văn bản trước khi dùng: nêu rõ mục đích, kênh đăng, thời hạn, cách rút lại và cách che thông
  tin. **Hiện chưa có đồng ý nào.**

## 4. VERIFY (TL-M5 tài sản và mẻ sản xuất)

- [x] Năng lực phản ánh đúng bản chốt thật; thiếu phân vai thì ghi thành một dòng cần chốt, không điền giả.
- [x] Toàn bộ tài sản chưa xác lập quyền sử dụng; không dòng nào chọn, dùng lại hay ngụ ý đã có quyền.
- [x] Cổng đồng ý nêu rõ cho hậu trường đội ngũ và cho founder; chưa có đồng ý nào.
- [x] Mẻ sản xuất tôn trọng thời gian chuẩn bị 2 ngày; mẻ tuần 2 chờ người có chuyên môn rà trước khi đăng.
- [x] Ngày đã chuẩn hoá về dạng `D-1` … `D-28`, bỏ hết dạng zero-pad (sửa lỗi mô hình #8).
- [x] Header khai đúng tab `YV_11_asset_batch_plan` (sửa lỗi mô hình #1: bản cũ khai
      `TL_REELS_PRODUCTION`, một dataset không tồn tại).
- [x] Ba ô vàng (`AST-TEAM-BTS`, `AST-FOUNDER`, `TL-BATCH-ROLE`) mở đầu bằng `CHƯA CHỐT — `, mỗi ô có
      đúng một dòng đối ứng ở `00_Y_VIEN_CAN_CHOT`.
- [x] `external_writes=0`; không mục nào `APPROVED`.
