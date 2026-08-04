# TL-M5 Run 1 Phase A — Agency review + safety ledger (Toplink Y Viện)

> **Local-only · `external_writes=0`.** Coordinated Agency review theo workstream (≤3 agent/workstream,
> no competing versions). Allowed verdicts: `DRAFT`/`REVIEWED`/`VERIFIED`/`PASS`/`FAIL`/`NEEDS_HUMAN_REVIEW`.
> **Không reviewer nào cấp human `APPROVED`.** DMP `3.15.1`, active brand `toplink-y-vien`.

## 1. Workstream A — Calendar & copy: Content Creator → PR Manager

- **Scope:** `month-calendar.md` `0d2d2d16…`, `production-briefs.md` `42cb8e7d…`, `asset-and-batch-plan.md` `435969cf…`, `workflow-approval-measurement.md` `651dff61…`.
- **Content Creator verdict:** `REVIEWED` → structural `PASS`. 28 identity đủ field; A/B/C option; pillar
  6/6/8/4/4=28; CTA follow/save/share; claim ID + source gắn mọi item; placeholder-asset only.
- **PR Manager verdict:** `PASS` (structural/compliance) **+ `NEEDS_HUMAN_REVIEW`** cho:
  - 10 health item (`TL-P2`/`TL-P4`): cần professional/human trước publish.
  - Public positioning (định vị `HYPOTHESIS · NOT_PUBLIC_APPROVED`) chưa human-approved.
  - Founder item (D05/D20/D24/D28): allowed-use + consent.
  - Product-adjacent (D14/D26): `TL-GAP-010` fail-closed.
- **Escalation:** health/positioning/founder/product → human owner gate.

## 2. Workstream B — Reels: Short-Video Coach → TikTok Strategist (mechanics-only)

- **Scope:** `reels-briefs.md` `51b18d91…` (12 Reels).
- **Short-Video Coach verdict:** `REVIEWED` → `PASS` (mechanics). 9:16, hook 0–3s không giật gân,
  subtitle bắt buộc, safe-zone chuẩn (14% trên/20% dưới), disclaimer ≥5s cho health, editing cơ bản khả thi.
- **TikTok Strategist verdict:** `REVIEWED` (mechanics-only). Retention/nhịp cắt/subtitle động tham chiếu
  hợp lệ. **Ghi rõ:** TikTok KHÔNG phải kênh publish; chỉ review cơ chế; không cross-post.
- **Escalation:** 6 Reels health (D08/D11/D14/D23/D27 + D14 product) → `NEEDS_HUMAN_REVIEW` (workstream A/safety).

> Workstream B = 2 agent (≤3 ✓). Không tạo competing version của bất kỳ Reel nào.

## 3. Workstream C — Safety: PR Manager → human/professional gate

- **Real authoring (2026-08-04):** the 5 deliverables were re-invoked via real DMP authoring-subagent
  dispatch (content-calendar, content-engine, video-script) with raw output + metadata captured to
  `raw-repair/` (`dmp-trace.md` §2); all 5 reconciled as KEEP (byte-unchanged).
- **Deterministic DMP check layer (separate, `eval-runner.py`):** the `check` capability runs
  `scripts/eval-runner.py --action run-full` + `scripts/hallucination-detector.py --action detect` over the 5
  deliverables (`logged=false`), raw JSON under `raw-repair/check/`. Result: **0 CRITICAL flags, 0
  auto-reject** on all 5; low composite (`reels-briefs.md` 44) = generic-scorer false-positives on in-file
  Reels mechanics; `production-briefs`/`workflow` "only" flags = Vietnamese governance phrases. Evidence in
  `dmp-trace.md` §3. Check is recorded as `check` only, not as an authoring capability.
- **PR Manager (safety) verdict:** `NEEDS_HUMAN_REVIEW` overall — mọi material health claim an toàn ở mức
  agency (support-level + disclaimer) nhưng **phải** qua human/professional trước publish. Safety ledger §4.
  Deterministic check PASS (0 critical) does **not** substitute for the human/professional health gate.
- **Escalation owner:** human owner (Guru, minhkhang.guru) + teacher "Thảo Tây" (person-level, user-attested
  per `TL-D17`) cho health; human owner cho legal/franchise/privacy/positioning.

