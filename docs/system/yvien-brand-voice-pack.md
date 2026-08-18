# Y Viện — Brand voice pack (workbook `YV_*`)

- **ID:** `YV-VOICE-001`
- **Version:** 0.1.1
- **State:** `APPROVED` (người dùng duyệt 2026-08-05 ICT, bản 0.1.0)
- **Sửa sau duyệt:** 0.1.1 — §6 đổi "không quá ~140 ký tự" thành ngắm 140 · chặn cứng 210, kèm lý do.
  Chỉ nới một ngưỡng lint, không đổi từ cấm, không đổi xưng hô, không đổi bảng màu, không đổi ranh giới
  nguồn. Nếu người duyệt muốn giữ 140 làm ngưỡng cứng thì 27 ô vàng phải viết lại ngắn hơn.
- **Owner gate:** người dùng. Không nội dung `YV_*` nào được viết theo bộ này trước khi có duyệt.
- **Scope:** ngôn từ hiển thị của 21 tab workbook (`report`, `00_Y_VIEN_CAN_CHOT`, `00_CONTROL`…`06_COMPLIANCE_RULES`, `YV_01`…`YV_12`) và của 14 markdown canonical sau khi viết lại.
- **Nguồn:** repo `F:\Codex\Yvien Hotlink Website` (giọng · xưng hô · ngôn ngữ an toàn · bảng màu) và repo này (`docs Toplink/brand/**` — từ vựng lõi đã `TOPLINK_CONFIRMED`).
- **external_writes:** 0 · **network_calls:** 0.

---

## 0. Ranh giới nguồn — đọc trước khi dùng

Website `Yvien Hotlink Website` là **bản demo**. Bộ này mượn từ đó **ba thứ**: giọng, bảng màu, cách xưng hô.
Không mượn **dữ kiện**. Mọi con số, địa chỉ, giá, chứng nhận, testimonial trong repo website vào workbook
chỉ được mang `evidence_status = UNVERIFIED` và `allowed_use = DO_NOT_USE` (bảng §7).

Từ vựng lõi (§4) **không** lấy từ website — lấy từ hồ sơ DMP của chính dự án này, đã `TOPLINK_CONFIRMED`.

---

## 1. Xưng hô

| Quy tắc | Giá trị | Bằng chứng |
|---|---|---|
| Gọi khách | **`chị/anh`** (nữ trước) | `Yvien Hotlink Website/app-demo`: `chị/anh` 16 lần / 7 file (`data/content.ts` ×4, `components/BookingStepper.tsx` ×5, `app/tin-tuc/page.tsx` ×2, `app/quy-trinh-tri-lieu/page.tsx` ×2, `app/gioi-thieu/page.tsx`, `app/san-pham/page.tsx`, `app/not-found.tsx`) so với `anh/chị` 6 lần / 5 file |
| Brand tự xưng | **`Y Viện`**, ngôi thứ ba | `BookingStepper.tsx:200` "để Y Viện tư vấn liệu trình cho chị/anh"; `BodySignalInterface.tsx:35` "Y Viện lắng nghe trước khi chăm sóc" |
| `chúng tôi` | gần như không dùng — 1 lần duy nhất trong toàn bộ `app-demo` (`app/gioi-thieu/page.tsx`) | đếm bằng grep |
| `quý khách` | **cấm** — 0 lần trong `app-demo`; form khảo sát liệt kê nó như phương án bị loại | `Z-NeededUpdate/build_form.py:690-693` |
| `bạn` | **cấm** trong copy hướng khách | cùng nguồn trên |

**Áp vào workbook:** ô nội dung hướng người đọc (`report` Bảng A cột *Cách hiểu đơn giản*, ô vàng, mô tả pillar,
angle, CTA trong `YV_09`) dùng `chị/anh`. Ô mô tả nội bộ (`00_CONTROL`, `03_OUTPUT_INDEX`, cột `_audit`) viết
trung tính, không xưng hô.

---

## 2. Bốn trục giọng

