# TL-M5 — Production briefs (Toplink Y Viện)

> **Run 1 Phase A · local-only · `external_writes=0`.** DMP `content-engine` + `video-script` +
> `content-calendar` (v3.15.1). Brief sản xuất cho 28 item; mỗi item có: hook · shot · on-screen text ·
> caption · CTA · claim ID · source · review route · approval state · measurement mapping. Stable ID
> `TL-M5-PRODBRIEF-001`. Logical Sheet dataset: `TL_CONTENT_CALENDAR` + `TL_REELS_PRODUCTION`. Không
> item nào `APPROVED`/publish-ready.

## 0. Legend

- **Claim/source:** xem claim register ở `month-calendar.md §1`. `TOPLINK_CONFIRMED` / `UNVERIFIED` /
  allowed-use-gated.
- **Review:** R1 Content Creator→PR · R2 Short-Video Coach→TikTok (mechanics) · R3 PR→human/professional.
- **Measurement (KPI dict `kpi-experiment-plan.md`):** KPI-01 reach · KPI-02 impressions · KPI-03 reel
  starts · KPI-04 save/share · KPI-05 completion · KPI-06 on-topic questions · KPI-10 risk signals · KPI-11
  ops adherence. Rate KPI = `N/A` tới khi đủ minimum sample; **không `% from zero`.**
- **Approval:** `DRAFT` (thường) / `NEEDS_HUMAN_REVIEW` (sức khỏe/founder/product-adjacent). Không `APPROVED`.
- **CTA:** chỉ `Theo dõi` / `Lưu` / `Chia sẻ` (trước offer gate).

## 1. Master production table (28 item)

