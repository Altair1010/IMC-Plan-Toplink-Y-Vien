# TL-M3 — Chiến lược Facebook Page & mốc đo (Toplink Y Viện)

> **Run 1 Phase A · chỉ chạy nội bộ · `external_writes=0`.** Facebook Page là kênh chính, Reels hỗ
> trợ. Page xuất phát từ con số 0 (follower `0`, nhận biết `NO_MEASUREMENT`).

## 0. Khối định danh

| Trường | Giá trị |
|---|---|
| Milestone | `TL-M3` |
| Stable ID | `TL-PAGE-STRATEGY-001` |
| Tab đích | `YV_06_page_strategy` |
| Schema | `YV-SHEET-001/1.0.0` |
| Trạng thái | `LOCAL_VERIFIED` — chưa `APPROVED`, chưa ghi Sheet |
| Nguồn sự thật | master plan §11 · `profile.json` `channels` · `content-pillars.md §2` |
| Nhóm gộp | `Chiến lược` + `Mốc đo` (hai dataset cũ gộp về một tab, phân biệt bằng cột `Nhóm`) |
| Ghi ra ngoài | `0` |

## 1. Quy ước ô trống theo nhóm

Dòng nhóm `Chiến lược` để `—` ở `Giá trị đo`, `Mẫu số`, `Thời điểm đo`. Dòng nhóm `Mốc đo` để `—` ở
`Tỷ trọng %`, `Trụ liên quan`. Không để chuỗi rỗng thật — đọc lại từ Sheet cần một chuỗi xác định.

Cột `Trụ liên quan` trỏ về cột `Trụ nội dung` của `YV_05_content_pillars` bằng **tên tiếng Việt đầy
đủ**, không dùng mã trụ — mã kỹ thuật không được xuất hiện ở cột hiển thị.

## 2. Bảng dữ liệu — `YV_06_page_strategy`

