from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "toplink_sheet_sync.py"
SPEC = importlib.util.spec_from_file_location("toplink_sheet_sync", MODULE_PATH)
assert SPEC and SPEC.loader
sheet_sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sheet_sync)


class CompileMarkdownTests(unittest.TestCase):
    def test_compiles_unicode_tables_and_formula_like_text_as_literal_cells(self) -> None:
        markdown = """# Tiêu đề

Mô tả dưỡng sinh.

## Bảng

| ID | Nội dung | Trạng thái |
|---|---|---|
| `TL-01` | =IMPORTXML(\"x\") | `TOPLINK_CONFIRMED` |
"""

        result = sheet_sync.compile_markdown(
            markdown=markdown,
            artifact_id="TL-ART-001",
            source_path="docs Toplink/test.md",
            source_digest="a" * 64,
            prepared_at_ict="2026-08-04T19:30:00+07:00",
        )

        flat_cells = [cell for row in result["values"] for cell in row]
        self.assertIn("Mô tả dưỡng sinh.", flat_cells)
        self.assertIn('=IMPORTXML("x")', flat_cells)
        self.assertTrue(all(isinstance(cell, str) for cell in flat_cells))
        stable_keys = [row[0] for row in result["values"] if row and row[0].startswith("TL-ART-001/")]
        self.assertEqual(len(stable_keys), len(set(stable_keys)))

    def test_same_input_produces_same_values_and_digest(self) -> None:
        kwargs = {
            "markdown": "# A\n\nNội dung.\n",
            "artifact_id": "TL-ART-001",
            "source_path": "docs Toplink/a.md",
            "source_digest": "b" * 64,
            "prepared_at_ict": "2026-08-04T19:30:00+07:00",
        }

        first = sheet_sync.compile_markdown(**kwargs)
        second = sheet_sync.compile_markdown(**kwargs)

        self.assertEqual(first, second)
        self.assertEqual(first["payload_sha256"], sheet_sync.sha256_json(first["values"]))

    def test_groups_prose_rows_under_one_header_per_section(self) -> None:
        result = sheet_sync.compile_markdown(
            markdown="# A\n\nDòng một.\n\nDòng hai.\n",
            artifact_id="TL-ART-001",
            source_path="a.md",
            source_digest="b" * 64,
            prepared_at_ict="2026-08-04T19:30:00+07:00",
        )

        self.assertEqual(len(result["header_row_indexes"]), 1)


class RegistryTests(unittest.TestCase):
    def test_rejects_duplicate_tab_or_artifact_identity(self) -> None:
        mapping = [
            {"stable_id": "TL-A", "path": "a.md", "sha256": "a" * 64, "tab_key": "TL_A"},
            {"stable_id": "TL-A", "path": "b.md", "sha256": "b" * 64, "tab_key": "TL_B"},
        ]

        with self.assertRaisesRegex(sheet_sync.SyncError, "duplicate stable_id"):
            sheet_sync.validate_mapping(mapping)

    def test_builds_exact_used_ranges_and_rejects_source_hash_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "artifact.md"
            source.write_text("# A\n\n| ID | State |\n|---|---|\n| `TL-1` | DRAFT |\n", encoding="utf-8")
            registry = {
                "approval_bundle_id": "TL-SHEET-RUN2-14-V1",
                "spreadsheet_id": "sheet-1",
                "metadata_read_result": {"preserve_existing_tabs": ["Trang tính1"]},
                "auth_readiness": {"service_account": "writer@example.iam.gserviceaccount.com"},
                "input_manifest": {"run2_manifest_sha256": "c" * 64},
                "common_scope": {
                    "mapping": [
                        {
                            "stable_id": "TL-ART-001",
                            "path": "artifact.md",
                            "sha256": sheet_sync.sha256_file(source),
                            "tab_key": "TL_ARTIFACT",
                        }
                    ]
                },
            }

            payload = sheet_sync.build_payload(
                repo_root=root,
                registry=registry,
                prepared_at_ict="2026-08-04T19:30:00+07:00",
                expected_count=1,
            )

            self.assertEqual(payload["tabs"][0]["used_range"], "A1:M9")
            self.assertEqual(payload["tabs"][0]["tab_title"], "TL_ARTIFACT")

            registry["common_scope"]["mapping"][0]["sha256"] = "0" * 64
            with self.assertRaisesRegex(sheet_sync.SyncError, "source hash drift"):
                sheet_sync.build_payload(
                    repo_root=root,
                    registry=registry,
                    prepared_at_ict="2026-08-04T19:30:00+07:00",
                    expected_count=1,
                )