| ID | Fmt | Hook (default; A/B/C ở calendar) | Shot / visual | On-screen text | CTA | Claim | Source | Review | Approval | KPI |
|---|---|---|---|---|---|---|---|---|---|---|
| D01 | Reel | "Bạn có đang chăm sóc cơ thể đều đặn?" | WS không gian→MS lễ tân→text-card | "Chăm sóc chủ động, không thay thế y khoa" | Theo dõi·Lưu | `CL-ID1`,`CL-M1` | CONFIRMED | R1+R2 | DRAFT | 01,03,04 |
| D02 | static | "Toplink KHÔNG phải là…" | this/not-that card | 3 ranh giới rõ | Theo dõi·Lưu | `CL-ID1` | CONFIRMED | R1 | DRAFT | 01,04 |
| D03 | Reel | "Một khoảng dừng có chủ đích" | pan 4 tầng (AST-SPACE-4F) | tên 4 tầng | Theo dõi·Lưu | `CL-OP1` | CONFIRMED | R1+R2 | DRAFT | 01,03,04,05 |
| D04 | carousel | "Thân – Tâm – Trí" | 3 thẻ giá trị | 3 trụ + giới hạn | Lưu·Chia sẻ | `CL-M1`,`CL-ID1` | CONFIRMED | R1 | DRAFT | 04 |
| D05 | static | "Một ý niệm rất đời" | ảnh founder (AST-FOUNDER, consent) | câu ý niệm | Theo dõi·Lưu | `CL-FD1` | allowed-use gated | R1+R3 | NEEDS_HUMAN_REVIEW | 04,10 |
| D06 | static | "8 bước — minh bạch từ đầu" | thẻ 8 bước | 8 bước rút gọn | Lưu | `CL-OP2` | CONFIRMED | R1 | DRAFT | 04,06 |
| D07 | Reel | "3 điều nên biết về Toplink" | ghép b-roll W1+text | "LÀ / KHÔNG LÀ" | Theo dõi·Lưu | `CL-ID1`,`CL-M1` | CONFIRMED | R1+R2 | DRAFT | 01,03,04 |
| D08 | Reel | "Cổ vai gáy căng sau ngày ngồi nhiều?" | người ngồi→thả lỏng→text | "Hỗ trợ thư giãn — không thay thế chẩn đoán" | Lưu | `CL-M2` | CONFIRMED(support)/efficacy UNVERIFIED | R1+R2+R3 | NEEDS_HUMAN_REVIEW | 03,04,06,10 |
| D09 | static | "Lý – Dược – Dưỡng là gì?" | 3 lớp graphic | 3 lớp + giới hạn | Lưu | `CL-M4` | naming CONFIRMED/efficacy UNVERIFIED | R1+R3 | NEEDS_HUMAN_REVIEW | 04,06,10 |
| D10 | carousel | "Thói quen nhỏ, đều đặn" | 5 thẻ thói quen | mỗi thẻ 1 thói quen | Lưu·Chia sẻ | `CL-M2` | CONFIRMED(support) | R1+R3 | NEEDS_HUMAN_REVIEW | 04,06,10 |
| D11 | Reel | "Một khoảng dừng để làm ấm" | cận làm ấm (placeholder), tông ấm | support phrasing | Lưu | `CL-M2` | CONFIRMED(support) | R1+R2+R3 | NEEDS_HUMAN_REVIEW | 03,04,10 |
| D12 | carousel | "Đúng người, đúng cách, đúng lúc" | 3 thẻ nguyên tắc | 3 câu hỏi + nhóm thận trọng | Lưu | `CL-M4` | naming CONFIRMED | R1+R3 | NEEDS_HUMAN_REVIEW | 04,06,10 |
| D13 | static | "Nhóm cần thận trọng" | thẻ lưu ý | bệnh nền/mang thai/cấy ghép | Lưu·Chia sẻ | `CL-M2` | CONFIRMED(support) | R1+R3 | NEEDS_HUMAN_REVIEW | 04,06,10 |
| D14 | Reel | "Chăm sóc như một thói quen" | không gian dưỡng liệu (no label) | "Trải nghiệm — theo hướng dẫn" | Lưu | `CL-CX1`,`CL-M4` | UNVERIFIED (customer-exp only) | R1+R2+R3 | NEEDS_HUMAN_REVIEW | 03,04,10 |
| D15 | Reel | "Được gọi bằng tên khi bước vào" | tầng 1–2 (AST-SPACE-4F) | tên tầng TĨNH/THÔNG | Theo dõi·Lưu | `CL-OP1`,`CL-M3` | CONFIRMED | R1+R2 | DRAFT | 01,03,04,05 |
| D16 | carousel | "Giải thích trước khi làm" | 8 thẻ bước | 8 bước | Lưu | `CL-OP2`,`CL-M3` | CONFIRMED | R1 | DRAFT | 04,06 |
| D17 | static | "Thơm dịu, sạch, yên" | chi tiết vệ sinh | quy chuẩn vệ sinh | Theo dõi·Lưu | `CL-OP3` | CONFIRMED | R1 | DRAFT | 04 |
| D18 | Reel | "Chuẩn bị trước mỗi buổi" | BTS đội ngũ (AST-TEAM-BTS, consent) | "xin phép trước thao tác" | Theo dõi·Lưu | `CL-OP3` | CONFIRMED (no qualification) | R1+R2 | DRAFT | 01,03,04 |
| D19 | static | "Nghỉ ngơi & chuyển hóa" | tầng 3–4 | tên tầng DƯỠNG/TỈNH | Lưu | `CL-OP1` | CONFIRMED | R1 | DRAFT | 04 |
| D20 | static | "Đôi tay + trái tim lắng nghe" | đào tạo/cộng đồng | giá trị nghề có tâm | Theo dõi·Chia sẻ | `CL-FD1` | allowed-use gated | R1+R3 | NEEDS_HUMAN_REVIEW | 04,10 |
| D21 | Reel | "Không ép mua khi đang thư giãn" | moment tin cậy (placeholder) | minh bạch giới hạn | Theo dõi·Lưu | `CL-OP3`,`CL-M3` | CONFIRMED | R1+R2 | DRAFT | 01,03,04,05 |
| D22 | static | "Toplink là ai / không phải" | recap card | tóm định vị | Theo dõi·Lưu | `CL-ID1`,`CL-M1` | CONFIRMED | R1 | DRAFT | 04 |
| D23 | Reel | "1 tín hiệu + 1 thói quen" | khung body-literacy | support phrasing | Lưu | `CL-M2` | CONFIRMED(support) | R1+R2+R3 | NEEDS_HUMAN_REVIEW | 03,04,10 |
| D24 | static | "Từ ý niệm đến hôm nay" | cột mốc hành trình | lời cảm ơn cộng đồng | Theo dõi·Chia sẻ | `CL-FD1` | allowed-use gated | R1+R3 | NEEDS_HUMAN_REVIEW | 04,10 |
| D25 | Reel | "3 giá trị của Toplink" | text-card + b-roll | "chăm sóc chủ động" | Theo dõi·Lưu | `CL-ID1`,`CL-M1` | CONFIRMED | R1+R2 | DRAFT | 01,03,04 |
| D26 | carousel | "Lý – Dược – Dưỡng, đúng nhu cầu" | 3 thẻ recap | customer-experience | Lưu | `CL-CX1`,`CL-M4` | UNVERIFIED (customer-exp only) | R1+R3 | NEEDS_HUMAN_REVIEW | 04,06,10 |
| D27 | Reel | "1 thói quen mỗi ngày" | khung body-literacy | nhắc nhóm thận trọng | Lưu·Chia sẻ | `CL-M2` | CONFIRMED(support) | R1+R2+R3 | NEEDS_HUMAN_REVIEW | 03,04,10 |
| D28 | static | "Cùng nhau dưỡng sinh" | tổng kết 4 tuần | mời cộng đồng | Theo dõi·Lưu·Chia sẻ | `CL-FD1` | allowed-use gated | R1+R3 | NEEDS_HUMAN_REVIEW | 04,07 |

## 2. Caption skeletons (khung — chủ hoàn thiện; chưa phải bản đăng)

