# Structured Artifact Contracts

## No TypeScript layer exists

There is no TypeScript compiler or frontend runtime. Structured contracts are
instead represented by Python types, JSON/JSONL records, and explicit Markdown
schemas. Treat them as interfaces: a prose change can break a reader, hook, or
handoff just as a type change can break code.

## Existing contract owners

- `common/types.py` defines the `TaskData`, `TaskInfo`, and `AgentRecord`
  shapes used by Trellis readers.
- `docs/system/templates/handoff-envelope.template.json` and
  `toplink-run-manifest.template.json` define machine-readable handoff and run
  records.
- `docs/system/toplink-google-sheets-operational-contract.md` owns the
  proposed approval, delivery, mapping, stable-identity, and read-back fields;
  it does not authorize a Sheet target.
- `TOPLINK_PAGE_MILESTONES.md` owns the stable identity namespace and status
  state machine for milestone artifacts.

## Contract rules

- Add a field only after identifying every reader, writer, template, and
  validator. Preserve unknown JSON fields during a targeted update.
- Use stable IDs and exact status strings; do not derive identity from a title,
  local path, or changing display label.
- Keep UTF-8 text intact and write JSON with `ensure_ascii=False`.
- Mark provenance and evidence state where a material claim requires it.
  `MISSING_INPUT` is a valid contract value, not an omission to hide.

## Avoid

- Do not add TypeScript interfaces that have no code consumer.
- Do not rename or remove template fields to make a one-off artifact shorter.
- Do not use an unverified source as if it satisfied a typed, confirmed field.
