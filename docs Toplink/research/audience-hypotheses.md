# TL-M3 — Audience hypotheses (Toplink Y Viện)

> **Run 1 Phase A · local-only · `external_writes=0`.** DMP `audience-intelligence` (v3.15.1,
> hypothesis-only / limited-data branch) applied to launch hypotheses `TL-A01`–`TL-A04`
> (master plan §8). **Every persona is `LAUNCH_AUDIENCE_HYPOTHESIS`, not observed insight.** No
> demographic/behavioral data exists (greenfield, follower 0). Stable ID `TL-AUDIENCE-001`.
> Logical Sheet dataset: `TL_AUDIENCE_POSITIONING`.

## 0. Data-quality declaration

- Data level: **hypothesis-only.** No CRM, analytics, survey, or interview data. Page is greenfield
  (`TL-D02`/`TL-D03`, follower 0, `NO_MEASUREMENT`).
- Method: JTBD + six-dimension persona built from business model (Local Business, health-sensitive
  regulated) + product/service architecture + master plan §8 hypotheses. Labeled "Hypothesis — v1".
- Validation cadence: revisit after 30–60 days of real Page signal (`TL-M4` KPI plan owns the signals).

## 1. Verdict summary — keep / edit / drop

| ID | Hypothesis (master plan §8) | Verdict | Rationale |
|---|---|---|---|
| `TL-A01` | Người bận rộn/văn phòng 28–55, Hà Nội | **KEEP** | Matches Hà Nội local service lane (`TL-D08`) + trust-led, low-pressure care job; primary conversion candidate when offer gate opens. |
| `TL-A02` | Trung niên/lớn tuổi + người chăm sóc cha mẹ | **KEEP (edit)** | Highest health-sensitivity; split the *caregiver* sub-job from the *elder self* sub-job — different reassurance need + different reviewer gate. |
| `TL-A03` | Phụ nữ quan tâm sức khỏe chủ động | **KEEP** | Aligns with space/experience assets (4-floor, refined aesthetic) and privacy/discretion job; strong save/share candidate. |
| `TL-A04` | Người quan tâm dưỡng sinh toàn quốc | **KEEP (bound)** | Valid for national **awareness/education only**; explicitly **not** a service-demand segment (`TL-D08` boundary). No national service inference. |

No hypothesis dropped; none promoted to confirmed persona. `TL-A02` edited into two sub-jobs below.

## 2. Persona hypotheses (six-dimension, JTBD)

### `TL-A01` — "Người bận rộn tìm cách chăm sóc dễ hiểu" (Hà Nội)
- **Demographic (hyp.):** 28–55, văn phòng/bận rộn, Hà Nội. Income/education `MISSING_INPUT`.
- **JTBD — functional:** tìm một cách chăm sóc cơ thể đều đặn, dễ hiểu, không bị ép mua.
- **JTBD — social:** được xem là người biết chăm sóc bản thân một cách chỉn chu, có hiểu biết.
- **JTBD — emotional:** an tâm, không bị hù dọa, không áp lực bán.
- **Struggling moment:** đau mỏi cổ vai gáy/căng cứng do ngồi nhiều; muốn giải pháp nhưng ngại "bán hàng sức khỏe".
- **Behavioral (hyp.):** lướt Facebook; phản hồi nội dung giải thích rõ ràng, minh bạch giới hạn.
- **Trusted signals:** quy trình rõ ràng, không gian thật, ngôn ngữ không phóng đại.
- **Validation signal (master plan §8):** save/share, câu hỏi về quy trình, qualified inquiry.
- **CTA state:** follow/save trước offer gate; booking chỉ khi Hà Nội offer verify.

### `TL-A02a` — "Người trung niên/lớn tuổi muốn an tâm về phạm vi"
- **JTBD — functional:** hiểu liệu cách chăm sóc này có phù hợp và an toàn với thể trạng mình.
- **JTBD — emotional:** an tâm về mức tác động và giới hạn; không sợ bị thổi phồng.
- **Validation signal:** câu hỏi phù hợp/an toàn, repeat interaction.
- **Gate:** health-sensitive cao nhất → mọi item cần disclaimer + professional/human review (`TL-D13`).

