# Skills and agents catalog

## Trellis workflow layer

Inherited through fresh Trellis initialization: `trellis-spec-bootstrap`, `trellis-update-spec`,
`trellis-before-dev`, `trellis-brainstorm`, `trellis-channel`, `trellis-session-insight`,
`trellis-check`, `trellis-break-loop`, and `trellis-meta`; plus `trellis-research`,
`trellis-implement`, and `trellis-check` agents.

## Agency reviewer layer

Installed in `.claude/agents/`: Social Media Strategist, Content Creator, Growth Hacker,
Short-Video Editing Coach, PR & Communications Manager, and TikTok Strategist. Their roles and
boundaries are in `agency-agents-installation.md` and the routing matrix.

## DMP runtime layer

The selected DMP capability map is in `dmp-capability-inventory.md`. DMP is referenced as a
shared runtime; this repository does not vendor or duplicate the entire plugin catalog.

## Toplink-specific skills

| Skill | Purpose |
|---|---|
| `toplink-source-grounding` | Classify evidence, status, allowed use, and human input gaps. |
| `toplink-imc-delivery` | Route a scoped deliverable through DMP, reviewers, gates, and staging. |
| `toplink-communication-safety` | Check public copy, claims, consent, disclaimer, and escalation. |
| `toplink-milestone-governance` | Apply milestone, lease, two-run, stable-ID, and external-state controls. |
