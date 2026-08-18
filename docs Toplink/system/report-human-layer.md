# Báo cáo tổng hợp — lớp đọc của workbook

- **Mã tài liệu:** `TL-REPORT-001`
- **Tab đích:** `report` (registry `YV-SHEET-001/1.0.0`, index 0, layout `STACKED_SECTIONS`)
- **Trạng thái:** `DRAFT · LOCAL_ONLY`
- **Vai trò:** lớp đọc. **Không dòng nào ở đây là nguồn sự thật.** Mọi ô đều truy được về tab gốc
  qua cột ẩn `_key`. Sửa nội dung phải sửa ở tab gốc, không sửa ở đây.
- **Nguồn:** `docs Toplink/brand/dmp-profile.md` · `positioning.md` · `narrative.md` ·
  `content-pillars.md` · `facebook-page-strategy.md` · `campaign-architecture.md` ·
  `kpi-experiment-plan.md` · `docs Toplink/research/audience-hypotheses.md` ·
  `docs Toplink/content/month-calendar.md` · `production-briefs.md` · `reels-briefs.md` ·
  `workflow-approval-measurement.md` · `docs Toplink/system/owner-decisions.md`

---

## 1. Quy ước bảng

Theo `docs Toplink/brand/dmp-profile.md §1`, với **ngoại lệ đã khai trong registry**: tab `report`
có layout `STACKED_SECTIONS` nên tệp này chứa **ba bảng dữ liệu**, đúng ba mục §3, §4, §5, ánh xạ
sang ba section `A`, `B`, `C`. Mọi tệp canonical khác vẫn giữ đúng một bảng.

Bốn luật riêng của tab này:

1. **Lưới rộng 9 cột hiển thị.** Bảng B dùng đủ 9. Bảng A dùng 6 và Bảng C dùng 6; trình biên dịch
   đệm ba cột cuối bằng chuỗi rỗng thật, **không** đệm bằng `—`, để mắt người không đọc nhầm đó là
   ô trống có nghĩa. Hai cột ẩn `_key` và `_audit` nằm ở vị trí 10 và 11.
2. **Cột `Cách hiểu đơn giản` bắt buộc dịch sang lời đời thường.** Lặp lại nguyên văn `Hạng mục` là
   lỗi, trình kiểm tra chặn.
3. **Tab này có 0 ô vàng.** Mọi việc còn treo đã có ô vàng ở tab gốc và có đúng một dòng ở
   `00_Y_VIEN_CAN_CHOT`. Tô lại ở đây sẽ phá luật đối xứng một-đổi-một và làm loãng chính cái tab
   sinh ra để gom việc. Cột `Cần chốt / review` của Bảng A và cột `Chặn bởi` của Bảng C vì vậy viết
   mô tả trần, **không** mang tiền tố `CHƯA CHỐT — `, và trỏ người đọc sang tab `Y Viện cần chốt`.
4. **Bảng B không được viết tay.** §4 chỉ khai luật dẫn xuất; 84 dòng do trình biên dịch nổ ra từ
   `YV_09_content_calendar`. Số dòng khác 84 × số chu kỳ thì dừng, không tự bù.

---

## 2. Đọc báo cáo theo thứ tự nào

Bảng A trả lời "Y Viện đang tin điều gì và tin tới mức nào". Bảng B trả lời "28 ngày tới đăng gì,
và nếu hướng chính không chạy được thì lùi về đâu". Bảng C trả lời "muốn biến hai bảng trên thành
việc thật thì làm theo thứ tự nào, ai làm, đang vướng ở đâu".

Ba bảng đọc từ trên xuống. Ai chỉ có mười phút thì đọc Bảng A và tab `Y Viện cần chốt`.

---

## 3. Bảng A — Nền tảng chiến lược

