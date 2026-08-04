# Canonical Reuse Thinking Guide

## Reuse the owner, not a convenient copy

This repository has many documents that summarize, template, or stage the same
work. The safe reuse rule is to locate the canonical owner first:

| Need | Canonical owner | Reusable support only |
|---|---|---|
| Strategy, scope, audience, channel | `docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md` | briefs and local staging |
| Milestone sequence and Done gates | `docs Toplink/TOPLINK_PAGE_MILESTONES.md` | checklists and manifests |
| Safety, source status, external mutations | `RULES.md` | prompts and reviewer outputs |
| Current work, lease, and handoff | `task.md` | `STATE.md` summaries |
| Sheet tab/schema/read-back design | `docs/system/toplink-google-sheets-operational-contract.md` | run output and local mapping |

`docs/system/templates/` contains reusable shapes, not facts. Populate a
template with sourced data; do not copy a prior artifact's brand claims,
external IDs, baseline, or approval status.

## Search before creating or duplicating

- Search for the stable ID, contract name, and owner before adding a document,
  field, or helper. Examples include `TL-M1`, `TL-OUT-*`, `SheetTargetApproval`,
  and the DMP slug `toplink-y-vien`.
- Extend the existing Python owner when an automation function already covers
  the behavior. `common/io.py`, `common/paths.py`, `common/active_task.py`, and
  `common/log.py` are single sources of truth for their respective mechanics.
- Reuse committed prompt and handoff templates instead of creating a second
  format that a recipient cannot validate.

## Copies that are forbidden

- Never import a Thảo Tây Page, Sheet, credentials, external target, analytics
  baseline, deliverable, or milestone into Toplink work.
- Never copy a `LOCAL_VERIFIED`, reviewer `PASS`, or staging result as if it
  were human `APPROVED` or externally delivered.
- Never duplicate a canonical plan into a competing “final” document; link to
  the owner and record only the bounded output needed for the current run.

## Review checklist

- Is there one canonical owner for every decision in the artifact?
- Does every reused field retain its provenance and evidence status?
- Is the new helper or template truly new, rather than a variant of an existing
  project primitive?
- Are stable IDs, source digests, and target boundaries preserved exactly?
