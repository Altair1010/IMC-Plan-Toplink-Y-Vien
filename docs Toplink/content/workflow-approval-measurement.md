# TL-M5 — Workflow, approval ledger & measurement (Toplink Y Viện)

> **Run 1 Phase A · local-only · `external_writes=0`.** DMP `content-calendar` + `check` (v3.15.1).
> Fail-closed production→approval→measurement system trước publish. Stable ID `TL-M5-WORKFLOW-001`.
> Logical Sheet dataset: `TL_WORKFLOW_APPROVAL`. **Không item nào tự `APPROVED` hoặc publish-ready.**

## 1. Production → publish workflow (fail-closed)

```text
Ý tưởng (calendar item, A/B/C)
  → Draft copy/script (content-engine/video-script)
  → DMP check (compliance gate)
  → R1 Content Creator → PR Manager (calendar/copy)
  → [nếu video] R2 Short-Video Coach → TikTok Strategist (mechanics-only)
  → [nếu health/founder/product-adjacent] R3 PR Manager → human/professional gate
  → HUMAN APPROVE (chỉ người sở hữu; per-item)  ← GATE DUY NHẤT mở publish
  → Publish (Facebook Page) + log measurement
```

- Không bước reviewer nào cấp `APPROVED`. Verdict agent tối đa: `REVIEWED`/`NEEDS_HUMAN_REVIEW`/`PASS`/`FAIL`.
- **Không publish** khi bất kỳ gate nào chưa PASS. Health item bắt buộc qua R3 + human trước publish.
- CTA thương mại (booking/tư vấn/giá/mua) **khoá** tới khi offer gate tồn tại (chưa có).

## 2. Approval states (per-item)

| State | Ý nghĩa | Ai đặt |
|---|---|---|
| `DRAFT` | Bản nháp, chưa review | tác giả |
| `REVIEWED` | Qua R1 (và R2 nếu video) | Agency reviewer |
| `NEEDS_HUMAN_REVIEW` | Cần human/professional (health/founder/product/legal/privacy) | reviewer |
| `PASS` (agency) | Đạt review chuyên môn của Agency, **chưa** là human approve | reviewer |
| `FAIL` | Vi phạm rule → sửa hoặc bỏ | reviewer |
| `HUMAN_APPROVED` | Người sở hữu duyệt publish (per-item) | **chỉ human owner** |
| `PUBLISHED` | Đã đăng + log measurement | human owner |

Mặc định TL-M5 Phase A: item thường `DRAFT`; item health/founder/product-adjacent `NEEDS_HUMAN_REVIEW`.
**Không** item nào ở `HUMAN_APPROVED`/`PUBLISHED`.

## 3. Approval ledger (gắn content hash/revision)

> Mỗi item 1 dòng ledger. **Content hash** = SHA-256 của bản copy/script cuối. **Material edit reset
> approval:** bất kỳ chỉnh sửa nội dung/claim/CTA/visual có ý nghĩa ⇒ hash đổi ⇒ approval quay về
> `DRAFT`/`NEEDS_HUMAN_REVIEW`, phải review lại. Chỉnh sửa non-material (typo không đổi nghĩa) ghi chú
> nhưng vẫn khuyến nghị re-hash.

### Ledger schema (Sheet `TL_WORKFLOW_APPROVAL`)

| Cột | Kiểu | Mô tả |
|---|---|---|
| `item_id` | text | `TL-M5-CAL-Dnn` (stable identity) |
| `revision` | int | tăng mỗi material edit |
| `content_hash` | sha256 | hash bản nội dung của revision |
| `claim_ids` | list | claim ID dùng (register §1) |
| `risk_class` | enum | `none`/`health`/`founder`/`product-adjacent`/`legal-privacy` |
| `dmp_check` | enum | `PASS`/`WARN`/`BLOCKED` (từ §5) |
| `review_route` | text | R1/R2/R3 |
| `reviewer_verdict` | enum | `DRAFT`/`REVIEWED`/`PASS`/`FAIL`/`NEEDS_HUMAN_REVIEW` |
| `human_gate` | enum | `PENDING`/`HUMAN_APPROVED`/`REJECTED` |
| `consent_state` | enum | `N/A`/`REQUIRED`/`OBTAINED` (founder/BTS/testimonial) |
| `publish_state` | enum | `NOT_PUBLISHED`/`PUBLISHED` |
| `publish_ts` | ts | rỗng tới khi publish |
| `measurement_ref` | text | KPI ids theo `production-briefs §3` |
| `edit_reset_note` | text | ghi khi material edit reset approval |

