# GM-3 Requirement-to-Evidence Matrix

- Revision under test: `ea93668` plus current GM-3 artifacts
- Inputs: CURRENT_KTD_TRUTH; migration ledger; target architecture; locked exclusions

| REQ_ID | Requirement | Acceptance condition | Required evidence | Observed evidence | Verdict | Notes |
|---|---|---|---|---|---|---|
| GM3-01 | Brand target rebuilt | Current KTD identity and explicit unknowns replace legacy facts | E1 | `strategy/YV_01_BRAND.md` | PASS | Slogan and detailed story remain UNKNOWN. |
| GM3-02 | Audience and Page target rebuilt | Need-state model avoids unsupported precision and defines Page role | E1 | `strategy/YV_02_AUDIENCE_PAGE.md` | PASS | First need state is visibly hypothetical. |
| GM3-03 | Content target rebuilt | Current territories grammar and intake rules exist | E1 | `strategy/YV_03_CONTENT_SYSTEM.md` | PASS | Current-source gates remain explicit. |
| GM3-04 | Cross-layer semantics agree | Identity phase CTA boundaries and evidence rules do not conflict | E2 | `strategy-consistency-matrix.md` | PASS | Eight checks pass. |
| GM3-05 | Dry Run event is consumable | A fixture maps end to end without being called current truth | E2 | `strategy/tests/strategy-fixture.md` | PASS | Fixture requires a current source before real use. |
| GM3-06 | Legacy contamination absent | No Toplink-only factual content is promoted | E2 | strategy source/status review | PASS | Legacy is method and lineage only. |
| GM3-07 | Removed constraints absent | No legal reviewer approval or claim gate appears in active flow | E2 | strategy boundary scan | PASS | Prohibited concepts appear only as exclusions. |

- HARD_FAILS: none
- OPEN_UNKNOWNS: exact current brand, operational, audience, and asset facts listed in GM-1
- CONVERGENCE: PROGRESSING
- NEXT_SIGNAL: instantiate the state-based Dry Run campaign and content pipeline
- PROMOTION_ALLOWED: YES
