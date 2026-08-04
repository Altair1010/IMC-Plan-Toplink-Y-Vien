# Host Event-Hook Guidelines

## Scope

The word “hook” in this repository means an AI-host lifecycle adapter, not a
React hook. Current examples are:

- `.codex/hooks/session-start.py`
- `.codex/hooks/inject-workflow-state.py`
- `.codex/hooks/inject-subagent-context.py`
- their configured counterparts under `.claude/hooks/` and `.cursor/hooks/`

## Pattern

- Decode the host JSON input defensively, locate the repository, and delegate
  task/session resolution to `.trellis/scripts/common`.
- Make optional context injection best-effort. A hook may omit supplemental
  context when no valid session/task state exists; it must not prevent the host
  from starting.
- Emit only the response envelope required by that host on stdout. The Codex
  session-start hook emits `hookSpecificOutput` with a `SessionStart` event.
- Preserve UTF-8 protections before reading or writing non-ASCII payloads. The
  Codex hook explicitly reconfigures Windows standard streams.
- Keep host-specific payload parsing at the adapter boundary. Do not pull
  Claude, Cursor, or Codex wire formats into `common/`.

## Change checklist

1. Identify the host event and expected JSON response before editing.
2. Inspect every equivalent configured host adapter for the same semantic
   behavior.
3. Test a valid input, missing task/session state, malformed optional input,
   and Vietnamese text.
4. Confirm no debug output corrupts stdout and no hook writes an external
   target.

## Avoid

- Do not add client-side data fetching, browser state, or a `use*` function:
  none belongs to the current repository.
- Do not make hook success depend on an unavailable Page, Sheet, network, or
  unapproved external integration.
