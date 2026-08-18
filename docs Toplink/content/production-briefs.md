# TL-M5 — Brief sản xuất bài viết (Toplink Y Viện)

> **Run 1 Phase A · chỉ chạy nội bộ · `external_writes=0`.** Tệp này giữ brief cho **16 mục dạng bài
> tĩnh và carousel**. 12 mục Reel nằm ở `reels-briefs.md`; hai tệp đổ chung vào một tab và phân biệt
> bằng cột `Loại brief`. Không mục nào `APPROVED`, không mục nào sẵn sàng đăng.

## 0. Khối định danh

| Trường | Giá trị |
|---|---|
| Milestone | `TL-M5` |
| Stable ID | `TL-M5-PRODBRIEF-001` |
| Tab đích | `YV_10_production_briefs` |
| Schema | `YV-SHEET-001/1.0.0` |
| Trạng thái | `LOCAL_VERIFIED` — chưa `APPROVED`, chưa ghi Sheet |
| Chu kỳ hiện tại | `C1` |
| Loại brief của tệp này | `Bài` — 16 dòng |
| Tệp anh em | `reels-briefs.md` — `Loại brief = Reel`, 12 dòng |
| Nguồn sự thật | `month-calendar.md §2` · `asset-and-batch-plan.md §2` · `kpi-experiment-plan.md §2` |
| Ghi ra ngoài | `0` |

## 1. Quy ước bảng

Theo `dmp-profile.md §1`, cộng bốn điều riêng cho tab brief:

