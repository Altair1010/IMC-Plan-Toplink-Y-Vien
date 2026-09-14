import importlib.util
import re
import sys
import unicodedata
import unittest
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS_DIR))


class WorkbookPlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.find_spec("ktd_migration")
        if spec is None:
            raise AssertionError("ktd_migration runtime is not implemented")
        cls.module = importlib.util.module_from_spec(spec)
        assert spec.loader
        spec.loader.exec_module(cls.module)

    def test_builds_exact_human_first_workbook(self):
        """Catches a missing, extra, or legacy active sheet in the target plan."""
        spec = importlib.util.find_spec("ktd_migration")
        self.assertIsNotNone(spec, "ktd_migration runtime is not implemented")

        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)
        plan = module.build_workbook_plan()

        self.assertEqual(
            [sheet["title"] for sheet in plan["sheets"]],
            [
                "YV_01_BRAND",
                "YV_02_AUDIENCE_PAGE",
                "YV_03_CONTENT_SYSTEM",
                "YV_04_CAMPAIGN_CALENDAR",
                "_CONTROL_PLANE",
            ],
        )
        self.assertEqual(plan["language"], "vi")
        self.assertTrue(all(sheet["rows"] for sheet in plan["sheets"]))

    def test_plan_passes_structural_and_human_surface_validation(self):
        validate = getattr(self.module, "validate_workbook_plan", None)
        self.assertIsNotNone(validate, "workbook validator is not implemented")
        self.assertEqual(validate(self.module.build_workbook_plan()), [])

    def test_validator_rejects_machine_metadata_on_human_surface(self):
        validate = getattr(self.module, "validate_workbook_plan", None)
        self.assertIsNotNone(validate, "workbook validator is not implemented")
        plan = self.module.build_workbook_plan()
        plan["sheets"][0]["rows"][4][0] = "_key"
        errors = validate(plan)
        self.assertTrue(any("machine metadata" in error for error in errors))

    def test_control_plane_nodes_resolve_uniquely(self):
        resolve = getattr(self.module, "resolve_node", None)
        self.assertIsNotNone(resolve, "control-plane resolver is not implemented")
        row = resolve(self.module.build_workbook_plan(), "ktd.content.status")
        self.assertEqual(row["sheet"], "YV_04_CAMPAIGN_CALENDAR")
        self.assertEqual(row["binding"], "header:Trạng thái")

    def test_machine_write_is_denied_for_human_canonical_fields(self):
        allowed = getattr(self.module, "machine_write_allowed", None)
        self.assertIsNotNone(allowed, "authority guard is not implemented")
        plan = self.module.build_workbook_plan()
        self.assertFalse(allowed(plan, "ktd.content.status"))
        self.assertTrue(allowed(plan, "ktd.view.pending_evidence"))

    def test_runtime_context_contains_only_current_target_contract(self):
        build_context = getattr(self.module, "build_runtime_context", None)
        self.assertIsNotNone(build_context, "runtime context builder is not implemented")
        context = build_context(self.module.build_workbook_plan())
        self.assertEqual(context["brand_name"], "KHIẾT TÂM ĐƯỜNG")
        self.assertEqual(context["business_phase"], "DRY_RUN")
        self.assertEqual(context["human_sheets"], list(self.module.HUMAN_SHEETS))
        self.assertNotIn("archived_context", context)
        self.assertNotIn("reviewer", context)
        self.assertNotIn("legal_pending", context)
        self.assertNotIn("YV_08_experiments", repr(context))

    def test_plan_fingerprint_is_stable_and_changes_with_content(self):
        fingerprint = getattr(self.module, "plan_fingerprint", None)
        self.assertIsNotNone(fingerprint, "plan fingerprint is not implemented")
        first = self.module.build_workbook_plan()
        second = self.module.build_workbook_plan()
        self.assertEqual(fingerprint(first), fingerprint(second))
        second["sheets"][0]["rows"][5][1] = "CHANGED"
        self.assertNotEqual(fingerprint(first), fingerprint(second))

    def test_cell_text_is_nfc_and_cannot_be_interpreted_as_formula(self):
        plan = self.module.build_workbook_plan()
        values = [str(value) for sheet in plan["sheets"] for row in sheet["rows"] for value in row]
        self.assertTrue(all(value == unicodedata.normalize("NFC", value) for value in values))
        self.assertFalse(any(value.startswith(("=", "+", "-", "@")) for value in values if value))

    def test_plan_contains_no_obvious_secret_material(self):
        payload = repr(self.module.build_workbook_plan())
        patterns = [r"AIza[0-9A-Za-z_-]{30,}", r"ghp_[0-9A-Za-z]{20,}", r"-----BEGIN .*PRIVATE KEY-----"]
        self.assertFalse(any(re.search(pattern, payload) for pattern in patterns))


if __name__ == "__main__":
    unittest.main()
