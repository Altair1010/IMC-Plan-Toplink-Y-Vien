# User-Facing Artifact Structure

## Existing surface areas

The repository deliberately separates canonical decisions, reusable controls,
and local work-in-progress:

```text
docs Toplink/     canonical strategy, milestones, and verified evidence inputs
docs/system/      reusable contracts, routing, templates, and operational controls
docs/prompts/     reusable two-run prompts
docs/brand/, docs/content/, docs/research/, docs/reports/
                  milestone outputs only
staging/          local non-canonical run artifacts; not an external target
.codex/, .claude/, .cursor/
                  host-specific integration adapters
```

`docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md` owns strategy and
`TOPLINK_PAGE_MILESTONES.md` owns execution and Done gates. A supporting
document must reference, not restate or override, the canonical decision.

## Placement rules

- Put reusable protocol, schemas, and handoff templates in `docs/system/`.
  `docs/system/templates/handoff-claude-to-codex.template.md` is the local
  pattern for an explicit envelope, provenance, review result, repair ledger,
  and remaining human gates.
- Put a run-specific output in `staging/toplink-reconciled/<run>/` only after a
  real run begins. Keep it local and non-canonical until its promotion gate.
- Keep reusable prompts in `docs/prompts/`; do not hide prompts in a milestone
  artifact or duplicate them per runtime.
- Keep host protocol code in the host folder and shared workflow logic in
  `.trellis/scripts/`, as described by the backend structure guide.

## Avoid

- Do not create `src/`, `pages/`, `components/`, or a frontend build setup:
  there is no approved UI scope.
- Do not put an external Sheet/Page target, secret, or unverified public claim
  in a user-facing document or a template.
- Do not treat a staging file as a published page, delivered Sheet, or approved
  public artifact.
