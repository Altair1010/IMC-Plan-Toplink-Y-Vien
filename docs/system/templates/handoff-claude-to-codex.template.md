# Handoff — Claude → Codex

## Envelope

- **Run/stage:** `<TOPLINK_RUN1_BUILD | TOPLINK_RUN2_FRESH_AUDIT_FINALIZE>`
- **Prepared by / timestamp (ICT):** `<runtime · ISO-8601>`
- **Recipient:** `Codex CLI`
- **Lease:** `<released row or BLOCKED>`
- **Read timing:** `<before independent audit | after independent audit>`

## Scope and provenance

- **Canonical inputs:** `<relative paths>`
- **DMP trace:** `<trace ID · DMP version · active-brand read-back>`
- **Input/profile digest:** `<SHA-256 or NOT_AVAILABLE>`
- **Output paths/digests:** `<relative paths and SHA-256>`
- **Stable IDs affected:** `<IDs or none>`
- **Sheet delivery plan:** `<TL-SHEET-001 tab key(s), local/sync state, or BLOCKED_TARGET_INPUT>`

## Reviewer and check results

| Reviewer/check | Verdict | Evidence/location | Required repair or gate |
|---|---|---|---|
| `<name>` | `<PASS | FAIL | NEEDS_HUMAN_REVIEW | SKIPPED>` | `<path/section>` | `<action>` |

## Issue and repair ledger

| ID | Severity | Classification | Evidence | Allowed repair route | Status |
|---|---|---|---|---|---|
| `<TL-ISSUE-NNN>` | `<minor/major/critical>` | `<evidence/schema/claim/runtime>` | `<path/section>` | `<DIRECT_REPAIR | DMP_SKILL_REAUTHOR | HUMAN_GATE>` | `<open/resolved>` |

## Human gates, recipient constraints, and release

- **Human gate/blocker:** `<owner, decision needed, and why it cannot be self-approved>`
- **Allowed next action:** `<bounded action>`
- **Forbidden:** `<external mutation, claim, target, or scope boundary>`
- **Stop if:** `<brand/digest/lease/evidence conflict>`

I stopped writing the leased file set, persisted this handoff, and released the lease above. This
handoff does not grant human approval.
