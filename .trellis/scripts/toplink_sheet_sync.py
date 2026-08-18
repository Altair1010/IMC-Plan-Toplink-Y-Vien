from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence


TARGET_SPREADSHEET_ID = "1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms"
TARGET_SERVICE_ACCOUNT = "yvien-sheet-writer@imcforyvien.iam.gserviceaccount.com"
REGISTRY_PATH = Path("docs/system/yvien-sheet-dataset-registry.json")
CORRECTION_DIR = Path("docs Toplink/staging/run2/correction")
YV_P27_DIR = Path("staging/yv-humanize/p2.7-p2.8")
YV_P26_EXECUTION_SHA256 = "fbfc22b096183ff651b2b87b3d324ed189fed3b97ae430cc0d09c9ec363ca610"
YV_P26_READBACK_SHA256 = "7b5d5be579cb673e06f86160a1d3f402a4ce4da2a25cee1af6c5ede21cdf15f5"
YV_P27_PLAN_SHA256 = "b7117fbac5614fe9ea777eba51a71012d0cfe3070bcfa3da98197c4cd102ac21"
YV_P27_APPROVAL_SHA256 = {
    "P2_7_LEDGER_UPSERT": "52542f39ddef6048d5e9169e546ee0085f38571f2c113d28d0888c995cbc264f",
    "P2_7_LEDGER_READBACK": "e8c5df7e50f9788ab4a926fd3732ee2e22594dcf2dd66606361039758af6acb5",
}
YV_P3_APPROVAL_SHA256 = "d92c9fb12ae960aa895c140a90273501df4876840a1103a803f37e0a03a47fca"
YV_LIVE_WORKBOOK_SHA256 = "f5a373b814c5995592514b0eea670e8c1540ad4ed8bdcb769a6f8d2365f5a585"
YV_LIVE_STATE_SHA256 = "e444b6e52cc82f78fec7f7c7423b225e5d550006b3c5d8546700f03522e4be9a"
YV_LIVE_STATE_JSON_SHA256 = "9ae25485c682f4200149090d1d97c0f33782414e510c9cfa25a08305c7798e5e"
REPOSITORY_BINDING_PATHS = {
    "registry_sha256": REGISTRY_PATH,
    "run1_manifest_sha256": Path("docs Toplink/staging/run1/run1-manifest.json"),
    "run2_manifest_sha256": Path("docs Toplink/staging/run2/run2-manifest.json"),
    "v2_payload_sha256": Path("docs Toplink/staging/run2/codex/61-sheet-payload-v2.json"),
    "v2_readback_sha256": Path("docs Toplink/staging/run2/codex/63-sheet-readback-v2.json"),
}
YV_P3_REPOSITORY_BINDINGS = {
    "registry_sha256": "fddae345806dc0f5619440a38fb506baad5e49f0241c90f634742361312364c3",
    "run1_manifest_sha256": "99227153de577887966ae09124fdabcb2b3bf8ff23d838503531be507c2f4d2d",
    "run2_manifest_sha256": "50756122e25ff0cdd9e57b7ff313e881b586b0c3af338ee6a742ec0f2c72c712",
    "v2_payload_sha256": "64e9c656bee240951e41f9c4ad172d24059af0f13f0438f762d4f0c0ba4267b3",
    "v2_readback_sha256": "be0e0efca02f3a7d5cba09cc404d3dba02ecc77a268d57de8b4d43d824caa719",
}
COMMON_COLUMNS = [
    "stable_row_key",
    "record_id",
    "source_path",
    "source_location",
    "source_id",
    "evidence_status",
    "allowed_use",
    "revision",
    "source_digest",
    "owner",
    "updated_at_ict",
]
TAB_KEYS = (
    "report",
    "00_Y_VIEN_CAN_CHOT",
    "00_CONTROL",
    "01_SOURCE_INVENTORY",
    "02_INPUT_GAPS",
    "03_OUTPUT_INDEX",
    "04_DECISIONS",
    "05_KPI_DICTIONARY",
    "06_COMPLIANCE_RULES",
    "YV_01_brand_profile",
    "YV_02_audience",
    "YV_03_positioning",
    "YV_04_narrative",
    "YV_05_content_pillars",
    "YV_06_page_strategy",
    "YV_07_campaign",
    "YV_08_experiments",
    "YV_09_content_calendar",
    "YV_10_production_briefs",
    "YV_11_asset_batch_plan",
    "YV_12_workflow_approval",
)
ARTIFACT_DATASETS = {
    "TL-BRAND-PROFILE-001": ["TL_BRAND_PROFILE"],
    "TL-RUNTIME-COMPAT-001": ["TL_RUNTIME_COMPATIBILITY", "TL_CONTROL"],
    "TL-AUDIENCE-001": ["TL_AUDIENCE_HYPOTHESES"],
    "TL-POSITIONING-001": ["TL_POSITIONING", "TL_COMPLIANCE_RULES"],
    "TL-NARRATIVE-001": ["TL_NARRATIVE"],
    "TL-PILLARS-001": ["TL_CONTENT_PILLARS"],
    "TL-PAGE-STRATEGY-001": ["TL_FACEBOOK_STRATEGY", "TL_PAGE_BENCHMARK"],
    "TL-CAMPAIGN-001": ["TL_CAMPAIGN", "TL_EXPERIMENTS"],
    "TL-KPI-001": ["TL_KPI_DICTIONARY", "TL_EXPERIMENTS"],
    "TL-M5-CALENDAR-001": ["TL_CONTENT_CALENDAR", "TL_WORKFLOW_APPROVAL"],
    "TL-M5-ASSET-001": ["TL_ASSET_BATCH_PLAN"],
    "TL-M5-REELS-001": ["TL_REELS_BRIEFS", "TL_PRODUCTION_BRIEFS"],
    "TL-M5-PRODBRIEF-001": ["TL_PRODUCTION_BRIEFS", "TL_WORKFLOW_APPROVAL"],
    "TL-M5-WORKFLOW-001": ["TL_WORKFLOW_APPROVAL", "TL_COMPLIANCE_RULES", "TL_REPORT"],
}


class SyncError(RuntimeError):
    pass


