# Sổ việc chủ Y Viện cần chốt

- **Mã tài liệu:** `TL-OWNER-DECISIONS-001`
- **Tab đích:** `00_Y_VIEN_CAN_CHOT` (registry `YV-SHEET-001/1.0.0`, index 1)
- **Trạng thái:** `DRAFT · LOCAL_ONLY` — không dòng nào ở đây là `APPROVED`
- **Nguồn:** `docs Toplink/system/runtime-compatibility.md` · `docs Toplink/brand/campaign-architecture.md`
  · `docs Toplink/brand/kpi-experiment-plan.md` · `docs Toplink/content/asset-and-batch-plan.md`
  · `docs Toplink/content/reels-briefs.md` · `docs Toplink/content/workflow-approval-measurement.md`
  · `docs Toplink/TOPLINK_PAGE_MILESTONES.md` §sổ thiếu đầu vào · `STATE.md` §quyết định

---

## 1. Quy ước bảng

Theo `docs Toplink/brand/dmp-profile.md §1`. Riêng tab này thêm bốn luật:

1. **Cột `STT` do trình biên dịch sinh**, đánh số 1, 2, 3… theo đúng thứ tự dòng ở §2. Markdown
   không viết cột này. `STT` **không** phải mã việc.
2. **Đối xứng ô vàng.** Mỗi ô vàng ở 20 tab còn lại phải có đúng một dòng ở đây; ngược lại mỗi dòng
   ở đây có `Trạng thái = OPEN` mang đúng một ô vàng của chính nó ở cột `Cần chốt điều gì`.
3. **Dòng đã có quyết định thì không vàng.** Hợp đồng ô vàng đòi *đồng thời* trạng thái mở **và**
   một hành động của người thật còn treo. Việc mà chủ Y Viện đã quyết giữ khoá, hoặc bị chặn theo
   thiết kế, vẫn đứng trong sổ để không ai quên — nhưng `Trạng thái` ghi `DECIDED` hoặc `BLOCKED`
   và ô **không** tô vàng. Tô vàng một việc đã quyết là báo động giả.
4. **`Chặn cái gì` và `Đầu vào từ tab` ghi khoá tab máy**; Sheet hiển thị tên tiếng Việt tra từ
   `display_label_map.tab_title` và `display_label_map.milestone_gate`. Trong tệp này ghi giá trị máy.

Số dòng: **23**. Trong đó **18 dòng vàng** (`OPEN`) và **5 dòng không vàng** (`BLOCKED` theo quyết
định hoặc theo thiết kế). Cộng với 9 ô vàng ở tab nguồn, cả workbook có **27 ô vàng**.

---

## 2. Bảng chính

