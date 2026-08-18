# TL-M5 — Luồng duyệt, sổ phê duyệt và cách đo (Toplink Y Viện)

> **Run 1 Phase A · chỉ chạy nội bộ · `external_writes=0`.** Luồng này **đóng theo mặc định**: không
> có cổng người thật thì không có gì được đăng. Không mục nào trong chu kỳ `C1` đang ở trạng thái được
> duyệt hay đã đăng.

## 0. Khối định danh

| Trường | Giá trị |
|---|---|
| Milestone | `TL-M5` |
| Stable ID | `TL-M5-WORKFLOW-001` |
| Tab đích | `YV_12_workflow_approval` |
| Schema | `YV-SHEET-001/1.0.0` |
| Trạng thái | `LOCAL_VERIFIED` — chưa `APPROVED`, chưa ghi Sheet |
| Chu kỳ hiện tại | `C1` |
| Số dòng của tab | 84 — bằng đúng số dòng của `YV_09_content_calendar` |
| Nguồn dòng | `YV_09_content_calendar` (28 ngày × ba hướng A, B, C) |
| Nguồn sự thật | `RULES.md` · `month-calendar.md §2` · `asset-and-batch-plan.md §2` · `kpi-experiment-plan.md §2` |
| Ghi ra ngoài | `0` |

## 1. Quy ước bảng

Theo `dmp-profile.md §1`, với **một khác biệt quan trọng**: bảng ở §3 là **bảng quy tắc dẫn xuất**,
không phải bảng dòng dữ liệu. Tab `YV_12_workflow_approval` không có dòng nguồn riêng — mỗi dòng của
nó là **một dòng của lịch nội dung nhìn từ phía duyệt**, ghép 1:1 theo bộ ba `Chu kỳ · Ngày · Hướng`.

Vì vậy trình biên dịch làm đúng ba việc:

1. Lấy đủ 84 dòng của `YV_09_content_calendar`.
2. Với mỗi dòng, điền 18 cột hiển thị của `YV_12` theo đúng luật ở §3.
3. **Đếm lại: thiếu hoặc thừa một dòng so với lịch là dừng, không đi tiếp.** Sổ duyệt lệch với lịch
   nghĩa là có bài không ai duyệt.

Tab này **không có ô vàng**, cùng lý do đã ghi ở `month-calendar.md §1`: trạng thái quy trình không
phải quyết định đang treo. Việc người thật còn nợ đã có ô vàng riêng ở `YV_07_campaign` tuần 2.

## 2. Luồng duyệt (đóng theo mặc định)

```text
ý tưởng
  → bản nháp
  → soát bộ công cụ tiếp thị (8 chiều)
  → R1: phụ trách truyền thông
  → [nếu là video] R2: rà cơ chế và phụ đề
  → [nếu chạm sức khoẻ, founder, hoặc quanh sản phẩm] R3: người có chuyên môn
  → CỔNG NGƯỜI THẬT — chủ Y Viện duyệt từng bài
  → đăng, rồi ghi lại số đo
```

Chỉ **một** mũi tên trong chuỗi trên mở được cửa đăng: cổng người thật. Mọi vòng trước đó là vòng rà.

**Kết luận cao nhất mà một vòng rà đạt được là `REVIEWED`, `NEEDS_HUMAN_REVIEW`, `PASS` hoặc `FAIL`.**
Không vòng nào — kể cả `PASS` của agency, kể cả `LOCAL_VERIFIED` của runtime — được đặt `APPROVED`.
Trạng thái không bao giờ tự leo thang (`RULES.md:53`, `RULES.md:129-130`).

Bảy trạng thái duyệt: `DRAFT` · `REVIEWED` · `NEEDS_HUMAN_REVIEW` · `PASS` · `FAIL` ·
`HUMAN_APPROVED` (chỉ chủ Y Viện đặt được) · `PUBLISHED`.

## 3. Bảng quy tắc dẫn xuất — `YV_12_workflow_approval`

