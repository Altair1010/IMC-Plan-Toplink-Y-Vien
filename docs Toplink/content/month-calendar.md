# TL-M5 — Lịch nội dung 28 ngày (Toplink Y Viện)

> **Run 1 Phase A · local-only · `external_writes=0`.** DMP `content-calendar` + `content-engine`
> (v3.15.1), active brand `toplink-y-vien`, profile `a45e4ae4…c8cbe349`. **Lịch tương đối `D-1 … D-28`
> — KHÔNG ngày tuyệt đối; `TOPLINK_CONTENT_START_DATE = UNSET`.** Ngày lễ/ra mắt/sự kiện là *special
> priority slot*, không bind vào ngày cứng (gate `TL-M6`). Stable ID `TL-M5-CALENDAR-001`. Logical
> Sheet dataset: `TL_CONTENT_CALENDAR`. Không item nào `APPROVED`/publish-ready ở phase này.

## 0. Tham số nguồn (từ input lock 2026-08-03)

- **Capacity:** ~3 video/tuần; ≥7 item/tuần; ≥1/ngày; editing cơ bản; video lead-time 2 ngày; bài
  viết same-day; chưa cần vai trò team riêng (`TL-GAP-006 = BOUNDED`).
- **Phân bổ 28 item theo pillar** (weights §content-pillars 20/20/30/15/15):
  `TL-P1`×6 · `TL-P2`×6 · `TL-P3`×8 · `TL-P4`×4 · `TL-P5`×4 = 28.
- **Format:** 12 Reels (3/tuần) + 16 static/carousel.
- **CTA trước offer gate:** chỉ `theo dõi Page` · `lưu` · `chia sẻ`. Không booking/giá/tư vấn/mua.
- **Item sức khỏe** (`TL-P2`/`TL-P4`, 10 item): disclaimer §3.3 bắt buộc + route professional/human.

## 1. Claim register (dùng chung mọi item)

| Claim ID | Nội dung được phép | Source | Trạng thái | Điều kiện |
|---|---|---|---|---|
| `CL-ID1` | Toplink là không gian chăm sóc **chủ động**, KHÔNG phải bệnh viện / không cam kết chữa khỏi | positioning §2 | `TOPLINK_CONFIRMED` | none |
| `CL-M1` | "Chăm sóc cơ thể bắt đầu từ việc lắng nghe" | positioning §4 M1 | `TOPLINK_CONFIRMED` | none |
| `CL-M2` | "Hỗ trợ thư giãn, làm ấm, lưu thông, phục hồi — đúng người, đúng lúc" | positioning §4 M2; safety §3.1 | `TOPLINK_CONFIRMED` (support) | disclaimer + professional review |
| `CL-M3` | "Không gian, quy trình rõ ràng, minh bạch giới hạn" | positioning §4 M3 | `TOPLINK_CONFIRMED` (operational) | operational-only |
| `CL-M4` | "Hiểu Lý–Dược–Dưỡng để chăm sóc chủ động" | positioning §4 M4 | naming `TOPLINK_CONFIRMED` / efficacy `UNVERIFIED` | professional review per item |
| `CL-OP1` | Hành trình 4 tầng TĨNH/THÔNG/DƯỠNG/TỈNH | dossier §7.1 | `TOPLINK_CONFIRMED` (mô tả không gian) | real imagery; no outcome |
| `CL-OP2` | Quy trình chăm sóc 8 bước | dossier §7.2 | `TOPLINK_CONFIRMED` (mô tả quy trình) | no outcome/qualification claim |
| `CL-OP3` | Vệ sinh, chỉn chu, không gian thật | dossier §7.3 | `TOPLINK_CONFIRMED` (operational) | operational-only |
| `CL-CX1` | Trải nghiệm khách hàng quanh dưỡng liệu/sản phẩm | `11_Product_Yvien.md` | `UNVERIFIED` | **customer-experience framing only; no product/efficacy claim** |
| `CL-FD1` | Ý niệm/hành trình founder & cộng đồng | narrative §3 | allowed-use gated | consent; no cơ chế/chỉ định/diagnosis |