| Mã | Mức ưu tiên | Nhóm việc | Cần chốt điều gì | Vì sao đang chặn | Chặn cái gì | Ai quyết | Hạn / cổng | Trạng thái | Ngày quyết | Nội dung quyết | Ghi chú | Chủ sở hữu |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TL-OA-01 | CHẶN NGAY | Chuyên môn sức khoẻ | CHƯA CHỐT — chủ Y Viện cần chỉ định người có chuyên môn rà từng bài tuần 2; chưa có tên người thì cả tuần không đăng được | Bảy ngày của tuần 2 nói về tín hiệu cơ thể. Không ai đủ chuyên môn ký thì mọi bài đều dừng ở cổng sức khoẻ | YV_07_campaign, YV_09_content_calendar, YV_12_workflow_approval, TL-M5 | Chủ Y Viện | Trước khi đăng D-8 | OPEN | — | — | Ô vàng gốc ở tab Chiến dịch, dòng Tuần 2, cột Cổng cứng | Cổng sức khoẻ |
| TL-OA-02 | CHẶN NGAY | Đồng ý hình ảnh | CHƯA CHỐT — chủ Y Viện cần xác nhận ai được lên hình ở tuần 3 và đã có đồng ý bằng văn bản chưa; chưa có thì bỏ hết phần con người, chỉ giữ không gian và quy trình | Tuần 3 là tuần bằng chứng vận hành. Phần đội ngũ cần đồng ý của từng người xuất hiện | YV_07_campaign, YV_11_asset_batch_plan, TL-M5 | Chủ Y Viện | Trước mẻ quay tuần 3 | OPEN | — | — | Ô vàng gốc ở tab Chiến dịch, dòng Tuần 3, cột Cổng cứng | Cổng pháp lý |
| TL-OA-03 | CAO | Hồ sơ sản phẩm | CHƯA CHỐT — chủ Y Viện chọn nhánh cho tuần 4: nộp hồ sơ một sản phẩm hoặc dịch vụ để mở nhánh có bằng chứng, hoặc giữ nhánh dự phòng an toàn | Chưa có hồ sơ nào kiểm chứng được thì không nói được gì về sản phẩm. Không chọn thì chạy nhánh dự phòng | YV_07_campaign, YV_09_content_calendar, TL-M5 | Chủ Y Viện | Trước khi lên brief D-22 | OPEN | — | — | Ô vàng gốc ở tab Chiến dịch, dòng Tuần 4, cột Cổng cứng. Không chọn cũng là một lựa chọn: mặc định là nhánh dự phòng | Chủ Y Viện |
| TL-OA-04 | TRUNG BÌNH | Đo lường | CHƯA CHỐT — chủ Y Viện cần mở cổng chào bán (dịch vụ cụ thể, điều kiện phù hợp, đầu mối, thời gian phản hồi, thông báo riêng tư) thì chỉ số hỏi dịch vụ nghiêm túc mới có mốc xuất phát | Chưa mở cổng chào bán thì không có gì để hỏi, nên chỉ số này không có mẫu số | 05_KPI_DICTIONARY, YV_06_page_strategy, TL-M6 | Chủ Y Viện | Trước khi mở cổng chào bán | OPEN | — | — | Ô vàng gốc ở tab Từ điển chỉ số, dòng Hỏi dịch vụ nghiêm túc | Chủ Y Viện |
| TL-OA-05 | TRUNG BÌNH | Đo lường | CHƯA CHỐT — chủ Y Viện cần chọn cách đo mức nhận biết thương hiệu: khảo sát nhỏ, hỏi trực tiếp tại cơ sở, hoặc bỏ chỉ số này khỏi chu kỳ | Chưa có nơi đo và chưa có cách tính. Giữ nguyên thì chỉ số nằm im, không sinh dữ liệu | 05_KPI_DICTIONARY, TL-M4 | Chủ Y Viện | Trước khi chốt chu kỳ C1 | OPEN | — | — | Ô vàng gốc ở tab Từ điển chỉ số, dòng Mức nhận biết thương hiệu. Bỏ chỉ số cũng là một kết luận hợp lệ | Chủ Y Viện |
| TL-OA-06 | CAO | Kênh liên hệ | CHƯA CHỐT — chủ Y Viện cần cấp số điện thoại, tài khoản Zalo và điểm Google Maps chính thức kèm người giữ đầu mối; chưa có thì cả ba kênh này không được xuất hiện trong bất kỳ lời kêu gọi nào | Ba kênh chưa đấu nối và chưa có người trực. Đưa lên bài mà không ai trả lời thì hỏng niềm tin nhanh hơn là không đưa | 00_CONTROL, YV_06_page_strategy, TL-M6 | Chủ Y Viện | Trước khi lời kêu gọi vượt khỏi theo dõi Page | OPEN | — | — | Ô vàng gốc ở tab Kiểm soát & runtime, dòng Vai trò kênh | Chủ Y Viện |
| TL-OA-07 | CHẶN NGAY | Đồng ý hình ảnh | CHƯA CHỐT — chủ Y Viện cần lấy đồng ý bằng văn bản của từng người xuất hiện trong video hậu trường, nêu rõ mục đích, kênh đăng, thời hạn và cách rút lại; chưa có thì bỏ hết phần con người, chỉ giữ không gian | Hậu trường có mặt nhân sự. Không có văn bản đồng ý thì không được quay và không được đăng | YV_11_asset_batch_plan, YV_09_content_calendar, TL-M5 | Chủ Y Viện | Trước mẻ quay tuần 3 | OPEN | — | — | Ô vàng gốc ở tab Kế hoạch tư liệu & mẻ quay, dòng Video hậu trường | Cổng pháp lý |
| TL-OA-08 | CHẶN NGAY | Đồng ý hình ảnh | CHƯA CHỐT — chủ Y Viện cần xác nhận phạm vi được nói của founder bằng văn bản và ký đồng ý cho hình ảnh; chưa có thì hai ngày founder chuyển sang nội dung không có founder | Founder nói ngoài phạm vi là rủi ro cao nhất của cả chu kỳ. Không có văn bản thì không có ranh giới để rà | YV_11_asset_batch_plan, YV_09_content_calendar, TL-M5 | Chủ Y Viện | Trước mẻ quay tuần 1 | OPEN | — | — | Ô vàng gốc ở tab Kế hoạch tư liệu & mẻ quay, dòng Video và ảnh founder | Cổng pháp lý |
| TL-OA-09 | CAO | Sản xuất | CHƯA CHỐT — chủ Y Viện cần chốt ai quay, ai dựng và ai duyệt; chưa chốt thì mặc định một người kiêm hết, và mọi cam kết về nhịp đăng chỉ là ước lượng | Không có phân vai thì không tính được năng lực thật của một tuần. Lịch 28 ngày đang đứng trên một ước lượng | YV_11_asset_batch_plan, YV_10_production_briefs, TL-M5 | Chủ Y Viện | Trước mẻ quay tuần 1 | OPEN | — | — | Ô vàng gốc ở tab Kế hoạch tư liệu & mẻ quay, dòng Phân vai sản xuất | Chủ Y Viện |
| TL-OA-10 | CHẶN NGAY | Chuyên môn sức khoẻ | CHƯA CHỐT — chủ Y Viện cần nộp bằng chứng chuyên môn của người rà nội dung sức khoẻ, và xác nhận người đó duyệt từng bài chứ không duyệt gộp cả tuần | Người rà đang được chủ Y Viện tự chứng thực, chưa có giấy tờ chuyên môn. Mọi bài chạm sức khoẻ vẫn phải duyệt từng bài | YV_12_workflow_approval, 06_COMPLIANCE_RULES, TL-M5 | Chủ Y Viện | Trước khi đăng bài sức khoẻ đầu tiên | OPEN | — | — | Sổ thiếu đầu vào `TL-GAP-007`. Khác với dòng cổng tuần 2: dòng này là hồ sơ chuyên môn, dòng kia là lịch trực tuần | Cổng sức khoẻ |
| TL-OA-11 | CHẶN NGAY | Ghi Sheet | CHƯA CHỐT — chủ Y Viện cần ký ba phê duyệt ghi Sheet riêng biệt (tạo tab, ghi dữ liệu, đọc lại kiểm chứng) bằng cách trích đường dẫn, mã băm SHA-256 và chữ APPROVED | Tài khoản dịch vụ và đích ghi đã sẵn sàng, nhưng sẵn sàng kỹ thuật không phải là phê duyệt ghi. Chưa ký thì Codex không được chạm workbook | 03_OUTPUT_INDEX, 04_DECISIONS, TL-M5H | Chủ Y Viện | Trước khi Codex chạy Phase 2 | OPEN | — | — | Sổ thiếu đầu vào `TL-GAP-008`. Ba phê duyệt là ba hành động tách rời, không gộp một chữ ký | Chủ Y Viện |
| TL-OA-12 | CHẶN NGAY | Quyền tư liệu | CHƯA CHỐT — chủ Y Viện cần chốt chính sách quyền dùng tư liệu cho cả chu kỳ: ai giữ bản gốc, dùng được ở kênh nào, trong bao lâu, và rút lại thế nào | Chín nhóm tư liệu đều chưa xác lập quyền dùng. Không có chính sách chung thì mỗi lần quay lại phải hỏi lại từ đầu | YV_11_asset_batch_plan, YV_10_production_briefs, TL-M5 | Chủ Y Viện | Trước mẻ quay tuần 1 | OPEN | — | — | Sổ thiếu đầu vào `TL-M5-ASSET-RIGHTS-001`. Bao trùm hai dòng đồng ý hình ảnh ở trên | Cổng pháp lý |
| TL-OA-13 | CHẶN NGAY | Nội dung | CHƯA CHỐT — chủ Y Viện cần chọn nơi đặt câu miễn trừ sức khoẻ: đọc trong video, chèn chữ trên hình, hay đặt ở dòng đầu phần mô tả; chọn xong thì áp cho cả năm Reel sức khoẻ | Câu miễn trừ đang có nội dung nhưng chưa có chỗ đứng cố định. Mỗi Reel đặt một kiểu thì rà không được | YV_10_production_briefs, 06_COMPLIANCE_RULES, TL-M5 | Chủ Y Viện | Trước khi dựng Reel sức khoẻ đầu tiên | OPEN | — | — | Phát hiện rà soát `TL-R2-F08`. Năm Reel liên quan: D-8, D-11, D-14, D-23, D-27 | Cổng sức khoẻ |
| TL-OA-14 | CAO | Nội dung | CHƯA CHỐT — chủ Y Viện cần quyết một trong hai: viết câu claim cho trụ Hiểu và lắng nghe tín hiệu cơ thể, hoặc xác nhận trụ này chạy không cần câu claim riêng | Trụ này đang trỏ tới một câu claim không tồn tại trong sổ luật phát ngôn. Brief nào tham chiếu tới nó cũng đứt | 06_COMPLIANCE_RULES, YV_05_content_pillars, YV_10_production_briefs, TL-M5 | Cổng sức khoẻ | Trước khi lên brief D-8 | OPEN | — | — | Phát hiện rà soát `TL-R2-F02`, câu claim mồ côi | Cổng sức khoẻ |
| TL-OA-15 | CAO | Sản xuất | CHƯA CHỐT — chủ Y Viện cần chốt ngày bắt đầu đăng thật và số bài một tuần làm được, để nhãn ngày tương đối quy được về lịch thật | Cả lịch đang chạy trên nhãn D-1 tới D-28 vì chưa có ngày gốc. Chưa có ngày gốc thì không hẹn được với ai | YV_09_content_calendar, YV_11_asset_batch_plan, TL-M6 | Chủ Y Viện | Trước khi mở chu kỳ C1 trên Page | OPEN | — | — | Sổ thiếu đầu vào `TL-GAP-006`. Đang được khoanh vùng cho giai đoạn soạn nội dung, chưa giải | Chủ Y Viện |
| TL-OA-16 | CAO | Hồ sơ sản phẩm | CHƯA CHỐT — chủ Y Viện cần nộp hồ sơ nguồn gốc, kiểm định và cơ sở của từng câu nói về sản phẩm trước khi bất kỳ câu nào rời khỏi mức trải nghiệm | Tệp nguồn sản phẩm đã có nhưng chưa qua kiểm chứng. Mọi nội dung chạm sản phẩm đang bị hạ xuống mức kể trải nghiệm | 06_COMPLIANCE_RULES, YV_10_production_briefs, TL-M1 | Chủ Y Viện | Trước khi nói bất kỳ công dụng nào | OPEN | — | — | Sổ thiếu đầu vào `TL-GAP-010`. Hai ngày liên quan sản phẩm hiện chạy theo hướng đóng an toàn | Cổng sức khoẻ |
| TL-OA-17 | TRUNG BÌNH | Hồ sơ sản phẩm | CHƯA CHỐT — chủ Y Viện cần nộp hồ sơ mô tả từng sản phẩm và từng dịch vụ đang thật sự cung cấp, kèm phạm vi và giới hạn của mỗi thứ | Chưa có danh mục nào được xác nhận thì không dựng được nhánh giải pháp cho tuần 4 | YV_07_campaign, 06_COMPLIANCE_RULES, TL-M1 | Chủ Y Viện | Trước khi mở nhánh có bằng chứng ở tuần 4 | OPEN | — | — | Sổ thiếu đầu vào `TL-GAP-004`. Chủ Y Viện đã báo sẽ cấp sau kèm hồ sơ pháp lý | Chủ Y Viện |
| TL-OA-18 | TRUNG BÌNH | Kênh liên hệ | CHƯA CHỐT — chủ Y Viện cần chốt cách đặt lịch, cách liên hệ, thời gian phản hồi cam kết và thông báo riêng tư trước khi lời kêu gọi được phép mời hành động thương mại | Chưa có bộ này thì mọi lời kêu gọi phải dừng ở theo dõi Page, lưu bài và chia sẻ | YV_06_page_strategy, YV_09_content_calendar, TL-M6 | Chủ Y Viện | Trước khi mở cổng chào bán | OPEN | — | — | Sổ thiếu đầu vào `TL-GAP-005` | Chủ Y Viện |
| TL-OA-19 | TRUNG BÌNH | Pháp lý | Giữ khoá mọi cách nói công khai về quan hệ nhượng quyền cho tới khi có giấy tờ trong tay | Chưa có bằng chứng công khai nào về quan hệ nhượng quyền. Chủ Y Viện đã quyết giữ khoá, nên không còn việc nào treo ở phía người | YV_01_brand_profile, YV_03_positioning, TL-M1 | Chủ Y Viện | Cổng pháp lý, chưa hẹn | BLOCKED | — | Giữ khoá | Sổ thiếu đầu vào `TL-GAP-002`. Đã quyết nên không tô vàng; mở lại khi có giấy tờ | Cổng pháp lý |
| TL-OA-20 | TRUNG BÌNH | Pháp lý | Giữ khoá mọi phát ngôn công khai về tên pháp lý, giấy phép và phạm vi hoạt động | Chưa có văn bản nào trong tay. Chủ Y Viện đã quyết giữ khoá cùng lượt với quan hệ nhượng quyền | YV_01_brand_profile, YV_06_page_strategy, TL-M1 | Chủ Y Viện | Cổng pháp lý, chưa hẹn | BLOCKED | — | Giữ khoá | Sổ thiếu đầu vào `TL-GAP-009`. Đã quyết nên không tô vàng | Cổng pháp lý |
| TL-OA-21 | TRUNG BÌNH | Nguồn gốc dữ liệu | Không tuyên bố kho nguồn hiện tại bằng với kho nguồn lịch sử đầy đủ | Chỉ có một bản kiểm kê khoanh vùng từ dự án gốc. Đây là giới hạn theo thiết kế, không phải việc chủ Y Viện phải làm | 01_SOURCE_INVENTORY, 00_CONTROL, TL-M1 | Codex | Đóng theo thiết kế | BLOCKED | — | Đóng an toàn theo thiết kế | Sổ thiếu đầu vào `TL-GAP-012`. Giữ trong sổ để không ai nhầm là đã đủ | Codex |
| TL-OA-22 | TRUNG BÌNH | Nguồn gốc dữ liệu | Không suy rộng nguồn gốc trường dữ liệu hồ sơ ra ngoài phần bằng chứng đã khoanh vùng | Chỉ có con trỏ hồ sơ gốc và một bản sao lưu trước sửa. Giới hạn theo thiết kế | 01_SOURCE_INVENTORY, YV_01_brand_profile, TL-M2 | Codex | Đóng theo thiết kế | BLOCKED | — | Đóng an toàn theo thiết kế | Sổ thiếu đầu vào `TL-GAP-013` | Codex |
| TL-OA-23 | TRUNG BÌNH | Nguồn gốc dữ liệu | Không tuyên bố lịch sử quyết định và đối chiếu cũ là đầy đủ | Chỉ có con trỏ tệp quyết định gốc kèm mã băm. Giới hạn theo thiết kế | 04_DECISIONS, 01_SOURCE_INVENTORY, TL-M1 | Codex | Đóng theo thiết kế | BLOCKED | — | Đóng an toàn theo thiết kế | Sổ thiếu đầu vào `TL-GAP-014` | Codex |

