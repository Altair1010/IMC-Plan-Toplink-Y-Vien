# Luật phát ngôn và sổ câu claim

- **Mã tài liệu:** `TL-COMPLIANCE-001`
- **Tab đích:** `06_COMPLIANCE_RULES` (registry `YV-SHEET-001/1.0.0`, index 8)
- **Trạng thái:** `DRAFT · LOCAL_ONLY` — không câu nào ở đây là `APPROVED`; đây là ranh giới soạn
  thảo, không phải giấy phép đăng
- **Nguồn:** `docs/system/yvien-brand-voice-pack.md` §5 · `docs Toplink/content/month-calendar.md` §1
  · `docs Toplink/system/owner-decisions.md` · `STATE.md` §quyết định

---

## 1. Quy ước bảng

Theo `docs Toplink/brand/dmp-profile.md §1`. Riêng tab này thêm năm luật:

1. **Một bảng, hai nhóm.** Cột `Nhóm` là cột phân loại gộp: `Luật` là ranh giới chung áp cho mọi
   nội dung; `Câu claim` là từng phát ngôn cụ thể có mã tra được. Sheet đọc `Nhóm` để tách hai vùng
   khi hiển thị.
2. **`Mã` vừa là khoá máy vừa là cột hiển thị.** Mọi mã `CL-*` rải trong lịch nội dung, brief sản
   xuất và sổ duyệt đều phải tra ngược về đúng một dòng ở đây. Mã luật dùng tiền tố `LP-`.
3. **`Được nói gì` là trần, không phải bản mẫu.** Người viết không được copy nguyên câu ở cột này
   thành nội dung đăng; đó là ranh giới rộng nhất được phép, câu thật vẫn phải viết riêng và vẫn
   phải qua cổng người.
4. **`Cấm nói gì` thắng `Được nói gì` khi hai bên chạm nhau.** Nghi ngờ thì coi là cấm.
5. **Câu claim chưa có nội dung được duyệt vẫn phải có dòng.** Ghi rõ là chưa có, không bịa câu để
   lấp chỗ. Dòng đó tồn tại để mã không mồ côi và để việc còn treo nhìn thấy được.

Số dòng: **25**. Trong đó **14 dòng `Luật`** và **11 dòng `Câu claim`**.

---

## 2. Bảng chính

