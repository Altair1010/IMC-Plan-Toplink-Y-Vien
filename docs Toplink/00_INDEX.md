# 00_INDEX — Bộ tri thức sản phẩm Y Viện Toplink

> Nguồn gốc: tách từ `11_Product_Yvien.md` (biên tập từ transcript video, tư liệu truyền thông, video sản phẩm).
> Mục đích: chia nhỏ để dễ đọc, dễ maintain, và để Claude Code hydrate vào `data/brands/y_vien_toplink/knowledge/` mà không tràn context.

> **TRẠNG THÁI (cập nhật 2026-06-18):** ĐÃ HYDRATE 2026-06-09 — nội dung đã map vào
> `data/brands/y_vien_toplink/knowledge/`. **Giữ thư mục này (KHÔNG xóa, KHÔNG đổi tên)**
> cho tới khi reviewer ký xong 27 claims + 16 angles, vì ~40 tham chiếu `hydrated_from:` /
> `Source:` trong KB và SPEC.md trỏ về đây để audit. Chi tiết: `HYDRATION_REPORT_2026-06-09.md`.

## Danh sách file

| File | Nội dung | Map tới product slug |
|---|---|---|
| `00_INDEX.md` | File này — mục lục + quy ước | — |
| `01_positioning_and_pillars.md` | Định vị chung, 3 trụ cột (lý liệu / dược liệu / dưỡng liệu) | brand-level |
| `02_communication_safety.md` | Nguyên tắc truyền thông an toàn: nên / không nên dùng, disclaimer | compliance.profile + tất cả products |
| `03_product_may_vtv.md` | Máy vật lý trị liệu đa chức năng Vương Trung Vương | `vtv_machine` |
| `04_product_dai_tu.md` | Đai từ tiêu viêm giảm đau | `magnetic_belt` |
| `05_product_tham_da.md` | Thảm đá năng lượng | `energy_stone_mat` |
| `06_product_goi_tu.md` | Gối từ đa năng | `magnetic_pillow` |
| `07_duong_lieu.md` | Nhóm dưỡng liệu: Albumin, Collagen, Maca | (3 sản phẩm mới — xem ghi chú) |
| `08_summary_table.md` | Bảng tóm tắt 7 sản phẩm | products_index reference |
| `09_scripts_and_hooks.md` | Kịch bản giới thiệu tổng thể, bộ câu thương hiệu, FAQ | content_angles + brand voice |
| `10_content_formulas_and_checklist.md` | Công thức content FB/video, checklist kiểm duyệt | brand-level content rules |
| `11_Product_Yvien.md` | Tài liệu nguồn gốc (chưa tách) — chuyển vào đây 2026-06-18 từ `.claude/docs/context/` | nguồn của 01–10 |

## Quy ước map sản phẩm → slug trong knowledge base

| Tên trong tài liệu | slug trong `data/brands/.../02_products/` | Trạng thái skeleton |
|---|---|---|
| Máy Vương Trung Vương | `vtv_machine` | ✅ đã có skeleton |
| Đai từ tiêu viêm giảm đau | `magnetic_belt` | ✅ đã có skeleton |
| Thảm đá năng lượng | `energy_stone_mat` | ✅ đã có skeleton |
| Gối từ đa năng | `magnetic_pillow` | ✅ đã có skeleton |
| Albumin | `duong_lieu_albumin` | ⚠️ CHƯA có skeleton — cần UPD-3 |
| Collagen | `duong_lieu_collagen` | ⚠️ CHƯA có skeleton — cần UPD-3 |
| Maca | `duong_lieu_maca` | ⚠️ CHƯA có skeleton — cần UPD-3 |

> **Lưu ý quan trọng:** Skeleton hiện tại (từ M1-S3) có các slug dòng Sao Thiên Y (`sty_thoai_hoa_khop`, `sty_an_ap_khang`, `sty_tien_dinh`, `sty_full_line`) — nhưng tài liệu này KHÔNG có thông tin về Sao Thiên Y. Ngược lại, tài liệu có nhóm dưỡng liệu (Albumin/Collagen/Maca) mà skeleton CHƯA có.
>
> → Cần quyết định: dòng Sao Thiên Y có còn bán không? Nếu không, đánh dấu `status: deprecated`. Nhóm dưỡng liệu cần tạo skeleton mới qua UPD-3.

## Cảnh báo compliance (đọc trước khi hydrate)

Đây là brand y tế/sức khỏe. Mọi công dụng trong tài liệu này đều ở dạng **"hỗ trợ"**, KHÔNG phải claim điều trị. Khi hydrate vào `claims_and_compliance.md`:
- Phần "Nên dùng" / "Lợi ích truyền thông" → có thể thành **unverified claims** (cần nguồn NSX để lên approved)
- Phần "Không nên dùng" / "Không nên viết" → thành **forbidden claims** (bắt buộc)
- Disclaimer ở `02_communication_safety.md` §3.3 → mandatory disclaimer
