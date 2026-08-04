from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "toplink_sheet_sync.py"
SPEC = importlib.util.spec_from_file_location("toplink_sheet_sync", MODULE_PATH)
assert SPEC and SPEC.loader
sheet_sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sheet_sync)
REPO_ROOT = Path(__file__).resolve().parents[3]


class RegistryContractTests(unittest.TestCase):
    def test_registry_has_exact_24_operational_tabs_and_common_columns(self) -> None:
        registry = sheet_sync.load_registry(REPO_ROOT)
        self.assertEqual(registry["schema_version"], "TL-SHEET-001/0.2.0")
        self.assertEqual(set(registry["datasets"]), set(sheet_sync.TAB_KEYS))
        self.assertEqual(len(registry["datasets"]), 24)
        for schema in registry["datasets"].values():
            self.assertEqual(schema["columns"][: len(sheet_sync.COMMON_COLUMNS)], sheet_sync.COMMON_COLUMNS)
            self.assertIn(schema["primary_key"], schema["columns"])

    def test_registry_rejects_unknown_foreign_dataset(self) -> None:
        registry = copy.deepcopy(sheet_sync.load_registry(REPO_ROOT))
        registry["datasets"]["TL_CAMPAIGN"]["foreign_keys"].append(
            {"columns": ["record_id"], "dataset": "TL_UNKNOWN", "target_columns": ["record_id"]}
        )
        with self.assertRaisesRegex(sheet_sync.SyncError, "unknown foreign dataset"):
            sheet_sync.validate_registry(registry)


class DatasetValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = sheet_sync.load_registry(REPO_ROOT)
        self.bundle = sheet_sync.compile_datasets(REPO_ROOT)

    def test_rejects_duplicate_primary_key(self) -> None:
        broken = copy.deepcopy(self.bundle)
        broken["datasets"]["TL_INPUT_GAPS"]["records"].append(
            copy.deepcopy(broken["datasets"]["TL_INPUT_GAPS"]["records"][0])
        )
        with self.assertRaisesRegex(sheet_sync.SyncError, "duplicate primary key"):
            sheet_sync.validate_dataset_bundle(broken, self.registry)

    def test_rejects_orphan_foreign_key(self) -> None:
        broken = copy.deepcopy(self.bundle)
        broken["datasets"]["TL_EXPERIMENTS"]["records"][0]["campaign_item_id"] = "TL-CAMPAIGN-MISSING"
        with self.assertRaisesRegex(sheet_sync.SyncError, "orphan foreign key"):
            sheet_sync.validate_dataset_bundle(broken, self.registry)

    def test_rejects_unknown_enum_and_blank_confirmation_state(self) -> None:
        broken = copy.deepcopy(self.bundle)
        broken["datasets"]["TL_OWNER_ACTIONS"]["records"][0]["evidence_status"] = ""
        with self.assertRaisesRegex(sheet_sync.SyncError, "blank required field"):
            sheet_sync.validate_dataset_bundle(broken, self.registry)
        broken = copy.deepcopy(self.bundle)
        broken["datasets"]["TL_OWNER_ACTIONS"]["records"][0]["evidence_status"] = "CONFIRMED_BY_SHEET"
        with self.assertRaisesRegex(sheet_sync.SyncError, "unknown enum"):
            sheet_sync.validate_dataset_bundle(broken, self.registry)

    def test_rejects_prose_rows_and_section_text_dump(self) -> None:
        broken = copy.deepcopy(self.bundle)
        broken["datasets"]["TL_REPORT"]["records"][0]["record_type"] = "PROSE"
        with self.assertRaisesRegex(sheet_sync.SyncError, "prose row"):
            sheet_sync.validate_dataset_bundle(broken, self.registry)

    def test_bundle_has_24_valid_sidecars_and_14_of_14_artifact_coverage(self) -> None:
        sheet_sync.validate_dataset_bundle(self.bundle, self.registry)
        self.assertEqual(len(self.bundle["datasets"]), 24)
        output_records = self.bundle["datasets"]["TL_OUTPUT_INDEX"]["records"]
        self.assertEqual(len(output_records), 14)
        self.assertTrue(all(record["dataset_keys"] for record in output_records))
        self.assertGreaterEqual(len(self.bundle["datasets"]["TL_CONTENT_CALENDAR"]["records"]), 84)

    def test_identical_inputs_compile_to_byte_identical_bundle(self) -> None:
        first = sheet_sync.compile_datasets(REPO_ROOT)
        second = sheet_sync.compile_datasets(REPO_ROOT)
        self.assertEqual(sheet_sync.canonical_json_bytes(first), sheet_sync.canonical_json_bytes(second))
        self.assertEqual(first["bundle_sha256"], second["bundle_sha256"])

    def test_source_digest_drift_is_rejected(self) -> None:
        broken = copy.deepcopy(self.bundle)
        broken["datasets"]["TL_OUTPUT_INDEX"]["records"][0]["artifact_digest"] = "0" * 64
        with self.assertRaisesRegex(sheet_sync.SyncError, "source digest drift"):
            sheet_sync.validate_source_digests(broken, REPO_ROOT)

    def test_all_row_sources_are_in_inventory_and_dataset_digest_is_bound(self) -> None:
        inventory = {record["inventory_source_id"] for record in self.bundle["datasets"]["TL_SOURCE_INVENTORY"]["records"]}
        row_sources = {record["source_id"] for payload in self.bundle["datasets"].values() for record in payload["records"]}
        self.assertTrue(row_sources.issubset(inventory))
        broken = copy.deepcopy(self.bundle)
        broken["datasets"]["TL_REPORT"]["dataset_sha256"] = "0" * 64
        with self.assertRaisesRegex(sheet_sync.SyncError, "dataset digest mismatch"):
            sheet_sync.validate_dataset_bundle(broken, self.registry)
        broken = copy.deepcopy(self.bundle)
        broken["datasets"]["TL_CONTENT_CALENDAR"]["records"][0]["claim_ids"] = "`CL-ID1` (prose)"
        with self.assertRaisesRegex(sheet_sync.SyncError, "invalid claim reference"):
            sheet_sync.validate_dataset_bundle(broken, self.registry)

    def test_committed_sidecars_must_match_bundle_exactly(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir)
            sheet_sync.write_dataset_sidecars(self.bundle, output)
            sheet_sync.validate_dataset_sidecars(self.bundle, output)
            (output / "TL_REPORT.json").write_text("{}\n", encoding="utf-8")
            with self.assertRaisesRegex(sheet_sync.SyncError, "sidecar drift"):
                sheet_sync.validate_dataset_sidecars(self.bundle, output)

    def test_sidecars_exclude_machine_local_paths_secrets_and_cross_brand_data(self) -> None:
        serialized = sheet_sync.canonical_json_bytes(self.bundle).decode("utf-8")
        self.assertNotIn("C:/Users/", serialized)
        self.assertNotIn("private_key", serialized)
        self.assertNotIn(".secrets/", serialized)
        self.assertNotIn("Thảo Tây", serialized)


