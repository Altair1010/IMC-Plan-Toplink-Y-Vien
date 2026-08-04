# Evidence-to-Delivery Flow Guide

## The relevant flow is operational, not browser-to-API

Most high-impact changes cross several owners. Map the complete path before
writing:

```text
Verified source
  → allowed-use and evidence status
  → canonical plan or milestone gate
  → DMP draft / local staging
  → routed review and human gate
  → approved bounded external action
  → exact read-back and checkpoint
```

The flow is defined by `TOPLINK_PAGE_MASTER_PLAN.md`,
`TOPLINK_PAGE_MILESTONES.md`, `RULES.md`, and the Claude–Codex operating
contract. A local file may be valid staging at one arrow and still be blocked
from progressing to the next.

## Boundaries to check

| Boundary | Verify |
|---|---|
| Evidence → claim | provenance, location, status, and permitted use |
| Plan → milestone | scope, dependency, required artifact, and Done gate |
| Claude → Codex | released lease, explicit handoff, paths, digests, verdicts, blockers |
| DMP → deliverable | real invocation trace, active brand read-back, source/output digests |
| Local staging → Sheet/Page | exact user-approved target, bounded action, stable ID, read-back |
| Python script → host hook | input envelope, shared state owner, UTF-8, and clean protocol output |

## Typical failures

- A supporting document rephrases an unverified source as a public fact.
- A reviewer result is shown as a human approval.
- A DMP output has no real invocation trace, or the active profile has drifted.
- A local artifact is called delivered without an approved Sheet target and
  per-tab exact read-back.
- A hook or JSON schema changes in one runtime while its reader, template, or
  platform counterpart remains stale.

## Before and after a cross-layer change

Before: list the canonical owner, input paths/digests, status vocabulary,
affected readers/writers, reviewers, human gates, and whether an external
mutation is in scope.

After: validate the narrow contract, record the verdict and blockers in
`task.md`, update only allowed summaries, run `git diff --check`, and release
the lease. Stop rather than widening a target, creating a fallback Sheet, or
inventing evidence to make the flow appear complete.
