# Google Sheets architecture

## Current state

Toplink has no approved Sheet target. The state is `BLOCKED_TARGET_INPUT`; no script, connector,
or agent may create, guess, or reuse a Thảo Tây spreadsheet, tab, range, or schema.

## Future write contract

Before an external write, obtain the user-approved spreadsheet ID, tab, range, schema, stable
identity fields, source artifact, and write authorization. Then:

1. Validate the local source artifact and DMP/review state.
2. Upsert only the smallest approved range using stable identity.
3. Preserve unrelated formulas, formatting, protected cells, and user data.
4. Read back the exact range and verify identity, row count, required values/formulas, and
   Vietnamese Unicode.
5. Record the revision and evidence in the canonical output index/decision log required by the
   active milestone.

A response acknowledging a write is not verification. A failed or unreadable target remains
`VERIFY_FAILED` or `BLOCKED_AUTH`; local work stays staging.
