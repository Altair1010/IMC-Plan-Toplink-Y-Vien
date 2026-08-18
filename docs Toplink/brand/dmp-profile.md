# TL-M2 — Hồ sơ thương hiệu Toplink Y Viện

> **Run 1 Phase A · chỉ chạy nội bộ · `external_writes=0`.** Bản dựng hồ sơ thương hiệu cho DMP.
> Chỉ ghi lại hồ sơ đã sửa và đã duyệt trước đó (`TL-M2-PROFILE-REPAIR-001`, duyệt 2026-07-30);
> **không** suy diễn lại và **không** ghi đè `profile.json`.

## 0. Khối định danh

| Trường | Giá trị |
|---|---|
| Milestone | `TL-M2` |
| Stable ID | `TL-BRAND-PROFILE-001` |
| Tab đích | `YV_01_brand_profile` |
| Schema | `YV-SHEET-001/1.0.0` (`docs/system/yvien-sheet-dataset-registry.json`) |
| Trạng thái | `LOCAL_VERIFIED · SYNC_PENDING_TARGET` — chưa `APPROVED`, chưa ghi Sheet |
| Nguồn sự thật | `profile.json` (`toplink-y-vien`) · brief §Foundation · taxonomy §1–3 · entity-map §2–4 |
| DMP version | `3.15.1` |
| Đường dẫn hồ sơ | `C:/Users/MCBAu/.claude-marketing/brands/toplink-y-vien/profile.json` |
| `profile_digest` (G5 LOCK) | `a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349` |
| `source_digest` (G5 LOCK) | `3ba91761612ca482471dc1c071bd7e9d82e5708a3bb13ceb630fed476541fe76` |
| Digest kiểm lại lần này | Hồ sơ MATCH · 5/5 nguồn MATCH (`00-input-lock.json`) |
| Bộ hướng dẫn | 5 nhóm / 52 luật (`guidelines/_manifest.json`) |
| Tính duy nhất của slug | Đúng 1 slug; **không** tạo `toplink-page` |
| Ghi ra ngoài | `0` |
| Milestone tiến lên | `false` |

## 1. Quy ước bảng (dùng chung 14 tệp canonical)

- Bảng ở §2 là **bảng dữ liệu duy nhất** mà trình biên dịch đọc cho tab đích.
- Cột `Mã` và cột `Chủ sở hữu` là **cột máy**: chúng đi vào hai cột ẩn `_key` / `_audit` của tab,
  **không** hiển thị ở mặt trước.
- Mọi cột còn lại là **cột hiển thị**, đúng thứ tự và đúng tên đã khai trong registry.
- `Mức bằng chứng` và `Được dùng ở đâu` ghi bằng giá trị enum máy; Sheet hiển thị nhãn tiếng Việt
  tra từ `display_label_map`.
- Ô trống có nghĩa ghi `—`, không để rỗng thật.

## 2. Slug & kiểm chứng runtime

- Đúng một thực thể DMP: `toplink-y-vien`. Không có thực thể thứ hai cho cùng thương hiệu.
- Đọc lại thương hiệu đang hoạt động = `toplink-y-vien` (khớp `TL-M1-DMP-SWITCH-001`).
- Không lưu bí mật, thông tin đăng nhập, mã nguồn, tech stack hay đường dẫn máy cục bộ trong hồ sơ.
  Website · Zalo · điện thoại · Maps giữ ngoài runtime chuyển đổi.

## 3. Bảng dữ liệu — `YV_01_brand_profile`

Đúng 21 dòng `TL-BP-01`…`TL-BP-21`. Không dòng nào được thêm nếu không truy được về `profile.json`.