---

## 3. Đọc bảng này thế nào

- **CHẶN NGAY** nghĩa là chưa chốt thì có nội dung không đăng được, hoặc có buổi quay không diễn ra
  được. Tám dòng đang ở mức này.
- **CAO** nghĩa là chốt muộn thì phải làm lại việc đã làm. Sáu dòng.
- **TRUNG BÌNH** nghĩa là chưa chốt vẫn chạy được chu kỳ C1, nhưng chu kỳ C2 sẽ vướng. Chín dòng,
  trong đó hai dòng pháp lý đã quyết giữ khoá và ba dòng nguồn gốc dữ liệu đóng theo thiết kế.
- Ba dòng cuối không phải việc của chủ Y Viện. Chúng là giới hạn nguồn gốc dữ liệu, giữ trong sổ
  để không ai nhầm rằng kho nguồn hiện tại là đầy đủ.

Không dòng nào ở đây tự chuyển sang `DECIDED`. Chỉ chủ Y Viện đặt được `DECIDED`, và khi đặt thì
phải điền cả `Ngày quyết` lẫn `Nội dung quyết`. Trình biên dịch không được phép nâng trạng thái.

---

## 4. VERIFY

- [x] Đúng 23 dòng, mã `TL-OA-01` … `TL-OA-23`, không trùng.
- [x] 18 dòng `OPEN` mở đầu cột `Cần chốt điều gì` bằng `CHƯA CHỐT — `, mỗi dòng nêu rõ *ai quyết* và
      *chốt điều gì*.
