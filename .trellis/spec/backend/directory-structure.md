# Python Automation Structure

## Place code by responsibility

The project keeps reusable Trellis mechanics separate from thin command and
platform adapters:

```text
.trellis/scripts/
  get_context.py, task.py, init_developer.py  # executable CLI entry points
  common/                                     # shared paths, state, config, I/O
  hooks/                                      # optional external-workflow adapters
.codex/hooks/, .claude/hooks/, .cursor/hooks/ # host-specific hook entry points
```

`task.py` delegates task creation, context validation, and task storage to
`common/task_store.py` and `common/task_context.py`; new command behavior
should follow that split instead of collecting domain logic in the CLI parser.

## Import and path rules

- Start reusable scripts with `from __future__ import annotations`, matching
  `.trellis/scripts/task.py` and `common/io.py`.
- Resolve repository-relative locations with `common.paths.get_repo_root()` and
  the named constants in `common/paths.py`. Do not derive paths from the
  current shell directory or hard-code a developer's home directory.
- Use `pathlib.Path` at filesystem boundaries. `common.paths.normalize_task_ref`
  converts stored task references to portable POSIX-style paths; preserve that
  convention for new persisted references.
- Put behavior shared by more than one command or hook in `common/`. Keep a
  platform hook limited to decoding that host's payload, calling shared logic,
  and emitting the host's required response.

## Platform-hook boundary

`.codex/hooks/session-start.py` imports `.trellis/scripts/common` only after it
has located the repository. Its equivalent hooks under `.claude/` and `.cursor/`
are separate host adapters. A change to shared workflow semantics must identify
every configured host affected; do not copy a Codex-specific JSON envelope into
another host without checking that host's hook contract.

## Avoid

- Do not create `src/routes`, controllers, services, or an API layer: none
  exists in this repository.
- Do not place business/Toplink strategy decisions in Python helpers. Canonical
  decisions belong in `docs Toplink/`, with enforcement rules in the repository
  control documents.
- Do not duplicate `common` constants, JSON I/O, task-reference normalization,
  or encoding setup in a command script.
