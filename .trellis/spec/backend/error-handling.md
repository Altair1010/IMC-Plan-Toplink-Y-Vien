# Error Handling for Local Automation

## Match the local failure style

Low-level optional reads return a sentinel rather than terminating the process:

- `common.io.read_json()` returns `None` for an absent, invalid, or unreadable
  JSON file.
- `common.paths.get_developer()` returns `None` when `.trellis/.developer` is
  unavailable or malformed.
- Hook code such as `.codex/hooks/session-start.py` keeps optional context
  injection non-fatal so a missing Trellis state cannot block the host session.

Command boundaries then turn known failures into a clear diagnostic and a
non-zero integer return. `task.py` is the reference: validate input early,
print an actionable message, and return `1` or `2`; its module entry calls
`sys.exit(main())`.

## Required handling

- Catch only expected filesystem, decoding, parsing, or subprocess failures at
  the boundary where the fallback is safe. Return the documented sentinel or
  exit code; do not silently continue with fabricated data.
- For a governance conflict, missing evidence, missing approval, bad digest, or
  failed read-back, fail closed. Preserve the blocker and route it to the human
  or canonical owner rather than selecting a convenient value.
- Keep a host hook non-fatal only for optional augmentation. It must not hide a
  failed action that would mutate an external Page, Sheet, publication, or
  runtime.
- Include the affected path, task, or next command in command-line diagnostics
  when that information is non-sensitive.

## Avoid

- Do not use `except Exception: pass` around core state changes or validation.
- Do not convert an error into a successful or `APPROVED` status.
- Do not expose credentials, unnecessary PII, or sensitive health information
  in exceptions or diagnostics.
