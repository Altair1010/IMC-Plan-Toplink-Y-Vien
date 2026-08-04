from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence


TARGET_SPREADSHEET_ID = "1s-Pm5fIxSfh6znWAWy9QUG4ZXLj0fcO4lC6sRAh8hms"
TARGET_SERVICE_ACCOUNT = "yvien-sheet-writer@imcforyvien.iam.gserviceaccount.com"
REGISTRY_PATH = Path("docs/system/toplink-sheet-dataset-registry.json")
CORRECTION_DIR = Path("docs Toplink/staging/run2/correction")
REPOSITORY_BINDING_PATHS = {
    "registry_sha256": REGISTRY_PATH,
    "run1_manifest_sha256": Path("docs Toplink/staging/run1/run1-manifest.json"),
    "run2_manifest_sha256": Path("docs Toplink/staging/run2/run2-manifest.json"),
    "v2_payload_sha256": Path("docs Toplink/staging/run2/codex/61-sheet-payload-v2.json"),
    "v2_readback_sha256": Path("docs Toplink/staging/run2/codex/63-sheet-readback-v2.json"),
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
    "TL_REPORT",
    "TL_OWNER_ACTIONS",
    "TL_CONTROL",
    "TL_SOURCE_INVENTORY",
    "TL_INPUT_GAPS",
    "TL_OUTPUT_INDEX",
    "TL_DECISIONS",
    "TL_KPI_DICTIONARY",
    "TL_COMPLIANCE_RULES",
    "TL_BRAND_PROFILE",
    "TL_RUNTIME_COMPATIBILITY",
    "TL_PAGE_BENCHMARK",
    "TL_AUDIENCE_HYPOTHESES",
    "TL_POSITIONING",
    "TL_NARRATIVE",
    "TL_CONTENT_PILLARS",
    "TL_FACEBOOK_STRATEGY",
    "TL_CAMPAIGN",
    "TL_EXPERIMENTS",
    "TL_CONTENT_CALENDAR",
    "TL_ASSET_BATCH_PLAN",
    "TL_REELS_BRIEFS",
    "TL_PRODUCTION_BRIEFS",
    "TL_WORKFLOW_APPROVAL",
)
EXISTING_TAB_IDS = {
    "TL_BRAND_PROFILE": 870562582,
    "TL_RUNTIME_COMPATIBILITY": 1414192553,
    "TL_AUDIENCE_HYPOTHESES": 67597104,
    "TL_POSITIONING": 708781861,
    "TL_NARRATIVE": 379404649,
    "TL_CONTENT_PILLARS": 1291995432,
    "TL_FACEBOOK_STRATEGY": 1402539487,
    "TL_CAMPAIGN": 1965931116,
    "TL_KPI_DICTIONARY": 1094283857,
    "TL_CONTENT_CALENDAR": 1711003519,
    "TL_ASSET_BATCH_PLAN": 1923291014,
    "TL_REELS_BRIEFS": 23016754,
    "TL_PRODUCTION_BRIEFS": 1097464105,
    "TL_WORKFLOW_APPROVAL": 1858037963,
}
NEW_TAB_KEYS = tuple(key for key in TAB_KEYS if key not in EXISTING_TAB_IDS)
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
    raw = read_json(repo_root / REGISTRY_PATH)
    common = raw.get("common_columns")
    if common != COMMON_COLUMNS:
        raise SyncError("registry common columns mismatch")
    registry = copy.deepcopy(raw)
    for schema in registry.get("datasets", {}).values():
        schema["columns"] = list(common) + list(schema.get("columns", []))
        schema["foreign_keys"] = copy.deepcopy(registry.get("common_foreign_keys", [])) + list(schema.get("foreign_keys", []))
        schema.setdefault("field_enums", {})
    validate_registry(registry)
    return registry


