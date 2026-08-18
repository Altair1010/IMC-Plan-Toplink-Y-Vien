# TL-M4 — Kiến trúc chiến dịch dẫn dắt bằng niềm tin (Toplink Y Viện)

> **Run 1 Phase A · chỉ chạy nội bộ · `external_writes=0`.** Toàn bộ lịch dùng **ngày tương đối
> `D-1` … `D-28`**; không có ngày tuyệt đối nào, ngày bắt đầu chưa đặt. Nhịp 1 tới 2 bài mỗi ngày.
> Đây là **khung**, không phải nội dung hoàn chỉnh — chủ Y Viện quay, dựng và chốt lời viết.

## 0. Khối định danh

| Trường | Giá trị |
|---|---|
| Milestone | `TL-M4` |
| Stable ID | `TL-CAMPAIGN-001` |
| Tab đích | `YV_07_campaign` |
| Schema | `YV-SHEET-001/1.0.0` |
| Trạng thái | `LOCAL_VERIFIED` — chưa `APPROVED`, chưa ghi Sheet |
| Chu kỳ hiện tại | `C1` |
| Nguồn sự thật | master plan §9, §11 · `content-pillars.md §2` · `positioning.md §2` |
| Ghi ra ngoài | `0` |

## 1. Bảng dữ liệu — `YV_07_campaign`

Quy ước bảng theo `dmp-profile.md §1`. Cột `Trụ nội dung` trỏ về `YV_05_content_pillars` bằng tên
tiếng Việt đầy đủ. Ô nền vàng ở cột `Cổng cứng` nghĩa là còn một việc của người thật chưa làm.

| Mã | Chu kỳ | Tuần | Ngày | Vai trò giai đoạn | Trụ nội dung | Việc cần giải cho khách | Cổng cứng | Kêu gọi mặc định | Chủ sở hữu |
|---|---|---|---|---|---|---|---|---|---|
| TL-CAMP-W1 | C1 | Tuần 1 | D-1 … D-7 | Nói rõ Y Viện là gì và không phải là gì; dựng danh tính và giới hạn | Y Viện là ai — phạm vi và giới hạn, Bằng chứng vận hành: không gian, quy trình, con người | Người mới cần hiểu Y Viện đứng ở đâu trước khi tin điều gì | Đã chốt — chỉ nói trong phạm vi danh tính Page; cấm mọi cách nói công khai về nhượng quyền và pháp lý | Theo dõi Page, lưu bài | Hướng dẫn thương hiệu |
| TL-CAMP-W2 | C1 | Tuần 2 | D-8 … D-14 | Tín hiệu đời thường, thói quen nhỏ, đọc hiểu cơ thể | Hiểu và lắng nghe tín hiệu cơ thể, Lý – Dược – Dưỡng dễ hiểu | Người đang mỏi mệt cần hiểu cơ thể mình mà không bị doạ | CHƯA CHỐT — chủ Y Viện cần chỉ định người có chuyên môn rà từng bài tuần này; chưa có tên người thì cả tuần không đăng được | Lưu bài, chia sẻ | Cổng sức khoẻ |
| TL-CAMP-W3 | C1 | Tuần 3 | D-15 … D-21 | Không gian, quy trình, vệ sinh, đội ngũ | Bằng chứng vận hành: không gian, quy trình, con người | Người đang cân nhắc cần thấy sự chỉn chu bằng thứ kiểm chứng được | CHƯA CHỐT — chủ Y Viện cần xác nhận ai được lên hình và đã có đồng ý bằng văn bản chưa; chưa có thì bỏ hết phần con người, chỉ giữ không gian và quy trình | Theo dõi Page, lưu bài | Cổng pháp lý |
| TL-CAMP-W4 | C1 | Tuần 4 | D-22 … D-28 | Khép chu kỳ theo một trong hai nhánh: nhánh có hồ sơ sản phẩm hoặc nhánh dự phòng an toàn | Y Viện là ai — phạm vi và giới hạn, Bằng chứng vận hành: không gian, quy trình, con người, Hành trình Y Viện, founder và cộng đồng | Người đã theo dõi cần một bước tiếp theo nhẹ, không bị ép | CHƯA CHỐT — chủ Y Viện chọn nhánh: nộp hồ sơ một sản phẩm hoặc dịch vụ để mở nhánh có bằng chứng, hoặc giữ nhánh dự phòng an toàn. Chưa chọn thì mặc định chạy nhánh dự phòng | Theo dõi Page, lưu bài, chia sẻ | Chủ Y Viện |

## 2. Khung từng tuần (cấu trúc, không phải lời viết hoàn chỉnh)

### Tuần 1 — Danh tính và giới hạn
- **Góc kể:** Y Viện là ai, phạm vi chăm sóc chủ động, và giới hạn rõ ràng — không bệnh viện, không
  chữa khỏi.
- **Khung mỗi bài:** một câu hỏi đời thường mở đầu, một ý định vị, một ý giới hạn, rồi lời kêu gọi
  theo dõi hoặc lưu.
- **Câu claim được dùng:** `CL-M1`, `CL-M3`. **Cấm:** nhượng quyền, pháp lý, công dụng.
- **Vị trí trong tuần:** `D-1` giới thiệu Page · `D-3` Y Viện không phải là gì · `D-5` hé không gian ·
  `D-7` giá trị Thân – Tâm – Trí.