`DO_NOT_USE`: mọi franchise/legal wording (`TL-D16`); "hospital"/"+"/thập tự; forbidden health terms (safety §3.2).

## 2. Review routes (áp dụng theo cột calendar)

- **R1 — Content Creator → PR Manager:** mọi item (calendar/copy).
- **R2 — Short-Video Coach → TikTok Strategist:** item video (mechanics-only; Facebook-first).
- **R3 — PR Manager → human/professional gate:** item sức khỏe (`TL-P2`/`TL-P4`), founder (`CL-FD1`),
  product-adjacent (`CL-CX1`), và mọi public-positioning nhạy cảm.

## 3. Lịch 28 ngày (D-1 … D-28)

> Cột **Option A/B/C** = ba hướng hook/angle để chủ chọn 1 khi sản xuất (chi tiết copy ở
> `production-briefs.md`; script Reel ở `reels-briefs.md`). **Approval** mặc định `DRAFT`; item sức khỏe
> `NEEDS_HUMAN_REVIEW`. Không item nào `APPROVED`.

### Tuần 1 — Định vị & giới hạn (`TL-P1` + `TL-P3` teaser)

| ID | Pillar | Format | Angle chính | A / B / C option | Claim | CTA | Review | Approval |
|---|---|---|---|---|---|---|---|---|
| `TL-M5-CAL-D01` | `TL-P1` | Reel | Toplink là ai — giới thiệu Page | A: câu hỏi "Bạn có đang chăm sóc cơ thể đều đặn?" · B: mở đầu bằng không gian · C: 1 câu định vị + 1 câu giới hạn | `CL-ID1`,`CL-M1` | follow/save | R1+R2 | DRAFT |
| `TL-M5-CAL-D02` | `TL-P1` | static | Toplink KHÔNG phải gì | A: this/not-that card · B: 3 hiểu lầm thường gặp · C: 1 câu ranh giới rõ | `CL-ID1` | follow/save | R1 | DRAFT |
| `TL-M5-CAL-D03` | `TL-P3` | Reel | Teaser không gian 4 tầng | A: pan 4 tầng · B: chi tiết 1 tầng · C: âm thanh/không khí tĩnh | `CL-OP1` | follow/save | R1+R2 | DRAFT |
| `TL-M5-CAL-D04` | `TL-P1` | carousel | Thân–Tâm–Trí & giới hạn | A: 3 trụ giá trị · B: "vì sao trước làm gì" · C: minh bạch giới hạn | `CL-M1`,`CL-ID1` | save/share | R1 | DRAFT |
| `TL-M5-CAL-D05` | `TL-P5` | static | Ý niệm & hành trình founder | A: một câu ý niệm · B: "một khoảng dừng có chủ đích" · C: cộng đồng dưỡng sinh | `CL-FD1` | follow/save | R1+R3 | NEEDS_HUMAN_REVIEW |
| `TL-M5-CAL-D06` | `TL-P3` | static | Quy trình 8 bước — minh bạch | A: liệt kê 8 bước · B: "xin phép trước mỗi thao tác" · C: bước sàng lọc/ khuyến nghị khám | `CL-OP2` | save | R1 | DRAFT |
| `TL-M5-CAL-D07` | `TL-P1` | Reel | Recap định vị tuần 1 | A: tóm 3 ý · B: "Toplink là/không là" · C: mời theo dõi | `CL-ID1`,`CL-M1` | follow/save | R1+R2 | DRAFT |

### Tuần 2 — Hiểu & lắng nghe cơ thể (`TL-P2` + `TL-P4`) — HEALTH-SENSITIVE

