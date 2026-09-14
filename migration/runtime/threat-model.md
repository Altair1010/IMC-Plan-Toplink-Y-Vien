# KTD Migration Runtime Threat Model

## Trust boundaries

- Google Sheets metadata and cell payloads cross an external API boundary.
- Human-entered workbook content crosses into machine resolution.
- Legacy repository content crosses from historical evidence into current runtime selection.

## Assets

- Human canonical business decisions.
- The original legacy workbook and Git lineage.
- Staging workbook topology and semantic bindings.
- Migration evidence integrity.

## Primary abuse and failure cases

| Threat | Failure | Control |
|---|---|---|
| Spoofing | Wrong workbook or tab is treated as target | Exact spreadsheet ID, sheet ID, and title readback |
| Tampering | Target changes after verification | Hash/revision snapshot and pre-promotion revalidation |
| Repudiation | A write cannot be tied to the run | Run ID, exact ranges, evidence pointers, and gate record |
| Information disclosure | Credentials or personal data enter evidence | No credential reads in runtime; secret scan and bounded cell content |
| Denial of service | Broad range or retry loop consumes excessive calls | Bounded ranges and one retry only with mechanism delta |
| Elevation of privilege | Automation overwrites human decisions | Explicit authority map; machine writes allowed only for MACHINE_DERIVED nodes |
| Prompt injection | Retrieved legacy text changes migration authority | Retrieved content is data; source precedence and allowlisted runtime context are enforced in code |

The staging workbook is disposable and non-canonical. Deleting legacy sheets inside that copy
does not delete source history; GM-9 promotion remains separately gated.
