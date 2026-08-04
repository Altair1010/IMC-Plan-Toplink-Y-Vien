# TL Run 2 Phase A — Source ledger (independent, pre-reconciliation)

> **Run 2 Phase A · fresh Claude · local-only · `external_writes=0`.** Built independently from the
> canonical plan/milestones + frozen `00-input-lock.json` evidence set + the 14 artifact-contract
> outputs, BEFORE reading any withheld Run 1 reasoning. Evidence status vocab per master prompt §5:
> `TOPLINK_CONFIRMED` · `INFERENCE` · `HYPOTHESIS` · `MISSING_INPUT` · `UNVERIFIED` · `DO_NOT_USE`.
> Fail-closed on Page identity, offer, franchise/legal, product efficacy, qualification, price,
> availability, booking, testimonial/UGC consent, asset rights, and Sheet permission.

## 1. Frozen evidence base (source_digest members, all byte-unchanged this run)

| # | Source path | SHA-256 (prefix) | Role |
|---|---|---|---|
| S1 | `spec.md` | `aa8465ea…` | Toplink policy / channel primacy |
| S2 | `docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md` | `aa923b51…` | Strategy + decision register (TL-D01–D15) |
| S3 | `RULES.md` | `96c1bb4c…` | Root governance / cross-brand isolation |
| S4 | `docs Toplink/Ho-so-thuong-hieu-Y-Vien-Toplink-Cai-tien-2026.md` | `645b1ad2…` | Brand dossier (source of brand facts) |
| S5 | `staging/toplink-reconciled/TL-M1-evidence/entity-franchise-allowed-use-map.md` | `56618b18…` | Entity/franchise/product allowed-use |
| S6 | `docs Toplink/staging/run1/00-input-lock.json` | (lock) | Human-owner TL-M5 input decisions |

Digest recompute this run: `profile_digest a45e4ae4… MATCH`, `source_digest 3ba91761… MATCH`
(5-member SHA LF-join + trailing LF), `manifest 99227153… MATCH`, DMP `3.15.1`, brand `toplink-y-vien`.

## 2. Material facts / claims used by the 14 artifacts

