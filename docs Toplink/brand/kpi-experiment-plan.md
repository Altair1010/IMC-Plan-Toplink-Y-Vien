# TL-M4 — Từ điển chỉ số và vòng thử nghiệm (Toplink Y Viện)

> **Run 1 Phase A · chỉ chạy nội bộ · `external_writes=0`.** Page xuất phát từ số 0. Chỉ số đếm được
> phép ghi `0` **sau khi** đã có phép đo; chỉ số dạng tỷ lệ ghi `Chưa đủ mẫu` cho tới khi đủ mẫu số.
> **Tuyệt đối không báo phần trăm tăng trưởng tính từ mốc 0.** Dấu tích xanh không phải chỉ số niềm
> tin. Mức nhận biết là `NO_MEASUREMENT`, không phải bằng 0.

## 0. Khối định danh

| Trường | Giá trị |
|---|---|
| Milestone | `TL-M4` |
| Stable ID | `TL-KPI-001` |
| Tab đích | `05_KPI_DICTIONARY` (§2) và `YV_08_experiments` (§3) |
| Schema | `YV-SHEET-001/1.0.0` |
| Trạng thái | `LOCAL_VERIFIED` — chưa `APPROVED`, chưa ghi Sheet |
| Chu kỳ hiện tại | `C1` |
| Nguồn sự thật | master plan §17 · `facebook-page-strategy.md` nhóm `Mốc đo` · `campaign-architecture.md §2` |
| Ghi ra ngoài | `0` |

## 1. Luật đặt ngưỡng

Chu kỳ `C1` **không có dữ liệu lịch sử**, nên mọi ngưỡng đều là **luật so sánh trong nội bộ chu kỳ**,
không phải con số bịa ra:

- **Tiếp tục:** trung vị 7 ngày cuối cửa sổ ≥ trung vị 7 ngày đầu cửa sổ, và không có tín hiệu rủi ro.
- **Sửa:** hai cửa sổ ngang nhau hoặc dữ liệu mâu thuẫn — đổi **một** biến, chạy lại.
- **Dừng:** tín hiệu rủi ro tăng, hoặc xuất hiện một câu bị hiểu thành khẳng định chữa bệnh.

Từ `C2` trở đi, mốc xuất phát của mỗi chỉ số là giá trị đóng chu kỳ của `C1`, ghi ở `04_DECISIONS`.
Không chỉ số nào được ra quyết định trước khi đủ cỡ mẫu tối thiểu ghi ở §2.

## 2. Bảng dữ liệu — `05_KPI_DICTIONARY`

Quy ước bảng theo `dmp-profile.md §1`. Ô nền vàng nghĩa là còn một việc của người thật chưa làm.