| Mã | Hạng mục | Cách hiểu đơn giản | Ý nghĩa với campaign / content | Điều đã chốt | Cần chốt / review | Người cần can thiệp |
|---|---|---|---|---|---|---|
| TL-RA-01 | Y Viện là gì | Một nơi chăm sóc cơ thể đều đặn, kết hợp dưỡng sinh Đông y với lý liệu và công nghệ | Mọi bài phải đứng trong khung này. Bài nào đẩy Y Viện thành nơi chữa bệnh là bài sai khung, không phải bài mạnh | Định vị lõi: điểm chạm dưỡng thân — tỉnh thức, dùng hệ Lý – Dược – Dưỡng đúng nhu cầu, đúng người, đúng thời điểm và đúng giới hạn | Định vị đang ở mức giả thuyết, chờ 28 ngày nội dung đo tín hiệu lưu bài và chia sẻ | Chủ Y Viện |
| TL-RA-02 | Y Viện không phải là gì | Không phải bệnh viện, không phải phòng khám, không phải nơi hứa khỏi bệnh | Cặp "là gì — không phải gì" là nội dung tuần 1. Nói rõ giới hạn sớm thì về sau đỡ phải đính chính | Cấm mọi cam kết kết quả. Thêm chữ hỗ trợ không hợp thức hoá một khẳng định thiếu bằng chứng | Không còn gì phải chốt. Đây là ranh giới cứng | Cổng sức khoẻ |
| TL-RA-03 | Hệ Lý – Dược – Dưỡng | Ba lớp chăm sóc: đọc hiểu cơ thể, dùng thảo dược, và duy trì nếp sống | Là trụ nội dung số 4. Giải thích ở mức trải nghiệm, tuyệt đối không giải thích ở mức cơ chế | Chỉ nói tới mức người thường hiểu được, cấm mọi khẳng định công dụng | Hồ sơ sản phẩm chưa kiểm chứng nên phần Dược đang bị giữ ở mức kể trải nghiệm | Cổng sức khoẻ |
| TL-RA-04 | Khách hàng nhắm tới | Năm nhóm: người bận rộn ở Hà Nội, người trung niên và lớn tuổi, người chăm sóc cha mẹ, phụ nữ chăm sóc chủ động, và người quan tâm dưỡng sinh toàn quốc | Mỗi ngày trong lịch gắn đúng một nhóm. Không có nhóm thì không biết viết cho ai, và bài sẽ chung chung | Năm nhóm và bốn nhóm không nhắm tới đều đã liệt kê rõ | Cả năm nhóm đang là giả thuyết. Chu kỳ C1 là lần kiểm chứng đầu tiên | Chủ Y Viện |
| TL-RA-05 | Khách hàng không nhắm tới | Người tìm nơi chữa bệnh, người tìm giảm cân cấp tốc, người tìm giá rẻ nhất, và người ở quá xa | Biết mình không nói với ai thì bớt được phần lớn bình luận lệch hướng | Bốn nhóm loại trừ đã ghi rõ kèm lý do | Không còn gì phải chốt trong chu kỳ này | Chủ Y Viện |
| TL-RA-06 | Cách xưng hô | Gọi khách là chị hoặc anh, brand tự gọi mình là Y Viện ở ngôi thứ ba | Áp cho toàn bộ lời thoại, chữ trên hình và phần trả lời bình luận. Sai xưng hô là sai giọng ngay câu đầu | Cấm dùng bạn và quý khách. Chủ ngữ ưu tiên là cơ thể, không phải khách hàng | Không còn gì phải chốt. Đây là luật giọng | Hướng dẫn thương hiệu |
| TL-RA-07 | Từ cấm | Có một danh sách từ mà một chữ thôi cũng chặn cả bài | Người viết phải rà trước khi gửi duyệt. Vi phạm thì chặn cả bài, không sửa cục bộ rồi đăng | Cấm chữa khỏi, điều trị dứt điểm, thay thế thuốc, khỏi hoàn toàn, cam kết khỏi sau X ngày, chống ung thư | Không còn gì phải chốt. Danh sách là ranh giới cứng | Cổng sức khoẻ |
| TL-RA-08 | Năm trụ nội dung | Năm chủ đề xoay vòng suốt 28 ngày, mỗi trụ có số ngày cố định | Trụ quyết định ngày nào viết gì. Đổi tỷ trọng là đổi cả lịch, nên đổi thì phải đổi ở một chỗ | Sáu ngày cho trụ danh tính, sáu ngày tín hiệu cơ thể, tám ngày bằng chứng vận hành, bốn ngày Lý – Dược – Dưỡng, bốn ngày founder và cộng đồng | Tỷ trọng là giả thuyết. Thử nghiệm tuần 4 sẽ chạm đúng câu hỏi này | Chủ Y Viện |
| TL-RA-09 | Vai trò phễu | Ba trụ để người lạ biết tới, hai trụ để người đã biết cân nhắc, chưa trụ nào để ra quyết định | Chưa mở cổng chào bán thì chưa có tầng ra quyết định. Cố ép bán ở giai đoạn này là phá niềm tin đang xây | Nhận biết dùng trụ 1, 2, 5. Cân nhắc dùng trụ 3, 4. Ra quyết định để trống có chủ đích | Tầng ra quyết định mở khi nào là việc của cổng chào bán, chưa hẹn | Chủ Y Viện |
| TL-RA-10 | Chiến dịch 28 ngày | Bốn tuần, mỗi tuần một việc: nói rõ mình là ai, đọc hiểu cơ thể, chứng minh vận hành, rồi khép nhẹ | Tuần trước dựng nền cho tuần sau. Đảo thứ tự thì tuần 3 mất chỗ dựa và thành khoe suông | Bốn tuần và việc cần giải cho khách ở từng tuần đã chốt | Ba trong bốn tuần đang có cổng cứng chưa mở: tuần 2, tuần 3 và tuần 4 | Chủ Y Viện |
| TL-RA-11 | Lời kêu gọi | Chỉ mời theo dõi Page, lưu bài, chia sẻ — chưa mời đặt lịch, chưa mời mua | Ba lời mời này là trần cứng cho tới khi cổng chào bán mở. Bài nào vượt trần thì chặn ở khâu duyệt | Trần lời kêu gọi đã chốt và áp cho cả 28 ngày | Cổng chào bán cần dịch vụ cụ thể, đầu mối, thời gian phản hồi và thông báo riêng tư | Chủ Y Viện |
| TL-RA-12 | Điểm xuất phát đo lường | Page mới, không người theo dõi, không dữ liệu cũ | Vì xuất phát từ số không nên cấm mọi cách nói phần trăm tăng trưởng. Số đếm thật mới có nghĩa | Người theo dõi bắt đầu từ 0. Mức nhận biết ghi là không đo được | Chọn cách đo mức nhận biết, hoặc quyết bỏ chỉ số này khỏi chu kỳ | Chủ Y Viện |
| TL-RA-13 | Bộ chỉ số | Mười hai chỉ số, mỗi chỉ số có ngưỡng tiếp tục, ngưỡng sửa và ngưỡng dừng | Cuối mỗi cửa sổ đo, ba ngưỡng cho ra một trong ba kết luận. Không có ngưỡng thì mọi con số đều biện minh được | Mười hai chỉ số, nguồn đo, cửa sổ đo và ba ngưỡng đều đã ghi rõ | Hai chỉ số chưa có mốc xuất phát: hỏi dịch vụ nghiêm túc và mức nhận biết thương hiệu | Chủ Y Viện |
| TL-RA-14 | Ba thử nghiệm | Tuần 1 thử kiểu mở bài, tuần 3 thử định dạng, tuần 4 thử cơ cấu trụ | Mỗi thử nghiệm gắn vào đúng những ngày của tuần đó, nên chạy lịch là chạy luôn thử nghiệm | Ba thử nghiệm, chỉ số quyết định và cách đọc kết quả đã chốt | Cả ba chưa chạy. Kết luận chốt ở cuối chu kỳ C1 | Chủ Y Viện |
| TL-RA-15 | Tuyến duyệt | Bài thường qua một cửa, bài chạm sức khoẻ qua hai cửa, bài chạm người thật hoặc pháp lý qua ba cửa | Tuyến duyệt quyết định thời gian chờ. Xếp lịch mà quên tuyến ba cửa thì tuần đó trễ | Ba tuyến và cách gán tuyến theo mức rủi ro đã chốt | Tuyến hai và ba đang thiếu người có chuyên môn ký. Chưa có tên người thì bài đứng lại | Cổng sức khoẻ |
| TL-RA-16 | Cổng người thật | Máy rà được nhiều thứ, nhưng chỉ chủ Y Viện mới ký duyệt đăng | Không có bài nào tự lên. Trạng thái cao nhất mà máy đặt được là cần người duyệt | Cổng người thật là bắt buộc cho từng bài, không duyệt gộp cả tuần | Không còn gì phải chốt. Đây là luật quản trị | Chủ Y Viện |
| TL-RA-17 | Câu miễn trừ sức khoẻ | Một đoạn nói rõ sản phẩm và liệu trình chỉ hỗ trợ, không thay chẩn đoán hay điều trị | Năm Reel chạm sức khoẻ đều phải mang câu này và giữ đủ lâu để người xem đọc kịp | Nội dung câu miễn trừ đã chốt nguyên văn, không được rút gọn | Chưa chốt đặt câu này ở đâu: đọc trong video, chèn chữ trên hình, hay dòng đầu phần mô tả | Cổng sức khoẻ |
| TL-RA-18 | Quyền dùng tư liệu | Ai xuất hiện trong hình đều phải đồng ý bằng văn bản trước khi quay | Chín nhóm tư liệu đang chưa xác lập quyền. Không có văn bản thì phần con người bị cắt, chỉ còn không gian | Nguyên tắc đã chốt: không có đồng ý thì không quay và không đăng | Chưa có chính sách chung về ai giữ bản gốc, dùng ở kênh nào, trong bao lâu và rút lại thế nào | Cổng pháp lý |

