# TL-M5 — Kế hoạch asset & batch production (Toplink Y Viện)

> **Run 1 Phase A · local-only · `external_writes=0`.** DMP `content-calendar` + `content-engine`
> (v3.15.1). Phản ánh **capacity thật** (input lock 2026-08-03). **Direction B: chỉ placeholder brief
> — KHÔNG chọn/tái sử dụng/công bố hay ngụ ý rights-clearance cho bất kỳ asset thật nào**
> (`TL-M5-ASSET-RIGHTS-001 = BOUNDED`; Q9 rights deferred). Stable ID `TL-M5-ASSET-001`.
> Logical Sheet dataset: `TL_REELS_PRODUCTION`.

## 1. Capacity thật (nguồn: input lock `TL-GAP-006-CAPACITY`)

| Tham số | Giá trị | Ghi chú |
|---|---|---|
| Video/tuần | ~3 | 12 Reels / 28 ngày |
| Tổng item/tuần | ≥7 (≥1/ngày) | 28 item / 28 ngày |
| Xen kẽ | video + static/carousel | 16 static/carousel |
| Editing | cơ bản (không professional) | tránh VFX/motion phức tạp |
| Video lead-time | 2 ngày | shoot → edit → review → sẵn sàng |
| Bài viết | same-day | static/carousel |
| Vai trò team | chưa yêu cầu | 1 người đa vai (`MISSING_INPUT` cho phân vai chi tiết) |

> Phân vai chi tiết (quay/edit/duyệt tách người) = `MISSING_INPUT` — **không điền giả**; mặc định
> single-operator cho tới khi user chốt (gate `TL-M6`).

## 2. Placeholder asset brief (KHÔNG asset thật)

> Mỗi ô dưới là *yêu cầu cần quay/chuẩn bị mới* dạng placeholder. **Không** trỏ tới file/thư viện/asset
> có sẵn; **không** giả định đã có quyền dùng. Chọn/clear asset thật là hành động sau khi rights PASS.

| Asset placeholder ID | Loại | Mô tả cần chuẩn bị | Rights state | Dùng cho item |
|---|---|---|---|---|
| `AST-SPACE-4F` | video/photo không gian | b-roll 4 tầng (TĨNH/THÔNG/DƯỠNG/TỈNH), real imagery | `RIGHTS_UNCLEARED` (placeholder) | D03,D15,D19 |
| `AST-PROCESS-8S` | video/photo quy trình | minh hoạ 8 bước, xin phép/giải thích | `RIGHTS_UNCLEARED` | D06,D16 |
| `AST-HYGIENE` | photo/video vệ sinh | quy chuẩn vệ sinh, chi tiết chỉn chu | `RIGHTS_UNCLEARED` | D17,D21 |
| `AST-TEAM-BTS` | video hậu trường | đội ngũ chuẩn bị (no qualification claim, cần consent người xuất hiện) | `RIGHTS_UNCLEARED` + consent gate | D18,D20 |
| `AST-BODY-LIT` | video/graphic body-literacy | minh hoạ tín hiệu cơ thể, không medical-fear | `RIGHTS_UNCLEARED` | D08,D10,D11,D13,D23,D27 |
| `AST-LDD-EXPLAIN` | graphic/carousel | Lý–Dược–Dưỡng dễ hiểu (customer-experience, no product claim) | `RIGHTS_UNCLEARED` | D09,D12,D26 |
| `AST-CX-DUONGLIEU` | video trải nghiệm | trải nghiệm khách hàng (UNVERIFIED product → customer-experience framing only) | `RIGHTS_UNCLEARED` + `TL-GAP-010` fail-closed | D14 |
| `AST-FOUNDER` | video/photo founder | founder ý niệm/hành trình | `RIGHTS_UNCLEARED` + allowed-use + consent | D05,D24 |
| `AST-BRAND-ID` | graphic nhận diện | định vị/this-not-that, palette Tân Trung Hoa (ivory/wine/brass) | `RIGHTS_UNCLEARED` | D01,D02,D04,D07,D22,D25,D28 |

> Bất kỳ testimonial/UGC/người xuất hiện thật nào ⇒ documented consent (mục đích/kênh/thời hạn/thu hồi/
> che thông tin) trước khi dùng. Chưa có consent nào ở phase này.

## 3. Batch plan theo tuần (khớp lead-time 2 ngày)

> Nguyên tắc: gom video cùng bối cảnh vào 1 buổi quay để đủ ~3 Reels/tuần với editing cơ bản; bài viết
> chuẩn bị same-day. Không ngày tuyệt đối — dùng "trước D-1 ≥2 ngày" cho video.

| Batch | Item video | Bối cảnh gom quay | Chuẩn bị | Ràng buộc lead-time |
|---|---|---|---|---|
| `B-W1` | D01,D03,D07 | không gian + intro brand | AST-BRAND-ID, AST-SPACE-4F | quay ≥2 ngày trước D-1 |
| `B-W2` | D08,D11,D14 | body-literacy + trải nghiệm | AST-BODY-LIT, AST-CX-DUONGLIEU | quay ≥2 ngày trước D-8; **chờ professional review trước publish** |
| `B-W3` | D15,D18,D21 | không gian 4 tầng + BTS đội ngũ | AST-SPACE-4F, AST-TEAM-BTS, AST-HYGIENE | quay ≥2 ngày trước D-15; consent người xuất hiện |
| `B-W4` | D23,D25,D27 | recap (tái dùng khung, quay mới nếu cần) | AST-BODY-LIT, AST-BRAND-ID | quay ≥2 ngày trước D-22 |

Static/carousel (16 item): sản xuất same-day theo ngày phát, dùng placeholder graphic AST-*.

## 4. Editing constraint (cơ bản)

- Ưu tiên cut đơn giản, subtitle rõ, safe-zone chuẩn 9:16; tránh motion-graphics/VFX nặng.
- Mọi Reel: subtitle bắt buộc (xem `reels-briefs.md`), disclaimer đủ thời gian đọc cho item sức khỏe.
- Không AI-generated asset ở phase này; nếu sau này dùng và có thị trường EU → cần C2PA (ngoài scope).

## 5. VERIFY (TL-M5 asset/batch)

- [x] Capacity phản ánh input lock thật; thiếu phân vai = `MISSING_INPUT` (không điền giả).
- [x] 100% asset là placeholder `RIGHTS_UNCLEARED`; không chọn/tái dùng/ngụ ý clearance asset thật.
- [x] Consent gate cho founder/BTS/testimonial nêu rõ; chưa có consent nào.
- [x] Batch tôn trọng lead-time 2 ngày; W2 chờ professional review trước publish.
- [x] Product-adjacent (D14/D26) = customer-experience only, `TL-GAP-010` fail-closed.
- [x] `external_writes=0`; không item `APPROVED`.
