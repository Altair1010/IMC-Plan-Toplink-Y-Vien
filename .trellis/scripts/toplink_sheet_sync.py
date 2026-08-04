from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import unicodedata
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Sequence


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from common.io import read_json, write_json  # noqa: E402
from common.log import log_error, log_success  # noqa: E402
from common.paths import get_repo_root  # noqa: E402


EVIDENCE_STATES = (
    "TOPLINK_CONFIRMED",
    "INFERENCE",
    "HYPOTHESIS",
    "MISSING_INPUT",
    "UNVERIFIED",
    "DO_NOT_USE",
)
COMMON_HEADERS = [
    "stable_row_key",
    "record_id",
    "source_path",
    "source_id",
    "evidence_status",
    "allowed_use",
    "revision_or_digest",
    "owner",
    "updated_at_ict",
    "record_type",
    "section",
]
ICT = timezone(timedelta(hours=7))


class SyncError(RuntimeError):
    """A fail-closed validation or delivery error."""


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def ict_timestamp(value: datetime) -> str:
    return value.astimezone(ICT).isoformat()


def strip_markdown(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == "`":
        return value[1:-1]
    return value


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", strip_markdown(value))
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")
    return slug or "section"


def split_markdown_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [strip_markdown(cell.replace("\\|", "|")) for cell in line.split("|")]


def is_table_separator(line: str) -> bool:
    cells = split_markdown_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def evidence_status(values: Sequence[str]) -> str:
    joined = " ".join(values)
    for state in EVIDENCE_STATES:
        if re.search(rf"\b{re.escape(state)}\b", joined):
            return state
    return "UNVERIFIED"


def value_for_header(headers: Sequence[str], values: Sequence[str], names: set[str]) -> str | None:
    for index, header in enumerate(headers):
        if slugify(header) in names and index < len(values):
            return values[index] or None
    return None


def row_identity(headers: Sequence[str], values: Sequence[str], fallback: str) -> str:
    id_names = {
        "id",
        "stable-id",
        "kpi-id",
        "claim-id",
        "item-id",
        "asset-placeholder-id",
        "batch",
        "week",
        "rule",
        "field",
        "channel",
        "pillar",
        "tru",
    }
    explicit = value_for_header(headers, values, id_names)
    return slugify(explicit or fallback)


def compile_markdown(
    *,
    markdown: str,
    artifact_id: str,
    source_path: str,
    source_digest: str,
    prepared_at_ict: str,
) -> dict[str, Any]:
    lines = markdown.splitlines()
    values: list[list[str]] = [
        ["artifact_stable_id", artifact_id],
        ["source_path", source_path],
        ["source_sha256", source_digest],
        ["prepared_at_ict", prepared_at_ict],
        ["delivery_state", "LOCAL_VALIDATED · APPROVAL_PENDING"],
        ["human_approval", "NOT_GRANTED"],
        [],
    ]
    header_rows: list[int] = []
    section = "document"
    section_slug = "document"
    prose_ordinal = 0
    table_ordinal = 0
    prose_header_section: str | None = None
    used_keys: set[str] = set()
    index = 0

    def common_cells(stable_key: str, status: str, allowed_use: str, owner: str, record_type: str) -> list[str]:
        if stable_key in used_keys:
            raise SyncError(f"duplicate stable row key: {stable_key}")
        used_keys.add(stable_key)
        return [
            stable_key,
            artifact_id,
            source_path,
            artifact_id,
            status,
            allowed_use,
            source_digest,
            owner,
            prepared_at_ict,
            record_type,
            section,
        ]

    while index < len(lines):
        raw_line = lines[index]
        stripped = raw_line.strip()
        heading_match = re.match(r"^#{1,6}\s+(.+?)\s*$", stripped)
        if heading_match:
            section = strip_markdown(heading_match.group(1))
            section_slug = slugify(section)
            prose_header_section = None
            index += 1
            continue

        if (
            stripped.startswith("|")
            and index + 1 < len(lines)
            and is_table_separator(lines[index + 1])
        ):
            table_ordinal += 1
            headers = split_markdown_row(stripped)
            values.append(COMMON_HEADERS + headers)
            header_rows.append(len(values) - 1)
            index += 2
            row_ordinal = 0
            while index < len(lines) and lines[index].strip().startswith("|"):
                row_values = split_markdown_row(lines[index])
                row_ordinal += 1
                fallback = f"row-{row_ordinal:03d}"
                identity = row_identity(headers, row_values, fallback)
                stable_key = f"{artifact_id}/{section_slug}/table-{table_ordinal:02d}/{identity}"
                status = evidence_status(row_values)
                allowed_use = value_for_header(
                    headers, row_values, {"allowed-use", "allowed-use-status"}
                ) or "STAGING_ONLY"
                owner = value_for_header(headers, row_values, {"owner"}) or "MISSING_INPUT"
                values.append(common_cells(stable_key, status, allowed_use, owner, "TABLE") + row_values)
                index += 1
            values.append([])
            prose_header_section = None
            continue

        if stripped:
            prose_ordinal += 1
            if prose_header_section != section_slug:
                values.append(COMMON_HEADERS + ["text"])
                header_rows.append(len(values) - 1)
                prose_header_section = section_slug
            stable_key = f"{artifact_id}/{section_slug}/prose-{prose_ordinal:03d}"
            values.append(
                common_cells(
                    stable_key,
                    evidence_status([stripped]),
                    "STAGING_ONLY",
                    "MISSING_INPUT",
                    "PROSE",
                )
                + [stripped]
            )
        index += 1

    while values and not values[-1]:
        values.pop()
    width = max((len(row) for row in values), default=1)
    padded = [row + [""] * (width - len(row)) for row in values]
    result = {
        "values": padded,
        "row_count": len(padded),
        "column_count": width,
        "header_row_indexes": header_rows,
    }
    result["payload_sha256"] = sha256_json(result["values"])
    return result


def validate_mapping(mapping: Sequence[dict[str, Any]]) -> None:
    seen_ids: set[str] = set()
    seen_tabs: set[str] = set()
    seen_paths: set[str] = set()
    for item in mapping:
        stable_id = str(item.get("stable_id", ""))
        tab_key = str(item.get("tab_key", ""))
        path = str(item.get("path", ""))
        if stable_id in seen_ids:
            raise SyncError(f"duplicate stable_id: {stable_id}")
        if tab_key in seen_tabs:
            raise SyncError(f"duplicate tab_key: {tab_key}")
        if path in seen_paths:
            raise SyncError(f"duplicate source path: {path}")
        seen_ids.add(stable_id)
        seen_tabs.add(tab_key)
        seen_paths.add(path)


def parse_ict(value: str) -> datetime:
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        raise SyncError("approval expiry must include timezone")
    return parsed


def validate_approval_statement(
    *,
    statement: str,
    approval_path: Path,
    repository_path: str,
    now: datetime,
) -> None:
    approval = read_json(approval_path)
    if not approval:
        raise SyncError(f"invalid approval envelope: {repository_path}")
    bundle_id = str(approval.get("approval_bundle_id", ""))
    digest = sha256_file(approval_path)
    expected = f"APPROVED: {bundle_id} at {repository_path} SHA-256 {digest}"
    if statement.strip() != expected:
        raise SyncError("approval statement mismatch")
    expiry = parse_ict(str(approval.get("expires_at_ict", "")))
    if now.astimezone(expiry.tzinfo) >= expiry:
        raise SyncError("approval expired")


def normalize_matrix(values: Sequence[Sequence[Any]], width: int, height: int) -> list[list[str]]:
    normalized: list[list[str]] = []
    for row_index in range(height):
        source = list(values[row_index]) if row_index < len(values) else []
        row = ["" if value is None else str(value) for value in source[:width]]
        normalized.append(row + [""] * (width - len(row)))
    return normalized


def assert_exact_readback(
    expected: Sequence[Sequence[Any]],
    actual: Sequence[Sequence[Any]],
    *,
    width: int,
) -> None:
    expected_normalized = normalize_matrix(expected, width, len(expected))
    actual_normalized = normalize_matrix(actual, width, len(expected))
    if expected_normalized != actual_normalized or len(actual) > len(expected):
        raise SyncError("read-back mismatch")


def column_name(column_count: int) -> str:
    if column_count < 1:
        raise SyncError("column count must be positive")
    result = ""
    value = column_count
    while value:
        value, remainder = divmod(value - 1, 26)
        result = chr(65 + remainder) + result
    return result


def build_payload(
    *,
    repo_root: Path,
    registry: dict[str, Any],
    prepared_at_ict: str,
    expected_count: int = 14,
) -> dict[str, Any]:
    if registry.get("approval_bundle_id") != "TL-SHEET-RUN2-14-V1":
        raise SyncError("unexpected source approval bundle")
    scope = registry.get("common_scope")
    if not isinstance(scope, dict) or not isinstance(scope.get("mapping"), list):
        raise SyncError("registry mapping missing")
    mapping = scope["mapping"]
    if len(mapping) != expected_count:
        raise SyncError(f"expected {expected_count} mappings, found {len(mapping)}")
    validate_mapping(mapping)

    tabs: list[dict[str, Any]] = []
    for item in mapping:
        relative_path = str(item["path"])
        source_path = repo_root / Path(relative_path)
        if not source_path.is_file():
            raise SyncError(f"source missing: {relative_path}")
        actual_digest = sha256_file(source_path)
        expected_digest = str(item["sha256"])
        if actual_digest != expected_digest:
            raise SyncError(f"source hash drift: {relative_path}")
        compiled = compile_markdown(
            markdown=source_path.read_text(encoding="utf-8"),
            artifact_id=str(item["stable_id"]),
            source_path=relative_path.replace("\\", "/"),
            source_digest=actual_digest,
            prepared_at_ict=prepared_at_ict,
        )
        tab_key = str(item["tab_key"])
        if "_v2" in tab_key.lower() or "thao" in slugify(tab_key):
            raise SyncError(f"prohibited tab identity: {tab_key}")
        tabs.append(
            {
                "artifact_stable_id": str(item["stable_id"]),
                "source_path": relative_path.replace("\\", "/"),
                "source_sha256": actual_digest,
                "tab_key": tab_key,
                "tab_title": tab_key,
                "schema": f"TL-SHEET-001/0.1.3/{tab_key}/v2",
                "used_range": f"A1:{column_name(compiled['column_count'])}{compiled['row_count']}",
                **compiled,
            }
        )

    payload: dict[str, Any] = {
        "contract_id": "TL-SHEET-001",
        "contract_version": "0.1.3",
        "payload_id": "TL-SHEET-RUN2-14-PAYLOAD-V2",
        "prepared_at_ict": prepared_at_ict,
        "spreadsheet_id": str(registry.get("spreadsheet_id", "")),
        "preserve_existing_tabs": list(
            registry.get("metadata_read_result", {}).get("preserve_existing_tabs", [])
        ),
        "service_account": str(registry.get("auth_readiness", {}).get("service_account", "")),
        "input_manifest": dict(registry.get("input_manifest", {})),
        "format_policy": {
            "value_input_option": "RAW",
            "wrap_used_range": True,
            "bold_header_rows": True,
            "freeze_metadata_rows": 7,
            "default_column_width_px": 180,
        },
        "tabs": tabs,
        "external_writes": 0,
    }
    payload["tabs_digest"] = sha256_json(
        [
            {
                "tab_key": tab["tab_key"],
                "used_range": tab["used_range"],
                "payload_sha256": tab["payload_sha256"],
            }
            for tab in tabs
        ]
    )
    return payload


def build_approval_envelope(
    *,
    payload: dict[str, Any],
    payload_repository_path: str,
    payload_file_sha256: str,
    prepared_at_ict: str,
    expires_at_ict: str,
) -> dict[str, Any]:
    parse_ict(prepared_at_ict)
    expiry = parse_ict(expires_at_ict)
    if expiry <= parse_ict(prepared_at_ict):
        raise SyncError("approval expiry must be after preparation")
    tabs = payload.get("tabs")
    if not isinstance(tabs, list) or not tabs:
        raise SyncError("payload tabs missing")
    tab_scope = [
        {
            key: tab[key]
            for key in (
                "artifact_stable_id",
                "source_path",
                "source_sha256",
                "tab_key",
                "tab_title",
                "schema",
                "used_range",
                "row_count",
                "column_count",
                "payload_sha256",
            )
        }
        for tab in tabs
    ]
    max_rows = max(int(tab["row_count"]) for tab in tabs)
    common = {
        "bound_payload_path": payload_repository_path,
        "bound_payload_sha256": payload_file_sha256,
        "tab_scope": tab_scope,
        "format_policy": payload["format_policy"],
    }
    envelope = {
        "contract_id": "TL-SHEET-001",
        "contract_version": "0.1.3",
        "approval_bundle_id": "TL-SHEET-RUN2-14-V2",
        "approval_state": "DRAFT_UNSIGNED",
        "supersedes_unsigned_bundle": "TL-SHEET-RUN2-14-V1",
        "prepared_at_ict": prepared_at_ict,
        "expires_at_ict": expires_at_ict,
        "spreadsheet_id": payload["spreadsheet_id"],
        "target_class": "TOPLINK_ONLY",
        "service_account": payload["service_account"],
        "preserve_existing_tabs": payload["preserve_existing_tabs"],
        "payload_binding": {
            "repository_path": payload_repository_path,
            "sha256": payload_file_sha256,
            "tabs_digest": payload["tabs_digest"],
        },
        "approval_records": [
            {
                "phase": 1,
                "action": "CREATE_TAB",
                "limits": {"max_tabs": len(tabs), "max_rows_per_tab": max_rows},
                "authorized_agent": "Codex CLI",
                "expires_at_ict": expires_at_ict,
                "readback_required": True,
                "bound_scope": common,
                "postcondition": "exact registered tab titles exist; preserved tabs unchanged",
            },
            {
                "phase": 2,
                "action": "UPSERT",
                "limits": {"max_tabs": 0, "max_rows_per_tab": max_rows},
                "authorized_agent": "Codex CLI",
                "expires_at_ict": expires_at_ict,
                "readback_required": True,
                "bound_scope": common,
                "postcondition": "exact payload cells written only inside approved used ranges",
            },
            {
                "phase": 3,
                "action": "READBACK",
                "limits": {"max_tabs": 0, "max_rows_per_tab": max_rows},
                "authorized_agent": "Codex CLI",
                "expires_at_ict": expires_at_ict,
                "readback_required": True,
                "bound_scope": common,
                "postcondition": "14 tab matrices, stable IDs, Unicode, row counts, and gate fields match",
            },
        ],
        "signature": {
            "required_statement": "APPROVED: TL-SHEET-RUN2-14-V2 at <repository path> SHA-256 <digest>",
            "signer": "minhkhang.guru",
            "signed_at_ict": None,
        },
        "external_writes": 0,
    }
    return envelope


def validate_execution_bundle(
    *,
    repo_root: Path,
    payload_path: Path,
    payload_repository_path: str,
    approval_path: Path,
    approval_repository_path: str,
    statement: str,
    now: datetime,
) -> tuple[dict[str, Any], dict[str, Any]]:
    validate_approval_statement(
        statement=statement,
        approval_path=approval_path,
        repository_path=approval_repository_path,
        now=now,
    )
    payload = read_json(payload_path)
    approval = read_json(approval_path)
    if not payload or not approval:
        raise SyncError("payload or approval JSON invalid")
    binding = approval.get("payload_binding")
    if not isinstance(binding, dict):
        raise SyncError("approval payload binding missing")
    if binding.get("repository_path") != payload_repository_path:
        raise SyncError("payload repository path mismatch")
    if binding.get("sha256") != sha256_file(payload_path):
        raise SyncError("payload file digest mismatch")
    if binding.get("tabs_digest") != payload.get("tabs_digest"):
        raise SyncError("tab digest mismatch")
    if approval.get("approval_bundle_id") != "TL-SHEET-RUN2-14-V2":
        raise SyncError("unexpected approval bundle")
    if approval.get("approval_state") != "DRAFT_UNSIGNED":
        raise SyncError("approval state is not an unsigned V2 draft")
    if approval.get("target_class") != "TOPLINK_ONLY":
        raise SyncError("approval target is not Toplink-only")
    for field in ("spreadsheet_id", "service_account"):
        if approval.get(field) != payload.get(field):
            raise SyncError(f"{field} mismatch")
    if not isinstance(payload.get("spreadsheet_id"), str) or not payload["spreadsheet_id"]:
        raise SyncError("payload spreadsheet ID missing")
    if not isinstance(payload.get("service_account"), str) or not payload["service_account"].endswith(
        ".iam.gserviceaccount.com"
    ):
        raise SyncError("payload service-account identity invalid")
    records = approval.get("approval_records")
    if not isinstance(records, list):
        raise SyncError("approval records missing")
    actions = [record.get("action") for record in records if isinstance(record, dict)]
    if actions != ["CREATE_TAB", "UPSERT", "READBACK"]:
        raise SyncError("approval action sequence mismatch")
    tabs = payload.get("tabs")
    if not isinstance(tabs, list) or not tabs:
        raise SyncError("payload tabs missing")
    seen_tabs: set[str] = set()
    expected_scope: list[dict[str, Any]] = []
    for tab in tabs:
        if not isinstance(tab, dict):
            raise SyncError("invalid payload tab")
        title = tab.get("tab_title")
        if not isinstance(title, str) or not re.fullmatch(r"TL_[A-Z0-9_]+", title):
            raise SyncError("invalid Toplink tab title")
        if title in seen_tabs or tab.get("tab_key") != title:
            raise SyncError("duplicate or mismatched tab identity")
        seen_tabs.add(title)
        row_count = tab.get("row_count")
        column_count = tab.get("column_count")
        if not isinstance(row_count, int) or not isinstance(column_count, int) or row_count < 1 or column_count < 1:
            raise SyncError(f"invalid tab dimensions: {title}")
        if tab.get("used_range") != f"A1:{column_name(column_count)}{row_count}":
            raise SyncError(f"tab range mismatch: {title}")
        if tab.get("schema") != f"TL-SHEET-001/0.1.3/{title}/v2":
            raise SyncError(f"tab schema mismatch: {title}")
        values = tab.get("values")
        if not isinstance(values, list) or len(values) != row_count or any(
            not isinstance(row, list) or len(row) != column_count or any(not isinstance(value, str) for value in row)
            for row in values
        ):
            raise SyncError(f"tab matrix mismatch: {title}")
        source_relative = str(tab.get("source_path", ""))
        source = (repo_root / Path(source_relative)).resolve()
        try:
            source.relative_to(repo_root.resolve())
        except ValueError as exc:
            raise SyncError(f"source path escapes repository: {source_relative}") from exc
        if not source.is_file() or sha256_file(source) != tab.get("source_sha256"):
            raise SyncError(f"source hash drift: {source_relative}")
        if sha256_json(values) != tab.get("payload_sha256"):
            raise SyncError(f"tab payload digest mismatch: {tab.get('tab_key', source_relative)}")
        expected_scope.append(
            {
                key: tab[key]
                for key in (
                    "artifact_stable_id", "source_path", "source_sha256", "tab_key", "tab_title",
                    "schema", "used_range", "row_count", "column_count", "payload_sha256",
                )
            }
        )
    max_rows = max(tab["row_count"] for tab in tabs)
    expected_common = {
        "bound_payload_path": payload_repository_path,
        "bound_payload_sha256": sha256_file(payload_path),
        "tab_scope": expected_scope,
        "format_policy": payload.get("format_policy"),
    }
    expected_limits = [
        {"max_tabs": len(tabs), "max_rows_per_tab": max_rows},
        {"max_tabs": 0, "max_rows_per_tab": max_rows},
        {"max_tabs": 0, "max_rows_per_tab": max_rows},
    ]
    for phase, (record, limits) in enumerate(zip(records, expected_limits), start=1):
        if not isinstance(record, dict) or record.get("phase") != phase:
            raise SyncError("approval phase sequence mismatch")
        if record.get("authorized_agent") != "Codex CLI" or record.get("readback_required") is not True:
            raise SyncError("approval operator or read-back requirement mismatch")
        if record.get("expires_at_ict") != approval.get("expires_at_ict"):
            raise SyncError("approval record expiry mismatch")
        if record.get("limits") != limits or record.get("bound_scope") != expected_common:
            raise SyncError("approval scope mismatch")
    return payload, approval


def quote_tab(title: str) -> str:
    return "'" + title.replace("'", "''") + "'"


def metadata_by_title(metadata: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for sheet in metadata.get("sheets", []):
        properties = sheet.get("properties", {})
        title = properties.get("title")
        if isinstance(title, str):
            result[title] = properties
    return result


def format_requests(tab: dict[str, Any], sheet_id: int) -> list[dict[str, Any]]:
    row_count = int(tab["row_count"])
    column_count = int(tab["column_count"])
    requests: list[dict[str, Any]] = [
        {
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": 0,
                    "endRowIndex": row_count,
                    "startColumnIndex": 0,
                    "endColumnIndex": column_count,
                },
                "cell": {"userEnteredFormat": {"wrapStrategy": "WRAP"}},
                "fields": "userEnteredFormat.wrapStrategy",
            }
        },
        {
            "updateSheetProperties": {
                "properties": {
                    "sheetId": sheet_id,
                    "gridProperties": {"frozenRowCount": 7},
                },
                "fields": "gridProperties.frozenRowCount",
            }
        },
        {
            "updateDimensionProperties": {
                "range": {
                    "sheetId": sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": 0,
                    "endIndex": column_count,
                },
                "properties": {"pixelSize": 180},
                "fields": "pixelSize",
            }
        },
    ]
    for row_index in tab.get("header_row_indexes", []):
        requests.append(
            {
                "repeatCell": {
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": int(row_index),
                        "endRowIndex": int(row_index) + 1,
                        "startColumnIndex": 0,
                        "endColumnIndex": column_count,
                    },
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColorStyle": {
                                "rgbColor": {"red": 0.92, "green": 0.92, "blue": 0.92}
                            },
                            "textFormat": {"bold": True},
                        }
                    },
                    "fields": "userEnteredFormat(backgroundColorStyle,textFormat.bold)",
                }
            }
        )
    return requests


