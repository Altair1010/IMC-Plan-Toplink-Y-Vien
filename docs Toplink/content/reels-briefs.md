# TL-M5 — Brief Reel (Toplink Y Viện)

> **Run 1 Phase A · chỉ chạy nội bộ · `external_writes=0`.** Tệp này giữ brief cho **12 mục Reel**. 16
> mục dạng bài tĩnh và carousel nằm ở `production-briefs.md`; hai tệp đổ chung vào một tab và phân
> biệt bằng cột `Loại brief`. **Reel trên Facebook là kênh đăng; TikTok chỉ để tham chiếu cơ chế**,
> không đăng trong chu kỳ này. Không Reel nào `APPROVED`, không Reel nào sẵn sàng đăng.

## 0. Khối định danh

| Trường | Giá trị |
|---|---|
| Milestone | `TL-M5` |
| Stable ID | `TL-M5-REELS-001` |
| Tab đích | `YV_10_production_briefs` |
| Schema | `YV-SHEET-001/1.0.0` |
| Trạng thái | `LOCAL_VERIFIED` — chưa `APPROVED`, chưa ghi Sheet |
| Chu kỳ hiện tại | `C1` |
| Loại brief của tệp này | `Reel` — 12 dòng |
| Tệp anh em | `production-briefs.md` — `Loại brief = Bài`, 16 dòng |
| Chuẩn kỹ thuật | Khung dọc 9:16 · 15 tới 30 giây · phụ đề bắt buộc · dựng cắt đơn giản |
| Nguồn sự thật | `month-calendar.md §2` · `asset-and-batch-plan.md §2` · `kpi-experiment-plan.md §2` |
| Ghi ra ngoài | `0` |

## 1. Quy ước bảng và chuẩn chung

Theo `dmp-profile.md §1` và đúng bốn quy ước đã ghi ở `production-briefs.md §1`. Bản cũ của tệp này để
brief ở dạng tiêu đề và gạch đầu dòng nên máy không đọc được; nay chuyển hết vào bảng, phần diễn giải
nằm trong ô chứ không nằm ngoài bảng.

Chuẩn áp cho **mọi** Reel:

- **Vùng an toàn:** chừa khoảng 14 phần trăm phía trên cho tên Page và 20 phần trăm phía dưới cho phần
  giao diện và mô tả. Chữ trên hình không tràn mép.
- **Ba giây đầu:** không giật gân, không doạ. Chủ ngữ ưu tiên là **cơ thể**, không phải khách hàng.
- **Phụ đề bắt buộc**, phông đủ tương phản, nằm trong vùng an toàn.
- **Cấm:** ảnh trước và sau, hình ảnh gây sợ về bệnh tật, lời chứng thực khái quát, nói cơ chế, nói
  chẩn đoán, nói trình độ hay kết quả của nhân sự, và mọi cách nói về nhượng quyền hay pháp lý.
- **Mục chạm sức khoẻ:** câu miễn trừ hiện ở cuối, giữ **ít nhất 5 giây** đủ để đọc hết — với Reel dài
  dưới 20 giây thì giữ tới hết — kèm lưu ý mỗi người mỗi khác, và phải qua người có chuyên môn rà.

**Câu miễn trừ chuẩn** (dán nguyên văn cho mục chạm sức khoẻ). Nơi đặt câu này **chưa chốt** —
`TL-R2-F08` vẫn đang mở; người có chuyên môn phải xác nhận bản cuối trước khi đăng, và ghi chú này
không tự phê duyệt câu chữ:

> Sản phẩm và liệu trình chăm sóc tại Y Viện có vai trò hỗ trợ chăm sóc sức khỏe chủ động, thư giãn
> và phục hồi thể trạng. Nội dung không thay thế cho chẩn đoán, điều trị hoặc chỉ định của bác sĩ.
> Với khách hàng có bệnh nền, đang mang thai, đang dùng thuốc điều trị hoặc có thiết bị y tế cấy ghép
> trong cơ thể, cần tham khảo ý kiến chuyên môn trước khi sử dụng.

**Tab này không có ô vàng**, cùng lý do đã ghi ở `production-briefs.md §1`.

## 2. Bảng dữ liệu — `YV_10_production_briefs` (phần `Reel`)