| Statement / claim ID | Source path/location | Evidence status | Allowed use | Missing proof / human gate |
|---|---|---|---|---|
| Brand names Nhất Liệu Y Viện Toplink / Y Viện Toplink / Toplink | S4 frontmatter+§1; S5 §1 | `TOPLINK_CONFIRMED` (internal name) | Name within sourced meaning; not "hospital" | — |
| Descriptor "Y Viện Dưỡng Thân – Tỉnh Thức"; slogan "Thân khỏe–Tâm an–Trí sáng" | S4 line 82; knowledge-brief | `TOPLINK_CONFIRMED` (descriptor) | Descriptor/tagline; never legal entity | — |
| Positioning "chăm sóc chủ động, Lý–Dược–Dưỡng" | S2 §9; profile `positioning_statement` | `HYPOTHESIS · NOT_PUBLIC_APPROVED` | Internal working positioning only | Pilot evidence + human gate |
| CL-ID1 "không phải bệnh viện / không chữa khỏi" | positioning §2 | `TOPLINK_CONFIRMED` | Category boundary statement | — |
| CL-M1 "chăm sóc bắt đầu từ lắng nghe" | positioning §4 | `TOPLINK_CONFIRMED` | Message, no gate | — |
| CL-M2 "hỗ trợ thư giãn/làm ấm/lưu thông/phục hồi" | positioning §4; safety §3.1 | `TOPLINK_CONFIRMED` (support-level) | Support framing ONLY | Disclaimer §3.3 + per-item professional/human review |
| CL-M3 "không gian/quy trình minh bạch giới hạn" | positioning §4 | `TOPLINK_CONFIRMED` (operational) | Operational-only | — |
| CL-M4 "hiểu Lý–Dược–Dưỡng" | positioning §4 | naming `TOPLINK_CONFIRMED` / efficacy `UNVERIFIED` | Naming/explain; no efficacy | Per-item professional review |
| CL-OP1/OP2/OP3 (không gian 4 tầng / quy trình 8 bước / vệ sinh) | S4; profile `_brand_architecture`; entity-map | `TOPLINK_CONFIRMED` (description) | Operational proof; real imagery; no outcome | Asset rights + (BTS) consent |
| CL-CX1 customer-experience around dưỡng liệu/products | `11_Product_Yvien.md` | `UNVERIFIED` | Customer-experience framing ONLY; no product/efficacy claim | `TL-GAP-010` fail-closed |
| CL-FD1 founder ý niệm/hành trình | narrative §3 | allowed-use gated | Journey/philosophy only; no mechanism/prescription | Consent + human (R3) |
| `CL-P2` (used on 6 P2 health items) | **not in claim register** | **ORPHAN — undefined** | intended = TL-P2 body-literacy support | See blind-audit `TL-R2-F02` |
| 7 products (máy VTV, đai từ, thảm đá, gối từ, dưỡng liệu…) | S5 §3; profile `products_7` | `UNVERIFIED` (efficacy) | Support/comfort naming only; forbidden efficacy | Product dossier `TL-GAP-004` |
| Franchise: Toplink = đơn vị nhượng quyền Nhất Liệu Y Viện | S4 line 71; S5 §2 | `PUBLIC_BRAND_RELATIONSHIP_PENDING_DOCUMENT` | Internal orientation ONLY | No public wording; `TL-GAP-002/009` |
| Legal name / giấy phép / phạm vi | S4 line 54; S5 §2 | `LEGAL_SCOPE_PENDING` / `MISSING_INPUT` | None public | `TL-GAP-009` |
| Facebook Page = primary channel | S1 §4; S3; profile `channels` | `TOPLINK_CONFIRMED` (policy) | Page primary; Reels support | Official Page URL/ID `MISSING_INPUT` |
| Tick xanh (verified badge) | S2 TL-D01 | `PLATFORM_IDENTITY_SIGNAL` | Identity signal only | Never quality/legal/efficacy proof |
| Page ID 61591880797654; follower 0; greenfield | S2 TL-D12; TL-GAP-001 | `USER_CONFIRMED_IDENTITY` | Baseline identity | Awareness = `NO_MEASUREMENT`; dated snapshot optional |
| Hà Nội service lane / national awareness-only | S2 §7, TL-D08 | `TOPLINK_CONFIRMED` (boundary) | Hà Nội service; national education only | No national-service inference |
| Zalo/phone/Maps/Website conversion role | S5 §4; profile `channels.pending_input` | `PENDING_INPUT` | Held out of runtime | Verify identity/flow |
| Content start date | S6 `TL-GAP-006-START-DATE` | `TOPLINK_CONFIRMED` (decision: UNSET) | Relative D-1..D-28 only | No hard date until `TL-M6` |
| Capacity ~3 vids/wk, ≥7 items/wk, ≥1/day | S6 `TL-GAP-006-CAPACITY` | `TOPLINK_CONFIRMED` (human decision) | Drives 12 Reels + 16 static/28 | Detailed team roles `MISSING_INPUT` |
| Asset rights uncleared → direction B placeholder | S6 `TL-M5-ASSET-RIGHTS-001` | `TOPLINK_CONFIRMED` (bounded B) | Placeholder briefs only | Rights clearance (Q9 deferred) |
| Source-lock direction A (Milestones = status owner) | S6 `TL-SOURCE-LOCK-STATUS-001` | `TOPLINK_CONFIRMED` (cleared) | No master-plan/source rebaseline | — |
| Google Sheet target | S2 §18 / TL-D14 | `BLOCKED_TARGET_INPUT` (write) | No write | `SheetTargetApproval` + read-back `TL-GAP-008` |
| `TL-D16` (cited franchise-internal authority) | **not in S2 register (D01–D15)** | **undefined ID** | semantic = TL-D04 franchise-internal | See `TL-R2-F01` |

## 3. Fail-closed inventory (kept blocked; artifacts correctly did not assert)

Public franchise/legal wording · product efficacy · price/availability/booking · staff qualification ·
outcome/testimonial without consent · asset rights · official Page URL/ID · Sheet write · national
service · measured awareness · any `HUMAN_APPROVED`/`PUBLISHED` state. No Thảo Tây fact/target/
credential/baseline imported (S3/S5 isolation held).
