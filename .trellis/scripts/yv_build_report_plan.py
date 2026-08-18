#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generator thuần cho lớp người của workbook Y Viện.

Đọc registry `docs/system/yvien-sheet-dataset-registry.json` + các tệp markdown canonical,
sinh `staging/yv-humanize/report-plan.json`.

Ràng buộc:
  * Hàm thuần: không mạng, không ghi ngoài `--output`, không đọc biến môi trường, không đọc đồng hồ.
  * Chạy hai lần liên tiếp phải cho `content_hash` giống hệt (YV-V23).
  * Không nâng trạng thái, không bịa nội dung: mọi ô đều đến từ markdown hoặc từ registry.

Chế độ:
  --check   in bảng đối chiếu header markdown vs header registry, không ghi tệp
  (mặc định) sinh plan và ghi ra --output
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- hằng số

MACHINE_COLUMNS = ("Mã", "Chủ sở hữu")
YELLOW_PREFIX = "CHƯA CHỐT — "
FALLBACK_PREFIX = "DỰ PHÒNG — "
OPTION_SEPARATOR = " · "
HIDDEN_HEADERS = ("_key", "_audit")
FORMULA_LEADERS = ("+", "=", "-", "@")
ALLOWED_CTA = ("theo dõi page", "lưu bài", "lưu", "chia sẻ")