def canonical_json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def sha256_v2_values(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def normalize_matrix(values: Sequence[Sequence[Any]], width: int, height: int) -> list[list[Any]]:
    normalized: list[list[Any]] = []
    for row_index in range(height):
        source_row = list(values[row_index]) if row_index < len(values) else []
        normalized.append((source_row + [""] * width)[:width])
    return normalized


def snapshot_values_digest(values: Sequence[Sequence[Any]], used_range: str) -> str:
    _, _, height, width = _parse_range(used_range)
    return sha256_v2_values(normalize_matrix(values, width=width, height=height))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SyncError(f"unable to read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SyncError(f"JSON object required: {path}")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(canonical_json_bytes(value))
    temporary.replace(path)


def load_registry(repo_root: Path) -> dict[str, Any]:
    registry = read_json(repo_root / REGISTRY_PATH)
    validate_registry(registry)
    return registry


def validate_registry(registry: dict[str, Any]) -> None:
    if registry.get("schema_version") != "YV-SHEET-001/1.0.0":
        raise SyncError("registry schema version drift")
    tabs = registry.get("tabs")
    if not isinstance(tabs, list) or [tab.get("tab") for tab in sorted(tabs, key=lambda item: item.get("index", -1))] != list(TAB_KEYS):
        raise SyncError("registry must contain the exact ordered 21 tab keys")
    for tab in tabs:
        hidden = tab.get("hidden_columns")
        if not isinstance(hidden, list) or [item.get("header") for item in hidden] != ["_key", "_audit"] or [item.get("field") for item in hidden] != ["stable_row_key", "_audit"] or not all(item.get("hidden_by_user") is True for item in hidden):
            raise SyncError(f"hidden column contract drift: {tab.get('tab')}")


def _strip_cell(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value.startswith("`") and value.endswith("`"):
        value = value[1:-1]
    return value.replace("<br>", " · ").strip()


def parse_markdown_tables(path: Path) -> list[dict[str, Any]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    tables: list[dict[str, Any]] = []
    index = 0
    while index < len(lines) - 1:
        if lines[index].lstrip().startswith("|") and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[index + 1]):
            headers = [_strip_cell(cell) for cell in lines[index].strip().strip("|").split("|")]
            rows: list[dict[str, Any]] = []
            cursor = index + 2
            while cursor < len(lines) and lines[cursor].lstrip().startswith("|"):
                values = [_strip_cell(cell) for cell in lines[cursor].strip().strip("|").split("|")]
                values = (values + [""] * len(headers))[: len(headers)]
                rows.append({"values": values, "location": f"line {cursor + 1}"})
                cursor += 1
            tables.append({"headers": headers, "rows": rows, "location": f"line {index + 1}"})
            index = cursor
        else:
            index += 1
    return tables


def _manifest_outputs(repo_root: Path) -> list[dict[str, str]]:
    manifest = read_json(repo_root / "docs Toplink/staging/run2/run2-manifest.json")
    outputs = manifest.get("generated_outputs")
    if not isinstance(outputs, list) or len(outputs) != 14:
        raise SyncError("Run 2 manifest must contain 14 generated outputs")
    normalized: list[dict[str, str]] = []
    for item in outputs:
        stable_id = str(item.get("stable_id", ""))
        path = str(item.get("path", ""))
        digest = str(item.get("sha256", ""))
        if stable_id not in ARTIFACT_DATASETS or not path or len(digest) != 64:
            raise SyncError(f"invalid generated output: {stable_id}")
        absolute = repo_root / path
        if sha256_file(absolute) != digest:
            raise SyncError(f"source digest drift: {path}")
        normalized.append({"stable_id": stable_id, "path": path, "sha256": digest})
    return normalized


def _source(repo_root: Path, outputs: list[dict[str, str]], stable_id: str) -> dict[str, str]:
    try:
        return next(item for item in outputs if item["stable_id"] == stable_id)
    except StopIteration as exc:
        raise SyncError(f"source artifact missing: {stable_id}") from exc


def _file_source(repo_root: Path, path: str, source_id: str) -> dict[str, str]:
    absolute = repo_root / path
    return {"stable_id": source_id, "path": path, "sha256": sha256_file(absolute)}


def _record(
    dataset: str,
    identity: str,
    source: dict[str, str],
    location: str,
    updated_at: str,
    fields: dict[str, Any],
    evidence_status: str = "TOPLINK_CONFIRMED",
    allowed_use: str = "INTERNAL_ONLY",
    owner: str = "Toplink human owner",
) -> dict[str, str]:
    record: dict[str, str] = {
        "stable_row_key": f"{dataset}/{identity}",
        "record_id": identity,
        "source_path": source["path"],
        "source_location": location,
        "source_id": source["stable_id"],
        "evidence_status": evidence_status,
        "allowed_use": allowed_use,
        "revision": "1",
        "source_digest": source["sha256"],
        "owner": owner,
        "updated_at_ict": updated_at,
    }
    record.update({key: "NOT_AVAILABLE" if value is None else str(value) for key, value in fields.items()})
    return record


def _id_refs(value: str, pattern: str) -> str:
    matches = list(dict.fromkeys(re.findall(pattern, value)))
    return ",".join(matches) if matches else "NOT_AVAILABLE"


def _content_refs(value: str) -> str:
    days = list(dict.fromkeys(re.findall(r"D-?(\d{1,2})", value, flags=re.IGNORECASE)))
    return ",".join(f"TL-M5-CAL-D{int(day):02d}-A" for day in days) if days else "NOT_AVAILABLE"


def _kpi_refs(value: str) -> str:
    numbers = list(dict.fromkeys(re.findall(r"\b(\d{1,2})\b", value)))
    return ",".join(f"TL-KPI-{int(number):02d}" for number in numbers) if numbers else "NOT_AVAILABLE"


def _claim_refs(value: str) -> str:
    claims = list(dict.fromkeys(re.findall(r"CL-[A-Z0-9-]+", value)))
    return ",".join(claims) if claims else "NOT_AVAILABLE"


def _rows_from_all_tables(
    repo_root: Path,
    dataset: str,
    source: dict[str, str],
    updated_at: str,
    field_names: Sequence[str],
    id_prefix: str,
    evidence_status: str = "TOPLINK_CONFIRMED",
) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    ordinal = 0
    for table in parse_markdown_tables(repo_root / source["path"]):
        for row in table["rows"]:
            ordinal += 1
            values = row["values"]
            joined = " | ".join(values)
            if re.search(r"(?:[A-Za-z]:/Users/|\.secrets/|private_key)", joined, re.IGNORECASE):
                continue
            fields = {field: values[index] if index < len(values) else "NOT_AVAILABLE" for index, field in enumerate(field_names)}
            identity = f"{id_prefix}-{ordinal:03d}"
            records.append(_record(dataset, identity, source, row["location"], updated_at, fields, evidence_status))
    return records


def _split_options(value: str) -> list[tuple[str, str]]:
    pieces = re.split(r"\s+·\s+(?=[ABC]:)", value)
    options: list[tuple[str, str]] = []
    for piece in pieces:
        match = re.match(r"^([ABC]):\s*(.*)$", piece.strip())
        if match:
            options.append((match.group(1), match.group(2).strip()))
    if len(options) != 3 or [code for code, _ in options] != ["A", "B", "C"]:
        raise SyncError(f"three options A/B/C required, got {len(options)}: {value!r}")
    bodies = [body for _, body in options]
    if any(not body for body in bodies):
        raise SyncError(f"empty option body: {value!r}")
    if len(set(bodies)) != 3:
        raise SyncError(f"duplicate option bodies are forbidden: {value!r}")
    return options


def _compile_calendar(repo_root: Path, source: dict[str, str], updated_at: str) -> list[dict[str, str]]:
    tables = parse_markdown_tables(repo_root / source["path"])
    records: list[dict[str, str]] = []
    for table in tables:
        if not table["headers"] or table["headers"][0] != "ID" or len(table["headers"]) != 9:
            continue
        for row in table["rows"]:
            values = row["values"]
            base_id = values[0]
            day_match = re.search(r"D(\d{2})$", base_id)
            if not day_match:
                continue
            day = int(day_match.group(1))
            audience = "TL-A01" if day <= 7 else ("TL-A02" if day <= 14 else "TL-A03")
            funnel = "MOFU" if values[1] in {"TL-P3", "TL-P4"} else "TOFU"
            for option, angle in _split_options(values[4]):
                content_id = f"{base_id}-{option}"
                approval = values[8] if values[8] in {"DRAFT", "NEEDS_HUMAN_REVIEW"} else "NEEDS_HUMAN_REVIEW"
                records.append(
                    _record(
                        "TL_CONTENT_CALENDAR",
                        content_id,
                        source,
                        row["location"],
                        updated_at,
                        {
                            "content_id": content_id,
                            "relative_day": f"D-{day}",
                            "option": option,
                            "audience_id": audience,
                            "pillar_id": values[1],
                            "format": values[2],
                            "funnel_role": funnel,
                            "angle": angle,
                            "cta_class": values[6],
                            "claim_ids": _claim_refs(values[5]),
                            "experiment_ids": "NOT_AVAILABLE",
                            "content_revision": "1",
                            "approval_state": approval,
                        },
                        "HYPOTHESIS",
                        "HYPOTHESIS_VALIDATION_ONLY",
                    )
                )
    return records


def _compile_reels(repo_root: Path, source: dict[str, str], updated_at: str) -> list[dict[str, str]]:
    text = (repo_root / source["path"]).read_text(encoding="utf-8")
    headings = list(re.finditer(r"^### `(?P<id>TL-M5-CAL-D\d{2})`[^\n]*$", text, re.MULTILINE))
    records: list[dict[str, str]] = []
    for index, heading in enumerate(headings):
        block = text[heading.end() : headings[index + 1].start() if index + 1 < len(headings) else len(text)]
        def bullet(label: str) -> str:
            match = re.search(rf"^- \*\*{re.escape(label)}[^:]*:\*\*\s*(.+)$", block, re.MULTILINE)
            return _strip_cell(match.group(1)) if match else "NOT_AVAILABLE"
        content_id = f"{heading.group('id')}-A"
        health = "NEEDS_HUMAN_REVIEW" in heading.group(0) or "HEALTH-SENSITIVE" in block
        records.append(
            _record(
                "TL_REELS_BRIEFS",
                content_id,
                source,
                f"heading {heading.group('id')}",
                updated_at,
                {
                    "reel_id": f"TL-REEL-{heading.group('id')[-3:]}",
                    "content_id": content_id,
                    "duration_seconds": "15-30",
                    "aspect_ratio": "9:16",
                    "hook_options": bullet("Hook"),
                    "script_body": re.sub(r"\s+", " ", block).strip()[:2000],
                    "shot_list": bullet("Shot"),
                    "on_screen_text": bullet("On-screen text"),
                    "subtitle_required": "TRUE",
                    "safe_zone": "14% top · 20% bottom",
                    "cta_class": "follow/save/share",
                    "claim_ids": _claim_refs(block),
                    "accessibility": "subtitle required; readable disclaimer duration",
                    "risk_gate": "PROFESSIONAL_HUMAN_REVIEW" if health else "STANDARD_REVIEW",
                    "production_status": "DRAFT",
                },
                "HYPOTHESIS",
                "INTERNAL_ONLY",
            )
        )
    return records


def _build_base_datasets(repo_root: Path, outputs: list[dict[str, str]], updated_at: str) -> dict[str, list[dict[str, str]]]:
    datasets: dict[str, list[dict[str, str]]] = {key: [] for key in TAB_KEYS}
    contract = _file_source(repo_root, "docs/system/toplink-google-sheets-operational-contract.md", "TL-SHEET-001")
    rules = _file_source(repo_root, "RULES.md", "TL-RULES-001")
    milestones = _file_source(repo_root, "docs Toplink/TOPLINK_PAGE_MILESTONES.md", "TL-MS-001")
    master = _file_source(repo_root, "docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md", "TL-PMP-001")

    control_values = {
        "model": "TL-SHEET-001/0.2.0/24-DATASETS",
        "target": TARGET_SPREADSHEET_ID,
        "approval": "NOT_GRANTED",
        "macro_runs": "2",
        "external_writes": "0",
    }
    for key, value in control_values.items():
        datasets["TL_CONTROL"].append(_record("TL_CONTROL", f"TL-CONTROL-{key.upper()}", contract, "§ Status", updated_at, {"control_key": key, "control_value": value, "control_status": "LOCAL_VERIFIED", "approval_bundle_id": "TL-SHEET-RUN2-CORRECTION-01", "external_writes": "0"}, allowed_use="OPERATIONAL_CONTROL"))

    for item in outputs:
        datasets["TL_SOURCE_INVENTORY"].append(_record("TL_SOURCE_INVENTORY", item["stable_id"], item, "whole canonical artifact", updated_at, {"inventory_source_id": item["stable_id"], "relative_path": item["path"], "sha256": item["sha256"], "category": "CANONICAL_OUTPUT", "sensitivity": "MIXED", "source_status": "LOCAL_VERIFIED", "exclusion_reason": "NOT_AVAILABLE"}, allowed_use="OPERATIONAL_CONTROL"))
        datasets["TL_OUTPUT_INDEX"].append(_record("TL_OUTPUT_INDEX", item["stable_id"], item, "Run 2 generated_outputs[]", updated_at, {"artifact_id": item["stable_id"], "artifact_path": item["path"], "artifact_digest": item["sha256"], "dmp_trace_ids": "SEE_RUN1_RUN2_MANIFESTS", "dataset_keys": ",".join(ARTIFACT_DATASETS[item["stable_id"]]), "schema_version": "TL-SHEET-001/0.2.0", "local_qa_state": "LOCAL_VERIFIED", "sheet_delivery_state": "SYNC_PENDING_APPROVAL", "readback_state": "NOT_AVAILABLE"}, allowed_use="OPERATIONAL_CONTROL"))
    for governance_source in (contract, rules, milestones, master):
        datasets["TL_SOURCE_INVENTORY"].append(_record("TL_SOURCE_INVENTORY", governance_source["stable_id"], governance_source, "whole governance source", updated_at, {"inventory_source_id": governance_source["stable_id"], "relative_path": governance_source["path"], "sha256": governance_source["sha256"], "category": "GOVERNANCE", "sensitivity": "INTERNAL", "source_status": "LOCAL_VERIFIED", "exclusion_reason": "NOT_AVAILABLE"}, allowed_use="OPERATIONAL_CONTROL"))

    gaps = [
        ("TL-GAP-002", "Public franchise/legal evidence", "Legal owner", "TL-M1", "Supply verified document"),
        ("TL-GAP-004", "Product/service dossiers", "Product owner", "TL-M1/TL-M4", "Supply claim dossiers"),
        ("TL-GAP-005", "Offer/booking/contact/privacy/SLA", "Operations owner", "TL-M5/TL-M6", "Verify operating flow"),
        ("TL-GAP-006", "Hard content start date and final capacity", "Content owner", "TL-M6", "Approve dated schedule"),
        ("TL-GAP-007", "Item-level qualified health review", "Professional reviewer", "TL-M5/TL-M6", "Review each sensitive item"),
        ("TL-GAP-009", "Legal name/licence/scope documents", "Legal owner", "TL-M1", "Supply verified documents"),
        ("TL-GAP-010", "Product provenance/certification/inspection", "Product owner", "TL-M1/TL-M4", "Verify product source"),
        ("TL-GAP-ASSET", "Asset rights and consent", "Content owner", "TL-M5/TL-M6", "Clear rights per asset"),
        ("TL-GAP-SHEET-CORRECTION", "Digest-bound correction approval", "Human owner", "Sheet correction", "Approve exact bundle path and SHA-256"),
    ]
    for ordinal, (gap_id, requested, owner, milestone, action) in enumerate(gaps, 1):
        datasets["TL_INPUT_GAPS"].append(_record("TL_INPUT_GAPS", gap_id, milestones, f"§5 blocker register item {ordinal}", updated_at, {"gap_id": gap_id, "requested_input": requested, "gap_owner": owner, "blocked_milestone": milestone, "unblock_action": action, "gap_status": "MISSING_INPUT"}, "MISSING_INPUT", "BLOCKED", owner))
        datasets["TL_OWNER_ACTIONS"].append(_record("TL_OWNER_ACTIONS", f"TL-ACTION-{ordinal:03d}", milestones, f"§5 blocker register item {ordinal}", updated_at, {"action_id": f"TL-ACTION-{ordinal:03d}", "priority": "HIGH", "category": milestone, "requested_decision_or_input": requested, "deadline_gate": "BEFORE_PUBLISH_OR_MUTATION", "blocked_effect": milestone, "live_source_reference": gap_id, "source_status": "MISSING_INPUT", "decision_status": "OPEN", "approver_role": owner, "decision_date": "NOT_AVAILABLE", "decision_value": "NOT_AVAILABLE", "notes": action}, "MISSING_INPUT", "BLOCKED", owner))

    decisions = [
        ("TL-D-SHEET-MODEL", "24 domain datasets; many-to-many artifact mapping", "Sheet correction"),
        ("TL-D-CANONICAL", "Canonical Markdown retained; JSON sidecars are machine interface", "Repository"),
        ("TL-D-RUN-COUNT", "Correction remains in existing Run 1/Run 2; no Run 3", "TL-M1-TL-M5"),
        ("TL-D-V2-CLASS", "V2 is TECHNICAL_READBACK_PASS · BUSINESS_MODEL_FAILED", "Historical delivery"),
        ("TL-D-APPROVAL", "Consumed V2 approval authorizes no later mutation", "External Sheet"),
    ]
    for decision_id, decision, scope in decisions:
        datasets["TL_DECISIONS"].append(_record("TL_DECISIONS", decision_id, master, "§18-§19", updated_at, {"decision_id": decision_id, "authority": "Human owner + canonical plan", "decision_date": "2026-08-04", "decision": decision, "effective_scope": scope, "evidence_reference": "TL-SHEET-001/0.2.0", "review_condition": "Explicit human change control", "decision_status": "DECIDED"}, allowed_use="OPERATIONAL_CONTROL"))

    compliance = [
        ("TL-RULE-HEALTH", "HEALTH", "OUTCOME", "Support-level wording only", "Diagnosis/treatment/cure/prevention/guarantee", "Professional reviewer", "ITEM_LEVEL"),
        ("TL-RULE-LEGAL", "LEGAL", "FRANCHISE", "Internal classification only", "Unverified public relationship wording", "Legal reviewer", "DOCUMENT_REQUIRED"),
        ("TL-RULE-PRIVACY", "PRIVACY", "TESTIMONIAL", "Purpose/channel/duration/withdrawal/redaction consent", "Unconsented PII/UGC", "Privacy owner", "CONSENT_REQUIRED"),
        ("TL-RULE-CTA", "COMMERCIAL", "OFFER", "Follow/save/share before offer readiness", "Booking/purchase CTA without operating proof", "Operations owner", "OFFER_GATE"),
        ("TL-RULE-APPROVAL", "WORKFLOW", "APPROVAL", "Human digest-bound approval only", "Sheet/reviewer self-approval", "Human owner", "HUMAN_ONLY"),
    ]
    for rule in compliance:
        datasets["TL_COMPLIANCE_RULES"].append(_record("TL_COMPLIANCE_RULES", rule[0], rules, "Hard stops / approval", updated_at, {"rule_id": rule[0], "risk_class": rule[1], "claim_class": rule[2], "permitted_boundary": rule[3], "forbidden_boundary": rule[4], "reviewer_role": rule[5], "human_gate": rule[6]}, allowed_use="OPERATIONAL_CONTROL"))

    datasets["TL_PAGE_BENCHMARK"].extend([
        _record("TL_PAGE_BENCHMARK", "TL-PAGE-BASELINE-FOLLOWERS", master, "§18 target record", updated_at, {"page_snapshot_id": "TL-PAGE-BASELINE-FOLLOWERS", "page_id": "61591880797654", "snapshot_at_ict": "2026-07-30T00:00:00+07:00", "metric": "followers", "measured_value": "0", "denominator": "NOT_AVAILABLE", "baseline_status": "TOPLINK_CONFIRMED"}, allowed_use="OPERATIONAL_CONTROL"),
        _record("TL_PAGE_BENCHMARK", "TL-PAGE-BASELINE-AWARENESS", master, "§17 baseline rules", updated_at, {"page_snapshot_id": "TL-PAGE-BASELINE-AWARENESS", "page_id": "61591880797654", "snapshot_at_ict": "2026-07-30T00:00:00+07:00", "metric": "awareness", "measured_value": "N/A", "denominator": "NOT_AVAILABLE", "baseline_status": "NO_MEASUREMENT"}, "UNVERIFIED", "DO_NOT_USE"),
    ])

    datasets["TL_REPORT"].extend([
        _record("TL_REPORT", "TL-REPORT-STATUS", contract, "§ Status", updated_at, {"report_id": "TL-REPORT-STATUS", "report_section": "Sheet correction", "synthesis": "24 normalized datasets local build; external mutation not approved", "source_record_ids": "TL-SHEET-RUN2-CORRECTION-01", "status": "SYNC_PENDING_APPROVAL", "blocker_ids": "TL-GAP-SHEET-CORRECTION"}, allowed_use="OPERATIONAL_CONTROL"),
        _record("TL_REPORT", "TL-REPORT-HUMAN-GATES", milestones, "§5 blocker register", updated_at, {"report_id": "TL-REPORT-HUMAN-GATES", "report_section": "Human gates", "synthesis": "Health, legal, product, privacy, consent, and asset-rights gates remain open", "source_record_ids": "TL-GAP-002,TL-GAP-004,TL-GAP-005,TL-GAP-007,TL-GAP-009,TL-GAP-010,TL-GAP-ASSET", "status": "NOT_COMPLETE", "blocker_ids": "OPEN_HUMAN_GATES"}, "MISSING_INPUT", "BLOCKED"),
    ])
    return datasets


def compile_datasets(repo_root: Path) -> dict[str, Any]:
    plan = build_human_layer_plan(repo_root)
    bundle: dict[str, Any] = {
        "bundle_id": "YV-HUMAN-LAYER-DATASETS-1.0.0",
        "schema_version": plan["schema_version"],
        "spreadsheet_id": TARGET_SPREADSHEET_ID,
        "source_digests": copy.deepcopy(plan["source_digests"]),
        "workbook_content_hash": plan["workbook_content_hash"],
        "datasets": {
            tab["tab"]: {
                "dataset_key": tab["tab"],
                "schema_version": plan["schema_version"],
                "used_range": tab["used_range"],
                "row_count": tab["row_count"],
                "column_count": tab["column_count"],
                "yellow_cells": copy.deepcopy(tab["yellow_cells"]),
                "hidden_columns": copy.deepcopy(tab["hidden_columns"]),
                "values": copy.deepcopy(tab["values"]),
                "dataset_sha256": tab["content_hash"],
            }
            for tab in plan["tabs"]
        },
    }
    bundle["bundle_sha256"] = sha256_json(bundle)
    return bundle

    # Historical 24-tab compiler retained below as unreachable evidence until
    # the live YV executor is accepted; the active code path above is YV-only.
    registry = load_registry(repo_root)
    correction = read_json(repo_root / "docs Toplink/staging/run2/correction/correction-manifest.json")
    updated_at = str(correction.get("created_at_ict", ""))
    if not updated_at:
        raise SyncError("correction timestamp missing")
    outputs = _manifest_outputs(repo_root)
    datasets = _build_base_datasets(repo_root, outputs, updated_at)

    brand = _source(repo_root, outputs, "TL-BRAND-PROFILE-001")
    brand_rows = _rows_from_all_tables(repo_root, "TL_BRAND_PROFILE", brand, updated_at, ["field_name", "field_value", "profile_digest", "mutation_gate"], "TL-PROFILE")
    for index, row in enumerate(brand_rows, 1):
        row["profile_field_id"] = f"TL-PROFILE-FIELD-{index:03d}"
    datasets["TL_BRAND_PROFILE"] = brand_rows

    runtime = _source(repo_root, outputs, "TL-RUNTIME-COMPAT-001")
    runtime_rows = _rows_from_all_tables(repo_root, "TL_RUNTIME_COMPATIBILITY", runtime, updated_at, ["category", "runtime_role", "runtime_state", "compatibility_rule"], "TL-RUNTIME")
    for index, row in enumerate(runtime_rows, 1):
        row["runtime_rule_id"] = f"TL-RUNTIME-RULE-{index:03d}"
    datasets["TL_RUNTIME_COMPATIBILITY"] = runtime_rows

    audience = _source(repo_root, outputs, "TL-AUDIENCE-001")
    audience_table = parse_markdown_tables(repo_root / audience["path"])[0]
    for index, row in enumerate(audience_table["rows"], 1):
        values = row["values"]
        datasets["TL_AUDIENCE_HYPOTHESES"].append(_record("TL_AUDIENCE_HYPOTHESES", values[0] or f"TL-A{index:02d}", audience, row["location"], updated_at, {"audience_id": values[0] or f"TL-A{index:02d}", "hypothesis": values[1], "evidence_level": "HYPOTHESIS", "validation_method": "Observe content utility and qualitative questions", "observation_window": "30-day pilot", "current_verdict": values[2], "rationale": values[3]}, "HYPOTHESIS", "HYPOTHESIS_VALIDATION_ONLY"))

    positioning = _source(repo_root, outputs, "TL-POSITIONING-001")
    position_rows = _rows_from_all_tables(repo_root, "TL_POSITIONING", positioning, updated_at, ["positioning_type", "statement", "proof_status", "proof_boundary", "validation_path"], "TL-POS")
    for index, row in enumerate(position_rows, 1):
        row["positioning_id"] = f"TL-POS-{index:03d}"
        row["evidence_status"] = "HYPOTHESIS" if "draft" in row.get("positioning_type", "").lower() else row["evidence_status"]
    datasets["TL_POSITIONING"] = position_rows

    narrative = _source(repo_root, outputs, "TL-NARRATIVE-001")
    narrative_rows = _rows_from_all_tables(repo_root, "TL_NARRATIVE", narrative, updated_at, ["narrative_rule", "boundary", "voice_owner", "founder_gate"], "TL-NARR")
    for index, row in enumerate(narrative_rows, 1):
        row["narrative_id"] = f"TL-NARR-{index:03d}"
    datasets["TL_NARRATIVE"] = narrative_rows

    pillars = _source(repo_root, outputs, "TL-PILLARS-001")
    pillar_table = parse_markdown_tables(repo_root / pillars["path"])[0]
    pillar_rows = [row for row in pillar_table["rows"] if re.fullmatch(r"TL-P[1-5]", row["values"][0])]
    slots = [int(re.match(r"(\d+)", row["values"][1]).group(1)) for row in pillar_rows]
    weights = [round(slot * 100 / sum(slots), 4) for slot in slots]
    weights[-1] = round(100 - sum(weights[:-1]), 4)
    for row, weight in zip(pillar_rows, weights):
        pillar_id = row["values"][0]
        datasets["TL_CONTENT_PILLARS"].append(_record("TL_CONTENT_PILLARS", pillar_id, pillars, row["location"], updated_at, {"pillar_id": pillar_id, "pillar_name": row["values"][2], "weight_percent": weight, "audience_job": "See canonical pillar decision", "formats": "Facebook post/Reel", "funnel_role": "MOFU" if pillar_id in {"TL-P3", "TL-P4"} else "TOFU", "risk_gate": "ITEM_LEVEL_REVIEW" if pillar_id in {"TL-P2", "TL-P4", "TL-P5"} else "STANDARD_REVIEW", "rationale": row["values"][2]}, "HYPOTHESIS", "HYPOTHESIS_VALIDATION_ONLY"))

    facebook = _source(repo_root, outputs, "TL-PAGE-STRATEGY-001")
    facebook_rows = _rows_from_all_tables(repo_root, "TL_FACEBOOK_STRATEGY", facebook, updated_at, ["channel", "role", "strategy_state", "share_percent", "pillar_ids", "strategy_type"], "TL-FB")
    for index, row in enumerate(facebook_rows, 1):
        row["strategy_id"] = f"TL-FB-STRATEGY-{index:03d}"
        row["pillar_ids"] = _id_refs(row["pillar_ids"], r"TL-P[1-5]")
    datasets["TL_FACEBOOK_STRATEGY"] = facebook_rows

    campaign = _source(repo_root, outputs, "TL-CAMPAIGN-001")
    campaign_tables = parse_markdown_tables(repo_root / campaign["path"])
    for index, row in enumerate(campaign_tables[0]["rows"], 1):
        values = row["values"]
        campaign_id = f"TL-CAMPAIGN-W{index}"
        datasets["TL_CAMPAIGN"].append(_record("TL_CAMPAIGN", campaign_id, campaign, row["location"], updated_at, {"campaign_item_id": campaign_id, "relative_week": values[0], "relative_days": values[1], "campaign_role": values[2], "pillar_ids": _id_refs(values[3], r"TL-P[1-5]"), "audience_job": values[4], "hard_gate": values[5], "default_cta_class": values[6]}, "HYPOTHESIS", "HYPOTHESIS_VALIDATION_ONLY"))
    for index, row in enumerate(campaign_tables[1]["rows"], 1):
        values = row["values"]
        signal_parts = re.split(r";\s*", values[2])
        datasets["TL_EXPERIMENTS"].append(_record("TL_EXPERIMENTS", f"TL-EXP-{index:03d}", campaign, row["location"], updated_at, {"experiment_id": f"TL-EXP-{index:03d}", "campaign_item_id": "TL-CAMPAIGN-W1", "hypothesis": values[0], "variable": values[1], "evidence_level": "HYPOTHESIS", "validation_method": "One variable at a time", "observation_window": "Minimum sample from KPI dictionary", "continue_signal": signal_parts[0] if signal_parts else values[2], "repair_signal": signal_parts[1] if len(signal_parts) > 1 else "Flat signal", "stop_signal": signal_parts[2] if len(signal_parts) > 2 else "Risk signal increases", "experiment_decision": "DEFERRED"}, "HYPOTHESIS", "HYPOTHESIS_VALIDATION_ONLY"))

    kpi = _source(repo_root, outputs, "TL-KPI-001")
    kpi_table = parse_markdown_tables(repo_root / kpi["path"])[0]
    for row in kpi_table["rows"]:
        values = row["values"]
        launch_value = values[8]
        denominator_status = "NOT_AVAILABLE" if "N/A" in launch_value else "COUNT_NOT_RATE"
        datasets["TL_KPI_DICTIONARY"].append(_record("TL_KPI_DICTIONARY", values[0], kpi, row["location"], updated_at, {"kpi_id": values[0], "metric": values[1], "definition": values[2], "formula": values[3], "measurement_source": values[4], "metric_owner": values[5], "cadence": values[6], "minimum_sample": values[7], "launch_value": launch_value, "denominator_status": denominator_status}, "HYPOTHESIS", "HYPOTHESIS_VALIDATION_ONLY"))

    calendar = _source(repo_root, outputs, "TL-M5-CALENDAR-001")
    datasets["TL_CONTENT_CALENDAR"] = _compile_calendar(repo_root, calendar, updated_at)

    asset = _source(repo_root, outputs, "TL-M5-ASSET-001")
    asset_tables = parse_markdown_tables(repo_root / asset["path"])
    asset_records: list[dict[str, str]] = []
    for row in asset_tables[1]["rows"]:
        values = row["values"]
        asset_records.append(_record("TL_ASSET_BATCH_PLAN", values[0], asset, row["location"], updated_at, {"asset_batch_id": values[0], "asset_id": values[0], "content_ids": _content_refs(values[4]), "asset_type": values[1], "description": values[2], "batch_id": "DEFERRED", "capacity": "3 videos/week · at least 7 items/week", "rights_state": values[3], "consent_state": "REQUIRED_IF_PERSON_APPEARS", "production_status": "PLACEHOLDER_ONLY"}, "MISSING_INPUT", "BLOCKED"))
    for row in asset_tables[2]["rows"]:
        values = row["values"]
        asset_records.append(_record("TL_ASSET_BATCH_PLAN", values[0], asset, row["location"], updated_at, {"asset_batch_id": values[0], "asset_id": values[3], "content_ids": _content_refs(values[1]), "asset_type": "BATCH", "description": values[2], "batch_id": values[0], "capacity": "3 videos/week", "rights_state": "RIGHTS_UNCLEARED", "consent_state": "ITEM_LEVEL", "production_status": values[4]}, "MISSING_INPUT", "BLOCKED"))
    datasets["TL_ASSET_BATCH_PLAN"] = asset_records

    reels = _source(repo_root, outputs, "TL-M5-REELS-001")
    datasets["TL_REELS_BRIEFS"] = _compile_reels(repo_root, reels, updated_at)

    production = _source(repo_root, outputs, "TL-M5-PRODBRIEF-001")
    production_table = parse_markdown_tables(repo_root / production["path"])[0]
    for row in production_table["rows"]:
        values = row["values"]
        content_id = f"TL-M5-CAL-{values[0]}-A"
        datasets["TL_PRODUCTION_BRIEFS"].append(_record("TL_PRODUCTION_BRIEFS", f"TL-PROD-{values[0]}", production, row["location"], updated_at, {"production_id": f"TL-PROD-{values[0]}", "content_id": content_id, "format": values[1], "hook": values[2], "shot_visual": values[3], "on_screen_text": values[4], "cta_class": values[5], "claim_ids": _claim_refs(values[6]), "kpi_ids": _kpi_refs(values[10]), "accessibility": "subtitle/safe-zone/readable disclaimer as applicable", "risk_gate": values[8], "production_status": values[9]}, "HYPOTHESIS", "INTERNAL_ONLY"))

    workflow = _source(repo_root, outputs, "TL-M5-WORKFLOW-001")
    for content in datasets["TL_CONTENT_CALENDAR"]:
        content_id = content["content_id"]
        content_hash = sha256_json({key: value for key, value in content.items() if key not in COMMON_COLUMNS})
        verdict = content["approval_state"]
        datasets["TL_WORKFLOW_APPROVAL"].append(_record("TL_WORKFLOW_APPROVAL", f"TL-APPROVAL-{content_id}-R1", workflow, "approval ledger derived from canonical content revision", updated_at, {"approval_id": f"TL-APPROVAL-{content_id}-R1", "content_id": content_id, "content_hash": content_hash, "content_revision": "1", "reviewer_role": "Human/professional as routed", "verdict": verdict, "conditions": "All claim, rights, consent, and human gates must pass", "expires_at_ict": "NOT_AVAILABLE", "publish_state": "BLOCKED", "material_edit_reset": "TRUE"}, "HYPOTHESIS", "BLOCKED"))

    closure_evidence_path = repo_root / CORRECTION_DIR / "output-index-closure-readback.json"
    if closure_evidence_path.exists():
        closure_evidence = read_json(closure_evidence_path)
        if closure_evidence.get("status") == "SYNC_READBACK_PASS":
            overlay = read_json(repo_root / CORRECTION_DIR / "datasets/TL_OUTPUT_INDEX.json")
            if closure_evidence.get("output_index_dataset_sha256") != overlay.get("dataset_sha256"):
                raise SyncError("output-index closure overlay digest drift")
            if any(
                record.get("sheet_delivery_state") != "SYNC_READBACK_PASS"
                or record.get("readback_state") != "SYNC_READBACK_PASS"
                for record in overlay.get("records", [])
            ):
                raise SyncError("output-index closure overlay state drift")
            datasets["TL_OUTPUT_INDEX"] = copy.deepcopy(overlay["records"])

    bundle: dict[str, Any] = {
        "bundle_id": "TL-SHEET-DATASETS-0.2.0",
        "schema_version": registry["schema_version"],
        "spreadsheet_id": TARGET_SPREADSHEET_ID,
        "generated_at_ict": updated_at,
        "source_manifest_path": "docs Toplink/staging/run2/run2-manifest.json",
        "datasets": {},
    }
    for key in TAB_KEYS:
        schema = registry["datasets"][key]
        records = datasets[key]
        payload = {"dataset_key": key, "schema_version": registry["schema_version"], "columns": schema["columns"], "records": records}
        payload["dataset_sha256"] = sha256_json(payload)
        bundle["datasets"][key] = payload
    bundle["bundle_sha256"] = sha256_json(bundle)
    validate_dataset_bundle(bundle, registry)
    validate_source_digests(bundle, repo_root)
    return bundle


def validate_dataset_bundle(bundle: dict[str, Any], registry: dict[str, Any]) -> None:
    if bundle.get("schema_version") == "YV-SHEET-001/1.0.0":
        datasets = bundle.get("datasets")
        if not isinstance(datasets, dict) or set(datasets) != set(TAB_KEYS):
            raise SyncError("human-layer bundle must contain the ordered 21 tabs")
        return
    datasets = bundle.get("datasets")
    if not isinstance(datasets, dict) or set(datasets) != set(TAB_KEYS):
        raise SyncError("dataset bundle must contain exact 24 datasets")
    indexes: dict[tuple[str, tuple[str, ...]], set[tuple[str, ...]]] = {}
    for key, payload in datasets.items():
        schema = registry["datasets"][key]
        records = payload.get("records")
        if not isinstance(records, list):
            raise SyncError(f"records missing: {key}")
        minimum = int(schema.get("min_records", 0))
        maximum = int(schema.get("max_records", 10**9))
        if not minimum <= len(records) <= maximum:
            raise SyncError(f"cardinality violation: {key} ({len(records)})")
        primary_key = str(schema["primary_key"])
        seen: set[str] = set()
        for record in records:
            if record.get("record_type") == "PROSE" or {"section", "text"}.issubset(record):
                raise SyncError(f"prose row forbidden: {key}")
            unknown = set(record) - set(schema["columns"])
            if unknown:
                raise SyncError(f"unknown columns in {key}: {sorted(unknown)}")
            for field in schema["columns"]:
                if field not in record or record[field] == "":
                    raise SyncError(f"blank required field: {key}.{field}")
            identity = str(record[primary_key])
            if identity in seen:
                raise SyncError(f"duplicate primary key: {key}.{identity}")
            seen.add(identity)
            for field in ("evidence_status", "allowed_use"):
                if record[field] not in registry["enums"][field]:
                    raise SyncError(f"unknown enum: {key}.{field}={record[field]}")
            for field, enum_name in schema.get("field_enums", {}).items():
                if record[field] not in registry["enums"][enum_name]:
                    raise SyncError(f"unknown enum: {key}.{field}={record[field]}")
            for reference in schema.get("external_references", []):
                contract = reference["contract"]
                for field in reference["columns"]:
                    value = str(record[field])
                    if contract == "registry_dataset_keys" and any(part.strip() not in TAB_KEYS for part in value.split(",")):
                        raise SyncError(f"unknown registry dataset reference: {key}.{field}")
                    if contract == "manifest_trace_ids" and value != "SEE_RUN1_RUN2_MANIFESTS":
                        raise SyncError(f"manifest trace reference drift: {key}.{field}")
                    if contract == "claim_ids":
                        sentinels = set(registry["external_reference_contracts"][contract]["allowed_sentinels"])
                        if value not in sentinels and any(not re.fullmatch(r"CL-[A-Z0-9-]+", part) for part in value.split(",")):
                            raise SyncError(f"invalid claim reference: {key}.{field}")
        candidate_columns = {primary_key}
        for other_schema in registry["datasets"].values():
            for foreign_key in other_schema.get("foreign_keys", []):
                if foreign_key.get("dataset") == key:
                    candidate_columns.update(foreign_key.get("target_columns", []))
        for column in candidate_columns:
            indexes[(key, (column,))] = {(str(record[column]),) for record in records}
    for key, payload in datasets.items():
        for foreign_key in registry["datasets"][key].get("foreign_keys", []):
            source_columns = tuple(foreign_key["columns"])
            target_columns = tuple(foreign_key["target_columns"])
            target_values = indexes.get((foreign_key["dataset"], target_columns))
            if target_values is None:
                target_records = datasets[foreign_key["dataset"]]["records"]
                target_values = {tuple(str(record[column]) for column in target_columns) for record in target_records}
            for record in payload["records"]:
                raw_values = tuple(str(record[column]) for column in source_columns)
                if len(source_columns) == 1 and foreign_key.get("multi_value_separator"):
                    values_to_check = [
                        (part.strip(),)
                        for part in raw_values[0].split(str(foreign_key["multi_value_separator"]))
                    ]
                else:
                    values_to_check = [raw_values]
                allowed = set(str(value) for value in foreign_key.get("allow_values", []))
                for value in values_to_check:
                    if len(value) == 1 and value[0] in allowed:
                        continue
                    if value not in target_values:
                        raise SyncError(f"orphan foreign key: {key}{value} -> {foreign_key['dataset']}")
    for key, payload in datasets.items():
        declared_dataset_digest = payload.get("dataset_sha256")
        payload_without_digest = copy.deepcopy(payload)
        payload_without_digest.pop("dataset_sha256", None)
        if declared_dataset_digest != sha256_json(payload_without_digest):
            raise SyncError(f"dataset digest mismatch: {key}")
    expected_bundle_digest = bundle.get("bundle_sha256")
    if expected_bundle_digest:
        without_digest = copy.deepcopy(bundle)
        without_digest.pop("bundle_sha256", None)
        if expected_bundle_digest != sha256_json(without_digest):
            raise SyncError("bundle digest mismatch")


def validate_source_digests(bundle: dict[str, Any], repo_root: Path) -> None:
    if bundle.get("schema_version") == "YV-SHEET-001/1.0.0":
        for relative, digest in bundle.get("source_digests", {}).items():
            path = repo_root / relative
            if not path.is_file() or sha256_file(path) != digest:
                raise SyncError(f"source digest drift: {relative}")
        return
    for record in bundle["datasets"]["TL_OUTPUT_INDEX"]["records"]:
        path = repo_root / record["artifact_path"]
        if not path.is_file() or sha256_file(path) != record["artifact_digest"]:
            raise SyncError(f"source digest drift: {record['artifact_path']}")
    checked: set[tuple[str, str]] = set()
    for payload in bundle["datasets"].values():
        for record in payload["records"]:
            binding = (record["source_path"], record["source_digest"])
            path = repo_root / record["source_path"]
            if binding not in checked:
                checked.add(binding)
                if not path.is_file() or sha256_file(path) != record["source_digest"]:
                    raise SyncError(f"row source digest drift: {record['source_path']}")
            claim_ids = record.get("claim_ids", "NOT_AVAILABLE")
            if claim_ids not in {"NOT_AVAILABLE", "NONE", "N/A", "No claim"}:
                source_text = path.read_text(encoding="utf-8")
                for claim_id in claim_ids.split(","):
                    if claim_id not in source_text:
                        raise SyncError(f"unresolved external claim reference: {claim_id}")


def validate_dataset_sidecars(bundle: dict[str, Any], output_dir: Path) -> None:
    expected_names = {f"{key}.json" for key in TAB_KEYS}
    actual_names = {path.name for path in output_dir.glob("*.json")}
    if actual_names != expected_names:
        raise SyncError("dataset sidecar set drift")
    for key in TAB_KEYS:
        if read_json(output_dir / f"{key}.json") != bundle["datasets"][key]:
            raise SyncError(f"dataset sidecar drift: {key}")


def write_dataset_sidecars(bundle: dict[str, Any], output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for key in TAB_KEYS:
        path = output_dir / f"{key}.json"
        write_json(path, bundle["datasets"][key])
        paths.append(path)
    return paths


def _column_number(name: str) -> int:
    number = 0
    for character in name:
        number = number * 26 + ord(character.upper()) - 64
    return number


def _column_name(number: int) -> str:
    if number < 1:
        raise SyncError("column number must be positive")
    result = ""
    while number:
        number, remainder = divmod(number - 1, 26)
        result = chr(65 + remainder) + result
    return result


def _parse_range(value: str) -> tuple[int, int, int, int]:
    match = re.fullmatch(r"([A-Z]+)(\d+):([A-Z]+)(\d+)", value)
    if not match:
        raise SyncError(f"unsupported A1 range: {value}")
    return int(match.group(2)), _column_number(match.group(1)), int(match.group(4)), _column_number(match.group(3))


def plan_bounded_replace(old_used_range: str, new_used_range: str) -> dict[str, str]:
    old = _parse_range(old_used_range)
    new = _parse_range(new_used_range)
    if old[:2] != (1, 1) or new[:2] != (1, 1):
        raise SyncError("bounded replacement ranges must start at A1")
    clear_range = f"A1:{_column_name(max(old[3], new[3]))}{max(old[2], new[2])}"
    return {"write_range": new_used_range, "clear_range": clear_range}


def apply_bounded_replace(matrix: list[list[str]], plan: dict[str, str], values: list[list[str]]) -> list[list[str]]:
    result = copy.deepcopy(matrix)
    _, _, clear_row, clear_column = _parse_range(plan["clear_range"])
    for row in range(min(clear_row, len(result))):
        for column in range(min(clear_column, len(result[row]))):
            result[row][column] = ""
    _, _, write_row, write_column = _parse_range(plan["write_range"])
    if len(values) != write_row or any(len(row) != write_column for row in values):
        raise SyncError("replacement values do not match write range")
    for row, values_row in enumerate(values):
        for column, value in enumerate(values_row):
            result[row][column] = value
    return result


def reset_approval_on_material_edit(record: dict[str, str], new_content_hash: str) -> dict[str, str]:
    result = copy.deepcopy(record)
    if result.get("content_hash") != new_content_hash:
        result["content_hash"] = new_content_hash
        result["verdict"] = "NEEDS_HUMAN_REVIEW"
        result["publish_state"] = "BLOCKED"
    return result


def validate_create_actions(create_titles: Iterable[str], existing_titles: set[str]) -> None:
    overlap = set(create_titles) & existing_titles
    if overlap:
        raise SyncError(f"existing tab cannot use one-shot CREATE_TAB: {sorted(overlap)}")


def example_approval_bundle(expires_at: datetime) -> dict[str, Any]:
    action = {"tab_key": "TL_REPORT", "action": "REPLACE_RANGE", "old_used_range": "A1:A1", "new_used_range": "A1:A2", "approved_new_used_range": "A1:A2", "clear_range": "A1:A2", "max_rows": 2, "max_columns": 1}
    return {"bundle_id": "TL-SHEET-RUN2-CORRECTION-01", "approval_state": "APPROVED", "spreadsheet_id": TARGET_SPREADSHEET_ID, "service_account": TARGET_SERVICE_ACCOUNT, "expires_at_ict": expires_at.isoformat(), "actions": [action], "recovery": False}


def validate_correction_approval(bundle: dict[str, Any], now: datetime | None = None) -> None:
    now = now or datetime.now(timezone.utc)
    if bundle.get("spreadsheet_id") != TARGET_SPREADSHEET_ID:
        raise SyncError("wrong target")
    if bundle.get("service_account") != TARGET_SERVICE_ACCOUNT:
        raise SyncError("wrong service account")
    try:
        expiry = datetime.fromisoformat(str(bundle.get("expires_at_ict", "")))
    except ValueError as exc:
        raise SyncError("invalid approval expiry") from exc
    if expiry.tzinfo is None or expiry <= now:
        raise SyncError("approval expired")
    if bundle.get("approval_state") != "APPROVED":
        raise SyncError("human APPROVED state required")
    for action in bundle.get("actions", []):
        if action.get("new_used_range") != action.get("approved_new_used_range"):
            raise SyncError("scope drift")
        _, _, rows, columns = _parse_range(str(action.get("new_used_range", "")))
        if rows > int(action.get("max_rows", -1)) or columns > int(action.get("max_columns", -1)):
            raise SyncError("scope drift")


def validate_approval_statement(path: Path, statement: str, now: datetime | None = None) -> dict[str, Any]:
    bundle = read_json(path)
    expected = f"APPROVED: {bundle.get('bundle_id')} at {path.as_posix()} SHA-256 {sha256_file(path)}"
    if statement != expected:
        raise SyncError("approval statement mismatch")
    approved = copy.deepcopy(bundle)
    approved["approval_state"] = "APPROVED"
    validate_correction_approval(approved, now)
    return approved


def validate_active_lease(repo_root: Path) -> None:
    task_text = (repo_root / "task.md").read_text(encoding="utf-8")
    active_rows = [
        line
        for line in task_text.splitlines()
        if line.startswith("| Codex CLI (`root`) |")
    ]
    if len(active_rows) != 1 or "toplink_sheet_sync.py" not in active_rows[0] or "digest-bound approval" not in active_rows[0]:
        raise SyncError("lease drift: exact active Codex Sheet-correction lease required")


def validate_repository_bindings(bundle: dict[str, Any], repo_root: Path) -> None:
    bindings = bundle.get("repository_bindings", {})
    for name, relative_path in REPOSITORY_BINDING_PATHS.items():
        if bindings.get(name) != sha256_file(repo_root / relative_path):
            label = "registry" if name == "registry_sha256" else name.removesuffix("_sha256")
            raise SyncError(f"{label} digest drift")


def validate_exact_correction_scope(
    approved: dict[str, Any], repo_root: Path, dataset_bundle: dict[str, Any], snapshot: dict[str, Any]
) -> None:
    expected = build_correction_bundle(
        repo_root, dataset_bundle, snapshot, str(approved.get("expires_at_ict", ""))
    )
    actual = copy.deepcopy(approved)
    actual["approval_state"] = "DRAFT_UNSIGNED"
    if actual != expected:
        raise SyncError("approved correction scope drift")


def validate_live_baseline(
    approved: dict[str, Any],
    frozen_snapshot: dict[str, Any],
    current_sheets: list[dict[str, Any]],
    live_values: dict[str, dict[str, str]],
) -> None:
    frozen_by_title = {sheet["title"]: sheet for sheet in frozen_snapshot.get("sheets", [])}
    current_by_title = {sheet["title"]: sheet for sheet in current_sheets}
    if set(current_by_title) != set(frozen_by_title):
        raise SyncError("live sheet registry drift")
    for title, frozen in frozen_by_title.items():
        if current_by_title[title].get("sheet_id") != frozen.get("sheet_id"):
            raise SyncError(f"live sheet ID drift: {title}")
        expected_digest = frozen.get("values_digest", frozen.get("baseline_digest"))
        expected_range = frozen.get("used_range", frozen.get("baseline_range"))
        if expected_digest:
            actual = live_values.get(title, {})
            if actual.get("range") != expected_range or actual.get("digest") != expected_digest:
                raise SyncError(f"live values drift: {title}")
    if approved.get("snapshot_sha256") != sha256_json(frozen_snapshot):
        raise SyncError("approved snapshot digest drift")


def build_recovery_bundle(parent_bundle_id: str, snapshot: dict[str, Any]) -> dict[str, Any]:
    return {"bundle_id": f"{parent_bundle_id}-RECOVERY-01", "parent_bundle_id": parent_bundle_id, "approval_state": "NOT_GRANTED", "current_state": snapshot, "automatic_rollback": False, "new_approval_required": True}


def build_verify_only_recovery_bundle(
    repo_root: Path,
    parent: dict[str, Any],
    partial_evidence: dict[str, Any],
    expires_at_ict: str,
) -> dict[str, Any]:
    parent_path = repo_root / CORRECTION_DIR / "approval-bundle-unsigned.json"
    evidence_path = repo_root / CORRECTION_DIR / "correction-readback.json"
    if read_json(parent_path) != parent:
        raise SyncError("recovery parent bundle input drift")
    if read_json(evidence_path) != partial_evidence:
        raise SyncError("recovery partial evidence input drift")
    if partial_evidence.get("status") != "VERIFY_FAILED":
        raise SyncError("VERIFY_FAILED evidence required for recovery")
    completed = partial_evidence.get("completed_phases", [])
    if completed != ["CREATE_TAB", "CLEAR_BOUNDED_RANGES", "WRITE_DATASETS", "FORMAT_AND_VALIDATE"]:
        raise SyncError("verify-only recovery requires all mutation phases completed")
    current_metadata = partial_evidence.get("current_state", {}).get("metadata", {})
    current_sheets = {sheet["title"]: sheet for sheet in current_metadata.get("sheets", [])}
    expected_titles = {"Trang tính1", *TAB_KEYS}
    if set(current_sheets) != expected_titles:
        raise SyncError("recovery current sheet registry drift")
    actions: list[dict[str, Any]] = []
    for parent_action in parent["actions"]:
        title = parent_action["tab_key"]
        current_sheet_id = current_sheets[title]["sheet_id"]
        actions.append({
            "tab_key": title,
            "action": "EXACT_READBACK_ONLY",
            "sheet_id": current_sheet_id,
            "new_used_range": parent_action["new_used_range"],
            "approved_new_used_range": parent_action["approved_new_used_range"],
            "max_rows": parent_action["max_rows"],
            "max_columns": parent_action["max_columns"],
            "dataset_sha256": parent_action["dataset_sha256"],
            "formatting": copy.deepcopy(parent_action["formatting"]),
            "validations": copy.deepcopy(parent_action["validations"]),
            "date_columns": list(parent_action.get("date_columns", [])),
        })
    recovery: dict[str, Any] = {
        "bundle_id": f"{parent['bundle_id']}-RECOVERY-01",
        "parent_bundle_id": parent["bundle_id"],
        "parent_bundle_path": CORRECTION_DIR.joinpath("approval-bundle-unsigned.json").as_posix(),
        "parent_bundle_sha256": sha256_file(parent_path),
        "partial_failure_path": CORRECTION_DIR.joinpath("correction-readback.json").as_posix(),
        "partial_failure_sha256": sha256_file(evidence_path),
        "approval_state": "DRAFT_UNSIGNED",
        "recovery_mode": "EXACT_READBACK_ONLY",
        "spreadsheet_id": TARGET_SPREADSHEET_ID,
        "service_account": TARGET_SERVICE_ACCOUNT,
        "operator": "Codex CLI",
        "expires_at_ict": expires_at_ict,
        "schema_version": parent["schema_version"],
        "dataset_bundle_sha256": parent["dataset_bundle_sha256"],
        "snapshot_sha256": parent["snapshot_sha256"],
        "repository_bindings": copy.deepcopy(parent["repository_bindings"]),
        "current_state_sha256": sha256_json(partial_evidence["current_state"]),
        "actions": actions,
        "readback_tabs": list(TAB_KEYS),
        "preserve_tabs": ["Trang tính1"],
        "authorized_external_mutations": 0,
        "automatic_rollback": False,
        "new_approval_required": True,
    }
    recovery["scope_sha256"] = sha256_json({"actions": actions, "preserve_tabs": recovery["preserve_tabs"], "authorized_external_mutations": 0})
    return recovery


def validate_exact_recovery_scope(
    approved: dict[str, Any], repo_root: Path, parent: dict[str, Any], partial_evidence: dict[str, Any]
) -> None:
    expected = build_verify_only_recovery_bundle(
        repo_root, parent, partial_evidence, str(approved.get("expires_at_ict", ""))
    )
    actual = copy.deepcopy(approved)
    actual["approval_state"] = "DRAFT_UNSIGNED"
    if actual != expected:
        raise SyncError("approved recovery scope drift")


def _closed_output_index_sidecar(sidecar: dict[str, Any], status_at_ict: str) -> dict[str, Any]:
    closed = copy.deepcopy(sidecar)
    records = closed.get("records", [])
    if len(records) != 14:
        raise SyncError("output-index cardinality drift")
    for record in records:
        if record.get("sheet_delivery_state") != "SYNC_PENDING_APPROVAL" or record.get("readback_state") != "NOT_AVAILABLE":
            raise SyncError("output-index pre-closure state drift")
        try:
            record["revision"] = str(int(record["revision"]) + 1)
        except (KeyError, TypeError, ValueError) as exc:
            raise SyncError("output-index revision drift") from exc
        record["updated_at_ict"] = status_at_ict
        record["sheet_delivery_state"] = "SYNC_READBACK_PASS"
        record["readback_state"] = "SYNC_READBACK_PASS"
    closed.pop("dataset_sha256", None)
    closed["dataset_sha256"] = sha256_json(closed)
    return closed


def build_closed_dataset_bundle(
    dataset_bundle: dict[str, Any], closed_output_index: dict[str, Any]
) -> dict[str, Any]:
    closed_bundle = copy.deepcopy(dataset_bundle)
    if closed_output_index.get("dataset_key") != "TL_OUTPUT_INDEX":
        raise SyncError("closed output-index dataset key drift")
    closed_bundle["datasets"]["TL_OUTPUT_INDEX"] = copy.deepcopy(closed_output_index)
    closed_bundle.pop("bundle_sha256", None)
    closed_bundle["bundle_sha256"] = sha256_json(closed_bundle)
    return closed_bundle


def persist_closed_output_index(
    repo_root: Path,
    closed_dataset_bundle: dict[str, Any],
    closed_output_index: dict[str, Any],
) -> dict[str, str]:
    dataset_bundle_path = repo_root / CORRECTION_DIR / "dataset-bundle.json"
    sidecar_path = repo_root / CORRECTION_DIR / "datasets/TL_OUTPUT_INDEX.json"
    write_json(dataset_bundle_path, closed_dataset_bundle)
    write_json(sidecar_path, closed_output_index)
    if read_json(dataset_bundle_path) != closed_dataset_bundle or read_json(sidecar_path) != closed_output_index:
        raise SyncError("output-index closure local persistence mismatch")
    return {
        "dataset_bundle_sha256": closed_dataset_bundle["bundle_sha256"],
        "dataset_bundle_file_sha256": sha256_file(dataset_bundle_path),
        "output_index_dataset_sha256": closed_output_index["dataset_sha256"],
        "output_index_sidecar_file_sha256": sha256_file(sidecar_path),
    }


def build_output_index_closure_bundle(
    repo_root: Path,
    correction_readback: dict[str, Any],
    expires_at_ict: str,
    status_at_ict: str,
) -> dict[str, Any]:
    if correction_readback.get("status") != "SYNC_READBACK_PASS" or correction_readback.get("mismatch_count") != 0:
        raise SyncError("SYNC_READBACK_PASS correction evidence required")
    if correction_readback.get("authorized_external_mutations") != 0 or correction_readback.get("tab_count") != 24:
        raise SyncError("zero-mutation 24-tab recovery evidence required")
    sidecar_path = repo_root / CORRECTION_DIR / "datasets/TL_OUTPUT_INDEX.json"
    sidecar = read_json(sidecar_path)
    closed_sidecar = _closed_output_index_sidecar(sidecar, status_at_ict)
    dataset_bundle_path = repo_root / CORRECTION_DIR / "dataset-bundle.json"
    dataset_bundle = read_json(dataset_bundle_path)
    if dataset_bundle.get("datasets", {}).get("TL_OUTPUT_INDEX") != sidecar:
        raise SyncError("output-index sidecar/bundle drift")
    closed_dataset_bundle = build_closed_dataset_bundle(dataset_bundle, closed_sidecar)
    readback_path = repo_root / CORRECTION_DIR / "correction-readback.json"
    if read_json(readback_path) != correction_readback:
        raise SyncError("correction readback input drift")
    recovery_path = repo_root / CORRECTION_DIR / "recovery-bundle-unsigned.json"
    parent_path = repo_root / CORRECTION_DIR / "approval-bundle-unsigned.json"
    recovery = read_json(recovery_path)
    if recovery.get("bundle_id") != correction_readback.get("recovery_bundle_id"):
        raise SyncError("recovery bundle binding drift")
    output_tab = next((tab for tab in correction_readback.get("tabs", []) if tab.get("tab_key") == "TL_OUTPUT_INDEX"), None)
    if output_tab is None or output_tab.get("status") != "PASS":
        raise SyncError("TL_OUTPUT_INDEX recovery readback missing")
    columns = sidecar.get("columns", [])
    expected_columns = {"revision": "H", "updated_at_ict": "K", "sheet_delivery_state": "S", "readback_state": "T"}
    for field, column_name in expected_columns.items():
        if columns.index(field) + 1 != _column_number(column_name):
            raise SyncError(f"output-index column drift: {field}")
    row_count = len(sidecar["records"]) + 1
    if output_tab.get("range") != f"A1:T{row_count}":
        raise SyncError("output-index used-range drift")
    actions: list[dict[str, Any]] = []
    for field, column_name in expected_columns.items():
        values = [[str(record[field])] for record in closed_sidecar["records"]]
        old_values = [[str(record[field])] for record in sidecar["records"]]
        write_range = f"{column_name}2:{column_name}{row_count}"
        actions.append({
            "tab_key": "TL_OUTPUT_INDEX",
            "action": "REPLACE_VALUES",
            "field": field,
            "new_used_range": write_range,
            "approved_new_used_range": write_range,
            "max_rows": row_count,
            "max_columns": _column_number(column_name),
            "expected_old_values": old_values,
            "values": values,
        })
    bundle: dict[str, Any] = {
        "bundle_id": "TL-SHEET-RUN2-CORRECTION-01-CLOSURE-01",
        "approval_state": "DRAFT_UNSIGNED",
        "closure_mode": "OUTPUT_INDEX_STATUS_FINALIZE",
        "spreadsheet_id": TARGET_SPREADSHEET_ID,
        "service_account": TARGET_SERVICE_ACCOUNT,
        "operator": "Codex CLI",
        "expires_at_ict": expires_at_ict,
        "status_at_ict": status_at_ict,
        "schema_version": sidecar.get("schema_version"),
        "tab_key": "TL_OUTPUT_INDEX",
        "sheet_id": output_tab["sheet_id"],
        "full_readback_range": output_tab["range"],
        "parent_bundle_path": CORRECTION_DIR.joinpath("approval-bundle-unsigned.json").as_posix(),
        "parent_bundle_sha256": sha256_file(parent_path),
        "recovery_bundle_path": CORRECTION_DIR.joinpath("recovery-bundle-unsigned.json").as_posix(),
        "recovery_bundle_sha256": sha256_file(recovery_path),
        "correction_readback_path": CORRECTION_DIR.joinpath("correction-readback.json").as_posix(),
        "correction_readback_sha256": sha256_file(readback_path),
        "input_sidecar_path": CORRECTION_DIR.joinpath("datasets/TL_OUTPUT_INDEX.json").as_posix(),
        "input_sidecar_sha256": sha256_file(sidecar_path),
        "input_dataset_bundle_file_sha256": sha256_file(dataset_bundle_path),
        "before_bundle_sha256": dataset_bundle.get("bundle_sha256"),
        "after_bundle_sha256": closed_dataset_bundle["bundle_sha256"],
        "before_dataset_sha256": sidecar.get("dataset_sha256"),
        "after_dataset_sha256": closed_sidecar["dataset_sha256"],
        "before_matrix_sha256": sha256_json(matrix_for_dataset(sidecar)),
        "after_matrix_sha256": sha256_json(matrix_for_dataset(closed_sidecar)),
        "repository_bindings": {
            name: sha256_file(repo_root / relative_path)
            for name, relative_path in REPOSITORY_BINDING_PATHS.items()
        },
        "actions": actions,
        "readback_tabs": list(TAB_KEYS),
        "preserve_tabs": ["Trang tÃ­nh1", *[key for key in TAB_KEYS if key != "TL_OUTPUT_INDEX"]],
        "authorized_external_mutations": 1,
        "mutation_api_call_limit": 1,
        "automatic_rollback": False,
        "recovery_requires_new_approval": True,
    }
    bundle["scope_sha256"] = sha256_json({
        "tab_key": bundle["tab_key"],
        "sheet_id": bundle["sheet_id"],
        "actions": actions,
        "after_matrix_sha256": bundle["after_matrix_sha256"],
        "after_bundle_sha256": bundle["after_bundle_sha256"],
        "authorized_external_mutations": 1,
        "mutation_api_call_limit": 1,
        "preserve_tabs": bundle["preserve_tabs"],
    })
    return bundle


def validate_exact_output_index_closure_scope(
    approved: dict[str, Any], repo_root: Path, correction_readback: dict[str, Any]
) -> None:
    expected = build_output_index_closure_bundle(
        repo_root,
        correction_readback,
        str(approved.get("expires_at_ict", "")),
        str(approved.get("status_at_ict", "")),
    )
    actual = copy.deepcopy(approved)
    actual["approval_state"] = "DRAFT_UNSIGNED"
    if actual != expected:
        raise SyncError("output-index closure scope drift")


def record_partial_write(written_tabs: list[str], pending_tabs: list[str]) -> dict[str, Any]:
    return {"status": "VERIFY_FAILED", "written_tabs": written_tabs, "pending_tabs": pending_tabs, "automatic_rollback": False, "new_approval_required": True}


def verify_dataset_readback(expected: dict[str, Any], actual: dict[str, Any]) -> None:
    for field in ("sheet_id", "values", "formulas", "validations"):
        if expected.get(field) != actual.get(field):
            raise SyncError(f"readback mismatch: {field}")


def matrix_for_dataset(payload: dict[str, Any]) -> list[list[str]]:
    columns = payload["columns"]
    return [columns] + [[str(record[column]) for column in columns] for record in payload["records"]]


def build_correction_bundle(repo_root: Path, bundle: dict[str, Any], snapshot: dict[str, Any], expires_at_ict: str) -> dict[str, Any]:
    registry = load_registry(repo_root)
    if snapshot.get("spreadsheet_id") != TARGET_SPREADSHEET_ID:
        raise SyncError("snapshot wrong target")
    sheets = {sheet["title"]: sheet for sheet in snapshot.get("sheets", [])}
    if sheets.get("Trang tính1", {}).get("sheet_id") != 0:
        raise SyncError("Trang tính1 baseline drift")
    if set(sheets) != {"Trang tính1"}:
        raise SyncError("human-layer CREATE_TAB requires a default-tab-only workbook")
    validate_create_actions(TAB_KEYS, set(sheets))
    actions: list[dict[str, Any]] = []
    creates = [{"tab_key": title, "action": "CREATE_TAB"} for title in TAB_KEYS]
    old_ranges = {tab.get("tab_key"): tab.get("used_range") for tab in read_json(repo_root / "docs Toplink/staging/run2/codex/63-sheet-readback-v2.json").get("tabs", [])}
    for key in TAB_KEYS:
        payload = bundle["datasets"][key]
        schema = registry["datasets"][key]
        rows = len(payload["records"]) + 1
        columns = len(payload["columns"])
        new_range = f"A1:{_column_name(columns)}{rows}"
        old_range = old_ranges.get(key, "A1:A1")
        ranges = plan_bounded_replace(old_range, new_range)
        validation_fields = {"evidence_status": "evidence_status", "allowed_use": "allowed_use"}
        validation_fields.update(schema.get("field_enums", {}))
        validations = [
            {"field": field, "column_index": payload["columns"].index(field), "allowed_values": registry["enums"][enum_name]}
            for field, enum_name in validation_fields.items()
        ]
        actions.append({"tab_key": key, "action": "REPLACE_RANGE", "sheet_id": None, "old_used_range": old_range, "new_used_range": new_range, "approved_new_used_range": new_range, "clear_range": ranges["clear_range"], "max_rows": rows, "max_columns": columns, "dataset_sha256": payload["dataset_sha256"], "formatting": copy.deepcopy(registry["formatting"]), "validations": validations, "date_columns": [index for index, field in enumerate(payload["columns"]) if field.endswith("_at_ict")]})
    correction: dict[str, Any] = {
        "bundle_id": "TL-SHEET-RUN2-CORRECTION-01",
        "approval_state": "DRAFT_UNSIGNED",
        "spreadsheet_id": TARGET_SPREADSHEET_ID,
        "service_account": TARGET_SERVICE_ACCOUNT,
        "operator": "Codex CLI",
        "expires_at_ict": expires_at_ict,
        "schema_version": bundle["schema_version"],
        "dataset_bundle_sha256": bundle["bundle_sha256"],
        "snapshot_sha256": sha256_json(snapshot),
        "repository_bindings": {
            name: sha256_file(repo_root / relative_path)
            for name, relative_path in REPOSITORY_BINDING_PATHS.items()
        },
        "create_actions": creates,
        "actions": actions,
        "readback_tabs": list(TAB_KEYS),
        "preserve_tabs": ["Trang tính1"],
        "automatic_rollback": False,
        "recovery_requires_new_approval": True,
        "external_writes": 0,
    }
    correction["scope_sha256"] = sha256_json({"creates": creates, "actions": actions})
    return correction


def _snapshot_from_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
    sheets: list[dict[str, Any]] = []
    for item in metadata.get("sheets", []):
        properties = item.get("properties", item)
        sheets.append({"title": properties.get("title"), "sheet_id": properties.get("sheetId", properties.get("sheet_id")), "row_count": properties.get("gridProperties", {}).get("rowCount", properties.get("row_count")), "column_count": properties.get("gridProperties", {}).get("columnCount", properties.get("column_count")), "frozen_row_count": properties.get("gridProperties", {}).get("frozenRowCount", properties.get("frozen_row_count", 0))})
    return {"snapshot_id": "TL-SHEET-CORRECTION-SNAPSHOT-01", "spreadsheet_id": TARGET_SPREADSHEET_ID, "read_only": True, "sheets": sheets}


def validate_human_layer_target_snapshot(metadata: dict[str, Any], credential_email: str) -> dict[str, Any]:
    spreadsheet_id = metadata.get("spreadsheetId", TARGET_SPREADSHEET_ID)
    title = str(metadata.get("properties", {}).get("title", "")).strip()
    if spreadsheet_id != TARGET_SPREADSHEET_ID:
        raise SyncError("snapshot-target wrong spreadsheet id")
    if credential_email != TARGET_SERVICE_ACCOUNT:
        raise SyncError("snapshot-target wrong service account")
    if not title:
        raise SyncError("snapshot-target spreadsheet title missing")
    sheets = _snapshot_from_metadata(metadata)["sheets"]
    if any(str(sheet.get("title", "")).endswith("_v2") for sheet in sheets):
        raise SyncError("snapshot-target forbidden _v2 tab")
    if sheets != [next((sheet for sheet in sheets if sheet.get("title") == "Trang tính1"), {})]:
        raise SyncError("snapshot-target workbook must contain only Trang tính1")
    if not sheets or sheets[0].get("sheet_id") != 0:
        raise SyncError("snapshot-target Trang tính1 sheetId drift")
    return {
        "snapshot_id": "YV-HUMAN-LAYER-TARGET-SNAPSHOT-01",
        "spreadsheet_id": spreadsheet_id,
        "spreadsheet_title": title,
        "read_only": True,
        "api_read_pass": True,
        "credential_client_email": credential_email,
        "credential_email_match": True,
        "external_writes": 0,
        "sheets": sheets,
    }


def _google_service(expected_email: str) -> Any:
    credential_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not credential_path:
        raise SyncError("GOOGLE_APPLICATION_CREDENTIALS is not bound")
    credential_json = read_json(Path(credential_path))
    if credential_json.get("client_email") != expected_email:
        raise SyncError("wrong service account")
    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
    except ImportError as exc:
        raise SyncError("Google client libraries unavailable") from exc
    credentials = service_account.Credentials.from_service_account_file(credential_path, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    return build("sheets", "v4", credentials=credentials, cache_discovery=False)


def expected_native_sheet_state(action: dict[str, Any], sheet_id: int) -> dict[str, Any]:
    rows = int(action["max_rows"])
    columns = int(action["max_columns"])
    validation_map = {
        str(item["column_index"]): list(item["allowed_values"])
        for item in action["validations"]
    }
    return {
        "sheet_id": sheet_id,
        "frozen_rows": int(action["formatting"]["frozen_rows"]),
        "column_widths": [180] * columns,
        "wrap_cells": rows * columns,
        "header_cells": columns,
        "validation_cells": {column: rows - 1 for column in validation_map},
        "validation_values": validation_map,
        "date_cells": {str(column): rows - 1 for column in action.get("date_columns", [])},
        "date_format": action["formatting"]["date_format"],
    }


def normalize_native_sheet_state(sheet: dict[str, Any], action: dict[str, Any]) -> dict[str, Any]:
    properties = sheet.get("properties", {})
    grid = (sheet.get("data") or [{}])[0]
    row_data = grid.get("rowData", [])
    rows = int(action["max_rows"])
    columns = int(action["max_columns"])
    header_cells = 0
    wrap_cells = 0
    validation_counts = {str(item["column_index"]): 0 for item in action["validations"]}
    validation_values: dict[str, list[str]] = {}
    date_counts = {str(column): 0 for column in action.get("date_columns", [])}
    date_pattern = "NOT_AVAILABLE"
    for row_index in range(rows):
        cells = row_data[row_index].get("values", []) if row_index < len(row_data) else []
        for column_index in range(columns):
            cell = cells[column_index] if column_index < len(cells) else {}
            formatting = cell.get("userEnteredFormat", {})
            if formatting.get("wrapStrategy") == "WRAP":
                wrap_cells += 1
            if row_index == 0:
                background = formatting.get("backgroundColor", {})
                text_format = formatting.get("textFormat", {})
                color_ok = all(abs(float(background.get(name, -1)) - value) <= (1 / 255 + 0.0001) for name, value in (("red", 0.4196), ("green", 0.1216), ("blue", 0.2118)))
                foreground = text_format.get("foregroundColor", {})
                foreground_ok = all(abs(float(foreground.get(name, -1)) - 1.0) < 0.001 for name in ("red", "green", "blue"))
                if color_ok and foreground_ok and text_format.get("bold") is True:
                    header_cells += 1
            if row_index > 0 and str(column_index) in validation_counts:
                rule = cell.get("dataValidation", {})
                condition = rule.get("condition", {})
                if rule.get("strict") is True and condition.get("type") == "ONE_OF_LIST":
                    values = [item.get("userEnteredValue", "") for item in condition.get("values", [])]
                    validation_values[str(column_index)] = values
                    validation_counts[str(column_index)] += 1
            if row_index > 0 and str(column_index) in date_counts:
                number_format = formatting.get("numberFormat", {})
                if number_format.get("type") == "DATE_TIME":
                    date_pattern = number_format.get("pattern", "")
                    date_counts[str(column_index)] += 1
    widths = [item.get("pixelSize") for item in grid.get("columnMetadata", [])[:columns]]
    return {
        "sheet_id": properties.get("sheetId"),
        "frozen_rows": properties.get("gridProperties", {}).get("frozenRowCount", 0),
        "column_widths": widths,
        "wrap_cells": wrap_cells,
        "header_cells": header_cells,
        "validation_cells": validation_counts,
        "validation_values": validation_values,
        "date_cells": date_counts,
        "date_format": date_pattern if date_counts else action["formatting"]["date_format"],
    }


def verify_native_sheet_readback(action: dict[str, Any], sheet: dict[str, Any], sheet_id: int) -> None:
    if normalize_native_sheet_state(sheet, action) != expected_native_sheet_state(action, sheet_id):
        raise SyncError(f"native Sheet readback mismatch: {action['tab_key']}")


def verify_current_correction_readback(
    spreadsheets: Any,
    approved: dict[str, Any],
    dataset_bundle: dict[str, Any],
    frozen_snapshot: dict[str, Any],
) -> dict[str, Any]:
    metadata = spreadsheets.get(spreadsheetId=TARGET_SPREADSHEET_ID, fields="sheets.properties").execute()
    current = _snapshot_from_metadata(metadata)
    current_by_title = {sheet["title"]: sheet for sheet in current["sheets"]}
    if set(current_by_title) != {"Trang tính1", *TAB_KEYS}:
        raise SyncError("readback sheet registry drift")
    ranges = [f"'{action['tab_key']}'!{action['new_used_range']}" for action in approved["actions"]]
    preserved = next(sheet for sheet in frozen_snapshot["sheets"] if sheet["sheet_id"] == 0)
    preserved_range = preserved["baseline_range"]
    values_response = spreadsheets.values().batchGet(
        spreadsheetId=TARGET_SPREADSHEET_ID,
        ranges=ranges + [f"'{preserved['title']}'!{preserved_range}"],
        majorDimension="ROWS",
        valueRenderOption="FORMULA",
    ).execute()
    returned = values_response.get("valueRanges", [])
    if len(returned) != len(approved["actions"]) + 1:
        raise SyncError("partial correction readback")
    native = spreadsheets.get(
        spreadsheetId=TARGET_SPREADSHEET_ID,
        ranges=ranges,
        includeGridData=True,
        fields="sheets(properties(sheetId,title,gridProperties(frozenRowCount)),data(rowData(values(userEnteredFormat(wrapStrategy,backgroundColor,textFormat,numberFormat),dataValidation)),columnMetadata(pixelSize)))",
    ).execute()
    native_by_title = {sheet.get("properties", {}).get("title"): sheet for sheet in native.get("sheets", [])}
    evidence_tabs: list[dict[str, Any]] = []
    for action, actual in zip(approved["actions"], returned[:-1]):
        title = action["tab_key"]
        current_sheet_id = current_by_title[title]["sheet_id"]
        if current_sheet_id != action["sheet_id"]:
            raise SyncError(f"readback sheet ID mismatch: {title}")
        expected_values = matrix_for_dataset(dataset_bundle["datasets"][title])
        if expected_values != actual.get("values", []):
            raise SyncError(f"readback values/formulas mismatch: {title}")
        native_sheet = native_by_title.get(title)
        if native_sheet is None:
            raise SyncError(f"native Sheet readback missing: {title}")
        verify_native_sheet_readback(action, native_sheet, current_sheet_id)
        evidence_tabs.append({
            "tab_key": title,
            "sheet_id": current_sheet_id,
            "range": action["new_used_range"],
            "dataset_sha256": action["dataset_sha256"],
            "values_and_formulas": "PASS",
            "formatting_and_validation": "PASS",
            "status": "PASS",
        })
    if snapshot_values_digest(returned[-1].get("values", []), preserved_range) != preserved["baseline_digest"]:
        raise SyncError("Trang tính1 post-write drift")
    return {
        "record_id": "TL-SHEET-RUN2-CORRECTION-READBACK-01",
        "status": "SYNC_READBACK_PASS",
        "spreadsheet_id": TARGET_SPREADSHEET_ID,
        "tabs": evidence_tabs,
        "tab_count": len(evidence_tabs),
        "mismatch_count": 0,
        "preserved_trang_tinh1_sheet_id": current_by_title[preserved["title"]]["sheet_id"],
        "automatic_rollback": False,
    }


def capture_recovery_state(spreadsheets: Any, approved: dict[str, Any]) -> dict[str, Any]:
    metadata = spreadsheets.get(spreadsheetId=TARGET_SPREADSHEET_ID, fields="sheets.properties").execute()
    ranges = [f"'{action['tab_key']}'!{action['clear_range']}" for action in approved["actions"]]
    values = spreadsheets.values().batchGet(spreadsheetId=TARGET_SPREADSHEET_ID, ranges=ranges, majorDimension="ROWS").execute()
    return {"metadata": _snapshot_from_metadata(metadata), "ranges": values.get("valueRanges", [])}


def persist_partial_failure(
    repo_root: Path,
    approved: dict[str, Any],
    completed_phases: list[str],
    error: Exception,
    spreadsheets: Any,
) -> None:
    try:
        current_state = capture_recovery_state(spreadsheets, approved)
    except Exception as capture_error:
        current_state = {"capture_status": "FAILED", "error": str(capture_error)}
    all_tabs = [action["tab_key"] for action in approved["actions"]]
    written_tabs = all_tabs if "WRITE_DATASETS" in completed_phases else []
    pending_tabs = [] if written_tabs else all_tabs
    evidence = record_partial_write(written_tabs, pending_tabs)
    evidence.update({"bundle_id": approved["bundle_id"], "completed_phases": completed_phases, "error": str(error), "current_state": current_state})
    recovery = build_recovery_bundle(approved["bundle_id"], current_state)
    write_json(repo_root / CORRECTION_DIR / "correction-readback.json", evidence)
    write_json(repo_root / CORRECTION_DIR / "recovery-bundle-unsigned.json", recovery)


def execute_correction(repo_root: Path, approval_path: Path, statement: str) -> dict[str, Any]:
    approved = validate_approval_statement(approval_path, statement)
    validate_active_lease(repo_root)
    validate_repository_bindings(approved, repo_root)
    bundle = read_json(repo_root / CORRECTION_DIR / "dataset-bundle.json")
    frozen_snapshot = read_json(repo_root / CORRECTION_DIR / "target-snapshot.json")
    registry = load_registry(repo_root)
    validate_dataset_bundle(bundle, registry)
    validate_dataset_sidecars(bundle, repo_root / CORRECTION_DIR / "datasets")
    if approved.get("dataset_bundle_sha256") != bundle.get("bundle_sha256"):
        raise SyncError("approved dataset digest drift")
    if approved.get("snapshot_sha256") != sha256_json(frozen_snapshot):
        raise SyncError("approved snapshot digest drift")
    validate_exact_correction_scope(approved, repo_root, bundle, frozen_snapshot)
    service = _google_service(TARGET_SERVICE_ACCOUNT)
    spreadsheets = service.spreadsheets()
    metadata = spreadsheets.get(spreadsheetId=TARGET_SPREADSHEET_ID, fields="sheets.properties").execute()
    current = _snapshot_from_metadata(metadata)
    frozen_value_sheets = [
        sheet for sheet in frozen_snapshot["sheets"]
        if sheet.get("values_digest") or sheet.get("baseline_digest")
    ]
    baseline_ranges = [
        f"'{sheet['title']}'!{sheet.get('used_range', sheet.get('baseline_range'))}"
        for sheet in frozen_value_sheets
    ]
    baseline_response = spreadsheets.values().batchGet(
        spreadsheetId=TARGET_SPREADSHEET_ID,
        ranges=baseline_ranges,
        majorDimension="ROWS",
    ).execute()
    baseline_returned = baseline_response.get("valueRanges", [])
    if len(baseline_returned) != len(frozen_value_sheets):
        raise SyncError("partial live baseline readback")
    live_values = {
        sheet["title"]: {
            "range": sheet.get("used_range", sheet.get("baseline_range")),
            "digest": snapshot_values_digest(actual.get("values", []), sheet.get("used_range", sheet.get("baseline_range"))),
        }
        for sheet, actual in zip(frozen_value_sheets, baseline_returned)
    }
    validate_live_baseline(approved, frozen_snapshot, current["sheets"], live_values)
    current_titles = {sheet["title"] for sheet in current["sheets"]}
    validate_create_actions([item["tab_key"] for item in approved["create_actions"]], current_titles)
    completed_phases: list[str] = []

    def guarded_mutation(phase: str, operation: Any) -> Any:
        try:
            result = operation()
        except Exception as exc:
            persist_partial_failure(repo_root, approved, completed_phases, exc, spreadsheets)
            raise
        completed_phases.append(phase)
        return result

    def guarded_post_mutation(operation: Any) -> Any:
        try:
            return operation()
        except Exception as exc:
            persist_partial_failure(repo_root, approved, completed_phases, exc, spreadsheets)
            raise

    requests = [{"addSheet": {"properties": {"title": item["tab_key"], "gridProperties": {"rowCount": 100, "columnCount": 26, "frozenRowCount": 1}}}} for item in approved["create_actions"]]
    if requests:
        guarded_mutation("CREATE_TAB", lambda: spreadsheets.batchUpdate(spreadsheetId=TARGET_SPREADSHEET_ID, body={"requests": requests}).execute())
    metadata = guarded_post_mutation(lambda: spreadsheets.get(spreadsheetId=TARGET_SPREADSHEET_ID, fields="sheets.properties").execute())
    post_create = _snapshot_from_metadata(metadata)
    by_title = {sheet["title"]: sheet for sheet in post_create["sheets"]}
    def validate_post_create_ids() -> None:
        if by_title.get("Trang tính1", {}).get("sheet_id") != 0:
            raise SyncError("Trang tính1 drift after CREATE_TAB")
        if set(by_title) != {"Trang tính1", *TAB_KEYS}:
            raise SyncError("human-layer sheet registry drift after CREATE_TAB")
    guarded_post_mutation(validate_post_create_ids)
    clear_ranges = [f"'{action['tab_key']}'!{action['clear_range']}" for action in approved["actions"]]
    guarded_mutation("CLEAR_BOUNDED_RANGES", lambda: spreadsheets.values().batchClear(spreadsheetId=TARGET_SPREADSHEET_ID, body={"ranges": clear_ranges}).execute())
    data = [{"range": f"'{action['tab_key']}'!{action['new_used_range']}", "majorDimension": "ROWS", "values": matrix_for_dataset(bundle["datasets"][action["tab_key"]])} for action in approved["actions"]]
    guarded_mutation("WRITE_DATASETS", lambda: spreadsheets.values().batchUpdate(spreadsheetId=TARGET_SPREADSHEET_ID, body={"valueInputOption": "RAW", "data": data}).execute())
    format_requests: list[dict[str, Any]] = []
    for action in approved["actions"]:
        sheet_id = by_title[action["tab_key"]]["sheet_id"]
        row_count = int(action["max_rows"])
        column_count = int(action["max_columns"])
        formatting = action["formatting"]
        format_requests.extend([
            {"updateSheetProperties": {"properties": {"sheetId": sheet_id, "gridProperties": {"frozenRowCount": int(formatting["frozen_rows"])}}, "fields": "gridProperties.frozenRowCount"}},
            {"repeatCell": {"range": {"sheetId": sheet_id, "startRowIndex": 0, "endRowIndex": row_count, "startColumnIndex": 0, "endColumnIndex": column_count}, "cell": {"userEnteredFormat": {"wrapStrategy": "WRAP"}}, "fields": "userEnteredFormat.wrapStrategy"}},
            {"repeatCell": {"range": {"sheetId": sheet_id, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 0, "endColumnIndex": column_count}, "cell": {"userEnteredFormat": {"backgroundColor": {"red": 0.4196, "green": 0.1216, "blue": 0.2118}, "textFormat": {"foregroundColor": {"red": 1, "green": 1, "blue": 1}, "bold": True}}}, "fields": "userEnteredFormat(backgroundColor,textFormat)"}},
            {"updateDimensionProperties": {"range": {"sheetId": sheet_id, "dimension": "COLUMNS", "startIndex": 0, "endIndex": column_count}, "properties": {"pixelSize": 180}, "fields": "pixelSize"}},
        ])
        for validation in action["validations"]:
            column = int(validation["column_index"])
            format_requests.append({"setDataValidation": {"range": {"sheetId": sheet_id, "startRowIndex": 1, "endRowIndex": row_count, "startColumnIndex": column, "endColumnIndex": column + 1}, "rule": {"condition": {"type": "ONE_OF_LIST", "values": [{"userEnteredValue": value} for value in validation["allowed_values"]]}, "strict": True, "showCustomUi": True}}})
        for column in action.get("date_columns", []):
            format_requests.append({"repeatCell": {"range": {"sheetId": sheet_id, "startRowIndex": 1, "endRowIndex": row_count, "startColumnIndex": column, "endColumnIndex": column + 1}, "cell": {"userEnteredFormat": {"numberFormat": {"type": "DATE_TIME", "pattern": formatting["date_format"]}}}, "fields": "userEnteredFormat.numberFormat"}})
    guarded_mutation("FORMAT_AND_VALIDATE", lambda: spreadsheets.batchUpdate(spreadsheetId=TARGET_SPREADSHEET_ID, body={"requests": format_requests}).execute())
    preserved_sheet = next(sheet for sheet in frozen_snapshot["sheets"] if sheet["title"] == "Trang tính1")
    preserved_range = preserved_sheet["baseline_range"]
    readback_ranges = [item["range"] for item in data] + [f"'Trang tính1'!{preserved_range}"]
    readback = guarded_post_mutation(lambda: spreadsheets.values().batchGet(spreadsheetId=TARGET_SPREADSHEET_ID, ranges=readback_ranges, majorDimension="ROWS", valueRenderOption="FORMULA").execute())
    returned = readback.get("valueRanges", [])
    native = guarded_post_mutation(lambda: spreadsheets.get(
        spreadsheetId=TARGET_SPREADSHEET_ID,
        ranges=[item["range"] for item in data],
        includeGridData=True,
        fields="sheets(properties(sheetId,title,gridProperties(frozenRowCount)),data(rowData(values(userEnteredFormat(wrapStrategy,backgroundColor,textFormat,numberFormat),dataValidation)),columnMetadata(pixelSize)))",
    ).execute())
    native_by_title = {sheet.get("properties", {}).get("title"): sheet for sheet in native.get("sheets", [])}

    def verify_post_write() -> dict[str, Any]:
        if len(returned) != len(data) + 1:
            raise SyncError("partial write readback")
        evidence_tabs: list[dict[str, Any]] = []
        for action, actual in zip(approved["actions"], returned[: len(data)]):
            expected_values = matrix_for_dataset(bundle["datasets"][action["tab_key"]])
            actual_values = actual.get("values", [])
            if expected_values != actual_values:
                raise SyncError(f"readback values/formulas mismatch: {action['tab_key']}")
            sheet_id = by_title[action["tab_key"]]["sheet_id"]
            native_sheet = native_by_title.get(action["tab_key"])
            if native_sheet is None:
                raise SyncError(f"native Sheet readback missing: {action['tab_key']}")
            verify_native_sheet_readback(action, native_sheet, sheet_id)
            evidence_tabs.append({"tab_key": action["tab_key"], "sheet_id": sheet_id, "range": action["new_used_range"], "dataset_sha256": action["dataset_sha256"], "values_and_formulas": "PASS", "formatting_and_validation": "PASS", "status": "PASS"})
        if snapshot_values_digest(returned[-1].get("values", []), preserved_range) != preserved_sheet["baseline_digest"]:
            raise SyncError("Trang tính1 post-write drift")
        return {"record_id": "TL-SHEET-RUN2-CORRECTION-READBACK-01", "status": "SYNC_READBACK_PASS", "spreadsheet_id": TARGET_SPREADSHEET_ID, "tabs": evidence_tabs, "tab_count": len(evidence_tabs), "mismatch_count": 0, "preserved_trang_tinh1_sheet_id": by_title.get("Trang tính1", {}).get("sheet_id"), "automatic_rollback": False}

    return guarded_post_mutation(verify_post_write)


def _repo_root(value: str | None) -> Path:
    return Path(value).resolve() if value else Path(__file__).resolve().parents[2]


def _compile_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    bundle = compile_datasets(repo_root)
    output = repo_root / YV_COMPILED_DIR
    write_json(output / "dataset-bundle.json", bundle)
    write_dataset_sidecars(bundle, output / "datasets")
    print(json.dumps({"status": "PASS", "datasets": 21, "bundle_sha256": bundle["bundle_sha256"]}, ensure_ascii=False))
    return 0


def _validate_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    bundle = read_json(repo_root / YV_COMPILED_DIR / "dataset-bundle.json")
    registry = load_registry(repo_root)
    validate_dataset_bundle(bundle, registry)
    validate_source_digests(bundle, repo_root)
    validate_human_layer_bundle(bundle, repo_root)
    validate_dataset_sidecars(bundle, repo_root / YV_COMPILED_DIR / "datasets")
    print(json.dumps({"status": "PASS", "datasets": 21}, ensure_ascii=False))
    return 0


def _snapshot_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    validate_active_lease(repo_root)
    if args.metadata_json:
        metadata = read_json(Path(args.metadata_json))
        credential_email = str(metadata.pop("credential_client_email", ""))
    else:
        credential_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        if not credential_path:
            raise SyncError("GOOGLE_APPLICATION_CREDENTIALS is not bound")
        credential_email = str(read_json(Path(credential_path)).get("client_email", ""))
        service = _google_service(TARGET_SERVICE_ACCOUNT)
        metadata = service.spreadsheets().get(
            spreadsheetId=TARGET_SPREADSHEET_ID,
            fields="spreadsheetId,properties.title,sheets.properties(sheetId,title,index,gridProperties)",
        ).execute()
    snapshot = validate_human_layer_target_snapshot(metadata, credential_email)
    output = repo_root / "staging/yv-humanize/target-snapshot.json"
    write_json(output, snapshot)
    print(json.dumps({"status": "PASS", "sheet_count": 1, "spreadsheet_title": snapshot["spreadsheet_title"], "external_writes": 0, "output": output.as_posix()}, ensure_ascii=True))
    return 0


def _build_bundle_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    datasets = read_json(repo_root / CORRECTION_DIR / "dataset-bundle.json")
    snapshot = read_json(repo_root / CORRECTION_DIR / "target-snapshot.json")
    correction = build_correction_bundle(repo_root, datasets, snapshot, args.expires_at_ict)
    path = repo_root / CORRECTION_DIR / "approval-bundle-unsigned.json"
    write_json(path, correction)
    print(json.dumps({"status": "DRAFT_UNSIGNED", "path": path.relative_to(repo_root).as_posix(), "sha256": sha256_file(path)}, ensure_ascii=False))
    return 0


def _build_recovery_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    parent = read_json(repo_root / CORRECTION_DIR / "approval-bundle-unsigned.json")
    partial = read_json(repo_root / CORRECTION_DIR / "correction-readback.json")
    recovery = build_verify_only_recovery_bundle(repo_root, parent, partial, args.expires_at_ict)
    path = repo_root / CORRECTION_DIR / "recovery-bundle-unsigned.json"
    write_json(path, recovery)
    print(json.dumps({"status": "DRAFT_UNSIGNED", "mode": "EXACT_READBACK_ONLY", "path": path.relative_to(repo_root).as_posix(), "sha256": sha256_file(path), "authorized_external_mutations": 0}, ensure_ascii=False))
    return 0


def _build_output_index_closure_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    readback = read_json(repo_root / CORRECTION_DIR / "correction-readback.json")
    closure = build_output_index_closure_bundle(
        repo_root, readback, args.expires_at_ict, args.status_at_ict
    )
    path = repo_root / CORRECTION_DIR / "output-index-closure-bundle-unsigned.json"
    write_json(path, closure)
    print(json.dumps({
        "status": "DRAFT_UNSIGNED",
        "mode": closure["closure_mode"],
        "path": path.relative_to(repo_root).as_posix(),
        "sha256": sha256_file(path),
        "authorized_external_mutations": 1,
        "mutation_api_call_limit": 1,
    }, ensure_ascii=False))
    return 0


def _validate_approval_command(args: argparse.Namespace) -> int:
    validate_approval_statement(Path(args.approval_path), args.approval_statement)
    print(json.dumps({"status": "PASS"}))
    return 0


def _execute_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    try:
        evidence = execute_correction(repo_root, Path(args.approval_path), args.approval_statement)
    except SyncError:
        raise
    write_json(repo_root / CORRECTION_DIR / "correction-readback.json", evidence)
    print(json.dumps({"status": evidence["status"], "tab_count": evidence["tab_count"]}, ensure_ascii=False))
    return 0


def _execute_recovery_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    approval_path = Path(args.approval_path)
    approved = validate_approval_statement(approval_path, args.approval_statement)
    if approved.get("recovery_mode") != "EXACT_READBACK_ONLY" or approved.get("authorized_external_mutations") != 0:
        raise SyncError("verify-only recovery approval required")
    validate_active_lease(repo_root)
    validate_repository_bindings(approved, repo_root)
    parent_path = repo_root / CORRECTION_DIR / "approval-bundle-unsigned.json"
    partial_path = repo_root / CORRECTION_DIR / "correction-readback.json"
    if approved.get("parent_bundle_sha256") != sha256_file(parent_path):
        raise SyncError("recovery parent bundle digest drift")
    if approved.get("partial_failure_sha256") != sha256_file(partial_path):
        raise SyncError("recovery partial-failure digest drift")
    parent = read_json(parent_path)
    partial = read_json(partial_path)
    if approved.get("current_state_sha256") != sha256_json(partial.get("current_state")):
        raise SyncError("recovery current-state digest drift")
    dataset_bundle = read_json(repo_root / CORRECTION_DIR / "dataset-bundle.json")
    frozen_snapshot = read_json(repo_root / CORRECTION_DIR / "target-snapshot.json")
    registry = load_registry(repo_root)
    validate_dataset_bundle(dataset_bundle, registry)
    validate_source_digests(dataset_bundle, repo_root)
    validate_dataset_sidecars(dataset_bundle, repo_root / CORRECTION_DIR / "datasets")
    if approved.get("dataset_bundle_sha256") != dataset_bundle.get("bundle_sha256"):
        raise SyncError("recovery dataset digest drift")
    if approved.get("snapshot_sha256") != sha256_json(frozen_snapshot):
        raise SyncError("recovery snapshot digest drift")
    validate_exact_recovery_scope(approved, repo_root, parent, partial)
    service = _google_service(TARGET_SERVICE_ACCOUNT)
    evidence = verify_current_correction_readback(service.spreadsheets(), approved, dataset_bundle, frozen_snapshot)
    evidence.update({
        "recovery_bundle_id": approved["bundle_id"],
        "recovery_bundle_sha256": sha256_file(approval_path),
        "recovery_mode": "EXACT_READBACK_ONLY",
        "authorized_external_mutations": 0,
        "prior_verify_failed_sha256": approved["partial_failure_sha256"],
        "mutation_phases_from_parent": partial["completed_phases"],
    })
    write_json(partial_path, evidence)
    print(json.dumps({"status": evidence["status"], "tab_count": evidence["tab_count"], "authorized_external_mutations": 0}, ensure_ascii=False))
    return 0


def _verify_output_index_closure_values(
    spreadsheets: Any,
    correction_readback: dict[str, Any],
    parent: dict[str, Any],
    dataset_bundle: dict[str, Any],
    output_index_payload: dict[str, Any],
    frozen_snapshot: dict[str, Any],
) -> dict[str, Any]:
    metadata = spreadsheets.get(
        spreadsheetId=TARGET_SPREADSHEET_ID, fields="sheets.properties"
    ).execute()
    current = _snapshot_from_metadata(metadata)
    by_title = {sheet["title"]: sheet for sheet in current["sheets"]}
    if set(by_title) != {"Trang tÃ­nh1", *TAB_KEYS}:
        raise SyncError("closure live sheet registry drift")
    expected_ids = {tab["tab_key"]: tab["sheet_id"] for tab in correction_readback["tabs"]}
    for title, sheet_id in expected_ids.items():
        if by_title.get(title, {}).get("sheet_id") != sheet_id:
            raise SyncError(f"closure live sheet ID drift: {title}")
    actions = parent["actions"]
    preserved = next(sheet for sheet in frozen_snapshot["sheets"] if sheet["sheet_id"] == 0)
    ranges = [f"'{action['tab_key']}'!{action['new_used_range']}" for action in actions]
    ranges.append(f"'{preserved['title']}'!{preserved['baseline_range']}")
    response = spreadsheets.values().batchGet(
        spreadsheetId=TARGET_SPREADSHEET_ID,
        ranges=ranges,
        majorDimension="ROWS",
        valueRenderOption="FORMULA",
    ).execute()
    returned = response.get("valueRanges", [])
    if len(returned) != len(actions) + 1:
        raise SyncError("partial output-index closure readback")
    evidence_tabs: list[dict[str, Any]] = []
    for action, actual in zip(actions, returned[:-1]):
        title = action["tab_key"]
        payload = output_index_payload if title == "TL_OUTPUT_INDEX" else dataset_bundle["datasets"][title]
        if matrix_for_dataset(payload) != actual.get("values", []):
            raise SyncError(f"closure values/formulas mismatch: {title}")
        evidence_tabs.append({
            "tab_key": title,
            "sheet_id": by_title[title]["sheet_id"],
            "range": action["new_used_range"],
            "status": "PASS",
        })
    if snapshot_values_digest(returned[-1].get("values", []), preserved["baseline_range"]) != preserved["baseline_digest"]:
        raise SyncError("Trang tÃ­nh1 closure drift")
    return {
        "tabs": evidence_tabs,
        "tab_count": len(evidence_tabs),
        "preserved_trang_tinh1_sheet_id": by_title[preserved["title"]]["sheet_id"],
    }


def _execute_output_index_closure_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    approval_path = Path(args.approval_path)
    approved = validate_approval_statement(approval_path, args.approval_statement)
    if approved.get("closure_mode") != "OUTPUT_INDEX_STATUS_FINALIZE":
        raise SyncError("output-index closure approval required")
    if approved.get("authorized_external_mutations") != 1 or approved.get("mutation_api_call_limit") != 1:
        raise SyncError("output-index closure mutation scope drift")
    validate_active_lease(repo_root)
    validate_repository_bindings(approved, repo_root)
    readback_path = repo_root / CORRECTION_DIR / "correction-readback.json"
    recovery_path = repo_root / CORRECTION_DIR / "recovery-bundle-unsigned.json"
    parent_path = repo_root / CORRECTION_DIR / "approval-bundle-unsigned.json"
    sidecar_path = repo_root / CORRECTION_DIR / "datasets/TL_OUTPUT_INDEX.json"
    dataset_bundle_path = repo_root / CORRECTION_DIR / "dataset-bundle.json"
    for field, path in (
        ("correction_readback_sha256", readback_path),
        ("recovery_bundle_sha256", recovery_path),
        ("parent_bundle_sha256", parent_path),
        ("input_sidecar_sha256", sidecar_path),
        ("input_dataset_bundle_file_sha256", dataset_bundle_path),
    ):
        if approved.get(field) != sha256_file(path):
            raise SyncError(f"output-index closure {field} drift")
    correction_readback = read_json(readback_path)
    validate_exact_output_index_closure_scope(approved, repo_root, correction_readback)
    parent = read_json(parent_path)
    dataset_bundle = read_json(dataset_bundle_path)
    frozen_snapshot = read_json(repo_root / CORRECTION_DIR / "target-snapshot.json")
    registry = load_registry(repo_root)
    validate_dataset_bundle(dataset_bundle, registry)
    validate_source_digests(dataset_bundle, repo_root)
    validate_dataset_sidecars(dataset_bundle, repo_root / CORRECTION_DIR / "datasets")
    original_sidecar = read_json(sidecar_path)
    closed_sidecar = _closed_output_index_sidecar(original_sidecar, approved["status_at_ict"])
    closed_dataset_bundle = build_closed_dataset_bundle(dataset_bundle, closed_sidecar)
    if approved.get("before_matrix_sha256") != sha256_json(matrix_for_dataset(original_sidecar)):
        raise SyncError("output-index closure before-matrix drift")
    if approved.get("after_matrix_sha256") != sha256_json(matrix_for_dataset(closed_sidecar)):
        raise SyncError("output-index closure after-matrix drift")
    if approved.get("before_bundle_sha256") != dataset_bundle.get("bundle_sha256"):
        raise SyncError("output-index closure before-bundle drift")
    if approved.get("after_bundle_sha256") != closed_dataset_bundle.get("bundle_sha256"):
        raise SyncError("output-index closure after-bundle drift")
    validate_dataset_bundle(closed_dataset_bundle, registry)
    validate_source_digests(closed_dataset_bundle, repo_root)
    service = _google_service(TARGET_SERVICE_ACCOUNT)
    spreadsheets = service.spreadsheets()
    _verify_output_index_closure_values(
        spreadsheets, correction_readback, parent, dataset_bundle, original_sidecar, frozen_snapshot
    )
    mutation_started = False
    try:
        mutation_started = True
        data = [{
            "range": f"'TL_OUTPUT_INDEX'!{action['approved_new_used_range']}",
            "majorDimension": "ROWS",
            "values": action["values"],
        } for action in approved["actions"]]
        spreadsheets.values().batchUpdate(
            spreadsheetId=TARGET_SPREADSHEET_ID,
            body={"valueInputOption": "RAW", "data": data},
        ).execute()
        verified = _verify_output_index_closure_values(
            spreadsheets, correction_readback, parent, dataset_bundle, closed_sidecar, frozen_snapshot
        )
        persisted = persist_closed_output_index(repo_root, closed_dataset_bundle, closed_sidecar)
    except Exception as exc:
        if mutation_started:
            failure = {
                "record_id": "TL-SHEET-RUN2-OUTPUT-INDEX-CLOSURE-READBACK-01",
                "status": "CLOSURE_VERIFY_FAILED",
                "bundle_id": approved["bundle_id"],
                "error": str(exc),
                "automatic_rollback": False,
                "new_approval_required": True,
                "authorized_external_mutations": 1,
                "mutation_api_calls_attempted": 1,
            }
            failure_path = repo_root / CORRECTION_DIR / "output-index-closure-readback.json"
            write_json(failure_path, failure)
            recovery = build_recovery_bundle(approved["bundle_id"], failure)
            write_json(repo_root / CORRECTION_DIR / "output-index-closure-recovery-bundle-unsigned.json", recovery)
        raise
    evidence = {
        "record_id": "TL-SHEET-RUN2-OUTPUT-INDEX-CLOSURE-READBACK-01",
        "status": "SYNC_READBACK_PASS",
        "bundle_id": approved["bundle_id"],
        "bundle_sha256": sha256_file(approval_path),
        "spreadsheet_id": TARGET_SPREADSHEET_ID,
        "tab_key": "TL_OUTPUT_INDEX",
        "sheet_id": approved["sheet_id"],
        "range": approved["full_readback_range"],
        "updated_records": 14,
        "sheet_delivery_state": "SYNC_READBACK_PASS",
        "readback_state": "SYNC_READBACK_PASS",
        **persisted,
        "tabs": verified["tabs"],
        "tab_count": verified["tab_count"],
        "mismatch_count": 0,
        "preserved_trang_tinh1_sheet_id": verified["preserved_trang_tinh1_sheet_id"],
        "authorized_external_mutations": 1,
        "mutation_api_calls": 1,
        "automatic_rollback": False,
    }
    path = repo_root / CORRECTION_DIR / "output-index-closure-readback.json"
    write_json(path, evidence)
    print(json.dumps({
        "status": evidence["status"],
        "tab_count": evidence["tab_count"],
        "updated_records": 14,
        "mutation_api_calls": 1,
    }, ensure_ascii=False))
    return 0


# ---------------------------------------------------------------------------
# Y Viện human-layer compiler (YV-SHEET-001/1.0.0)

YV_REGISTRY_PATH = Path("docs/system/yvien-sheet-dataset-registry.json")
YV_PLAN_PATH = Path("staging/yv-humanize/report-plan.json")
YV_COMPILED_DIR = Path("staging/yv-humanize/compiled")
YV_MACHINE_HEADERS = {"Mã", "Chủ sở hữu"}
YV_HIDDEN_HEADERS = ["_key", "_audit"]
YV_YELLOW_PREFIX = "CHƯA CHỐT — "
YV_FALLBACK_PREFIX = "DỰ PHÒNG — "
YV_FORMULA_LEADERS = ("+", "=", "-", "@")


def _yv_parse_tables(path: Path) -> list[dict[str, Any]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    tables: list[dict[str, Any]] = []
    index = 0
    separator = re.compile(r"^\|\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")

    def split_row(line: str) -> list[str]:
        stripped = line.strip().removeprefix("|").removesuffix("|")
        return [cell.strip() for cell in stripped.split("|")]

    while index < len(lines) - 1:
        if lines[index].lstrip().startswith("|") and separator.match(lines[index + 1].strip()):
            headers = split_row(lines[index])
            rows: list[dict[str, Any]] = []
            cursor = index + 2
            while cursor < len(lines) and lines[cursor].lstrip().startswith("|"):
                values = split_row(lines[cursor])
                if len(values) > len(headers):
                    raise SyncError(f"markdown row wider than header: {path}:{cursor + 1}")
                values.extend([""] * (len(headers) - len(values)))
                rows.append({"values": values, "line": cursor + 1})
                cursor += 1
            tables.append({"headers": headers, "rows": rows, "line": index + 1})
            index = cursor
        else:
            index += 1
    return tables


def load_human_layer_registry(repo_root: Path) -> dict[str, Any]:
    registry = read_json(repo_root / YV_REGISTRY_PATH)
    if registry.get("schema_version") != "YV-SHEET-001/1.0.0":
        raise SyncError("human-layer registry version drift")
    tabs = registry.get("tabs")
    if not isinstance(tabs, list) or len(tabs) != 21:
        raise SyncError("human-layer registry must contain 21 tabs")
    return registry


def _yv_display_headers(block: dict[str, Any]) -> list[str]:
    return [item["header"] for item in sorted(block["display_columns"], key=lambda item: item["pos"])]


def _yv_specs(registry: dict[str, Any]) -> list[dict[str, Any]]:
    specs: list[dict[str, Any]] = []
    for tab in sorted(registry["tabs"], key=lambda item: item["index"]):
        base = {
            "tab": tab["tab"],
            "index": tab["index"],
            "grid_width": tab["grid_width"],
            "hidden_columns": tab["hidden_columns"],
            "source_markdown": tab.get("source_markdown", []),
            "id_exposure_scope": tab.get("id_exposure_scope", []),
            "generated_columns": tab.get("generated_columns", []),
            "evidence_status": tab["default_evidence_status"],
            "allowed_use": tab["default_allowed_use"],
        }
        blocks = tab.get("sections") or [tab]
        for block in blocks:
            specs.append(
                {
                    **base,
                    "section": block.get("section_id"),
                    "heading": block.get("heading"),
                    "headers": _yv_display_headers(block),
                    "min_records": block.get("min_records"),
                    "max_records": block.get("max_records"),
                }
            )
    return specs


def _yv_expected_headers(spec: dict[str, Any]) -> set[str]:
    generated = {item["header"] for item in spec["generated_columns"]}
    return set(spec["headers"]) - generated


def _yv_select_table(
    repo_root: Path, spec: dict[str, Any], expected: set[str] | None = None
) -> tuple[str, dict[str, Any]]:
    wanted = expected if expected is not None else _yv_expected_headers(spec)
    exposed = set(spec["id_exposure_scope"])
    matches: list[tuple[str, dict[str, Any]]] = []
    for relative in spec["source_markdown"]:
        path = repo_root / relative
        if not path.is_file():
            raise SyncError(f"missing human-layer source: {relative}")
        for table in _yv_parse_tables(path):
            if not table["rows"] or not table["headers"] or table["headers"][0] != "Mã":
                continue
            actual = {header for header in table["headers"] if header not in YV_MACHINE_HEADERS or header in exposed}
            if actual == wanted:
                matches.append((relative, table))
    label = spec["tab"] + (f" §{spec['section']}" if spec["section"] else "")
    if len(matches) != 1:
        raise SyncError(f"{label}: expected one exact markdown table, found {len(matches)}")
    return matches[0]


def _yv_rows(relative: str, table: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for raw in table["rows"]:
        cells = dict(zip(table["headers"], raw["values"]))
        if not cells.get("Mã"):
            raise SyncError(f"missing row identity: {relative}:L{raw['line']}")
        cells["__source_path"] = relative
        cells["__source_location"] = f"L{raw['line']}"
        rows.append(cells)
    return rows


def _yv_escape(value: str) -> str:
    return "'" + value if value and value[0] in YV_FORMULA_LEADERS else value


def _yv_column(index: int) -> str:
    value = index + 1
    output = ""
    while value:
        value, remainder = divmod(value - 1, 26)
        output = chr(65 + remainder) + output
    return output


def _yv_content_hash(values: list[list[str]]) -> str:
    encoded = json.dumps(values, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _yv_audit(
    registry: dict[str, Any], spec: dict[str, Any], cells: dict[str, str], digest: str
) -> str:
    key = cells["Mã"]
    return " · ".join(
        [
            f"{spec['tab']}:{key}",
            f"{cells['__source_path']}#{cells['__source_location']}",
            key,
            spec["evidence_status"],
            spec["allowed_use"],
            registry["schema_version"],
            digest,
            cells.get("Chủ sở hữu") or "—",
            registry["created_at_ict"],
        ]
    )


def _yv_emit(
    registry: dict[str, Any], spec: dict[str, Any], records: list[dict[str, str]], digests: dict[str, str]
) -> list[list[str]]:
    generated = {item["header"] for item in spec["generated_columns"]}
    emitted: list[list[str]] = []
    for ordinal, cells in enumerate(records, start=1):
        row: list[str] = []
        for header in spec["headers"]:
            if header in generated:
                row.append(str(ordinal))
            elif header not in cells:
                raise SyncError(f"{spec['tab']}:{cells['Mã']} missing column {header}")
            else:
                row.append(_yv_escape(cells[header] or "—"))
        relative = cells["__source_path"]
        if relative not in digests:
            raise SyncError(f"source digest not bound: {relative}")
        row.extend([cells["Mã"], _yv_audit(registry, spec, cells, digests[relative])])
        emitted.append(row)
    return emitted


def _yv_calendar(repo_root: Path, spec: dict[str, Any]) -> list[dict[str, str]]:
    wanted = (_yv_expected_headers(spec) - {"Hướng", "Nói gì"}) | {"Ba hướng A / B / C", "Angle chính"}
    relative, table = _yv_select_table(repo_root, spec, wanted)
    records: list[dict[str, str]] = []
    for cells in _yv_rows(relative, table):
        for option, body in _split_options(cells["Ba hướng A / B / C"]):
            row = dict(cells)
            row["Hướng"] = option
            row["Nói gì"] = body[:1].upper() + body[1:] if option == "A" else YV_FALLBACK_PREFIX + body
            row["Mã"] = f"{cells['Mã']}-{option}"
            row["__option_body"] = body
            records.append(row)
    return records


YV_REVIEWER_BY_LEG = {"R1": "Phụ trách truyền thông", "R2": "rà cơ chế video", "R3": "người có chuyên môn"}
YV_HEALTH_PILLARS = ("Hiểu và lắng nghe tín hiệu cơ thể", "Lý – Dược – Dưỡng dễ hiểu")
YV_FOUNDER_PILLAR = "Hành trình Y Viện, founder và cộng đồng"
YV_PRODUCT_DAYS = ("D-14", "D-26")
YV_FOUNDER_DAYS = ("D-5", "D-20", "D-24", "D-28")
YV_FUNNEL_METRIC = {"TOFU": "Chỉ số tiếp cận và tỷ lệ xem hết Reel", "MOFU": "Lượt lưu, lượt chia sẻ và số câu hỏi về quy trình"}
YV_DMP_CHECK = (
    "Đạt 7 trên 8 chiều; bỏ qua chiều chấm điểm nhanh vì bộ chấm nhanh đã được thay bằng một lượt "
    "quét xác định, nên điểm của nó không còn ý nghĩa so sánh"
)
YV_CONDITION = {
    "health": "Cần người có chuyên môn rà từng bài, và câu miễn trừ phải nằm ngay trong phần mô tả của chính bài đó vì nơi đặt câu miễn trừ chưa chốt",
    "founder": "Chặn tới khi có đồng ý bằng văn bản và phạm vi được nói của founder; chưa có đồng ý thì cắt hết phần con người, chỉ giữ không gian và đồ hoạ",
    "product-adjacent": "Chỉ kể ở mức trải nghiệm khách hàng; cấm mọi câu về công dụng vì hồ sơ sản phẩm chưa kiểm chứng",
    "none": "Giữ nguyên câu ranh giới của dòng; lời kêu gọi không vượt quá theo dõi Page, lưu bài, chia sẻ",
}
YV_FALLBACK_CONDITION = (
    YV_FALLBACK_PREFIX
    + "chưa có brief sản xuất, chưa có brief Reel, chưa có tài sản. Muốn chạy hướng này thì phải viết brief trước, và nó đi lại đúng tuyến duyệt của hướng A cùng ngày"
)


def _yv_risk(cells: dict[str, str]) -> str:
    if cells.get("Trụ nội dung") in YV_HEALTH_PILLARS:
        return "health"
    if cells.get("Trụ nội dung") == YV_FOUNDER_PILLAR:
        return "founder"
    if cells.get("Ngày") in YV_PRODUCT_DAYS:
        return "product-adjacent"
    return "none"


def _yv_workflow(calendar: list[dict[str, str]]) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for cells in calendar:
        route = cells["Tuyến duyệt"]
        legs = route.split("+")
        if any(leg not in YV_REVIEWER_BY_LEG for leg in legs):
            raise SyncError(f"unknown review route: {route}")
        risk = _yv_risk(cells)
        if cells["Vai trò phễu"] not in YV_FUNNEL_METRIC:
            raise SyncError(f"unknown funnel role: {cells['Vai trò phễu']}")
        option = cells["Hướng"]
        condition = YV_CONDITION[risk] if option == "A" else YV_FALLBACK_CONDITION
        if option == "A" and cells["Ngày"] in YV_PRODUCT_DAYS and risk != "product-adjacent":
            condition += ". " + YV_CONDITION["product-adjacent"]
        records.append(
            {
                "Mã": cells["Mã"].replace("-CAL-", "-WF-"),
                "Chu kỳ": cells["Chu kỳ"], "Ngày": cells["Ngày"], "Hướng": option,
                "Người duyệt": ", ".join(YV_REVIEWER_BY_LEG[leg] for leg in legs),
                "Kết luận": cells["Trạng thái duyệt"], "Điều kiện kèm theo": condition,
                "Hết hạn (ICT)": "—", "Trạng thái đăng": "NOT_PUBLISHED", "Bản sửa": cells["Bản sửa"],
                "Sửa lớn có reset không": "Có", "Tuyến duyệt": route, "Mức rủi ro": risk,
                "DMP check": YV_DMP_CHECK,
                "Trạng thái đồng ý": "CHƯA CÓ ĐỒNG Ý" if option == "A" and cells["Ngày"] in YV_FOUNDER_DAYS else ("Không cần" if option == "A" else "—"),
                "Giờ đăng": "—", "Tham chiếu đo": YV_FUNNEL_METRIC[cells["Vai trò phễu"]],
                "Ghi chú reset": "Đổi câu claim, đổi lời kêu gọi, đổi người xuất hiện, đổi kết luận sức khoẻ",
                "Câu claim": cells["Câu claim dùng"], "Chủ sở hữu": cells.get("Chủ sở hữu", "—"),
                "__source_path": cells["__source_path"], "__source_location": cells["__source_location"],
            }
        )
    return records


def _yv_briefs(repo_root: Path, spec: dict[str, Any], calendar: list[dict[str, str]]) -> list[dict[str, str]]:
    wanted = _yv_expected_headers(spec)
    briefs: dict[str, dict[str, str]] = {}
    for relative in spec["source_markdown"]:
        for table in _yv_parse_tables(repo_root / relative):
            actual = {header for header in table["headers"] if header not in YV_MACHINE_HEADERS}
            if actual != wanted:
                continue
            for cells in _yv_rows(relative, table):
                if cells["Ngày"] in briefs:
                    raise SyncError(f"duplicate production brief day: {cells['Ngày']}")
                briefs[cells["Ngày"]] = cells
    records: list[dict[str, str]] = []
    for cells in calendar:
        day = cells["Ngày"]
        if day not in briefs:
            raise SyncError(f"missing production brief day: {day}")
        if cells["Hướng"] == "A":
            records.append(briefs[day])
            continue
        records.append(
            {
                "Mã": f"{briefs[day]['Mã']}-{cells['Hướng']}", "Chu kỳ": cells["Chu kỳ"], "Ngày": day,
                "Hướng": cells["Hướng"], "Loại brief": "Reel" if cells["Định dạng"] == "Reel" else "Bài",
                "Định dạng": cells["Định dạng"], "Hook": YV_FALLBACK_PREFIX + cells["__option_body"],
                "Hình ảnh / shot": "—", "Chữ trên hình": "—", "Thời lượng": "—", "Tỷ lệ khung": "—",
                "Lời thoại": "—", "Phụ đề": "—", "Vùng an toàn": "—", "Kêu gọi": cells["Kêu gọi"],
                "Câu claim dùng": cells["Câu claim dùng"], "Chỉ số theo dõi": "—", "Tiếp cận": "—",
                "Rủi ro / cổng": "Chưa có brief nên chưa soát được rủi ro; hướng này đi lại đúng tuyến duyệt của hướng A cùng ngày",
                "Trạng thái sản xuất": "CHƯA CÓ BRIEF", "Chủ sở hữu": cells.get("Chủ sở hữu", "—"),
                "__source_path": cells["__source_path"], "__source_location": cells["__source_location"],
            }
        )
    return records


def _yv_report_calendar(calendar: list[dict[str, str]]) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for cells in calendar:
        cta = cells["Kêu gọi"]
        if not any(token in cta.lower() for token in ("theo dõi page", "lưu bài", "lưu", "chia sẻ")):
            raise SyncError(f"report CTA outside allowed scope: {cta}")
        option = cells["Hướng"]
        tradeoff = cells["Angle chính"] if option == "A" else YV_FALLBACK_PREFIX + f"hướng thay thế cho {cells['Angle chính']}; đổi lại là chưa có brief và chưa có tư liệu"
        records.append(
            {
                "Mã": cells["Mã"].replace("-CAL-", "-RPT-"), "Ngày": cells["Ngày"], "Hướng": option,
                "Trụ nội dung": cells["Trụ nội dung"], "Định dạng": cells["Định dạng"], "Nói gì": cells["Nói gì"],
                "Vì sao chọn / đánh đổi": tradeoff, "Kêu gọi": cta, "Ai duyệt": cells["Tuyến duyệt"],
                "Trạng thái": cells["Trạng thái duyệt"], "Chủ sở hữu": cells.get("Chủ sở hữu", "—"),
                "__source_path": cells["__source_path"], "__source_location": cells["__source_location"],
            }
        )
    return records


def _yv_source_inventory(repo_root: Path, registry: dict[str, Any]) -> list[dict[str, str]]:
    sources: dict[str, None] = {}
    for tab in sorted(registry["tabs"], key=lambda item: item["index"]):
        for relative in tab.get("source_markdown", []) + tab.get("derives_from_markdown", []):
            sources.setdefault(relative, None)
    for relative in (
        "docs/system/yvien-sheet-dataset-registry.json",
        "docs/system/yvien-sheet-human-layer-spec.md",
        "docs/system/yvien-brand-voice-pack.md",
    ):
        sources.setdefault(relative, None)
    categories = {
        "docs Toplink/brand": "Thương hiệu", "docs Toplink/research": "Nghiên cứu",
        "docs Toplink/content": "Nội dung", "docs Toplink/system": "Hệ thống",
        "docs/system": "Hợp đồng kỹ thuật",
    }
    sensitive = ("compliance", "reels", "production", "asset", "owner-decisions", "input-gaps")
    records: list[dict[str, str]] = []
    for ordinal, relative in enumerate(sorted(sources), start=1):
        path = repo_root / relative
        if not path.is_file():
            raise SyncError(f"inventory source missing: {relative}")
        folder = "/".join(relative.split("/")[:2])
        records.append(
            {
                "Mã": f"SRC-{ordinal:02d}", "Tệp nguồn": relative,
                "Nhóm": categories.get(folder, "Khác"),
                "Mức nhạy cảm": "Cần cổng người" if any(token in relative for token in sensitive) else "Thường",
                "Trạng thái": "Đang dùng", "Lý do loại trừ": "—", "SHA-256": sha256_file(path),
                "Chủ sở hữu": "Codex", "__source_path": relative, "__source_location": "L1",
            }
        )
    return records


def _yv_output_index(repo_root: Path, tab_of_source: dict[str, set[str]]) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for ordinal, relative in enumerate(sorted(tab_of_source), start=1):
        path = repo_root / relative
        records.append(
            {
                "Mã": f"OUT-{ordinal:02d}", "Sản phẩm": path.name, "Đường dẫn": relative,
                "Tab hiển thị": ", ".join(sorted(tab_of_source[relative])),
                "Trạng thái QA nội bộ": "LOCAL_VERIFIED", "Trạng thái đưa lên Sheet": "CHƯA GHI",
                "Trạng thái đọc lại": "CHƯA ĐỌC LẠI", "Digest": sha256_file(path), "Chủ sở hữu": "Codex",
                "__source_path": relative, "__source_location": "L1",
            }
        )
    return records


def _yv_build_block(
    repo_root: Path, registry: dict[str, Any], spec: dict[str, Any], state: dict[str, Any]
) -> dict[str, Any]:
    tab = spec["tab"]
    if tab == "YV_09_content_calendar":
        records = _yv_calendar(repo_root, spec)
        state["calendar"] = records
    elif tab == "YV_10_production_briefs":
        records = _yv_briefs(repo_root, spec, state["calendar"])
    elif tab == "YV_12_workflow_approval":
        records = _yv_workflow(state["calendar"])
    elif tab == "report" and spec["section"] == "B":
        records = _yv_report_calendar(state["calendar"])
    elif tab == "01_SOURCE_INVENTORY":
        records = _yv_source_inventory(repo_root, registry)
    elif tab == "03_OUTPUT_INDEX":
        records = _yv_output_index(repo_root, state["tab_of_source"])
    else:
        relative, table = _yv_select_table(repo_root, spec)
        records = _yv_rows(relative, table)
    for cells in records:
        relative = cells["__source_path"]
        path = repo_root / relative
        if relative not in state["digests"] and path.is_file():
            state["digests"][relative] = sha256_file(path)
        cells.setdefault("Chủ sở hữu", "—")
    values = _yv_emit(registry, spec, records, state["digests"])
    minimum, maximum = spec["min_records"], spec["max_records"]
    if minimum is not None and not minimum <= len(values) <= maximum:
        raise SyncError(f"{tab}: record count {len(values)} outside [{minimum}, {maximum}]")
    keys = [row[-2] for row in values]
    if len(set(keys)) != len(keys):
        raise SyncError(f"{tab}: duplicate stable key")
    return {"spec": spec, "values": values, "records": records}


def _yv_legend(registry_tab: dict[str, Any]) -> str:
    if registry_tab.get("expected_yellow_count") == 0:
        return "Chú giải — tab này không có ô vàng. Việc còn treo nằm ở tab Y Viện cần chốt. Hai cột cuối là cột máy, đã ẩn."
    return (
        "Chú giải — ô nền vàng nghĩa là còn một việc của người thật chưa làm; nội dung ô mở đầu "
        "bằng CHƯA CHỐT và nêu rõ ai chốt điều gì. Dòng mở đầu bằng DỰ PHÒNG là hướng thay thế, "
        "không bao giờ vàng. Hai cột cuối là cột máy, đã ẩn."
    )


def _yv_pad_row(row: list[str], visible_count: int, width: int) -> list[str]:
    padding = width - 2 - visible_count
    if padding < 0:
        raise SyncError("human-layer visible columns exceed grid width")
    return row[:visible_count] + [""] * padding + row[-2:]


def _yv_yellow(values: list[list[str]], visible_count: int, first_row: int) -> list[str]:
    return [
        f"{_yv_column(column)}{first_row + row}"
        for row, cells in enumerate(values)
        for column, cell in enumerate(cells[:visible_count])
        if cell.startswith(YV_YELLOW_PREFIX)
    ]


def _yv_assemble(registry: dict[str, Any], tab_name: str, blocks: list[dict[str, Any]]) -> dict[str, Any]:
    registry_tab = next(tab for tab in registry["tabs"] if tab["tab"] == tab_name)
    width = registry_tab["grid_width"]
    visible = registry_tab.get("visible_column_count", width - 2)
    body: list[list[str]] = []
    yellow: list[str] = []
    sections: list[dict[str, Any]] = []
    if len(blocks) == 1:
        spec = blocks[0]["spec"]
        header = spec["headers"] + YV_HIDDEN_HEADERS
        body.extend(_yv_pad_row(row, len(spec["headers"]), width) for row in blocks[0]["values"])
        yellow = _yv_yellow(blocks[0]["values"], len(spec["headers"]), 3)
    else:
        header = ["Mục"] + [""] * (visible - 1) + YV_HIDDEN_HEADERS
        cursor = 3
        for block in blocks:
            spec = block["spec"]
            body.append([spec["heading"] or f"Bảng {spec['section']}"] + [""] * (width - 1))
            cursor += 1
            body.append(spec["headers"] + [""] * (width - len(spec["headers"])))
            cursor += 1
            start = cursor
            body.extend(_yv_pad_row(row, len(spec["headers"]), width) for row in block["values"])
            cursor += len(block["values"])
            yellow.extend(_yv_yellow(block["values"], len(spec["headers"]), start))
            sections.append({"section_id": spec["section"], "heading": spec["heading"], "header_row": start - 1, "first_data_row": start, "row_count": len(block["values"])} )
            body.append([""] * width)
            cursor += 1
        if body and not any(body[-1]):
            body.pop()
    values = [header, [_yv_legend(registry_tab)] + [""] * (width - 1)] + body
    if any(len(row) != width for row in values):
        raise SyncError(f"{tab_name}: inconsistent grid width")
    expected_yellow = registry_tab.get("expected_yellow_count")
    if expected_yellow is not None and len(yellow) != expected_yellow:
        raise SyncError(f"{tab_name}: yellow count drift")
    plan: dict[str, Any] = {
        "tab": tab_name, "index": registry_tab["index"], "title_display": registry["display_label_map"]["tab_title"][tab_name],
        "grid_width": width, "visible_column_count": visible, "row_count": len(values), "column_count": width,
        "used_range": f"'{tab_name}'!A1:{_yv_column(width - 1)}{len(values)}", "header_row": 1, "legend_row": 2,
        "first_data_row": 3, "hidden_columns": registry_tab["hidden_columns"],
        "hidden_column_letters": [_yv_column(width - 2), _yv_column(width - 1)],
        "evidence_status": registry_tab["default_evidence_status"], "allowed_use": registry_tab["default_allowed_use"],
        "yellow_cells": yellow, "expected_yellow_count": len(yellow), "values": values, "content_hash": _yv_content_hash(values),
    }
    if sections:
        plan["sections"] = sections
    return plan


def build_human_layer_plan(repo_root: Path) -> dict[str, Any]:
    """Independently rebuild the signed human-layer plan from registry + Markdown."""
    registry = load_human_layer_registry(repo_root)
    specs = _yv_specs(registry)
    tab_of_source: dict[str, set[str]] = {}
    for spec in specs:
        for relative in spec["source_markdown"]:
            tab_of_source.setdefault(relative, set()).add(spec["tab"])
    state: dict[str, Any] = {"digests": {}, "tab_of_source": tab_of_source}
    order = [spec for spec in specs if spec["tab"] != "report"] + [spec for spec in specs if spec["tab"] == "report"]
    blocks: dict[str, list[dict[str, Any]]] = {}
    for spec in order:
        blocks.setdefault(spec["tab"], []).append(_yv_build_block(repo_root, registry, spec, state))
    for tab_blocks in blocks.values():
        tab_blocks.sort(key=lambda block: block["spec"].get("section") or "")
    plans = [_yv_assemble(registry, tab["tab"], blocks[tab["tab"]]) for tab in sorted(registry["tabs"], key=lambda item: item["index"])]
    workbook_hash = hashlib.sha256(json.dumps([tab["content_hash"] for tab in plans], ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
    return {
        "plan_id": "YV-REPORT-PLAN-001", "schema_version": registry["schema_version"], "registry_id": registry["registry_id"],
        "generated_from": YV_REGISTRY_PATH.as_posix(), "state": "DRAFT_UNSIGNED · LOCAL_ONLY", "write_executed": False,
        "external_writes": 0, "spreadsheet_target": registry["spreadsheet_target"], "formatting": registry["formatting"],
        "palette": registry["palette"], "hidden_column_contract": registry["hidden_column_contract"], "tab_count": len(plans),
        "total_yellow_cells": sum(tab["expected_yellow_count"] for tab in plans), "source_digests": dict(sorted(state["digests"].items())),
        "tabs": plans, "workbook_content_hash": workbook_hash,
    }


YV_HUMAN_ONLY_STATUSES = {"APPROVED", "HUMAN_APPROVED", "PUBLISHED"}
YV_EXPECTED_TOTAL_YELLOW = 27
YV_EXTERNAL_YELLOW_OWNER = {
    "TL-CTL-15": "TL-OA-06",
    "TL-KPI-09": "TL-OA-04",
    "TL-KPI-12": "TL-OA-05",
    "TL-CAMP-W2": "TL-OA-01",
    "TL-CAMP-W3": "TL-OA-02",
    "TL-CAMP-W4": "TL-OA-03",
    "AST-TEAM-BTS": "TL-OA-07",
    "AST-FOUNDER": "TL-OA-08",
    "TL-BATCH-ROLE": "TL-OA-09",
}
YV_YELLOW_ROLE_TOKENS = (
    "chủ Y Viện",
    "cổng sức khoẻ",
    "cổng pháp lý",
    "người phụ trách",
    "phụ trách truyền thông",
)


def _yv_plan_rows(tab: dict[str, Any], section: str | None = None) -> list[tuple[int, list[str], list[str]]]:
    """Return (zero-based row index, section header, row) for actual data rows."""
    values = tab.get("values")
    if not isinstance(values, list) or not values:
        raise SyncError(f"{tab.get('tab', '<unknown>')}: values missing")
    sections = tab.get("sections")
    if sections:
        output: list[tuple[int, list[str], list[str]]] = []
        for item in sections:
            if section is not None and item.get("section_id") != section:
                continue
            header_index = item["header_row"] - 1
            first_index = item["first_data_row"] - 1
            count = item["row_count"]
            header = values[header_index]
            for row_index in range(first_index, first_index + count):
                if row_index >= len(values):
                    raise SyncError(f"{tab['tab']}: section row range exceeds values")
                output.append((row_index, header, values[row_index]))
        return output
    if section is not None:
        return []
    return [(index, values[0], row) for index, row in enumerate(values[2:], start=2)]


def _yv_cell(header: list[str], row: list[str], column: str, tab_name: str) -> str:
    try:
        return str(row[header.index(column)]).strip()
    except ValueError as exc:
        raise SyncError(f"{tab_name}: foreign key column missing: {column}") from exc


def _yv_fk_values(value: str, separator: str | None) -> list[str]:
    if separator is None:
        return [value.strip()]
    return [part.strip() for part in value.split(separator) if part.strip()]


def _yv_multi_fk_resolves(value: str, separator: str, targets: set[Any]) -> bool:
    """Resolve delimited labels even when a canonical label contains the delimiter."""
    remaining = value.strip()
    string_targets = sorted(
        (item for item in targets if isinstance(item, str) and item), key=len, reverse=True
    )
    while remaining:
        match = next(
            (
                item
                for item in string_targets
                if remaining == item or remaining.startswith(item + separator)
            ),
            None,
        )
        if match is None:
            return False
        remaining = remaining[len(match) :]
        if not remaining:
            return True
        if not remaining.startswith(separator):
            return False
        remaining = remaining[len(separator) :].strip()
    return True


def validate_human_layer_plan(plan: dict[str, Any], registry: dict[str, Any]) -> None:
    """Validate human-facing semantics without relying on the plan's own hashes."""
    tabs = plan.get("tabs")
    if not isinstance(tabs, list):
        raise SyncError("human-layer tabs missing")
    ordered_registry = sorted(registry["tabs"], key=lambda item: item["index"])
    expected_names = [item["tab"] for item in ordered_registry]
    actual_names = [item.get("tab") for item in tabs]
    if actual_names != expected_names or plan.get("tab_count") != len(expected_names):
        raise SyncError("human-layer tab order/count drift")
    by_name = {tab["tab"]: tab for tab in tabs}

    all_yellow: list[tuple[str, str]] = []
    for registry_tab in ordered_registry:
        name = registry_tab["tab"]
        tab = by_name[name]
        values = tab.get("values", [])
        width = registry_tab["grid_width"]
        visible = registry_tab.get("visible_column_count", width - 2)
        if tab.get("grid_width") != width or tab.get("column_count") != width:
            raise SyncError(f"{name}: grid width drift")
        if tab.get("row_count") != len(values) or any(not isinstance(row, list) or len(row) != width for row in values):
            raise SyncError(f"{name}: row/column shape drift")
        if values[0][-2:] != YV_HIDDEN_HEADERS or tab.get("hidden_columns") != registry_tab["hidden_columns"]:
            raise SyncError(f"{name}: hidden _key/_audit contract drift")

        if registry_tab.get("sections"):
            registry_sections = {item["section_id"]: item for item in registry_tab["sections"]}
            plan_sections = {item["section_id"]: item for item in tab.get("sections", [])}
            if set(plan_sections) != set(registry_sections):
                raise SyncError(f"{name}: section contract drift")
            for section_id, section_spec in registry_sections.items():
                count = len(_yv_plan_rows(tab, section_id))
                if not section_spec["min_records"] <= count <= section_spec["max_records"]:
                    raise SyncError(f"{name}/{section_id}: cardinality {count} outside registry bounds")
        else:
            count = len(_yv_plan_rows(tab))
            if not registry_tab["min_records"] <= count <= registry_tab["max_records"]:
                raise SyncError(f"{name}: cardinality {count} outside registry bounds")

        stable_keys: list[str] = []
        actual_yellow: list[str] = []
        for row_index, header, row in _yv_plan_rows(tab):
            stable_key = str(row[-2]).strip()
            audit = str(row[-1]).strip()
            if not stable_key or not audit:
                raise SyncError(f"{name}: blank stable key or audit")
            stable_keys.append(stable_key)
            for column_index, raw in enumerate(row[:visible]):
                cell = str(raw).strip()
                if cell in YV_HUMAN_ONLY_STATUSES:
                    raise SyncError(f"{name}: status escalation to {cell}")
                if cell.startswith(YV_YELLOW_PREFIX):
                    address = f"{_yv_column(column_index)}{row_index + 1}"
                    actual_yellow.append(address)
                    all_yellow.append((name, address))
                    if len(cell) > 210 or not any(token in cell for token in YV_YELLOW_ROLE_TOKENS):
                        raise SyncError(f"{name}!{address}: yellow cell contract violation")
                if cell.startswith("DỰ PHÒNG") and f"{_yv_column(column_index)}{row_index + 1}" in tab.get("yellow_cells", []):
                    raise SyncError(f"{name}: fallback row marked yellow")
        if len(stable_keys) != len(set(stable_keys)):
            raise SyncError(f"{name}: duplicate stable key")
        declared_yellow = tab.get("yellow_cells", [])
        expected_yellow = registry_tab.get("expected_yellow_count")
        if (
            actual_yellow != declared_yellow
            or tab.get("expected_yellow_count") != len(actual_yellow)
            or (expected_yellow is not None and len(actual_yellow) != expected_yellow)
        ):
            raise SyncError(f"{name}: yellow coordinate/count drift")

    if len(all_yellow) != plan.get("total_yellow_cells") or len(all_yellow) != YV_EXPECTED_TOTAL_YELLOW:
        raise SyncError("workbook yellow total drift")

    owner = by_name["00_Y_VIEN_CAN_CHOT"]
    owner_open_keys: set[str] = set()
    for _row_index, header, row in _yv_plan_rows(owner):
        status = _yv_cell(header, row, "Trạng thái", owner["tab"])
        yellow_count = sum(str(cell).strip().startswith(YV_YELLOW_PREFIX) for cell in row[: owner["visible_column_count"]])
        if status == "OPEN" and yellow_count != 1:
            raise SyncError("00_Y_VIEN_CAN_CHOT: OPEN row must carry exactly one yellow cell")
        if status != "OPEN" and yellow_count:
            raise SyncError("00_Y_VIEN_CAN_CHOT: settled row must not carry a yellow cell")
        if status == "OPEN":
            owner_open_keys.add(str(row[-2]).strip())
    external_yellow_keys = {
        str(row[-2]).strip()
        for tab in tabs
        if tab["tab"] != owner["tab"]
        for row_index, _header, row in _yv_plan_rows(tab)
        if any(
            f"{_yv_column(column_index)}{row_index + 1}" in tab["yellow_cells"]
            for column_index in range(tab["visible_column_count"])
        )
    }
    if external_yellow_keys != set(YV_EXTERNAL_YELLOW_OWNER) or not set(YV_EXTERNAL_YELLOW_OWNER.values()) <= owner_open_keys:
        raise SyncError("yellow correspondence drift between source tabs and 00_Y_VIEN_CAN_CHOT")

    expected_sources: set[str] = set()
    for registry_tab in registry["tabs"]:
        expected_sources.update(registry_tab.get("source_markdown", []))
        for section in registry_tab.get("sections", []):
            expected_sources.update(section.get("source_markdown", []))
    output_index = by_name["03_OUTPUT_INDEX"]
    indexed_sources = {
        _yv_cell(header, row, "Đường dẫn", output_index["tab"])
        for _index, header, row in _yv_plan_rows(output_index)
    }
    if indexed_sources != expected_sources:
        missing = sorted(expected_sources - indexed_sources)
        extra = sorted(indexed_sources - expected_sources)
        raise SyncError(f"03_OUTPUT_INDEX: orphan source artifact; missing={missing}, extra={extra}")

    registry_tab_keys = set(expected_names)
    for foreign_key in registry.get("foreign_keys", []):
        source_tab = foreign_key["tab"]
        # The wildcard audit binding is a provenance structure, not a displayed
        # relational value; nonblank audit cells were checked above.
        if source_tab == "*":
            continue
        source = by_name[source_tab]
        source_rows = _yv_plan_rows(source, foreign_key.get("section"))
        source_columns = foreign_key["columns"]
        allow = {str(value).strip() for value in foreign_key.get("allow_values", [])}
        if foreign_key.get("target") == "registry_tab_keys":
            target_values: set[Any] = registry_tab_keys
        else:
            target = by_name[foreign_key["target_tab"]]
            target_columns = foreign_key.get("target_columns") or [foreign_key["target_column"]]
            target_values = {
                tuple(_yv_cell(header, row, column, target["tab"]) for column in target_columns)
                for _index, header, row in _yv_plan_rows(target)
            }
            if len(target_columns) == 1:
                target_values = {item[0] for item in target_values}
            if foreign_key.get("target_tab") == "YV_08_experiments" and target_columns == ["_key"]:
                for _target_index, target_header, target_row in _yv_plan_rows(target):
                    week = _yv_cell(target_header, target_row, "Thuộc giai đoạn", target["tab"])
                    variable = _yv_cell(target_header, target_row, "Biến thay đổi", target["tab"]).split(" — ", 1)[0]
                    variable = variable.replace("Kiểu câu ", "Kiểu ").replace(" trong tuần", "")
                    target_values.add(f"{week} — {variable.lower()}")
        for _index, header, row in source_rows:
            raw_values = [_yv_cell(header, row, column, source_tab) for column in source_columns]
            if len(source_columns) > 1:
                candidate: Any = tuple(raw_values)
                if candidate not in target_values and not all(value in allow for value in raw_values):
                    raise SyncError(f"{source_tab}: orphan foreign key {candidate}")
                continue
            separator = foreign_key.get("multi_value_separator")
            if raw_values[0] in allow or raw_values[0] in target_values:
                continue
            if (
                source_tab == "YV_08_experiments"
                and foreign_key.get("target_tab") == "04_DECISIONS"
                and raw_values[0] == f"Chốt chu kỳ {_yv_cell(header, row, 'Chu kỳ', source_tab)}"
            ):
                # This is a deliberately deferred edge: its target row is created
                # only when the cycle closes, so it must bind to the row's cycle.
                continue
            if source_tab == "YV_11_asset_batch_plan" and foreign_key.get("target_tab") == "YV_09_content_calendar":
                day_range = re.fullmatch(r"D-(\d+)\s*…\s*D-(\d+)", raw_values[0])
                if day_range:
                    first, last = (int(value) for value in day_range.groups())
                    expanded = {f"D-{number}" for number in range(first, last + 1)}
                    if first <= last and expanded <= target_values:
                        continue
            if foreign_key.get("target_tab") == "05_KPI_DICTIONARY":
                kpi_rollups = {
                    "Chỉ số tiếp cận và tỷ lệ xem hết Reel": {"Số người tiếp cận", "Tỷ lệ xem hết Reel"},
                    "Lượt lưu, lượt chia sẻ và số câu hỏi về quy trình": {"Lượt lưu và lượt chia sẻ", "Câu hỏi đúng chủ đề"},
                }
                required_kpis = kpi_rollups.get(raw_values[0])
                if required_kpis is not None and required_kpis <= target_values:
                    continue
            if separator and _yv_multi_fk_resolves(raw_values[0], separator, target_values | allow):
                continue
            for candidate in _yv_fk_values(raw_values[0], separator):
                if candidate not in allow and candidate not in target_values:
                    raise SyncError(f"{source_tab}: orphan foreign key {candidate}")


def validate_human_layer_bundle(bundle: dict[str, Any], repo_root: Path) -> None:
    if bundle.get("schema_version") != "YV-SHEET-001/1.0.0":
        raise SyncError("human-layer bundle schema drift")
    datasets = bundle.get("datasets")
    if not isinstance(datasets, dict) or set(datasets) != set(TAB_KEYS):
        raise SyncError("human-layer bundle must contain the ordered 21 tabs")
    locked = read_json(repo_root / YV_PLAN_PATH)
    rebuilt = build_human_layer_plan(repo_root)
    validate_human_layer_plan(rebuilt, load_human_layer_registry(repo_root))
    if rebuilt["workbook_content_hash"] != locked.get("workbook_content_hash"):
        raise SyncError("workbook content hash drift")
    for tab in rebuilt["tabs"]:
        payload = datasets[tab["tab"]]
        if payload.get("values") != tab["values"] or payload.get("dataset_sha256") != tab["content_hash"]:
            raise SyncError(f"compiled dataset drift: {tab['tab']}")
    expected_bundle = copy.deepcopy(bundle)
    expected_digest = expected_bundle.pop("bundle_sha256", None)
    if expected_digest != sha256_json(expected_bundle):
        raise SyncError("human-layer bundle digest drift")


def _build_report_plan_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    plan = build_human_layer_plan(repo_root)
    output = Path(args.output)
    if not output.is_absolute():
        output = repo_root / output
    write_json(output, plan)
    print(json.dumps({"status": "PASS", "tab_count": 21, "workbook_content_hash": plan["workbook_content_hash"], "output": output.as_posix()}, ensure_ascii=False))
    return 0


YV_APPROVALS = (
    ("CREATE_TAB", Path("staging/yv-humanize/approvals/approval-01-create-tab.md"), "7ab5d96d5ebaf7459050786f9a70d809fe2012398e01de6d1953e8bd2ee13e2b"),
    ("UPSERT", Path("staging/yv-humanize/approvals/approval-02-upsert.md"), "b96f9f2511984172dda20b672a2c23c719612f9162d850924ec0c11d882ef409"),
    ("READBACK", Path("staging/yv-humanize/approvals/approval-03-readback.md"), "122d7a81c2eafd44db5a9b2c3dc6600d1bff5ff2aae15de31e0df16487120e21"),
)
YV_PLAN_SHA256 = "14efcf8661c6cd0306658879bf933eecfcf4e4bc778e1d5dfb249d0b6ffc403b"
YV_WORKBOOK_SHA256 = "8cbb4e12ff6c8054b969e4c44ab4432bd4b2def3303ba03697c1aceec84e338b"
YV_RECOVERY_DIR = Path("staging/yv-humanize/recovery-p2.6")
YV_RECOVERY_SNAPSHOT_PATH = Path("staging/yv-humanize/live-state-after-restore.json")
YV_RECOVERY_SNAPSHOT_SHA256 = "16bb24aec5f663d427039a1f361dafce75eaa87ef77e141b4f70b4758ce25a8f"
YV_PRIOR_VERIFY_FAILED_SHA256 = "f41b26ac60607625c00ca28f53a150a371c5154af495369e52dfc621a1949984"


def validate_human_layer_approvals(repo_root: Path, require_unconsumed: bool = True) -> dict[str, str]:
    plan_path = repo_root / YV_PLAN_PATH
    plan = read_json(plan_path)
    if sha256_file(plan_path) != YV_PLAN_SHA256 or plan.get("workbook_content_hash") != YV_WORKBOOK_SHA256:
        raise SyncError("signed human-layer plan digest drift")
    ledger_path = repo_root / "staging/yv-humanize/approvals/SIGNATURES.md"
    ledger = ledger_path.read_text(encoding="utf-8")
    digests: dict[str, str] = {}
    now = datetime.now(timezone.utc)
    for action, relative, expected_digest in YV_APPROVALS:
        path = repo_root / relative
        digest = sha256_file(path)
        text_value = path.read_text(encoding="utf-8")
        if digest != expected_digest or expected_digest not in ledger:
            raise SyncError(f"{action} approval digest/signature drift")
        if f"action: {action}" not in text_value or "write_executed: false" not in text_value:
            raise SyncError(f"{action} approval missing field or already executed")
        if f"plan_digest: {YV_PLAN_SHA256}" not in text_value or f"workbook_content_hash: {YV_WORKBOOK_SHA256}" not in text_value:
            raise SyncError(f"{action} approval plan binding drift")
        expiry_match = re.search(r"^expires_at_ict:\s*(\S+)\s*$", text_value, re.MULTILINE)
        if not expiry_match:
            raise SyncError(f"{action} approval expiry missing")
        expiry = datetime.fromisoformat(expiry_match.group(1))
        if expiry.astimezone(timezone.utc) <= now:
            raise SyncError(f"{action} approval expired")
        for tab in plan["tabs"]:
            if tab["tab"] not in text_value or tab["used_range"] not in text_value:
                raise SyncError(f"{action} approval range/tab drift: {tab['tab']}")
        if require_unconsumed:
            ledger_line = next((line for line in ledger.splitlines() if relative.as_posix() in line), "")
            if "UNCONSUMED" not in ledger_line:
                raise SyncError(f"{action} approval already consumed")
        digests[action] = digest
    return digests


def validate_human_layer_recovery_approvals(
    repo_root: Path, *, require_unconsumed: bool = True
) -> dict[str, str]:
    approval_specs = (
        ("UPSERT_RECOVERY", YV_RECOVERY_DIR / "approval-04-upsert-recovery.md"),
        ("READBACK_RECOVERY", YV_RECOVERY_DIR / "approval-05-readback-recovery.md"),
    )
    ledger_path = repo_root / YV_RECOVERY_DIR / "SIGNATURES.md"
    if not ledger_path.is_file():
        raise SyncError("P2.6 recovery signatures missing")
    ledger = ledger_path.read_text(encoding="utf-8")
    if require_unconsumed and "SIGNED · UNCONSUMED" not in ledger:
        raise SyncError("P2.6 recovery signatures are not unconsumed")
    if not require_unconsumed and not any(
        status in ledger
        for status in ("SIGNED · UNCONSUMED", "CONSUMED · SYNC_READBACK_PASS")
    ):
        raise SyncError("P2.6 recovery signature ledger status invalid")
    plan_path = repo_root / YV_PLAN_PATH
    snapshot_path = repo_root / YV_RECOVERY_SNAPSHOT_PATH
    prior_failure_path = repo_root / "staging/yv-humanize/readback-evidence.json"
    if sha256_file(plan_path) != YV_PLAN_SHA256:
        raise SyncError("P2.6 recovery plan digest drift")
    if sha256_file(snapshot_path) != YV_RECOVERY_SNAPSHOT_SHA256:
        raise SyncError("P2.6 recovery snapshot digest drift")
    if sha256_file(prior_failure_path) != YV_PRIOR_VERIFY_FAILED_SHA256:
        raise SyncError("P2.6 prior failure evidence drift")
    now = datetime.now(timezone.utc)
    digests: dict[str, str] = {}
    plan = read_json(plan_path)
    for action, relative in approval_specs:
        path = repo_root / relative
        digest = sha256_file(path)
        text_value = path.read_text(encoding="utf-8")
        signature_pattern = (
            re.escape(relative.as_posix())
            + r"[\s\S]{0,200}"
            + re.escape(digest)
            + r"[\s\S]{0,80}\bAPPROVED\b"
        )
        if not re.search(signature_pattern, ledger):
            raise SyncError(f"{action} recovery signature digest drift")
        if f"action: {action}" not in text_value or "write_executed: false" not in text_value:
            raise SyncError(f"{action} recovery approval field drift")
        for field, expected in (
            ("plan_digest", YV_PLAN_SHA256),
            ("workbook_content_hash", YV_WORKBOOK_SHA256),
            ("recovery_snapshot_digest", YV_RECOVERY_SNAPSHOT_SHA256),
            ("prior_verify_failed_digest", YV_PRIOR_VERIFY_FAILED_SHA256),
        ):
            if f"{field}: {expected}" not in text_value:
                raise SyncError(f"{action} recovery binding drift: {field}")
        expiry_match = re.search(r"^expires_at_ict:\s*(\S+)\s*$", text_value, re.MULTILINE)
        if not expiry_match or datetime.fromisoformat(expiry_match.group(1)).astimezone(timezone.utc) <= now:
            raise SyncError(f"{action} recovery approval expired or missing")
        if action == "UPSERT_RECOVERY":
            for tab in plan["tabs"]:
                if tab["used_range"] not in text_value:
                    raise SyncError(f"UPSERT_RECOVERY range drift: {tab['tab']}")
        digests[action] = digest
    return digests


def build_human_layer_ledger_closure(repo_root: Path) -> dict[str, Any]:
    """Build the immutable P2.7 status/revision payload without network access."""
    plan_path = repo_root / YV_PLAN_PATH
    execution_path = repo_root / YV_RECOVERY_DIR / "execution-evidence.json"
    readback_path = repo_root / YV_RECOVERY_DIR / "readback-evidence.json"
    if sha256_file(plan_path) != YV_PLAN_SHA256:
        raise SyncError("P2.7 report plan digest drift")
    if sha256_file(execution_path) != YV_P26_EXECUTION_SHA256:
        raise SyncError("P2.7 execution evidence digest drift")
    if sha256_file(readback_path) != YV_P26_READBACK_SHA256:
        raise SyncError("P2.7 readback evidence digest drift")
    execution = read_json(execution_path)
    readback = read_json(readback_path)
    if execution.get("status") != "SYNC_READBACK_PASS" or readback.get("status") != "SYNC_READBACK_PASS":
        raise SyncError("P2.7 requires P2.6 SYNC_READBACK_PASS")
    if readback.get("mismatch_count") != 0 or readback.get("restore_executed") is not False:
        raise SyncError("P2.7 requires zero mismatch and no restore")
    plan = read_json(plan_path)
    by_name = {tab["tab"]: tab for tab in plan["tabs"]}
    output_index = by_name["03_OUTPUT_INDEX"]
    decisions = by_name["04_DECISIONS"]
    output_rows = output_index["values"][2:]
    if len(output_rows) != 19 or [row[-2] for row in output_rows] != [f"OUT-{index:02d}" for index in range(1, 20)]:
        raise SyncError("P2.7 output index identity drift")
    if len(decisions["values"]) != 19 or decisions["values"][-1][-2] != "TL-D32":
        raise SyncError("P2.7 decision append position drift")
    revision_key = "YV-REV-20260805-01"
    revision_row = [
        "C1",
        "2026-08-05",
        "Codex CLI",
        "Ghi nhận lớp người Y Viện đã đồng bộ và đọc lại chính xác theo payload được duyệt; sự kiện này không nâng trạng thái nội dung hay milestone",
        "03_OUTPUT_INDEX, 04_DECISIONS và toàn workbook Y Viện",
        "staging/yv-humanize/recovery-p2.6/readback-evidence.json · SHA-256 7b5d5be579cb673e06f86160a1d3f402a4ce4da2a25cee1af6c5ede21cdf15f5",
        "Khi schema, payload hoặc workbook_content_hash thay đổi",
        "DECIDED",
        revision_key,
        (
            f"04_DECISIONS:{revision_key} · staging/yv-humanize/recovery-p2.6/readback-evidence.json#L1"
            f" · {revision_key} · TOPLINK_CONFIRMED · OPERATIONAL_CONTROL · YV-SHEET-001/1.0.0"
            f" · {YV_P26_READBACK_SHA256} · Codex CLI · 2026-08-05"
        ),
    ]
    closure: dict[str, Any] = {
        "closure_id": "YV-P2.7-LEDGER-CLOSURE-01",
        "status": "DRAFT_UNSIGNED",
        "spreadsheet_id": TARGET_SPREADSHEET_ID,
        "service_account": TARGET_SERVICE_ACCOUNT,
        "plan_digest": YV_PLAN_SHA256,
        "workbook_content_hash": YV_WORKBOOK_SHA256,
        "p2_6_execution_digest": YV_P26_EXECUTION_SHA256,
        "p2_6_readback_digest": YV_P26_READBACK_SHA256,
        "precondition_tab_content_hashes": {
            "03_OUTPUT_INDEX": output_index["content_hash"],
            "04_DECISIONS": decisions["content_hash"],
        },
        "value_input_option": "RAW",
        "external_writes_authorized": 2,
        "readback_required": True,
        "touch_trang_tinh1": False,
        "create_tab": False,
        "conditional_formatting": False,
        "structural_action": {
            "tab": "04_DECISIONS",
            "old_row_count": 19,
            "new_row_count": 20,
            "direct_format_range": "'04_DECISIONS'!A20:J20",
            "basic_filter_range": "'04_DECISIONS'!A1:J20",
        },
        "actions": [
            {
                "tab": "03_OUTPUT_INDEX",
                "range": "'03_OUTPUT_INDEX'!E3:F21",
                "values": [["SYNC_WRITE_PASS", "SYNC_READBACK_PASS"] for _ in output_rows],
            },
            {
                "tab": "04_DECISIONS",
                "range": "'04_DECISIONS'!A20:J20",
                "values": [revision_row],
            },
        ],
    }
    closure["payload_digest"] = sha256_json(closure)
    return closure


def apply_human_layer_ledger_closure(
    plan: dict[str, Any], closure: dict[str, Any]
) -> dict[str, Any]:
    """Overlay a validated P2.7 closure onto a freshly rebuilt base plan."""
    if closure.get("closure_id") != "YV-P2.7-LEDGER-CLOSURE-01":
        raise SyncError("P2.7 closure identity drift")
    expected = copy.deepcopy(plan)
    by_name = {tab["tab"]: tab for tab in expected["tabs"]}
    output_index = by_name["03_OUTPUT_INDEX"]
    decisions = by_name["04_DECISIONS"]
    actions = closure.get("actions", [])
    if [action.get("range") for action in actions] != [
        "'03_OUTPUT_INDEX'!E3:F21",
        "'04_DECISIONS'!A20:J20",
    ]:
        raise SyncError("P2.7 closure range drift")
    status_values = actions[0].get("values")
    revision_values = actions[1].get("values")
    if not isinstance(status_values, list) or len(status_values) != 19:
        raise SyncError("P2.7 output status row count drift")
    if not isinstance(revision_values, list) or len(revision_values) != 1:
        raise SyncError("P2.7 revision row count drift")
    for row, status_pair in zip(output_index["values"][2:], status_values):
        if status_pair != ["SYNC_WRITE_PASS", "SYNC_READBACK_PASS"]:
            raise SyncError("P2.7 output status escalation/drift")
        row[4:6] = status_pair
    revision_row = revision_values[0]
    if len(revision_row) != 10 or revision_row[-2] != "YV-REV-20260805-01" or revision_row[7] != "DECIDED":
        raise SyncError("P2.7 revision identity/status drift")
    decisions["values"].append(copy.deepcopy(revision_row))
    decisions["row_count"] = 20
    decisions["used_range"] = "'04_DECISIONS'!A1:J20"
    for tab in (output_index, decisions):
        tab["content_hash"] = _yv_content_hash(tab["values"])
    expected["workbook_content_hash"] = hashlib.sha256(
        json.dumps(
            [tab["content_hash"] for tab in expected["tabs"]],
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()
    return expected


def validate_human_layer_ledger_closure_approvals(
    repo_root: Path, *, require_unconsumed: bool = True
) -> dict[str, str]:
    ledger_path = repo_root / YV_P27_DIR / "SIGNATURES.md"
    if not ledger_path.is_file():
        raise SyncError("P2.7 ledger closure signatures missing")
    ledger = ledger_path.read_text(encoding="utf-8")
    if require_unconsumed and "SIGNED · UNCONSUMED" not in ledger:
        raise SyncError("P2.7 ledger closure signatures are not unconsumed")
    if not require_unconsumed and not any(
        status in ledger
        for status in ("SIGNED · UNCONSUMED", "CONSUMED · SYNC_READBACK_PASS")
    ):
        raise SyncError("P2.7 ledger closure signature status invalid")
    closure_path = repo_root / YV_P27_DIR / "ledger-closure-plan.json"
    if sha256_file(closure_path) != YV_P27_PLAN_SHA256:
        raise SyncError("P2.7 ledger closure plan digest drift")
    if read_json(closure_path) != build_human_layer_ledger_closure(repo_root):
        raise SyncError("P2.7 ledger closure rebuild drift")
    approvals = {
        "P2_7_LEDGER_UPSERT": YV_P27_DIR / "approval-06-ledger-upsert.md",
        "P2_7_LEDGER_READBACK": YV_P27_DIR / "approval-07-ledger-readback.md",
    }
    now = datetime.now(timezone.utc)
    digests: dict[str, str] = {}
    for action, relative in approvals.items():
        path = repo_root / relative
        digest = sha256_file(path)
        if digest != YV_P27_APPROVAL_SHA256[action]:
            raise SyncError(f"{action} approval digest drift")
        approval_text = path.read_text(encoding="utf-8")
        if f"action: {action}" not in approval_text or "write_executed: false" not in approval_text:
            raise SyncError(f"{action} approval field drift")
        if f"closure_plan_sha256: {YV_P27_PLAN_SHA256}" not in approval_text:
            raise SyncError(f"{action} closure binding drift")
        expiry = re.search(r"^expires_at_ict:\s*(\S+)\s*$", approval_text, re.MULTILINE)
        if not expiry or datetime.fromisoformat(expiry.group(1)).astimezone(timezone.utc) <= now:
            raise SyncError(f"{action} approval expired or missing")
        signature_pattern = (
            re.escape(relative.as_posix())
            + r"[\s\S]{0,200}"
            + re.escape(digest)
            + r"[\s\S]{0,80}\bAPPROVED\b"
        )
        if not re.search(signature_pattern, ledger):
            raise SyncError(f"{action} signature digest drift")
        digests[action] = digest
    return digests


def build_p27_structural_requests(plan: dict[str, Any], decisions_sheet_id: int) -> list[dict[str, Any]]:
    if not isinstance(decisions_sheet_id, int) or decisions_sheet_id == 0:
        raise SyncError("P2.7 invalid decisions sheet id")
    body_format = {
        "backgroundColor": _yv_rgb(plan["palette"]["sheet_background"]),
        "textFormat": {"foregroundColor": _yv_rgb(plan["palette"]["text"])},
        "wrapStrategy": "WRAP",
        "verticalAlignment": "TOP",
    }
    row_20 = {
        "sheetId": decisions_sheet_id,
        "startRowIndex": 19,
        "endRowIndex": 20,
        "startColumnIndex": 0,
        "endColumnIndex": 10,
    }
    return [
        {
            "updateSheetProperties": {
                "properties": {"sheetId": decisions_sheet_id, "gridProperties": {"rowCount": 20}},
                "fields": "gridProperties.rowCount",
            }
        },
        {
            "repeatCell": {
                "range": row_20,
                "cell": {"userEnteredFormat": body_format},
                "fields": "userEnteredFormat(backgroundColor,textFormat.foregroundColor,wrapStrategy,verticalAlignment)",
            }
        },
        {"setBasicFilter": {"filter": {"range": {**row_20, "startRowIndex": 0}}}},
    ]


def audit_human_layer_idempotency(
    expected_plan: dict[str, Any], values_response: dict[str, Any]
) -> dict[str, Any]:
    value_ranges = values_response.get("valueRanges", [])
    if len(value_ranges) != len(expected_plan["tabs"]):
        raise SyncError("P2.8 readback range count drift")
    tab_diffs: dict[str, int] = {}
    actual_hashes: list[str] = []
    for tab, value_range in zip(expected_plan["tabs"], value_ranges):
        actual = _yv_normalize_read_values(
            value_range.get("values", []), tab["row_count"], tab["column_count"]
        )
        expected = tab["values"]
        diff_count = sum(
            actual[row][column] != expected[row][column]
            for row in range(tab["row_count"])
            for column in range(tab["column_count"])
        )
        tab_diffs[tab["tab"]] = diff_count
        actual_hashes.append(_yv_content_hash(actual))
    actual_workbook_hash = hashlib.sha256(
        json.dumps(actual_hashes, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    total = sum(tab_diffs.values())
    return {
        "status": "PASS" if total == 0 else "VERIFY_FAILED",
        "cell_diff_count": total,
        "tab_diff_counts": tab_diffs,
        "actual_workbook_content_hash": actual_workbook_hash,
        "expected_workbook_content_hash": expected_plan["workbook_content_hash"],
        "same_payload_second_run_diff_count": total,
        "would_write": total != 0,
    }


def build_p3_expected_live_plan(repo_root: Path) -> dict[str, Any]:
    locked = {
        Path("staging/yv-humanize/LIVE-STATE.md"): YV_LIVE_STATE_SHA256,
        Path("staging/yv-humanize/live-state.json"): YV_LIVE_STATE_JSON_SHA256,
        YV_PLAN_PATH: YV_PLAN_SHA256,
        YV_P27_DIR / "ledger-closure-plan.json": YV_P27_PLAN_SHA256,
        YV_P27_DIR / "p2.8-audit-evidence.json": "b6a857148014d5220b217022f2f10bedfe0c4352aa9f39f85c9eceae53b8b495",
        YV_P27_DIR / "readback-evidence.json": "5e11a21e48cc69f0dcef877f3e147b0f2845f144749f263774944cec10d46a55",
        YV_RECOVERY_DIR / "readback-evidence.json": YV_P26_READBACK_SHA256,
        Path("docs/system/toplink-google-sheets-operational-contract.md"): "082a1167034bdec8d1e85df245acbff4a245c1a7ea26df82fa71d0f55981d1c4",
    }
    for relative, expected_digest in locked.items():
        if sha256_file(repo_root / relative) != expected_digest:
            raise SyncError(f"P3.0 digest drift: {relative.as_posix()}")
    validate_repository_bindings(
        {"repository_bindings": YV_P3_REPOSITORY_BINDINGS}, repo_root
    )
    base_plan = build_human_layer_plan(repo_root)
    signed_plan = read_json(repo_root / YV_PLAN_PATH)
    if (
        base_plan["workbook_content_hash"] != YV_WORKBOOK_SHA256
        or [tab["content_hash"] for tab in base_plan["tabs"]]
        != [tab["content_hash"] for tab in signed_plan["tabs"]]
    ):
        raise SyncError("P3.1 base plan rebuild drift")
    closure = read_json(repo_root / YV_P27_DIR / "ledger-closure-plan.json")
    if closure != build_human_layer_ledger_closure(repo_root):
        raise SyncError("P3.1 closure overlay rebuild drift")
    expected = apply_human_layer_ledger_closure(base_plan, closure)
    if expected["workbook_content_hash"] != YV_LIVE_WORKBOOK_SHA256:
        raise SyncError("P3.1 live workbook hash drift")
    live_state = read_json(repo_root / "staging/yv-humanize/live-state.json")
    if live_state.get("live_baseline", {}).get("workbook_content_hash") != YV_LIVE_WORKBOOK_SHA256:
        raise SyncError("P3.1 LIVE-STATE baseline drift")
    return expected


def validate_p3_live_verify_approval(
    repo_root: Path, *, require_unconsumed: bool = True
) -> dict[str, Any]:
    relative = Path("staging/yv-humanize/approvals/approval-08-verify-live.md")
    path = repo_root / relative
    if sha256_file(path) != YV_P3_APPROVAL_SHA256:
        raise SyncError("P3 approval 08 digest drift")
    approval_text = path.read_text(encoding="utf-8")
    required = (
        "action: READBACK",
        "write_executed: false",
        "mutation_requests_allowed: 0",
        f"workbook_content_hash: {YV_LIVE_WORKBOOK_SHA256}",
    )
    if any(item not in approval_text for item in required):
        raise SyncError("P3 approval 08 field drift")
    expiry = re.search(r"^expires_at_ict:\s*(\S+)\s*$", approval_text, re.MULTILINE)
    if not expiry or datetime.fromisoformat(expiry.group(1)).astimezone(timezone.utc) <= datetime.now(timezone.utc):
        raise SyncError("P3 approval 08 expired or missing")
    ledger = (repo_root / "staging/yv-humanize/approvals/SIGNATURES.md").read_text(encoding="utf-8")
    signature_pattern = (
        re.escape(relative.as_posix())
        + r"[\s\S]{0,200}"
        + re.escape(YV_P3_APPROVAL_SHA256)
        + r"[\s\S]{0,80}\bAPPROVED\b"
    )
    if not re.search(signature_pattern, ledger) or "Approval 08" not in ledger:
        raise SyncError("P3 approval 08 signature missing or consumed")
    if require_unconsumed and "SIGNED · UNCONSUMED" not in ledger:
        raise SyncError("P3 approval 08 signature missing or consumed")
    if not require_unconsumed and not any(
        status in ledger
        for status in ("SIGNED · UNCONSUMED", "CONSUMED · LIVE_STATE_VERIFIED")
    ):
        raise SyncError("P3 approval 08 ledger status invalid")
    return {
        "approval_sha256": YV_P3_APPROVAL_SHA256,
        "mutation_requests_allowed": 0,
        "read_plane_count": 3,
        "workbook_content_hash": YV_LIVE_WORKBOOK_SHA256,
    }


def collect_human_layer_cell_mismatches(
    expected_plan: dict[str, Any], values_response: dict[str, Any]
) -> list[dict[str, Any]]:
    value_ranges = values_response.get("valueRanges", [])
    if len(value_ranges) != len(expected_plan["tabs"]):
        return [
            {
                "kind": "VALUE_RANGE_COUNT",
                "expected": len(expected_plan["tabs"]),
                "actual": len(value_ranges),
            }
        ]
    mismatches: list[dict[str, Any]] = []
    for tab, value_range in zip(expected_plan["tabs"], value_ranges):
        actual = _yv_normalize_read_values(
            value_range.get("values", []), tab["row_count"], tab["column_count"]
        )
        for row_index, (expected_row, actual_row) in enumerate(zip(tab["values"], actual)):
            for column_index, (expected_cell, actual_cell) in enumerate(zip(expected_row, actual_row)):
                if expected_cell != actual_cell:
                    mismatches.append(
                        {
                            "kind": "CELL_VALUE",
                            "cell": f"{tab['tab']}!{_yv_column(column_index)}{row_index + 1}",
                            "expected": expected_cell,
                            "actual": actual_cell,
                        }
                    )
    return mismatches


def _yv_rgb(hex_color: str) -> dict[str, float]:
    value = hex_color.lstrip("#")
    if not re.fullmatch(r"[0-9a-fA-F]{6}", value):
        raise SyncError(f"invalid palette color: {hex_color}")
    return {name: int(value[offset : offset + 2], 16) / 255 for name, offset in (("red", 0), ("green", 2), ("blue", 4))}


def build_human_layer_create_requests(plan: dict[str, Any]) -> list[dict[str, Any]]:
    requests: list[dict[str, Any]] = []
    for tab in plan["tabs"]:
        requests.append({
            "addSheet": {
                "properties": {
                    "title": tab["tab"],
                    "index": tab["index"],
                    "gridProperties": {"rowCount": tab["row_count"], "columnCount": tab["column_count"]},
                }
            }
        })
    if len(requests) != 21 or any(request["addSheet"]["properties"]["title"].endswith("_v2") for request in requests):
        raise SyncError("CREATE_TAB request scope drift")
    return requests


def _yv_registry_widths(registry_tab: dict[str, Any], width: int, default_width: int, narrow_width: int) -> list[int]:
    widths = [default_width] * width
    column_specs = list(registry_tab.get("display_columns", []))
    for section in registry_tab.get("sections", []):
        column_specs.extend(section.get("display_columns", []))
    declared: dict[int, list[int]] = {}
    for item in column_specs:
        position = int(item["pos"]) - 1
        if 0 <= position < width and item.get("width") is not None:
            declared.setdefault(position, []).append(int(item["width"]))
    for position, values in declared.items():
        widths[position] = max(values)
    widths[-2:] = [narrow_width, narrow_width]
    return widths


def _yv_a1_cell(address: str) -> tuple[int, int]:
    match = re.fullmatch(r"([A-Z]+)([1-9][0-9]*)", address)
    if not match:
        raise SyncError(f"invalid A1 cell: {address}")
    column = 0
    for char in match.group(1):
        column = column * 26 + ord(char) - 64
    return int(match.group(2)) - 1, column - 1


def build_human_layer_format_requests(
    plan: dict[str, Any], registry: dict[str, Any], sheet_ids: dict[str, int]
) -> list[dict[str, Any]]:
    requests: list[dict[str, Any]] = []
    registry_by_name = {tab["tab"]: tab for tab in registry["tabs"]}
    base_format = {
        "backgroundColor": _yv_rgb(plan["palette"]["sheet_background"]),
        "textFormat": {"foregroundColor": _yv_rgb(plan["palette"]["text"])},
        "wrapStrategy": "WRAP",
        "verticalAlignment": "TOP",
    }
    header_format = {
        "backgroundColor": _yv_rgb(plan["palette"]["header_bg"]),
        "textFormat": {"foregroundColor": _yv_rgb(plan["palette"]["header_fg"]), "bold": True},
        "wrapStrategy": "WRAP",
        "verticalAlignment": "TOP",
    }
    legend_format = {
        "backgroundColor": _yv_rgb(plan["palette"]["header_bg"]),
        "textFormat": {"foregroundColor": _yv_rgb(plan["palette"]["text_soft"]), "italic": True},
        "wrapStrategy": "WRAP",
        "verticalAlignment": "TOP",
    }
    gold = _yv_rgb(plan["palette"]["action_required"])
    for tab in plan["tabs"]:
        sheet_id = sheet_ids.get(tab["tab"])
        if not isinstance(sheet_id, int) or sheet_id == 0:
            raise SyncError(f"invalid human-layer sheet id: {tab['tab']}")
        bounded = {"sheetId": sheet_id, "startRowIndex": 0, "endRowIndex": tab["row_count"], "startColumnIndex": 0, "endColumnIndex": tab["column_count"]}
        requests.extend([
            {"updateSheetProperties": {"properties": {"sheetId": sheet_id, "gridProperties": {"frozenRowCount": 2}}, "fields": "gridProperties.frozenRowCount"}},
            {"setBasicFilter": {"filter": {"range": bounded}}},
            {"repeatCell": {"range": bounded, "cell": {"userEnteredFormat": base_format}, "fields": "userEnteredFormat(backgroundColor,textFormat.foregroundColor,wrapStrategy,verticalAlignment)"}},
            {"repeatCell": {"range": {**bounded, "endRowIndex": 1}, "cell": {"userEnteredFormat": header_format}, "fields": "userEnteredFormat(backgroundColor,textFormat,wrapStrategy,verticalAlignment)"}},
            {"repeatCell": {"range": {**bounded, "startRowIndex": 1, "endRowIndex": 2}, "cell": {"userEnteredFormat": legend_format}, "fields": "userEnteredFormat(backgroundColor,textFormat,wrapStrategy,verticalAlignment)"}},
        ])
        for section in tab.get("sections", []):
            for row_number in (section["header_row"] - 1, section["header_row"]):
                requests.append({"repeatCell": {"range": {**bounded, "startRowIndex": row_number - 1, "endRowIndex": row_number}, "cell": {"userEnteredFormat": header_format}, "fields": "userEnteredFormat(backgroundColor,textFormat,wrapStrategy,verticalAlignment)"}})
        widths = _yv_registry_widths(
            registry_by_name[tab["tab"]], tab["column_count"],
            int(plan["formatting"]["default_column_width"]), int(plan["formatting"]["narrow_column_width"]),
        )
        for column_index, pixel_size in enumerate(widths):
            properties: dict[str, Any] = {"pixelSize": pixel_size}
            fields = "pixelSize"
            if column_index >= tab["column_count"] - 2:
                properties["hiddenByUser"] = True
                fields += ",hiddenByUser"
            requests.append({"updateDimensionProperties": {"range": {"sheetId": sheet_id, "dimension": "COLUMNS", "startIndex": column_index, "endIndex": column_index + 1}, "properties": properties, "fields": fields}})
        for address in tab["yellow_cells"]:
            row_index, column_index = _yv_a1_cell(address)
            requests.append({"repeatCell": {"range": {"sheetId": sheet_id, "startRowIndex": row_index, "endRowIndex": row_index + 1, "startColumnIndex": column_index, "endColumnIndex": column_index + 1}, "cell": {"userEnteredFormat": {"backgroundColor": gold}}, "fields": "userEnteredFormat.backgroundColor"}})
    if any("addConditionalFormatRule" in request or "updateConditionalFormatRule" in request for request in requests):
        raise SyncError("conditional formatting is forbidden")
    return requests


def validate_human_layer_created_tabs(metadata: dict[str, Any]) -> dict[str, int]:
    properties = [item.get("properties", item) for item in metadata.get("sheets", [])]
    ordered = sorted(properties, key=lambda item: item.get("index", 0))
    if len(ordered) != 22:
        raise SyncError("CREATE_TAB readback sheet count drift")
    human = ordered[:21]
    preserved = ordered[21]
    if [item.get("title") for item in human] != list(TAB_KEYS):
        raise SyncError("CREATE_TAB readback title/index drift")
    if preserved.get("title") != "Trang tính1" or preserved.get("sheetId") != 0:
        raise SyncError("CREATE_TAB touched Trang tính1")
    return {item["title"]: int(item["sheetId"]) for item in human}


def _execute_human_layer_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    validate_active_lease(repo_root)
    approval_digests = validate_human_layer_approvals(repo_root)
    plan = read_json(repo_root / YV_PLAN_PATH)
    rebuilt = build_human_layer_plan(repo_root)
    if [tab["content_hash"] for tab in rebuilt["tabs"]] != [tab["content_hash"] for tab in plan["tabs"]] or rebuilt["workbook_content_hash"] != YV_WORKBOOK_SHA256:
        raise SyncError("P2.5 independent rebuild drift")
    registry = load_human_layer_registry(repo_root)
    validate_human_layer_plan(rebuilt, registry)
    service = _google_service(TARGET_SERVICE_ACCOUNT)
    spreadsheets = service.spreadsheets()
    metadata = spreadsheets.get(spreadsheetId=TARGET_SPREADSHEET_ID, fields="spreadsheetId,properties.title,sheets.properties(sheetId,title,index,gridProperties)").execute()
    credential_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    credential_email = str(read_json(Path(credential_path)).get("client_email", "")) if credential_path else ""
    validate_human_layer_target_snapshot(metadata, credential_email)

    evidence_path = repo_root / "staging/yv-humanize/execution-evidence.json"
    evidence: dict[str, Any] = {
        "status": "EXECUTION_STARTED",
        "spreadsheet_id": TARGET_SPREADSHEET_ID,
        "approval_digests": approval_digests,
        "plan_digest": YV_PLAN_SHA256,
        "workbook_content_hash": YV_WORKBOOK_SHA256,
        "completed_phases": [],
        "external_writes": 0,
    }
    write_json(evidence_path, evidence)
    try:
        create_requests = build_human_layer_create_requests(plan)
        create_response = spreadsheets.batchUpdate(spreadsheetId=TARGET_SPREADSHEET_ID, body={"requests": create_requests}).execute()
        evidence["external_writes"] += 1
        evidence["completed_phases"].append("CREATE_TAB")
        evidence["create_reply_count"] = len(create_response.get("replies", []))
        write_json(evidence_path, evidence)

        created_metadata = spreadsheets.get(spreadsheetId=TARGET_SPREADSHEET_ID, fields="sheets.properties(sheetId,title,index,gridProperties)").execute()
        sheet_ids = validate_human_layer_created_tabs(created_metadata)
        evidence["sheet_ids"] = sheet_ids
        evidence["completed_phases"].append("CREATE_TAB_READBACK_PASS")
        write_json(evidence_path, evidence)

        ranges = [tab["used_range"] for tab in plan["tabs"]]
        before_values = spreadsheets.values().batchGet(spreadsheetId=TARGET_SPREADSHEET_ID, ranges=ranges, majorDimension="ROWS").execute()
        before_grid = spreadsheets.get(
            spreadsheetId=TARGET_SPREADSHEET_ID,
            ranges=ranges,
            includeGridData=True,
            fields="sheets(properties(sheetId,title,index,gridProperties),basicFilter,conditionalFormats,data(startRow,startColumn,rowData.values(userEnteredValue,userEnteredFormat),columnMetadata,rowMetadata))",
        ).execute()
        before = {"snapshot_id": "YV-HUMAN-LAYER-BEFORE-UPSERT-01", "ranges": ranges, "values": before_values, "grid": before_grid, "external_writes": 0}
        before_path = repo_root / "staging/yv-humanize/before-ranges.json"
        write_json(before_path, before)
        evidence["before_snapshot_sha256"] = sha256_file(before_path)
        evidence["before_range_count"] = len(ranges)
        write_json(evidence_path, evidence)

        value_body = {"valueInputOption": "RAW", "data": [{"range": tab["used_range"], "majorDimension": "ROWS", "values": tab["values"]} for tab in plan["tabs"]]}
        value_response = spreadsheets.values().batchUpdate(spreadsheetId=TARGET_SPREADSHEET_ID, body=value_body).execute()
        evidence["external_writes"] += 1
        evidence["completed_phases"].append("UPSERT_VALUES_RAW")
        evidence["updated_cells"] = value_response.get("totalUpdatedCells")
        write_json(evidence_path, evidence)

        format_requests = build_human_layer_format_requests(plan, registry, sheet_ids)
        format_response = spreadsheets.batchUpdate(spreadsheetId=TARGET_SPREADSHEET_ID, body={"requests": format_requests}).execute()
        evidence["external_writes"] += 1
        evidence["completed_phases"].append("DIRECT_FORMAT")
        evidence["format_request_count"] = len(format_requests)
        evidence["format_reply_count"] = len(format_response.get("replies", []))
        evidence["status"] = "WRITE_COMPLETED_READBACK_PENDING"
        write_json(evidence_path, evidence)
    except Exception as exc:
        evidence["status"] = "VERIFY_FAILED"
        evidence["error_type"] = type(exc).__name__
        evidence["error"] = str(exc)
        write_json(evidence_path, evidence)
        raise
    print(json.dumps({"status": evidence["status"], "completed_phases": evidence["completed_phases"], "external_writes": evidence["external_writes"], "evidence": evidence_path.as_posix()}, ensure_ascii=True))
    return 0


def _yv_normalize_read_values(values: list[list[Any]], rows: int, columns: int) -> list[list[str]]:
    normalized: list[list[str]] = []
    for row_index in range(rows):
        source = values[row_index] if row_index < len(values) else []
        normalized.append([str(source[column_index]) if column_index < len(source) else "" for column_index in range(columns)])
    return normalized


def _yv_color_matches(actual: dict[str, Any], expected: dict[str, float]) -> bool:
    tolerance = 1 / 255 + 1e-7
    return all(abs(float(actual.get(channel, 0.0)) - value) <= tolerance for channel, value in expected.items())


def human_layer_grid_ranges(plan: dict[str, Any]) -> list[str]:
    return [tab["used_range"] for tab in plan["tabs"]]


def validate_human_layer_topology_metadata(metadata: dict[str, Any]) -> None:
    properties = [item.get("properties", {}) for item in metadata.get("sheets", [])]
    ordered = sorted(properties, key=lambda item: item.get("index", 0))
    if len(ordered) != 22 or [item.get("title") for item in ordered[:21]] != list(TAB_KEYS):
        raise SyncError("readback topology title/index/count drift")
    preserved = ordered[21]
    preserved_grid = preserved.get("gridProperties", {})
    if (
        preserved.get("title") != "Trang tính1"
        or preserved.get("sheetId") != 0
        or preserved_grid.get("rowCount") != 1000
        or preserved_grid.get("columnCount") != 26
    ):
        raise SyncError("readback topology Trang tính1 metadata drift")
    if any(str(item.get("title", "")).endswith("_v2") for item in ordered):
        raise SyncError("readback topology forbidden _v2 tab")


def validate_human_layer_grid_scope(metadata: dict[str, Any]) -> set[str]:
    titles = {item.get("properties", {}).get("title") for item in metadata.get("sheets", [])}
    if titles != set(TAB_KEYS) or len(metadata.get("sheets", [])) != 21:
        raise SyncError("readback grid scope drift")
    return {str(title) for title in titles}


def validate_blank_human_layer_recovery_target(
    plan: dict[str, Any],
    topology_metadata: dict[str, Any],
    grid_metadata: dict[str, Any],
    values_response: dict[str, Any],
) -> dict[str, Any]:
    validate_human_layer_topology_metadata(topology_metadata)
    validate_human_layer_grid_scope(grid_metadata)
    value_ranges = values_response.get("valueRanges", [])
    if len(value_ranges) != 21 or any(item.get("values") for item in value_ranges):
        raise SyncError("recovery target is not blank across all 21 ranges")
    by_title = {
        item.get("properties", {}).get("title"): item for item in grid_metadata.get("sheets", [])
    }
    sheet_ids: dict[str, int] = {}
    for tab in plan["tabs"]:
        sheet = by_title[tab["tab"]]
        properties = sheet.get("properties", {})
        grid = properties.get("gridProperties", {})
        if (
            grid.get("rowCount") != tab["row_count"]
            or grid.get("columnCount") != tab["column_count"]
            or grid.get("frozenRowCount", 0) != 0
        ):
            raise SyncError(f"recovery target grid drift: {tab['tab']}")
        if "basicFilter" in sheet or sheet.get("conditionalFormats"):
            raise SyncError(f"recovery target formatting not reset: {tab['tab']}")
        for data in sheet.get("data", []):
            for column in data.get("columnMetadata", []):
                if column.get("hiddenByUser") is True or column.get("pixelSize") not in (None, 100):
                    raise SyncError(f"recovery target column state drift: {tab['tab']}")
            for row in data.get("rowData", []):
                for cell in row.get("values", []):
                    if cell.get("userEnteredValue") or cell.get("userEnteredFormat"):
                        raise SyncError(f"recovery target cell state drift: {tab['tab']}")
        sheet_ids[tab["tab"]] = int(properties["sheetId"])
    if any(sheet.get("conditionalFormats") for sheet in topology_metadata.get("sheets", [])):
        raise SyncError("recovery target conditional-format rules remain")
    return {"blank_range_count": 21, "sheet_ids": sheet_ids, "conditional_format_rule_count": 0}


def validate_live_human_layer_readback(
    plan: dict[str, Any],
    registry: dict[str, Any],
    topology_metadata: dict[str, Any],
    grid_metadata: dict[str, Any],
    values_response: dict[str, Any],
) -> dict[str, Any]:
    validate_human_layer_topology_metadata(topology_metadata)
    validate_human_layer_grid_scope(grid_metadata)

    value_ranges = values_response.get("valueRanges", [])
    if len(value_ranges) != 21:
        raise SyncError("readback value range count drift")
    actual_plan = copy.deepcopy(plan)
    actual_by_name = {tab["tab"]: tab for tab in actual_plan["tabs"]}
    content_hashes: list[str] = []
    for expected_tab, value_range in zip(plan["tabs"], value_ranges):
        normalized = _yv_normalize_read_values(
            value_range.get("values", []), expected_tab["row_count"], expected_tab["column_count"]
        )
        if normalized != expected_tab["values"]:
            raise SyncError(f"readback value mismatch: {expected_tab['tab']}")
        if any(unicodedata.normalize("NFC", cell) != cell for row in normalized for cell in row):
            raise SyncError(f"readback Unicode NFC drift: {expected_tab['tab']}")
        digest = _yv_content_hash(normalized)
        if digest != expected_tab["content_hash"]:
            raise SyncError(f"readback content hash drift: {expected_tab['tab']}")
        actual_by_name[expected_tab["tab"]]["values"] = normalized
        content_hashes.append(digest)
    workbook_hash = hashlib.sha256(json.dumps(content_hashes, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
    if workbook_hash != plan["workbook_content_hash"]:
        raise SyncError("readback workbook content hash drift")
    validate_human_layer_plan(actual_plan, registry)

    sheet_by_title = {
        item.get("properties", {}).get("title"): item for item in grid_metadata.get("sheets", [])
    }
    registry_by_name = {tab["tab"]: tab for tab in registry["tabs"]}
    gold = _yv_rgb(plan["palette"]["action_required"])
    cream = _yv_rgb(plan["palette"]["header_bg"])
    ivory = _yv_rgb(plan["palette"]["sheet_background"])
    gold_coordinates: list[str] = []
    hidden_count = 0
    conditional_count = sum(
        len(sheet.get("conditionalFormats", [])) for sheet in topology_metadata.get("sheets", [])
    )
    for tab in plan["tabs"]:
        sheet = sheet_by_title.get(tab["tab"])
        if not sheet:
            raise SyncError(f"readback missing sheet metadata: {tab['tab']}")
        grid = sheet["properties"].get("gridProperties", {})
        if grid.get("rowCount") != tab["row_count"] or grid.get("columnCount") != tab["column_count"] or grid.get("frozenRowCount") != 2:
            raise SyncError(f"readback grid/freeze drift: {tab['tab']}")
        if "basicFilter" not in sheet:
            raise SyncError(f"readback basicFilter missing: {tab['tab']}")
        data = sheet.get("data", [])
        if not data:
            raise SyncError(f"readback grid data missing: {tab['tab']}")
        grid_data = data[0]
        columns = grid_data.get("columnMetadata", [])
        expected_widths = _yv_registry_widths(
            registry_by_name[tab["tab"]], tab["column_count"],
            int(plan["formatting"]["default_column_width"]), int(plan["formatting"]["narrow_column_width"]),
        )
        if len(columns) < tab["column_count"]:
            raise SyncError(f"readback column metadata missing: {tab['tab']}")
        for column_index, expected_width in enumerate(expected_widths):
            column = columns[column_index]
            if column.get("pixelSize") != expected_width:
                raise SyncError(f"readback column width drift: {tab['tab']}:{column_index + 1}")
            hidden = column.get("hiddenByUser") is True
            should_hide = column_index >= tab["column_count"] - 2
            if hidden != should_hide:
                raise SyncError(f"readback hidden column drift: {tab['tab']}:{column_index + 1}")
            hidden_count += int(hidden)
        section_rows = {
            row_number - 1
            for section in tab.get("sections", [])
            for row_number in (section["header_row"] - 1, section["header_row"])
        }
        row_data = grid_data.get("rowData", [])
        declared_gold = set(tab["yellow_cells"])
        for row_index in range(tab["row_count"]):
            cells = row_data[row_index].get("values", []) if row_index < len(row_data) else []
            for column_index in range(tab["column_count"]):
                cell = cells[column_index] if column_index < len(cells) else {}
                effective = cell.get("effectiveFormat", {})
                address = f"{_yv_column(column_index)}{row_index + 1}"
                expected_background = gold if address in declared_gold else (cream if row_index in {0, 1} | section_rows else ivory)
                if not _yv_color_matches(effective.get("backgroundColor", {}), expected_background):
                    raise SyncError(f"readback background drift: {tab['tab']}!{address}")
                if effective.get("wrapStrategy") != "WRAP" or effective.get("verticalAlignment") != "TOP":
                    raise SyncError(f"readback wrap/alignment drift: {tab['tab']}!{address}")
                if _yv_color_matches(effective.get("backgroundColor", {}), gold):
                    gold_coordinates.append(f"{tab['tab']}!{address}")
    expected_gold = [f"{tab['tab']}!{address}" for tab in plan["tabs"] for address in tab["yellow_cells"]]
    if gold_coordinates != expected_gold or len(gold_coordinates) != 27:
        raise SyncError("readback yellow coordinate/count drift")
    if hidden_count != 42:
        raise SyncError("readback hidden _key/_audit count drift")
    if conditional_count != 0:
        raise SyncError("readback conditional-format rule drift")
    return {
        "status": "SYNC_READBACK_PASS",
        "tab_count": 21,
        "sheet_count_including_preserved": 22,
        "workbook_content_hash": workbook_hash,
        "yellow_cell_count": len(gold_coordinates),
        "yellow_cells": gold_coordinates,
        "hidden_column_count": hidden_count,
        "conditional_format_rule_count": conditional_count,
        "preserved_trang_tinh1_sheet_id": 0,
        "mismatch_count": 0,
    }


def _restore_human_layer_before(spreadsheets: Any, plan: dict[str, Any], sheet_ids: dict[str, int]) -> int:
    ranges = [tab["used_range"] for tab in plan["tabs"]]
    spreadsheets.values().batchClear(spreadsheetId=TARGET_SPREADSHEET_ID, body={"ranges": ranges}).execute()
    requests: list[dict[str, Any]] = []
    for tab in plan["tabs"]:
        sheet_id = sheet_ids[tab["tab"]]
        bounded = {"sheetId": sheet_id, "startRowIndex": 0, "endRowIndex": tab["row_count"], "startColumnIndex": 0, "endColumnIndex": tab["column_count"]}
        requests.extend([
            {"clearBasicFilter": {"sheetId": sheet_id}},
            {"updateSheetProperties": {"properties": {"sheetId": sheet_id, "gridProperties": {"frozenRowCount": 0}}, "fields": "gridProperties.frozenRowCount"}},
            {"repeatCell": {"range": bounded, "cell": {"userEnteredFormat": {}}, "fields": "userEnteredFormat"}},
            {"updateDimensionProperties": {"range": {"sheetId": sheet_id, "dimension": "COLUMNS", "startIndex": 0, "endIndex": tab["column_count"]}, "properties": {"pixelSize": 100, "hiddenByUser": False}, "fields": "pixelSize,hiddenByUser"}},
        ])
    spreadsheets.batchUpdate(spreadsheetId=TARGET_SPREADSHEET_ID, body={"requests": requests}).execute()
    return 2


def _read_human_layer_planes(spreadsheets: Any, plan: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    topology = spreadsheets.get(
        spreadsheetId=TARGET_SPREADSHEET_ID,
        fields="spreadsheetId,properties.title,sheets(properties(sheetId,title,index,gridProperties),basicFilter,conditionalFormats)",
    ).execute()
    ranges = human_layer_grid_ranges(plan)
    values_response = spreadsheets.values().batchGet(
        spreadsheetId=TARGET_SPREADSHEET_ID,
        ranges=ranges,
        majorDimension="ROWS",
        valueRenderOption="UNFORMATTED_VALUE",
    ).execute()
    grid_metadata = spreadsheets.get(
        spreadsheetId=TARGET_SPREADSHEET_ID, ranges=ranges, includeGridData=True
    ).execute()
    return topology, grid_metadata, values_response


def _execute_human_layer_recovery_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    validate_active_lease(repo_root)
    approval_digests = validate_human_layer_recovery_approvals(repo_root)
    plan = read_json(repo_root / YV_PLAN_PATH)
    rebuilt = build_human_layer_plan(repo_root)
    if (
        rebuilt["workbook_content_hash"] != YV_WORKBOOK_SHA256
        or [tab["content_hash"] for tab in rebuilt["tabs"]]
        != [tab["content_hash"] for tab in plan["tabs"]]
    ):
        raise SyncError("P2.6 recovery independent rebuild drift")
    registry = load_human_layer_registry(repo_root)
    validate_human_layer_plan(rebuilt, registry)
    service = _google_service(TARGET_SERVICE_ACCOUNT)
    spreadsheets = service.spreadsheets()
    topology, grid_metadata, values_response = _read_human_layer_planes(spreadsheets, plan)
    target = validate_blank_human_layer_recovery_target(
        plan, topology, grid_metadata, values_response
    )
    before_path = repo_root / YV_RECOVERY_DIR / "before-recovery-upsert.json"
    write_json(
        before_path,
        {
            "snapshot_id": "YV-P2.6-BEFORE-RECOVERY-UPSERT-01",
            "topology": topology,
            "grid": grid_metadata,
            "values": values_response,
            "external_writes": 0,
        },
    )
    evidence_path = repo_root / YV_RECOVERY_DIR / "execution-evidence.json"
    evidence: dict[str, Any] = {
        "status": "RECOVERY_EXECUTION_STARTED",
        "approval_digests": approval_digests,
        "snapshot_sha256": YV_RECOVERY_SNAPSHOT_SHA256,
        "before_snapshot_sha256": sha256_file(before_path),
        "plan_digest": YV_PLAN_SHA256,
        "workbook_content_hash": YV_WORKBOOK_SHA256,
        "sheet_ids": target["sheet_ids"],
        "completed_phases": [],
        "external_writes": 0,
    }
    write_json(evidence_path, evidence)
    mutation_started = False
    try:
        mutation_started = True
        value_response = spreadsheets.values().batchUpdate(
            spreadsheetId=TARGET_SPREADSHEET_ID,
            body={
                "valueInputOption": "RAW",
                "data": [
                    {"range": tab["used_range"], "majorDimension": "ROWS", "values": tab["values"]}
                    for tab in plan["tabs"]
                ],
            },
        ).execute()
        evidence["external_writes"] = 1
        evidence["completed_phases"].append("UPSERT_RECOVERY_VALUES_RAW")
        evidence["updated_cells"] = value_response.get("totalUpdatedCells")
        write_json(evidence_path, evidence)
        format_requests = build_human_layer_format_requests(
            plan, registry, target["sheet_ids"]
        )
        format_response = spreadsheets.batchUpdate(
            spreadsheetId=TARGET_SPREADSHEET_ID, body={"requests": format_requests}
        ).execute()
        evidence["external_writes"] = 2
        evidence["completed_phases"].append("UPSERT_RECOVERY_DIRECT_FORMAT")
        evidence["format_request_count"] = len(format_requests)
        evidence["format_reply_count"] = len(format_response.get("replies", []))
        evidence["status"] = "RECOVERY_WRITE_COMPLETED_READBACK_PENDING"
        write_json(evidence_path, evidence)
    except Exception as exc:
        evidence["status"] = "VERIFY_FAILED"
        evidence["error_type"] = type(exc).__name__
        evidence["error"] = str(exc)
        if mutation_started:
            restore_writes = _restore_human_layer_before(
                spreadsheets, plan, target["sheet_ids"]
            )
            evidence["restore_executed"] = True
            evidence["restore_external_writes"] = restore_writes
            evidence["external_writes"] += restore_writes
        write_json(evidence_path, evidence)
        raise
    print(json.dumps({"status": evidence["status"], "external_writes": 2, "evidence": evidence_path.as_posix()}, ensure_ascii=True))
    return 0


def _verify_human_layer_recovery_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    validate_active_lease(repo_root)
    approval_digests = validate_human_layer_recovery_approvals(repo_root)
    plan = read_json(repo_root / YV_PLAN_PATH)
    registry = load_human_layer_registry(repo_root)
    execution_path = repo_root / YV_RECOVERY_DIR / "execution-evidence.json"
    execution = read_json(execution_path)
    if execution.get("status") != "RECOVERY_WRITE_COMPLETED_READBACK_PENDING":
        raise SyncError("P2.6 recovery readback requires completed recovery write")
    service = _google_service(TARGET_SERVICE_ACCOUNT)
    spreadsheets = service.spreadsheets()
    topology, grid_metadata, values_response = _read_human_layer_planes(spreadsheets, plan)
    readback_path = repo_root / YV_RECOVERY_DIR / "readback-evidence.json"
    try:
        evidence = validate_live_human_layer_readback(
            plan, registry, topology, grid_metadata, values_response
        )
        evidence.update(
            {
                "recovery": True,
                "approval_digest": approval_digests["READBACK_RECOVERY"],
                "read_plane_count": 3,
                "external_writes": 0,
                "restore_executed": False,
            }
        )
        execution["status"] = "SYNC_READBACK_PASS"
        execution["completed_phases"].append("RECOVERY_EXACT_READBACK")
        write_json(execution_path, execution)
    except Exception as exc:
        restore_writes = _restore_human_layer_before(
            spreadsheets, plan, execution["sheet_ids"]
        )
        evidence = {
            "status": "VERIFY_FAILED",
            "recovery": True,
            "mismatch_count": 1,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "restore_executed": True,
            "restore_external_writes": restore_writes,
            "automatic_retry": False,
        }
        execution["status"] = "VERIFY_FAILED"
        execution["restore_executed"] = True
        execution["external_writes"] += restore_writes
        write_json(execution_path, execution)
        write_json(readback_path, evidence)
        raise SyncError(f"P2.6 recovery readback failed and before state restored: {exc}") from exc
    write_json(readback_path, evidence)
    print(json.dumps(evidence, ensure_ascii=True))
    return 0


def _snapshot_human_layer_recovery_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    validate_active_lease(repo_root)
    plan = read_json(repo_root / YV_PLAN_PATH)
    service = _google_service(TARGET_SERVICE_ACCOUNT)
    spreadsheets = service.spreadsheets()
    topology = spreadsheets.get(
        spreadsheetId=TARGET_SPREADSHEET_ID,
        fields="spreadsheetId,properties.title,sheets(properties(sheetId,title,index,gridProperties),basicFilter,conditionalFormats)",
    ).execute()
    ranges = human_layer_grid_ranges(plan)
    values_response = spreadsheets.values().batchGet(
        spreadsheetId=TARGET_SPREADSHEET_ID, ranges=ranges, majorDimension="ROWS"
    ).execute()
    grid_metadata = spreadsheets.get(
        spreadsheetId=TARGET_SPREADSHEET_ID, ranges=ranges, includeGridData=True
    ).execute()
    validated = validate_blank_human_layer_recovery_target(
        plan, topology, grid_metadata, values_response
    )
    evidence = {
        "snapshot_id": "YV-P2.6-RECOVERY-TARGET-01",
        "spreadsheet_id": TARGET_SPREADSHEET_ID,
        "spreadsheet_title": topology.get("properties", {}).get("title"),
        "read_only": True,
        "external_writes": 0,
        "tab_order": [
            item.get("properties", {}).get("title")
            for item in sorted(topology.get("sheets", []), key=lambda item: item.get("properties", {}).get("index", 0))
        ],
        "human_sheet_ids": validated["sheet_ids"],
        "blank_range_count": validated["blank_range_count"],
        "conditional_format_rule_count": validated["conditional_format_rule_count"],
        "preserved_trang_tinh1_sheet_id": 0,
        "plan_digest": sha256_file(repo_root / YV_PLAN_PATH),
        "workbook_content_hash": plan["workbook_content_hash"],
    }
    output = repo_root / "staging/yv-humanize/live-state-after-restore.json"
    write_json(output, evidence)
    print(json.dumps({"status": "PASS", "blank_ranges": 21, "external_writes": 0, "snapshot_sha256": sha256_file(output), "output": output.as_posix()}, ensure_ascii=True))
    return 0


def _build_human_layer_ledger_closure_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    validate_active_lease(repo_root)
    closure = build_human_layer_ledger_closure(repo_root)
    output = repo_root / YV_P27_DIR / "ledger-closure-plan.json"
    write_json(output, closure)
    print(
        json.dumps(
            {
                "status": "DRAFT_UNSIGNED",
                "external_writes": 0,
                "payload_digest": closure["payload_digest"],
                "file_sha256": sha256_file(output),
                "output": output.as_posix(),
            },
            ensure_ascii=True,
        )
    )
    return 0


def _p27_sheet_ids(topology: dict[str, Any]) -> dict[str, int]:
    validate_human_layer_topology_metadata(topology)
    return {
        str(sheet["properties"]["title"]): int(sheet["properties"]["sheetId"])
        for sheet in topology["sheets"]
        if sheet.get("properties", {}).get("title") in TAB_KEYS
    }


def _restore_p27_before(
    spreadsheets: Any, base_plan: dict[str, Any], sheet_ids: dict[str, int]
) -> int:
    by_name = {tab["tab"]: tab for tab in base_plan["tabs"]}
    output = by_name["03_OUTPUT_INDEX"]
    output_rows = [
        {
            "values": [
                {"userEnteredValue": {"stringValue": str(row[4])}},
                {"userEnteredValue": {"stringValue": str(row[5])}},
            ]
        }
        for row in output["values"][2:]
    ]
    output_id = sheet_ids["03_OUTPUT_INDEX"]
    decisions_id = sheet_ids["04_DECISIONS"]
    requests = [
        {
            "updateCells": {
                "range": {
                    "sheetId": output_id,
                    "startRowIndex": 2,
                    "endRowIndex": 21,
                    "startColumnIndex": 4,
                    "endColumnIndex": 6,
                },
                "rows": output_rows,
                "fields": "userEnteredValue",
            }
        },
        {
            "updateSheetProperties": {
                "properties": {"sheetId": decisions_id, "gridProperties": {"rowCount": 19}},
                "fields": "gridProperties.rowCount",
            }
        },
        {
            "setBasicFilter": {
                "filter": {
                    "range": {
                        "sheetId": decisions_id,
                        "startRowIndex": 0,
                        "endRowIndex": 19,
                        "startColumnIndex": 0,
                        "endColumnIndex": 10,
                    }
                }
            }
        },
    ]
    spreadsheets.batchUpdate(
        spreadsheetId=TARGET_SPREADSHEET_ID, body={"requests": requests}
    ).execute()
    return 1


def _execute_human_layer_ledger_closure_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    validate_active_lease(repo_root)
    approval_digests = validate_human_layer_ledger_closure_approvals(repo_root)
    closure = read_json(repo_root / YV_P27_DIR / "ledger-closure-plan.json")
    base_plan = build_human_layer_plan(repo_root)
    if base_plan["workbook_content_hash"] != YV_WORKBOOK_SHA256:
        raise SyncError("P2.7 base plan rebuild drift")
    expected = apply_human_layer_ledger_closure(base_plan, closure)
    registry = load_human_layer_registry(repo_root)
    validate_human_layer_plan(expected, registry)
    service = _google_service(TARGET_SERVICE_ACCOUNT)
    spreadsheets = service.spreadsheets()
    topology, grid_metadata, values_response = _read_human_layer_planes(
        spreadsheets, base_plan
    )
    validate_live_human_layer_readback(
        base_plan, registry, topology, grid_metadata, values_response
    )
    sheet_ids = _p27_sheet_ids(topology)
    before_path = repo_root / YV_P27_DIR / "before-ledger-closure.json"
    write_json(
        before_path,
        {
            "snapshot_id": "YV-P2.7-BEFORE-LEDGER-CLOSURE-01",
            "output_status_values": [row[4:6] for row in next(tab for tab in base_plan["tabs"] if tab["tab"] == "03_OUTPUT_INDEX")["values"][2:]],
            "decisions_row_count": 19,
            "external_writes": 0,
        },
    )
    evidence_path = repo_root / YV_P27_DIR / "execution-evidence.json"
    evidence: dict[str, Any] = {
        "status": "P2_7_EXECUTION_STARTED",
        "approval_digests": approval_digests,
        "closure_plan_sha256": YV_P27_PLAN_SHA256,
        "before_snapshot_sha256": sha256_file(before_path),
        "base_workbook_content_hash": YV_WORKBOOK_SHA256,
        "expected_workbook_content_hash": expected["workbook_content_hash"],
        "completed_phases": [],
        "external_writes": 0,
        "sheet_ids": {
            "03_OUTPUT_INDEX": sheet_ids["03_OUTPUT_INDEX"],
            "04_DECISIONS": sheet_ids["04_DECISIONS"],
        },
    }
    write_json(evidence_path, evidence)
    mutation_started = False
    try:
        mutation_started = True
        structural = build_p27_structural_requests(
            base_plan, sheet_ids["04_DECISIONS"]
        )
        spreadsheets.batchUpdate(
            spreadsheetId=TARGET_SPREADSHEET_ID, body={"requests": structural}
        ).execute()
        evidence["external_writes"] = 1
        evidence["completed_phases"].append("RESIZE_AND_DIRECT_FORMAT_DECISION_ROW")
        write_json(evidence_path, evidence)
        value_reply = spreadsheets.values().batchUpdate(
            spreadsheetId=TARGET_SPREADSHEET_ID,
            body={
                "valueInputOption": "RAW",
                "data": [
                    {
                        "range": action["range"],
                        "majorDimension": "ROWS",
                        "values": action["values"],
                    }
                    for action in closure["actions"]
                ],
            },
        ).execute()
        evidence["external_writes"] = 2
        evidence["completed_phases"].append("LEDGER_VALUES_RAW")
        evidence["updated_cells"] = value_reply.get("totalUpdatedCells")
        evidence["status"] = "P2_7_WRITE_COMPLETED_READBACK_PENDING"
        write_json(evidence_path, evidence)
    except Exception as exc:
        evidence["status"] = "VERIFY_FAILED"
        evidence["error_type"] = type(exc).__name__
        evidence["error"] = str(exc)
        if mutation_started:
            evidence["restore_executed"] = True
            evidence["restore_external_writes"] = _restore_p27_before(
                spreadsheets, base_plan, sheet_ids
            )
        write_json(evidence_path, evidence)
        raise
    print(json.dumps({"status": evidence["status"], "external_writes": 2}, ensure_ascii=True))
    return 0


def _verify_human_layer_ledger_closure_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    validate_active_lease(repo_root)
    approvals = validate_human_layer_ledger_closure_approvals(repo_root)
    closure = read_json(repo_root / YV_P27_DIR / "ledger-closure-plan.json")
    base_plan = build_human_layer_plan(repo_root)
    expected = apply_human_layer_ledger_closure(base_plan, closure)
    registry = load_human_layer_registry(repo_root)
    execution_path = repo_root / YV_P27_DIR / "execution-evidence.json"
    execution = read_json(execution_path)
    if execution.get("status") != "P2_7_WRITE_COMPLETED_READBACK_PENDING":
        raise SyncError("P2.7 readback requires completed ledger write")
    service = _google_service(TARGET_SERVICE_ACCOUNT)
    spreadsheets = service.spreadsheets()
    topology, grid_metadata, values_response = _read_human_layer_planes(
        spreadsheets, expected
    )
    readback_path = repo_root / YV_P27_DIR / "readback-evidence.json"
    values_path = repo_root / YV_P27_DIR / "readback-values.json"
    try:
        evidence = validate_live_human_layer_readback(
            expected, registry, topology, grid_metadata, values_response
        )
        write_json(values_path, values_response)
        evidence.update(
            {
                "p2_7": True,
                "approval_digest": approvals["P2_7_LEDGER_READBACK"],
                "read_plane_count": 3,
                "readback_values_sha256": sha256_file(values_path),
                "external_writes": 0,
                "restore_executed": False,
            }
        )
        execution["status"] = "SYNC_READBACK_PASS"
        execution["completed_phases"].append("P2_7_EXACT_READBACK")
        write_json(execution_path, execution)
    except Exception as exc:
        restore_writes = _restore_p27_before(
            spreadsheets, base_plan, execution["sheet_ids"]
        )
        evidence = {
            "status": "VERIFY_FAILED",
            "p2_7": True,
            "mismatch_count": 1,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "restore_executed": True,
            "restore_external_writes": restore_writes,
            "automatic_retry": False,
        }
        execution["status"] = "VERIFY_FAILED"
        execution["restore_executed"] = True
        execution["external_writes"] += restore_writes
        write_json(execution_path, execution)
        write_json(readback_path, evidence)
        raise SyncError(f"P2.7 readback failed and before state restored: {exc}") from exc
    write_json(readback_path, evidence)
    print(json.dumps(evidence, ensure_ascii=True))
    return 0


def _audit_human_layer_idempotency_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    validate_active_lease(repo_root)
    validate_human_layer_ledger_closure_approvals(
        repo_root, require_unconsumed=False
    )
    readback_path = repo_root / YV_P27_DIR / "readback-evidence.json"
    readback = read_json(readback_path)
    values_path = repo_root / YV_P27_DIR / "readback-values.json"
    if readback.get("status") != "SYNC_READBACK_PASS":
        raise SyncError("P2.8 requires P2.7 SYNC_READBACK_PASS")
    if readback.get("readback_values_sha256") != sha256_file(values_path):
        raise SyncError("P2.8 frozen readback values digest drift")
    base_plan = build_human_layer_plan(repo_root)
    closure = build_human_layer_ledger_closure(repo_root)
    expected = apply_human_layer_ledger_closure(base_plan, closure)
    registry = load_human_layer_registry(repo_root)
    validate_human_layer_plan(expected, registry)
    audit = audit_human_layer_idempotency(expected, read_json(values_path))
    if audit["cell_diff_count"] != 0 or audit["actual_workbook_content_hash"] != expected["workbook_content_hash"]:
        raise SyncError("P2.8 independent compile/readback mismatch")
    audit.update(
        {
            "audit_id": "YV-P2.8-INDEPENDENT-AUDIT-01",
            "independent_markdown_rebuild": True,
            "source_digest_count": len(base_plan["source_digests"]),
            "tab_count": 21,
            "format_readback_status": readback["status"],
            "planned_structural_diff_count": 0,
            "external_writes": 0,
            "network_calls": 0,
        }
    )
    output = repo_root / YV_P27_DIR / "p2.8-audit-evidence.json"
    write_json(output, audit)
    print(json.dumps({**audit, "evidence_sha256": sha256_file(output)}, ensure_ascii=True))
    return 0


def _verify_live_state_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    validate_active_lease(repo_root)
    approval = validate_p3_live_verify_approval(repo_root)
    expected = build_p3_expected_live_plan(repo_root)
    registry = load_human_layer_registry(repo_root)
    validate_human_layer_plan(expected, registry)
    service = _google_service(TARGET_SERVICE_ACCOUNT)
    spreadsheets = service.spreadsheets()
    topology, grid_metadata, values_response = _read_human_layer_planes(
        spreadsheets, expected
    )
    mismatches = collect_human_layer_cell_mismatches(expected, values_response)
    value_audit: dict[str, Any] | None = None
    if not mismatches:
        value_audit = audit_human_layer_idempotency(expected, values_response)
    output = repo_root / "staging/yv-humanize/p3-verify/live-verify-evidence.json"
    common: dict[str, Any] = {
        "approval_sha256": approval["approval_sha256"],
        "expected_workbook_content_hash": YV_LIVE_WORKBOOK_SHA256,
        "mutation_requests_sent": 0,
        "read_plane_count": 3,
        "read_request_count": 3,
        "request_counts": {
            "spreadsheets.get": 2,
            "values.batchGet": 1,
            "mutation": 0,
        },
        "verified_at_ict": datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    try:
        if mismatches:
            raise SyncError(f"live value drift in {len(mismatches)} cell(s)")
        validated = validate_live_human_layer_readback(
            expected, registry, topology, grid_metadata, values_response
        )
        evidence = {
            **common,
            "verdict": "LIVE_STATE_VERIFIED",
            "workbook_content_hash": validated["workbook_content_hash"],
            "mismatch_count": 0,
            "mismatches": [],
            "yellow_cell_count": validated["yellow_cell_count"],
            "hidden_column_count": validated["hidden_column_count"],
            "conditional_format_rule_count": validated["conditional_format_rule_count"],
            "sheet_count_including_preserved": validated["sheet_count_including_preserved"],
            "preserved_trang_tinh1_sheet_id": validated["preserved_trang_tinh1_sheet_id"],
        }
    except SyncError as exc:
        if not mismatches:
            mismatches = [{"kind": "STRUCTURE_OR_FORMAT", "message": str(exc)}]
        preserved = next(
            (
                sheet.get("properties", {}).get("sheetId")
                for sheet in topology.get("sheets", [])
                if sheet.get("properties", {}).get("title") == "Trang tính1"
            ),
            None,
        )
        evidence = {
            **common,
            "verdict": "LIVE_STATE_DRIFTED",
            "workbook_content_hash": (
                value_audit.get("actual_workbook_content_hash") if value_audit else None
            ),
            "mismatch_count": len(mismatches),
            "mismatches": mismatches,
            "yellow_cell_count": None,
            "hidden_column_count": None,
            "conditional_format_rule_count": sum(
                len(sheet.get("conditionalFormats", []))
                for sheet in topology.get("sheets", [])
            ),
            "sheet_count_including_preserved": len(topology.get("sheets", [])),
            "preserved_trang_tinh1_sheet_id": preserved,
            "error": str(exc),
        }
    write_json(output, evidence)
    print(json.dumps({**evidence, "evidence_sha256": sha256_file(output)}, ensure_ascii=True))
    return 0 if evidence["verdict"] == "LIVE_STATE_VERIFIED" else 1


def _verify_readback_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    validate_active_lease(repo_root)
    approval_digests = validate_human_layer_approvals(repo_root)
    plan = read_json(repo_root / YV_PLAN_PATH)
    registry = load_human_layer_registry(repo_root)
    execution_path = repo_root / "staging/yv-humanize/execution-evidence.json"
    execution = read_json(execution_path)
    if execution.get("status") != "WRITE_COMPLETED_READBACK_PENDING" or execution.get("completed_phases")[-1:] != ["DIRECT_FORMAT"]:
        raise SyncError("readback requires completed P2.5 execution")
    service = _google_service(TARGET_SERVICE_ACCOUNT)
    spreadsheets = service.spreadsheets()
    ranges = [tab["used_range"] for tab in plan["tabs"]]
    values_response = spreadsheets.values().batchGet(
        spreadsheetId=TARGET_SPREADSHEET_ID, ranges=ranges, majorDimension="ROWS", valueRenderOption="UNFORMATTED_VALUE"
    ).execute()
    topology_metadata = spreadsheets.get(
        spreadsheetId=TARGET_SPREADSHEET_ID,
        fields="sheets(properties(sheetId,title,index,gridProperties),conditionalFormats)",
    ).execute()
    grid_metadata = spreadsheets.get(
        spreadsheetId=TARGET_SPREADSHEET_ID,
        ranges=human_layer_grid_ranges(plan),
        includeGridData=True,
    ).execute()
    readback_path = repo_root / "staging/yv-humanize/readback-evidence.json"
    try:
        evidence = validate_live_human_layer_readback(
            plan, registry, topology_metadata, grid_metadata, values_response
        )
        evidence.update({"approval_digest": approval_digests["READBACK"], "external_writes": 0, "restore_executed": False})
        execution["status"] = "SYNC_READBACK_PASS"
        execution["completed_phases"].append("EXACT_READBACK")
        write_json(execution_path, execution)
    except Exception as exc:
        restore_writes = _restore_human_layer_before(spreadsheets, plan, execution["sheet_ids"])
        evidence = {
            "status": "VERIFY_FAILED",
            "mismatch_count": 1,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "restore_executed": True,
            "restore_external_writes": restore_writes,
            "automatic_retry": False,
        }
        execution["status"] = "VERIFY_FAILED"
        execution["restore_executed"] = True
        execution["external_writes"] += restore_writes
        write_json(execution_path, execution)
        write_json(readback_path, evidence)
        raise SyncError(f"human-layer readback failed and before state restored: {exc}") from exc
    write_json(readback_path, evidence)
    print(json.dumps(evidence, ensure_ascii=True))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fail-closed Toplink 24-dataset Sheet correction")
    parser.add_argument("--repo-root")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("compile-datasets").set_defaults(handler=_compile_command)
    subparsers.add_parser("validate-datasets").set_defaults(handler=_validate_command)
    snapshot = subparsers.add_parser("snapshot-target")
    snapshot.add_argument("--metadata-json")
    snapshot.set_defaults(handler=_snapshot_command)
    correction = subparsers.add_parser("build-correction-bundle")
    correction.add_argument("--expires-at-ict", required=True)
    correction.set_defaults(handler=_build_bundle_command)
    recovery = subparsers.add_parser("build-recovery-bundle")
    recovery.add_argument("--expires-at-ict", required=True)
    recovery.set_defaults(handler=_build_recovery_command)
    closure = subparsers.add_parser("build-output-index-closure-bundle")
    closure.add_argument("--expires-at-ict", required=True)
    closure.add_argument("--status-at-ict", required=True)
    closure.set_defaults(handler=_build_output_index_closure_command)
    validate = subparsers.add_parser("validate-approval")
    validate.add_argument("--approval-path", required=True)
    validate.add_argument("--approval-statement", required=True)
    validate.set_defaults(handler=_validate_approval_command)
    execute = subparsers.add_parser("execute-correction")
    execute.add_argument("--approval-path", required=True)
    execute.add_argument("--approval-statement", required=True)
    execute.set_defaults(handler=_execute_command)
    execute_recovery = subparsers.add_parser("execute-recovery")
    execute_recovery.add_argument("--approval-path", required=True)
    execute_recovery.add_argument("--approval-statement", required=True)
    execute_recovery.set_defaults(handler=_execute_recovery_command)
    execute_closure = subparsers.add_parser("execute-output-index-closure")
    execute_closure.add_argument("--approval-path", required=True)
    execute_closure.add_argument("--approval-statement", required=True)
    execute_closure.set_defaults(handler=_execute_output_index_closure_command)
    report_plan = subparsers.add_parser("build-report-plan")
    report_plan.add_argument("--output", default=YV_PLAN_PATH.as_posix())
    report_plan.set_defaults(handler=_build_report_plan_command)
    human_layer = subparsers.add_parser("execute-human-layer")
    human_layer.set_defaults(handler=_execute_human_layer_command)
    verify = subparsers.add_parser("verify-readback")
    verify.set_defaults(handler=_verify_readback_command)
    recovery_snapshot = subparsers.add_parser("snapshot-human-layer-recovery")
    recovery_snapshot.set_defaults(handler=_snapshot_human_layer_recovery_command)
    recovery_execute = subparsers.add_parser("execute-human-layer-recovery")
    recovery_execute.set_defaults(handler=_execute_human_layer_recovery_command)
    recovery_verify = subparsers.add_parser("verify-human-layer-recovery")
    recovery_verify.set_defaults(handler=_verify_human_layer_recovery_command)
    p27_closure = subparsers.add_parser("build-human-layer-ledger-closure")
    p27_closure.set_defaults(handler=_build_human_layer_ledger_closure_command)
    p27_execute = subparsers.add_parser("execute-human-layer-ledger-closure")
    p27_execute.set_defaults(handler=_execute_human_layer_ledger_closure_command)
    p27_verify = subparsers.add_parser("verify-human-layer-ledger-closure")
    p27_verify.set_defaults(handler=_verify_human_layer_ledger_closure_command)
    p28_audit = subparsers.add_parser("audit-human-layer-idempotency")
    p28_audit.set_defaults(handler=_audit_human_layer_idempotency_command)
    p3_verify = subparsers.add_parser("verify-live-state")
    p3_verify.set_defaults(handler=_verify_live_state_command)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.handler(args))
    except SyncError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
