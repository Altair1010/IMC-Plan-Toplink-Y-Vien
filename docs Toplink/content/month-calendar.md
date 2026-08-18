# TL-M5 — Lịch nội dung 28 ngày (Toplink Y Viện)

> **Run 1 Phase A · chỉ chạy nội bộ · `external_writes=0`.** Lịch dùng **ngày tương đối `D-1` …
> `D-28`** — không ngày tuyệt đối, ngày bắt đầu chưa đặt. Ngày lễ, ngày ra mắt và sự kiện là **ô ưu
> tiên chèn thêm**, không gán vào ngày cứng. Không mục nào `APPROVED` hay sẵn sàng đăng ở giai đoạn này.

## 0. Khối định danh

| Trường | Giá trị |
|---|---|
| Milestone | `TL-M5` |
| Stable ID | `TL-M5-CALENDAR-001` |
| Tab đích | `YV_09_content_calendar` |
| Schema | `YV-SHEET-001/1.0.0` |
| Trạng thái | `LOCAL_VERIFIED` — chưa `APPROVED`, chưa ghi Sheet |
| Chu kỳ hiện tại | `C1` |
| Số dòng nguồn | 28 (mỗi ngày một dòng) |
| Số dòng sau khi bung | 84 (28 × ba hướng A, B, C) |
| Phân bổ trụ | 6 · 6 · 8 · 4 · 4 = 28 |
| Định dạng | 12 Reel + 16 bài tĩnh hoặc carousel |
| Nguồn sự thật | `content-pillars.md §2` · `campaign-architecture.md §1` · `audience-hypotheses.md §2` · `kpi-experiment-plan.md §3` |
| Ghi ra ngoài | `0` |

## 1. Quy ước bảng

Theo `dmp-profile.md §1`, cộng ba điều riêng cho tab lịch:

