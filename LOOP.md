# Delivery loop — Toplink Y Viện

1. Read the canonical milestone, evidence sources, `STATE.md`, and `task.md`.
2. Classify every input as confirmed, inference, hypothesis, missing, or prohibited.
3. Acquire the writer lease and run the routed DMP skill to local staging with a trace.
4. Route the draft to the required Agency reviewers; preserve issue/evidence/verdict records.
5. Apply human/professional/legal/privacy gates where required.
6. Validate files, digests, stable IDs, and exact external read-back before any promotion.
7. Update `task.md`, `STATE.md`, and verified durable lessons in `MEMORY.md`.

## 1. State machine

```text
PREFLIGHT → FRAME → ROUTE → PRODUCE → REVIEW → VERIFY
                                  ↑                  │
                                  └──── REPAIR ──────┘
VERIFY → SYNC (only when approved) → CLOSE
```

No state transition bypasses a hard stop, a canonical Done gate, or an active conflicting lease.
`SYNC` is optional only when the milestone does not require an external destination.

## 2. PREFLIGHT — establish a safe start

1. Read the current user instruction and required read order in `CLAUDE.md`.
2. Check `GOVERNANCE.md §1`, canonical milestone dependencies, `STATE.md`, active `task.md`, and
   the `task.md` lease ledger.
3. Classify inputs as confirmed, inference, hypothesis, missing, unverified, or do-not-use.
4. Name the exact output, human gates, external target state, stop conditions, and verification.
5. If any prerequisite is absent, create a bounded blocker and stop before writing a deliverable.

## 3. FRAME — define success before writing

- Record scope proof, deliverables, non-goals, owner, review route, stable-ID namespace, and next
  safe action in `task.md`.
- Acquire the scoped writer lease. A file set without an acquired lease is read-only.
- For TL-M1–TL-M5, declare the active macro-run and preserve the exact two-run contract.

## 4. ROUTE — assign bounded responsibility

- Use the capability routing matrix and no more than three Agency reviewers per workstream.
- Claude and Codex use the coordination contract; no runtime silently takes over another's work.
- A DMP capability, reviewer, human gate, or operator is selected by need—not by convenience.

## 5. PRODUCE — create traceable local staging

- Verify DMP runtime capability, active brand `toplink-y-vien`, inputs, and source/profile digest.
- Invoke DMP when required, save the exact trace and output digest, and keep output local staging.
- A runtime failure is `BLOCKED_DMP_RUNTIME`; do not call a mock, manual review, or prior output a
  real invocation.

## 6. REVIEW — challenge before verification

- Route reviewers by specialty; retain their issues, evidence/location, repair request, and
  verdict. Keep health/legal/privacy matters as human gates.
- For Run 2, the fresh auditor performs the required independent/blind review before seeing the
  other runtime's detailed findings.
- Turn findings into a stable issue/repair ledger. New creative or health/strategy content routes
  back to the appropriate DMP authoring owner rather than being silently invented in repair.

## 7. VERIFY — prove the local result

- Check source/profile/output digests, active brand, stable IDs, reference integrity, schema,
  Unicode, secrets/PII, safety rules, required reviewers, and `git diff --check`.
- A required check that is skipped, failed, or cannot be evidenced is not a pass. Record the
  precise failure rather than averaging it away.
- Produce the Run 1 or Run 2 manifest from the committed template when the run requires it.

## 8. REPAIR — classify failure before retrying

- `DIRECT_REPAIR` is limited to structural, provenance, status, identity, or bounded formatting
  corrections that introduce no new marketing/health/legal fact.
- `DMP_SKILL_REAUTHOR` is required for net-new strategy, creative, health-sensitive, or substantive
  deliverable content. `HUMAN_GATE` remains open until a qualified person decides.
- After two identical bounded failures, stop and record a blocker. Never create a third run.

## 9. SYNC — promote only with authority

- Confirm exact user approval, target, range/schema, stable identity, and intended mutation.
- Make the smallest bounded external write; immediately exact-read-back and compare required
  fields, IDs, row counts, and Unicode.
- Failure leaves local staging authoritative and status blocked. Never reuse a Thảo Tây target.

## 10. CLOSE — atomic handoff or completion

1. Update `task.md` with changed paths, checks/verdicts, blockers/human gates, and next action.
2. Update `STATE.md` with concise verified sprint truth; distill only durable verified memory.
3. Release the lease after the checkpoint. A recipient acquires a new lease only then.
4. Commit only the verified, in-scope change when authorized; do not start the next milestone in
   the same close step.

## 11. Goal syntax

```text
/goal: <Toplink work item> is complete when <named checks> PASS;
       stop on <named hard stop>; do not advance beyond <milestone/gate>.
```