| ID | Pillar | Format | Angle chính | A / B / C option | Claim | CTA | Review | Approval |
|---|---|---|---|---|---|---|---|---|
| `TL-M5-CAL-D08` | `TL-P2` | Reel | Tín hiệu cổ vai gáy do ngồi nhiều | A: mô tả cảm giác quen thuộc · B: thói quen nhỏ giữa giờ · C: khi nào nên hỏi chuyên môn | `CL-M2`,`CL-P2` | save | R1+R2+R3 | NEEDS_HUMAN_REVIEW |
| `TL-M5-CAL-D09` | `TL-P4` | static | Lý–Dược–Dưỡng dễ hiểu | A: 3 lớp là gì · B: "đúng người/đúng lúc" · C: giới hạn & lưu ý | `CL-M4` | save | R1+R3 | NEEDS_HUMAN_REVIEW |
| `TL-M5-CAL-D10` | `TL-P2` | carousel | Thói quen nhỏ, đều đặn | A: 5 thói quen · B: 1 thói quen/ngày · C: lắng nghe cơ thể | `CL-M2`,`CL-P2` | save/share | R1+R3 | NEEDS_HUMAN_REVIEW |
| `TL-M5-CAL-D11` | `TL-P2` | Reel | Hỗ trợ làm ấm & thư giãn | A: cảm giác làm ấm · B: nhịp thở/dừng lại · C: support-level framing | `CL-M2`,`CL-P2` | save | R1+R2+R3 | NEEDS_HUMAN_REVIEW |
| `TL-M5-CAL-D12` | `TL-P4` | carousel | "Đúng người, đúng cách, đúng thời điểm" | A: nguyên tắc cá nhân hóa · B: 3 câu hỏi trước khi chọn · C: nhóm cần thận trọng | `CL-M4` | save | R1+R3 | NEEDS_HUMAN_REVIEW |
| `TL-M5-CAL-D13` | `TL-P2` | static | Nhóm cần thận trọng (caregiver) | A: bệnh nền/mang thai/cấy ghép · B: hỏi trước khi dùng · C: hiếu thảo & an tâm | `CL-M2`,`CL-P2` | save/share | R1+R3 | NEEDS_HUMAN_REVIEW |
| `TL-M5-CAL-D14` | `TL-P4` | Reel | Dưỡng liệu — trải nghiệm khách hàng | A: trải nghiệm tại trung tâm · B: "theo hướng dẫn" · C: chăm sóc định kỳ | `CL-CX1`,`CL-M4` | save | R1+R2+R3 | NEEDS_HUMAN_REVIEW |

### Tuần 3 — Bằng chứng vận hành (`TL-P3`)

| ID | Pillar | Format | Angle chính | A / B / C option | Claim | CTA | Review | Approval |
|---|---|---|---|---|---|---|---|---|
| `TL-M5-CAL-D15` | `TL-P3` | Reel | Tầng 1–2: TĨNH & THÔNG | A: đón tiếp/check-in · B: gội dưỡng sinh/ngâm chân · C: chất liệu xuyên sáng | `CL-OP1`,`CL-M3` | follow/save | R1+R2 | DRAFT |
| `TL-M5-CAL-D16` | `TL-P3` | carousel | Quy trình 8 bước minh bạch | A: 8 thẻ bước · B: "giải thích trước khi làm" · C: bước sàng lọc rủi ro | `CL-OP2`,`CL-M3` | save | R1 | DRAFT |
| `TL-M5-CAL-D17` | `TL-P3` | static | Vệ sinh & sự chỉn chu | A: quy chuẩn vệ sinh · B: "thơm dịu, sạch, yên" · C: chi tiết không gian | `CL-OP3` | follow/save | R1 | DRAFT |
| `TL-M5-CAL-D18` | `TL-P3` | Reel | Hậu trường đội ngũ (nghề có tâm) | A: chuẩn bị trước buổi · B: "xin phép trước thao tác" · C: chăm chút chi tiết | `CL-OP3` (no qualification claim) | follow/save | R1+R2 | DRAFT |
| `TL-M5-CAL-D19` | `TL-P3` | static | Tầng 3–4: DƯỠNG & TỈNH | A: xông/ngâm/đá nóng · B: trà/thiền/workshop · C: không gian cộng đồng | `CL-OP1` | save | R1 | DRAFT |
| `TL-M5-CAL-D20` | `TL-P5` | static | Nghề có tâm & cộng đồng | A: giá trị đào tạo · B: "đôi tay + trái tim lắng nghe" · C: mời cộng đồng | `CL-FD1` | follow/share | R1+R3 | NEEDS_HUMAN_REVIEW |
| `TL-M5-CAL-D21` | `TL-P3` | Reel | Khoảnh khắc tạo niềm tin | A: nhớ điều khách dặn · B: nói rõ phù hợp/không phù hợp · C: không ép mua khi đang thư giãn | `CL-OP3`,`CL-M3` | follow/save | R1+R2 | DRAFT |

