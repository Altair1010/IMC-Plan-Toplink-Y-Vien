# Phiếu sửa hồ sơ DMP — TL-M2 profile repair spec (Toplink Y Viện)

> **Trạng thái:** `APPROVED · 2026-07-30` — user đã ký §6. Đây là bounded-action approval cho một lần
> sửa hồ sơ DMP local; §5 được phép chạy đúng phạm vi đã duyệt.

## 0. Document control

| Trường | Giá trị |
|---|---|
| Spec ID | `TL-M2-PROFILE-REPAIR-001` |
| Version | `0.1.1` |
| Ngày | 2026-07-30 |
| Runtime thực thi | Claude Code (DMP owner) |
| Đối tượng sửa | DMP local profile `toplink-y-vien` (`C:\Users\MCBAu\.claude-marketing\brands\toplink-y-vien\profile.json`) |
| Gỡ blocker | `TL-GAP-011` (profile drift) → mở đường DMP trace cho TL-M1 |
| External writes | `0` (profile là DMP runtime local, **không** phải Sheet/Page/publish) |
| Milestone advance | `KHÔNG` — sửa profile không tự PASS TL-M1/TL-M2 |

## 1. Vì sao cần sửa

Profile `toplink-y-vien` bị clone từ IMC Thảo Tây nên **drift**: kênh chính sai, mục tiêu còn "hỗ trợ
thương hiệu Thảo Tây", và `Nhất Liệu Y Viện` bị xếp `competitor` (thực ra là hệ thống mẹ/franchisor).
Mọi bước sinh deliverable của TL-M1 cần DMP trace thật, nhưng skill `import-guidelines`/`brand-setup`
mutate profile và **không có dry-run** → hiện fail-closed. Sửa profile là điều kiện gỡ.

### Tension thứ tự (ghi rõ, có chủ đích)

Repair này dán nhãn **TL-M2** (profile là deliverable của TL-M2), nhưng TL-M2 "depends on TL-M1 local
evidence PASS", còn TL-M1 DMP-trace lại bị chặn bởi drift. Cách giải: chạy repair **sớm** để unblock,
sau đó TL-M1 chạy DMP có trace → TL-M1 local PASS → TL-M2 formalize. Không tạo Run 3; vẫn trong Run 1.

## 2. Nguồn cho giá trị target (chỉ dùng nguồn thật)

- Kênh/mục tiêu/geo: `spec.md §4`, `docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md §5–§6`, `RULES.md`.
- Brand facts (name/tagline/industry/voice): hồ sơ thương hiệu `docs Toplink/Ho-so-thuong-hieu-Y-Vien-Toplink-Cai-tien-2026.md`.
- Quan hệ entity/franchise: `staging/toplink-reconciled/TL-M1-evidence/entity-franchise-allowed-use-map.md` (`TL-D04`).
- **Cấm:** bịa field, hoặc lấy bất kỳ giá trị/goal/identifier nào từ Thảo Tây.

## 3. Bảng sửa field-by-field

| Field | Current (drift) | Target | Nguồn | Gate |
|---|---|---|---|---|
| `primary_channel` | `Website` | `Facebook Page` | `spec.md §4`, `RULES.md` | G2 |
| `active_channels` | `["Website"]` | `["Facebook Page"]` (Reels = discovery support) | `spec.md §4` | G2 |
| `primary_goal` | `"…củng cố uy tín cho thương hiệu cá nhân Thảo Tây (supporting brand)."` | Goal Toplink **độc lập**: xây Facebook Page trust-led từ 0, chăm sóc sức khỏe chủ động; **0 tham chiếu Thảo Tây/supporting** | master plan §5 | G2, G4 |
| `competitor_count` | `1` | `0` | entity map §2 (`TL-D04`) | G3 |
| `competitor_names` | `["Nhất Liệu Y Viện"]` | `[]` | entity map §2 | G3 |
| Quan hệ `Nhất Liệu Y Viện` | (ẩn trong competitor) | Ghi INTERNAL = hệ thống mẹ/franchisor; **public = `PENDING_DOCUMENT`**, không assert trong field công khai | entity map §2, `TL-GAP-002` | G3 |
| `brand_name` | `Toplink Y Viện` | **VERIFY** với dossier frontmatter (full = "Nhất Liệu Y Viện Toplink"); giữ short nếu dossier cho phép | dossier | G2 (verify, không tự đổi ẩu) |
| `tagline` | `Y Viện Dưỡng Thân – Tỉnh Thức` | GIỮ | dossier | — |
| `industry_primary` | (đã đúng) | GIỮ | dossier | — |
| `voice` (formality/energy/humor/authority/traits) | (đã đúng) | GIỮ | dossier §voice | — |
| `business_model_type` / `revenue_model` | (đã đúng) | GIỮ | dossier | — |
| `industry_regulated` / `regulation_codes` | `true` / `["health-claim-compliance"]` | GIỮ | RULES health | — |
| `kpis` | `[]` | GIỮ trống (khóa ở TL-M4) | — | — |
| `active_channels` phụ (Zalo/phone/Maps) | — | `PENDING_INPUT`, không thêm làm active | master plan §11 | G2 |