class ApprovalAndRangeSafetyTests(unittest.TestCase):
    def test_material_content_edit_resets_approval(self) -> None:
        record = {"content_hash": "a" * 64, "verdict": "APPROVED", "publish_state": "READY"}
        changed = sheet_sync.reset_approval_on_material_edit(record, "b" * 64)
        self.assertEqual(changed["verdict"], "NEEDS_HUMAN_REVIEW")
        self.assertEqual(changed["publish_state"], "BLOCKED")

    def test_bounded_replace_clears_only_union_tail(self) -> None:
        plan = sheet_sync.plan_bounded_replace("A1:F20", "A1:D12")
        self.assertEqual(plan["write_range"], "A1:D12")
        self.assertEqual(plan["clear_range"], "A1:F20")
        matrix = [[f"{row}:{col}" for col in range(8)] for row in range(25)]
        result = sheet_sync.apply_bounded_replace(matrix, plan, [["new"] * 4 for _ in range(12)])
        self.assertEqual(result[20][6], "20:6")
        self.assertEqual(result[0][0], "new")
        self.assertEqual(result[19][5], "")

    def test_rejects_one_shot_create_for_existing_tabs(self) -> None:
        with self.assertRaisesRegex(sheet_sync.SyncError, "existing tab"):
            sheet_sync.validate_create_actions(
                ["TL_REPORT", "TL_BRAND_PROFILE"], existing_titles={"TL_BRAND_PROFILE"}
            )

    def test_rejects_wrong_target_service_account_expiry_and_scope_drift(self) -> None:
        now = datetime(2026, 8, 4, 15, 0, tzinfo=timezone.utc)
        bundle = sheet_sync.example_approval_bundle(now + timedelta(hours=2))
        sheet_sync.validate_correction_approval(bundle, now=now)
        for field, value, message in (
            ("spreadsheet_id", "wrong", "wrong target"),
            ("service_account", "other@example.com", "wrong service account"),
            ("expires_at_ict", "2026-08-04T20:00:00+07:00", "approval expired"),
        ):
            broken = copy.deepcopy(bundle)
            broken[field] = value
            with self.assertRaisesRegex(sheet_sync.SyncError, message):
                sheet_sync.validate_correction_approval(broken, now=now)
        broken = copy.deepcopy(bundle)
        broken["actions"][0]["new_used_range"] = "A1:ZZ99999"
        with self.assertRaisesRegex(sheet_sync.SyncError, "scope drift"):
            sheet_sync.validate_correction_approval(broken, now=now)

    def test_recovery_bundle_always_requires_new_approval(self) -> None:
        recovery = sheet_sync.build_recovery_bundle("TL-SHEET-RUN2-CORRECTION-01", {"partial": True})
        self.assertEqual(recovery["approval_state"], "NOT_GRANTED")
        self.assertNotEqual(recovery["bundle_id"], "TL-SHEET-RUN2-CORRECTION-01")

    def test_repository_bindings_and_live_baseline_fail_closed(self) -> None:
        datasets = sheet_sync.compile_datasets(REPO_ROOT)
        snapshot = sheet_sync.read_json(
            REPO_ROOT / sheet_sync.CORRECTION_DIR / "target-snapshot.json"
        )
        correction = sheet_sync.build_correction_bundle(
            REPO_ROOT, datasets, snapshot, "2026-08-05T23:00:00+07:00"
        )
        sheet_sync.validate_repository_bindings(correction, REPO_ROOT)
        broken = copy.deepcopy(correction)
        broken["repository_bindings"]["registry_sha256"] = "0" * 64
        with self.assertRaisesRegex(sheet_sync.SyncError, "registry digest drift"):
            sheet_sync.validate_repository_bindings(broken, REPO_ROOT)

        live_values = {
            sheet["title"]: {"range": sheet.get("used_range", sheet.get("baseline_range")), "digest": sheet.get("values_digest", sheet.get("baseline_digest"))}
            for sheet in snapshot["sheets"]
            if sheet.get("values_digest") or sheet.get("baseline_digest")
        }
        sheet_sync.validate_live_baseline(correction, snapshot, snapshot["sheets"], live_values)
        live_values["TL_BRAND_PROFILE"]["digest"] = "f" * 64
        with self.assertRaisesRegex(sheet_sync.SyncError, "live values drift"):
            sheet_sync.validate_live_baseline(correction, snapshot, snapshot["sheets"], live_values)

    def test_active_lease_is_required_before_execution(self) -> None:
        sheet_sync.validate_active_lease(REPO_ROOT)
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "task.md").write_text("## no active lease\n", encoding="utf-8")
            with self.assertRaisesRegex(sheet_sync.SyncError, "lease drift"):
                sheet_sync.validate_active_lease(root)

    def test_bundle_has_10_creates_24_bounded_replacements_and_native_rules(self) -> None:
        datasets = sheet_sync.compile_datasets(REPO_ROOT)
        sheets = [{"title": "Trang tính1", "sheet_id": 0}]
        sheets.extend(
            {"title": title, "sheet_id": sheet_id}
            for title, sheet_id in sheet_sync.EXISTING_TAB_IDS.items()
        )
        correction = sheet_sync.build_correction_bundle(
            REPO_ROOT,
            datasets,
            {"spreadsheet_id": sheet_sync.TARGET_SPREADSHEET_ID, "sheets": sheets},
            "2026-08-05T23:00:00+07:00",
        )
        self.assertEqual(len(correction["create_actions"]), 10)
        self.assertEqual(len(correction["actions"]), 24)
        self.assertEqual({item["action"] for item in correction["actions"]}, {"REPLACE_RANGE"})
        for action in correction["actions"]:
            self.assertEqual(action["formatting"]["frozen_rows"], 1)
            fields = {item["field"] for item in action["validations"]}
            self.assertTrue({"evidence_status", "allowed_use"}.issubset(fields))
            self.assertNotIn("DELETE", json.dumps(action))
            self.assertNotIn("RENAME", json.dumps(action))
        approved = copy.deepcopy(correction)
        approved["approval_state"] = "APPROVED"
        sheet_sync.validate_exact_correction_scope(approved, REPO_ROOT, datasets, {"spreadsheet_id": sheet_sync.TARGET_SPREADSHEET_ID, "sheets": sheets})
        for mutation in ("create", "tab", "clear", "validation", "scope", "missing", "duplicate", "sheet_id"):
            broken = copy.deepcopy(approved)
            if mutation == "create":
                broken["create_actions"][0]["tab_key"] = "UNAPPROVED_TAB"
            elif mutation == "tab":
                broken["actions"][0]["tab_key"] = "Trang tính1"
            elif mutation == "clear":
                broken["actions"][0]["clear_range"] = "A1:Z1000"
            elif mutation == "validation":
                broken["actions"][0]["validations"] = []
            elif mutation == "scope":
                broken["scope_sha256"] = "0" * 64
            elif mutation == "missing":
                broken["actions"].pop()
            elif mutation == "duplicate":
                broken["actions"][1] = copy.deepcopy(broken["actions"][0])
            else:
                broken["actions"][10]["sheet_id"] = 999
            with self.assertRaisesRegex(sheet_sync.SyncError, "scope drift"):
                sheet_sync.validate_exact_correction_scope(broken, REPO_ROOT, datasets, {"spreadsheet_id": sheet_sync.TARGET_SPREADSHEET_ID, "sheets": sheets})

    def test_live_baseline_uses_historical_v2_no_newline_digest(self) -> None:
        payload = sheet_sync.read_json(REPO_ROOT / "docs Toplink/staging/run2/codex/61-sheet-payload-v2.json")
        brand = next(tab for tab in payload["tabs"] if tab["tab_key"] == "TL_BRAND_PROFILE")
        self.assertEqual(sheet_sync.sha256_v2_values(brand["values"]), "9917067b522ef620364712e44ce4d042965eb2a121ef565aef02ac7834e6cf5e")
        self.assertNotEqual(sheet_sync.sha256_json(brand["values"]), sheet_sync.sha256_v2_values(brand["values"]))