### `TL-A02b` — "Người chăm sóc cha mẹ" (caregiver)
- **JTBD — functional:** tìm cách chăm sóc phù hợp cho cha mẹ; sàng lọc rủi ro.
- **JTBD — social:** làm tròn trách nhiệm hiếu thảo.
- **JTBD — emotional:** yên tâm rằng lựa chọn không gây hại; cần hướng dẫn rõ chống chỉ định.
- **Validation signal:** câu hỏi thay người thân, lưu bài để tham khảo.
- **Gate:** nhấn mạnh nhóm chống chỉ định (bệnh nền/mang thai/thiết bị cấy ghép); không outcome claim.

### `TL-A03` — "Phụ nữ quan tâm sức khỏe chủ động, tinh tế"
- **JTBD — functional:** trải nghiệm chăm sóc tinh tế, riêng tư, minh bạch.
- **JTBD — social:** thuộc nhóm sống chất lượng, chăm sóc bản thân có gu.
- **JTBD — emotional:** được tôn trọng sự riêng tư; tin vào sự chỉn chu.
- **Validation signal:** engagement với proof không gian/quy trình.
- **Asset fit:** không gian 4 tầng + visual refined (New Chinese, ivory/wine/brass) là proof mạnh nhất.

### `TL-A04` — "Người quan tâm dưỡng sinh toàn quốc" (awareness-only)
- **JTBD — functional:** học kiến thức và thói quen dưỡng sinh dễ áp dụng tại nhà.
- **JTBD — emotional:** cảm giác chủ động chăm sóc sức khỏe mà không cần đến cơ sở.
- **Validation signal:** completion, save/share. **Không** coi là service demand.
- **Boundary:** education/awareness toàn quốc; cấm ngụ ý có cơ sở/dịch vụ tại địa phương ngoài Hà Nội.

## 3. Anti-personas (exclude)

| Anti-persona | Why excluded | Identification signal |
|---|---|---|
| Người tìm "chữa khỏi bệnh"/điều trị dứt điểm | Toplink không chẩn đoán/điều trị/cam kết; fail-closed | Comment/inbox đòi cam kết khỏi, hỏi "chữa được bệnh X không" → route to safety framing, không đưa vào offer path |
| Săn khuyến mãi/giá rẻ | Trust-led premium; chưa có offer/giá | Chỉ hỏi giá/giảm giá, không quan tâm quy trình |
| Người cần cấp cứu/triệu chứng cấp | Rủi ro y tế; phải chuyển chuyên môn | Mô tả triệu chứng cấp/nặng → escalate to medical care, never conversion |
| Nhu cầu dịch vụ tại tỉnh ngoài Hà Nội | Không có cơ sở/dịch vụ được verify ngoài Hà Nội | Hỏi đặt lịch/địa chỉ ngoài Hà Nội → awareness content only |

## 4. Segment → activation (hypothesis)

- Priority for **conversion readiness (when gate opens):** `TL-A01` > `TL-A03` > `TL-A02a/b` (Hà Nội).
- Priority for **awareness/reach:** `TL-A04` (national) + all Hà Nội segments.
- Channel: Facebook Page primary for all; Reels for discovery (`TL-A01`, `TL-A04`).
- No lookalike/paid seed defined — paid is out of scope until `TL-M8` gate.

## 5. VERIFY (TL-M3 audience)

- [x] No audience fact stated without a source; every persona labeled `HYPOTHESIS`.
- [x] Hà Nội service/conversion vs national awareness separated (`TL-A04` bound to awareness).
- [x] No national-service inference.
- [x] Anti-personas defined incl. health fail-closed cases.
- [x] `external_writes=0`; validation deferred to real signal (`TL-M4`).