| Mã | Chỉ số | Nghĩa là gì | Tính thế nào | Đo ở đâu | Ai theo dõi | Nhịp đo | Cỡ mẫu tối thiểu | Mốc xuất phát | Ngưỡng Tiếp tục | Ngưỡng Sửa | Ngưỡng Dừng | Cửa sổ đo | Trạng thái mẫu số | Chủ sở hữu |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TL-KPI-01 | Số người tiếp cận | Bao nhiêu tài khoản khác nhau nhìn thấy bài | Đếm trực tiếp trên nền tảng | Thống kê Page Facebook | Chủ Y Viện | Hằng tuần | Không cần — đây là số đếm | 0 sau khi chốt ảnh chụp danh tính Page | Trung vị 7 ngày cuối ≥ 7 ngày đầu | Hai nửa cửa sổ ngang nhau | Giảm liên tiếp hai cửa sổ | 7 ngày | Không áp dụng | Chủ Y Viện |
| TL-KPI-02 | Số lần hiển thị | Tổng số lần bài được hiện ra | Đếm trực tiếp trên nền tảng | Thống kê Page Facebook | Chủ Y Viện | Hằng tuần | Không cần — đây là số đếm | 0 sau khi chốt ảnh chụp danh tính Page | Trung vị 7 ngày cuối ≥ 7 ngày đầu | Hai nửa cửa sổ ngang nhau | Giảm liên tiếp hai cửa sổ | 7 ngày | Không áp dụng | Chủ Y Viện |
| TL-KPI-03 | Số lượt bắt đầu xem Reel | Bao nhiêu lần người xem bấm vào Reel | Đếm trực tiếp trên nền tảng | Thống kê Page Facebook | Chủ Y Viện | Hằng tuần | Không cần — đây là số đếm | 0 sau khi chốt ảnh chụp danh tính Page | Trung vị 7 ngày cuối ≥ 7 ngày đầu | Hai nửa cửa sổ ngang nhau | Giảm liên tiếp hai cửa sổ | 7 ngày | Không áp dụng | Chủ Y Viện |
| TL-KPI-04 | Lượt lưu và lượt chia sẻ | Người đọc thấy đủ hữu ích để giữ lại hoặc gửi cho người khác | Cộng lượt lưu và lượt chia sẻ của từng bài | Thống kê Page Facebook | Chủ Y Viện | Hằng tuần | 30 bài trước khi tính tỷ lệ | 0 sau khi chốt ảnh chụp danh tính Page | Trung vị 7 ngày cuối ≥ 7 ngày đầu | Hai nửa cửa sổ ngang nhau | Giảm liên tiếp hai cửa sổ | 7 ngày | Chưa đủ mẫu | Chủ Y Viện |
| TL-KPI-05 | Tỷ lệ xem hết Reel | Bao nhiêu phần người bấm vào đã xem tới cuối | Số lượt xem hết chia số lượt bắt đầu xem | Thống kê Page Facebook | Chủ Y Viện | Hằng tuần | 100 lượt bắt đầu xem | Chưa đủ mẫu | Trung vị 7 ngày cuối ≥ 7 ngày đầu | Hai nửa cửa sổ ngang nhau | Giảm liên tiếp hai cửa sổ | 14 ngày | Chưa đủ mẫu | Chủ Y Viện |
| TL-KPI-06 | Câu hỏi đúng chủ đề | Bình luận và tin nhắn hỏi về quy trình, mức phù hợp hoặc an toàn | Đếm tay, gắn nhãn theo chủ đề | Bình luận và hộp thư Page | Chủ Y Viện | Hằng tuần | Không cần — đây là số đếm | 0 sau khi chốt ảnh chụp danh tính Page | Trung vị 7 ngày cuối ≥ 7 ngày đầu | Hai nửa cửa sổ ngang nhau | Giảm liên tiếp hai cửa sổ | 7 ngày | Không áp dụng | Chủ Y Viện |
| TL-KPI-07 | Người theo dõi mới | Số người theo dõi tăng ròng | Đếm trực tiếp trên nền tảng | Thống kê Page Facebook | Chủ Y Viện | Hằng tuần | Không cần — đây là số đếm; cấm quy ra phần trăm | 0 người theo dõi | Trung vị 7 ngày cuối ≥ 7 ngày đầu | Hai nửa cửa sổ ngang nhau | Giảm liên tiếp hai cửa sổ | 7 ngày | Không áp dụng | Chủ Y Viện |
| TL-KPI-08 | Người quay lại tương tác | Tài khoản tương tác ở ít nhất hai cửa sổ đo | Đếm theo nhóm người, so giữa hai cửa sổ | Thống kê Page Facebook | Chủ Y Viện | Hằng tháng | Hai cửa sổ đo liên tiếp | Chưa đủ mẫu | Nhóm quay lại lớn hơn cửa sổ trước | Nhóm quay lại đứng yên | Nhóm quay lại co lại hai cửa sổ | 28 ngày | Chưa đủ mẫu | Chủ Y Viện |
| TL-KPI-09 | Hỏi dịch vụ nghiêm túc | Tin nhắn có ý định dùng dịch vụ thật | Đếm tay, gắn nhãn theo ý định | Hộp thư Page | Chủ Y Viện | Hằng tuần | Chỉ đo sau khi cổng chào bán mở | CHƯA CHỐT — chủ Y Viện cần mở cổng chào bán (dịch vụ cụ thể, điều kiện phù hợp, đầu mối, thời gian phản hồi, thông báo riêng tư) thì chỉ số này mới có mốc xuất phát | Chưa đo được | Chưa đo được | Chưa đo được | Chưa đặt | Chưa có mẫu số | Chủ Y Viện |
| TL-KPI-10 | Tín hiệu rủi ro | Bình luận hiểu sai thành khẳng định chữa bệnh, câu bị đẩy quá giới hạn, thời gian duyệt kéo dài | Đếm sự việc kèm số giờ chờ duyệt | Page và sổ duyệt nội bộ | Cổng sức khoẻ | Hằng tuần | Không cần — một sự việc cũng phải xử lý | 0 sau khi chốt ảnh chụp danh tính Page | Không có sự việc mới | Một sự việc, đã xử lý xong | Từ hai sự việc trở lên trong một cửa sổ | 7 ngày | Không áp dụng | Cổng sức khoẻ |
| TL-KPI-11 | Kỷ luật vận hành | Đăng đúng lịch, trả lời đúng hẹn, số lần trượt cổng duyệt | Đếm số việc đúng hẹn trên tổng số việc | Sổ sản xuất nội bộ | Chủ Y Viện | Hằng tuần | Một tuần đầy đủ | 0 sau khi chốt ảnh chụp danh tính Page | Từ 80 phần trăm đúng hẹn trở lên | Từ 60 tới dưới 80 phần trăm | Dưới 60 phần trăm | 7 ngày | Chưa đủ mẫu | Chủ Y Viện |
| TL-KPI-12 | Mức nhận biết thương hiệu | Bao nhiêu người trong nhóm khách mục tiêu biết tới Y Viện | Chưa có cách tính nào được chọn | Chưa có nơi đo | Chủ Y Viện | Chưa đặt | Chưa đặt | CHƯA CHỐT — chủ Y Viện cần chọn cách đo mức nhận biết (khảo sát nhỏ, hỏi trực tiếp tại cơ sở, hoặc bỏ chỉ số này khỏi chu kỳ). Chưa chọn thì giữ nguyên trạng thái không đo | Chưa đo được | Chưa đo được | Chưa đo được | Chưa đặt | Chưa có mẫu số | Chủ Y Viện |

