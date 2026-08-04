# Reusable Artifact Components

## No UI component system exists

There are no React, Vue, HTML, CSS, or TypeScript components in this project.
Do not invent prop, styling, or client-accessibility conventions from a generic
frontend template.

The reusable components are structured document sections and templates. Reuse
them by preserving their roles rather than copying a slightly altered version:

| Reusable unit | Source of truth | Required role |
|---|---|---|
| Handoff envelope | `docs/system/templates/handoff-claude-to-codex.template.md` | scope, provenance, reviews, repairs, human gates |
| Machine-readable handoff | `docs/system/templates/handoff-envelope.template.json` | stable transfer fields between runtimes |
| Run manifest | `docs/system/templates/toplink-run-manifest.template.json` | trace, digests, verdicts, blockers |
| Page plan and gates | `docs Toplink/TOPLINK_PAGE_*.md` | canonical decision and milestone ownership |

## Composition rules

- Start from an existing committed template when the artifact role already
  exists. Populate its fields with sourced values; do not create a competing
  structure that omits provenance or human gates.
- Keep the canonical owner's vocabulary and section ordering where readers or
  validators depend on it. For example, the milestone document separates
  Inputs, Work, Deliverables, and VERIFY for each milestone.
- State uncertainty as `MISSING_INPUT`, `UNVERIFIED`, or the appropriate
  status; a polished document layout never turns a gap into a fact.

## Future UI work

If the user later approves a browser UI, create a separate Trellis planning
task first. Establish the framework, directory layout, component contract,
accessibility baseline, and test commands from the implemented code before
adding application-specific component rules here.
