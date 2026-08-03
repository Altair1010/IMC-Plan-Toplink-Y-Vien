# TL-M2 — DMP profile & brand architecture (Toplink Y Viện)

> **Run 1 Phase A · local-only · `external_writes=0`.** Non-canonical staging-of-record for the DMP
> brand entity. Formalizes the already-repaired profile (`TL-M2-PROFILE-REPAIR-001`, APPROVED
> 2026-07-30); it does **not** re-derive or mutate `profile.json`. Logical Sheet dataset:
> `TL_BRAND_PROFILE` (no write until a signed `SheetTargetApproval`).

## 0. Document control

| Field | Value |
|---|---|
| Milestone | `TL-M2` |
| Stable ID | `TL-BRAND-PROFILE-001` |
| DMP version | `3.15.1` |
| Active brand read-back | `toplink-y-vien` (`_active-brand.json`, `active_slug=toplink-y-vien`) |
| Profile path | `C:/Users/MCBAu/.claude-marketing/brands/toplink-y-vien/profile.json` |
| `profile_digest` (G5 LOCK) | `a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349` |
| `source_digest` (G5 LOCK) | `3ba91761612ca482471dc1c071bd7e9d82e5708a3bb13ceb630fed476541fe76` |
| Digest verified this run | Profile MATCH · 5/5 sources MATCH (`00-input-lock.json`) |
| Guidelines | 5 categories / 52 rules (`guidelines/_manifest.json`) |
| Slug uniqueness | 1 slug only; **no** `toplink-page` profile created |
| External writes | `0` |
| Milestone advanced | `false` (LOCAL only; not COMPLETE/APPROVED) |

## 1. Slug & runtime read-back (VERIFY 1–2)

- Single DMP brand entity: `toplink-y-vien`. No second entity for the same brand; no `toplink-page`.
- Active-brand read-back = `toplink-y-vien` (verified before authoring; matches `TL-M1-DMP-SWITCH-001`).
- No secret, credential, source-code, tech-stack, or local machine path stored in the profile
  (`_m2_verification.no_secret`). Website/Zalo/phone/Maps kept out of the conversion runtime.

## 2. Field-layer map — core / profile / guideline / staging-only

Layer legend: **CORE** = identity/runtime fields DMP reads for every generation · **PROFILE** = brand
architecture context (`_brand_architecture`, franchise-internal) · **GUIDELINE** = `guidelines/**`
(52 rules) · **STAGING-ONLY** = evidence lives in `docs Toplink/`, never forced into runtime.