Nguyên văn brief (`Yvien Hotlink Website/Z-NeededUpdate/build_form.py:687-688`):

> chuyên môn nhưng không khô · Đông y nhưng không mê tín · cao cấp nhưng không xa cách · chuyển đổi mạnh nhưng không bán hàng lộ liễu

| Trục | Làm | Không làm |
|---|---|---|
| Chuyên môn không khô | nêu cơ chế bằng lời thường ("vùng vai gáy căng vì ngồi lâu") | thuật ngữ trần trụi không giải thích |
| Đông y không mê tín | nói bằng trải nghiệm cơ thể và quy trình | huyền bí hoá, hứa hiệu quả siêu nhiên |
| Cao cấp không xa cách | câu ngắn, chăm sóc, cụ thể | trang trọng rỗng, `quý khách` |
| Chuyển đổi mạnh không lộ liễu | CTA mềm: theo dõi · lưu · nhắn Zalo · đặt lịch | `mua ngay`, `chốt đơn ngay`, đếm ngược giả |

**Chủ ngữ ưu tiên là cơ thể, không phải khách hàng.** Mẫu có sẵn trên site: *"Hôm nay cơ thể đang báo điều gì?"*
(`BodySignalInterface.tsx:32`), *"Cơ thể chị/anh đang cần gì?"* (`BookingStepper.tsx:170`).

**Nhịp câu:** câu ngắn. `—` (em dash) là dấu nối đặc trưng. `·` phân tách liệt kê ngang hàng.

---

## 3. CTA được phép theo giai đoạn

Trước khi gate offer/giá mở (`TL-GAP-*` liên quan còn treo), CTA trong `YV_09_content_calendar` chỉ được là:

```
theo dõi Page · lưu bài · chia sẻ · nhắn Zalo để được tư vấn · xem đường đến Y Viện
```

`đặt lịch` và `để Toplink tư vấn liệu trình` là CTA hợp lệ của website (`02_UI_UX_GUIDE.md:80-83`) nhưng trên
Page chỉ dùng sau khi gate offer được người duyệt. Trước đó ghi `CHƯA CHỐT — chờ mở gate offer`.

---

## 4. Từ vựng lõi (nguồn: DMP profile repo này, `TOPLINK_CONFIRMED`)

| Cụm | Nghĩa dùng trong workbook | Nguồn |
|---|---|---|
| `Tĩnh · Thông · Dưỡng · Tỉnh` | tên 4 tầng không gian — tài sản không gian mạnh nhất | `docs Toplink/brand/dmp-profile.md:55`; `docs Toplink/brand/positioning.md:32` |
| `Lý · Dược · Dưỡng` | hệ ba trụ dịch vụ. **Naming** confirmed; **efficacy** `UNVERIFIED` | `dmp-profile.md:52`; `positioning.md:34` |
| `Y Viện Dưỡng Thân – Tỉnh Thức` | tagline khoá (`LOCKED`) | `dmp-profile.md:41` |
| `Thân · Tâm · Trí` | trục cân bằng, dùng trong angle và pillar | `app-demo/data/content.ts:34`, `:152` |
| `dưỡng sinh`, `khí huyết`, `căng mỏi`, `thể trạng`, `liệu trình`, `thảo dược` | từ nền, dùng tự do | `content.ts:29`, `:706`, `:818`; `narrative.md:28` |

**Cấm mở rộng bộ này.** Thêm cụm mới = thêm một dòng `02_INPUT_GAPS` + ô vàng, không tự đặt.

---

## 5. Ngôn ngữ an toàn sức khoẻ — bắt buộc

Nên dùng (nguyên văn `Z-NeededUpdate/00_MASTER_YVIEN_TOPLINK_WEBSITE_SPEC.md:220-225`):

```
Hỗ trợ thư giãn
Hỗ trợ lưu thông khí huyết
Hỗ trợ cải thiện cảm giác căng mỏi
Góp phần cân bằng thân – tâm – trí
Không thay thế tư vấn y khoa chuyên môn
```