def validate_registry(registry: dict[str, Any]) -> None:
    datasets = registry.get("datasets")
    if not isinstance(datasets, dict) or set(datasets) != set(TAB_KEYS):
        raise SyncError("registry must contain the exact 24 tab keys")
    for key, schema in datasets.items():
        columns = schema.get("columns", [])
        if len(columns) != len(set(columns)) or columns[: len(COMMON_COLUMNS)] != COMMON_COLUMNS:
            raise SyncError(f"invalid ordered columns: {key}")
        if schema.get("primary_key") not in columns:
            raise SyncError(f"primary key missing from columns: {key}")
        for foreign_key in schema.get("foreign_keys", []):
            target = foreign_key.get("dataset")
            if target not in datasets:
                raise SyncError(f"unknown foreign dataset: {target}")
            if any(column not in columns for column in foreign_key.get("columns", [])):
                raise SyncError(f"foreign key column missing: {key}")
            target_columns = datasets[target].get("columns", [])
            if any(column not in target_columns for column in foreign_key.get("target_columns", [])):
                raise SyncError(f"foreign target column missing: {target}")
        for field, enum_name in schema.get("field_enums", {}).items():
            if field not in columns or enum_name not in registry.get("enums", {}):
                raise SyncError(f"invalid field enum: {key}.{field}")
        for reference in schema.get("external_references", []):
            if reference.get("contract") not in registry.get("external_reference_contracts", {}):
                raise SyncError(f"unknown external reference contract: {key}")
            if any(column not in columns for column in reference.get("columns", [])):
                raise SyncError(f"external reference column missing: {key}")


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
    return options if len(options) == 3 else [("A", value), ("B", value), ("C", value)]


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
    for title, sheet_id in EXISTING_TAB_IDS.items():
        if sheets.get(title, {}).get("sheet_id") != sheet_id:
            raise SyncError(f"existing sheet ID drift: {title}")
    validate_create_actions(NEW_TAB_KEYS, set(sheets))
    actions: list[dict[str, Any]] = []
    creates = [{"tab_key": title, "action": "CREATE_TAB"} for title in NEW_TAB_KEYS]
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
        actions.append({"tab_key": key, "action": "REPLACE_RANGE", "sheet_id": EXISTING_TAB_IDS.get(key), "old_used_range": old_range, "new_used_range": new_range, "approved_new_used_range": new_range, "clear_range": ranges["clear_range"], "max_rows": rows, "max_columns": columns, "dataset_sha256": payload["dataset_sha256"], "formatting": copy.deepcopy(registry["formatting"]), "validations": validations, "date_columns": [index for index, field in enumerate(payload["columns"]) if field.endswith("_at_ict")]})
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
                color_ok = all(abs(float(background.get(name, -1)) - value) < 0.001 for name, value in (("red", 0.4196), ("green", 0.1216), ("blue", 0.2118)))
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
            "digest": sha256_v2_values(actual.get("values", [])),
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
        for title, sheet_id in EXISTING_TAB_IDS.items():
            if by_title.get(title, {}).get("sheet_id") != sheet_id:
                raise SyncError(f"existing sheet ID drift after CREATE_TAB: {title}")
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
        if sha256_v2_values(returned[-1].get("values", [])) != preserved_sheet["baseline_digest"]:
            raise SyncError("Trang tính1 post-write drift")
        return {"record_id": "TL-SHEET-RUN2-CORRECTION-READBACK-01", "status": "SYNC_READBACK_PASS", "spreadsheet_id": TARGET_SPREADSHEET_ID, "tabs": evidence_tabs, "tab_count": len(evidence_tabs), "mismatch_count": 0, "preserved_trang_tinh1_sheet_id": by_title.get("Trang tính1", {}).get("sheet_id"), "automatic_rollback": False}

    return guarded_post_mutation(verify_post_write)


def _repo_root(value: str | None) -> Path:
    return Path(value).resolve() if value else Path(__file__).resolve().parents[2]


def _compile_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    bundle = compile_datasets(repo_root)
    output = repo_root / CORRECTION_DIR
    write_json(output / "dataset-bundle.json", bundle)
    write_dataset_sidecars(bundle, output / "datasets")
    print(json.dumps({"status": "PASS", "datasets": 24, "bundle_sha256": bundle["bundle_sha256"]}, ensure_ascii=False))
    return 0


def _validate_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    bundle = read_json(repo_root / CORRECTION_DIR / "dataset-bundle.json")
    registry = load_registry(repo_root)
    validate_dataset_bundle(bundle, registry)
    validate_source_digests(bundle, repo_root)
    validate_dataset_sidecars(bundle, repo_root / CORRECTION_DIR / "datasets")
    print(json.dumps({"status": "PASS", "datasets": 24}, ensure_ascii=False))
    return 0


def _snapshot_command(args: argparse.Namespace) -> int:
    repo_root = _repo_root(args.repo_root)
    if args.metadata_json:
        metadata = read_json(Path(args.metadata_json))
    else:
        service = _google_service(TARGET_SERVICE_ACCOUNT)
        metadata = service.spreadsheets().get(spreadsheetId=TARGET_SPREADSHEET_ID, fields="sheets.properties").execute()
    snapshot = _snapshot_from_metadata(metadata)
    write_json(repo_root / CORRECTION_DIR / "target-snapshot.json", snapshot)
    print(json.dumps({"status": "PASS", "sheet_count": len(snapshot["sheets"])}, ensure_ascii=False))
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


def _verify_readback_command(args: argparse.Namespace) -> int:
    evidence = read_json(Path(args.readback_path))
    if evidence.get("status") != "SYNC_READBACK_PASS" or evidence.get("tab_count") != 24 or evidence.get("mismatch_count") != 0 or evidence.get("preserved_trang_tinh1_sheet_id") != 0:
        raise SyncError("correction readback verification failed")
    print(json.dumps({"status": "PASS", "tab_count": 24}))
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
    validate = subparsers.add_parser("validate-approval")
    validate.add_argument("--approval-path", required=True)
    validate.add_argument("--approval-statement", required=True)
    validate.set_defaults(handler=_validate_approval_command)
    execute = subparsers.add_parser("execute-correction")
    execute.add_argument("--approval-path", required=True)
    execute.add_argument("--approval-statement", required=True)
    execute.set_defaults(handler=_execute_command)
    verify = subparsers.add_parser("verify-readback")
    verify.add_argument("--readback-path", required=True)
    verify.set_defaults(handler=_verify_readback_command)
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