**Nhóm chỉ số:** phân phối (01–03) · tính hữu ích (04, 06) · sự chú ý (05) · quan hệ (07–08) · ý định
(09, đang khoá) · rủi ro (10) · vận hành (11) · nhận biết (12, chưa đo).

## 3. Bảng dữ liệu — `YV_08_experiments`

Đây là **nguồn duy nhất** cho tab thử nghiệm; `campaign-architecture.md` không lặp lại bảng này.
Mỗi thử nghiệm đổi **đúng một** biến. Không thử nghiệm nào được gắn vào một khẳng định sức khoẻ.

| Mã | Chu kỳ | Thuộc giai đoạn | Giả thuyết | Biến thay đổi | Mức bằng chứng | Đo bằng cách nào | Cửa sổ quan sát | Dấu hiệu Tiếp tục | Dấu hiệu Sửa | Dấu hiệu Dừng | Kết luận | Chốt ở quyết định nào | Chủ sở hữu |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TL-EXP-01 | C1 | Tuần 1 | Mở bài bằng một câu hỏi đời thường giữ người đọc lâu hơn mở bài bằng chi tiết không gian | Kiểu câu mở bài — câu hỏi hay chi tiết không gian; mọi thứ khác giữ nguyên | HYPOTHESIS | Lượt lưu và lượt chia sẻ trên mỗi bài, so giữa hai nửa tuần | 7 ngày | Nhánh câu hỏi có trung vị lượt lưu cao hơn ở nửa sau | Hai nhánh ngang nhau | Bình luận hiểu sai thành khẳng định chữa bệnh | Chưa chạy | Chốt chu kỳ C1 | Chủ Y Viện |
| TL-EXP-02 | C1 | Tuần 3 | Reel hậu trường không gian giúp người lạ tìm thấy Page tốt hơn ảnh tĩnh cùng nội dung | Định dạng — ảnh tĩnh hay Reel; cùng góc kể, cùng lời kêu gọi | HYPOTHESIS | Số người tiếp cận và số người theo dõi mới trong 24 giờ đầu mỗi bài | 7 ngày | Nhánh Reel có trung vị tiếp cận cao hơn | Hai nhánh ngang nhau, hoặc Reel hơn nhưng lượt lưu kém hơn | Năng lực sản xuất Reel không theo kịp lịch đăng | Chưa chạy | Chốt chu kỳ C1 | Chủ Y Viện |
| TL-EXP-03 | C1 | Tuần 4 | Tăng phần bằng chứng vận hành so với phần giáo dục giữ chân người theo dõi tốt hơn | Cơ cấu trụ trong tuần — nghiêng giáo dục hay nghiêng bằng chứng vận hành | HYPOTHESIS | Người quay lại tương tác và lượt lưu trên mỗi bài | 7 ngày | Nhánh nghiêng bằng chứng vận hành có nhóm quay lại lớn hơn | Hai nhánh ngang nhau | Tín hiệu rủi ro tăng ở nhánh nào thì dừng nhánh đó | Chưa chạy | Chốt chu kỳ C1 | Chủ Y Viện |