def execute_sync(
    *,
    repo_root: Path,
    payload_path: Path,
    payload_repository_path: str,
    approval_path: Path,
    approval_repository_path: str,
    approval_statement: str,
    readback_path: Path,
    now: datetime,
) -> dict[str, Any]:
    payload, approval = validate_execution_bundle(
        repo_root=repo_root,
        payload_path=payload_path,
        payload_repository_path=payload_repository_path,
        approval_path=approval_path,
        approval_repository_path=approval_repository_path,
        statement=approval_statement,
        now=now,
    )
    credential_value = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not credential_value:
        raise SyncError("GOOGLE_APPLICATION_CREDENTIALS is not bound")
    credential_path = Path(credential_value)
    credential = read_json(credential_path)
    if not credential or credential.get("client_email") != payload.get("service_account"):
        raise SyncError("service-account identity mismatch")

    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
    except ImportError as exc:
        raise SyncError("Google Sheets runtime dependencies unavailable") from exc

    credentials = service_account.Credentials.from_service_account_file(
        str(credential_path),
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    service = build("sheets", "v4", credentials=credentials, cache_discovery=False)
    spreadsheet_id = str(payload["spreadsheet_id"])
    evidence: dict[str, Any] = {
        "record_id": "TL-SHEET-RUN2-14-READBACK-V2",
        "spreadsheet_id": spreadsheet_id,
        "approval_bundle_id": approval["approval_bundle_id"],
        "approval_sha256": sha256_file(approval_path),
        "payload_sha256": sha256_file(payload_path),
        "started_at_ict": ict_timestamp(now),
        "service_account": payload["service_account"],
        "phases": [],
        "tabs": [],
        "final_status": "SYNC_WRITTEN_UNVERIFIED",
    }

    def persist() -> None:
        if not write_json(readback_path, evidence):
            raise SyncError(f"unable to persist read-back evidence: {readback_path}")

    try:
        metadata = (
            service.spreadsheets()
            .get(
                spreadsheetId=spreadsheet_id,
                fields="spreadsheetId,sheets.properties(sheetId,title,gridProperties)",
            )
            .execute()
        )
        if metadata.get("spreadsheetId") != spreadsheet_id:
            raise SyncError("target spreadsheet read-back mismatch")
        current = metadata_by_title(metadata)
        preserved = set(payload.get("preserve_existing_tabs", []))
        if set(current) != preserved:
            raise SyncError("target tab set drifted before CREATE_TAB")

        create_requests = [
            {
                "addSheet": {
                    "properties": {
                        "title": tab["tab_title"],
                        "gridProperties": {
                            "rowCount": max(100, int(tab["row_count"])),
                            "columnCount": max(26, int(tab["column_count"])),
                        },
                    }
                }
            }
            for tab in payload["tabs"]
        ]
        service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={"requests": create_requests},
        ).execute()
        metadata = (
            service.spreadsheets()
            .get(
                spreadsheetId=spreadsheet_id,
                fields="spreadsheetId,sheets.properties(sheetId,title,gridProperties)",
            )
            .execute()
        )
        current = metadata_by_title(metadata)
        expected_titles = preserved | {tab["tab_title"] for tab in payload["tabs"]}
        if set(current) != expected_titles:
            raise SyncError("CREATE_TAB exact title read-back failed")
        evidence["phases"].append({"action": "CREATE_TAB", "status": "PASS", "tab_count": len(payload["tabs"])})
        persist()

        for tab in payload["tabs"]:
            title = tab["tab_title"]
            a1_range = f"{quote_tab(title)}!{tab['used_range']}"
            service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id,
                range=a1_range,
                valueInputOption="RAW",
                body={"majorDimension": "ROWS", "values": tab["values"]},
            ).execute()
            actual = (
                service.spreadsheets()
                .values()
                .get(
                    spreadsheetId=spreadsheet_id,
                    range=a1_range,
                    valueRenderOption="UNFORMATTED_VALUE",
                    dateTimeRenderOption="FORMATTED_STRING",
                )
                .execute()
                .get("values", [])
            )
            assert_exact_readback(tab["values"], actual, width=int(tab["column_count"]))
            sheet_id = int(current[title]["sheetId"])
            service.spreadsheets().batchUpdate(
                spreadsheetId=spreadsheet_id,
                body={"requests": format_requests(tab, sheet_id)},
            ).execute()
            evidence["tabs"].append(
                {
                    "artifact_stable_id": tab["artifact_stable_id"],
                    "tab_key": tab["tab_key"],
                    "sheet_id": sheet_id,
                    "used_range": tab["used_range"],
                    "row_count": tab["row_count"],
                    "column_count": tab["column_count"],
                    "payload_sha256": tab["payload_sha256"],
                    "readback_sha256": sha256_json(normalize_matrix(actual, int(tab["column_count"]), int(tab["row_count"]))),
                    "status": "PASS",
                }
            )
            persist()

        evidence["phases"].append({"action": "UPSERT", "status": "PASS", "tab_count": len(payload["tabs"])})
        final_metadata = (
            service.spreadsheets()
            .get(
                spreadsheetId=spreadsheet_id,
                fields="spreadsheetId,sheets.properties(sheetId,title,gridProperties(frozenRowCount,rowCount,columnCount))",
            )
            .execute()
        )
        final_titles = metadata_by_title(final_metadata)
        if set(final_titles) != expected_titles:
            raise SyncError("final target tab set mismatch")
        for tab in payload["tabs"]:
            properties = final_titles[tab["tab_title"]]
            if int(properties.get("gridProperties", {}).get("frozenRowCount", 0)) != 7:
                raise SyncError(f"format read-back failed: {tab['tab_title']}")
        evidence["phases"].append({"action": "READBACK", "status": "PASS", "tab_count": len(payload["tabs"])})
        evidence["verified_at_ict"] = ict_timestamp(datetime.now(ICT))
        evidence["final_status"] = "SYNC_READBACK_PASS"
        persist()
        return evidence
    except Exception as exc:
        evidence["failed_at_ict"] = ict_timestamp(datetime.now(ICT))
        evidence["final_status"] = "VERIFY_FAILED"
        evidence["failure"] = type(exc).__name__ + ": " + str(exc)
        persist()
        if isinstance(exc, SyncError):
            raise
        raise SyncError("Google Sheets execution failed; see bounded read-back evidence") from exc


