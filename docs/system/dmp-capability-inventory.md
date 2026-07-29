# Digital Marketing Pro capability inventory

## Runtime status

- Expected plugin: Digital Marketing Pro v3.15.1.
- Required active brand slug: `toplink-y-vien`.
- DMP is a shared runtime/plugin, not a repository folder to copy.
- This repository records its capability contract and validates the runtime before real execution.

## Approved capability map

| Group | Capabilities |
|---|---|
| Foundation | `brand-setup`, `import-guidelines`, `switch-brand` |
| Strategy | `audience-intelligence`, `competitor-analysis`, `social-strategy`, `campaign-plan` |
| Content | `content-engine`, `content-calendar`, `video-script` |
| Operations and QA | `check`, `status`, `doctor`, `integrations`, `output-folder`, `resume`, `engagement` |

## Invocation guard

Before a deliverable-producing run, verify DMP version, switch/read back the active brand, lock
profile/source digests, and write only local staging. A trace is mandatory. A missing connector
or Sheets target is a blocker, never a reason to improvise an external destination.
