# Program Acceptance Matrix

Revision under test: branch `program/ktd-great-migration`; plan fingerprint
`627ab66d724c2e5017a3ee613433d65ba11048233c42b523bf288ee71e043c30`;
staging workbook `1v2bk-MOrYyDybgfAh1sYnOZ8D-Rw0bE9VO2HLG-t794`.

`PASS_WITH_NOTE` is non-blocking and preserves a stated evidence boundary. The GM-9 row is not
eligible to pass before the owner cutover gate.

| ID | Requirement / observable condition | Level | Evidence | Verdict |
|---|---|---:|---|---|
| ID-01 | Historical Toplink files are not renamed or deleted | E2 | Git diff; baseline manifest | PASS |
| ID-02 | KTD becomes canonical at cutover | E3 | GM-9 post-cutover readback | NOT_TESTED — GM-9 gate |
| ID-03 | Legacy lineage is explainable without becoming current context | E2 | migration ledger; runtime-context test | PASS |
| ID-04 | No current KTD fact is inferred solely from legacy | E1 | fact provenance and unknown register | PASS |
| CON-01 | Legal-pending data does not block ordinary KTD planning | E2 | runtime-context test; Sheet readback | PASS |
| CON-02 | Reviewer identity/credentials are absent from active Page runtime | E2 | runtime-context test | PASS |
| CON-03 | Writer/production approver is absent as a content gate | E2 | human-tab and runtime inspection | PASS |
| CON-04 | Claim-substantiation workflow is absent from active runtime | E2 | runtime-context test | PASS |
| CON-05 | Price/promotion/usage-condition gates are absent | E2 | exact target readback | PASS |
| COM-01 | Active Page plan does not require price publication | E1 | Page-role section | PASS |
| COM-02 | No promotion publication workflow is active | E1 | Page-role section | PASS |
| COM-03 | No usage-condition publication workflow is active | E1 | Page-role section | PASS |
| COM-04 | No efficacy/result claim architecture is active | E1 | Page boundaries and content grammars | PASS |
| COM-05 | No result-promise architecture is active | E1 | Page boundaries and content grammars | PASS |
| COM-06 | No verified/proven positioning is active | E1 | strategy consistency matrix | PASS |
| DRY-01 | Current business phase is represented as Dry Run | E3 | live staging readback | PASS |
| DRY-02 | A real Dry Run event has an ordinary-language intake | E3 | `YV_03_CONTENT_SYSTEM` readback | PASS |
| DRY-03 | Event-to-content flow does not expose machine IDs | E2 | validator and human-tab scan | PASS |
| DRY-04 | Content priority is editable as operations change | E3 | editable state-based staging pipeline | PASS |
| DRY-05 | No fixed 28-day sequence is required | E2 | plan inspection and active runtime tests | PASS |
| HUM-01 | Exactly four human tabs plus Control Plane are active | E3 | staging metadata readback | PASS |
| HUM-02 | No `_key` or `_audit` columns exist in human tabs | E2 | validator and exact values | PASS |
| HUM-03 | No node/path/hash fields exist in human tabs | E2 | validator and exact values | PASS |
| HUM-04 | No sync/readback codes exist in human tabs | E2 | validator and exact values | PASS |
| HUM-05 | Human states use understandable Vietnamese labels | E3 | live readback and validation rules | PASS |
| HUM-06 | Operator workflow does not require Control Plane | E2 | operator walkthrough | PASS_WITH_NOTE |
| HUM-07 | `YV_08_experiments` is not active | E3 | staging metadata readback | PASS |
| LIN-01 | Brand/positioning/narrative lineage has a coherent target disposition | E1 | ledger and `YV_01_BRAND` | PASS |
| LIN-02 | Audience/Page lineage is represented in `YV_02_AUDIENCE_PAGE` | E1 | ledger and target readback | PASS |
| LIN-03 | Useful content-pillar logic is transformed into territories | E1 | ledger and `YV_03_CONTENT_SYSTEM` | PASS |
| LIN-04 | Campaign/calendar value is transformed without calendar-first assumptions | E2 | ledger, target, active tests | PASS |
| LIN-05 | YV_10–YV_12 knowledge is absorbed only where useful | E1 | ledger dispositions | PASS |
| CP-01 | Every active human table has a machine binding | E2 | validator and Control Plane readback | PASS |
| CP-02 | Every required node resolves to a source or derived rule | E2 | resolver test | PASS |
| CP-03 | Growing tables do not rely on fixed data-row bindings | E2 | binding validator | PASS |
| CP-04 | Machine IDs do not leak into human tabs | E2 | negative validator test | PASS |
| CP-05 | Control Plane stores topology rather than business values | E1 | Control Plane inspection | PASS |
| CP-06 | Human canonical fields cannot be silently overwritten | E2 | authority negative test | PASS |
| STATE-01 | One current business state exists per semantic object | E2 | unique-node validator and workbook scan | PASS |
| STATE-02 | Views are projections, not independently maintained truth | E1 | pending-evidence VIEW authority | PASS |
| STATE-03 | Canonical changes invalidate or update projections | E1 | VIEW points to canonical pipeline; no duplicate store | PASS_WITH_NOTE |
| STATE-04 | No stale owner-action/input-gap projection can contradict current state | E3 | legacy tabs absent from staging | PASS |
| MIG-01 | Every active legacy object has one disposition | E2 | 50/50 ledger coverage check | PASS |
| MIG-02 | Archive-only objects are absent from normal KTD runtime | E2 | runtime-context test | PASS |
| MIG-03 | No current KTD fact is inferred solely from legacy | E1 | provenance map and unknown register | PASS |
| MIG-04 | Campaign/content is grounded in current Dry Run truth | E1 | campaign brief and source-bounded capture needs | PASS_WITH_NOTE |

## Summary

- Blocking PASS: 42
- Non-blocking PASS_WITH_NOTE: 3
- GM-9-only NOT_TESTED: 1
- FAIL: 0
- BLOCKED: 0

The structural operator walkthrough is evidence, not an independent end-user study. The current
campaign seed contains explicit capture needs because present events/assets were not available;
no fabricated event was promoted. These notes do not invalidate cutover readiness.