def default_paths(repo_root: Path) -> dict[str, Path]:
    base = repo_root / "docs Toplink" / "staging" / "run2" / "codex"
    return {
        "registry": base / "60-sheet-target-approval-draft.json",
        "payload": base / "61-sheet-payload-v2.json",
        "approval": base / "62-sheet-target-approval-v2.json",
        "readback": base / "63-sheet-readback-v2.json",
    }


def repository_path(repo_root: Path, path: Path) -> str:
    return path.resolve().relative_to(repo_root.resolve()).as_posix()


def compile_command(args: argparse.Namespace) -> int:
    repo_root = get_repo_root()
    paths = default_paths(repo_root)
    registry = read_json(paths["registry"])
    if not registry:
        raise SyncError(f"invalid registry: {repository_path(repo_root, paths['registry'])}")
    prepared_at = args.prepared_at or datetime.now().astimezone().replace(microsecond=0).isoformat()
    expires_at = args.expires_at or (
        parse_ict(prepared_at) + timedelta(hours=24)
    ).isoformat()
    payload = build_payload(
        repo_root=repo_root,
        registry=registry,
        prepared_at_ict=prepared_at,
    )
    if not write_json(paths["payload"], payload):
        raise SyncError("unable to write payload")
    payload_repo_path = repository_path(repo_root, paths["payload"])
    approval = build_approval_envelope(
        payload=payload,
        payload_repository_path=payload_repo_path,
        payload_file_sha256=sha256_file(paths["payload"]),
        prepared_at_ict=prepared_at,
        expires_at_ict=expires_at,
    )
    if not write_json(paths["approval"], approval):
        raise SyncError("unable to write approval envelope")
    approval_repo_path = repository_path(repo_root, paths["approval"])
    digest = sha256_file(paths["approval"])
    log_success(f"Compiled and locally validated {len(payload['tabs'])} tabs; external_writes=0")
    print(f"APPROVED: {approval['approval_bundle_id']} at {approval_repo_path} SHA-256 {digest}")
    return 0


