# Quality Checks for Python Automation

## Existing code conventions

- Use standard-library Python and explicit type annotations, as in
  `common/types.py`, `common/paths.py`, and `common/task_context.py`.
- Preserve Windows UTF-8 behavior. `common/__init__.py` configures standard
  streams and platform hooks repeat that protection before handling Vietnamese
  JSON payloads.
- Keep shared state transitions in one owner. For example, active-session
  lookup and mutation live in `common/active_task.py`; commands should call it
  rather than edit pointer files directly.
- Treat task and governance files as data contracts. A structural change to a
  `task.json`, JSONL entry, manifest, or handoff envelope requires an impact
  check across readers, writers, hooks, templates, and docs.

## Minimum verification

For a Python or configuration change, run the narrow affected command and a
repository integrity check:

```powershell
python ./.trellis/scripts/get_context.py
python ./.trellis/scripts/task.py list
git diff --check
```

If a JSON or JSONL contract changed, also run the relevant `task.py validate`
command or a bounded parse/read-back. If a hook changed, test its documented
input/output shape without sending an external mutation.

## Repository-specific review questions

- Does the change preserve UTF-8 and `ensure_ascii=False` for Vietnamese data?
- Does it keep path resolution repository-relative and avoid machine-local
  identifiers?
- Does it preserve task unknown fields and atomic JSON-write behavior?
- Does it respect Toplink's lease, evidence, approval, and cross-brand
  isolation controls?
- Does it touch more than one host hook or generated runtime template? If so,
  inspect every configured counterpart before declaring it complete.
