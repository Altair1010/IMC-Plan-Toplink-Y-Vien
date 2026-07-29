---
name: toplink-imc-delivery
description: Route a Toplink Y Viện IMC workstream from the canonical milestone through DMP, Agency review, human gates, staging, and verification. Use when planning or executing a Toplink audience, positioning, Facebook, content, Reels, KPI, or production deliverable.
---

# Toplink IMC Delivery

## Preflight

Read `STATE.md`, `task.md`, `spec.md`, the current milestone section, and the source ledger from `$toplink-source-grounding`. Confirm the work is in scope and list the required inputs, blocked inputs, output path, and Done gate.

If the canonical milestone is not open or a required input is missing, return `BLOCKED_INPUT` with the minimum human unblock action. Do not simulate completion.

## Route the work

| Workstream | DMP | Review |
|---|---|---|
| Evidence | `import-guidelines`, `brand-setup` | PR Manager |
| Audience/positioning/campaign/KPI | `audience-intelligence`, `campaign-plan` | Social Strategist → Growth Hacker |
| Pillars/copy/calendar | `social-strategy`, `content-engine`, `content-calendar` | Content Creator → PR Manager |
| Reels | `video-script` | Short-Video Coach → TikTok Strategist |
| Safety/workflow | `check`, `status`, `output-folder` | PR Manager → required human gate |

Use no more than three Agency Agents on one workstream. DMP creates a local staging draft only. Capture trace ID, version, active-brand read-back, input/output paths and digests, status, and skipped dimensions.

## Gate promotion

Run `$toplink-communication-safety` on public-facing or health-sensitive material. Collect reviewer findings with evidence, repair, and verdict. Human/professional/legal/privacy approval cannot be self-granted.

For TL-M1 through TL-M5, preserve exactly two macro-runs: Run 1 build/reconciliation then fresh-context Run 2 audit/finalize. Digest, version, or active-brand drift returns the work to Run 1; never create a third run.

## Output

Report the artifact location, provenance status, DMP trace state, reviewer verdicts, open human gates, and whether the result is `STAGING`, `SYNC_PENDING_TARGET`, `VERIFIED`, or `BLOCKED`.
