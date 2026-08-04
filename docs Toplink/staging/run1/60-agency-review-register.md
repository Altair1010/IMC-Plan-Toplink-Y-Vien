# 60 — Agency review register

Sources:

- `staging/toplink-reconciled/TL-M2-M4-run1/agency-review.md` — `d6006af993afd09c7f090e616c00b2a0c386c37ba275f314dc027d9c4b89ea6d`
- `staging/toplink-reconciled/TL-M5-run1/agency-review.md` — `c8390a46de479d655a751a814b4ab89bee8832ee7c9ffdcaae731db839c29306`

| Stable ID | Workstream | Reviewer route | Finding | Verdict | Required gate |
|---|---|---|---|---|---|
| `TL-R1-REV-001` | TL-M1 | PR Manager | evidence/status/allowed-use locally reconciled | `NEEDS_HUMAN_REVIEW` | entity/legal/health inputs |
| `TL-R1-REV-002` | TL-M2 | PR Manager | profile and one-slug runtime structure pass | `PASS` | public franchise/legal/product wording held |
| `TL-R1-REV-003` | TL-M3 audience | Social Strategist → Growth Hacker | audience remains a launch hypothesis | `PASS` | pilot validation |
| `TL-R1-REV-004` | TL-M3 positioning | Social Strategist → Growth Hacker → PR | positioning is not public-approved | `NEEDS_HUMAN_REVIEW` | human public-use gate |
| `TL-R1-REV-005` | TL-M3 pillars | Social Strategist → Growth Hacker | 6/6/8/4/4 fills 28 slots | `PASS` | TL-P2/TL-P4 per-item review |
| `TL-R1-REV-006` | TL-M4 campaign | Social Strategist → Growth Hacker | four-week relative structure and safe fallback pass | `PASS` | W2 professional review; offer gate |
| `TL-R1-REV-007` | TL-M4 KPI | Growth Hacker → PR | greenfield count/rate rules and CTA boundary pass | `PASS` | baseline/capacity/offer inputs |
| `TL-R1-REV-008` | TL-M5 calendar/copy | Content Creator → PR Manager | 28 identities, A/B/C, claims, routes and placeholder assets complete | `PASS` | 10 health, 4 founder and 2 product-adjacent items need human review |
| `TL-R1-REV-009` | TL-M5 Reels | Short-Video Coach → TikTok Strategist | 12 Reels structurally pass; Facebook-first; TikTok mechanics only | `REVIEWED` | six health Reels and asset rights held |
| `TL-R1-REV-010` | TL-M5 safety | PR Manager → human/professional | support-level framing and disclaimers pass Agency review | `NEEDS_HUMAN_REVIEW` | health professional gate before publish |
| `TL-R1-REV-011` | TL-M5 founder/privacy | PR Manager → human owner | founder/BTS/UGC require documented consent | `NEEDS_HUMAN_REVIEW` | purpose/channel/duration/withdrawal/redaction consent |
| `TL-R1-REV-012` | TL-M5 legal/product | PR Manager → human owner | franchise/legal and unsupported product efficacy remain blocked | `NEEDS_HUMAN_REVIEW` | legal documents and product dossier |

## Rollup

- Structural/compliance reviewer result: `PASS` locally.
- Overall sensitive-material result: `NEEDS_HUMAN_REVIEW`.
- Reviewer count is at most three per workstream; no competing artifact version was accepted.
- Testimonial/UGC stays blocked unless consent is `OBTAINED`; no generalized testimonial is present.
- No reviewer or runtime granted human `APPROVED`; no item is publish-ready.
