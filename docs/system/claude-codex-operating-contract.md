# Claude ↔ Codex operating contract — Toplink Y Viện

## Status and purpose

`ACCEPTED · 2026-07-29`. This is the canonical coordination contract when Claude Code and Codex
CLI work in the same repository. It uses a file ledger instead of a deployed coordination service
and does not grant either runtime human authority.

## Authorities and precedence

1. Current explicit user instruction and platform safety rules prevail.
2. `RULES.md` owns safety and integrity; `GOVERNANCE.md §1` owns permitted scope.
3. `docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md` owns strategy; `TOPLINK_PAGE_MILESTONES.md` owns
   sequence and Done gates.
4. `task.md` owns active work, leases, checkpoints, and handoffs. `STATE.md` is a concise sprint
   view only; `MEMORY.md` stores verified durable lessons.

Conflicting canonical owners stop only the affected mutation. Record both references and request
user direction; a summary or template never silently overrides a canonical owner.

## Default roles

| Runtime | Accountable for | Must not do |
|---|---|---|
| Claude Code | DMP raw authoring, creative/strategy drafts, Agency-review coordination | Run production connectors or self-approve health, legal, privacy, publication, Page, or Sheet actions |
| Codex CLI | Repository plumbing, evidence/status/allowed-use reconciliation, schemas, manifests, QA, bounded automation, and read-back | Invent brand, founder, legal/franchise, product, service, medical, or performance facts; self-approve; take over DMP authoring without handoff |

The role assignment is accountability, not a blanket file lock. One active writer is still
required for each shared file set.

## Two-run contract: TL-M1 through TL-M5

`TL-M1`–`TL-M5` are one package with exactly two macro-runs. A repair remains in its originating
run. A third run is forbidden; any active-brand, DMP-version, profile, source-digest, or scope
mismatch returns the affected work to Run 1.

### `TOPLINK_RUN1_BUILD`

1. Claude acquires the scoped lease, makes required real DMP invocations, saves local staging, and
   coordinates routed Agency reviews.
2. Claude checkpoints exact inputs/digests, outputs, findings, and human gates; then stops writing
   and releases the lease.
3. Codex acquires a new scoped lease as reconciliation owner. It may make evidence-grounded staging
   repairs, validate IDs/schema, run QA, and create the Run 1 manifest.

### `TOPLINK_RUN2_FRESH_AUDIT_FINALIZE`

1. A fresh Claude context performs the required independent/blind audit, DMP check, and fresh
   Agency review before handoff.
2. A fresh Codex context performs its own independent audit before relying on the handoff, records
   the merged issue/repair ledger, then performs evidence-grounded targeted repair.
3. Local canonical promotion is not human `APPROVED`, published, or externally complete. A Sheet
   action remains blocked until its exact target, user approval, and read-back are present.

## Lease and handoff

`task.md → 🔒 Lease` is the only active lock ledger.

1. Before a shared write, add runtime, concrete file set, ICT start time, and purpose.
2. An overlapping writer is a hard stop; read-only work may run in parallel.
3. At each meaningful checkpoint, record paths, digests, verdicts, blockers/human gates, and next
   safe action in `task.md`; mirror only the sprint fact in `STATE.md`.
4. Handoff means stop writing → persist checkpoint → release old lease → next writer acquires a
   new lease. No implicit role change is allowed.
5. On close, preserve only verified reusable lessons in `MEMORY.md`, release the lease, and reset
   `task.md` to its idle template.

Use the templates in `docs/system/templates/`. A recipient rejects any handoff with missing
provenance, an active overlapping lease, a brand/digest mismatch, an unbounded external target,
or an agent-created claim of `APPROVED`.

## Approval tiers

| Tier | Permitted action | Required evidence |
|---|---|---|
| Local safe | Read, inspect, draft local staging, edit non-secret repository docs, run bounded local checks | Scope and lease satisfied |
| Explicit user | Page/Sheet/external-runtime mutation, publishing, messaging, external target change | Exact target, bounded action, user authorization, and read-back where applicable |
| Qualified human/professional | Health, legal, privacy, qualification, testimonial/UGC, or public-claim decision | Named gate and supporting provenance |

No agent grants any tier. `LOCAL_VERIFIED` and an Agency `PASS` never mean `APPROVED`.

## Artifact and isolation boundaries

- Canonical strategy/milestones remain in `docs Toplink/`; reusable protocol/templates remain in
  `docs/system/`; reusable run prompts remain in `docs/prompts/`.
- Create `staging/toplink-reconciled/<run>/` only when a real run starts. It is ignored by Git,
  contains no secrets/unnecessary PII, and remains non-canonical until promotion gates pass.
- The only DMP slug is `toplink-y-vien`. Sheet status remains `BLOCKED_TARGET_INPUT` until the user
  supplies spreadsheet, tab, range, schema, and bounded write approval.
- `docs/system/toplink-google-sheets-operational-contract.md` is the shared Toplink-only registry
  for tab keys, delivery payloads, mapping, validation, and read-back. Claude stages DMP output;
  Codex performs any approved Sheet write and exact read-back.
- Never reuse any Thảo Tây identifier, credential, Sheet, Page, baseline, deliverable, or
  milestone. Never create `_v2` tabs, broad overwrites, a competing plan, or an unsupported
  nationwide, franchise/legal, health, or commercial claim.

## Consequence

The small file-ledger overhead is intentional: it provides auditable ownership and safe recovery
without coupling Toplink to another brand or to a coordination service.
