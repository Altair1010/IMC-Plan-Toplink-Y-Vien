# File-Backed State and Data Contracts

## No database layer exists

This repository has no database, ORM, query builder, migration system, or
server-side persistence service. Do not add database guidance, schemas, or
migrations by analogy to a web application.

The existing persistence forms are deliberately small and local:

| Data | Owner and format | Reference |
|---|---|---|
| Trellis task metadata | `.trellis/tasks/*/task.json` | `common/types.py`, `common/task_store.py` |
| Curated task context | `implement.jsonl` / `check.jsonl` | `common/task_context.py` |
| Local workflow state | UTF-8 Markdown ledgers | `STATE.md`, `task.md`, `MEMORY.md` |
| External-delivery contract | JSON-shaped records in a Markdown contract | `docs/system/toplink-google-sheets-operational-contract.md` |

## JSON and JSONL rules

- Use `common.io.read_json()` for tolerant reads and `common.io.write_json()`
  for writes to task metadata. `write_json()` writes a same-directory temporary
  file and replaces the target atomically; do not open `task.json` directly for
  overwrite.
- `TaskData` in `common/types.py` is a read-path type aid. When changing an
  existing task, preserve the original dictionary and unknown fields, as
  `TaskInfo.raw` documents.
- JSONL is append-oriented context metadata. `common/task_context.py` treats a
  row without a `file` field as a seed/comment row; do not reinterpret it as a
  real context item.
- Use UTF-8 and `ensure_ascii=False`, as the shared I/O code does. Vietnamese
  content and stable identifiers must survive a full write/read-back unchanged.

## Governance ledger rules

`task.md` is the live lease ledger; `STATE.md` is the short sprint view; and
`MEMORY.md` stores only durable verified lessons. Do not use a local JSON file
to bypass their ownership or invent an external target. The Google Sheets
contract remains `BLOCKED_TARGET_INPUT` until the explicit approval payload is
present.

## Avoid

- Do not introduce an ORM, migration directory, or fake database schema.
- Do not overwrite a broad Markdown or JSON file to update one record when the
  documented operation is a bounded lease, append, or stable-identity upsert.
- Do not turn missing source facts into default values in a persisted record;
  retain `MISSING_INPUT`, `UNVERIFIED`, or the applicable blocked state.
