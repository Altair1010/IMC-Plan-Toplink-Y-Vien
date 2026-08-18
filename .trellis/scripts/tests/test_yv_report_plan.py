# -*- coding: utf-8 -*-
"""Kiểm thử cục bộ cho lớp người của workbook Y Viện.

Chạy:  python -B -m unittest discover -s .trellis/scripts/tests -v
Không chạm mạng, không chạm Google API, `external_writes = 0`.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
import unittest
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = TESTS_DIR.parent
REPO_ROOT = SCRIPTS_DIR.parent.parent
FIXTURE_DIR = TESTS_DIR / "fixtures" / "yv"

sys.path.insert(0, str(SCRIPTS_DIR))

import yv_build_report_plan as G  # noqa: E402

FIXTURE_TABS = ("report", "YV_08_experiments", "YV_09_content_calendar")

# docs/system/yvien-brand-voice-pack.md:101-109 — lint chặn cứng, 0 hit.
FORBIDDEN_WORDS = (
    "chữa khỏi",
    "cam kết khỏi",
    "điều trị dứt điểm",
    "trị dứt điểm",
    "thay thế bác sĩ",
    "khỏi bệnh hoàn toàn",
    "thần dược",
    "mua ngay",
    "chốt đơn ngay",
)

# Lệnh cấm chi phối *lời sẽ đăng*, không chi phối cột nói về chính lệnh cấm đó.
# Cột chép lời công khai — 0 hit, không ngoại lệ.
COPY_COLUMNS = {
    "report": ("Nói gì", "Kêu gọi"),
    "YV_07_campaign": ("Kêu gọi mặc định",),
    "YV_09_content_calendar": ("Angle chính", "Nói gì", "Kêu gọi"),
    "YV_10_production_briefs": ("Hook", "Chữ trên hình", "Lời thoại", "Phụ đề", "Kêu gọi"),
    "YV_11_asset_batch_plan": ("Mô tả",),
}

# Ngoài cột chép lời, từ cấm chỉ được xuất hiện đúng ở 12 chỗ đang giữ luật, persona hoặc ranh giới.
# Danh sách đóng băng: thêm một chỗ mới là test đỏ, buộc người rà lại.
FORBIDDEN_WORD_MENTIONS = {
    ("report", "Điều đã chốt", "TL-RA-07"),
    ("06_COMPLIANCE_RULES", "Cấm nói gì", "LP-01"),
    ("06_COMPLIANCE_RULES", "Cấm nói gì", "LP-02"),
    ("06_COMPLIANCE_RULES", "Cấm nói gì", "LP-03"),
    ("YV_01_brand_profile", "Nội dung", "TL-BP-12"),
    ("YV_02_audience", "Nhóm khách", "TL-AX-01"),
    ("YV_02_audience", "Giả định về họ", "TL-AX-01"),
    ("YV_03_positioning", "Ranh giới được nói", "TL-POS-01"),
    ("YV_03_positioning", "Câu tuyên bố", "TL-POS-03"),
    ("YV_03_positioning", "Câu tuyên bố", "TL-POS-05"),
    ("YV_04_narrative", "Luật kể chuyện", "TL-NAR-10"),
    ("YV_06_page_strategy", "Vai trò", "TL-PS-15"),
}

# Chỉ người mới đặt được ba trạng thái này (RULES.md:53, RULES.md:129-130).
HUMAN_ONLY_STATUSES = ("APPROVED", "HUMAN_APPROVED", "PUBLISHED")

YELLOW_MAX_LEN = 210
ROLE_TOKENS = ("chủ Y Viện", "cổng sức khoẻ", "cổng pháp lý", "người phụ trách", "phụ trách truyền thông")

SECRET_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\"private_key\""),
    re.compile(r"\bAIza[0-9A-Za-z_\-]{20,}"),
    re.compile(r"\.secrets/"),
)


def build() -> dict:
    return G.build_plan(REPO_ROOT, G.load_registry(REPO_ROOT))


def header_for(tab: dict, row_index: int) -> list[str]:
    """Hàng tiêu đề chi phối một dòng dữ liệu. `report` xếp chồng ba bảng nên phải tra theo section."""
    if "sections" not in tab:
        return tab["values"][0]
    chosen = tab["values"][0]
    for section in tab["sections"]:
        if row_index >= section["header_row"] - 1:
            chosen = tab["values"][section["header_row"] - 1]
    return chosen


def data_rows(tab: dict):
    """Sinh (row_index_0based, header, row) cho mọi dòng dữ liệu thật, bỏ hàng tiêu đề và hàng trống."""
    for i, row in enumerate(tab["values"]):
        if i < 2:
            continue
        header = header_for(tab, i)
        if row == header or not any(cell for cell in row):
            continue
        yield i, header, row


class YvReportPlanTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.plan = build()
        cls.by_tab = {t["tab"]: t for t in cls.plan["tabs"]}
        cls.registry = G.load_registry(REPO_ROOT)

    # ------------------------------------------------------------ fixture

    def test_fixtures_match(self) -> None:
        for tab in FIXTURE_TABS:
            with self.subTest(tab=tab):
                fixture = json.loads((FIXTURE_DIR / ("%s.json" % tab)).read_text(encoding="utf-8"))
                actual = self.by_tab[tab]
                self.assertEqual(fixture["row_count"], actual["row_count"])
                self.assertEqual(fixture["column_count"], actual["column_count"])
                self.assertEqual(fixture["used_range"], actual["used_range"])
                self.assertEqual(fixture["yellow_cells"], actual["yellow_cells"])
                self.assertEqual(fixture["values"], actual["values"])
                self.assertEqual(fixture["content_hash"], actual["content_hash"])

    def test_workbook_fixture(self) -> None:
        fixture = json.loads((FIXTURE_DIR / "workbook.json").read_text(encoding="utf-8"))
        self.assertEqual(fixture["tab_count"], self.plan["tab_count"])
        self.assertEqual(fixture["total_yellow_cells"], self.plan["total_yellow_cells"])
        self.assertEqual(fixture["workbook_content_hash"], self.plan["workbook_content_hash"])
        self.assertEqual(
            fixture["tab_hashes"], {t["tab"]: t["content_hash"] for t in self.plan["tabs"]}
        )

    def test_deterministic_rebuild(self) -> None:
        """YV-V23 — hai lần chạy liên tiếp cho `content_hash` giống hệt."""
        again = build()
        self.assertEqual(self.plan["workbook_content_hash"], again["workbook_content_hash"])
        for a, b in zip(self.plan["tabs"], again["tabs"]):
            self.assertEqual(a["content_hash"], b["content_hash"], a["tab"])

    def test_plan_is_local_only(self) -> None:
        self.assertEqual(0, self.plan["external_writes"])
        self.assertFalse(self.plan["write_executed"])
        self.assertIn("LOCAL_ONLY", self.plan["state"])

    # ------------------------------------------------------------ nội dung

    def test_no_human_only_status(self) -> None:
        """Không ô nào tự đặt trạng thái chỉ người mới đặt được."""
        for tab in self.plan["tabs"]:
            for i, _, row in data_rows(tab):
                for c, cell in enumerate(row[:-2]):
                    self.assertNotIn(
                        cell.strip(),
                        HUMAN_ONLY_STATUSES,
                        "%s!%s%d tự leo thang" % (tab["tab"], G.column_letter(c), i + 1),
                    )

    def test_workflow_conclusions_stay_unapproved(self) -> None:
        tab = self.by_tab["YV_12_workflow_approval"]
        headers = tab["values"][0]
        conclusion = headers.index("Kết luận")
        publish = headers.index("Trạng thái đăng")
        counts: dict[str, int] = {}
        for _, _, row in data_rows(tab):
            counts[row[conclusion]] = counts.get(row[conclusion], 0) + 1
            self.assertEqual("NOT_PUBLISHED", row[publish])
        self.assertEqual({"DRAFT": 42, "NEEDS_HUMAN_REVIEW": 42}, counts)

    def test_confirmed_status_traces_to_source(self) -> None:
        """`TOPLINK_CONFIRMED` chỉ được đứng ở dòng mà chính file nguồn đã khai."""
        cache: dict[str, str] = {}
        for tab in self.plan["tabs"]:
            for i, _, row in data_rows(tab):
                if "TOPLINK_CONFIRMED" not in row[:-2]:
                    continue
                audit = row[-1]
                self.assertTrue(audit, "%s dòng %d thiếu _audit" % (tab["tab"], i + 1))
                source_path = audit.split(" · ")[1].split("#")[0]
                if source_path not in cache:
                    cache[source_path] = (REPO_ROOT / source_path).read_text(encoding="utf-8")
                self.assertIn(
                    "TOPLINK_CONFIRMED",
                    cache[source_path],
                    "%s dòng %d khai TOPLINK_CONFIRMED mà nguồn %s không có"
                    % (tab["tab"], i + 1, source_path),
                )

    def test_no_forbidden_words_in_copy_columns(self) -> None:
        """Lời sẽ đăng: 0 hit, không ngoại lệ (yvien-brand-voice-pack.md:98-112)."""
        for tab in self.plan["tabs"]:
            allowed = COPY_COLUMNS.get(tab["tab"])
            if not allowed:
                continue
            for i, headers, row in data_rows(tab):
                for c, cell in enumerate(row[:-2]):
                    if c >= len(headers) or headers[c] not in allowed:
                        continue
                    low = cell.lower()
                    for word in FORBIDDEN_WORDS:
                        self.assertNotIn(
                            word,
                            low,
                            "%s!%s%d là lời sẽ đăng mà chứa từ cấm %r"
                            % (tab["tab"], G.column_letter(c), i + 1, word),
                        )

    def test_forbidden_word_mentions_are_frozen(self) -> None:
        """Ngoài cột chép lời, mọi lần nhắc từ cấm phải nằm đúng danh sách đã đóng băng."""
        found = set()
        for tab in self.plan["tabs"]:
            allowed = COPY_COLUMNS.get(tab["tab"], ())
            for _, headers, row in data_rows(tab):
                for c, cell in enumerate(row[:-2]):
                    header = headers[c] if c < len(headers) else ""
                    if header in allowed:
                        continue
                    low = cell.lower()
                    if any(word in low for word in FORBIDDEN_WORDS):
                        found.add((tab["tab"], header, row[-2]))
        self.assertEqual(FORBIDDEN_WORD_MENTIONS, found)

    def test_claim_codes_resolve(self) -> None:
        rules = self.by_tab["06_COMPLIANCE_RULES"]
        known = {row[1] for row in rules["values"][2:] if row[1].startswith("CL-")}
        self.assertGreaterEqual(len(known), 10)
        used: set[str] = set()
        for tab in self.plan["tabs"]:
            if tab["tab"] == "06_COMPLIANCE_RULES":
                continue
            for row in tab["values"][2:]:
                for cell in row[:-2]:
                    used.update(re.findall(r"\bCL-[A-Z0-9]+\b", cell))
        self.assertEqual(set(), used - known, "câu claim mồ côi")

    def test_visible_cells_hide_machine_fields(self) -> None:
        banned = ("stable_row_key", "record_id", "source_digest", "evidence_status", "allowed_use")
        for tab in self.plan["tabs"]:
            for row in tab["values"][2:]:
                for cell in row[:-2]:
                    for token in banned:
                        self.assertNotIn(token, cell, tab["tab"])

    def test_no_formula_leader(self) -> None:
        """YV-V17 — ô mở đầu bằng + = - @ phải được viết lại thành chữ."""
        for tab in self.plan["tabs"]:
            for row in tab["values"]:
                for cell in row:
                    if cell[:1] in G.FORMULA_LEADERS:
                        self.fail("%s: ô %r sẽ bị Sheets hiểu thành công thức" % (tab["tab"], cell[:40]))

    # ------------------------------------------------------------ ô vàng

    def test_yellow_contract(self) -> None:
        total = 0
        for tab in self.plan["tabs"]:
            for row in tab["values"][2:]:
                for cell in row[:-2]:
                    if not cell.startswith(G.YELLOW_PREFIX):
                        continue
                    total += 1
                    self.assertLessEqual(
                        len(cell), YELLOW_MAX_LEN, "ô vàng quá dài ở %s: %r" % (tab["tab"], cell[:60])
                    )
                    self.assertTrue(
                        any(token in cell for token in ROLE_TOKENS),
                        "ô vàng không nêu vai trò ở %s: %r" % (tab["tab"], cell[:60]),
                    )
                    self.assertFalse(cell.startswith(G.FALLBACK_PREFIX))
        self.assertEqual(total, self.plan["total_yellow_cells"])
        self.assertEqual(27, total, "tổng ô vàng của workbook")

    def test_yellow_cells_match_declared_coordinates(self) -> None:
        for tab in self.plan["tabs"]:
            found = []
            offset = 3
            if "sections" in tab:
                for section in tab["sections"]:
                    for r in range(section["row_count"]):
                        row = tab["values"][section["first_data_row"] - 1 + r]
                        for c, cell in enumerate(row[:-2]):
                            if cell.startswith(G.YELLOW_PREFIX):
                                found.append("%s%d" % (G.column_letter(c), section["first_data_row"] + r))
            else:
                for r, row in enumerate(tab["values"][2:]):
                    for c, cell in enumerate(row[:-2]):
                        if cell.startswith(G.YELLOW_PREFIX):
                            found.append("%s%d" % (G.column_letter(c), offset + r))
            self.assertEqual(found, tab["yellow_cells"], tab["tab"])

    def test_fallback_rows_never_yellow(self) -> None:
        for tab in self.plan["tabs"]:
            for row in tab["values"][2:]:
                has_fallback = any(cell.startswith(G.FALLBACK_PREFIX) for cell in row[:-2])
                has_yellow = any(cell.startswith(G.YELLOW_PREFIX) for cell in row[:-2])
                self.assertFalse(has_fallback and has_yellow, tab["tab"])

    def test_open_ledger_rows_have_one_yellow_each(self) -> None:
        ledger = self.by_tab["00_Y_VIEN_CAN_CHOT"]
        headers = ledger["values"][0]
        status_col = headers.index("Trạng thái")
        open_rows = [row for row in ledger["values"][2:] if row[status_col] == "OPEN"]
        self.assertEqual(len(open_rows), ledger["expected_yellow_count"])
        for row in open_rows:
            self.assertEqual(
                1,
                sum(1 for cell in row[:-2] if cell.startswith(G.YELLOW_PREFIX)),
                "mỗi dòng OPEN đúng một ô vàng",
            )

    # ------------------------------------------------------------ hình thức

    def test_grid_shape(self) -> None:
        for tab in self.plan["tabs"]:
            width = tab["column_count"]
            self.assertEqual(["_key", "_audit"], tab["values"][0][-2:], tab["tab"])
            for row in tab["values"]:
                self.assertEqual(width, len(row), tab["tab"])
            self.assertEqual(2, len(tab["hidden_columns"]), tab["tab"])
            for hidden in tab["hidden_columns"]:
                self.assertTrue(hidden["hidden_by_user"], tab["tab"])

    def test_audit_column_has_nine_fields(self) -> None:
        for tab in self.plan["tabs"]:
            for row in tab["values"][2:]:
                audit = row[-1]
                if not audit:
                    continue
                self.assertEqual(9, len(audit.split(" · ")), "%s: %r" % (tab["tab"], audit[:80]))

    def test_vietnamese_text_is_nfc(self) -> None:
        for tab in self.plan["tabs"]:
            for row in tab["values"]:
                for cell in row:
                    self.assertEqual(unicodedata.normalize("NFC", cell), cell, tab["tab"])
                    self.assertNotIn("�", cell, tab["tab"])

    def test_no_absolute_dates_in_calendar(self) -> None:
        pattern = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
        for tab_name in ("YV_09_content_calendar", "YV_10_production_briefs", "YV_12_workflow_approval"):
            tab = self.by_tab[tab_name]
            for row in tab["values"][2:]:
                for cell in row[:-2]:
                    self.assertIsNone(pattern.search(cell), "%s: %r" % (tab_name, cell[:60]))

    def test_no_secret_material(self) -> None:
        blob = json.dumps(self.plan, ensure_ascii=False)
        for pattern in SECRET_PATTERNS:
            self.assertIsNone(pattern.search(blob), "rò rỉ bí mật: %s" % pattern.pattern)


if __name__ == "__main__":
    unittest.main()
