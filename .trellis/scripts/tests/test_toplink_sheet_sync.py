from __future__ import annotations

import copy
import importlib.util
import inspect
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
    def test_registry_has_exact_ordered_21_human_layer_tabs(self) -> None:
        registry = sheet_sync.load_registry(REPO_ROOT)
        self.assertEqual(registry["schema_version"], "YV-SHEET-001/1.0.0")
        self.assertEqual(
            [tab["tab"] for tab in sorted(registry["tabs"], key=lambda item: item["index"])],
            list(sheet_sync.TAB_KEYS),
        )
        self.assertEqual(len(sheet_sync.TAB_KEYS), 21)

    def test_stale_existing_tab_id_map_is_removed(self) -> None:
        self.assertFalse(hasattr(sheet_sync, "EXISTING_TAB_IDS"))
        self.assertFalse(hasattr(sheet_sync, "NEW_TAB_KEYS"))

    def test_every_tab_declares_hidden_key_and_audit(self) -> None:
        for tab in sheet_sync.load_registry(REPO_ROOT)["tabs"]:
            hidden = tab["hidden_columns"]
            self.assertEqual([item["header"] for item in hidden], ["_key", "_audit"])
            self.assertTrue(all(item["hidden_by_user"] for item in hidden))


class HumanLayerCompilerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.plan = sheet_sync.build_human_layer_plan(REPO_ROOT)
        self.locked = json.loads(
            (REPO_ROOT / "staging/yv-humanize/report-plan.json").read_text(encoding="utf-8")
        )

    def test_independent_plan_rebuild_matches_locked_hashes(self) -> None:
        self.assertEqual(len(self.plan["tabs"]), 21)
        self.assertEqual(self.plan["workbook_content_hash"], self.locked["workbook_content_hash"])
        self.assertEqual(
            {tab["tab"]: tab["content_hash"] for tab in self.plan["tabs"]},
            {tab["tab"]: tab["content_hash"] for tab in self.locked["tabs"]},
        )

    def test_independent_plan_matches_all_four_phase_one_fixtures(self) -> None:
        fixture_dir = Path(__file__).resolve().parent / "fixtures" / "yv"
        by_tab = {tab["tab"]: tab for tab in self.plan["tabs"]}
        for name in ("report", "YV_08_experiments", "YV_09_content_calendar"):
            fixture = json.loads((fixture_dir / f"{name}.json").read_text(encoding="utf-8"))
            actual = by_tab[name]
            for field in ("row_count", "column_count", "used_range", "yellow_cells", "values", "content_hash"):
                self.assertEqual(fixture[field], actual[field], f"{name}:{field}")
        workbook = json.loads((fixture_dir / "workbook.json").read_text(encoding="utf-8"))
        self.assertEqual(workbook["tab_count"], self.plan["tab_count"])
        self.assertEqual(workbook["total_yellow_cells"], self.plan["total_yellow_cells"])
        self.assertEqual(workbook["workbook_content_hash"], self.plan["workbook_content_hash"])
        self.assertEqual(
            workbook["tab_hashes"],
            {tab["tab"]: tab["content_hash"] for tab in self.plan["tabs"]},
        )

    def test_split_options_fails_closed_instead_of_cloning(self) -> None:
        with self.assertRaisesRegex(sheet_sync.SyncError, "three options"):
            sheet_sync._split_options("A: one · B: two")
        with self.assertRaisesRegex(sheet_sync.SyncError, "duplicate option bodies"):
            sheet_sync._split_options("A: same · B: same · C: other")

    def test_split_options_returns_ordered_distinct_abc(self) -> None:
        self.assertEqual(
            sheet_sync._split_options("A: one · B: two · C: three"),
            [("A", "one"), ("B", "two"), ("C", "three")],
        )

    def test_calendar_carries_real_audience_experiment_review_and_cycle(self) -> None:
        calendar = next(tab for tab in self.plan["tabs"] if tab["tab"] == "YV_09_content_calendar")
        headers = calendar["values"][0]
        rows = calendar["values"][2:]
        for header in ("Chu kỳ", "Nhóm khách", "Tuyến duyệt"):
            index = headers.index(header)
            self.assertTrue(all(row[index] not in ("", "—", "NOT_AVAILABLE") for row in rows))
        experiment_index = headers.index("Thử nghiệm gắn kèm")
        experiments = {row[experiment_index] for row in rows}
        self.assertGreater(len(experiments - {"—"}), 0)
        self.assertNotIn("NOT_AVAILABLE", experiments)

    def test_all_tabs_put_key_and_audit_last(self) -> None:
        for tab in self.plan["tabs"]:
            self.assertEqual(tab["values"][0][-2:], ["_key", "_audit"])
            self.assertTrue(all(len(row) == tab["column_count"] for row in tab["values"]))

    def test_plan_is_pure_and_local_only(self) -> None:
        self.assertEqual(self.plan["external_writes"], 0)
        self.assertFalse(self.plan["write_executed"])
        self.assertEqual(self.plan["state"], "DRAFT_UNSIGNED · LOCAL_ONLY")


class DatasetBundleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bundle = sheet_sync.compile_datasets(REPO_ROOT)

    def test_bundle_has_21_deterministic_datasets(self) -> None:
        self.assertEqual(set(self.bundle["datasets"]), set(sheet_sync.TAB_KEYS))
        self.assertEqual(self.bundle, sheet_sync.compile_datasets(REPO_ROOT))
        sheet_sync.validate_human_layer_bundle(self.bundle, REPO_ROOT)

    def test_source_digest_drift_is_rejected(self) -> None:
        broken = copy.deepcopy(self.bundle)
        key = next(iter(broken["source_digests"]))
        broken["source_digests"][key] = "0" * 64
        with self.assertRaisesRegex(sheet_sync.SyncError, "source digest drift"):
            sheet_sync.validate_source_digests(broken, REPO_ROOT)

    def test_writes_one_sidecar_per_tab(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir)
            paths = sheet_sync.write_dataset_sidecars(self.bundle, output)
            self.assertEqual(len(paths), 21)
            sheet_sync.validate_dataset_sidecars(self.bundle, output)
            parsed = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
            self.assertEqual({item["dataset_key"] for item in parsed}, set(sheet_sync.TAB_KEYS))

    def test_bundle_digest_drift_is_rejected(self) -> None:
        broken = copy.deepcopy(self.bundle)
        broken["bundle_sha256"] = "0" * 64
        with self.assertRaisesRegex(sheet_sync.SyncError, "bundle digest drift"):
            sheet_sync.validate_human_layer_bundle(broken, REPO_ROOT)


class HumanLayerValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = sheet_sync.load_human_layer_registry(REPO_ROOT)
        self.plan = sheet_sync.build_human_layer_plan(REPO_ROOT)

    def tab(self, name: str) -> dict:
        return next(tab for tab in self.plan["tabs"] if tab["tab"] == name)

    def test_signed_plan_satisfies_semantic_contract(self) -> None:
        sheet_sync.validate_human_layer_plan(self.plan, self.registry)

    def test_status_escalation_is_rejected(self) -> None:
        tab = self.tab("YV_01_brand_profile")
        tab["values"][2][0] = "APPROVED"
        with self.assertRaisesRegex(sheet_sync.SyncError, "status escalation"):
            sheet_sync.validate_human_layer_plan(self.plan, self.registry)

    def test_yellow_cell_contract_is_recomputed_from_values(self) -> None:
        tab = self.tab("00_Y_VIEN_CAN_CHOT")
        address = tab["yellow_cells"][0]
        row_number = int("".join(char for char in address if char.isdigit()))
        column_letters = "".join(char for char in address if char.isalpha())
        column_number = 0
        for char in column_letters:
            column_number = column_number * 26 + ord(char) - ord("A") + 1
        tab["values"][row_number - 1][column_number - 1] = "DỰ PHÒNG — không phải việc chờ người chốt"
        with self.assertRaisesRegex(sheet_sync.SyncError, "yellow"):
            sheet_sync.validate_human_layer_plan(self.plan, self.registry)

    def test_external_yellow_cell_requires_corresponding_open_owner_row(self) -> None:
        tab = self.tab("00_Y_VIEN_CAN_CHOT")
        target = next(row for row in tab["values"][2:] if row[-2] == "TL-OA-06")
        target[-2] = "TL-OA-06-MISSING"
        with self.assertRaisesRegex(sheet_sync.SyncError, "yellow correspondence"):
            sheet_sync.validate_human_layer_plan(self.plan, self.registry)

    def test_duplicate_stable_key_is_rejected(self) -> None:
        tab = self.tab("YV_05_content_pillars")
        tab["values"][3][-2] = tab["values"][2][-2]
        with self.assertRaisesRegex(sheet_sync.SyncError, "duplicate stable key"):
            sheet_sync.validate_human_layer_plan(self.plan, self.registry)

    def test_minimum_record_count_is_enforced(self) -> None:
        tab = self.tab("YV_05_content_pillars")
        tab["values"].pop()
        tab["row_count"] -= 1
        with self.assertRaisesRegex(sheet_sync.SyncError, "cardinality"):
            sheet_sync.validate_human_layer_plan(self.plan, self.registry)

    def test_maximum_record_count_is_enforced(self) -> None:
        tab = self.tab("YV_05_content_pillars")
        extra = copy.deepcopy(tab["values"][-1])
        extra[-2] = "TEST-UNIQUE-EXTRA-KEY"
        tab["values"].append(extra)
        tab["row_count"] += 1
        with self.assertRaisesRegex(sheet_sync.SyncError, "cardinality"):
            sheet_sync.validate_human_layer_plan(self.plan, self.registry)

    def test_registry_tab_reference_orphan_is_rejected(self) -> None:
        tab = self.tab("03_OUTPUT_INDEX")
        column = tab["values"][0].index("Tab hiển thị")
        tab["values"][2][column] = "TAB_KHÔNG_TỒN_TẠI"
        with self.assertRaisesRegex(sheet_sync.SyncError, "orphan foreign key"):
            sheet_sync.validate_human_layer_plan(self.plan, self.registry)

    def test_dataset_foreign_key_orphan_is_rejected(self) -> None:
        tab = self.tab("YV_09_content_calendar")
        column = tab["values"][0].index("Nhóm khách")
        tab["values"][2][column] = "NHÓM KHÁCH KHÔNG TỒN TẠI"
        with self.assertRaisesRegex(sheet_sync.SyncError, "orphan foreign key"):
            sheet_sync.validate_human_layer_plan(self.plan, self.registry)

    def test_unindexed_source_artifact_is_rejected_as_orphan(self) -> None:
        tab = self.tab("03_OUTPUT_INDEX")
        tab["values"].pop()
        tab["row_count"] -= 1
        with self.assertRaisesRegex(sheet_sync.SyncError, "orphan source artifact"):
            sheet_sync.validate_human_layer_plan(self.plan, self.registry)


