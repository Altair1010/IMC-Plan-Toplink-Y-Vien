# Human Operator Walkthrough

This structural walkthrough uses the live staging workbook readback. It is not a claim that an
independent end user has completed a usability study.

| Operator question | Direct location | Result |
|---|---|---|
| Where do I update the current brand story? | `YV_01_BRAND` → `CÂU CHUYỆN` | PASS |
| Where do I capture a real Dry Run event? | `YV_03_CONTENT_SYSTEM` → `DRY RUN → ĐẦU VÀO NỘI DUNG` | PASS |
| Where do I turn the event into a content item? | same intake decision, then `YV_04_CAMPAIGN_CALENDAR` pipeline | PASS |
| Where do I see content status? | `YV_04_CAMPAIGN_CALENDAR` → `Trạng thái` | PASS |
| Where do I record response and learning? | pipeline columns `Inbox / phản hồi đáng chú ý` and `Điều học được` | PASS |

All locations use Vietnamese operational labels. None requires opening `_CONTROL_PLANE`.