| Mã | Nhóm | Mức rủi ro | Loại phát ngôn | Được nói gì | Cấm nói gì | Ai duyệt | Cổng người | Chủ sở hữu |
|---|---|---|---|---|---|---|---|---|
| LP-01 | Luật | health | Khung ngôn ngữ an toàn | Mọi câu chạm tới cơ thể phải đứng trong khung hỗ trợ: `hỗ trợ`, `góp phần`, `giúp cơ thể dễ chịu hơn`, kèm câu nhắc không thay thế tư vấn y khoa chuyên môn | Bất kỳ cách nói nào ám chỉ chữa khỏi, dứt điểm, cam kết kết quả, hoặc thay thế vai trò của bác sĩ | Người rà chuyên môn sức khoẻ | Cổng sức khoẻ | Cổng sức khoẻ |
| LP-02 | Luật | health | Từ cấm tuyệt đối | — | `chữa khỏi`, `cam kết khỏi`, `điều trị dứt điểm`, `thay thế bác sĩ`, `thần dược`, `đặc trị`, `khỏi hẳn`, `hết bệnh`. Cấm cả biến thể viết tắt, viết lái và viết tách chữ | Người rà chuyên môn sức khoẻ | Cổng sức khoẻ | Cổng sức khoẻ |
| LP-03 | Luật | none | Từ cấm bán hàng | Lời mời nhẹ: `theo dõi Page`, `lưu bài`, `chia sẻ cho người cần` | `mua ngay`, `chốt đơn ngay`, `số lượng có hạn`, `giá sốc`, đếm ngược giả, khan hiếm giả | Chủ Y Viện | Không cần cổng riêng | Bên làm kế hoạch |
| LP-04 | Luật | none | Xưng hô | Gọi người đọc là `chị` hoặc `anh`, nữ trước. Thương hiệu tự xưng `Y Viện` ở ngôi thứ ba | `bạn`, `quý khách`, `khách hàng thân mến`; hạn chế tối đa `chúng tôi` | Chủ Y Viện | Không cần cổng riêng | Bên làm kế hoạch |
| LP-05 | Luật | health | Câu miễn trừ | Nội dung chạm sức khoẻ phải mang câu miễn trừ. Nơi đặt câu chưa chốt: đọc trong lời thoại, hay chèn chữ trên hình, hay để trong phần mô tả | Đăng nội dung sức khoẻ mà không có câu miễn trừ ở bất kỳ vị trí nào | Người rà chuyên môn sức khoẻ | Cổng sức khoẻ | Cổng sức khoẻ |
| LP-06 | Luật | none | Lời kêu gọi | Trước khi cổng chào bán mở, lời kêu gọi chỉ được nằm trong ba việc: theo dõi Page, lưu bài, chia sẻ | Mời nhắn tin, mời đặt lịch, mời để lại số điện thoại, dẫn sang trang bán, nêu giá | Chủ Y Viện | Cổng chạy thử Page | Chủ Y Viện |
| LP-07 | Luật | product-adjacent | Phát ngôn sản phẩm | Khi chưa có hồ sơ sản phẩm kiểm chứng được: chỉ mô tả cảm nhận chung và nguyên lý dưỡng sinh, không gắn với một sản phẩm cụ thể | Nêu tên sản phẩm kèm công dụng, nêu thành phần kèm tác dụng, nêu giá, nêu kết quả mong đợi | Người rà chuyên môn sức khoẻ | Cổng sức khoẻ | Cổng sức khoẻ |
| LP-08 | Luật | legal-privacy | Phát ngôn pháp lý | — | Mọi cách nói công khai về quan hệ nhượng quyền, tên pháp lý đầy đủ, giấy phép hoạt động, phạm vi hành nghề đăng ký. Chủ Y Viện đã quyết giữ khoá | Chủ Y Viện | Cổng pháp lý | Cổng pháp lý |
| LP-09 | Luật | legal-privacy | Hình ảnh người thật | Người xuất hiện trong ảnh hoặc video phải có đồng ý bằng văn bản, ghi rõ dùng ở đâu, dùng bao lâu, gỡ thế nào | Dùng hình người chưa ký đồng ý; dùng hình khách; dùng hình lấy từ nguồn khác mà chưa gỡ quyền | Chủ Y Viện | Cổng pháp lý | Cổng pháp lý |
| LP-10 | Luật | founder | Phát ngôn người sáng lập | Người sáng lập chỉ nói trong phạm vi đã được xác nhận bằng văn bản: hành trình cá nhân, lý do làm nghề, quan sát nghề | Nêu bằng cấp, nêu số năm kinh nghiệm, nêu chức danh chuyên môn, nêu ca đã làm, khi chưa có giấy tờ | Chủ Y Viện | Cổng người sáng lập | Chủ Y Viện |
| LP-11 | Luật | legal-privacy | Chứng thực khách hàng | — | Mọi dạng chứng thực khách hàng: lời khen dẫn lại, ảnh trước sau, tin nhắn cảm ơn, đánh giá sao. Chưa có quy trình lấy đồng ý và chưa có cổng duyệt | Chủ Y Viện | Cổng pháp lý | Cổng pháp lý |
| LP-12 | Luật | none | Số liệu và mốc thời gian | Chỉ nêu con số khi có nguồn tra được, và ghi rõ nguồn | Nêu số năm hoạt động, số khách, số chi nhánh, tỷ lệ hài lòng, hoặc bất kỳ con số nào lấy từ trang giới thiệu chưa kiểm chứng | Chủ Y Viện | Không cần cổng riêng | Bên làm kế hoạch |
| LP-13 | Luật | legal-privacy | Dữ liệu riêng tư | Khi cổng chào bán mở, phải có câu thông báo riêng tư trước khi nhận bất kỳ thông tin cá nhân nào | Thu thập số điện thoại, tên, tình trạng sức khoẻ qua tin nhắn hoặc bình luận khi chưa có thông báo riêng tư | Chủ Y Viện | Cổng pháp lý | Cổng pháp lý |
| LP-14 | Luật | health | Ngôn ngữ Đông y | Dùng từ vựng lõi đúng nghĩa: `khí huyết`, `kinh lạc`, `dưỡng sinh`, `thể trạng`, `thảo dược`, và bốn trạng thái `Tĩnh · Thông · Dưỡng · Tỉnh` | Huyền bí hoá: nói về vận mệnh, phong thuỷ, năng lượng vũ trụ, chữa lành tâm linh, hoặc gán hiệu quả cho yếu tố không giải thích được | Người rà chuyên môn sức khoẻ | Cổng sức khoẻ | Cổng sức khoẻ |
| CL-ID1 | Câu claim | none | Định danh | Y Viện là nơi chăm sóc theo hướng dưỡng sinh Đông y, đặt việc lắng nghe cơ thể lên trước việc can thiệp | Gắn định danh với bất kỳ danh xưng nghề y nào, hoặc với quan hệ thương hiệu chưa có văn bản | Chủ Y Viện | Không cần cổng riêng | Chủ Y Viện |
| CL-M1 | Câu claim | health | Phương pháp | Nói được rằng cách làm bắt đầu từ quan sát thể trạng của từng người trước khi chọn cách chăm sóc | Nói cách làm phù hợp mọi người, hoặc cho kết quả giống nhau ở mọi người | Người rà chuyên môn sức khoẻ | Cổng sức khoẻ | Cổng sức khoẻ |
| CL-M2 | Câu claim | health | Phương pháp | Nói được rằng cơ thể phát tín hiệu sớm trước khi thành vấn đề, và học đọc tín hiệu đó là việc làm được hằng ngày | Quy một dấu hiệu cụ thể về một bệnh cụ thể; hướng dẫn tự chẩn đoán; khuyên ngưng điều trị đang có | Người rà chuyên môn sức khoẻ | Cổng sức khoẻ | Cổng sức khoẻ |
| CL-M3 | Câu claim | health | Phương pháp | Nói được rằng chăm sóc đều đặn và vừa sức có ích hơn một lần làm mạnh rồi bỏ | Cam kết mốc thời gian thấy kết quả; đưa lộ trình số buổi kèm hiệu quả | Người rà chuyên môn sức khoẻ | Cổng sức khoẻ | Cổng sức khoẻ |
| CL-M4 | Câu claim | health | Phương pháp | Nói được rằng nghỉ ngơi, hơi thở và giấc ngủ là phần của việc chăm sóc, không phải phần phụ | Gán cho giấc ngủ hay hơi thở khả năng thay thế điều trị y khoa | Người rà chuyên môn sức khoẻ | Cổng sức khoẻ | Cổng sức khoẻ |
| CL-OP1 | Câu claim | none | Vận hành | Nói được rằng mỗi lượt chăm sóc bắt đầu bằng một bước hỏi và quan sát trước khi làm | Mô tả bước hỏi như một bước khám bệnh; dùng từ chẩn đoán, chỉ định, phác đồ | Chủ Y Viện | Không cần cổng riêng | Chủ Y Viện |
| CL-OP2 | Câu claim | none | Vận hành | Nói được về không gian, dụng cụ và cách giữ vệ sinh ở mức mô tả trung thực | Nói `đạt chuẩn` mà không nêu đúng tên chuẩn và bên cấp | Chủ Y Viện | Không cần cổng riêng | Chủ Y Viện |
| CL-OP3 | Câu claim | none | Vận hành | Nói được rằng người làm được hướng dẫn theo một quy trình thống nhất | Nêu bằng cấp, chứng chỉ hoặc số giờ đào tạo khi chưa có giấy tờ | Chủ Y Viện | Cổng pháp lý | Cổng pháp lý |
| CL-CX1 | Câu claim | none | Trải nghiệm | Nói được về cảm giác chung khi cơ thể được nghỉ: vai thả xuống, hơi thở dài hơn, đầu nhẹ hơn | Mô tả cảm giác như một kết quả chắc chắn sẽ xảy ra với mọi người | Chủ Y Viện | Không cần cổng riêng | Bên làm kế hoạch |
| CL-FD1 | Câu claim | founder | Người sáng lập | Nói được lý do người sáng lập chọn hướng dưỡng sinh, ở mức câu chuyện cá nhân | Mọi chi tiết về đào tạo, chức danh, kinh nghiệm nghề, khi chưa có văn bản xác nhận phạm vi được nói | Chủ Y Viện | Cổng người sáng lập | Chủ Y Viện |
| CL-P2 | Câu claim | health | Phương pháp | CHƯA CÓ NỘI DUNG ĐƯỢC DUYỆT. Trụ nội dung về đọc tín hiệu cơ thể đang mượn tạm ranh giới của `CL-M2`. Chủ Y Viện cần quyết: viết một câu riêng cho trụ này, hay chính thức gộp vào `CL-M2` | Dùng mã này trong brief hoặc lịch nội dung khi chưa có quyết định | Người rà chuyên môn sức khoẻ | Cổng sức khoẻ | Cổng sức khoẻ |