| Mã | Chu kỳ | Ngày | Hướng | Loại brief | Định dạng | Hook | Hình ảnh / shot | Chữ trên hình | Thời lượng | Tỷ lệ khung | Lời thoại | Phụ đề | Vùng an toàn | Kêu gọi | Câu claim dùng | Chỉ số theo dõi | Tiếp cận | Rủi ro / cổng | Trạng thái sản xuất | Chủ sở hữu |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TL-M5-RB-D1 | C1 | D-1 | A | Reel | Reel | Chị có đang chăm sóc cơ thể đều đặn không | Toàn cảnh không gian, rồi trung cảnh khu đón tiếp, rồi thẻ chữ định vị | Chăm sóc chủ động, không thay thế y khoa | 15 tới 30 giây | 9:16 | Ba tới mười giây một câu định vị; mười tới hai mươi giây một câu giới hạn; hai mươi tới ba mươi giây mời theo dõi | Bắt buộc | Chừa 14 phần trăm trên và 20 phần trăm dưới | Theo dõi Page, lưu bài | CL-ID1, CL-M1 | Số người tiếp cận, Số lượt bắt đầu xem Reel, Lượt lưu và lượt chia sẻ | Phụ đề bắt buộc, chữ tương phản cao | Không chạm sức khoẻ; giữ nguyên câu ranh giới, không cần câu miễn trừ | Chưa quay | Chủ Y Viện |
| TL-M5-RB-D3 | C1 | D-3 | A | Reel | Reel | Một khoảng dừng có chủ đích trông như thế nào | Bốn đoạn ngắn, mỗi tầng một đoạn, lấy từ AST-SPACE-4F | Tên bốn tầng Tĩnh, Thông, Dưỡng, Tỉnh | 15 tới 30 giây | 9:16 | Ba tới mười giây giới thiệu bốn tầng; mười tới hai mươi giây nhấn sự chỉn chu của hình thật; hai mươi tới ba mươi giây mời lưu bài | Bắt buộc | Chừa 14 phần trăm trên và 20 phần trăm dưới | Theo dõi Page, lưu bài | CL-OP1 | Số người tiếp cận, Số lượt bắt đầu xem Reel, Lượt lưu và lượt chia sẻ, Tỷ lệ xem hết Reel | Phụ đề bắt buộc, chữ tương phản cao | Chỉ mô tả không gian, cấm suy ra kết quả sức khoẻ | Chưa quay | Chủ Y Viện |
| TL-M5-RB-D7 | C1 | D-7 | A | Reel | Reel | Ba điều nên biết về Y Viện | Ghép tư liệu quay trong tuần một, chèn thẻ chữ | Y Viện là gì và không phải gì | 15 tới 30 giây | 9:16 | Ba tới hai mươi giây gói ba ý gồm chăm sóc chủ động, minh bạch giới hạn, không gian thật; hai mươi tới ba mươi giây mời theo dõi | Bắt buộc | Chừa 14 phần trăm trên và 20 phần trăm dưới | Theo dõi Page, lưu bài | CL-ID1, CL-M1 | Số người tiếp cận, Số lượt bắt đầu xem Reel, Lượt lưu và lượt chia sẻ | Phụ đề bắt buộc, chữ tương phản cao | Không chạm sức khoẻ; giữ nguyên câu ranh giới | Chưa quay | Chủ Y Viện |
| TL-M5-RB-D8 | C1 | D-8 | A | Reel | Reel | Cổ vai gáy căng sau một ngày ngồi nhiều | Người ngồi làm việc, rồi động tác thả lỏng nhẹ, rồi thẻ chữ | Hỗ trợ thư giãn, không thay thế chẩn đoán y khoa | 15 tới 30 giây | 9:16 | Ba tới mười giây tả cảm giác đời thường và không gọi tên bệnh; mười tới hai mươi giây nói ở mức hỗ trợ kèm một thói quen nhỏ; hai mươi tới ba mươi giây nhắc khi nào nên hỏi người có chuyên môn | Bắt buộc | Chừa 14 phần trăm trên và 20 phần trăm dưới | Lưu bài | CL-M2 | Số lượt bắt đầu xem Reel, Lượt lưu và lượt chia sẻ, Câu hỏi đúng chủ đề, Tín hiệu rủi ro | Phụ đề bắt buộc, chữ tương phản cao | Chạm sức khoẻ — câu miễn trừ giữ ít nhất 5 giây, cần người có chuyên môn rà, cấm đưa vào đường chuyển đổi | Chưa quay | Cổng sức khoẻ |
| TL-M5-RB-D11 | C1 | D-11 | A | Reel | Reel | Một khoảng dừng để làm ấm cơ thể | Cận cảnh động tác làm ấm, tông ấm, lấy từ AST-BODY-LIT | Hỗ trợ làm ấm và thư giãn | 15 tới 30 giây | 9:16 | Ba tới hai mươi giây nói ở mức hỗ trợ lưu thông khí huyết và giảm cảm giác đau mỏi, không cam kết kết quả; hai mươi tới ba mươi giây gợi thói quen nghỉ ngơi đều đặn | Bắt buộc | Chừa 14 phần trăm trên và 20 phần trăm dưới | Lưu bài | CL-M2 | Số lượt bắt đầu xem Reel, Lượt lưu và lượt chia sẻ, Tín hiệu rủi ro | Phụ đề bắt buộc, chữ tương phản cao | Chạm sức khoẻ — câu miễn trừ giữ ít nhất 5 giây, cần người có chuyên môn rà | Chưa quay | Cổng sức khoẻ |
| TL-M5-RB-D14 | C1 | D-14 | A | Reel | Reel | Chăm sóc cơ thể như một thói quen | Không gian dưỡng liệu, không quay nhãn và không quay thông số sản phẩm | Trải nghiệm chăm sóc, theo hướng dẫn | 15 tới 30 giây | 9:16 | Ba tới hai mươi giây chỉ kể ở mức trải nghiệm khách hàng và làm theo hướng dẫn; hai mươi tới ba mươi giây nói về nhịp chăm sóc định kỳ | Bắt buộc | Chừa 14 phần trăm trên và 20 phần trăm dưới | Lưu bài | CL-CX1, CL-M4 | Số lượt bắt đầu xem Reel, Lượt lưu và lượt chia sẻ, Tín hiệu rủi ro | Phụ đề bắt buộc, chữ tương phản cao | Quanh sản phẩm, đóng theo mặc định vì hồ sơ sản phẩm chưa kiểm chứng; cấm nói công dụng; câu miễn trừ giữ ít nhất 5 giây | Chặn bởi cổng hồ sơ sản phẩm | Cổng sức khoẻ |
| TL-M5-RB-D15 | C1 | D-15 | A | Reel | Reel | Được gọi bằng tên khi bước vào | Hình thật hai tầng đầu, lấy từ AST-SPACE-4F | Tên hai tầng Tĩnh và Thông | 15 tới 30 giây | 9:16 | Ba tới hai mươi giây đi từ tầng đón tiếp sang tầng gội dưỡng sinh và ngâm chân, chỉ nêu dữ kiện; hai mươi tới ba mươi giây mời theo dõi phần tiếp | Bắt buộc | Chừa 14 phần trăm trên và 20 phần trăm dưới | Theo dõi Page, lưu bài | CL-OP1, CL-M3 | Số người tiếp cận, Số lượt bắt đầu xem Reel, Lượt lưu và lượt chia sẻ, Tỷ lệ xem hết Reel | Phụ đề bắt buộc, chữ tương phản cao | Chỉ nêu dữ kiện vận hành; cấm nói trình độ nhân sự và cấm suy ra kết quả | Chưa quay | Chủ Y Viện |
| TL-M5-RB-D18 | C1 | D-18 | A | Reel | Reel | Chuẩn bị trước mỗi buổi | Hậu trường đội ngũ, lấy từ AST-TEAM-BTS, đang chờ đồng ý | Xin phép trước mỗi thao tác | 15 tới 30 giây | 9:16 | Ba tới hai mươi giây kể hậu trường quy trình và tinh thần nghề có tâm; hai mươi tới ba mươi giây mời theo dõi | Bắt buộc | Chừa 14 phần trăm trên và 20 phần trăm dưới | Theo dõi Page, lưu bài | CL-OP3 | Số người tiếp cận, Số lượt bắt đầu xem Reel, Lượt lưu và lượt chia sẻ | Phụ đề bắt buộc, chữ tương phản cao | Chặn tới khi có đồng ý bằng văn bản của từng người xuất hiện; cấm nói trình độ hay chứng chỉ | Chặn bởi cổng đồng ý | Cổng pháp lý |
| TL-M5-RB-D21 | C1 | D-21 | A | Reel | Reel | Không mời mua khi khách đang thư giãn | Ghép các khoảnh khắc tạo niềm tin, quay mới trong mẻ tuần 3 | Minh bạch giới hạn | 15 tới 30 giây | 9:16 | Ba tới hai mươi giây kể ba khoảnh khắc gồm nhớ điều khách dặn, nói thẳng khi thấy không phù hợp, không mời mua giữa buổi; hai mươi tới ba mươi giây mời lưu bài | Bắt buộc | Chừa 14 phần trăm trên và 20 phần trăm dưới | Theo dõi Page, lưu bài | CL-OP3, CL-M3 | Số người tiếp cận, Số lượt bắt đầu xem Reel, Lượt lưu và lượt chia sẻ, Tỷ lệ xem hết Reel | Phụ đề bắt buộc, chữ tương phản cao | Chỉ nêu dữ kiện vận hành; cấm lời chứng thực khái quát | Chưa quay | Chủ Y Viện |
| TL-M5-RB-D23 | C1 | D-23 | A | Reel | Reel | Một tín hiệu và một thói quen | Dùng lại khung hình của mẻ đọc hiểu cơ thể | Lắng nghe trước, rồi mới nghỉ ngơi đúng cách | 15 tới 30 giây | 9:16 | Ba tới hai mươi giây nhắc lại ở mức hỗ trợ và nói rõ khi nào nên hỏi người có chuyên môn; hai mươi tới ba mươi giây mời lưu bài | Bắt buộc | Chừa 14 phần trăm trên và 20 phần trăm dưới | Lưu bài | CL-M2 | Số lượt bắt đầu xem Reel, Lượt lưu và lượt chia sẻ, Tín hiệu rủi ro | Phụ đề bắt buộc, chữ tương phản cao | Chạm sức khoẻ — câu miễn trừ giữ ít nhất 5 giây, cần người có chuyên môn rà | Chưa quay | Cổng sức khoẻ |
| TL-M5-RB-D25 | C1 | D-25 | A | Reel | Reel | Ba giá trị của Y Viện | Thẻ chữ ghép với tư liệu đã quay | Chăm sóc chủ động | 15 tới 30 giây | 9:16 | Ba tới hai mươi giây tóm định vị theo ba nhịp; hai mươi tới ba mươi giây mời theo dõi để nhận nội dung tuần tới | Bắt buộc | Chừa 14 phần trăm trên và 20 phần trăm dưới | Theo dõi Page, lưu bài | CL-ID1, CL-M1 | Số người tiếp cận, Số lượt bắt đầu xem Reel, Người theo dõi mới | Phụ đề bắt buộc, chữ tương phản cao | Không chạm sức khoẻ; giữ nguyên câu ranh giới | Chưa quay | Chủ Y Viện |
| TL-M5-RB-D27 | C1 | D-27 | A | Reel | Reel | Mỗi ngày một thói quen nhỏ | Dùng lại khung hình của mẻ đọc hiểu cơ thể | Nhắc nhóm cần thận trọng | 15 tới 30 giây | 9:16 | Ba tới hai mươi giây nói một thói quen ở mức hỗ trợ và nhắc nhóm bệnh nền, mang thai, có thiết bị cấy ghép nên hỏi người có chuyên môn; hai mươi tới ba mươi giây mời lưu và chia sẻ | Bắt buộc | Chừa 14 phần trăm trên và 20 phần trăm dưới | Lưu bài, chia sẻ | CL-M2 | Số lượt bắt đầu xem Reel, Lượt lưu và lượt chia sẻ, Câu hỏi đúng chủ đề, Tín hiệu rủi ro | Phụ đề bắt buộc, chữ tương phản cao | Chạm sức khoẻ — câu miễn trừ giữ ít nhất 5 giây, cần người có chuyên môn rà | Chưa quay | Cổng sức khoẻ |