## 4. Safety ledger (mọi material claim)

| Item/claim | Location | Classification | Evidence | Repair | Disclaimer | Escalation owner |
|---|---|---|---|---|---|---|
| `CL-ID1` không phải bệnh viện / không cam kết chữa khỏi | D01,02,04,07,22,25; reels | `ALLOWABLE_WITH_SOURCE` | positioning §2 `7c216e38…` | none | none | — |
| `CL-M1` "chăm sóc bắt đầu từ lắng nghe" | identity items | `ALLOWABLE_WITH_SOURCE` | positioning §4 M1 | none | none | — |
| `CL-M2` hỗ trợ thư giãn/làm ấm/lưu thông/giảm đau mỏi | D08,10,11,13,23,27 | `NEEDS_HUMAN_REVIEW` | safety §3.1 preferred; efficacy `UNVERIFIED` | giữ support-level, cấm efficacy/outcome | **§3.3 bắt buộc** + individual-variation | human/professional |
| `CL-M3` không gian/quy trình minh bạch | operational items | `ALLOWABLE_WITH_SOURCE` | positioning §4 M3; dossier §7 | operational-only | none | — |
| `CL-M4` Lý–Dược–Dưỡng | D09,12,26 | `NEEDS_HUMAN_REVIEW` | naming `TOPLINK_CONFIRMED`/efficacy `UNVERIFIED` | naming + "đúng người/lúc"; cấm efficacy | **§3.3 bắt buộc** | human/professional |
| `CL-OP1` 4 tầng | D03,15,19 | `ALLOWABLE_WITH_SOURCE` | dossier §7.1 `645b1ad2…` | real imagery; no outcome | none | — |
| `CL-OP2` 8 bước | D06,16 | `ALLOWABLE_WITH_SOURCE` | dossier §7.2 | no qualification/outcome | none | — |
| `CL-OP3` vệ sinh/BTS | D17,18,21 | `ALLOWABLE_WITH_SOURCE` | dossier §7.3 | **no staff qualification claim**; consent BTS | none | consent owner |
| `CL-CX1` product-adjacent (dưỡng liệu) | D14,26 | `NEEDS_HUMAN_REVIEW` | `11_Product_Yvien.md` `df367e1b…` `UNVERIFIED` | **customer-experience only; no product/efficacy** | **§3.3 bắt buộc** | human (`TL-GAP-010`) |
| `CL-FD1` founder/hành trình | D05,20,24,28 | `NEEDS_HUMAN_REVIEW` | narrative §3 allowed-use gated | no cơ chế/chỉ định/chẩn đoán; ≤1/5 founder-led | none | human + consent |
| Franchise/legal wording | — (không dùng) | `BLOCKED` | `PENDING_DOCUMENT` (`TL-GAP-002/009`, `TL-D16`) | fail-closed, không dùng | n/a | human owner |
| Testimonial/UGC generalized | — (không dùng) | `BLOCKED` | không có documented consent | fail-closed; chỉ khi consent OBTAINED | n/a | human owner |
| Commercial CTA (booking/giá/tư vấn/mua) | — (không dùng) | `REWRITE_REQUIRED` (đã xử lý) | dossier §11.6 nguồn có commercial CTA | **đã thay bằng follow/save/share**; khoá tới offer gate | n/a | offer gate (chưa có) |
| Diagnosis/treatment/cure/guarantee/medical-replacement | — (không dùng) | `BLOCKED` | safety §3.2 forbidden | fail-closed | n/a | human owner |

**Fail-closed confirmed:** diagnosis/treatment/cure/prevention, guarantee, medical replacement, unsupported
efficacy, unsupported franchise/legal, missing consent, privacy-sensitive — 0 xuất hiện dưới dạng claim.

## 5. Aggregate verdict

- **Agency structural/compliance:** `PASS`.
- **Overall:** `NEEDS_HUMAN_REVIEW` — health (10 item), public positioning, founder (4), product-adjacent
  (2) chờ human/professional gate.
- **Reviewers:** Content Creator, PR Manager (workstream A + C), Short-Video Coach, TikTok Strategist
  (workstream B). ≤3/workstream ✓. No competing versions.
- **No `APPROVED` granted. No publish. `external_writes=0`. `milestone_advanced=false`.**
