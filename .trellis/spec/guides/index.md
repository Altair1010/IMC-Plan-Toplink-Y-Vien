# Project Thinking Guides

These guides cover the cross-cutting decisions that recur in this
documentation-and-automation repository. They complement, but never override,
the canonical Toplink plan, milestones, governance, and safety controls.

| Guide | Use it when |
|---|---|
| [Canonical reuse](code-reuse-thinking-guide.md) | a plan, template, source fact, status, or automation helper appears reusable |
| [Artifact flow](cross-layer-thinking-guide.md) | a change crosses evidence, an artifact, a runtime, a reviewer, or an external delivery gate |

## Always start with ownership

Before changing an artifact, identify the owner in `RULES.md` and use the
source hierarchy in `CLAUDE.md`. In particular, the master plan owns strategy,
the milestone document owns sequencing and Done gates, and `task.md` owns the
current lease and handoff state.

These guides are not permission to invent missing inputs, bypass a human gate,
or reuse a Thảo Tây identifier, target, credential, baseline, deliverable, or
milestone.
