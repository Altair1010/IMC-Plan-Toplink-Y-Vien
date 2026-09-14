# GM-6 Requirement-to-Evidence Matrix

Revision under test: workbook plan fingerprint `627ab66d724c2e5017a3ee613433d65ba11048233c42b523bf288ee71e043c30`

| Requirement | Acceptance condition | Evidence | Verdict |
|---|---|---|---|
| Active-table coverage | Every human section has a Control Plane table node | `_CONTROL_PLANE!A1:O20` readback | PASS |
| Required field coverage | Brand, phase, event, decision, status, and learning fields resolve | resolver tests | PASS |
| Unique nodes | Machine nodes are non-empty and unique | validator test | PASS |
| Robust bindings | Section, label, and header bindings resolve without fixed data-row numbers | validator test | PASS |
| Authority | Human canonical fields are machine-read-only | negative authority test | PASS |
| State maps | Active phase, decision, and content status values have explicit mappings | Control Plane readback | PASS |
| No duplicated truth | Control Plane contains topology and mappings, not current business values | plan and range inspection | PASS |

Hard fails: none.

Promotion allowed: YES, to GM-7 only.