Cột `Chốt ở quyết định nào` trỏ về dòng `Chốt chu kỳ C1` ở `04_DECISIONS` — dòng này tồn tại sẵn với
trạng thái chưa tới hạn, để không có tham chiếu treo.

## 4. Luật bảo vệ chỉ số

- Chỉ số ý định (`TL-KPI-09`) **không đo** cho tới khi cổng chào bán mở. Cổng này hiện chưa tồn tại.
- Lượt lưu, lượt chia sẻ và câu hỏi đúng chủ đề là **tín hiệu để học**, không phải bằng chứng "đã có
  niềm tin".
- Mọi chỉ số dạng tỷ lệ hiện `Chưa đủ mẫu` cho tới khi đạt cỡ mẫu tối thiểu; khi báo tỷ lệ phải báo
  kèm mẫu số.
- Bài chạm sức khoẻ ghi thêm mã claim, mức rủi ro, kết quả kiểm tra tự động, người duyệt và điều kiện
  kèm theo vào sổ duyệt. Không có mặc định "trống nghĩa là đã duyệt".
- Dấu tích xanh không vào từ điển chỉ số.

## 5. VERIFY (TL-M4 chỉ số)

- [x] Mỗi chỉ số có nghĩa, cách tính, nơi đo, người theo dõi, nhịp đo, cỡ mẫu tối thiểu.
- [x] Ngưỡng Tiếp tục / Sửa / Dừng là luật so sánh nội bộ chu kỳ, không phải con số bịa.
- [x] Số đếm bắt đầu từ 0 sau khi có phép đo; tỷ lệ ghi `Chưa đủ mẫu`; không phần trăm từ mốc 0.
- [x] Chỉ số ý định bị khoá sau cổng chào bán; mức nhận biết vẫn chưa có phép đo.
- [x] Ba thử nghiệm, mỗi thử nghiệm đúng một biến, không thử nghiệm nào gắn vào khẳng định sức khoẻ.
- [x] Cột `Chốt ở quyết định nào` trỏ về một dòng có thật ở `04_DECISIONS` (không tham chiếu treo).
- [x] Header khai đúng hai tab đích (sửa lỗi mô hình #1: bản cũ khai `TL_CAMPAIGN_KPI`, một dataset
      không tồn tại).
- [x] Hai ô vàng (`TL-KPI-09`, `TL-KPI-12`) mở đầu bằng `CHƯA CHỐT — `, mỗi ô có đúng một dòng đối
      ứng ở `00_Y_VIEN_CAN_CHOT`.
- [x] `external_writes=0`.
