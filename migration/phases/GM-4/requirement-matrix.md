# GM-4 Requirement-to-Evidence Matrix

- Revision under test: current GM-3 strategy plus GM-4 campaign artifacts
- Inputs: current phase; current-truth boundary; strategy; pipeline contract

| REQ_ID | Requirement | Acceptance condition | Required evidence | Observed evidence | Verdict | Notes |
|---|---|---|---|---|---|---|
| GM4-01 | Current campaign exists | Brief is explicitly KTD and Dry Run | E1 | `campaign/current-campaign-brief.md` | PASS | No legacy calendar premise. |
| GM4-02 | State-based planning | Phase and priority change with operations rather than fixed weeks | E2 | `campaign/pipeline-model.md` | PASS | No Week 1–4 or 28-day dependency. |
| GM4-03 | End-to-end pipeline | Event or capture need reaches response and learning | E2 | pipeline model and seed | PASS | Response and learning remain empty until observed. |
| GM4-04 | Rows are grounded | Every initial row is a labeled capture need with explicit missing source | E2 | `campaign/pipeline-seed.csv` | PASS | No fictitious completed event or existing asset. |
| GM4-05 | Human statuses usable | Vietnamese labels and side exits are defined | E1 | pipeline model | PASS | Machine mapping is deferred to Control Plane. |
| GM4-06 | Variants are lean | No default A B C variants | E2 | seed structure scan | PASS | One row equals one item. |
| GM4-07 | CTA is operational | All seed CTAs are allowed low-pressure classes | E2 | seed CTA scan | PASS | Booking is not active. |

- HARD_FAILS: none
- OPEN_UNKNOWNS: real current events assets standards responses and learning are pending human observation
- CONVERGENCE: PROGRESSING
- NEXT_SIGNAL: build the exact four-tab Vietnamese human workbook in the isolated staging workbook
- PROMOTION_ALLOWED: YES
