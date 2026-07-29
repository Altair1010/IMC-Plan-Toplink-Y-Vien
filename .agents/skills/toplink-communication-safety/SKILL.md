---
name: toplink-communication-safety
description: Review Toplink Y Viện copy, scripts, briefs, CTAs, product mentions, testimonials, and public-facing plans for claim safety, privacy, and escalation requirements. Use before presenting, approving, publishing, or routing health-sensitive or commercial material.
---

# Toplink Communication Safety

## Load the controls

Read `RULES.md`, `spec.md` section 5, `docs/system/toplink-knowledge-brief.md`, and `docs Toplink/02_communication_safety.md`. Load the relevant product file when a product is named.

## Review every material claim

Classify each statement:

- `ALLOWABLE_WITH_SOURCE` — bounded, source-supported, and not misleading.
- `REWRITE_REQUIRED` — could be made safe by narrowing language or adding required context.
- `NEEDS_HUMAN_REVIEW` — health-sensitive, legal, privacy, consent, entity, or offer condition is unresolved.
- `BLOCKED` — diagnosis, treatment, cure, prevention, guarantee, medical replacement, unsupported efficacy, unverified franchise/public legal claim, or missing consent.

Never use a disclaimer to rescue a prohibited or unsupported claim.

## Required remedies

- Prefer support-level, individual-variation language only when source-supported.
- Require the Toplink safety framing for health-sensitive public material.
- Refer concerning symptoms, high-risk conditions, pregnancy, implants, treatment medication, or unusual symptoms to professional advice rather than a conversion path.
- Require documented testimonial/UGC consent for purpose, channel, duration, withdrawal, and redaction.
- Before offer readiness, restrict CTA to follow, save, or share.

## Output

Return a claim ledger with quote/location, classification, evidence, exact repair, required disclaimer, and escalation owner. Do not issue `APPROVED`; the highest agent verdict is `REVIEWED` or `NEEDS_HUMAN_REVIEW`.
