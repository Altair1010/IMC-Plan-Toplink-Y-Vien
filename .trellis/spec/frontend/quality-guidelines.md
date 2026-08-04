# User-Facing Artifact Quality

## What quality means here

The current UI surface is documentation and host-generated context, not a web
page. Review artifacts for canonical ownership, evidence, safety, privacy,
and protocol correctness before visual polish.

## Required checks

- Read the governing source before drafting: `AGENTS.md`, `STATE.md`,
  `RULES.md`, `task.md`, `GOVERNANCE.md`, and the relevant canonical Toplink
  plan or milestone.
- Verify every material statement has an appropriate source and evidence status.
  Do not write unsupported brand, medical, legal, availability, pricing, or
  performance claims.
- Verify the destination state: local staging is not a Page mutation, Sheet
  sync, publication, or human approval. External actions require the exact
  approved target and read-back.
- Preserve Vietnamese UTF-8 and exact stable IDs in Markdown, JSON, and hook
  responses.
- Before close, inspect the changed scope and run `git diff --check`.

## Future browser UI

There is no local lint, build, visual-regression, or accessibility test command
because there is no UI implementation. When a UI is approved, add its actual
toolchain and tests in the same task that introduces the code; do not claim
that a generic frontend checklist has been executed.
