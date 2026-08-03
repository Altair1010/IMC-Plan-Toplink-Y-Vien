# Design — Systematic multi-agent collaboration contract

## 1. Artifact Boundary

The implementation creates one standalone Markdown document:

`SYSTEMATIC_MULTI_AGENT_COLLABORATION_CONTRACT.md`

The document is a protocol specification. It does not import or link to the source repository and
does not require a companion application. All schemas and templates required for conformance are
embedded in the file.

## 2. Design Principles

1. **File-ledger first:** the minimum viable coordination mechanism is a human-readable ledger plus
   machine-readable envelopes. A service may be added later as an adapter.
2. **Accountability before tool identity:** roles are defined as Authoring Runtime and Control
   Runtime, with Claude/Codex provided only as default labels.
3. **Single writer per scope:** concurrency is allowed only where write scopes do not overlap.
4. **Evidence before state promotion:** no state transition occurs without its required evidence.
5. **Handoff transfers custody, not authority:** a handoff cannot grant approval or expand scope.
6. **Independent verification:** a fresh audit must not merely restate the preceding run.
7. **Fail closed:** uncertainty, conflict, drift, partial writes, and missing approval stop affected
   actions without silently broadening permissions.
8. **Portable core, replaceable adapters:** storage layout, version control, reviewers, automation,
   and external systems are configurable; invariants are not.

## 3. Logical Architecture

```text
Policy layer
  ├─ authority and precedence
  ├─ approval tiers
  └─ immutable invariants
          ↓
Coordination layer
  ├─ work ledger
  ├─ scoped leases
  ├─ checkpoints
  └─ handoff envelopes
          ↓
Execution layer
  ├─ milestone records
  ├─ Run 1 build/reconciliation
  └─ Run 2 independent audit/finalization
          ↓
Evidence layer
  ├─ stable IDs and digests
  ├─ issue/decision/approval ledgers
  ├─ run manifests
  └─ verification/read-back records
          ↓
Adapter layer
  ├─ filesystem or database
  ├─ version control or document history
  ├─ reviewer mechanism
  └─ external systems/connectors
```

## 4. Normative Model

The document uses RFC-style capitalized terms:

- `MUST` / `MUST NOT`: protocol invariant.
- `SHOULD` / `SHOULD NOT`: default required unless an explicit, recorded exception exists.
- `MAY`: optional behavior.

Every rule is either:

- **Invariant:** cannot be customized without creating a different protocol; or
- **Policy:** may be customized if the chosen value is explicit and preserves all invariants.

## 5. Required State Machines

### Work item

`PROPOSED → PLANNED → READY → IN_PROGRESS → VERIFYING → COMPLETE`

Alternative terminal or holding states:
`BLOCKED`, `CANCELLED`, `SUPERSEDED`.

### Lease

`ABSENT → REQUESTED → ACTIVE → CHECKPOINTED → RELEASED`

Exceptional transitions:
`ACTIVE → EXPIRED`, `ACTIVE → ABANDONED`, followed by a governed recovery procedure.

### Handoff

`DRAFT → SEALED → OFFERED → VALIDATING → ACCEPTED | REJECTED`

Custody transfers only on `ACCEPTED`.

### Artifact

`PLANNED → GENERATED → REVIEWED → LOCALLY_VERIFIED → PROMOTION_READY → PROMOTED`

An external-delivery branch adds:
`SYNC_READY → WRITTEN_UNVERIFIED → READBACK_PASS`.

### Run package

`RUN1_READY → RUN1_AUTHORING → RUN1_RECONCILING → RUN1_PASS → RUN2_BLIND_AUDIT
→ RUN2_FINALIZING → PACKAGE_PASS`.

Drift transitions to `RESET_TO_RUN1`; a third macro-run is invalid.

## 6. Contract Sections

The final document will contain:

1. Document control and intended use.
2. Normative language and glossary.
3. Immutable invariants.
4. Configurable policy surface.
5. Authority and precedence.
6. Role model and capability matrix.
7. Scope decomposition and stable identity.
8. Work ledger and lease protocol.
9. Checkpoint protocol.
10. Handoff protocol and templates.
11. Milestone specification schema.
12. Systematic end-to-end logic flow.
13. Run 1 contract.
14. Run 2 contract.
15. Review and issue reconciliation.
16. Approval tiers and human gates.
17. Artifact promotion and external mutation.
18. Manifest and evidence schemas.
19. Failure, interruption, and recovery.
20. Concurrency and multi-agent scaling.
21. Storage/versioning adapters.
22. Customization procedure.
23. Conformance tests and acceptance checklist.
24. Anti-patterns and invalid examples.
25. Worked neutral example.
26. Change-control policy.

## 7. Data Contracts

Embedded JSON-compatible schemas will be examples rather than JSON Schema dependencies. Required
records:

- `LeaseRecord`
- `CheckpointRecord`
- `HandoffEnvelope`
- `MilestoneRecord`
- `IssueRecord`
- `DecisionRecord`
- `ApprovalRecord`
- `ExternalWriteRecord`
- `RunManifest`

Each record includes a version, stable ID, timestamps, actor identity, scope, status, and evidence
references where applicable.

## 8. Portability Strategy

The specification uses logical names:

- `<CONTROL_ROOT>`
- `<WORK_LEDGER>`
- `<ARTIFACT_STORE>`
- `<RUN_ID>`
- `<MILESTONE_ID>`
- `<RUNTIME_ID>`
- `<EXTERNAL_TARGET>`

No physical directory is mandatory. A suggested file layout is labeled as an optional adapter, not
as protocol truth.

## 9. Trade-offs

- A file-ledger protocol is easier to adopt and audit than a coordination service but relies on
  disciplined atomic updates.
- Two independent runs increase cost but reduce correlated self-review errors.
- Digests improve custody and drift detection but require stable canonicalization rules.
- Strong approval separation slows external actions but prevents AI-generated authority.
- A large standalone document is less concise but satisfies the requirement that recipients need
  no repository context.

## 10. Compatibility and Migration

Adopters may map existing task trackers, lock services, review systems, or CI artifacts to the
logical contracts. Migration is conformant only if required fields and transition gates remain
observable. Existing project terms should be translated through a mapping table rather than copied
into the protocol core.

## 11. Rollback

The new file is additive. Rollback consists of removing only
`SYSTEMATIC_MULTI_AGENT_COLLABORATION_CONTRACT.md` and the task planning artifacts if explicitly
requested. Existing source contracts remain untouched.
