# Terminal and Hook Output

## CLI scripts

Use the single terminal-formatting owner in `common/log.py`:

- `colored()` and `Colors` for concise human-facing status output.
- `log_info`, `log_success`, `log_warn`, and `log_error` for consistent
  prefixed diagnostics when a command needs level-like messaging.
- Machine-readable modes must write clean JSON with `ensure_ascii=False`, as
  `task.py current --json` does. Do not prepend prose or ANSI sequences.

Status output should identify the operation and next safe action. Examples in
`task.py` report an absent task, a stale branch, or a failed context-file
validation without printing the full task contents.

## Hooks

Platform hooks have protocol-owned stdout. `.codex/hooks/session-start.py`
emits one JSON object for `hookSpecificOutput`; debug print statements on stdout
would corrupt that response. During a hook change, send optional diagnostics to
stderr only if the host contract permits it, or omit them.

## Safety

- Never log secrets, credentials, full health information, private contact
  data, or an unapproved external identifier.
- Logs do not replace the checkpoint required in `task.md`; record durable
  paths, verdicts, and blockers in the ledger.
- A success-colored message must describe a completed local operation, never
  imply publication, external sync, or human approval.