class ApprovalAndRangeSafetyTests(unittest.TestCase):
    def test_signed_human_layer_approvals_remain_digest_exact_but_are_consumed(self) -> None:
        self.assertEqual(
            set(sheet_sync.validate_human_layer_approvals(REPO_ROOT, require_unconsumed=False)),
            {"CREATE_TAB", "UPSERT", "READBACK"},
        )
        with self.assertRaisesRegex(sheet_sync.SyncError, "already consumed"):
            sheet_sync.validate_human_layer_approvals(REPO_ROOT)

    def test_recovery_signatures_remain_digest_exact_but_are_consumed(self) -> None:
        self.assertEqual(
            set(
                sheet_sync.validate_human_layer_recovery_approvals(
                    REPO_ROOT, require_unconsumed=False
                )
            ),
            {"UPSERT_RECOVERY", "READBACK_RECOVERY"},
        )
        with self.assertRaisesRegex(sheet_sync.SyncError, "not unconsumed"):
            sheet_sync.validate_human_layer_recovery_approvals(REPO_ROOT)

    def test_p27_closure_plan_is_bounded_and_deterministic(self) -> None:
        closure = sheet_sync.build_human_layer_ledger_closure(REPO_ROOT)
        self.assertEqual(closure["status"], "DRAFT_UNSIGNED")
        self.assertEqual(closure["external_writes_authorized"], 2)
        self.assertEqual(
            [action["range"] for action in closure["actions"]],
            ["'03_OUTPUT_INDEX'!E3:F21", "'04_DECISIONS'!A20:J20"],
        )
        self.assertEqual(len(closure["actions"][0]["values"]), 19)
        self.assertEqual(
            set(tuple(row) for row in closure["actions"][0]["values"]),
            {("SYNC_WRITE_PASS", "SYNC_READBACK_PASS")},
        )
        revision = closure["actions"][1]["values"][0]
        self.assertEqual(revision[-2], "YV-REV-20260805-01")
        self.assertEqual(revision[7], "DECIDED")
        expected = sheet_sync.apply_human_layer_ledger_closure(
            sheet_sync.build_human_layer_plan(REPO_ROOT), closure
        )
        decisions = next(tab for tab in expected["tabs"] if tab["tab"] == "04_DECISIONS")
        self.assertEqual(decisions["row_count"], 20)
        self.assertEqual(decisions["used_range"], "'04_DECISIONS'!A1:J20")
        sheet_sync.validate_human_layer_plan(
            expected, sheet_sync.load_human_layer_registry(REPO_ROOT)
        )
        self.assertEqual(
            closure,
            sheet_sync.build_human_layer_ledger_closure(REPO_ROOT),
        )

    def test_p27_closure_signatures_remain_digest_exact_but_are_consumed(self) -> None:
        self.assertEqual(
            set(
                sheet_sync.validate_human_layer_ledger_closure_approvals(
                    REPO_ROOT, require_unconsumed=False
                )
            ),
            {"P2_7_LEDGER_UPSERT", "P2_7_LEDGER_READBACK"},
        )
        with self.assertRaisesRegex(sheet_sync.SyncError, "not unconsumed"):
            sheet_sync.validate_human_layer_ledger_closure_approvals(REPO_ROOT)

    def test_p27_structural_requests_touch_only_decision_row_20(self) -> None:
        plan = sheet_sync.build_human_layer_plan(REPO_ROOT)
        requests = sheet_sync.build_p27_structural_requests(plan, 1314363516)
        self.assertEqual(len(requests), 3)
        serialized = json.dumps(requests)
        self.assertNotIn("ConditionalFormat", serialized)
        self.assertNotIn('"sheetId": 0', serialized)
        self.assertIn('"startRowIndex": 19', serialized)
        self.assertIn('"endRowIndex": 20', serialized)

    def test_p28_same_payload_second_run_has_zero_diff(self) -> None:
        base = sheet_sync.build_human_layer_plan(REPO_ROOT)
        expected = sheet_sync.apply_human_layer_ledger_closure(
            base, sheet_sync.build_human_layer_ledger_closure(REPO_ROOT)
        )
        readback = {
            "valueRanges": [
                {"range": tab["used_range"], "values": copy.deepcopy(tab["values"])}
                for tab in expected["tabs"]
            ]
        }
        audit = sheet_sync.audit_human_layer_idempotency(expected, readback)
        self.assertEqual(audit["same_payload_second_run_diff_count"], 0)
        self.assertFalse(audit["would_write"])
        readback["valueRanges"][0]["values"][0][0] = "drift"
        drift = sheet_sync.audit_human_layer_idempotency(expected, readback)
        self.assertEqual(drift["cell_diff_count"], 1)
        self.assertTrue(drift["would_write"])

    def test_p3_expected_live_plan_covers_runtime_overlay(self) -> None:
        expected = sheet_sync.build_p3_expected_live_plan(REPO_ROOT)
        self.assertEqual(
            expected["workbook_content_hash"],
            "f5a373b814c5995592514b0eea670e8c1540ad4ed8bdcb769a6f8d2365f5a585",
        )
        decisions = next(tab for tab in expected["tabs"] if tab["tab"] == "04_DECISIONS")
        self.assertEqual(decisions["values"][-1][-2], "YV-REV-20260805-01")

    def test_p3_approval_remains_exact_read_only_and_consumed(self) -> None:
        approval = sheet_sync.validate_p3_live_verify_approval(
            REPO_ROOT, require_unconsumed=False
        )
        self.assertEqual(approval["mutation_requests_allowed"], 0)
        self.assertEqual(approval["read_plane_count"], 3)
        with self.assertRaisesRegex(sheet_sync.SyncError, "consumed"):
            sheet_sync.validate_p3_live_verify_approval(REPO_ROOT)

    def test_p3_verifier_has_no_mutation_or_restore_path(self) -> None:
        source = inspect.getsource(sheet_sync._verify_live_state_command)
        self.assertIn("_read_human_layer_planes", source)
        for forbidden in ("batchUpdate", "batchClear", "_restore", "addSheet", "deleteSheet", "repeatCell"):
            self.assertNotIn(forbidden, source)

    def test_readback_metadata_scope_includes_preserved_sheet(self) -> None:
        plan = sheet_sync.build_human_layer_plan(REPO_ROOT)
        topology = {
            "sheets": [
                {"properties": {"title": name, "sheetId": index + 100, "index": index}}
                for index, name in enumerate(sheet_sync.TAB_KEYS)
            ]
            + [
                {
                    "properties": {
                        "title": "Trang tính1",
                        "sheetId": 0,
                        "index": 21,
                        "gridProperties": {"rowCount": 1000, "columnCount": 26},
                    }
                }
            ]
        }
        filtered_grid = {
            "sheets": [
                {"properties": {"title": name, "sheetId": index + 100, "index": index}}
                for index, name in enumerate(sheet_sync.TAB_KEYS)
            ]
        }
        sheet_sync.validate_human_layer_topology_metadata(topology)
        self.assertEqual(
            sheet_sync.validate_human_layer_grid_scope(filtered_grid),
            set(sheet_sync.TAB_KEYS),
        )
        with self.assertRaisesRegex(sheet_sync.SyncError, "topology"):
            sheet_sync.validate_human_layer_topology_metadata(filtered_grid)
        self.assertEqual(
            sheet_sync.human_layer_grid_ranges(plan),
            [tab["used_range"] for tab in plan["tabs"]],
        )

    def test_recovery_target_requires_21_existing_blank_default_grids(self) -> None:
        plan = sheet_sync.build_human_layer_plan(REPO_ROOT)
        topology_sheets = []
        grid_sheets = []
        for index, tab in enumerate(plan["tabs"]):
            properties = {
                "title": tab["tab"],
                "sheetId": index + 100,
                "index": index,
                "gridProperties": {
                    "rowCount": tab["row_count"],
                    "columnCount": tab["column_count"],
                },
            }
            topology_sheets.append({"properties": copy.deepcopy(properties)})
            grid_sheets.append({"properties": copy.deepcopy(properties)})
        topology_sheets.append(
            {
                "properties": {
                    "title": "Trang tính1",
                    "sheetId": 0,
                    "index": 21,
                    "gridProperties": {"rowCount": 1000, "columnCount": 26},
                }
            }
        )
        topology = {"sheets": topology_sheets}
        filtered_grid = {"sheets": grid_sheets}
        blank_values = {
            "valueRanges": [{"range": tab["used_range"]} for tab in plan["tabs"]]
        }
        result = sheet_sync.validate_blank_human_layer_recovery_target(
            plan, topology, filtered_grid, blank_values
        )
        self.assertEqual(result["blank_range_count"], 21)
        broken = copy.deepcopy(blank_values)
        broken["valueRanges"][0]["values"] = [["not blank"]]
        with self.assertRaisesRegex(sheet_sync.SyncError, "not blank"):
            sheet_sync.validate_blank_human_layer_recovery_target(
                plan, topology, filtered_grid, broken
            )

    def test_create_and_format_requests_are_bounded_to_human_tabs(self) -> None:
        plan = sheet_sync.build_human_layer_plan(REPO_ROOT)
        registry = sheet_sync.load_human_layer_registry(REPO_ROOT)
        creates = sheet_sync.build_human_layer_create_requests(plan)
        self.assertEqual(len(creates), 21)
        self.assertEqual(
            [request["addSheet"]["properties"]["title"] for request in creates],
            list(sheet_sync.TAB_KEYS),
        )
        self.assertEqual(
            [request["addSheet"]["properties"]["index"] for request in creates],
            list(range(21)),
        )
        sheet_ids = {name: index + 100 for index, name in enumerate(sheet_sync.TAB_KEYS)}
        formats = sheet_sync.build_human_layer_format_requests(plan, registry, sheet_ids)
        serialized = json.dumps(formats)
        self.assertNotIn("ConditionalFormat", serialized)
        self.assertNotIn('"sheetId": 0', serialized)
        self.assertEqual(sum("setBasicFilter" in request for request in formats), 21)
        self.assertEqual(
            sum(
                request.get("updateDimensionProperties", {}).get("properties", {}).get("hiddenByUser") is True
                for request in formats
            ),
            42,
        )
        gold = sheet_sync._yv_rgb(plan["palette"]["action_required"])
        self.assertEqual(
            sum(
                request.get("repeatCell", {}).get("cell", {}).get("userEnteredFormat", {}).get("backgroundColor") == gold
                and request.get("repeatCell", {}).get("fields") == "userEnteredFormat.backgroundColor"
                for request in formats
            ),
            27,
        )

    def test_human_layer_snapshot_accepts_only_pristine_target(self) -> None:
        metadata = {
            "spreadsheetId": sheet_sync.TARGET_SPREADSHEET_ID,
            "properties": {"title": "IMC Plan - Toplink Y Viện"},
            "sheets": [{"properties": {"title": "Trang tính1", "sheetId": 0, "index": 0}}],
        }
        snapshot = sheet_sync.validate_human_layer_target_snapshot(
            metadata, sheet_sync.TARGET_SERVICE_ACCOUNT
        )
        self.assertEqual(snapshot["sheets"][0]["sheet_id"], 0)
        self.assertEqual(snapshot["external_writes"], 0)

        extra = copy.deepcopy(metadata)
        extra["sheets"].append({"properties": {"title": "report", "sheetId": 123}})
        with self.assertRaisesRegex(sheet_sync.SyncError, "only Trang tính1"):
            sheet_sync.validate_human_layer_target_snapshot(extra, sheet_sync.TARGET_SERVICE_ACCOUNT)

        forbidden = copy.deepcopy(metadata)
        forbidden["sheets"].append({"properties": {"title": "report_v2", "sheetId": 124}})
        with self.assertRaisesRegex(sheet_sync.SyncError, "forbidden _v2"):
            sheet_sync.validate_human_layer_target_snapshot(forbidden, sheet_sync.TARGET_SERVICE_ACCOUNT)

        with self.assertRaisesRegex(sheet_sync.SyncError, "wrong service account"):
            sheet_sync.validate_human_layer_target_snapshot(metadata, "wrong@example.com")

    def test_bounded_replace_clears_only_union_tail(self) -> None:
        self.assertEqual(
            sheet_sync.plan_bounded_replace("A1:C10", "A1:B4"),
            {"clear_range": "A1:C10", "write_range": "A1:B4"},
        )

    def test_material_edit_resets_approval(self) -> None:
        payload = {"content_hash": "old", "verdict": "APPROVED", "publish_state": "READY"}
        reset = sheet_sync.reset_approval_on_material_edit(payload, "new")
        self.assertEqual(reset["verdict"], "NEEDS_HUMAN_REVIEW")
        self.assertEqual(reset["publish_state"], "BLOCKED")

    def test_create_action_rejects_existing_titles(self) -> None:
        with self.assertRaisesRegex(sheet_sync.SyncError, "existing tab"):
            sheet_sync.validate_create_actions(["report"], {"Trang tính1", "report"})

    def test_active_lease_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "task.md").write_text(
                "| Codex CLI (`root`) | `.trellis/scripts/toplink_sheet_sync.py` | now | digest-bound approval |\n",
                encoding="utf-8",
            )
            sheet_sync.validate_active_lease(root)
            (root / "task.md").write_text("## Lease\n", encoding="utf-8")
            with self.assertRaisesRegex(sheet_sync.SyncError, "lease drift"):
                sheet_sync.validate_active_lease(root)

    def test_partial_write_is_verify_failed_without_automatic_rollback(self) -> None:
        evidence = sheet_sync.record_partial_write(["report"], ["00_Y_VIEN_CAN_CHOT"])
        self.assertEqual(evidence["status"], "VERIFY_FAILED")
        self.assertFalse(evidence["automatic_rollback"])
        self.assertTrue(evidence["new_approval_required"])

    def test_expired_approval_fails_closed(self) -> None:
        bundle = {
            "spreadsheet_id": sheet_sync.TARGET_SPREADSHEET_ID,
            "service_account": sheet_sync.TARGET_SERVICE_ACCOUNT,
            "operator": "Codex CLI",
            "expires_at_ict": (datetime.now(timezone.utc) - timedelta(days=1)).isoformat(),
            "approval_state": "APPROVED",
            "actions": [],
        }
        with self.assertRaisesRegex(sheet_sync.SyncError, "expired"):
            sheet_sync.validate_correction_approval(bundle)


class CliContractTests(unittest.TestCase):
    def test_cli_exposes_human_layer_commands(self) -> None:
        parser = sheet_sync.build_parser()
        choices = next(action for action in parser._actions if action.dest == "command").choices
        for command in (
            "compile-datasets",
            "validate-datasets",
            "build-report-plan",
            "snapshot-target",
            "snapshot-human-layer-recovery",
            "execute-human-layer",
            "execute-human-layer-recovery",
            "verify-human-layer-recovery",
            "build-human-layer-ledger-closure",
            "execute-human-layer-ledger-closure",
            "verify-human-layer-ledger-closure",
            "audit-human-layer-idempotency",
            "verify-live-state",
            "verify-readback",
        ):
            self.assertIn(command, choices)


if __name__ == "__main__":
    unittest.main()
