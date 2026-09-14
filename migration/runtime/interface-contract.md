# KTD Workbook Runtime Interface Contract

## Boundary

The new runtime is additive and isolated. It does not modify or import the legacy
`toplink_sheet_sync.py` or `yv_build_report_plan.py` implementation.

## Public functions

- `build_workbook_plan()` returns a deterministic dictionary containing exactly four human
  sheets and one machine sheet. Human cells are Vietnamese; machine bindings remain internal.
- `validate_workbook_plan(plan)` returns a list of stable error codes. An empty list means
  the static workbook contract passes.
- `resolve_node(plan, machine_node)` returns exactly one binding or raises a validation error.
- `machine_write_allowed(plan, machine_node)` returns `False` for human canonical objects and
  `True` only for explicitly `MACHINE_DERIVED` objects.
- `build_runtime_context(plan)` returns only the active KTD communication context and excludes
  archive-only legacy governance.

External Sheet responses are untrusted input and must be validated against the plan before
promotion. No function reads credentials or performs network writes.