| Mã | Cột của tab | Lấy từ đâu | Luật điền | Giá trị hiện tại của cả chu kỳ C1 | Chủ sở hữu |
|---|---|---|---|---|---|
| TL-WF-01 | Chu kỳ | `YV_09.Chu kỳ` | Chép nguyên | C1 | Codex |
| TL-WF-02 | Ngày | `YV_09.Ngày` | Chép nguyên, dạng `D-1` … `D-28` | 28 giá trị | Codex |
| TL-WF-03 | Hướng | `YV_09.Hướng` | Chép nguyên A, B hoặc C | A, B, C | Codex |
| TL-WF-04 | Người duyệt | `YV_09.Tuyến duyệt` | Ghép theo từng chặng, không tra bảng cứng: `R1` ra "Phụ trách truyền thông", `R2` ra "rà cơ chế video", `R3` ra "người có chuyên môn"; nối bằng dấu phẩy đúng thứ tự chặng | Bốn tổ hợp: `R1` 7 dòng ngày, `R1+R2` 7, `R1+R3` 9, `R1+R2+R3` 5 — nhân ba hướng thành 84 dòng | Chủ Y Viện |
| TL-WF-05 | Kết luận | `YV_09.Trạng thái duyệt` | Chép nguyên, cấm nâng cấp | 42 dòng DRAFT, 42 dòng NEEDS_HUMAN_REVIEW | Chủ Y Viện |
| TL-WF-06 | Điều kiện kèm theo | Hướng và mức rủi ro | Hướng A ghi điều kiện thật; hướng B và C mở đầu `DỰ PHÒNG — ` và ghi rõ chưa có brief | Xem §4 | Chủ Y Viện |
| TL-WF-07 | Hết hạn (ICT) | — | Chưa có kết luận nào thì chưa có hạn; cấm ngày tuyệt đối ở giai đoạn này | — | Chủ Y Viện |
| TL-WF-08 | Trạng thái đăng | Cố định | Chưa qua cổng người thật thì luôn là chưa đăng | NOT_PUBLISHED, cả 84 dòng | Chủ Y Viện |
| TL-WF-09 | Bản sửa | Cố định | Bản đầu tiên | 1, cả 84 dòng | Codex |
| TL-WF-10 | Sửa lớn có reset không | Cố định | Sửa lớn đưa dòng về DRAFT và xoá mọi kết luận đã có | Có | Codex |
| TL-WF-11 | Tuyến duyệt | `YV_09.Tuyến duyệt` | Chép nguyên (sửa lỗi mô hình #4 và #7: bản cũ mất hẳn cột này) | `R1`, `R1+R2`, `R1+R3`, `R1+R2+R3` | Chủ Y Viện |
| TL-WF-12 | Mức rủi ro | Trụ nội dung và ngày của dòng | Luật có thứ tự, mức chặt hơn thắng: trụ đọc hiểu cơ thể hoặc Lý – Dược – Dưỡng ra `health`; trụ hành trình founder ra `founder`; `D-14` và `D-26` ra `product-adjacent`; còn lại `none` | 30 `health` · 12 `founder` · 42 `none` · 0 `product-adjacent` — cả `D-14` lẫn `D-26` đều thuộc trụ Lý – Dược – Dưỡng nên đã lên mức chặt hơn là `health`; ranh giới quanh sản phẩm không rơi mất, nó nằm ở `Điều kiện kèm theo` của hai ngày đó và ở `Trạng thái sản xuất = Chặn bởi cổng hồ sơ sản phẩm` bên `YV_10` | Cổng sức khoẻ |
| TL-WF-13 | DMP check | Bản soát 8 chiều | Chép nguyên kết quả soát, giữ nguyên lý do bỏ qua | 7 đạt, 1 bỏ qua | Codex |
| TL-WF-14 | Trạng thái đồng ý | `asset-and-batch-plan.md §2` | Hướng A dùng tài sản có người xuất hiện thì ghi `CHƯA CÓ ĐỒNG Ý`; hướng A không có người thì `Không cần`; hướng B và C chưa có brief nên chưa xác định được, ghi `—` | 4 dòng `CHƯA CÓ ĐỒNG Ý` (`D-5`, `D-20`, `D-24`, `D-28`) · 24 dòng `Không cần` · 56 dòng `—`. Chưa có đồng ý nào | Cổng pháp lý |
| TL-WF-15 | Giờ đăng | — | Chưa đăng thì chưa có giờ | — | Chủ Y Viện |
| TL-WF-16 | Tham chiếu đo | `kpi-experiment-plan.md §2` | Lấy tên chỉ số theo vai trò phễu của dòng | Xem §6 | Chủ Y Viện |
| TL-WF-17 | Ghi chú reset | Cố định | Ghi rõ điều gì tính là sửa lớn | Đổi câu claim, đổi lời kêu gọi, đổi người xuất hiện, đổi kết luận sức khoẻ | Cổng pháp lý |
| TL-WF-18 | Câu claim | `YV_09.Câu claim dùng` | Chép nguyên mã `CL-*`, tra được ở `06_COMPLIANCE_RULES` | 10 mã | Cổng pháp lý |

## 4. Điều kiện kèm theo hai hướng dự phòng

Hướng A của mỗi ngày là hướng khuyến nghị và có brief thật. **Hướng B và C hiện chưa có brief sản
xuất, chưa có brief Reel và chưa có tài sản.** Điều đó được ghi thẳng ra chứ không để im (sửa lỗi mô
hình #6): mọi dòng B và C mang `Trạng thái sản xuất = CHƯA CÓ BRIEF` ở `YV_10_production_briefs` và ô
`Điều kiện kèm theo` mở đầu bằng `DỰ PHÒNG — `. Muốn chạy một hướng B hay C thì phải viết brief cho
nó trước, và nó đi lại đúng tuyến duyệt của hướng A cùng ngày.

Dòng dự phòng **không bao giờ được tô vàng** — chúng là lựa chọn thay thế, không phải việc đang treo.

## 5. Sức khoẻ, pháp lý và quyền riêng tư

- **Câu miễn trừ chưa có nơi ở cố định.** Vẫn còn phát hiện `TL-R2-F08` đang mở: chưa chốt câu miễn
  trừ đặt ở đâu — trong phần mô tả từng bài, trong ảnh, hay ở phần giới thiệu Page. Trước khi chốt,
  mọi mục chạm sức khoẻ phải mang câu miễn trừ **ngay trong phần mô tả của chính bài đó**.
- **Bốn mức rủi ro** ngoài mức không có: chạm sức khoẻ, có founder, quanh sản phẩm, chạm pháp lý và
  quyền riêng tư.
- **Mục quanh sản phẩm đóng theo mặc định.** `D-14` và `D-26` chỉ được kể ở mức trải nghiệm khách hàng
  vì hồ sơ sản phẩm chưa kiểm chứng (`TL-GAP-010`). Không câu nào được nói về công dụng.
- **Mục có founder** là `D-5`, `D-20`, `D-24`, `D-28`, nằm gọn trong cửa sổ trượt cuối chu kỳ, tổng 4
  trên 28 mục tức 14,3%, dưới trần 20%. Cả bốn đều chặn tới khi có đồng ý bằng văn bản và phạm vi được
  nói của founder (`asset-and-batch-plan.md`, dòng `AST-FOUNDER`).
- **Chưa có đồng ý nào của người xuất hiện.** Chưa có đồng ý thì cắt hết phần con người, chỉ giữ không
  gian và đồ hoạ.

## 6. Cách soát bằng bộ công cụ và cách đo

Bản soát 8 chiều cho kết quả **7 chiều đạt, 1 chiều bỏ qua**. Chiều bỏ qua là chiều chấm điểm nhanh
bằng bộ chạy đánh giá — **lý do bỏ qua phải giữ nguyên khi ghi vào Sheet**: bộ chấm nhanh đã được thay
bằng một lượt quét xác định, nên điểm của nó không còn ý nghĩa so sánh. Bỏ mất lý do này là biến một ô
minh bạch thành một ô mập mờ.

Số đo lấy theo chỉ số đã định nghĩa ở `05_KPI_DICTIONARY`, không định nghĩa lại ở đây. Ghép theo vai
trò phễu: dòng TOFU theo dõi các chỉ số tiếp cận và xem hết Reel; dòng MOFU theo dõi lượt lưu, lượt
chia sẻ và số câu hỏi về quy trình. Mốc xuất phát của chu kỳ `C1` là 0 người theo dõi và mức nhận biết
chưa đo — cấm quy ra phần trăm tăng trưởng từ mốc 0.

## 7. VERIFY (TL-M5 luồng duyệt)

- [x] Luồng đóng theo mặc định; chỉ cổng người thật mở được cửa đăng.
- [x] Không vòng rà nào của agent đạt tới `APPROVED`; trạng thái không leo thang.
- [x] 84 dòng của tab ghép 1:1 với lịch nội dung theo `Chu kỳ · Ngày · Hướng`; lệch là dừng.
- [x] 18 cột hiển thị của registry đều có luật điền; 8 trường trước đây không có chỗ đáp nay đã có
      (sửa lỗi mô hình #7).
- [x] Hai hướng dự phòng được ghi rõ là chưa có brief thay vì để im (sửa lỗi mô hình #6).
- [x] Không dòng nào `HUMAN_APPROVED`; cả 84 dòng `NOT_PUBLISHED`, bản sửa 1.
- [x] Lý do bỏ qua một chiều soát được giữ nguyên văn.
- [x] Câu miễn trừ chưa có nơi ở cố định — ghi thành phát hiện đang mở `TL-R2-F08`, không tự chốt.
- [x] Header khai đúng tab `YV_12_workflow_approval` (sửa lỗi mô hình #1: bản cũ khai
      `TL_WORKFLOW_APPROVAL`).
- [x] `external_writes=0`.