---

## 4. Bảng B — luật dẫn xuất 84 dòng

Bảng B là bản đọc của `YV_09_content_calendar`, **không** phải một nguồn thứ hai. Trình biên dịch
nổ 28 dòng lịch thành 84 dòng theo cột `Ba hướng A / B / C`, rồi điền chín cột hiển thị theo bảng
dưới. Số dòng ra khác 84 × số chu kỳ thì dừng kèm mã ngày và chuỗi gốc, cấm nhân bản A = B = C.

| Mã | Cột của Bảng B | Lấy từ đâu | Luật điền | Chủ sở hữu |
|---|---|---|---|---|
| TL-RB-01 | Ngày | `YV_09_content_calendar`, cột Ngày | Chép nguyên nhãn tương đối `D-1` … `D-28`, không zero-pad, không quy ra ngày thật | Chủ Y Viện |
| TL-RB-02 | Hướng | Sinh khi nổ dòng | `A`, `B`, `C` theo đúng thứ tự tách được từ chuỗi gốc; ba hướng của cùng một ngày phải khác nhau | Codex |
| TL-RB-03 | Trụ nội dung | `YV_09_content_calendar`, cột Trụ nội dung | Chép tên trụ tiếng Việt, giống hệt cả ba hướng của cùng một ngày | Chủ Y Viện |
| TL-RB-04 | Định dạng | `YV_09_content_calendar`, cột Định dạng | Chép cho hướng A. Hướng B và C dùng định dạng ghi trong chính chuỗi option nếu có, không có thì chép của A | Chủ Y Viện |
| TL-RB-05 | Nói gì | Chuỗi `Ba hướng A / B / C` | Phần nội dung của từng option sau khi tách bằng dấu ` · `. Dấu này chỉ dùng để tách hướng, không dùng trong lời | Chủ Y Viện |
| TL-RB-06 | Vì sao chọn / đánh đổi | `YV_09_content_calendar`, cột Angle chính và cột Ba hướng | Hướng A ghi lý do chọn. Hướng B và C mở đầu `DỰ PHÒNG — ` rồi nêu đánh đổi. B và C **không bao giờ** tô vàng | Chủ Y Viện |
| TL-RB-07 | Kêu gọi | `YV_09_content_calendar`, cột Kêu gọi | Chỉ nhận theo dõi Page, lưu bài, chia sẻ. Giá trị ngoài ba cái này thì dừng | Chủ Y Viện |
| TL-RB-08 | Ai duyệt | `YV_09_content_calendar`, cột Tuyến duyệt | Chép nguyên `R1`, `R1+R2` hoặc `R1+R2+R3`. Ba hướng cùng ngày dùng chung tuyến của ngày đó | Cổng sức khoẻ |
| TL-RB-09 | Trạng thái | `YV_09_content_calendar`, cột Trạng thái duyệt | Chép nguyên, không nâng cấp. Hiện chu kỳ C1 có 14 ngày ở mức cần người duyệt, 14 ngày ở mức bản nháp; không ngày nào `APPROVED` | Chủ Y Viện |