1. **Cột `Ba hướng A / B / C` là cột bung.** Trình biên dịch tách đúng ba mảnh theo dạng
   `A: … · B: … · C: …`, sinh ra ba dòng cho mỗi ngày và điền vào hai cột hiển thị `Hướng` và
   `Nói gì`. **Tách không ra đúng ba mảnh thì dừng lại và báo lỗi**, không được nhân bản một mảnh
   thành cả ba (sửa lỗi mô hình #5). Vì vậy dấu ` · ` **chỉ** được dùng làm dấu tách giữa ba hướng,
   không dùng bên trong lời của một hướng.
2. **Hướng A là hướng khuyến nghị.** Hai hướng B và C là dự phòng: khi lên Sheet chúng mang tiền tố
   `DỰ PHÒNG — ` và **không bao giờ được tô vàng**.
3. **Hai cột tham chiếu chéo được phép mang mã**: `Câu claim dùng` mang mã `CL-*` tra được ở
   `06_COMPLIANCE_RULES` (tab này bày cột `Mã` ra mặt trước), và `Thử nghiệm gắn kèm` mang nhãn tuần
   tra được ở `YV_08_experiments`. Ngoài hai cột này, không cột hiển thị nào của tab được chứa mã kỹ thuật.

**Tab lịch không có ô vàng.** Trạng thái `NEEDS_HUMAN_REVIEW` của 14 mục là **trạng thái quy trình**,
không phải một quyết định đang treo. Việc người thật còn nợ là *chỉ định người có chuyên môn rà bài* —
việc đó đã có đúng một ô vàng ở `YV_07_campaign` tuần 2 và đúng một dòng ở `00_Y_VIEN_CAN_CHOT`.
Tô vàng 14 lần cho cùng một quyết định là làm loãng tín hiệu.

## 2. Bảng dữ liệu — `YV_09_content_calendar`

| Mã | Chu kỳ | Ngày | Nhóm khách | Trụ nội dung | Định dạng | Vai trò phễu | Angle chính | Ba hướng A / B / C | Kêu gọi | Câu claim dùng | Thử nghiệm gắn kèm | Tuyến duyệt | Bản sửa | Trạng thái duyệt | Chủ sở hữu |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TL-M5-CAL-D1 | C1 | D-1 | Người bận rộn ở Hà Nội | Y Viện là ai — phạm vi và giới hạn | Reel | TOFU | Y Viện là ai, mở đầu Page | A: mở bằng câu hỏi chị có đang chăm sóc cơ thể đều đặn không · B: mở bằng hình không gian trước khi nói lời nào · C: một câu định vị kèm ngay một câu giới hạn | Theo dõi Page, lưu bài | CL-ID1, CL-M1 | Tuần 1 — kiểu mở bài | R1+R2 | 1 | DRAFT | Chủ Y Viện |
| TL-M5-CAL-D2 | C1 | D-2 | Người bận rộn ở Hà Nội | Y Viện là ai — phạm vi và giới hạn | Bài tĩnh | TOFU | Y Viện không phải là gì | A: thẻ đôi là gì và không phải gì · B: ba hiểu lầm thường gặp về nơi như Y Viện · C: một câu ranh giới duy nhất, viết thật rõ | Theo dõi Page, lưu bài | CL-ID1 | Tuần 1 — kiểu mở bài | R1 | 1 | DRAFT | Chủ Y Viện |
| TL-M5-CAL-D3 | C1 | D-3 | Phụ nữ chăm sóc sức khoẻ chủ động | Bằng chứng vận hành: không gian, quy trình, con người | Reel | MOFU | Hé không gian bốn tầng | A: lia một lượt qua bốn tầng · B: đi sâu vào chi tiết của đúng một tầng · C: để âm thanh và khoảng tĩnh dẫn dắt | Theo dõi Page, lưu bài | CL-OP1 | Tuần 1 — kiểu mở bài | R1+R2 | 1 | DRAFT | Chủ Y Viện |
| TL-M5-CAL-D4 | C1 | D-4 | Người quan tâm dưỡng sinh toàn quốc | Y Viện là ai — phạm vi và giới hạn | Carousel | TOFU | Thân, Tâm, Trí và giới hạn | A: ba trụ giá trị, mỗi trụ một thẻ · B: nói vì sao trước khi nói làm gì · C: minh bạch giới hạn ngay từ thẻ đầu | Lưu bài, chia sẻ | CL-M1, CL-ID1 | Tuần 1 — kiểu mở bài | R1 | 1 | DRAFT | Hướng dẫn thương hiệu |
| TL-M5-CAL-D5 | C1 | D-5 | Người quan tâm dưỡng sinh toàn quốc | Hành trình Y Viện, founder và cộng đồng | Bài tĩnh | TOFU | Ý niệm và hành trình founder | A: một câu ý niệm, không giải thích thêm · B: kể về một khoảng dừng có chủ đích · C: nói về cộng đồng dưỡng sinh quanh Y Viện | Theo dõi Page, lưu bài | CL-FD1 | Tuần 1 — kiểu mở bài | R1+R3 | 1 | NEEDS_HUMAN_REVIEW | Cổng pháp lý |
| TL-M5-CAL-D6 | C1 | D-6 | Người trung niên và lớn tuổi | Bằng chứng vận hành: không gian, quy trình, con người | Bài tĩnh | MOFU | Quy trình tám bước, minh bạch | A: liệt kê đủ tám bước · B: nhấn vào việc xin phép trước mỗi thao tác · C: nhấn vào bước sàng lọc và lời khuyên đi khám khi cần | Lưu bài | CL-OP2 | Tuần 1 — kiểu mở bài | R1 | 1 | DRAFT | Chủ Y Viện |
| TL-M5-CAL-D7 | C1 | D-7 | Người bận rộn ở Hà Nội | Y Viện là ai — phạm vi và giới hạn | Reel | TOFU | Nhắc lại định vị tuần một | A: tóm gọn ba ý đã nói trong tuần · B: dựng lại cặp là gì và không phải gì · C: mời theo dõi để đi tiếp tuần sau | Theo dõi Page, lưu bài | CL-ID1, CL-M1 | Tuần 1 — kiểu mở bài | R1+R2 | 1 | DRAFT | Chủ Y Viện |
| TL-M5-CAL-D8 | C1 | D-8 | Người bận rộn ở Hà Nội | Hiểu và lắng nghe tín hiệu cơ thể | Reel | TOFU | Tín hiệu cổ vai gáy do ngồi nhiều | A: mô tả đúng cảm giác quen thuộc, không gọi tên bệnh · B: một thói quen nhỏ làm được giữa giờ · C: nói rõ khi nào nên hỏi người có chuyên môn | Lưu bài | CL-M2 | — | R1+R2+R3 | 1 | NEEDS_HUMAN_REVIEW | Cổng sức khoẻ |
| TL-M5-CAL-D9 | C1 | D-9 | Người trung niên và lớn tuổi | Lý – Dược – Dưỡng dễ hiểu | Bài tĩnh | MOFU | Lý – Dược – Dưỡng nói cho dễ hiểu | A: ba lớp là gì, mỗi lớp một câu · B: nhấn vào đúng người và đúng thời điểm · C: nói trước về giới hạn và lưu ý | Lưu bài | CL-M4 | — | R1+R3 | 1 | NEEDS_HUMAN_REVIEW | Cổng sức khoẻ |
| TL-M5-CAL-D10 | C1 | D-10 | Người bận rộn ở Hà Nội | Hiểu và lắng nghe tín hiệu cơ thể | Carousel | TOFU | Thói quen nhỏ, làm đều đặn | A: năm thói quen, mỗi thẻ một thói quen · B: chỉ một thói quen, làm mỗi ngày · C: dạy cách tự lắng nghe cơ thể trước đã | Lưu bài, chia sẻ | CL-M2 | — | R1+R3 | 1 | NEEDS_HUMAN_REVIEW | Cổng sức khoẻ |
| TL-M5-CAL-D11 | C1 | D-11 | Phụ nữ chăm sóc sức khoẻ chủ động | Hiểu và lắng nghe tín hiệu cơ thể | Reel | TOFU | Hỗ trợ làm ấm và thư giãn | A: kể lại cảm giác được làm ấm · B: một nhịp thở và một khoảng dừng · C: nói rõ đây là mức hỗ trợ, không phải điều trị | Lưu bài | CL-M2 | — | R1+R2+R3 | 1 | NEEDS_HUMAN_REVIEW | Cổng sức khoẻ |
| TL-M5-CAL-D12 | C1 | D-12 | Người chăm sóc cha mẹ | Lý – Dược – Dưỡng dễ hiểu | Carousel | MOFU | Đúng người, đúng cách, đúng thời điểm | A: nguyên tắc chọn theo thể trạng · B: ba câu hỏi cần tự trả lời trước khi chọn · C: nhóm cần thận trọng, nói ngay từ thẻ đầu | Lưu bài | CL-M4 | — | R1+R3 | 1 | NEEDS_HUMAN_REVIEW | Cổng sức khoẻ |
| TL-M5-CAL-D13 | C1 | D-13 | Người chăm sóc cha mẹ | Hiểu và lắng nghe tín hiệu cơ thể | Bài tĩnh | TOFU | Nhóm cần thận trọng | A: bệnh nền, mang thai, có thiết bị cấy ghép · B: nên hỏi trước khi dùng bất cứ thứ gì · C: chăm cha mẹ mà vẫn giữ được sự an tâm | Lưu bài, chia sẻ | CL-M2 | — | R1+R3 | 1 | NEEDS_HUMAN_REVIEW | Cổng sức khoẻ |
| TL-M5-CAL-D14 | C1 | D-14 | Phụ nữ chăm sóc sức khoẻ chủ động | Lý – Dược – Dưỡng dễ hiểu | Reel | MOFU | Dưỡng liệu kể ở mức trải nghiệm | A: kể lại trải nghiệm tại Y Viện · B: nhấn vào việc làm theo hướng dẫn · C: nói về nhịp chăm sóc định kỳ | Lưu bài | CL-CX1, CL-M4 | — | R1+R2+R3 | 1 | NEEDS_HUMAN_REVIEW | Cổng sức khoẻ |
| TL-M5-CAL-D15 | C1 | D-15 | Phụ nữ chăm sóc sức khoẻ chủ động | Bằng chứng vận hành: không gian, quy trình, con người | Reel | MOFU | Tầng một và tầng hai, Tĩnh và Thông | A: cảnh đón tiếp và nhận phòng · B: gội dưỡng sinh và ngâm chân · C: chất liệu và ánh sáng xuyên qua không gian | Theo dõi Page, lưu bài | CL-OP1, CL-M3 | Tuần 3 — định dạng | R1+R2 | 1 | DRAFT | Chủ Y Viện |
| TL-M5-CAL-D16 | C1 | D-16 | Người trung niên và lớn tuổi | Bằng chứng vận hành: không gian, quy trình, con người | Carousel | MOFU | Tám bước, kể bằng thẻ | A: tám thẻ, mỗi thẻ một bước · B: nhấn vào việc giải thích trước khi làm · C: nhấn vào bước sàng lọc rủi ro | Lưu bài | CL-OP2, CL-M3 | Tuần 3 — định dạng | R1 | 1 | DRAFT | Chủ Y Viện |
| TL-M5-CAL-D17 | C1 | D-17 | Phụ nữ chăm sóc sức khoẻ chủ động | Bằng chứng vận hành: không gian, quy trình, con người | Bài tĩnh | MOFU | Vệ sinh và sự chỉn chu | A: quy chuẩn vệ sinh, nói bằng dữ kiện · B: thơm dịu, sạch và yên · C: những chi tiết nhỏ trong không gian | Theo dõi Page, lưu bài | CL-OP3 | Tuần 3 — định dạng | R1 | 1 | DRAFT | Chủ Y Viện |
| TL-M5-CAL-D18 | C1 | D-18 | Người bận rộn ở Hà Nội | Bằng chứng vận hành: không gian, quy trình, con người | Reel | MOFU | Hậu trường đội ngũ chuẩn bị | A: cảnh chuẩn bị trước một buổi · B: nhấn vào việc xin phép trước thao tác · C: nhấn vào sự chăm chút từng chi tiết | Theo dõi Page, lưu bài | CL-OP3 | Tuần 3 — định dạng | R1+R2 | 1 | DRAFT | Chủ Y Viện |
| TL-M5-CAL-D19 | C1 | D-19 | Phụ nữ chăm sóc sức khoẻ chủ động | Bằng chứng vận hành: không gian, quy trình, con người | Bài tĩnh | MOFU | Tầng ba và tầng bốn, Dưỡng và Tỉnh | A: xông, ngâm và đá nóng · B: trà, thiền và buổi chia sẻ · C: không gian dành cho cộng đồng | Lưu bài | CL-OP1 | Tuần 3 — định dạng | R1 | 1 | DRAFT | Chủ Y Viện |
| TL-M5-CAL-D20 | C1 | D-20 | Người quan tâm dưỡng sinh toàn quốc | Hành trình Y Viện, founder và cộng đồng | Bài tĩnh | TOFU | Nghề có tâm và cộng đồng | A: giá trị của việc đào tạo tử tế · B: đôi tay cộng với một trái tim biết lắng nghe · C: lời mời cộng đồng cùng đi | Theo dõi Page, chia sẻ | CL-FD1 | Tuần 3 — định dạng | R1+R3 | 1 | NEEDS_HUMAN_REVIEW | Cổng pháp lý |
| TL-M5-CAL-D21 | C1 | D-21 | Người trung niên và lớn tuổi | Bằng chứng vận hành: không gian, quy trình, con người | Reel | MOFU | Khoảnh khắc tạo ra niềm tin | A: nhớ đúng điều khách đã dặn · B: nói thẳng khi thấy không phù hợp · C: không mời mua khi khách đang thư giãn | Theo dõi Page, lưu bài | CL-OP3, CL-M3 | Tuần 3 — định dạng | R1+R2 | 1 | DRAFT | Chủ Y Viện |
| TL-M5-CAL-D22 | C1 | D-22 | Người bận rộn ở Hà Nội | Y Viện là ai — phạm vi và giới hạn | Bài tĩnh | TOFU | Nhắc lại Y Viện là ai | A: tóm gọn định vị trong ba câu · B: nhắc lại giá trị Thân, Tâm, Trí · C: nhắc lại giới hạn thật rõ | Theo dõi Page, lưu bài | CL-ID1, CL-M1 | Tuần 4 — cơ cấu trụ | R1 | 1 | DRAFT | Chủ Y Viện |
| TL-M5-CAL-D23 | C1 | D-23 | Người bận rộn ở Hà Nội | Hiểu và lắng nghe tín hiệu cơ thể | Reel | TOFU | Nhắc lại cách lắng nghe cơ thể | A: một tín hiệu kèm một thói quen · B: một nhịp dừng lại giữa ngày · C: nhắc lại khi nào nên hỏi chuyên môn | Lưu bài | CL-M2 | Tuần 4 — cơ cấu trụ | R1+R2+R3 | 1 | NEEDS_HUMAN_REVIEW | Cổng sức khoẻ |
| TL-M5-CAL-D24 | C1 | D-24 | Người quan tâm dưỡng sinh toàn quốc | Hành trình Y Viện, founder và cộng đồng | Bài tĩnh | TOFU | Hành trình và cộng đồng | A: những cột mốc của ý niệm · B: lời cảm ơn gửi cộng đồng · C: lời mời cùng đi tiếp chặng sau | Theo dõi Page, chia sẻ | CL-FD1 | Tuần 4 — cơ cấu trụ | R1+R3 | 1 | NEEDS_HUMAN_REVIEW | Cổng pháp lý |
| TL-M5-CAL-D25 | C1 | D-25 | Người quan tâm dưỡng sinh toàn quốc | Y Viện là ai — phạm vi và giới hạn | Reel | TOFU | Nhắc lại giá trị thương hiệu | A: ba giá trị, mỗi giá trị một nhịp · B: giải thích chăm sóc chủ động nghĩa là gì · C: mời theo dõi để nhận nội dung tuần tới | Theo dõi Page, lưu bài | CL-ID1, CL-M1 | Tuần 4 — cơ cấu trụ | R1+R2 | 1 | DRAFT | Chủ Y Viện |
| TL-M5-CAL-D26 | C1 | D-26 | Phụ nữ chăm sóc sức khoẻ chủ động | Lý – Dược – Dưỡng dễ hiểu | Carousel | MOFU | Lý – Dược – Dưỡng ở mức trải nghiệm | A: nhắc lại ba lớp bằng ba thẻ · B: nhấn vào việc chọn đúng nhu cầu · C: nói về nhịp chăm sóc định kỳ | Lưu bài | CL-CX1, CL-M4 | Tuần 4 — cơ cấu trụ | R1+R3 | 1 | NEEDS_HUMAN_REVIEW | Cổng sức khoẻ |
| TL-M5-CAL-D27 | C1 | D-27 | Người chăm sóc cha mẹ | Hiểu và lắng nghe tín hiệu cơ thể | Reel | TOFU | Thói quen chăm sóc chủ động | A: mỗi ngày một thói quen nhỏ · B: lắng nghe rồi mới nghỉ ngơi đúng cách · C: nhắc lại nhóm cần thận trọng | Lưu bài, chia sẻ | CL-M2 | Tuần 4 — cơ cấu trụ | R1+R2+R3 | 1 | NEEDS_HUMAN_REVIEW | Cổng sức khoẻ |
| TL-M5-CAL-D28 | C1 | D-28 | Người quan tâm dưỡng sinh toàn quốc | Hành trình Y Viện, founder và cộng đồng | Bài tĩnh | TOFU | Mời cộng đồng dưỡng sinh | A: tổng kết bốn tuần vừa qua · B: nói về giá trị của một cộng đồng · C: mời theo dõi và lưu lại để dùng dần | Theo dõi Page, lưu bài, chia sẻ | CL-FD1 | Tuần 4 — cơ cấu trụ | R1+R3 | 1 | NEEDS_HUMAN_REVIEW | Cổng pháp lý |

## 3. Tuyến duyệt

- **R1 — người viết chuyển người phụ trách truyền thông:** áp cho mọi mục.
- **R2 — thêm một vòng cho cơ chế video:** áp cho mọi mục dạng Reel.
- **R3 — thêm cổng người có chuyên môn:** áp cho mục chạm sức khoẻ, mục có founder, mục nói quanh sản
  phẩm, và mọi mục định vị công khai nhạy cảm.

Không vòng duyệt nào của agent được cấp `APPROVED`. Chỉ chủ Y Viện mới đặt được trạng thái đó, và đặt
theo từng bài chứ không theo lô.

## 4. Ô ưu tiên chèn thêm

Ngày lễ, ngày ra mắt và sự kiện là **ô ưu tiên** chèn vào chuỗi tương đối khi lịch thật được duyệt, chứ
không gán ngày tuyệt đối ở giai đoạn này. Ứng viên: ngày giới thiệu không gian đi vào trụ bằng chứng
vận hành, buổi chia sẻ cộng đồng đi vào trụ hành trình và cộng đồng, mùa lễ đi vào trụ danh tính hoặc
trụ đọc hiểu cơ thể kèm câu miễn trừ. Mỗi ô vẫn theo đúng tuyến duyệt, đúng lời kêu gọi và đúng luật
câu claim.

## 5. VERIFY (TL-M5 lịch)

- [x] 28 ngày tương đối `D-1` … `D-28`, mỗi ngày một mã duy nhất, không ngày tuyệt đối.
- [x] Mỗi ngày có đủ ba hướng A, B, C theo đúng dạng tách được; A là khuyến nghị, B và C là dự phòng.
- [x] Phân bổ trụ 6 · 6 · 8 · 4 · 4 = 28; đúng 12 Reel.
- [x] Cột `Nhóm khách` là dữ liệu thật do người chọn, trỏ về `YV_02_audience` (sửa lỗi mô hình #2:
      bản cũ để trình biên dịch suy nhóm khách theo số thứ tự ngày).
- [x] Cột `Thử nghiệm gắn kèm` nối thật về `YV_08_experiments` (sửa lỗi mô hình #3: bản cũ ghi cứng
      không khả dụng cho cả 84 dòng).
- [x] Cột `Tuyến duyệt` được giữ lại thành cột thật (sửa lỗi mô hình #4: trình biên dịch cũ bỏ hẳn cột này).
- [x] Ngày đã chuẩn hoá về `D-1` … `D-28`, bỏ dạng zero-pad (sửa lỗi mô hình #8).
- [x] Lời kêu gọi chỉ gồm theo dõi Page, lưu bài, chia sẻ; không đặt lịch, không giá, không tư vấn, không mua.
- [x] 14 mục ở `NEEDS_HUMAN_REVIEW`; không mục nào `APPROVED` hay sẵn sàng đăng.
- [x] Tab này không có ô vàng; lý do ghi tại §1.
- [x] `external_writes=0`.