> Cấu trúc: **hook** → **1–2 ý giá trị (support/operational)** → **giới hạn/ranh giới** →
> **CTA follow/save/share** → **[disclaimer §3.3 nếu health]**. Tránh forbidden term; ưu tiên "hỗ trợ…".
> `DISCLAIMER_HOST_PENDING (TL-M1: docs Toplink/system/health-compliance.md)`: không đổi wording hiện có; human/professional phải xác nhận bản cuối trước publish.

- **Identity (`TL-P1`) — D01/D02/D04/D07/D22/D25:**
  > [Hook đời thường]. Toplink là nơi chăm sóc cơ thể **chủ động** — bắt đầu từ việc lắng nghe. Toplink
  > **không** phải bệnh viện và không cam kết chữa khỏi; điều Toplink làm là đồng hành để bạn hiểu cơ thể
  > mình rõ hơn mỗi ngày. Theo dõi Page để cùng chăm sóc đều đặn. [Lưu lại nếu hữu ích.]

- **Operational proof (`TL-P3`) — D03/D06/D15/D16/D17/D18/D19/D21:**
  > [Hook chi tiết không gian/quy trình]. Tại Toplink, [tầng/bước] được [mô tả operational] — minh bạch,
  > giải thích "vì sao" trước khi đề xuất "làm gì". Đây là điều bạn thấy khi bước vào. Theo dõi/Lưu để xem
  > tiếp hành trình 4 tầng · 8 bước.

- **Body-literacy (`TL-P2`) — D08/D10/D11/D13/D23/D27 [HEALTH]:**
  > [Hook tín hiệu quen thuộc, không hù dọa]. Đây là cảm giác nhiều người gặp khi [bối cảnh đời thường].
  > Một vài thói quen nhỏ có thể **hỗ trợ thư giãn / hỗ trợ giảm cảm giác đau mỏi**. Nếu cảm giác kéo dài
  > hoặc bất thường, hãy tham khảo ý kiến chuyên môn. Lưu lại để nhớ.
  > *[Disclaimer §3.3 nguyên văn — bắt buộc cuối bài.]*

- **Lý–Dược–Dưỡng (`TL-P4`) — D09/D12/D26 [HEALTH]:**
  > [Hook]. Lý – Dược – Dưỡng là cách Toplink sắp xếp việc chăm sóc **đúng người, đúng cách, đúng thời
  > điểm** — với giới hạn rõ ràng. Nội dung mang tính giới thiệu trải nghiệm, không phải chỉ định sản phẩm.
  > Lưu lại nếu bạn muốn hiểu thêm.
  > *[Disclaimer §3.3 nguyên văn — bắt buộc cuối bài.]*

- **Product-adjacent (`CL-CX1`) — D14/D26 [HEALTH + `TL-GAP-010` fail-closed]:**
  > [Hook trải nghiệm]. Bài viết mô tả **trải nghiệm chăm sóc tại Y Viện** theo hướng dẫn; **không** nêu
  > công dụng/hiệu quả cụ thể của sản phẩm. Lưu lại để tham khảo.
  > *[Disclaimer §3.3 nguyên văn — bắt buộc cuối bài.]*

- **Founder/community (`TL-P5`) — D05/D20/D24/D28 [allowed-use gated]:**
  > [Hook ý niệm/hành trình]. [Nội dung hành trình/triết lý/cộng đồng — **không** cơ chế/chỉ định/chẩn
  > đoán]. Theo dõi để đồng hành cùng cộng đồng dưỡng sinh. [Chia sẻ nếu thấy giá trị.]

## 3. Measurement mapping (per-item → KPI)

- **TOFU awareness (identity/operational/founder):** KPI-01 reach, KPI-02 impressions, KPI-07 followers.
- **Utility/learning:** KPI-04 save/share, KPI-06 on-topic questions (mọi item khuyến khích save).
- **Reels:** KPI-03 starts, KPI-05 completion (rate = `N/A` tới ≥100 starts).
- **Health items:** thêm KPI-10 risk signals (misread comment/claim-escalation) — log bắt buộc.
- **Ops:** KPI-11 adherence (đúng lịch, SLA review, review failures).
- **KPI-09 qualified inquiry:** `N/A` (gated) — chưa đo tới khi offer/CTA gate PASS.

## 4. VERIFY (TL-M5 production briefs)

- [x] 28 item đủ field: hook · shot · on-screen text · caption · CTA · claim ID · source · review · approval · measurement.
- [x] CTA chỉ follow/save/share; 0 booking/giá/tư vấn/mua.
- [x] Health item (10) → `NEEDS_HUMAN_REVIEW` + disclaimer §3.3 + KPI-10.
- [x] D14/D26 customer-experience only; `11_Product_Yvien.md` không được nâng thành verified.
- [x] Founder item allowed-use gated + consent; no cơ chế/chỉ định.
- [x] Không franchise/legal wording; không forbidden health term; không item `APPROVED`.
- [x] `external_writes=0`.