- [x] 5 dòng `BLOCKED` **không** mang tiền tố `CHƯA CHỐT — ` và **không** được tô vàng.
- [x] 9 ô vàng ở tab nguồn (`YV_07` ×3, `05_KPI_DICTIONARY` ×2, `00_CONTROL` ×1, `YV_11` ×3) đều có
      đúng một dòng đối ứng: `TL-OA-01` … `TL-OA-09`.
- [x] Mỗi `TL-GAP-*` đang mở có đúng một dòng: 004→`TL-OA-17`, 005→`TL-OA-18`, 006→`TL-OA-15`,
      007→`TL-OA-10`, 008→`TL-OA-11`, 010→`TL-OA-16`, ASSET→`TL-OA-12`, 002→`TL-OA-19`,
      009→`TL-OA-20`, 012→`TL-OA-21`, 013→`TL-OA-22`, 014→`TL-OA-23`.
- [x] Hai phát hiện rà soát còn mở có dòng riêng: `TL-R2-F02`→`TL-OA-14`, `TL-R2-F08`→`TL-OA-13`.
- [x] Không dòng nào mang trạng thái `APPROVED`. `Ngày quyết` và `Nội dung quyết` để `—` ở mọi dòng
      chưa quyết.
- [x] Cột `STT` không có trong markdown; trình biên dịch sinh 1…23 theo thứ tự dòng.
- [x] `Chặn cái gì` chỉ chứa khoá tab đã khai trong registry và mã cổng `TL-M1` / `TL-M2` / `TL-M4` /
      `TL-M5` / `TL-M5H` / `TL-M6`, đúng danh sách `allow_values`.
- [x] Không ngày tuyệt đối. Không xưng hô `bạn` hay `quý khách`. Không từ cấm.
- [x] Không ô nào bắt đầu bằng `+`, `=`, `-`, `@`.
