# Agency Agents installation record

## Installed project-local reviewers

The following six vetted Agency Agents are inherited from the Thảo Tây setup and stored in
`.claude/agents/`:

| Agent | Role in Toplink |
|---|---|
| Social Media Strategist | Facebook Page strategy, campaign architecture, channel boundaries |
| Content Creator | Narrative, pillars, editorial calendar, copy |
| Growth Hacker | Greenfield KPI, experiment, and growth-loop review |
| Short-Video Editing Coach | Reels briefs, production workflow, accessible short-form craft |
| PR & Communications Manager | Entity framing, reputation, sensitive wording, approval conditions |
| TikTok Strategist | Short-form mechanics review only; not a primary delivery channel |

## Rules

- DMP drafts; Agency Agents review or specialize. Do not create competing writers.
- Activate only the reviewers required by the routing matrix, with a maximum of three per
  workstream.
- Replace inherited Thảo Tây-specific context with `spec.md`, `RULES.md`, and the Toplink
  knowledge brief before use.
- No agent can mark health, legal, privacy, publication, or external-state work `APPROVED`.