## 3. TikTok — chỉ tham chiếu cơ chế

TikTok **không** phải kênh đăng trong chu kỳ này. Chỉ dùng để tham chiếu cơ chế: cách giữ chân trong
ba giây đầu, phụ đề động, nhịp cắt. Mọi tài sản, câu claim và lời kêu gọi vẫn theo chuẩn Facebook và
theo luật an toàn ở §1. Không đăng chéo, không mở kênh TikTok cho tới khi có một quyết định khác được
ghi vào `04_DECISIONS`.

## 4. VERIFY (TL-M5 brief Reel)

- [x] 12 dòng Reel, đúng 12 mục video của lịch nội dung; Facebook là kênh đăng, TikTok chỉ tham chiếu.
- [x] Mỗi Reel đủ hook, danh sách hình, chữ trên hình, thời lượng, tỷ lệ khung, lời thoại, phụ đề,
      vùng an toàn, lời kêu gọi.
- [x] Năm Reel chạm sức khoẻ (`D-8`, `D-11`, `D-14`, `D-23`, `D-27`) mang câu miễn trừ giữ ít nhất 5
      giây và đi tuyến duyệt có người có chuyên môn.
- [x] Reel vận hành chỉ nêu dữ kiện, không nói trình độ nhân sự và không suy ra kết quả; `D-14` chỉ kể
      ở mức trải nghiệm.
- [x] Không ảnh trước và sau, không hình gây sợ, không lời chứng thực khái quát, không từ cấm.
- [x] Chuyển toàn bộ brief từ dạng tiêu đề và gạch đầu dòng sang bảng để `parse_markdown_tables()` đọc được.
- [x] Xưng hô theo bộ giọng: gọi khách là chị hoặc anh; thương hiệu là Y Viện ngôi thứ ba; bỏ hết chữ
      "bạn" và chữ "Toplink" trong lời nói với khách.
- [x] Ngày đã chuẩn hoá về `D-1` … `D-28` (sửa lỗi mô hình #8).
- [x] Header khai đúng tab `YV_10_production_briefs` (sửa lỗi mô hình #1: bản cũ khai
      `TL_REELS_PRODUCTION`, một dataset không tồn tại).
- [x] `external_writes=0`; không Reel nào `APPROVED`.
