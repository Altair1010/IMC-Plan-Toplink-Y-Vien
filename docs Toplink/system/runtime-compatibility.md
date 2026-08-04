# TL-M2 — DMP runtime compatibility (Toplink Y Viện)

> **Run 1 Phase A · local-only · `external_writes=0`.** Records the runtime surface the M3/M4
> generations rely on, so a Run 2 fresh audit can confirm the same environment produced the package.
> Stable ID `TL-RUNTIME-COMPAT-001`.

## 1. Runtime identity

| Field | Value | Source |
|---|---|---|
| DMP product | Digital Marketing Pro | plugin `neels-plugins/digital-marketing-pro` |
| DMP version | `3.15.1` | plugin cache path `.../digital-marketing-pro/3.15.1/` |
| Active brand slug | `toplink-y-vien` | `_active-brand.json` |
| Active brand read-back | `Toplink Y Viện (toplink-y-vien)` | `switch-brand` read-back (`TL-M1-DMP-SWITCH-001`) |
| Profile schema_version | `1.0.0` | `profile.json` |
| Guidelines manifest | 5 categories / 52 rules | `guidelines/_manifest.json` |
| Locale | vi_VN · dd/MM/yyyy · metric | `profile.language.locale_formatting` |

## 2. Guidelines layer compatibility (read by every generation)

| Category | Rules | Digest (from `TL-M1-DMP-IMPORT-001`) | Precedence |
|---|---|---|---|
| `restrictions` | 18 | `fe586082…` | Highest — banned words / mandatory disclaimer |
| `voice-and-tone` | 11 | `47add05b…` | Voice detail beyond 4 numeric scores |
| `messaging` | 9 | `f85a0e69…` | Approved key messages / positioning language |
| `visual-identity` | 8 | `3e4585de…` | Colors / fonts / motion tokens |
| `channel-styles` | 6 | `2c355763…` | Channel overrides (FB Page primary) |

`channel-styles` overrides base voice when a specific channel is targeted. `restrictions` is
non-overridable (health forbidden catalogue + disclaimer).

## 3. Channel runtime roles

| Channel | Runtime role | State |
|---|---|---|
| Facebook Page | Primary — corporate identity, education, operational proof, community | `ACTIVE` |
| Reels (on Facebook) | Discovery / retention mechanics | `ACTIVE_SUPPORT` |
| Zalo · phone · Google Maps | Conversion role | `PENDING_INPUT` (not wired) |
| Website | Long-term digital layer | `ROADMAP` (not primary; not wired) |
| TikTok | Mechanics reference only | `REVIEW_ONLY` |
| Personal FB (founder) | Selective cross-post | `ITEM_APPROVAL_REQUIRED` |

No conversion runtime is enabled for a `PENDING_INPUT` channel. Booking/contact CTA stays disabled
until an offer gate (does not yet exist) passes.

## 4. Compatibility invariants for Run 1 ↔ Run 2

- Same `profile_digest` `a45e4ae4…` and `source_digest` `3ba91761…` across both runs.
- Same DMP version `3.15.1` and active brand `toplink-y-vien`.
- Guidelines manifest unchanged (5/52). A change to any of the above = `FAIL_BACK_TO_RUN1`.
- `_active-brand.json` is shared global state: any non-Toplink work must `switch-brand` away from
  `toplink-y-vien` first (and switch back before Toplink work); prior value backed up at
  `staging/…/TL-M1-evidence/dmp-runtime-backup/_active-brand.before.json`.

## 5. What the runtime must NOT do (fail-closed)

- No Sheet write / Page mutation / publish / messaging (`external_writes=0`).
- No new brand entity, no `brand-setup` wholesale re-derive that would clobber the G5-locked profile.
- No unsupported field (price, product efficacy, franchise/legal public wording) promoted into
  runtime output as fact.
- No secret / credential / local machine path written into any deliverable.

### 5.1. Non-breaking emitted-ID namespace crosswalk

Run 1 IDs are already emitted and remain immutable. This crosswalk resolves their namespace family without allocating or renaming any stable ID:

| Emitted Run 1 form | Milestones §2.6 family | Rule |
|---|---|---|
| `TL-A01`, `TL-A02a`, `TL-A02b`, `TL-A03`, `TL-A04` | `TL-AUD-{NNN}` | retained as Run 1 aliases; no automatic renumber |
| `TL-P1`–`TL-P5` | `TL-PIL-{NNN}` | retained as pillar aliases; no automatic renumber |
| `TL-KPI-01`–`TL-KPI-11` | `TL-KPI-{NNN}` | retained as KPI aliases; zero-padding change is not identity migration |
| `CL-*` claim IDs | `TL-CLAIM-{NNN}` | retained as claim aliases; a canonical numeric ID requires a separately governed allocation |

New artifacts must use the §2.6 namespace. Existing aliases may only be changed through an explicit migration with complete reference read-back; this Run 2 performs no breaking rename.

## 6. VERIFY

- [x] DMP version + active brand + guidelines manifest recorded and reproducible.
- [x] Channel runtime roles match `profile.channels` and RULES channel policy.
- [x] Run 1/Run 2 invariants stated; drift rule = `FAIL_BACK_TO_RUN1`.
- [x] `external_writes=0`; no runtime mutation performed by this file.