class ApprovalTests(unittest.TestCase):
    def test_requires_exact_unexpired_digest_bound_statement(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "approval.json"
            payload = {
                "approval_bundle_id": "TL-SHEET-RUN2-14-V2",
                "expires_at_ict": "2026-08-05T18:30:00+07:00",
            }
            path.write_text(json.dumps(payload), encoding="utf-8")
            digest = sheet_sync.sha256_file(path)
            repo_path = "docs Toplink/staging/run2/codex/62-sheet-target-approval-v2.json"
            statement = f"APPROVED: TL-SHEET-RUN2-14-V2 at {repo_path} SHA-256 {digest}"

            sheet_sync.validate_approval_statement(
                statement=statement,
                approval_path=path,
                repository_path=repo_path,
                now=datetime(2026, 8, 4, 12, 0, tzinfo=timezone.utc),
            )

            with self.assertRaisesRegex(sheet_sync.SyncError, "approval statement mismatch"):
                sheet_sync.validate_approval_statement(
                    statement=statement.replace(digest, "0" * 64),
                    approval_path=path,
                    repository_path=repo_path,
                    now=datetime(2026, 8, 4, 12, 0, tzinfo=timezone.utc),
                )

    def test_approval_envelope_binds_payload_without_credential_material(self) -> None:
        payload = {
            "spreadsheet_id": "sheet-1",
            "preserve_existing_tabs": ["Trang tính1"],
            "service_account": "writer@example.iam.gserviceaccount.com",
            "format_policy": {"value_input_option": "RAW"},
            "tabs_digest": "d" * 64,
            "tabs": [
                {
                    "artifact_stable_id": "TL-A",
                    "source_path": "a.md",
                    "source_sha256": "a" * 64,
                    "tab_key": "TL_A",
                    "tab_title": "TL_A",
                    "schema": "TL-SHEET-001/0.1.3/TL_A/v2",
                    "used_range": "A1:M12",
                    "row_count": 12,
                    "column_count": 13,
                    "payload_sha256": "b" * 64,
                }
            ],
        }

        approval = sheet_sync.build_approval_envelope(
            payload=payload,
            payload_repository_path="payload.json",
            payload_file_sha256="c" * 64,
            prepared_at_ict="2026-08-04T19:30:00+07:00",
            expires_at_ict="2026-08-05T19:30:00+07:00",
        )

        serialized = json.dumps(approval)
        self.assertEqual([record["action"] for record in approval["approval_records"]], ["CREATE_TAB", "UPSERT", "READBACK"])
        self.assertNotIn("private_key", serialized)
        self.assertNotIn("credential_path", serialized)

    def test_execution_bundle_rejects_payload_tampering_before_network(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "a.md"
            source.write_text("# A\n\nText\n", encoding="utf-8")
            payload = {
                "spreadsheet_id": "sheet-1",
                "service_account": "writer@example.iam.gserviceaccount.com",
                "format_policy": {"value_input_option": "RAW"},
                "tabs_digest": "d" * 64,
                "tabs": [
                    {
                        "artifact_stable_id": "TL-A",
                        "source_path": "a.md",
                        "source_sha256": sheet_sync.sha256_file(source),
                        "tab_key": "TL_A",
                        "tab_title": "TL_A",
                        "schema": "TL-SHEET-001/0.1.3/TL_A/v2",
                        "used_range": "A1:A1",
                        "row_count": 1,
                        "column_count": 1,
                        "payload_sha256": sheet_sync.sha256_json([["x"]]),
                        "values": [["x"]],
                    }
                ],
            }
            payload_path = root / "payload.json"
            payload_path.write_text(json.dumps(payload), encoding="utf-8")
            scope = {
                "bound_payload_path": "payload.json",
                "bound_payload_sha256": sheet_sync.sha256_file(payload_path),
                "tab_scope": [
                    {
                        key: payload["tabs"][0][key]
                        for key in (
                            "artifact_stable_id", "source_path", "source_sha256", "tab_key", "tab_title",
                            "schema", "used_range", "row_count", "column_count", "payload_sha256",
                        )
                    }
                ],
                "format_policy": payload["format_policy"],
            }
            approval = {
                "approval_bundle_id": "TL-SHEET-RUN2-14-V2",
                "approval_state": "DRAFT_UNSIGNED",
                "target_class": "TOPLINK_ONLY",
                "expires_at_ict": "2026-08-05T18:30:00+07:00",
                "spreadsheet_id": "sheet-1",
                "service_account": "writer@example.iam.gserviceaccount.com",
                "payload_binding": {
                    "repository_path": "payload.json",
                    "sha256": sheet_sync.sha256_file(payload_path),
                    "tabs_digest": "d" * 64,
                },
                "approval_records": [
                    {"phase": 1, "action": "CREATE_TAB", "limits": {"max_tabs": 1, "max_rows_per_tab": 1}, "authorized_agent": "Codex CLI", "expires_at_ict": "2026-08-05T18:30:00+07:00", "readback_required": True, "bound_scope": scope},
                    {"phase": 2, "action": "UPSERT", "limits": {"max_tabs": 0, "max_rows_per_tab": 1}, "authorized_agent": "Codex CLI", "expires_at_ict": "2026-08-05T18:30:00+07:00", "readback_required": True, "bound_scope": scope},
                    {"phase": 3, "action": "READBACK", "limits": {"max_tabs": 0, "max_rows_per_tab": 1}, "authorized_agent": "Codex CLI", "expires_at_ict": "2026-08-05T18:30:00+07:00", "readback_required": True, "bound_scope": scope},
                ],
            }
            approval_path = root / "approval.json"
            approval_path.write_text(json.dumps(approval), encoding="utf-8")
            statement = (
                "APPROVED: TL-SHEET-RUN2-14-V2 at approval.json SHA-256 "
                + sheet_sync.sha256_file(approval_path)
            )

            sheet_sync.validate_execution_bundle(
                repo_root=root,
                payload_path=payload_path,
                payload_repository_path="payload.json",
                approval_path=approval_path,
                approval_repository_path="approval.json",
                statement=statement,
                now=datetime(2026, 8, 4, 12, 0, tzinfo=timezone.utc),
            )

            payload["tabs"][0]["values"] = [["tampered"]]
            payload_path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(sheet_sync.SyncError, "payload file digest mismatch"):
                sheet_sync.validate_execution_bundle(
                    repo_root=root,
                    payload_path=payload_path,
                    payload_repository_path="payload.json",
                    approval_path=approval_path,
                    approval_repository_path="approval.json",
                    statement=statement,
                    now=datetime(2026, 8, 4, 12, 0, tzinfo=timezone.utc),
                )

    def test_execution_bundle_rejects_action_scope_drift_before_network(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "a.md"
            source.write_text("# A\n\nText\n", encoding="utf-8")
            values = [["x"]]
            payload = {
                "spreadsheet_id": "sheet-1",
                "service_account": "writer@example.iam.gserviceaccount.com",
                "format_policy": {"value_input_option": "RAW"},
                "tabs_digest": "d" * 64,
                "tabs": [{"artifact_stable_id": "TL-A", "source_path": "a.md", "source_sha256": sheet_sync.sha256_file(source), "tab_key": "TL_A", "tab_title": "TL_A", "schema": "TL-SHEET-001/0.1.3/TL_A/v2", "used_range": "A1:A1", "row_count": 1, "column_count": 1, "payload_sha256": sheet_sync.sha256_json(values), "values": values}],
            }
            payload_path = root / "payload.json"
            payload_path.write_text(json.dumps(payload), encoding="utf-8")
            scope = {"bound_payload_path": "payload.json", "bound_payload_sha256": sheet_sync.sha256_file(payload_path), "tab_scope": [{key: payload["tabs"][0][key] for key in ("artifact_stable_id", "source_path", "source_sha256", "tab_key", "tab_title", "schema", "used_range", "row_count", "column_count", "payload_sha256")}], "format_policy": payload["format_policy"]}
            approval = {"approval_bundle_id": "TL-SHEET-RUN2-14-V2", "approval_state": "DRAFT_UNSIGNED", "target_class": "TOPLINK_ONLY", "expires_at_ict": "2026-08-05T18:30:00+07:00", "spreadsheet_id": "sheet-1", "service_account": "writer@example.iam.gserviceaccount.com", "payload_binding": {"repository_path": "payload.json", "sha256": sheet_sync.sha256_file(payload_path), "tabs_digest": "d" * 64}, "approval_records": [{"phase": 1, "action": "CREATE_TAB", "limits": {"max_tabs": 99, "max_rows_per_tab": 1}, "authorized_agent": "Codex CLI", "expires_at_ict": "2026-08-05T18:30:00+07:00", "readback_required": True, "bound_scope": scope}, {"phase": 2, "action": "UPSERT", "limits": {"max_tabs": 0, "max_rows_per_tab": 1}, "authorized_agent": "Codex CLI", "expires_at_ict": "2026-08-05T18:30:00+07:00", "readback_required": True, "bound_scope": scope}, {"phase": 3, "action": "READBACK", "limits": {"max_tabs": 0, "max_rows_per_tab": 1}, "authorized_agent": "Codex CLI", "expires_at_ict": "2026-08-05T18:30:00+07:00", "readback_required": True, "bound_scope": scope}]}
            approval_path = root / "approval.json"
            approval_path.write_text(json.dumps(approval), encoding="utf-8")
            statement = f"APPROVED: TL-SHEET-RUN2-14-V2 at approval.json SHA-256 {sheet_sync.sha256_file(approval_path)}"

            with self.assertRaisesRegex(sheet_sync.SyncError, "approval scope mismatch"):
                sheet_sync.validate_execution_bundle(repo_root=root, payload_path=payload_path, payload_repository_path="payload.json", approval_path=approval_path, approval_repository_path="approval.json", statement=statement, now=datetime(2026, 8, 4, 12, 0, tzinfo=timezone.utc))


class ReadbackTests(unittest.TestCase):
    def test_normalizes_omitted_trailing_empty_cells_but_detects_value_drift(self) -> None:
        expected = [["a", "b", ""], ["c", "", ""]]
        actual = [["a", "b"], ["c"]]

        sheet_sync.assert_exact_readback(expected, actual, width=3)

        with self.assertRaisesRegex(sheet_sync.SyncError, "read-back mismatch"):
            sheet_sync.assert_exact_readback(expected, [["a", "x"], ["c"]], width=3)


if __name__ == "__main__":
    unittest.main()
