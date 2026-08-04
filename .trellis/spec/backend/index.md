# Python Automation and Repository-Control Guidelines

> This directory retains Trellis' legacy `backend` name. In this repository it
> governs the Python automation under `.trellis/scripts/` and platform hook
> entry points, not a web API or service.

## Current scope

- Python standard-library automation lives in `.trellis/scripts/` and is called
  from command-line tools or platform hooks.
- The repository has no application server, HTTP routes, database, ORM,
  migration tool, package manifest, or dependency lockfile.
- Operational state is stored locally as UTF-8 Markdown, JSON, or JSONL. It is
  constrained by the Toplink governance documents; it is not a substitute for
  an external system of record.

## Guides

| Guide | Use it when changing |
|---|---|
| [Directory structure](directory-structure.md) | script placement, imports, or platform hooks |
| [Data storage](database-guidelines.md) | JSON, JSONL, task metadata, or file-ledger state |
| [Error handling](error-handling.md) | command failures, optional reads, or hook fallbacks |
| [Logging](logging-guidelines.md) | terminal diagnostics or hook protocol output |
| [Quality](quality-guidelines.md) | any Python automation or generated-runtime change |

Read [the cross-layer guide](../guides/cross-layer-thinking-guide.md) whenever
a script, hook, task artifact, and human workflow must agree on one state.