## 4. Gates (bắt buộc, hiển thị rõ)

| Gate | Nội dung | Điều kiện PASS |
|---|---|---|
| **G1 — Authorization tier** | Sửa profile là mutation runtime local, cần user approval tier (`AGENTS.md`) | User ký approval payload §6 |
| **G2 — Source-only** | Mọi target từ dossier/canonical; không bịa; không lấy từ Thảo Tây | Mỗi field target trỏ đúng nguồn §2 |
| **G3 — Franchise public gated** | Reclassify competitor→franchisor **chỉ INTERNAL**; public franchise wording khóa | Không field công khai nào assert quan hệ; `TL-GAP-002` vẫn open |
| **G4 — Cross-brand isolation** | Sau repair, profile có **0** tham chiếu Thảo Tây (goal/channel/identifier) | `rg`/read-back = 0 match "Thảo Tây"/"supporting brand" |
| **G5 — Digest lock** | Tính `profile_digest` + `source_digest`, khóa cho two-run | Digest ghi vào staging run1 input-lock |
| **G6 — Read-back** | `switch-brand`+`status` xác nhận từng field target | Checklist §5 pass toàn bộ |
| **G7 — No advance / no external** | Không PASS milestone; `external_writes=0`; không Sheet/Page | Khẳng định trong trace + STATE |

## 5. Trình tự thực thi DMP + read-back (bước gated kế tiếp)

**Chỉ chạy sau khi user duyệt §6.**

1. **Backup** `profile.json` → `staging/toplink-reconciled/TL-M2-profile/backup/profile.<ISO>.json` (rollback point).
2. `import-guidelines` — load hồ sơ Toplink từ `docs Toplink/` vào profile guidelines (không kéo dữ liệu Thảo Tây).
3. `brand-setup` — set các field target ở §3. **Caveat:** nếu skill không cho field-level và muốn re-derive
   quá phạm vi, dừng và dùng controlled minimal correction đúng bounded field (vẫn qua cơ chế đã duyệt), không mở rộng.
4. `switch-brand toplink-y-vien` → `status --json` read-back.
5. Ghi **real-trace**: `trace_id · timestamp · DMP_version · active_brand_readback · skill · exact_input_paths ·
   input_digest · invocation_mode · output_path · output_digest · status · skipped_dimensions`.
6. Tính `profile_digest`+`source_digest`; khóa vào `docs Toplink/staging/run1/00-input-lock.json`.

### Read-back checklist (VERIFY)

- [ ] `active_brand` = `toplink-y-vien`.
- [ ] `primary_channel` = `Facebook Page`; `active_channels` = `["Facebook Page"]`.
- [ ] `primary_goal` **không** chứa "Thảo Tây" / "supporting brand"; nêu goal Toplink độc lập.
- [ ] `competitor_count` = `0`; `competitor_names` = `[]`.
- [ ] Không secret/private path/analytics lọt vào profile công khai.
- [ ] `industry_regulated=true` giữ nguyên.
- [ ] `profile_digest`+`source_digest` deterministic, đã khóa.
- [ ] `external_writes=0`; không milestone nào chuyển COMPLETE/PASS.

## 6. Approval payload (user ký)

~~~text
spec_id: TL-M2-PROFILE-REPAIR-001
authorized_agent: Claude Code (DMP owner)
action: LOCAL_DMP_PROFILE_FIELD_REPAIR (một lần)
bounded_fields: [primary_channel, active_channels, primary_goal, competitor_count, competitor_names,
                 relationship_note(internal), brand_name(verify-only)]
source: docs Toplink dossier + canonical (spec.md, master plan, RULES.md); NO Thảo Tây source
forbidden: external write, Sheet, Page mutation, publishing, milestone advance, invent brand/legal fact
rollback: restore profile.json từ backup nếu read-back fail
expires_at_ict: 2026-08-06T23:59+07:00
user_signature: APPROVED 2026-07-30 (minhkhang.guru@gmail.com — cấp quyền chạy §5)
~~~

## 7. Rollback

Nếu bất kỳ mục read-back §5 fail: `restore profile.json` từ backup §5.1, set `TL-GAP-011` giữ `BLOCKED`,
ghi lỗi + owner + unblock condition, **không** retry mở rộng phạm vi. Dừng sau lần fail thứ hai (RULES).

## 8. Sau khi repair PASS

- `TL-GAP-011` → `RESOLVED` (drift cleared).
- TL-M1 có thể chạy DMP thật (`import-guidelines`+`brand-setup`) để lấy trace → TL-M1 local evidence PASS.
- TL-M2 formalize profile/digest. Vẫn cần two-run + human gate + (khi có) Sheet read-back để đóng package.