**Danh sách cấm (lint chặn cứng, 0 hit)** — gộp từ `00_MASTER…:229-235` và `02_UI_UX_GUIDE.md:88-93`:

```
chữa khỏi
cam kết khỏi
điều trị dứt điểm
trị dứt điểm
thay thế bác sĩ
khỏi bệnh hoàn toàn
thần dược
mua ngay
chốt đơn ngay
```

Lint không phân biệt hoa/thường và bỏ dấu câu chen giữa. Một hit = `VALIDATION_FAILED`, không cảnh báo mềm.

Mọi dòng mang claim sức khoẻ trong `YV_05`, `YV_09`, `YV_10` phải trỏ về một `CL-*` trong `06_COMPLIANCE_RULES`;
`CL-*` orphan là lỗi `TL-R2-F02` đang mở.

---

## 6. Mẫu câu ô vàng (ACTION_REQUIRED)

Hợp đồng ô vàng: mở đầu bằng `CHƯA CHỐT — `, nêu **ai** và **chốt điều gì**, một câu.

```
CHƯA CHỐT — <vai trò> cần <hành động cụ thể> trước khi <việc bị chặn>.
```

Độ dài: ngắm ~140 ký tự, **chặn cứng ở 210**. Ngưỡng cứng nằm ở 210 chứ không ở 140 vì mệnh đề
"trước khi &lt;việc bị chặn&gt;" mới là phần biến ô vàng thành việc làm được — cắt nó đi thì người đọc
biết phải chốt gì nhưng không biết chốt muộn thì hỏng cái gì. 27 ô vàng hiện tại dài 121–207 ký tự,
mỗi ô vẫn đúng một câu. Lint `test_yellow_contract` chặn ở 210; 140 chỉ là mức ngắm, không fail.

Ví dụ hợp lệ:

```
CHƯA CHỐT — chủ Y Viện chọn 1 trong 3 hướng narrative trước khi lên brief D-8.
CHƯA CHỐT — người phụ trách pháp lý duyệt câu disclaimer và nêu nơi đăng chuẩn.
CHƯA CHỐT — chủ Y Viện xác nhận số năm kinh nghiệm thật; bản demo ghi "10+" chưa có nguồn.
```

Không hợp lệ (thiếu người hoặc thiếu hành động):

```
CHƯA CHỐT — cần review.
CHƯA CHỐT — HYPOTHESIS.
Đang chờ duyệt.
```

Dòng dự phòng B/C mở đầu `DỰ PHÒNG — ` và **không tô vàng**:

```
DỰ PHÒNG — hướng thay thế nếu A không qua review; chưa có brief sản xuất.
```

Trạng thái kỹ thuật đơn thuần (`HYPOTHESIS` mà không còn việc của người) **không** đủ điều kiện tô vàng.

---

## 7. Bảng màu workbook

Nguồn: `Yvien Hotlink Website/app-demo/styles/tokens.css:10-56` (`@theme`, bản shipped).
**Không dùng `DESIGN.md`** của repo đó — đã cũ và mâu thuẫn với tokens.

| Vai trò trong sheet | Token | Hex |
|---|---|---|
| Nền bảng | `--color-ivory` | `#fffcf7` |
| Nền header / dải section | `--color-cream` | `#f6f4df` |
| Viền, đường kẻ | `--color-sand` | `#e7d6b4` |
| Chữ thường | `--color-ink` | `#1a1410` |
| Chữ phụ, ghi chú | `--color-ink-soft` | `#4a4a4a` |
| Chữ tiêu đề tab / heading | `--color-crimson-600` | `#95131f` |
| **ACTION_REQUIRED (ô vàng)** | `--color-gold-200` | `#f7e8c2` |
| Blocker / gate cứng | `--color-accent-red` | `#c70002` |
| Đã xác minh / đã chốt | `--color-jade-500` | `#2f5d50` |

Ràng buộc:

- Màu **phẳng**, không gradient, không blend (`tokens.css:6`).
- `gold-500 #d8aa4b` trên nền ivory chỉ ~2.1:1 — **FAIL WCAG**, chỉ dùng cho viền/đường kẻ, không dùng làm màu chữ (`tokens.css:34-35`). Ô vàng dùng `gold-200` làm **nền**, chữ giữ `ink`.
- Không merge cell trong vùng dữ liệu.
- Tô vàng bằng **direct format** (`repeatCell.backgroundColor`). Số conditional-format rule phải bằng 0.

Google lượng tử hoá RGB một mã (đã ghi nhận: `0.4196` gửi đi đọc về `0.41568628`). Read-back so màu phải
giữ dung sai một mã như bản vá hiện có, không nới rộng hơn.

---

## 8. Dữ kiện website = `UNVERIFIED` — không được lên mặt trước

| Dữ kiện trong repo website | Vấn đề | Trạng thái bắt buộc |
|---|---|---|
| "10+" năm đồng hành (`content.ts:574`) | dòng ngay trên là `TODO(user): xác nhận con số thật` (`content.ts:572`) | `UNVERIFIED` · `DO_NOT_USE` |
| Địa chỉ | mâu thuẫn: metadata trang chủ ghi **Hà Nội** (`app/page.tsx:16,18`) còn dữ liệu chi nhánh ghi `"123 Đường Sức Khỏe, Quận 1, TP. Hồ Chí Minh"` (`content.ts:398`) — bản thân chuỗi này cũng là placeholder | `UNVERIFIED` · `DO_NOT_USE` |
| Testimonial / review | placeholder demo | `UNVERIFIED` · `DO_NOT_USE` |
| Bảng giá, `priceFrom` | mock data (`data/content.ts:3` tự khai "Dữ liệu tĩnh để demo giao diện. Chưa kết nối database.") | `UNVERIFIED` · `DO_NOT_USE` |
| "đạt chuẩn" | không nêu chuẩn nào | `UNVERIFIED` · `DO_NOT_USE` |
| Ảnh không gian, tên dịch vụ | chưa xác minh quyền dùng | `UNVERIFIED` · gate asset rights |

Mỗi dòng trên phải có đúng một mục ở `02_INPUT_GAPS` và một ô vàng ở `00_Y_VIEN_CAN_CHOT`.

---

## 9. Lint tự chạy (P1.7)

1. Danh sách cấm §5 — 0 hit trên mọi ô hiển thị.
2. `quý khách`, `bạn` (hướng khách) — 0 hit.
3. Ô vàng: khớp `^CHƯA CHỐT — ` **và** có dòng tương ứng ở `00_Y_VIEN_CAN_CHOT`.
4. Dòng B/C: khớp `^DỰ PHÒNG — ` **và** không nằm trong `yellow_cells`.
5. Ô hiển thị không chứa ID kỹ thuật (`TL-*`, `YV-*`, `sha256`, `revision`) — trừ cột ẩn `_key`/`_audit` và các tab hệ thống được khai báo miễn trừ.
6. Ô không bắt đầu bằng `+`, `=`, `-`, `@`.
7. Dấu tiếng Việt đầy đủ (không ký tự ASCII thay thế).
8. Màu dùng trong `report-plan.json` thuộc đúng bảng §7.

---

## 10. Duyệt

| Trường | Giá trị |
|---|---|
| Người duyệt | người dùng (chủ sở hữu repo) |
| Ngày (ICT) | 2026-08-05 |
| Quyết định | `APPROVED` |
| Phạm vi duyệt | ngôn từ · xưng hô · từ vựng · danh sách cấm · mẫu ô vàng · bảng màu (§1–§9). **Không** duyệt bất kỳ dữ kiện website nào ở §8 — các dòng đó vẫn `UNVERIFIED · DO_NOT_USE`. |

Chỉ người dùng đặt `APPROVED`. `LOCAL_VERIFIED` không thay thế (`RULES.md:53`, `RULES.md:129-130`).