1. **Chỉ hướng A có brief.** Mỗi dòng ở §2 là hướng A của một ngày. Hai hướng B và C được trình biên
   dịch sinh thêm dưới dạng dòng giữ chỗ mang `Trạng thái sản xuất = CHƯA CÓ BRIEF` và ô mở đầu
   `DỰ PHÒNG — `. Tab đủ 84 dòng, không dòng nào bị giấu (sửa lỗi mô hình #6).
2. **Năm cột riêng của Reel để `—` ở dòng bài**: `Thời lượng`, `Tỷ lệ khung`, `Lời thoại`, `Phụ đề`,
   `Vùng an toàn`.
3. **Cột `Câu claim dùng` mang mã `CL-*`** tra được ở `06_COMPLIANCE_RULES`; cột `Chỉ số theo dõi`
   mang **tên** chỉ số đúng như đã đặt ở `05_KPI_DICTIONARY`, không mang mã.
4. **Khung viết lời — không viết sẵn bản đăng.** Ô `Hook` và ô `Chữ trên hình` là câu gợi ý; bản đăng
   cuối cùng do chủ Y Viện viết và duyệt. Xưng hô theo bộ giọng: gọi khách là **chị** hoặc **anh**,
   thương hiệu tự gọi là **Y Viện** ở ngôi thứ ba, tuyệt đối không dùng "bạn" hay "quý khách".

**Tab này không có ô vàng.** Rủi ro của từng dòng đã có ô vàng đối ứng ở nơi sinh ra nó: cổng đồng ý ở
`YV_11_asset_batch_plan`, cổng người rà bài ở `YV_07_campaign`. Nhân bản ô vàng sang 84 dòng brief chỉ
làm loãng danh sách cần chốt.

## 2. Bảng dữ liệu — `YV_10_production_briefs` (phần `Bài`)

| Mã | Chu kỳ | Ngày | Hướng | Loại brief | Định dạng | Hook | Hình ảnh / shot | Chữ trên hình | Thời lượng | Tỷ lệ khung | Lời thoại | Phụ đề | Vùng an toàn | Kêu gọi | Câu claim dùng | Chỉ số theo dõi | Tiếp cận | Rủi ro / cổng | Trạng thái sản xuất | Chủ sở hữu |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TL-M5-PB-D2 | C1 | D-2 | A | Bài | Bài tĩnh | Y Viện không phải là gì | Thẻ đôi "là gì" và "không phải gì", nền ngà, chữ rượu vang | Chăm sóc chủ động, không thay thế y khoa | — | — | — | — | — | Theo dõi Page, lưu bài | CL-ID1 | Số người tiếp cận, Lượt lưu và lượt chia sẻ | Chữ tương phản cao, có mô tả ảnh | Không có rủi ro sức khoẻ; giữ nguyên câu ranh giới | Chưa dựng | Chủ Y Viện |
| TL-M5-PB-D4 | C1 | D-4 | A | Bài | Carousel | Thân, Tâm, Trí — và giới hạn đi kèm | Ba thẻ giá trị, thẻ thứ tư nói giới hạn | Ba trụ giá trị, một ranh giới | — | — | — | — | — | Lưu bài, chia sẻ | CL-M1, CL-ID1 | Lượt lưu và lượt chia sẻ | Chữ tương phản cao, có mô tả ảnh | Không nói công dụng, không cam kết kết quả | Chưa dựng | Hướng dẫn thương hiệu |
| TL-M5-PB-D5 | C1 | D-5 | A | Bài | Bài tĩnh | Một ý niệm rất đời | Ảnh founder từ tài sản AST-FOUNDER, đang chờ đồng ý | Câu ý niệm, không thêm chú thích chuyên môn | — | — | — | — | — | Theo dõi Page, lưu bài | CL-FD1 | Lượt lưu và lượt chia sẻ, Tín hiệu rủi ro | Chữ tương phản cao, có mô tả ảnh | Chặn tới khi có đồng ý bằng văn bản và phạm vi được nói của founder; cấm nói cơ chế, cấm chỉ định sản phẩm | Chặn bởi cổng đồng ý | Cổng pháp lý |
| TL-M5-PB-D6 | C1 | D-6 | A | Bài | Bài tĩnh | Tám bước, nói rõ ngay từ đầu | Thẻ liệt kê tám bước, ảnh quy trình từ AST-PROCESS-8S | Giải thích trước, làm sau | — | — | — | — | — | Lưu bài | CL-OP2 | Lượt lưu và lượt chia sẻ, Câu hỏi đúng chủ đề | Chữ tương phản cao, có mô tả ảnh | Chỉ nêu dữ kiện vận hành, cấm suy ra kết quả | Chưa dựng | Chủ Y Viện |
| TL-M5-PB-D9 | C1 | D-9 | A | Bài | Bài tĩnh | Lý – Dược – Dưỡng nói cho dễ hiểu | Đồ hoạ ba lớp từ AST-LDD-EXPLAIN | Ba lớp, kèm giới hạn ở thẻ cuối | — | — | — | — | — | Lưu bài | CL-M4 | Lượt lưu và lượt chia sẻ, Câu hỏi đúng chủ đề, Tín hiệu rủi ro | Chữ tương phản cao, có mô tả ảnh | Chạm sức khoẻ — cần người có chuyên môn rà; câu miễn trừ bắt buộc ở cuối phần mô tả | Chưa dựng | Cổng sức khoẻ |
| TL-M5-PB-D10 | C1 | D-10 | A | Bài | Carousel | Thói quen nhỏ, làm đều đặn | Năm thẻ thói quen, mỗi thẻ một hình minh hoạ đơn giản | Mỗi thẻ một thói quen làm được ngay | — | — | — | — | — | Lưu bài, chia sẻ | CL-M2 | Lượt lưu và lượt chia sẻ, Câu hỏi đúng chủ đề, Tín hiệu rủi ro | Chữ tương phản cao, có mô tả ảnh | Chạm sức khoẻ — chỉ nói mức hỗ trợ, cấm chẩn đoán; câu miễn trừ bắt buộc | Chưa dựng | Cổng sức khoẻ |
| TL-M5-PB-D12 | C1 | D-12 | A | Bài | Carousel | Đúng người, đúng cách, đúng thời điểm | Ba thẻ nguyên tắc, thẻ cuối nói nhóm cần thận trọng | Ba câu hỏi tự trả lời trước khi chọn | — | — | — | — | — | Lưu bài | CL-M4 | Lượt lưu và lượt chia sẻ, Câu hỏi đúng chủ đề, Tín hiệu rủi ro | Chữ tương phản cao, có mô tả ảnh | Chạm sức khoẻ — cần người có chuyên môn rà; câu miễn trừ bắt buộc | Chưa dựng | Cổng sức khoẻ |
| TL-M5-PB-D13 | C1 | D-13 | A | Bài | Bài tĩnh | Nhóm cần thận trọng | Thẻ lưu ý, nền ngà, viền cát | Bệnh nền, mang thai, có thiết bị cấy ghép | — | — | — | — | — | Lưu bài, chia sẻ | CL-M2 | Lượt lưu và lượt chia sẻ, Câu hỏi đúng chủ đề, Tín hiệu rủi ro | Chữ tương phản cao, có mô tả ảnh | Chạm sức khoẻ — nói bằng lời trấn an, không doạ; câu miễn trừ bắt buộc | Chưa dựng | Cổng sức khoẻ |
| TL-M5-PB-D16 | C1 | D-16 | A | Bài | Carousel | Giải thích trước khi làm | Tám thẻ bước, ảnh từ AST-PROCESS-8S | Tám bước, mỗi thẻ một bước | — | — | — | — | — | Lưu bài | CL-OP2, CL-M3 | Lượt lưu và lượt chia sẻ, Câu hỏi đúng chủ đề | Chữ tương phản cao, có mô tả ảnh | Chỉ nêu dữ kiện vận hành; cấm nói trình độ hay chứng chỉ của nhân sự | Chưa dựng | Chủ Y Viện |
| TL-M5-PB-D17 | C1 | D-17 | A | Bài | Bài tĩnh | Thơm dịu, sạch và yên | Ảnh chi tiết vệ sinh từ AST-HYGIENE | Quy chuẩn vệ sinh, nói bằng dữ kiện | — | — | — | — | — | Theo dõi Page, lưu bài | CL-OP3 | Số người tiếp cận, Lượt lưu và lượt chia sẻ | Chữ tương phản cao, có mô tả ảnh | Cấm dùng chữ đạt chuẩn nếu không nêu được chuẩn nào | Chưa dựng | Chủ Y Viện |
| TL-M5-PB-D19 | C1 | D-19 | A | Bài | Bài tĩnh | Nghỉ ngơi và chuyển hoá | Ảnh tầng ba và tầng bốn từ AST-SPACE-4F | Tên hai tầng Dưỡng và Tỉnh | — | — | — | — | — | Lưu bài | CL-OP1 | Lượt lưu và lượt chia sẻ | Chữ tương phản cao, có mô tả ảnh | Chỉ mô tả không gian, cấm suy ra kết quả sức khoẻ | Chưa dựng | Chủ Y Viện |
| TL-M5-PB-D20 | C1 | D-20 | A | Bài | Bài tĩnh | Đôi tay cộng một trái tim biết lắng nghe | Ảnh đào tạo và cộng đồng từ AST-FOUNDER | Giá trị của nghề có tâm | — | — | — | — | — | Theo dõi Page, chia sẻ | CL-FD1 | Lượt lưu và lượt chia sẻ, Tín hiệu rủi ro | Chữ tương phản cao, có mô tả ảnh | Chặn tới khi có đồng ý và phạm vi được nói của founder; cấm nói cơ chế | Chặn bởi cổng đồng ý | Cổng pháp lý |
| TL-M5-PB-D22 | C1 | D-22 | A | Bài | Bài tĩnh | Nhắc lại Y Viện là ai | Thẻ tóm tắt, dùng lại đồ hoạ nhận diện | Tóm định vị trong ba câu | — | — | — | — | — | Theo dõi Page, lưu bài | CL-ID1, CL-M1 | Lượt lưu và lượt chia sẻ | Chữ tương phản cao, có mô tả ảnh | Không rủi ro sức khoẻ; giữ nguyên câu ranh giới | Chưa dựng | Chủ Y Viện |
| TL-M5-PB-D24 | C1 | D-24 | A | Bài | Bài tĩnh | Từ ý niệm tới hôm nay | Ảnh cột mốc hành trình từ AST-FOUNDER | Lời cảm ơn gửi cộng đồng | — | — | — | — | — | Theo dõi Page, chia sẻ | CL-FD1 | Lượt lưu và lượt chia sẻ, Tín hiệu rủi ro | Chữ tương phản cao, có mô tả ảnh | Chặn tới khi có đồng ý và phạm vi được nói của founder | Chặn bởi cổng đồng ý | Cổng pháp lý |
| TL-M5-PB-D26 | C1 | D-26 | A | Bài | Carousel | Lý – Dược – Dưỡng, đúng nhu cầu | Ba thẻ nhắc lại, dùng lại đồ hoạ AST-LDD-EXPLAIN | Kể ở mức trải nghiệm, không nêu công dụng | — | — | — | — | — | Lưu bài | CL-CX1, CL-M4 | Lượt lưu và lượt chia sẻ, Câu hỏi đúng chủ đề, Tín hiệu rủi ro | Chữ tương phản cao, có mô tả ảnh | Quanh sản phẩm, đóng theo mặc định vì hồ sơ sản phẩm chưa kiểm chứng; chỉ kể trải nghiệm | Chặn bởi cổng hồ sơ sản phẩm | Cổng sức khoẻ |
| TL-M5-PB-D28 | C1 | D-28 | A | Bài | Bài tĩnh | Cùng nhau dưỡng sinh | Ảnh tổng kết bốn tuần, ghép lại từ tư liệu đã quay | Lời mời cộng đồng cùng đi tiếp | — | — | — | — | — | Theo dõi Page, lưu bài, chia sẻ | CL-FD1 | Người theo dõi mới, Lượt lưu và lượt chia sẻ | Chữ tương phản cao, có mô tả ảnh | Chặn tới khi có đồng ý và phạm vi được nói của founder | Chặn bởi cổng đồng ý | Cổng pháp lý |

## 3. Khung viết lời theo trụ

Đây là **khung**, không phải bản đăng. Cấu trúc chung: mở bằng một câu đời thường, một tới hai ý giá
trị ở mức hỗ trợ hoặc mức vận hành, một câu ranh giới, rồi lời mời theo dõi hoặc lưu bài. Mục chạm sức
khoẻ thêm câu miễn trừ ở cuối.

- **Trụ danh tính** — Y Viện là nơi chăm sóc cơ thể **chủ động**, bắt đầu từ việc lắng nghe. Y Viện
  **không** phải bệnh viện và không cam kết chữa khỏi. Mời chị theo dõi Page để chăm sóc đều đặn.
- **Trụ bằng chứng vận hành** — tại Y Viện, [tầng hoặc bước] được [mô tả bằng dữ kiện]. Giải thích vì
  sao trước khi đề xuất làm gì. Đây là điều chị thấy khi bước vào.
- **Trụ đọc hiểu cơ thể** *(chạm sức khoẻ)* — [cảm giác quen thuộc, không doạ]. Một vài thói quen nhỏ
  có thể **hỗ trợ thư giãn** và **hỗ trợ giảm cảm giác đau mỏi**. Nếu cảm giác kéo dài hoặc bất
  thường, chị nên hỏi ý kiến người có chuyên môn. *Kèm câu miễn trừ.*
- **Trụ Lý – Dược – Dưỡng** *(chạm sức khoẻ)* — Lý – Dược – Dưỡng là cách Y Viện sắp xếp việc chăm sóc
  **đúng người, đúng cách, đúng thời điểm**, với giới hạn rõ ràng. Nội dung mang tính giới thiệu trải
  nghiệm, không phải chỉ định sản phẩm. *Kèm câu miễn trừ.*
- **Trụ hành trình và cộng đồng** *(chặn bởi cổng đồng ý)* — [hành trình, triết lý, cộng đồng]. Cấm
  nói cơ chế, cấm chỉ định, cấm chẩn đoán.

**Câu miễn trừ chưa có nơi ở cố định** (`TL-R2-F08` đang mở). Trước khi chốt, câu miễn trừ đặt ngay
trong phần mô tả của chính bài đó, giữ nguyên văn bản đã có ở `reels-briefs.md §0`, và người có chuyên
môn phải xác nhận bản cuối trước khi đăng.

## 4. Ghép số đo

- Mục ở đầu phễu theo dõi số người tiếp cận, số lần hiển thị và người theo dõi mới.
- Mọi mục theo dõi lượt lưu và lượt chia sẻ; mục có tính giải thích theo dõi thêm câu hỏi đúng chủ đề.
- Mục chạm sức khoẻ **bắt buộc** theo dõi tín hiệu rủi ro — bình luận hiểu sai hoặc bị đẩy thành lời
  hứa chữa khỏi.
- Kỷ luật vận hành đo trên cả chu kỳ, không gắn vào từng bài.
- Chỉ số hỏi dịch vụ nghiêm túc **chưa đo** cho tới khi cổng chào bán mở.

## 5. VERIFY (TL-M5 brief bài viết)

- [x] 16 dòng dạng bài, đúng 16 mục không phải Reel của lịch nội dung.
- [x] Năm cột riêng của Reel để `—`, không để rỗng thật.
- [x] Lời kêu gọi chỉ gồm theo dõi Page, lưu bài, chia sẻ; không đặt lịch, không giá, không mua.
- [x] Mọi mục chạm sức khoẻ nêu rõ cần người có chuyên môn rà và cần câu miễn trừ.
- [x] Mục có founder chặn bởi cổng đồng ý; không mục nào nói cơ chế hay chỉ định sản phẩm.
- [x] `D-26` chỉ kể ở mức trải nghiệm; hồ sơ sản phẩm không được nâng lên mức đã kiểm chứng.
- [x] Xưng hô theo bộ giọng: gọi khách là chị hoặc anh, thương hiệu là Y Viện ngôi thứ ba; bỏ hết chữ
      "bạn" và chữ "Toplink" trong lời nói với khách.
- [x] Ngày đã chuẩn hoá về `D-1` … `D-28` (sửa lỗi mô hình #8).
- [x] Header khai đúng tab `YV_10_production_briefs` (sửa lỗi mô hình #1: bản cũ khai
      `TL_CONTENT_CALENDAR` và `TL_REELS_PRODUCTION`).
- [x] Hai hướng B và C được ghi rõ là chưa có brief thay vì bỏ im (sửa lỗi mô hình #6).
- [x] `external_writes=0`; không mục nào `APPROVED`.