### Tuần 2 — Đọc hiểu cơ thể (chạm sức khoẻ)
- **Góc kể:** lắng nghe tín hiệu cơ thể; thói quen nhỏ; hệ Lý – Dược – Dưỡng dùng đúng người, đúng
  cách, đúng thời điểm.
- **Khung mỗi bài:** một tín hiệu quen thuộc, giải thích mà **không chẩn đoán**, đóng khung ở mức hỗ
  trợ, **bắt buộc** câu miễn trừ kèm lưu ý khác biệt cá nhân, rồi lời kêu gọi lưu bài.
- **Mỗi bài:** gắn mã claim, chạy kiểm tra tự động, và **người có chuyên môn rà trước khi đăng** —
  rà theo từng bài, không rà theo lô.
- **Cấm:** ngôn từ nhân quả, ngôn từ chẩn đoán, khẳng định công dụng, chữ "chữa khỏi".

### Tuần 3 — Bằng chứng vận hành
- **Góc kể:** không gian bốn tầng, quy trình tám bước, vệ sinh, con người — minh bạch, ảnh thật.
- **Khung mỗi bài:** một chi tiết không gian hoặc quy trình, một dữ kiện vận hành, rồi lời kêu gọi
  theo dõi hoặc lưu.
- **Được nói:** chỉ dữ kiện vận hành. **Bị chặn:** bằng cấp nhân sự, kết quả, lời khách.

### Tuần 4 — Khép chu kỳ có điều kiện
- **Nhánh A — có bằng chứng:** chỉ mở khi một sản phẩm hoặc dịch vụ cụ thể có hồ sơ đạt (nhãn, giấy
  tờ, phạm vi pháp lý, hướng dẫn sử dụng, chống chỉ định) **và** đã có cổng chào bán. Kể cả khi đó,
  lời kêu gọi **vẫn phi thương mại** cho tới khi cổng chào bán mở.
- **Nhánh B — dự phòng an toàn (mặc định, trọn vẹn):** nhắc lại nội dung thương hiệu, quy trình và
  cộng đồng, củng cố phần đọc hiểu cơ thể, mời theo dõi và lưu. Đây là **một tuần trọn vẹn**, không
  phải bản rút gọn của nhánh A. Không được dùng mẹo lịch hay mẹo câu miễn trừ để thay cho một hồ sơ
  còn thiếu.
- **Trạng thái hiện tại:** chưa có hồ sơ nào đạt, chưa có cổng chào bán, nên **Tuần 4 chạy nhánh B**.

## 3. Luật lời kêu gọi

- Mặc định suốt bốn tuần: **theo dõi Page · lưu bài · chia sẻ**.
- Lời kêu gọi thương mại (đặt lịch, tư vấn, mua) cần một cổng chào bán **hiện chưa tồn tại**: đúng
  dịch vụ, điều kiện phù hợp, địa điểm, khả năng phục vụ, ai giữ đầu mối, cam kết thời gian phản hồi,
  thông báo riêng tư, kết luận tuân thủ.
- Bài do founder dẫn tối đa 1 trên mỗi 5 bài; không đặt hai lời kêu gọi thương mại do founder dẫn
  liền kề (hiện chưa có lời kêu gọi thương mại nào).

## 4. Thử nghiệm gắn với chiến dịch

Ba thử nghiệm của chu kỳ này (kiểu hook · định dạng · cơ cấu trụ) được khai **một lần duy nhất** ở
`docs Toplink/brand/kpi-experiment-plan.md §3`, là bảng dữ liệu của tab `YV_08_experiments`. Tệp này
không lặp lại bảng đó, để trình biên dịch chỉ có đúng một nguồn cho mỗi tab.

Nguyên tắc: đổi **một** biến mỗi lần; không bao giờ gắn một thử nghiệm vào khẳng định sức khoẻ; không
ra quyết định dựa trên phần trăm tính từ mốc 0.

## 5. VERIFY (TL-M4)

- [x] Bốn tuần, mỗi tuần truy được về trụ nội dung và việc cần giải cho khách.
- [x] Cổng tuần 2 và tuần 3 ở mức từng bài; tuần 4 có nhánh dự phòng trọn vẹn, không phải bản lách.
- [x] Ngày tương đối `D-1` … `D-28`; không ngày tuyệt đối; ngày bắt đầu chưa đặt.
- [x] Mặc định lời kêu gọi phi thương mại; lời kêu gọi thương mại nằm sau một cổng chưa tồn tại.
- [x] Chỉ là khung; nội dung hoàn chỉnh và media thuộc về chủ Y Viện.
- [x] Header khai đúng tab `YV_07_campaign` (sửa lỗi mô hình #1: bản cũ khai `TL_CAMPAIGN_KPI`, một
      dataset không tồn tại).
- [x] Ba ô `Cổng cứng` ở tuần 2, 3, 4 mở đầu bằng `CHƯA CHỐT — ` và nêu rõ ai quyết, quyết điều gì;
      mỗi ô có đúng một dòng đối ứng ở `00_Y_VIEN_CAN_CHOT`.
- [x] `external_writes=0`; tuần 4 hiện chạy nhánh dự phòng an toàn.
