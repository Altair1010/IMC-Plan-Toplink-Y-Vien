# User-Facing Artifact and Host-Interface Guidelines

> This directory retains Trellis' legacy `frontend` name. The repository has
> no browser application, component library, TypeScript project, or client-side
> state store. These guides define the actual user-facing boundaries: Markdown
> artifacts, platform hook interfaces, and generated prompt/context output.

## Current scope

- Toplink's user-facing work is authored as evidence-grounded Markdown under
  `docs Toplink/`, `docs/`, and local `staging/` runs; it is not a web UI.
- `.codex/`, `.claude/`, and `.cursor/` contain host-specific hook adapters,
  not React hooks or browser code.
- Do not introduce a frontend framework, package manager, component convention,
  or accessibility checklist until the user authorizes an actual product UI and
  the project has a design and toolchain for it.

## Guides

| Guide | Use it when changing |
|---|---|
| [Artifact structure](directory-structure.md) | public-facing documents, prompts, templates, or host adapters |
| [Components](component-guidelines.md) | reusable document/template sections or a future UI proposal |
| [Hooks](hook-guidelines.md) | Codex, Claude, or Cursor event handlers |
| [State](state-management.md) | reader-facing status, task context, or generated prompt state |
| [Contracts](type-safety.md) | JSON, JSONL, handoff, and status-vocabulary shapes |
| [Quality](quality-guidelines.md) | document rendering, host protocol, or future UI review |

For the end-to-end artifact flow, read
[the cross-layer guide](../guides/cross-layer-thinking-guide.md).