| Mã | Nhóm | Hạng mục | Kênh | Vai trò | Tỷ trọng % | Trụ liên quan | Giá trị đo | Mẫu số | Thời điểm đo | Trạng thái | Chủ sở hữu |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TL-PS-01 | Chiến lược | Vai trò kênh | Facebook Page Toplink Y Viện | Danh tính thương hiệu, giáo dục, bằng chứng vận hành, tín hiệu cộng đồng | — | — | — | — | — | Kênh chính | Chủ Y Viện |
| TL-PS-02 | Chiến lược | Vai trò kênh | Reels trên Facebook | Giúp người lạ tìm thấy Y Viện, giữ chân, giải thích ngắn | — | — | — | — | — | Kênh hỗ trợ | Chủ Y Viện |
| TL-PS-03 | Chiến lược | Vai trò kênh | Facebook cá nhân của founder | Bối cảnh founder có chọn lọc, đăng lại có kiểm soát | — | — | — | — | — | Duyệt theo từng bài | Cổng pháp lý |
| TL-PS-04 | Chiến lược | Vai trò kênh | Website, Zalo, điện thoại, Google Maps | Vai trò chuyển đổi — chưa đấu nối, chưa được đưa vào bất kỳ lời kêu gọi nào | — | — | — | — | — | Chờ đầu vào | Chủ Y Viện |
| TL-PS-05 | Chiến lược | Vai trò kênh | TikTok | Chỉ tham chiếu cơ chế, không mở kênh trong chu kỳ này | — | — | — | — | — | Chỉ để tham khảo | Chủ Y Viện |
| TL-PS-06 | Chiến lược | Nhịp đăng | Facebook Page Toplink Y Viện | Mục tiêu 1 tới 2 bài mỗi ngày, chặn trên bởi năng lực sản xuất thật | — | — | — | — | — | Giả thuyết khởi động | Chủ Y Viện |
| TL-PS-07 | Chiến lược | Nhịp đăng | Reels trên Facebook | Từ 2 tới 3 Reel mỗi tuần, chỉ mở sau khi xác nhận năng lực sản xuất | — | — | — | — | — | Chờ xác nhận năng lực | Chủ Y Viện |
| TL-PS-08 | Chiến lược | Nhịp đăng | Facebook Page Toplink Y Viện | Toàn bộ lịch dùng ngày tương đối từ D-1 tới D-28; không có ngày tuyệt đối nào | — | — | — | — | — | Ngày bắt đầu chưa đặt | Chủ Y Viện |
| TL-PS-09 | Chiến lược | Cơ cấu nội dung | Facebook Page Toplink Y Viện | Giáo dục và đọc hiểu tín hiệu cơ thể | 40 | Hiểu và lắng nghe tín hiệu cơ thể, Lý – Dược – Dưỡng dễ hiểu | — | — | — | Chặn theo từng bài vì chạm sức khoẻ | Cổng sức khoẻ |
| TL-PS-10 | Chiến lược | Cơ cấu nội dung | Facebook Page Toplink Y Viện | Bằng chứng vận hành và niềm tin | 30 | Bằng chứng vận hành: không gian, quy trình, con người | — | — | — | Mở | Chủ Y Viện |
| TL-PS-11 | Chiến lược | Cơ cấu nội dung | Facebook Page Toplink Y Viện | Danh tính và phạm vi thương hiệu | 20 | Y Viện là ai — phạm vi và giới hạn | — | — | — | Mở | Hướng dẫn thương hiệu |
| TL-PS-12 | Chiến lược | Cơ cấu nội dung | Facebook Page Toplink Y Viện | Founder và cộng đồng, tối đa 1 bài do founder dẫn trên mỗi 5 bài | 10 | Hành trình Y Viện, founder và cộng đồng | — | — | — | Chặn bởi trần founder | Cổng pháp lý |
| TL-PS-13 | Chiến lược | Cách trả lời | Facebook Page Toplink Y Viện | Bình luận và tin nhắn hỏi về mức độ phù hợp hay an toàn thì trả lời ở mức hỗ trợ kèm câu miễn trừ | — | — | — | — | — | Chặn mặc định | Cổng sức khoẻ |
| TL-PS-14 | Chiến lược | Cách trả lời | Facebook Page Toplink Y Viện | Triệu chứng đáng lo hoặc cấp tính thì chuyển tới nơi có chuyên môn, tuyệt đối không dẫn vào đường chuyển đổi | — | — | — | — | — | Chặn mặc định | Cổng sức khoẻ |
| TL-PS-15 | Chiến lược | Cách trả lời | Facebook Page Toplink Y Viện | Người hỏi chữa khỏi, hỏi giá hay hỏi đặt lịch thì không hứa gì, giữ ở lời kêu gọi phi thương mại | — | — | — | — | — | Chặn tới khi mở cổng chào bán | Chủ Y Viện |
| TL-PS-16 | Chiến lược | Cách trả lời | Facebook Page Toplink Y Viện | Không thu thập thông tin sức khoẻ hay thông tin cá nhân ngoài mức cần thiết; câu chuyện khách chỉ dùng khi có đồng ý bằng văn bản | — | — | — | — | — | Chặn mặc định | Cổng pháp lý |
| TL-PS-17 | Chiến lược | Cách trả lời | Facebook Page Toplink Y Viện | Không dựng phễu nhắn tin tự động, không thu thập liên hệ, không gắn liên kết đặt lịch | — | — | — | — | — | Chặn tới khi qua cổng riêng tư và tuân thủ | Cổng pháp lý |
| TL-PS-18 | Chiến lược | Lời kêu gọi | Facebook Page Toplink Y Viện | Trước khi mở cổng chào bán chỉ được dùng ba lời kêu gọi: theo dõi Page, lưu bài, chia sẻ nội dung | — | — | — | — | — | Chặn mặc định | Hướng dẫn thương hiệu |
| TL-PS-19 | Chiến lược | Cách lớn lên | Facebook Page Toplink Y Viện | Lan bằng niềm tin: nội dung bằng chứng vận hành và nội dung giáo dục, lấy lượt lưu và lượt chia sẻ làm tín hiệu lan chính | — | — | — | — | — | Mở | Chủ Y Viện |
| TL-PS-20 | Chiến lược | Cách lớn lên | Reels trên Facebook | Reels để người lạ tìm thấy; nội dung gắn Hà Nội cho làn địa phương, nội dung giáo dục cho làn toàn quốc | — | — | — | — | — | Mở | Chủ Y Viện |
| TL-PS-21 | Chiến lược | Cách lớn lên | Facebook Page Toplink Y Viện | Không chạy quảng cáo trả tiền trong chu kỳ này; đăng lại sang trang cá nhân của founder là hành động ngoài phạm vi và cần duyệt riêng | — | — | — | — | — | Chặn tới khi có cổng ngân sách | Chủ Y Viện |
| TL-PB-01 | Mốc đo | Người theo dõi | Facebook Page Toplink Y Viện | Mốc xuất phát của Page | — | — | 0 | Tổng người theo dõi Page | Ngay sau ảnh chụp danh tính Page | Đã chốt mốc xuất phát | Chủ Y Viện |
| TL-PB-02 | Mốc đo | Mức nhận biết | Facebook Page Toplink Y Viện | Chưa có phép đo nào cho nhận biết thương hiệu | — | — | NO_MEASUREMENT | Chưa có mẫu số | Chưa đo | Thiếu đầu vào | Chủ Y Viện |
| TL-PB-03 | Mốc đo | Dấu tích xanh | Facebook Page Toplink Y Viện | Dấu tích xanh chỉ là tín hiệu định danh của nền tảng, **không** phải chỉ số niềm tin và không được dùng làm bằng chứng năng lực | — | — | Không dùng làm chỉ số | Không áp dụng | Không áp dụng | Cấm dùng làm chỉ số | Hướng dẫn thương hiệu |
| TL-PB-04 | Mốc đo | Cách đọc tăng trưởng | Facebook Page Toplink Y Viện | Cấm báo cáo phần trăm tăng trưởng tính từ mốc 0; chỉ báo số tuyệt đối cho tới khi đủ cỡ mẫu | — | — | Cấm phần trăm từ 0 | Không áp dụng | Không áp dụng | Luật đọc số | Chủ Y Viện |