| Section | Subsection | Item ID | Content (from `profile.json`) | Evidence/source | Assumption status | Owner | Review status | Layer |
|---|---|---|---|---|---|---|---|---|
| Identity | brand_name | TL-BP-01 | Toplink Y Viện | profile `brand_name`; brief §Foundation | `TOPLINK_CONFIRMED` | DMP core | LOCKED | CORE |
| Identity | tagline | TL-BP-02 | Y Viện Dưỡng Thân – Tỉnh Thức | profile `identity.tagline`; brief §Foundation | `TOPLINK_CONFIRMED` | DMP core | LOCKED | CORE |
| Identity | positioning_statement | TL-BP-03 | Không gian chăm sóc sức khỏe kết hợp Đông y dưỡng sinh + lý liệu + công nghệ cao | profile `identity.positioning_statement` | `HYPOTHESIS` (not public-approved) | DMP core | HYPOTHESIS | CORE |
| Industry | primary + regulated | TL-BP-04 | Chăm sóc sức khỏe chủ động; `regulated=true`; code `health-claim-compliance` | profile `industry` | `TOPLINK_CONFIRMED` | DMP core | LOCKED | CORE |
| Industry | compliance disclaimer | TL-BP-05 | Verbatim disclaimer "…không thay thế chẩn đoán, điều trị…" + nhóm chống chỉ định | profile `industry.compliance_notes`; taxonomy §3 | `TOPLINK_CONFIRMED` (as policy) | Health gate | MANDATORY | CORE+GUIDELINE |
| Channels | primary | TL-BP-06 | Facebook Page (primary); Reels = discovery support | profile `channels`; RULES §Channel | `TOPLINK_CONFIRMED` | DMP core | LOCKED | CORE |
| Channels | pending_input | TL-BP-07 | Zalo / phone / Google Maps = `PENDING_INPUT` | profile `channels.pending_input`; entity-map §4 | `PENDING_INPUT` | Open gate | HELD | CORE |
| Goals | primary_objective | TL-BP-08 | Trust-led FB Page từ 0; Toplink độc lập — 0 tham chiếu thương hiệu bên ngoài | profile `goals.primary_objective` | `TOPLINK_CONFIRMED` | DMP core | LOCKED | CORE |
| Goals | kpis | TL-BP-09 | `[]` (empty; defined at TL-M4, greenfield) | profile `goals.kpis` | `MISSING_INPUT` (by design) | DMP core | DEFERRED→M4 | CORE |
| Business | price_range | TL-BP-10 | `UNVERIFIED` — source thiếu giá/bảo hành | profile `business_model.price_range` | `UNVERIFIED` | Open gate | HELD | CORE |
| Voice | brand_voice scores | TL-BP-11 | formality 6 · energy 3 · humor 2 · authority 6 | profile `brand_voice` | `TOPLINK_CONFIRMED` | Guidelines | LOCKED | GUIDELINE |
| Voice | avoid/prefer words | TL-BP-12 | avoid: "chữa khỏi/điều trị dứt điểm/thay thế thuốc…"; prefer: "hỗ trợ…" | profile `brand_voice`; taxonomy §1–2 | `TOPLINK_CONFIRMED` | Guidelines | LOCKED | GUIDELINE |
| Architecture | three_pillars | TL-BP-13 | Lý liệu · Dược liệu · Dưỡng liệu | profile `_brand_architecture.three_pillars`; `01` §2 | `TOPLINK_CONFIRMED` | Profile ctx | LOCKED | PROFILE |
| Architecture | services 3-tier / 12 | TL-BP-14 | basic/advanced/intensive (12 dịch vụ) | profile `_brand_architecture.services_3_tier` | `TOPLINK_CONFIRMED` (naming) | Profile ctx | LOCKED | PROFILE |
| Architecture | products 7 | TL-BP-15 | 4 lý liệu + 3 dưỡng liệu; efficacy `UNVERIFIED` | profile `_brand_architecture.products_7`; entity-map §3 | `UNVERIFIED` (efficacy) | Health gate | HELD | PROFILE |
| Architecture | space 4 floors | TL-BP-16 | Tĩnh/Thông/Dưỡng/Tỉnh — tài sản không gian mạnh nhất | profile `_brand_architecture.space_4_floors` | `TOPLINK_CONFIRMED` | Profile ctx | LOCKED | PROFILE |
| Architecture | process 8 steps | TL-BP-17 | Tiếp nhận→…→Hẹn lịch | profile `_brand_architecture.process_8_steps` | `TOPLINK_CONFIRMED` | Profile ctx | LOCKED | PROFILE |
| Architecture | visual tokens | TL-BP-18 | #FFFCF7/#D8AA4B/#F7E8C2/#1A1410; Be Vietnam Pro/Noto Sans; reduced-motion | profile `_brand_architecture.visual_tokens`; brief §Visual | `TOPLINK_CONFIRMED` | Guidelines | LOCKED | GUIDELINE |
| Franchise | `_franchise_internal` | TL-BP-19 | Parent Nhất Liệu Y Viện; `FRANCHISOR_PARENT (INTERNAL_ONLY)`; public `PENDING_DOCUMENT` | profile `_franchise_internal`; entity-map §2; TL-D04/D16 | `PUBLIC_BRAND_RELATIONSHIP_PENDING_DOCUMENT` | Legal gate | LOCKED-INTERNAL | PROFILE |
| Competitors | competitors | TL-BP-20 | `[]` (empty — Toplink độc lập) | profile `competitors` | `TOPLINK_CONFIRMED` | DMP core | LOCKED | CORE |
| Evidence | dossier/consent | TL-BP-21 | Giá/bảo hành/chứng nhận pháp lý/spec/case-study consent = `MISSING_INPUT` | profile `_m2_verification.missing_input` | `MISSING_INPUT` | Open gate | HELD | STAGING-ONLY |

## 3. Founder allowed-use & restrictions map (VERIFY 3)

- Corporate voice = default. Founder appears selectively; public role only
  `Founder/điều hành Toplink Y Viện` per current evidence (master plan §10 founder guardrail).
- Founder must **not** explain mechanism, indicate/prescribe products, diagnose, or speak for a
  professional. Cross-post to personal Facebook = separate external action + item-level approval.
- Restrictions (`guidelines/restrictions.md`, 18 rules) enforce the forbidden catalogue
  (taxonomy §2) and the mandatory disclaimer (taxonomy §3). No unsupported field forced into runtime.

## 4. Digest lock confirmation (VERIFY 4) — `TL_BRAND_PROFILE` anchor

`docs Toplink/staging/run1/00-input-lock.json` re-verified this run:

```text
profile_digest = a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349   [MATCH]
source_digest  = 3ba91761612ca482471dc1c071bd7e9d82e5708a3bb13ceb630fed476541fe76   [locked]
  spec.md                                    aa8465ea…  [MATCH]
  TOPLINK_PAGE_MASTER_PLAN.md                aa923b51…  [MATCH]
  RULES.md                                   96c1bb4c…  [MATCH]
  Ho-so…2026.md                              645b1ad2…  [MATCH]
  entity-franchise-allowed-use-map.md        56618b18…  [MATCH]
```

Digests are deterministic and locked for both Run 1 and Run 2. Any drift = `FAIL_BACK_TO_RUN1`.

## 5. VERIFY checklist (TL-M2)

- [x] One slug only; active read-back `toplink-y-vien`; no `toplink-page`.
- [x] No secret / local path / private analytics in profile or this file.
- [x] No unsupported field forced into runtime (Website/Zalo/phone/Maps held `PENDING_INPUT`;
      price/products efficacy held `UNVERIFIED`/`MISSING_INPUT`).
- [x] Digests deterministic + G5-locked (profile + 5 sources MATCH).
- [ ] Runtime/Sheet exact read-back — **DEFERRED** (Sheet write gated; `external_writes=0`).

## 6. Sheet column shape (logical only — `TL_BRAND_PROFILE`)

`Section | Subsection | Item ID | Content | Evidence/source | Assumption status | Owner | Review status | Last updated`.
Stable identity = `TL-BRAND-PROFILE-001` → one tab. No write; hold `LOCAL_VERIFIED · SYNC_PENDING_TARGET`.
