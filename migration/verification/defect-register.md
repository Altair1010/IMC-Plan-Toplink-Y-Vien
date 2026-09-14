# Defect and Repair Register

## KTD-DEF-001 — UTF-8 CLI output

- Observed failure: Windows CP1252 could not emit the Vietnamese JSON plan.
- Earliest broken edge: CLI serialization transport, before any Sheet write.
- Minimal repair: reconfigure stdout to UTF-8 in the CLI entry point.
- Retest: exact plan emission, Sheet write, and full range readback passed.
- Convergence: PROGRESSING.

## KTD-DEF-002 — Legacy approval-expiry tests

- Observed failure: four of 72 repository tests error because historical signed approvals are
  expired or missing on the current date.
- Earliest broken edge: time-bound legacy approval fixtures, not the active KTD runtime.
- Discriminating evidence: the failures name only `CREATE_TAB`, recovery, P2.7, and P3 legacy
  approvals; `git diff --name-only` shows no changes to legacy runtime or fixtures.
- Disposition: accepted non-blocking legacy-reference failure. Repairing or renewing the
  approvals would resurrect obsolete governance and is outside the active route.
- Retest: the isolated KTD suite passes; all other 68 repository tests pass.
- Convergence: PROGRESSING.