### Tuần 4 — SAFE FALLBACK (recap; không dossier PASS → Branch B mặc định)

| ID | Pillar | Format | Angle chính | A / B / C option | Claim | CTA | Review | Approval |
|---|---|---|---|---|---|---|---|---|
| `TL-M5-CAL-D22` | `TL-P1` | static | Recap "Toplink là ai / không phải" | A: tóm định vị · B: giá trị Thân–Tâm–Trí · C: giới hạn rõ | `CL-ID1`,`CL-M1` | follow/save | R1 | DRAFT |
| `TL-M5-CAL-D23` | `TL-P2` | Reel | Recap lắng nghe cơ thể | A: 1 tín hiệu + 1 thói quen · B: nhịp dừng lại · C: khi nào hỏi chuyên môn | `CL-M2`,`CL-P2` | save | R1+R2+R3 | NEEDS_HUMAN_REVIEW |
| `TL-M5-CAL-D24` | `TL-P5` | static | Hành trình & cộng đồng | A: cột mốc ý niệm · B: lời cảm ơn cộng đồng · C: mời đồng hành | `CL-FD1` | follow/share | R1+R3 | NEEDS_HUMAN_REVIEW |
| `TL-M5-CAL-D25` | `TL-P1` | Reel | Recap giá trị thương hiệu | A: 3 giá trị · B: "chăm sóc chủ động" · C: mời theo dõi | `CL-ID1`,`CL-M1` | follow/save | R1+R2 | DRAFT |
| `TL-M5-CAL-D26` | `TL-P4` | carousel | Lý–Dược–Dưỡng — trải nghiệm | A: 3 lớp recap · B: "đúng nhu cầu" · C: chăm sóc định kỳ | `CL-CX1`,`CL-M4` | save | R1+R3 | NEEDS_HUMAN_REVIEW |
| `TL-M5-CAL-D27` | `TL-P2` | Reel | Thói quen chăm sóc chủ động | A: 1 thói quen mỗi ngày · B: lắng nghe & nghỉ ngơi · C: nhắc nhóm thận trọng | `CL-M2`,`CL-P2` | save/share | R1+R2+R3 | NEEDS_HUMAN_REVIEW |
| `TL-M5-CAL-D28` | `TL-P5` | static | Mời cộng đồng dưỡng sinh | A: tổng kết 4 tuần · B: giá trị cộng đồng · C: theo dõi & lưu | `CL-FD1` | follow/save/share | R1+R3 | NEEDS_HUMAN_REVIEW |

## 4. Special priority slots (không bind ngày cứng)

Lễ/ra mắt/sự kiện là *priority slot* chèn vào chuỗi tương đối khi lịch thật được duyệt (`TL-M6`),
KHÔNG gán ngày tuyệt đối ở phase này. Ứng viên: ngày khai trương/giới thiệu không gian (→ `TL-P3`),
sự kiện cộng đồng/workshop (→ `TL-P5`), mùa lễ (→ `TL-P1`/`TL-P2` với disclaimer). Mỗi slot vẫn theo
cùng review route + CTA + claim rule.

## 5. VERIFY (TL-M5 calendar)

- [x] 28 identity tương đối `D-1..D-28`, mỗi ngày 1 item, stable ID duy nhất.
- [x] Mỗi item có A/B/C option, pillar, format, claim ID + source, CTA, review route, approval state.
- [x] Pillar phân bổ 6/6/8/4/4 = 28 (≈20/20/30/15/15); 12 Reels (~3/tuần).
- [x] CTA chỉ follow/save/share; không booking/giá/tư vấn/mua.
- [x] 10 item sức khỏe (`TL-P2`/`TL-P4`) → `NEEDS_HUMAN_REVIEW` + disclaimer §3.3.
- [x] Không ngày tuyệt đối; special dates = priority slot, không bind.
- [x] Không item `APPROVED`/publish-ready; `external_writes=0`.