def execute_command(args: argparse.Namespace) -> int:
    repo_root = get_repo_root()
    paths = default_paths(repo_root)
    execute_sync(
        repo_root=repo_root,
        payload_path=paths["payload"],
        payload_repository_path=repository_path(repo_root, paths["payload"]),
        approval_path=paths["approval"],
        approval_repository_path=repository_path(repo_root, paths["approval"]),
        approval_statement=args.approval_statement,
        readback_path=paths["readback"],
        now=datetime.now(timezone.utc),
    )
    log_success("Google Sheet exact read-back PASS")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fail-closed Toplink Google Sheet sync")
    subparsers = parser.add_subparsers(dest="command", required=True)
    compile_parser = subparsers.add_parser("compile", help="build local V2 payload and approval draft")
    compile_parser.add_argument("--prepared-at")
    compile_parser.add_argument("--expires-at")
    compile_parser.set_defaults(handler=compile_command)
    execute_parser = subparsers.add_parser("execute", help="run the signed CREATE_TAB/UPSERT/READBACK bundle")
    execute_parser.add_argument("--approval-statement", required=True)
    execute_parser.set_defaults(handler=execute_command)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    try:
        args = build_parser().parse_args(argv)
        return int(args.handler(args))
    except SyncError as exc:
        log_error(str(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