## 3. Cổng lời kêu gọi thương mại

Lời kêu gọi đặt lịch hoặc tư vấn chỉ mở khi có đủ: đúng dịch vụ hoặc sản phẩm cụ thể, điều kiện phù
hợp, địa điểm, khả năng phục vụ, ai giữ đầu mối liên hệ, cam kết thời gian phản hồi, thông báo riêng
tư, giá và điều kiện nếu có nhắc tới, và kết luận tuân thủ. Hiện chưa có cổng này.

## 4. VERIFY (TL-M3)

- [x] Facebook Page là kênh chính, Reels hỗ trợ; vai trò khớp hồ sơ và master plan §11.
- [x] Nhịp 1 tới 2 bài mỗi ngày, ngày tương đối, chặn trên bởi năng lực sản xuất.
- [x] Founder duyệt theo từng bài; mặc định lời kêu gọi phi thương mại; cách trả lời chặn mặc định.
- [x] Không suy ra dịch vụ toàn quốc; quảng cáo trả tiền nằm ngoài phạm vi.
- [x] Header khai đúng tab `YV_06_page_strategy` (sửa lỗi mô hình #1: bản cũ khai `TL_PAGE_STRATEGY`,
      một dataset không tồn tại).
- [x] Cột `Trụ liên quan` dùng tên trụ tiếng Việt, không lộ mã kỹ thuật ra cột hiển thị.
- [x] `external_writes=0`.
