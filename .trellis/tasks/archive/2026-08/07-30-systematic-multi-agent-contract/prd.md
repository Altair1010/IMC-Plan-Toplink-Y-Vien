# Systematic multi-agent collaboration contract

## Goal

Create one portable Markdown specification that any team can copy, customize, and use to coordinate
Claude Code, Codex CLI, or equivalent authoring/control runtimes through deterministic roles,
scoped write leases, evidence-bearing handoffs, milestone gates, independent audit runs, approvals,
manifests, external-write verification, and recovery rules.

## Requirements

### Functional requirements

- `REQ-001` — Produce exactly one distributable file:
  `SYSTEMATIC_MULTI_AGENT_COLLABORATION_CONTRACT.md`.
- `REQ-002` — The document must be a normative contract, not an overview, summary, marketing
  explanation, or repository walkthrough.
- `REQ-003` — Define RFC-style normative terms (`MUST`, `MUST NOT`, `SHOULD`, `MAY`) and a clear
  authority/precedence model.
- `REQ-004` — Define runtime roles by accountability and capability rather than by unrestricted
  filesystem ownership. The default two-role model must cover an authoring runtime and a
  control/reconciliation runtime while allowing renamed or additional runtimes.
- `REQ-005` — Specify a single-writer scoped lease protocol with acquisition, conflict detection,
  checkpointing, renewal/expiry policy, release, abandoned-lease recovery, and hard-stop rules.
- `REQ-006` — Specify a complete handoff protocol including Markdown and JSON-compatible field
  contracts, provenance, digests, issue ledger, human gates, allowed/forbidden actions, acceptance,
  rejection, and custody transfer.
- `REQ-007` — Define a systematic logic flow from intake through authority resolution, planning,
  execution, review, independent audit, promotion, external mutation, read-back, and closeout.
- `REQ-008` — Define reusable milestone records: identity, owner, dependencies, inputs, work,
  outputs, reviewers, verification, approval tier, status, blockers, and Done gates.
- `REQ-009` — Define a two-run control pattern: Run 1 build/reconciliation and fresh-context Run 2
  independent audit/finalization. State when a reset to Run 1 is required and forbid ambiguous
  “Run 3” continuation.
- `REQ-010` — Define state machines for work items, leases, artifacts, handoffs, approvals,
  external writes, and milestone completion.
- `REQ-011` — Define manifest, stable-identity, digest, issue, decision, approval, and read-back
  schemas with copyable examples.
- `REQ-012` — Define failure handling, stop conditions, repeated-failure policy, partial-write
  recovery, scope drift, conflicting authority, digest drift, stale context, and interrupted
  handoffs.
- `REQ-013` — Define concurrency rules distinguishing parallel read-only work, independent
  non-overlapping writes, and prohibited overlapping writes.
- `REQ-014` — Define human-approval tiers and make explicit that no AI runtime or automated reviewer
  may self-grant human, legal, safety, privacy, publication, financial, or production approval.
- `REQ-015` — Define how bounded external mutations are approved, executed, and verified through
  exact read-back; acknowledgment alone must not constitute success.
- `REQ-016` — Include a customization procedure and conformance checklist that tells adopters which
  placeholders, roles, statuses, files, authorities, risk domains, and gates to adapt.
- `REQ-017` — Include anti-patterns and invalid examples, not only the happy path.

### Portability and exclusion requirements

- `REQ-018` — Remove all project names, brand names, campaign details, health claims, geographic
  details, product facts, and project-specific identifiers.
- `REQ-019` — Remove all references to skills, plugins, marketplaces, MCP servers, installed tools,
  agent catalogs, or platform-specific extension systems.
- `REQ-020` — Remove all dependencies on the current repository, its canonical files, its directory
  tree, its brand slug, its milestones, its external targets, and its staging paths.
- `REQ-021` — Do not require Git, a particular CI system, Google Sheets, a particular programming
  language, or a particular filesystem layout. Such mechanisms may appear only as clearly labeled
  adapter examples.
- `REQ-022` — Use placeholders and logical artifact names so the contract remains directly
  customizable without editing its control logic.

### Presentation requirements

- `REQ-023` — Write the specification in Vietnamese while preserving concise standard technical
  tokens where they improve interoperability.
- `REQ-024` — Use systematic sections, normative rules, state diagrams, tables, and fenced
  templates. Avoid conversational commentary.
- `REQ-025` — Make the document self-contained: a recipient must not need this repository or prior
  conversation to implement the protocol.
- `REQ-026` — Include a version block, status, intended audience, assumptions, glossary, and change
  control rules.
- `REQ-027` — Distinguish immutable protocol invariants from configurable policy.

## Acceptance Criteria

- [ ] `AC-001` — Exactly one new distributable Markdown contract exists at the agreed output path.
- [ ] `AC-002` — A case-insensitive search finds no project-specific brand, repository, skill,
  plugin, marketplace, campaign, external-target, or legacy identifier from the source scaffold.
- [ ] `AC-003` — The file contains complete normative sections for authority, roles, leases,
  handoffs, runs, milestones, approvals, manifests, external writes, failures, customization, and
  conformance.
- [ ] `AC-004` — Every state machine defines states, allowed transitions, forbidden transitions,
  entry evidence, and terminal conditions.
- [ ] `AC-005` — Lease and handoff templates are copyable and contain all mandatory fields.
- [ ] `AC-006` — Run 1 and Run 2 assign explicit responsibilities to authoring and control runtimes,
  with a fresh-context audit rule and deterministic fallback.
- [ ] `AC-007` — The milestone schema is generic and includes at least one fully worked neutral
  example.
- [ ] `AC-008` — External mutation requires an exact target, bounded action, approval evidence,
  verification plan, and exact read-back result.
- [ ] `AC-009` — The customization chapter enables renaming runtimes and replacing storage,
  automation, review, and external-system adapters without weakening invariants.
- [ ] `AC-010` — Markdown structure and fenced JSON examples are syntactically well formed.
- [ ] `AC-011` — A final terminology and leakage scan passes.
- [ ] `AC-012` — No existing project contract is modified or superseded by the generic document.

## Out of Scope

- Implementing a lease service, database, connector, bot, CI pipeline, or runtime integration.
- Replacing the source project's existing operating contract.
- Creating platform-specific installation instructions.
- Defining domain-specific safety or legal policy for a particular industry.
- Automatically migrating an adopter's existing workflow.

## Confirmed Decisions

- The deliverable is one detailed Markdown file.
- The content is a reusable formal specification rather than a summary.
- The source scaffold is used only as design evidence; project-specific nouns and mechanisms are
  excluded from the deliverable.
- The protocol retains a default Claude/Codex mapping but defines generic authoring/control roles
  so adopters may rename or replace the runtimes.
- No blocking product, scope, compatibility, or risk decision remains.