---

## 3. Ghi chú đọc bảng

Mười bốn dòng `Luật` áp cho mọi nội dung, kể cả nội dung không gắn mã claim nào. Mười một dòng
`Câu claim` là những gì Y Viện được phép khẳng định; mỗi mã phải tra ngược được từ lịch nội dung,
brief sản xuất và sổ duyệt.

Ba mức rủi ro chiếm phần lớn bảng: `health` cho mọi thứ chạm cơ thể, `legal-privacy` cho hình ảnh
và dữ liệu người thật, `founder` cho phát ngôn cá nhân. Ba mức này đều dừng ở một cổng người —
không cổng nào tự mở bằng máy.

Dòng `CL-P2` là dòng duy nhất chưa có nội dung. Nó không bị xoá vì hai lý do: mã đã từng xuất hiện
trong tài liệu cũ nên phải tra được, và trụ nội dung tương ứng vẫn cần một ranh giới rõ ràng. Việc
quyết nằm ở `TL-OA-14`.

---

## 4. VERIFY

- Đúng **25 dòng**, mã duy nhất, khớp `min_records: 10` · `max_records: 210`.
- `Nhóm` chỉ nhận `Luật` (14) hoặc `Câu claim` (11), khớp `compliance_group`.
- `Mức rủi ro` chỉ nhận giá trị thuộc `risk_class`: `none` 10 · `health` 11 · `legal-privacy` 3 ·
  `founder` 1 · `product-adjacent` 1. Không dòng nào để trống.
- Mọi mã `CL-*` dùng ở `YV_09`, `YV_10`, `YV_12` phải nằm trong 11 mã ở đây; mã ngoài danh sách =
  `VALIDATION_FAILED`.
- **0 ô vàng** ở tab này (`expected_yellow_count: 0`): ranh giới là luật, không phải việc cần chốt.
  Việc treo của `CL-P2` và của câu miễn trừ đã có ô vàng ở `00_Y_VIEN_CAN_CHOT`
  (`TL-OA-14`, `TL-OA-13`).
- Cột hiển thị không chứa mã `TL-*` hay `YV-*`. Chỉ `CL-*` và `LP-*` được phép hiện, khai bằng
  `visible_id_allowed`.
- Không ô nào bắt đầu bằng `+`, `=`, `-`, `@`. Ô trống có nghĩa ghi `—`.