### Trạng thái ledger hiện tại (Phase A)

Tất cả 28 dòng: `revision=1`, `content_hash` gán khi copy cuối chốt (Phase A tạo khung, hash hoá khi sản
xuất), `human_gate=PENDING`, `publish_state=NOT_PUBLISHED`, `publish_ts` rỗng. Có **14 item distinct**
`NEEDS_HUMAN_REVIEW`: 10 health; trong đó D14/D26 đồng thời product-adjacent; cộng D05/D20/D24/D28
founder. Không cộng trùng D14/D26. **Không dòng nào `HUMAN_APPROVED`.**

## 4. Health / legal / privacy state (giữ nguyên trong Sheet schema)

- `DISCLAIMER_HOST_PENDING (TL-M1: docs Toplink/system/health-compliance.md)`: §3.3 hiện chỉ là wording chờ human/professional xác nhận; không item nào được publish chỉ dựa trên disclaimer hiện có.
- `risk_class=health` (10 item P2/P4): disclaimer §3.3 bắt buộc + individual-variation + nhóm chống chỉ
  định; route R3 + human; log KPI-10.
- `risk_class=legal-privacy`: **không** franchise/legal wording (`TL-D16`); không thu thập PII/health info
  không cần thiết; testimonial/UGC chỉ khi `consent_state=OBTAINED` (mục đích/kênh/thời hạn/thu hồi/redaction).
- `risk_class=product-adjacent` (D14/D26): `11_Product_Yvien.md` `UNVERIFIED` — customer-experience only,
  no product/efficacy claim (`TL-GAP-010` fail-closed). D26 binding = `product-adjacent`; health disclaimer
  và professional/human review vẫn được kế thừa từ `TL-P4`.
- `risk_class=founder` (D05/D20/D24/D28): allowed-use gated + consent; no cơ chế/chỉ định/chẩn đoán.

Các state này là dữ liệu bắt buộc trong Sheet; bounded write chỉ khi có signed `SheetTargetApproval` +
Codex upsert + exact read-back (ngoài scope Phase A; `external_writes=0`).

## 5. DMP check gate (compliance)

Chạy `check` (compliance mode) trước review. Dimension:

| Dimension | Rule | Verdict Phase A |
|---|---|---|
| Forbidden health terms | 0 lần xuất hiện (safety §3.2) | `PASS` (deterministic scan) |
| Mandatory disclaimer | mọi health item có §3.3 + caveat | `PASS` |
| No before/after / medical-fear / generalized testimonial | 0 | `PASS` |
| CTA restriction | chỉ follow/save/share | `PASS` |
| Franchise/legal wording | 0 public wording | `PASS` |
| Product/efficacy claim | 0 direct claim (customer-exp only) | `PASS` |
| Self-APPROVED | 0 item `APPROVED` | `PASS` |
| Hallucination/quality/readability (eval-runner quick) | rubric | `SKIPPED` — bản khung tiếng Việt, health-domain custom rule không nằm trong rubric mặc định; thay bằng deterministic scan ở trên |

**Skipped dimension:** eval-runner.py quick-mode scorer (hallucination/quality/readability) không phù hợp
health-domain tiếng Việt của bộ này ⇒ dùng deterministic compliance scan làm gate thật; ghi rõ skip.

## 6. Measurement plan

- KPI dictionary: `kpi-experiment-plan.md` (TL-KPI-01..11). Counts=0 chỉ sau khi có measurement; rate=`N/A`
  tới đủ minimum sample; **không `% from zero`**; tick xanh không phải KPI.
- Experiment: 1 biến/lần (hook A/B/C, format static-vs-Reel, pillar mix) — quyết định chỉ sau minimum
  sample; Stop khi KPI-10 risk tăng hoặc có claim-misread.
- Health item: log content hash · claim IDs · risk class · dmp_check · reviewer/human · publish state (không
  null→approved default).

## 7. VERIFY (TL-M5 workflow/approval/measurement)

- [x] Workflow fail-closed; human là gate duy nhất mở publish; reviewer không cấp `APPROVED`.
- [x] Approval ledger gắn content hash/revision; material edit reset approval (nêu rõ).
- [x] Health/legal/privacy/product/founder state giữ trong Sheet schema; consent gate cho testimonial/founder.
- [x] DMP check dimension liệt kê; skipped dimension ghi đúng lý do.
- [x] Measurement không `% from zero`; KPI-09 gated; health item log đủ.
- [x] Không item `APPROVED`/`PUBLISHED`; `external_writes=0`.