| Mã | Nhóm | Hạng mục | Nội dung | Mức bằng chứng | Được dùng ở đâu | Khoá / mở | Chủ sở hữu |
|---|---|---|---|---|---|---|---|
| TL-BP-01 | Nhận diện | Tên thương hiệu | Toplink Y Viện | TOPLINK_CONFIRMED | PUBLIC_WITHIN_SOURCE | Khoá (lõi runtime) | DMP core |
| TL-BP-02 | Nhận diện | Câu định vị ngắn | Y Viện Dưỡng Thân – Tỉnh Thức | TOPLINK_CONFIRMED | PUBLIC_WITHIN_SOURCE | Khoá (lõi runtime) | DMP core |
| TL-BP-03 | Nhận diện | Câu định vị đầy đủ | Không gian chăm sóc sức khoẻ kết hợp Đông y dưỡng sinh, lý liệu và công nghệ cao | HYPOTHESIS | HYPOTHESIS_VALIDATION_ONLY | Mở — chưa được duyệt để nói công khai (lõi runtime) | DMP core |
| TL-BP-04 | Ngành | Ngành chính & mức quản lý | Chăm sóc sức khoẻ chủ động; ngành có quản lý; áp bộ luật phát ngôn sức khoẻ | TOPLINK_CONFIRMED | OPERATIONAL_CONTROL | Khoá (lõi runtime) | DMP core |
| TL-BP-05 | Ngành | Câu miễn trừ bắt buộc | Nguyên văn câu "không thay thế chẩn đoán, điều trị" kèm nhóm chống chỉ định | TOPLINK_CONFIRMED | OPERATIONAL_CONTROL | Bắt buộc — mọi bài sức khoẻ (lõi runtime, hướng dẫn) | Cổng sức khoẻ |
| TL-BP-06 | Kênh | Kênh chính | Facebook Page là kênh chính; Reels giữ vai trò hỗ trợ khám phá | TOPLINK_CONFIRMED | PUBLIC_WITHIN_SOURCE | Khoá (lõi runtime) | DMP core |
| TL-BP-07 | Kênh | Kênh chờ đầu vào | Zalo, điện thoại và Google Maps chưa đấu nối; chưa được đưa vào bất kỳ lời kêu gọi nào | MISSING_INPUT | BLOCKED | Đang treo — chờ chủ Y Viện cấp (lõi runtime) | Chủ Y Viện |
| TL-BP-08 | Mục tiêu | Mục tiêu chính | Dựng một Facebook Page dẫn dắt bằng niềm tin, xuất phát từ con số 0; Toplink đứng độc lập, không tham chiếu thương hiệu bên ngoài | TOPLINK_CONFIRMED | INTERNAL_ONLY | Khoá (lõi runtime) | DMP core |
| TL-BP-09 | Mục tiêu | Bộ chỉ số | Để trống theo thiết kế — chỉ số được định nghĩa ở tab từ điển chỉ số, không nhét vào hồ sơ | MISSING_INPUT | INTERNAL_ONLY | Hoãn tới tab từ điển chỉ số (lõi runtime) | DMP core |
| TL-BP-10 | Kinh doanh | Khoảng giá | Chưa kiểm chứng — nguồn không có bảng giá và không có điều khoản bảo hành | UNVERIFIED | BLOCKED | Đang treo — chờ chủ Y Viện cấp (lõi runtime) | Chủ Y Viện |
| TL-BP-11 | Giọng | Thang giọng | Trang trọng 6 · năng lượng 3 · hài hước 2 · uy tín 6 | TOPLINK_CONFIRMED | OPERATIONAL_CONTROL | Khoá (hướng dẫn) | Hướng dẫn thương hiệu |
| TL-BP-12 | Giọng | Từ cấm và từ nên dùng | Cấm "chữa khỏi", "điều trị dứt điểm", "thay thế thuốc"; nên dùng "hỗ trợ", "góp phần" | TOPLINK_CONFIRMED | OPERATIONAL_CONTROL | Khoá (hướng dẫn) | Hướng dẫn thương hiệu |
| TL-BP-13 | Kiến trúc | Ba trụ dịch vụ | Lý liệu · Dược liệu · Dưỡng liệu | TOPLINK_CONFIRMED | PUBLIC_WITHIN_SOURCE | Khoá (bối cảnh hồ sơ) | DMP core |
| TL-BP-14 | Kiến trúc | Ba tầng dịch vụ | Cơ bản, nâng cao, chuyên sâu — tổng 12 dịch vụ | TOPLINK_CONFIRMED | PUBLIC_WITHIN_SOURCE | Khoá ở mức tên gọi (bối cảnh hồ sơ) | DMP core |
| TL-BP-15 | Kiến trúc | Bảy sản phẩm | Bốn sản phẩm lý liệu và ba sản phẩm dưỡng liệu; công dụng chưa kiểm chứng | UNVERIFIED | HYPOTHESIS_VALIDATION_ONLY | Đang treo — cổng sức khoẻ (bối cảnh hồ sơ) | Cổng sức khoẻ |
| TL-BP-16 | Kiến trúc | Không gian bốn tầng | Tĩnh · Thông · Dưỡng · Tỉnh — tài sản không gian mạnh nhất của Y Viện | TOPLINK_CONFIRMED | PUBLIC_WITHIN_SOURCE | Khoá (bối cảnh hồ sơ) | DMP core |
| TL-BP-17 | Kiến trúc | Quy trình tám bước | Từ tiếp nhận đến hẹn lịch, tám bước rõ ràng và công khai được | TOPLINK_CONFIRMED | PUBLIC_WITHIN_SOURCE | Khoá (bối cảnh hồ sơ) | DMP core |
| TL-BP-18 | Kiến trúc | Bộ màu và bộ chữ | Nền ngà, nhấn vàng đồng, vàng nhắc việc, chữ nâu đen; bộ chữ Be Vietnam Pro và Noto Sans; tôn trọng chế độ giảm chuyển động | TOPLINK_CONFIRMED | OPERATIONAL_CONTROL | Khoá (hướng dẫn) | Hướng dẫn thương hiệu |
| TL-BP-19 | Hệ thống mẹ | Quan hệ nhượng quyền | Hệ thống mẹ là Nhất Liệu Y Viện; quan hệ chỉ ở mức nội bộ, cách nói công khai còn chờ văn bản | TOPLINK_CONFIRMED | INTERNAL_ONLY | Khoá — chỉ nội bộ (bối cảnh hồ sơ) | Cổng pháp lý |
| TL-BP-20 | Đối thủ | Danh sách đối thủ | Để trống — Toplink giữ vị thế độc lập, không tự đặt cạnh thương hiệu nào | TOPLINK_CONFIRMED | INTERNAL_ONLY | Khoá (lõi runtime) | DMP core |
| TL-BP-21 | Bằng chứng | Hồ sơ và đồng ý | Giá, bảo hành, chứng nhận pháp lý, thông số kỹ thuật và đồng ý dùng câu chuyện khách đều đang thiếu | MISSING_INPUT | BLOCKED | Đang treo — chờ chủ Y Viện cấp (chỉ lưu ở kho tài liệu) | Chủ Y Viện |

