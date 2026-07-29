# 08 — Bảng tóm tắt sản phẩm

> Nguồn: `11_Product_Yvien.md` §6
> Dùng để cross-check khi hydrate `products_index.yaml`

| Sản phẩm | slug | Định vị ngắn | Công dụng truyền thông an toàn | Đối tượng phù hợp | Lưu ý |
|---|---|---|---|---|---|
| Máy Vương Trung Vương | `vtv_machine` | Thiết bị chăm sóc sức khỏe đa chức năng | Hỗ trợ thư giãn, làm ấm, giảm cảm giác đau mỏi, chăm sóc toàn thân | Người lớn tuổi, người đau mỏi, gia đình, trung tâm trị liệu | Dùng theo hướng dẫn; không thay thế điều trị y khoa |
| Đai từ tiêu viêm giảm đau | `magnetic_belt` | Thiết bị chăm sóc vùng đau mỏi cục bộ | Hỗ trợ làm ấm, thư giãn, giảm cảm giác căng cứng vùng tác động | Người hay mỏi lưng, vai gáy, chân, khớp | Thận trọng với phụ nữ mang thai, người suy tim, bệnh máu, huyết áp không ổn định |
| Thảm đá năng lượng | `energy_stone_mat` | Thiết bị thư giãn và phục hồi toàn thân | Hỗ trợ làm ấm, thư giãn, nghỉ ngơi sâu, lưu thông khí huyết | Người mệt mỏi, khó thư giãn, người lớn tuổi, gia đình | Không dùng nhiệt quá cao; thận trọng với bệnh nền |
| Gối từ đa năng | `magnetic_pillow` | Thiết bị chăm sóc cổ vai gáy | Hỗ trợ thư giãn cổ gáy, làm ấm, giảm căng cứng do ngồi lâu | Người văn phòng, người cúi điện thoại nhiều, người lái xe | Không dùng thay thế điều trị khi có triệu chứng thần kinh nặng |
| Albumin | `duong_lieu_albumin` | Dưỡng liệu hỗ trợ thể trạng | Hỗ trợ bổ sung dinh dưỡng và chăm sóc nền tảng cơ thể | Người cần bồi bổ theo hướng dẫn | Không dùng như thuốc điều trị |
| Collagen | `duong_lieu_collagen` | Dưỡng liệu hỗ trợ mô liên kết | Hỗ trợ da, khớp, độ đàn hồi và sự dẻo dai | Người cần chăm sóc sắc vóc và mô liên kết | Không cam kết chữa bệnh xương khớp |
| Maca | `duong_lieu_maca` | Dưỡng liệu hỗ trợ sinh khí | Hỗ trợ thể lực, sức bền, cảm giác khỏe khoắn | Người cần bồi bổ thể trạng | Không truyền thông như thuốc nội tiết |

## Ghi chú đối chiếu với skeleton hiện tại

| Skeleton hiện có (M1-S3) | Có trong tài liệu này? | Hành động đề xuất |
|---|---|---|
| `vtv_machine` | ✅ | Hydrate (HYD-S1) |
| `magnetic_belt` | ✅ | Hydrate (HYD-S1) |
| `energy_stone_mat` | ✅ | Hydrate (HYD-S1) |
| `magnetic_pillow` | ✅ | Hydrate (HYD-S1) |
| `sty_thoai_hoa_khop` | ❌ không có info | Giữ skeleton, hỏi team có còn bán không |
| `sty_an_ap_khang` | ❌ không có info | Giữ skeleton, hỏi team |
| `sty_tien_dinh` | ❌ không có info | Giữ skeleton, hỏi team |
| `sty_full_line` | ❌ không có info | Giữ skeleton, hỏi team |
| `o_nuts` (_pending) | ❌ không có info | Giữ pending |
| — | Albumin/Collagen/Maca cần tạo mới | UPD-3 tạo 3 skeleton |
