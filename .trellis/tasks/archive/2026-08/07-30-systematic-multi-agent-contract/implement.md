# Implementation Plan — Systematic multi-agent collaboration contract

## 1. Preconditions

- [ ] User approves the final planning summary in a subsequent message.
- [ ] Start the Trellis task and enter Phase 2.
- [ ] Load the repository's before-edit guidance.
- [ ] Replace the planning-only lease with an implementation lease covering the single output file.

## 2. Author the Contract

- [ ] Create `SYSTEMATIC_MULTI_AGENT_COLLABORATION_CONTRACT.md`.
- [ ] Add document control, audience, assumptions, normative language, and glossary.
- [ ] Define invariants and configurable policies.
- [ ] Define authority, precedence, role accountability, capability boundaries, and separation of
      duties.
- [ ] Define stable identity, scope boundaries, work ledger, leases, checkpoints, and handoffs.
- [ ] Add all required state machines with entry evidence, allowed transitions, forbidden
      transitions, and terminal conditions.
- [ ] Add milestone, run, review, issue, decision, approval, manifest, and external-write contracts.
- [ ] Add Run 1 and fresh-context Run 2 logic with deterministic reset behavior.
- [ ] Add external mutation approval, bounded execution, exact read-back, and partial-failure rules.
- [ ] Add interruption, stale-context, abandoned-lease, conflicting-authority, and repeated-failure
      recovery.
- [ ] Add customization steps, adapter guidance, anti-patterns, conformance tests, and a neutral
      worked example.

## 3. Content Isolation Checks

- [ ] Search for every known project/brand/runtime-extension term prohibited by `REQ-018`–`REQ-021`.
- [ ] Verify the document contains no source-repository paths or instructions that require a
      particular repository layout.
- [ ] Verify Claude/Codex names appear only as replaceable default runtime labels, never as required
      platform dependencies.
- [ ] Verify no skill, plugin, marketplace, connector catalog, or extension-system reference remains.

## 4. Structural Validation

- [ ] Check heading hierarchy and Markdown fence balance.
- [ ] Parse all JSON code blocks as JSON after substituting valid placeholder values or validate
      their documented pseudo-JSON status.
- [ ] Confirm every state mentioned in transitions is defined.
- [ ] Confirm every required record field is explained.
- [ ] Confirm every approval-sensitive transition identifies the necessary authority.
- [ ] Confirm the worked example exercises intake, lease, handoff, both runs, approval, and closeout.

## 5. Requirement Traceability

- [ ] Map `REQ-001`–`REQ-027` to document sections.
- [ ] Evaluate `AC-001`–`AC-012`.
- [ ] Record pass/fail evidence in the task checkpoint.

## 6. Quality Gate

- [ ] Run targeted terminology/leakage searches.
- [ ] Run Markdown/JSON structural checks available locally.
- [ ] Run `git diff --check`.
- [ ] Inspect only the new file's diff and confirm existing project contracts were not modified.
- [ ] Release the implementation lease and report the final file path.

## Rollback Points

- Before implementation: remove no product artifact; planning remains recoverable.
- After file creation but before validation: delete only the new unaccepted output if explicitly
  requested.
- After validation: revisions remain in-place; do not create version-suffixed duplicate files.