---

## 5. Bảng C — Ghép luồng vận hành

| Mã | Bước | Việc cần làm | Đầu vào từ tab | Kết quả ra | Ai làm | Chặn bởi |
|---|---|---|---|---|---|---|
| TL-RC-01 | 1 | Mở tab Y Viện cần chốt, xử lý trước tám dòng mức chặn ngay | 00_Y_VIEN_CAN_CHOT | Tám việc chặn ngay có tên người và có ngày | Chủ Y Viện | Không chặn — đây là bước mở đầu |
| TL-RC-02 | 2 | Chỉ định người có chuyên môn rà nội dung sức khoẻ và ghi tên vào tuyến duyệt | 00_Y_VIEN_CAN_CHOT, YV_12_workflow_approval | Tuyến hai cửa và ba cửa có người ký thật | Chủ Y Viện | Hồ sơ chuyên môn của người rà chưa nộp |
| TL-RC-03 | 3 | Ký giấy đồng ý hình ảnh cho từng người sẽ xuất hiện, kèm phạm vi được nói của founder | 00_Y_VIEN_CAN_CHOT, YV_11_asset_batch_plan | Danh sách người được lên hình, có chữ ký | Cổng pháp lý | Chính sách quyền dùng tư liệu chưa chốt |
| TL-RC-04 | 4 | Chốt phân vai quay, dựng, duyệt rồi quy ra số bài làm được một tuần | 00_Y_VIEN_CAN_CHOT, YV_11_asset_batch_plan | Năng lực sản xuất thật của một tuần | Chủ Y Viện | Chưa có ngày bắt đầu đăng nên chưa quy được về lịch thật |
| TL-RC-05 | 5 | Quay và dựng theo bốn mẻ, mỗi mẻ gom tư liệu của một tuần | YV_11_asset_batch_plan, YV_10_production_briefs | Chín nhóm tư liệu sẵn dùng | Chủ Y Viện | Hai nhóm có người xuất hiện đang chờ giấy đồng ý |
| TL-RC-06 | 6 | Viết bài và Reel theo brief, mỗi ngày lấy hướng A làm chính | YV_10_production_briefs, YV_09_content_calendar | 28 bản nháp, mỗi ngày một bản | Chủ Y Viện | Hai ngày chạm sản phẩm đang chạy hướng đóng an toàn |
| TL-RC-07 | 7 | Đưa từng bản nháp qua tuyến duyệt đúng mức rủi ro, rà từ cấm và câu miễn trừ | YV_12_workflow_approval, 06_COMPLIANCE_RULES | Bản nháp có kết luận duyệt của người thật | Cổng sức khoẻ | Chưa chốt chỗ đặt câu miễn trừ trong Reel |
| TL-RC-08 | 8 | Đăng theo lịch, ghi số đo vào từng cửa sổ, đọc ba ngưỡng rồi kết luận tiếp tục, sửa hay dừng | YV_09_content_calendar, 05_KPI_DICTIONARY, YV_08_experiments | Số đo từng cửa sổ và kết luận ba thử nghiệm | Chủ Y Viện | Hai chỉ số chưa có mốc xuất phát |
| TL-RC-09 | 9 | Hết ngày 28, ghi một dòng chốt chu kỳ rồi mở chu kỳ kế tiếp bằng đúng bộ tab này | 04_DECISIONS, YV_08_experiments | Chu kỳ C1 đóng, chu kỳ C2 mở | Chủ Y Viện | Chờ đủ dữ liệu của cả 28 ngày |