## 4. Founder — được nói gì, cấm nói gì

- Giọng thương hiệu là mặc định. Founder chỉ xuất hiện có chọn lọc, vai trò công khai duy nhất là
  `Founder/điều hành Toplink Y Viện`.
- Founder **không** giải thích cơ chế, **không** chỉ định sản phẩm, **không** chẩn đoán, **không**
  phát ngôn thay người có chuyên môn.
- Đăng lại sang Facebook cá nhân là một hành động ngoài phạm vi này và cần duyệt riêng từng bài.
- `guidelines/restrictions.md` (18 luật) thực thi danh mục cấm và câu miễn trừ bắt buộc.

## 5. Khoá digest — neo của `YV_01_brand_profile`

`docs Toplink/staging/run1/00-input-lock.json` kiểm lại trong lần chạy này:

```text
profile_digest = a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349   [MATCH]
source_digest  = 3ba91761612ca482471dc1c071bd7e9d82e5708a3bb13ceb630fed476541fe76   [locked]
  spec.md                                    aa8465ea…  [MATCH]
  TOPLINK_PAGE_MASTER_PLAN.md                aa923b51…  [MATCH]
  RULES.md                                   96c1bb4c…  [MATCH]
  Ho-so…2026.md                              645b1ad2…  [MATCH]
  entity-franchise-allowed-use-map.md        56618b18…  [MATCH]
```

Digest là tất định và bị khoá cho cả Run 1 lẫn Run 2. Lệch bất kỳ = `FAIL_BACK_TO_RUN1`.

## 6. VERIFY (TL-M2)

- [x] Đúng một slug; đọc lại `toplink-y-vien`; không có `toplink-page`.
- [x] Không bí mật, không đường dẫn cục bộ, không dữ liệu phân tích riêng tư trong hồ sơ hay tệp này.
- [x] Không ép trường thiếu bằng chứng vào runtime (Website · Zalo · điện thoại · Maps giữ
      `MISSING_INPUT`; giá và công dụng sản phẩm giữ `UNVERIFIED`).
- [x] Digest tất định và bị khoá (hồ sơ + 5 nguồn MATCH).
- [x] Đúng 21 dòng `TL-BP-*`, khớp `min_records = max_records = 21` của registry (sửa lỗi mô hình #10:
      nguồn 21 dòng nhưng bộ biên dịch cũ cho ra 32 record).
- [ ] Đọc lại từ Sheet — **hoãn** (chưa có approval, `external_writes=0`).