class ReadbackTests(unittest.TestCase):
    def test_detects_reordered_row_unicode_formula_validation_and_sheet_id_drift(self) -> None:
        expected = {
            "sheet_id": 123,
            "values": [["record_id", "formula"], ["TL-01", "=1+1"], ["TL-02", "Tiếng Việt"]],
            "formulas": [["", ""], ["", "=1+1"], ["", ""]],
            "validations": {"A2:A3": ["TL-01", "TL-02"]},
        }
        sheet_sync.verify_dataset_readback(expected, copy.deepcopy(expected))
        mutations = (
            ("values", [["record_id", "formula"], ["TL-02", "Tiếng Việt"], ["TL-01", "=1+1"]]),
            ("values", [["record_id", "formula"], ["TL-01", "=1+1"], ["TL-02", "Tieng Viet"]]),
            ("formulas", [["", ""], ["", ""], ["", ""]]),
            ("validations", {}),
            ("sheet_id", 456),
        )
        for field, value in mutations:
            actual = copy.deepcopy(expected)
            actual[field] = value
            with self.assertRaises(sheet_sync.SyncError):
                sheet_sync.verify_dataset_readback(expected, actual)

    def test_partial_write_is_verify_failed_and_not_auto_rollback(self) -> None:
        state = sheet_sync.record_partial_write(["TL_REPORT"], ["TL_OWNER_ACTIONS"])
        self.assertEqual(state["status"], "VERIFY_FAILED")
        self.assertFalse(state["automatic_rollback"])
        self.assertTrue(state["new_approval_required"])

    def test_native_sheet_state_checks_format_validation_and_dates(self) -> None:
        action = {
            "tab_key": "TL_REPORT",
            "max_rows": 2,
            "max_columns": 2,
            "formatting": {"frozen_rows": 1, "date_format": "yyyy-mm-dd hh:mm:ss"},
            "validations": [{"column_index": 0, "allowed_values": ["A", "B"]}],
            "date_columns": [1],
        }
        header_format = {
            "wrapStrategy": "WRAP",
            "backgroundColor": {"red": 0.4196, "green": 0.1216, "blue": 0.2118},
            "textFormat": {"foregroundColor": {"red": 1, "green": 1, "blue": 1}, "bold": True},
        }
        sheet = {
            "properties": {"sheetId": 123, "gridProperties": {"frozenRowCount": 1}},
            "data": [{
                "columnMetadata": [{"pixelSize": 180}, {"pixelSize": 180}],
                "rowData": [
                    {"values": [{"userEnteredFormat": copy.deepcopy(header_format)}, {"userEnteredFormat": copy.deepcopy(header_format)}]},
                    {"values": [
                        {"userEnteredFormat": {"wrapStrategy": "WRAP"}, "dataValidation": {"strict": True, "condition": {"type": "ONE_OF_LIST", "values": [{"userEnteredValue": "A"}, {"userEnteredValue": "B"}]}}},
                        {"userEnteredFormat": {"wrapStrategy": "WRAP", "numberFormat": {"type": "DATE_TIME", "pattern": "yyyy-mm-dd hh:mm:ss"}}},
                    ]},
                ],
            }],
        }
        sheet_sync.verify_native_sheet_readback(action, sheet, 123)
        for mutate in ("frozen", "width", "wrap", "header", "validation", "date"):
            broken = copy.deepcopy(sheet)
            if mutate == "frozen": broken["properties"]["gridProperties"]["frozenRowCount"] = 0
            elif mutate == "width": broken["data"][0]["columnMetadata"][0]["pixelSize"] = 100
            elif mutate == "wrap": broken["data"][0]["rowData"][1]["values"][0]["userEnteredFormat"]["wrapStrategy"] = "OVERFLOW_CELL"
            elif mutate == "header": broken["data"][0]["rowData"][0]["values"][0]["userEnteredFormat"]["textFormat"]["bold"] = False
            elif mutate == "validation": broken["data"][0]["rowData"][1]["values"][0]["dataValidation"]["strict"] = False
            else: broken["data"][0]["rowData"][1]["values"][1]["userEnteredFormat"]["numberFormat"]["pattern"] = "wrong"
            with self.assertRaises(sheet_sync.SyncError):
                sheet_sync.verify_native_sheet_readback(action, broken, 123)

    def test_partial_failure_persists_verify_failed_and_unsigned_recovery(self) -> None:
        class FailingSheets:
            def get(self, **_kwargs):
                raise RuntimeError("capture unavailable")
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            approved = {"bundle_id": "TL-SHEET-RUN2-CORRECTION-01", "actions": [{"tab_key": "TL_REPORT"}]}
            sheet_sync.persist_partial_failure(root, approved, ["CREATE_TAB"], RuntimeError("write failed"), FailingSheets())
            evidence = sheet_sync.read_json(root / sheet_sync.CORRECTION_DIR / "correction-readback.json")
            recovery = sheet_sync.read_json(root / sheet_sync.CORRECTION_DIR / "recovery-bundle-unsigned.json")
            self.assertEqual(evidence["status"], "VERIFY_FAILED")
            self.assertTrue(recovery["new_approval_required"])
            self.assertEqual(recovery["approval_state"], "NOT_GRANTED")


class CliContractTests(unittest.TestCase):
    def test_cli_exposes_all_correction_commands(self) -> None:
        parser = sheet_sync.build_parser()
        choices = next(action for action in parser._actions if action.dest == "command").choices
        self.assertEqual(
            set(choices),
            {
                "compile-datasets",
                "validate-datasets",
                "snapshot-target",
                "build-correction-bundle",
                "validate-approval",
                "execute-correction",
                "verify-readback",
            },
        )

    def test_writes_one_deterministic_json_sidecar_per_dataset(self) -> None:
        bundle = sheet_sync.compile_datasets(REPO_ROOT)
        with tempfile.TemporaryDirectory() as temp_dir:
            paths = sheet_sync.write_dataset_sidecars(bundle, Path(temp_dir))
            self.assertEqual(len(paths), 24)
            parsed = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
            self.assertEqual({item["dataset_key"] for item in parsed}, set(sheet_sync.TAB_KEYS))


if __name__ == "__main__":
    unittest.main()