Không tạo tab mới khi mở chu kỳ kế tiếp. Chu kỳ mới ghi thêm dòng với mã chu kỳ `C2`, dùng lại đúng
21 tab hiện có.

---

## 6. VERIFY

- [x] Ba bảng đúng ba section: §3 → A (18 dòng, trong khoảng 10–40), §4 → luật dẫn xuất B (9 dòng),
      §5 → C (9 dòng, trong khoảng 6–20).
- [x] Bảng B **không** viết tay; §4 chỉ khai luật, 84 dòng do trình biên dịch nổ ra từ
      `YV_09_content_calendar`, dừng nếu số dòng khác 84 × số chu kỳ.
- [x] Cột `Cách hiểu đơn giản` không dòng nào lặp lại nguyên văn cột `Hạng mục`.
- [x] Tab này có **0 ô vàng**; lý do ghi ở §1 điều 3. Không ô nào mang tiền tố `CHƯA CHỐT — `.
- [x] Không dòng nào nâng trạng thái. `TL-RB-09` ghi rõ chép nguyên, không nâng cấp; chu kỳ C1 không
      ngày nào `APPROVED`.
- [x] Không ngày tuyệt đối. Nhãn ngày giữ dạng `D-1` … `D-28`.
- [x] Lời kêu gọi chỉ gồm theo dõi Page, lưu bài, chia sẻ (`TL-RA-11`, `TL-RB-07`).
- [x] Không xưng hô `bạn` hay `quý khách`; khách gọi là chị hoặc anh, brand gọi là Y Viện.
- [x] Từ cấm chỉ xuất hiện trong dòng luật cấm (`TL-RA-07`), không xuất hiện như lời nói của brand.
- [x] `Đầu vào từ tab` chỉ chứa khoá tab đã khai trong registry; Sheet hiển thị tên tiếng Việt tra từ
      `display_label_map.tab_title`.
- [x] Không ô nào bắt đầu bằng `+`, `=`, `-`, `@`.