TABLE_SEP = re.compile(r"^\|\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
OPTION_HEAD = re.compile(r"^([ABC])\s*:\s*(.+)$", re.DOTALL)


class BuildError(RuntimeError):
    """Fail closed: dừng ngay, không degrade im lặng."""


# ---------------------------------------------------------------- markdown


def _split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def parse_markdown_tables(text: str) -> list[dict]:
    """Trả về danh sách bảng: {'header': [...], 'rows': [[...], ...], 'line': n}."""
    lines = text.splitlines()
    tables: list[dict] = []
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|") and i + 1 < len(lines) and TABLE_SEP.match(lines[i + 1].strip()):
            header = _split_row(lines[i])
            rows: list[list[str]] = []
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                cells = _split_row(lines[j])
                if len(cells) < len(header):
                    cells = cells + [""] * (len(header) - len(cells))
                elif len(cells) > len(header):
                    raise BuildError(
                        "Dòng có %d ô nhưng header có %d ô: %s" % (len(cells), len(header), lines[j][:120])
                    )
                rows.append(cells)
                j += 1
            tables.append({"header": header, "rows": rows, "line": i + 1})
            i = j
        else:
            i += 1
    return tables


def data_tables(text: str) -> list[dict]:
    """Chỉ giữ bảng dữ liệu: header có cột `Mã` và có ít nhất một dòng dữ liệu."""
    return [t for t in parse_markdown_tables(text) if t["header"] and t["header"][0] == "Mã" and t["rows"]]


# ---------------------------------------------------------------- registry


def load_registry(repo: Path) -> dict:
    path = repo / "docs" / "system" / "yvien-sheet-dataset-registry.json"
    return json.loads(path.read_text(encoding="utf-8"))


def display_headers(block: dict) -> list[str]:
    return [c["header"] for c in sorted(block["display_columns"], key=lambda c: c["pos"])]


def tab_specs(registry: dict) -> list[dict]:
    """Chuẩn hoá 21 tab thành danh sách khối cần dựng.

    Tab thường: một khối. Tab `report`: ba khối section A/B/C.
    """
    specs = []
    for tab in sorted(registry["tabs"], key=lambda t: t["index"]):
        base = {
            "tab": tab["tab"],
            "index": tab["index"],
            "grid_width": tab["grid_width"],
            "hidden_columns": tab["hidden_columns"],
            "source_markdown": tab.get("source_markdown", []),
            "id_exposure": tab.get("id_exposure"),
            "id_exposure_scope": tab.get("id_exposure_scope", []),
            "visible_id_allowed": tab.get("visible_id_allowed"),
            "generated_columns": tab.get("generated_columns", []),
            "expected_yellow_count": tab.get("expected_yellow_count"),
            "evidence_status": tab["default_evidence_status"],
            "allowed_use": tab["default_allowed_use"],
            "merge_discriminator": tab.get("merge_discriminator"),
        }
        if "sections" in tab:
            for sec in tab["sections"]:
                spec = dict(base)
                spec.update(
                    {
                        "section": sec["section_id"],
                        "heading": sec.get("heading"),
                        "headers": display_headers(sec),
                        "min_records": sec.get("min_records"),
                        "max_records": sec.get("max_records"),
                        "derived": sec.get("derived", False),
                        "visible_column_count": tab.get("visible_column_count"),
                        "section_padding": tab.get("section_padding"),
                    }
                )
                specs.append(spec)
        else:
            spec = dict(base)
            spec.update(
                {
                    "section": None,
                    "heading": None,
                    "headers": display_headers(tab),
                    "min_records": tab.get("min_records"),
                    "max_records": tab.get("max_records"),
                    "derived": False,
                    "visible_column_count": len(display_headers(tab)),
                    "section_padding": None,
                }
            )
            specs.append(spec)
    return specs


def spec_label(spec: dict) -> str:
    return spec["tab"] + ("" if spec["section"] is None else " §" + spec["section"])


# ---------------------------------------------------------------- tiện ích


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def column_letter(index_zero_based: int) -> str:
    n = index_zero_based + 1
    out = ""
    while n:
        n, rem = divmod(n - 1, 26)
        out = chr(65 + rem) + out
    return out


def canonical_hash(values: list[list[str]]) -> str:
    return sha256_text(json.dumps(values, ensure_ascii=False, separators=(",", ":")))


def escape_formula(cell: str) -> str:
    """Sheets hiểu nhầm ô mở đầu bằng + = - @ là công thức. Viết lại thành chữ (YV-V17)."""
    if cell and cell[0] in FORMULA_LEADERS:
        return "'" + cell
    return cell


# ---------------------------------------------------------------- chọn bảng


def candidate_tables(repo: Path, spec: dict) -> list[tuple[str, dict]]:
    found: list[tuple[str, dict]] = []
    for rel in spec["source_markdown"]:
        path = repo / rel
        if not path.exists():
            raise BuildError("%s: thiếu tệp nguồn %s" % (spec_label(spec), rel))
        found.extend((rel, t) for t in data_tables(path.read_text(encoding="utf-8")))
    return found


def expected_markdown_headers(spec: dict) -> set[str]:
    """Header markdown mong đợi = header hiển thị, trừ cột do trình biên dịch sinh."""
    generated = {g["header"] for g in spec["generated_columns"]}
    return {h for h in spec["headers"] if h not in generated}


def select_table(repo: Path, spec: dict, override_headers: set[str] | None = None) -> tuple[str, dict]:
    """Chọn đúng một bảng bằng cách khớp trọn bộ tên cột. Không khớp hoặc khớp nhiều = dừng."""
    expected = override_headers if override_headers is not None else expected_markdown_headers(spec)
    exposed = set(spec["id_exposure_scope"])
    matches = []
    for rel, table in candidate_tables(repo, spec):
        actual = {h for h in table["header"] if h not in MACHINE_COLUMNS or h in exposed}
        if actual == expected:
            matches.append((rel, table))
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise BuildError(
            "%s: không bảng markdown nào khớp trọn bộ cột %s"
            % (spec_label(spec), sorted(expected))
        )
    raise BuildError(
        "%s: %d bảng cùng khớp bộ cột — nguồn mơ hồ, phải tách tệp"
        % (spec_label(spec), len(matches))
    )


def row_dicts(rel: str, table: dict) -> list[dict]:
    """Mỗi dòng markdown thành dict kèm vị trí nguồn."""
    out = []
    for offset, row in enumerate(table["rows"]):
        cells = dict(zip(table["header"], row))
        if not cells.get("Mã"):
            raise BuildError("%s:%d thiếu cột Mã" % (rel, table["line"] + 2 + offset))
        cells["__source_path"] = rel
        cells["__source_location"] = "L%d" % (table["line"] + 2 + offset)
        out.append(cells)
    return out


# ---------------------------------------------------------------- dựng dòng


def build_audit(registry: dict, spec: dict, cells: dict, digest: str) -> str:
    key = cells["Mã"]
    parts = [
        "%s:%s" % (spec["tab"], key),
        "%s#%s" % (cells["__source_path"], cells["__source_location"]),
        key,
        spec["evidence_status"],
        spec["allowed_use"],
        registry["schema_version"],
        digest,
        cells.get("Chủ sở hữu") or "—",
        registry["created_at_ict"],
    ]
    return " · ".join(parts)


def emit_rows(registry: dict, spec: dict, records: list[dict], digests: dict[str, str]) -> list[list[str]]:
    """records: list dict đã mang đủ header hiển thị + `Mã` + `Chủ sở hữu` + `__source_*`."""
    generated = {g["header"] for g in spec["generated_columns"]}
    values: list[list[str]] = []
    for ordinal, cells in enumerate(records, start=1):
        row: list[str] = []
        for header in spec["headers"]:
            if header in generated:
                row.append(str(ordinal))
                continue
            if header not in cells:
                raise BuildError("%s: dòng %s thiếu cột %r" % (spec_label(spec), cells["Mã"], header))
            value = cells[header]
            row.append(escape_formula(value if value else "—"))
        digest = digests.setdefault(cells["__source_path"], "")
        row.append(cells["Mã"])
        row.append(build_audit(registry, spec, cells, digest))
        values.append(row)
    return values


# ---------------------------------------------------------------- nổ dòng


def sentence_case(text: str) -> str:
    """Ô người đọc mở đầu bằng chữ hoa; phần còn lại giữ nguyên (giữ tên riêng, giữ mã)."""
    return text[:1].upper() + text[1:] if text else text


def split_options(raw: str, day_label: str) -> list[tuple[str, str]]:
    """Tách chuỗi `A: … · B: … · C: …` thành ba cặp (hướng, nội dung). Fail closed."""
    parts = [p.strip() for p in raw.split(OPTION_SEPARATOR) if p.strip()]
    if len(parts) != 3:
        raise BuildError(
            "%s: tách được %d hướng thay vì 3. Chuỗi gốc: %r" % (day_label, len(parts), raw)
        )
    out: list[tuple[str, str]] = []
    for want, part in zip("ABC", parts):
        match = OPTION_HEAD.match(part)
        if not match:
            raise BuildError("%s: option %r không mở đầu bằng %s:" % (day_label, part, want))
        letter, body = match.group(1), match.group(2).strip()
        if letter != want:
            raise BuildError("%s: thứ tự hướng sai, gặp %s ở vị trí %s" % (day_label, letter, want))
        if not body:
            raise BuildError("%s: hướng %s rỗng" % (day_label, want))
        out.append((letter, body))
    bodies = [b for _, b in out]
    if len(set(bodies)) != 3:
        raise BuildError("%s: ba hướng trùng nội dung — cấm nhân bản A = B = C" % day_label)
    return out


def calendar_records(repo: Path, registry: dict, spec: dict) -> list[dict]:
    """Nổ 28 dòng lịch thành 84 dòng A/B/C."""
    md_headers = expected_markdown_headers(spec) - {"Hướng", "Nói gì"} | {"Ba hướng A / B / C", "Angle chính"}
    rel, table = select_table(repo, spec, override_headers=md_headers)
    records: list[dict] = []
    for cells in row_dicts(rel, table):
        day = cells["Ngày"]
        for letter, body in split_options(cells["Ba hướng A / B / C"], "%s %s" % (spec["tab"], day)):
            row = dict(cells)
            row["Hướng"] = letter
            row["Nói gì"] = sentence_case(body) if letter == "A" else FALLBACK_PREFIX + body
            row["Mã"] = "%s-%s" % (cells["Mã"], letter)
            row["__option_body"] = body
            records.append(row)
    return records


# ---------------------------------------------------------------- tab dẫn xuất


# workflow-approval-measurement.md:67 — tuyến duyệt ghép theo thành phần, không tra bảng cứng.
REVIEWER_BY_LEG = {
    "R1": "Phụ trách truyền thông",
    "R2": "rà cơ chế video",
    "R3": "người có chuyên môn",
}

# workflow-approval-measurement.md:75 — luật có thứ tự: sức khoẻ trước, founder, rồi quanh sản phẩm.
HEALTH_PILLARS = ("Hiểu và lắng nghe tín hiệu cơ thể", "Lý – Dược – Dưỡng dễ hiểu")
FOUNDER_PILLAR = "Hành trình Y Viện, founder và cộng đồng"
PRODUCT_ADJACENT_DAYS = ("D-14", "D-26")  # workflow-approval-measurement.md:100
FOUNDER_DAYS = ("D-5", "D-20", "D-24", "D-28")  # workflow-approval-measurement.md:102

# workflow-approval-measurement.md:115-117
FUNNEL_METRIC = {
    "TOFU": "Chỉ số tiếp cận và tỷ lệ xem hết Reel",
    "MOFU": "Lượt lưu, lượt chia sẻ và số câu hỏi về quy trình",
}

DMP_CHECK_VALUE = (
    "Đạt 7 trên 8 chiều; bỏ qua chiều chấm điểm nhanh vì bộ chấm nhanh đã được thay bằng một lượt "
    "quét xác định, nên điểm của nó không còn ý nghĩa so sánh"
)

CONDITION_BY_RISK = {
    "health": (
        "Cần người có chuyên môn rà từng bài, và câu miễn trừ phải nằm ngay trong phần mô tả của "
        "chính bài đó vì nơi đặt câu miễn trừ chưa chốt"
    ),
    "founder": (
        "Chặn tới khi có đồng ý bằng văn bản và phạm vi được nói của founder; chưa có đồng ý thì cắt "
        "hết phần con người, chỉ giữ không gian và đồ hoạ"
    ),
    "product-adjacent": (
        "Chỉ kể ở mức trải nghiệm khách hàng; cấm mọi câu về công dụng vì hồ sơ sản phẩm chưa kiểm chứng"
    ),
    "none": (
        "Giữ nguyên câu ranh giới của dòng; lời kêu gọi không vượt quá theo dõi Page, lưu bài, chia sẻ"
    ),
}

FALLBACK_CONDITION = (
    FALLBACK_PREFIX
    + "chưa có brief sản xuất, chưa có brief Reel, chưa có tài sản. Muốn chạy hướng này thì phải viết "
    "brief trước, và nó đi lại đúng tuyến duyệt của hướng A cùng ngày"
)


def reviewer_of(route: str, row_key: str) -> str:
    legs = route.split("+")
    for leg in legs:
        if leg not in REVIEWER_BY_LEG:
            raise BuildError("YV_12: tuyến duyệt lạ %r ở dòng %s" % (route, row_key))
    return ", ".join(REVIEWER_BY_LEG[leg] for leg in legs)


def risk_of(cells: dict) -> str:
    pillar = cells.get("Trụ nội dung", "")
    if pillar in HEALTH_PILLARS:
        return "health"
    if pillar == FOUNDER_PILLAR:
        return "founder"
    if cells.get("Ngày") in PRODUCT_ADJACENT_DAYS:
        return "product-adjacent"
    return "none"


def workflow_records(calendar: list[dict], repo: Path, spec: dict) -> list[dict]:
    """`YV_12` dẫn xuất từ 84 dòng đã nổ của `YV_09` theo luật ở workflow-approval-measurement.md §3."""
    records: list[dict] = []
    for cells in calendar:
        route = cells["Tuyến duyệt"]
        letter = cells["Hướng"]
        risk = risk_of(cells)
        funnel = cells["Vai trò phễu"]
        if funnel not in FUNNEL_METRIC:
            raise BuildError("YV_12: vai trò phễu lạ %r ở dòng %s" % (funnel, cells["Mã"]))
        if letter == "A":
            consent = "CHƯA CÓ ĐỒNG Ý" if cells["Ngày"] in FOUNDER_DAYS else "Không cần"
        else:
            consent = "—"
        condition = CONDITION_BY_RISK[risk] if letter == "A" else FALLBACK_CONDITION
        # Mức rủi ro lấy mức chặt hơn là sức khoẻ, nhưng ranh giới quanh sản phẩm không được rơi mất.
        if letter == "A" and cells["Ngày"] in PRODUCT_ADJACENT_DAYS and risk != "product-adjacent":
            condition = condition + ". " + CONDITION_BY_RISK["product-adjacent"]
        row = {
            "Mã": cells["Mã"].replace("-CAL-", "-WF-"),
            "Chu kỳ": cells["Chu kỳ"],
            "Ngày": cells["Ngày"],
            "Hướng": letter,
            "Người duyệt": reviewer_of(route, cells["Mã"]),
            "Kết luận": cells["Trạng thái duyệt"],
            "Điều kiện kèm theo": condition,
            "Hết hạn (ICT)": "—",
            "Trạng thái đăng": "NOT_PUBLISHED",
            "Bản sửa": cells["Bản sửa"],
            "Sửa lớn có reset không": "Có",
            "Tuyến duyệt": route,
            "Mức rủi ro": risk,
            "DMP check": DMP_CHECK_VALUE,
            "Trạng thái đồng ý": consent,
            "Giờ đăng": "—",
            "Tham chiếu đo": FUNNEL_METRIC[funnel],
            "Ghi chú reset": "Đổi câu claim, đổi lời kêu gọi, đổi người xuất hiện, đổi kết luận sức khoẻ",
            "Câu claim": cells["Câu claim dùng"],
            "Chủ sở hữu": cells.get("Chủ sở hữu", "—"),
            "__source_path": cells["__source_path"],
            "__source_location": cells["__source_location"],
        }
        records.append(row)
    return records


def brief_records(repo: Path, registry: dict, spec: dict, calendar: list[dict]) -> list[dict]:
    """`YV_10` = 28 brief thật của hướng A + 56 dòng dự phòng ghi rõ chưa có brief (sửa lỗi mô hình #6)."""
    briefs: dict[str, dict] = {}
    md_headers = expected_markdown_headers(spec)
    for rel in spec["source_markdown"]:
        path = repo / rel
        for table in data_tables(path.read_text(encoding="utf-8")):
            actual = {h for h in table["header"] if h not in MACHINE_COLUMNS}
            if actual != md_headers:
                continue
            for cells in row_dicts(rel, table):
                day = cells["Ngày"]
                if day in briefs:
                    raise BuildError("YV_10: hai brief cùng ngày %s" % day)
                briefs[day] = cells

    records: list[dict] = []
    for cells in calendar:
        day = cells["Ngày"]
        if day not in briefs:
            raise BuildError("YV_10: ngày %s không có brief cho hướng A" % day)
        if cells["Hướng"] == "A":
            records.append(briefs[day])
            continue
        records.append(
            {
                # Dòng dự phòng nối vào đúng họ mã của brief hướng A cùng ngày, không mở họ mã mới.
                "Mã": "%s-%s" % (briefs[day]["Mã"], cells["Hướng"]),
                "Chu kỳ": cells["Chu kỳ"],
                "Ngày": day,
                "Hướng": cells["Hướng"],
                "Loại brief": "Reel" if cells["Định dạng"] == "Reel" else "Bài",
                "Định dạng": cells["Định dạng"],
                "Hook": FALLBACK_PREFIX + cells["__option_body"],
                "Hình ảnh / shot": "—",
                "Chữ trên hình": "—",
                "Thời lượng": "—",
                "Tỷ lệ khung": "—",
                "Lời thoại": "—",
                "Phụ đề": "—",
                "Vùng an toàn": "—",
                "Kêu gọi": cells["Kêu gọi"],
                "Câu claim dùng": cells["Câu claim dùng"],
                "Chỉ số theo dõi": "—",
                "Tiếp cận": "—",
                "Rủi ro / cổng": (
                    "Chưa có brief nên chưa soát được rủi ro; hướng này đi lại đúng tuyến duyệt của "
                    "hướng A cùng ngày"
                ),
                "Trạng thái sản xuất": "CHƯA CÓ BRIEF",
                "Chủ sở hữu": cells.get("Chủ sở hữu", "—"),
                "__source_path": cells["__source_path"],
                "__source_location": cells["__source_location"],
            }
        )
    return records


def report_section_b_records(calendar: list[dict]) -> list[dict]:
    """Bảng B của `report` là bản đọc của `YV_09`, không phải nguồn thứ hai."""
    records: list[dict] = []
    for cells in calendar:
        letter = cells["Hướng"]
        cta = cells["Kêu gọi"]
        if not any(token in cta.lower() for token in ALLOWED_CTA):
            raise BuildError("report §B: lời kêu gọi ngoài phạm vi cho phép: %r" % cta)
        if letter == "A":
            why = cells["Angle chính"]
        else:
            why = FALLBACK_PREFIX + "hướng thay thế cho %s; đổi lại là chưa có brief và chưa có tư liệu" % (
                cells["Angle chính"]
            )
        records.append(
            {
                "Mã": cells["Mã"].replace("-CAL-", "-RPT-"),
                "Ngày": cells["Ngày"],
                "Hướng": letter,
                "Trụ nội dung": cells["Trụ nội dung"],
                "Định dạng": cells["Định dạng"],
                "Nói gì": cells["Nói gì"],
                "Vì sao chọn / đánh đổi": why,
                "Kêu gọi": cta,
                "Ai duyệt": cells["Tuyến duyệt"],
                "Trạng thái": cells["Trạng thái duyệt"],
                "Chủ sở hữu": cells.get("Chủ sở hữu", "—"),
                "__source_path": cells["__source_path"],
                "__source_location": cells["__source_location"],
            }
        )
    return records


# ---------------------------------------------------------------- tab tự sinh


SOURCE_CATEGORY = {
    "docs Toplink/brand": "Thương hiệu",
    "docs Toplink/research": "Nghiên cứu",
    "docs Toplink/content": "Nội dung",
    "docs Toplink/system": "Hệ thống",
    "docs/system": "Hợp đồng kỹ thuật",
}

SENSITIVE_HINTS = ("compliance", "reels", "production", "asset", "owner-decisions", "input-gaps")


def source_inventory_records(repo: Path, registry: dict) -> list[dict]:
    """`01_SOURCE_INVENTORY` sinh từ registry + digest thật của tệp trên đĩa."""
    seen: dict[str, None] = {}
    for tab in sorted(registry["tabs"], key=lambda t: t["index"]):
        for rel in tab.get("source_markdown", []) + tab.get("derives_from_markdown", []):
            seen.setdefault(rel, None)
    for rel in (
        "docs/system/yvien-sheet-dataset-registry.json",
        "docs/system/yvien-sheet-human-layer-spec.md",
        "docs/system/yvien-brand-voice-pack.md",
    ):
        seen.setdefault(rel, None)

    records: list[dict] = []
    for ordinal, rel in enumerate(sorted(seen), start=1):
        path = repo / rel
        if not path.exists():
            raise BuildError("01_SOURCE_INVENTORY: registry trỏ tới tệp không tồn tại %s" % rel)
        folder = "/".join(rel.split("/")[:2])
        sensitive = any(hint in rel for hint in SENSITIVE_HINTS)
        records.append(
            {
                "Mã": "SRC-%02d" % ordinal,
                "Tệp nguồn": rel,
                "Nhóm": SOURCE_CATEGORY.get(folder, "Khác"),
                "Mức nhạy cảm": "Cần cổng người" if sensitive else "Thường",
                "Trạng thái": "Đang dùng",
                "Lý do loại trừ": "—",
                "SHA-256": sha256_file(path),
                "Chủ sở hữu": "Codex",
                "__source_path": rel,
                "__source_location": "L1",
            }
        )
    return records


def output_index_records(repo: Path, registry: dict, tab_of_source: dict[str, list[str]]) -> list[dict]:
    """`03_OUTPUT_INDEX` phủ hết artifact, 0 orphan (YV-V10)."""
    records: list[dict] = []
    for ordinal, rel in enumerate(sorted(tab_of_source), start=1):
        path = repo / rel
        records.append(
            {
                "Mã": "OUT-%02d" % ordinal,
                "Sản phẩm": path.name,
                "Đường dẫn": rel,
                "Tab hiển thị": ", ".join(sorted(tab_of_source[rel])),
                "Trạng thái QA nội bộ": "LOCAL_VERIFIED",
                "Trạng thái đưa lên Sheet": "CHƯA GHI",
                "Trạng thái đọc lại": "CHƯA ĐỌC LẠI",
                "Digest": sha256_file(path),
                "Chủ sở hữu": "Codex",
                "__source_path": rel,
                "__source_location": "L1",
            }
        )
    return records


# ---------------------------------------------------------------- ô vàng


def yellow_cells(spec: dict, values: list[list[str]], first_data_row: int) -> list[str]:
    cells = []
    for r, row in enumerate(values):
        for c, cell in enumerate(row[: len(spec["headers"])]):
            if cell.startswith(YELLOW_PREFIX):
                cells.append("%s%d" % (column_letter(c), first_data_row + r))
    return cells


# ---------------------------------------------------------------- dựng plan


def build_block(repo: Path, registry: dict, spec: dict, state: dict) -> dict:
    tab = spec["tab"]
    digests = state["digests"]

    if tab == "YV_09_content_calendar":
        records = calendar_records(repo, registry, spec)
        state["calendar"] = records
    elif tab == "YV_10_production_briefs":
        if "calendar" not in state:
            raise BuildError("YV_10 dựng trước YV_09 — sai thứ tự index")
        records = brief_records(repo, registry, spec, state["calendar"])
    elif tab == "YV_12_workflow_approval":
        if "calendar" not in state:
            raise BuildError("YV_12 dựng trước YV_09 — sai thứ tự index")
        records = workflow_records(state["calendar"], repo, spec)
    elif tab == "report" and spec["section"] == "B":
        if "calendar" not in state:
            raise BuildError("report §B dựng trước YV_09 — phải hoãn tới lượt hai")
        records = report_section_b_records(state["calendar"])
    elif tab == "01_SOURCE_INVENTORY":
        records = source_inventory_records(repo, registry)
    elif tab == "03_OUTPUT_INDEX":
        records = output_index_records(repo, registry, state["tab_of_source"])
    else:
        rel, table = select_table(repo, spec)
        records = row_dicts(rel, table)

    for cells in records:
        path = repo / cells["__source_path"]
        if cells["__source_path"] not in digests and path.exists():
            digests[cells["__source_path"]] = sha256_file(path)
    for cells in records:
        cells.setdefault("Chủ sở hữu", "—")

    values = emit_rows(registry, spec, records, digests)

    lo, hi = spec["min_records"], spec["max_records"]
    if lo is not None and not (lo <= len(values) <= hi):
        raise BuildError(
            "%s: %d dòng, ngoài khoảng [%d, %d] (YV-V11)" % (spec_label(spec), len(values), lo, hi)
        )

    keys = [row[-2] for row in values]
    if len(set(keys)) != len(keys):
        dup = sorted({k for k in keys if keys.count(k) > 1})
        raise BuildError("%s: _key trùng %s (YV-V15)" % (spec_label(spec), dup))

    return {"spec": spec, "values": values, "records": records}


def assemble_tab(registry: dict, tab_name: str, blocks: list[dict]) -> dict:
    reg_tab = next(t for t in registry["tabs"] if t["tab"] == tab_name)
    width = reg_tab["grid_width"]
    visible = reg_tab.get("visible_column_count", width - 2)
    label = registry["display_label_map"]["tab_title"][tab_name]

    header: list[str] = []
    legend: list[str] = []
    body: list[list[str]] = []
    yellow: list[str] = []
    sections: list[dict] = []

    multi = len(blocks) > 1
    row_cursor = 3  # hàng 1 header, hàng 2 legend

    if not multi:
        spec = blocks[0]["spec"]
        header = spec["headers"] + list(HIDDEN_HEADERS)
        legend = [legend_text(reg_tab)] + [""] * (width - 1)
        for row in blocks[0]["values"]:
            body.append(pad_row(row, spec, width))
        yellow = yellow_cells(spec, blocks[0]["values"], 3)
    else:
        header = ["Mục"] + [""] * (visible - 1) + list(HIDDEN_HEADERS)
        legend = [legend_text(reg_tab)] + [""] * (width - 1)
        for block in blocks:
            spec = block["spec"]
            body.append(pad_cells([spec["heading"] or ("Bảng " + spec["section"])], width))
            row_cursor += 1
            body.append(pad_cells(spec["headers"], width))
            row_cursor += 1
            start = row_cursor
            for row in block["values"]:
                body.append(pad_row(row, spec, width))
            row_cursor += len(block["values"])
            yellow.extend(yellow_cells(spec, block["values"], start))
            sections.append(
                {
                    "section_id": spec["section"],
                    "heading": spec["heading"],
                    "header_row": start - 1,
                    "first_data_row": start,
                    "row_count": len(block["values"]),
                }
            )
            body.append(pad_cells([], width))
            row_cursor += 1
        if body and all(cell == "" for cell in body[-1]):
            body.pop()

    values = [header, legend] + body
    for row in values:
        if len(row) != width:
            raise BuildError("%s: dòng rộng %d, cần %d" % (tab_name, len(row), width))

    expected_yellow = reg_tab.get("expected_yellow_count")
    if expected_yellow is not None and len(yellow) != expected_yellow:
        raise BuildError(
            "%s: %d ô vàng, registry khai %d (YV-V05)" % (tab_name, len(yellow), expected_yellow)
        )

    last_col = column_letter(width - 1)
    plan = {
        "tab": tab_name,
        "index": reg_tab["index"],
        "title_display": label,
        "grid_width": width,
        "visible_column_count": visible,
        "row_count": len(values),
        "column_count": width,
        "used_range": "'%s'!A1:%s%d" % (tab_name, last_col, len(values)),
        "header_row": 1,
        "legend_row": 2,
        "first_data_row": 3,
        "hidden_columns": reg_tab["hidden_columns"],
        "hidden_column_letters": [column_letter(width - 2), column_letter(width - 1)],
        "evidence_status": reg_tab["default_evidence_status"],
        "allowed_use": reg_tab["default_allowed_use"],
        "yellow_cells": yellow,
        "expected_yellow_count": len(yellow),
        "values": values,
        "content_hash": canonical_hash(values),
    }
    if sections:
        plan["sections"] = sections
    return plan


def legend_text(reg_tab: dict) -> str:
    if reg_tab.get("expected_yellow_count") == 0:
        return (
            "Chú giải — tab này không có ô vàng. Việc còn treo nằm ở tab Y Viện cần chốt. "
            "Hai cột cuối là cột máy, đã ẩn."
        )
    return (
        "Chú giải — ô nền vàng nghĩa là còn một việc của người thật chưa làm; nội dung ô mở đầu "
        "bằng CHƯA CHỐT và nêu rõ ai chốt điều gì. Dòng mở đầu bằng DỰ PHÒNG là hướng thay thế, "
        "không bao giờ vàng. Hai cột cuối là cột máy, đã ẩn."
    )


def pad_cells(cells: list[str], width: int) -> list[str]:
    return list(cells) + [""] * (width - len(cells))


def pad_row(row: list[str], spec: dict, width: int) -> list[str]:
    """Giữ hai cột máy luôn ở hai vị trí cuối; phần đệm giữa là chuỗi rỗng thật."""
    visible = row[: len(spec["headers"])]
    machine = row[-2:]
    pad = width - 2 - len(visible)
    if pad < 0:
        raise BuildError("%s: cột hiển thị vượt chiều rộng lưới" % spec_label(spec))
    return visible + [""] * pad + machine


# ---------------------------------------------------------------- kiểm tra chéo


def cross_checks(registry: dict, plans: list[dict], state: dict) -> list[str]:
    notes: list[str] = []
    by_tab = {p["tab"]: p for p in plans}

    total_yellow = sum(p["expected_yellow_count"] for p in plans)
    notes.append("tổng ô vàng: %d" % total_yellow)

    banned = ("record_id", "stable_row_key", "source_digest", "revision")
    hex16 = re.compile(r"\b[0-9a-f]{16,}\b")
    for plan in plans:
        reg_tab = next(t for t in registry["tabs"] if t["tab"] == plan["tab"])
        if reg_tab.get("id_exposure") != "CONTENT_TAB":
            continue
        allowed = reg_tab.get("visible_id_allowed", "")
        patterns = [p.replace("*", "") for p in allowed.split("|")] if allowed else []
        for r, row in enumerate(plan["values"][2:], start=3):
            for c, cell in enumerate(row[:-2]):
                if hex16.search(cell):
                    raise BuildError("%s!%s%d: lộ chuỗi hex dài (YV-V04)" % (plan["tab"], column_letter(c), r))
                for token in banned:
                    if token in cell:
                        raise BuildError(
                            "%s!%s%d: lộ tên trường máy %r (YV-V04)" % (plan["tab"], column_letter(c), r, token)
                        )
                for match in re.finditer(r"\b(?:TL|YV)-[A-Z0-9]", cell):
                    if not any(cell[match.start():].startswith(p) for p in patterns):
                        raise BuildError(
                            "%s!%s%d: lộ mã kỹ thuật %r (YV-V04)"
                            % (plan["tab"], column_letter(c), r, cell[match.start(): match.start() + 12])
                        )

    for plan in plans:
        for row in plan["values"]:
            for cell in row:
                if cell[:1] in FORMULA_LEADERS and not cell.startswith("'"):
                    raise BuildError("%s: ô mở đầu bằng ký tự công thức: %r (YV-V17)" % (plan["tab"], cell[:40]))

    calendar = by_tab.get("YV_09_content_calendar")
    if calendar:
        cycles = {row[0] for row in calendar["values"][2:]}
        expected = 84 * len(cycles)
        actual = len(calendar["values"]) - 2
        if actual != expected:
            raise BuildError("YV_09: %d dòng, cần 84 × %d chu kỳ (YV-V13)" % (actual, len(cycles)))
        notes.append("YV_09: %d dòng, %d chu kỳ" % (actual, len(cycles)))

    pillars = by_tab.get("YV_05_content_pillars")
    if pillars:
        rows = pillars["values"][2:]
        weights = [int(row[2]) for row in rows]
        if len(rows) != 5 or sum(weights) != 100:
            raise BuildError("YV_05: %d dòng, tổng tỷ trọng %d (YV-V12)" % (len(rows), sum(weights)))
        slots = [int(row[1]) for row in rows]
        if sum(slots) != 28:
            raise BuildError("YV_05: tổng số ngày trong chu kỳ = %d, cần 28" % sum(slots))
        notes.append("YV_05: 5 trụ, tổng 100%, 28 ngày")

    claim_tab = by_tab.get("06_COMPLIANCE_RULES")
    if claim_tab:
        known = {row[1] for row in claim_tab["values"][2:] if row[1].startswith("CL-")}
        used: set[str] = set()
        for tab_name in ("YV_09_content_calendar", "YV_12_workflow_approval", "YV_10_production_briefs"):
            plan = by_tab.get(tab_name)
            if not plan:
                continue
            for row in plan["values"][2:]:
                for cell in row[:-2]:
                    used.update(re.findall(r"\bCL-[A-Z0-9]+\b", cell))
        orphan = sorted(used - known)
        if orphan:
            raise BuildError("YV-V09: mã claim mồ côi %s" % orphan)
        notes.append("YV-V09: %d mã claim dùng, %d mã khai báo, 0 mồ côi" % (len(used), len(known)))

    decisions = by_tab.get("00_Y_VIEN_CAN_CHOT")
    if decisions:
        open_rows = [row for row in decisions["values"][2:] if row[8] == "OPEN"]
        if len(open_rows) != decisions["expected_yellow_count"]:
            raise BuildError(
                "00_Y_VIEN_CAN_CHOT: %d dòng OPEN nhưng %d ô vàng (YV-V05)"
                % (len(open_rows), decisions["expected_yellow_count"])
            )
        notes.append("00_Y_VIEN_CAN_CHOT: %d dòng OPEN = %d ô vàng" % (len(open_rows), len(open_rows)))

    for plan in plans:
        for row in plan["values"][2:]:
            for cell in row[:-2]:
                if cell.startswith(FALLBACK_PREFIX) and cell.startswith(YELLOW_PREFIX):
                    raise BuildError("%s: dòng dự phòng bị tô vàng (YV-V07)" % plan["tab"])

    return notes


# ---------------------------------------------------------------- check mode


DERIVED_BLOCKS = {
    ("YV_09_content_calendar", None): "nổ 28 ngày thành 84 hướng A/B/C",
    ("YV_10_production_briefs", None): "ghép 2 tệp brief + 56 dòng dự phòng",
    ("YV_12_workflow_approval", None): "dẫn xuất từ YV_09 theo bảng luật §3",
    ("report", "B"): "dẫn xuất từ YV_09 theo bảng luật §4",
}


def run_check(repo: Path, registry: dict) -> int:
    problems = 0
    for spec in tab_specs(registry):
        label = spec_label(spec)
        derived = DERIVED_BLOCKS.get((spec["tab"], spec["section"]))
        if derived:
            print("[skip] %-42s dẫn xuất — %s" % (label, derived))
            continue
        if not spec["source_markdown"]:
            print("[skip] %-42s tab tự sinh, không đọc markdown" % label)
            continue
        expected = expected_markdown_headers(spec)
        exposed = set(spec["id_exposure_scope"])
        found = candidate_tables(repo, spec)
        matches = 0
        for rel, table in found:
            actual = [h for h in table["header"] if h not in MACHINE_COLUMNS or h in exposed]
            missing = [h for h in expected if h not in actual]
            extra = [h for h in actual if h not in expected]
            if not missing and not extra:
                matches += 1
                print("        OK   %s:%d rows=%-4d cols=%d" % (rel, table["line"], len(table["rows"]), len(actual)))
        if matches != 1:
            problems += 1
            print("[FAIL] %-42s %d bảng khớp trọn bộ cột (cần đúng 1)" % (label, matches))
            for rel, table in found:
                actual = [h for h in table["header"] if h not in MACHINE_COLUMNS or h in exposed]
                print(
                    "        cand %s:%d thiếu=%s thừa=%s"
                    % (
                        rel,
                        table["line"],
                        [h for h in expected if h not in actual],
                        [h for h in actual if h not in expected],
                    )
                )
        else:
            print("[ok  ] %-42s" % label)
    return problems


# ---------------------------------------------------------------- build


def build_plan(repo: Path, registry: dict) -> dict:
    specs = tab_specs(registry)
    state: dict = {"digests": {}, "tab_of_source": {}}

    for spec in specs:
        for rel in spec["source_markdown"]:
            state["tab_of_source"].setdefault(rel, set()).add(spec["tab"])

    order = [s for s in specs if s["tab"] != "report"] + [s for s in specs if s["tab"] == "report"]
    blocks: dict[str, list[dict]] = {}
    for spec in order:
        blocks.setdefault(spec["tab"], []).append(build_block(repo, registry, spec, state))

    for tab_name in blocks:
        blocks[tab_name].sort(key=lambda b: b["spec"].get("section") or "")

    plans = [
        assemble_tab(registry, tab["tab"], blocks[tab["tab"]])
        for tab in sorted(registry["tabs"], key=lambda t: t["index"])
    ]

    notes = cross_checks(registry, plans, state)

    workbook_hash = sha256_text(
        json.dumps([p["content_hash"] for p in plans], ensure_ascii=False, separators=(",", ":"))
    )
    return {
        "plan_id": "YV-REPORT-PLAN-001",
        "schema_version": registry["schema_version"],
        "registry_id": registry["registry_id"],
        "generated_from": "docs/system/yvien-sheet-dataset-registry.json",
        "state": "DRAFT_UNSIGNED · LOCAL_ONLY",
        "write_executed": False,
        "external_writes": 0,
        "spreadsheet_target": registry["spreadsheet_target"],
        "formatting": registry["formatting"],
        "palette": registry["palette"],
        "hidden_column_contract": registry["hidden_column_contract"],
        "tab_count": len(plans),
        "total_yellow_cells": sum(p["expected_yellow_count"] for p in plans),
        "source_digests": dict(sorted(state["digests"].items())),
        "notes": notes,
        "tabs": plans,
        "workbook_content_hash": workbook_hash,
    }


# ---------------------------------------------------------------- main


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", required=True)
    ap.add_argument("--output", default="staging/yv-humanize/report-plan.json")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)

    repo = Path(args.repo_root)
    registry = load_registry(repo)

    if args.check:
        return 1 if run_check(repo, registry) else 0

    try:
        plan = build_plan(repo, registry)
    except BuildError as exc:
        print("BUILD_FAILED: %s" % exc, file=sys.stderr)
        return 3

    out = Path(args.output)
    if not out.is_absolute():
        out = repo / out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("plan: %s" % out)
    print("tab: %d · ô vàng: %d" % (plan["tab_count"], plan["total_yellow_cells"]))
    for note in plan["notes"]:
        print("  - %s" % note)
    print("workbook_content_hash: %s" % plan["workbook_content_hash"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
