# Product and operating spec — Toplink Y Viện

## 1. Authority and scope

This specification operationalizes the independent corporate Facebook Page track for Nhất Liệu
Y Viện Toplink. It does not replace the canonical sources:

- `docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md` owns strategy, decisions, scope, and risk.
- `docs Toplink/TOPLINK_PAGE_MILESTONES.md` owns TL-M0–TL-M9 sequencing, deliverables, and Done gates.
- The other files in `docs Toplink/` are evidence inputs only.

The project creates a trust-led, evidence-grounded Facebook Page launch. It may develop local
awareness and service discovery in Hanoi only when the exact offer is verified. National activity
is education and brand awareness by default.

## 2. Non-goals

- No diagnosis, treatment, cure, prevention, medical replacement, or guaranteed result claim.
- No public franchise/legal relationship statement without independently verified permission.
- No unverified price, service menu, booking, qualification, address, product efficacy, logistics,
  warranty, or availability claim.
- No paid scale, nationwide conversion, new primary channel, Page mutation, Sheets mutation, or
  public publishing without the specific canonical and human gates.
- No reuse of a Thảo Tây external target, Sheet, analytics baseline, credential, or milestone.

## 3. Evidence model

Every material statement records `source_path`, location, status, and allowed use.

| Status | Permitted use |
|---|---|
| `TOPLINK_CONFIRMED` | State only within the sourced meaning. |
| `INFERENCE` | Label as reasoning, never as observed fact. |
| `HYPOTHESIS` | Propose only with a validation path. |
| `MISSING_INPUT` | Record as a blocker; cannot support a claim. |
| `UNVERIFIED` / `DO_NOT_USE` | Never use as public fact, proof, or promise. |

The project may use the sourced positioning that Toplink is a proactive, regular body-care
experience combining Lý liệu, Dược liệu, and Dưỡng liệu. It must not imply that Toplink is a
hospital, a replacement for care by a medical professional, a miracle-treatment provider, or a
pure beauty spa. Sources: `Ho-so-thuong-hieu-Y-Vien-Toplink-Cai-tien-2026.md` §§1–3;
`01_positioning_and_pillars.md`.

## 4. Audience, positioning, channel, and content boundaries

- The working audience is a launch hypothesis: busy adults 28–55 in Hanoi, middle-aged/older
  audiences and caregivers, women seeking refined proactive care, and nationwide learners of
  dưỡng sinh. Validate rather than present these segments as measured facts.
- Facebook Page is the primary channel. Facebook Reels supports discovery. TikTok informs
  short-form mechanics only unless a future milestone changes the boundary.
- Candidate territories are identity and limits, body literacy, operational proof,
  understandable Lý–Dược–Dưỡng, and founder/community journey. DMP validation must converge on
  three to five weighted pillars totaling 100%.
- Before offer readiness, calls to action are limited to follow, save, or share. Booking or
  commercial CTAs require verified offer, eligibility, location, availability, contact owner,
  response SLA, privacy notice, price/conditions when mentioned, and compliance approval.
- Founder presence is selective; corporate voice is the default. Founder content cannot diagnose,
  prescribe, explain medical mechanisms, or impersonate an expert.

Sources: `TOPLINK_PAGE_MASTER_PLAN.md` §§6–11 and
`10_content_formulas_and_checklist.md`.

## 5. Communication and safety contract

Use bounded support language such as “hỗ trợ thư giãn”, “hỗ trợ làm ấm”, “hỗ trợ cảm giác đau
mỏi/căng cứng”, “chăm sóc sức khỏe chủ động”, and individual variation where the source permits.
Do not claim treatment, recovery, cure, fixed timelines, absolute prevention, replacement of
medical advice, or effectiveness for everyone. Do not generalize a testimonial into an outcome.

Health-sensitive content must include the approved safety framing where applicable: Toplink’s
products/services support proactive care, relaxation, and restoration; they do not replace
diagnosis, treatment, or medical advice. People with underlying conditions, pregnancy, treatment
medication, implanted devices, or unusual symptoms need professional advice first.

Acute or concerning symptoms must route to medical care, not an offer or content conversion path.
Testimonials/UGC require consent for purpose, channel, duration, withdrawal, and redaction.

Sources: `02_communication_safety.md`; Brand Profile §9; product files `04`–`06`.

## 6. DMP and Agency workflow

Use brand slug `toplink-y-vien`. Every deliverable-producing milestone requires a real DMP trace
with trace ID, timestamp, DMP version, active-brand read-back, skill, exact input paths/digests,
output path/digest, status, and skipped dimensions.

Default routing:

| Workstream | Primary DMP capability | Agency review |
|---|---|---|
| Evidence and source intake | `import-guidelines`, `brand-setup` | PR Manager |
| Audience, positioning, campaign, KPI | `audience-intelligence`, `campaign-plan` | Social Strategist → Growth Hacker |
| Pillars, copy, calendar, production | `social-strategy`, `content-engine`, `content-calendar` | Content Creator → PR Manager |
| Reels briefs | `video-script` | Short-Video Coach → TikTok Strategist |
| Safety and governance | `check`, `status`, `output-folder` | PR Manager → required human gate |

No more than three Agency Agents may participate in one workstream. Agency review cannot set
`APPROVED`; human/professional/legal/privacy gates remain distinct.

## 7. Milestone acceptance contract

| Milestone | Required outcome |
|---|---|
| TL-M0 | Scope, evidence, safety, capability, and readiness gates locked without external mutation. |
| TL-M1 | Evidence/status/allowed-use map; unresolved legal, product, offer, and Page inputs remain blocked. |
| TL-M2 | DMP brand profile and source digest using `toplink-y-vien`, with required trace. |
| TL-M3 | Audience/positioning/pillar hypotheses with validation and weights totaling 100%. |
| TL-M4 | Relative four-week Facebook Page campaign architecture with safety and capacity gates. |
| TL-M5 | Calendar, asset plan, Reels briefs, production briefs, approval/measurement workflow. |
| TL-M6 | Controlled pilot only after approved start date, capacity, human reviewers, and operational inputs. |
| TL-M7–TL-M9 | Evidence-led roadmap, scale decisions, and bounded handoff only after earlier gates pass. |

TL-M1–TL-M5 use exactly two macro-runs: Run 1 build/reconciliation and fresh-context Run 2
audit/finalize. The same source/profile digest, DMP version, and active brand are required. A
mismatch returns work to Run 1; a third run is forbidden.

## 8. External-state and completion rules

Google Sheets is `BLOCKED_TARGET_INPUT` until the user provides the exact spreadsheet, tab,
range, schema, and write approval. When approved, use stable identity, a bounded upsert, and exact
read-back; never create `_v2` tabs, overwrite broadly, or reuse a Thảo Tây workbook.

The planned Toplink-only tab registry, approval payload, mapping, validation/error states, and
read-back evidence are defined in `docs/system/toplink-google-sheets-operational-contract.md`.
That contract plans the architecture only; it does not supply a target or authorize a write.

Local artifacts remain `SYNC_PENDING_TARGET` rather than complete whenever an external target is
required but not approved. A milestone is done only when its canonical deliverables, evidence,
DMP trace, reviewer records, human gates, and—when applicable—external read-back all pass.

## 9. Open inputs

- Official Page URL/ID and dated baseline snapshot.
- Public/legal proof for franchise and entity wording.
- Product/service dossiers, exact offer, pricing, availability, eligibility, and warranties.
- Booking/contact/privacy process, response owner, and SLA.
- Content start date, production capacity, professional reviewer, and approved Sheets target.
