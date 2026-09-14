"""Deterministic KTD workbook plan and semantic runtime.

This module is additive. It does not import or mutate the legacy Toplink Sheet runtime.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from copy import deepcopy


HUMAN_SHEETS = (
    "YV_01_BRAND",
    "YV_02_AUDIENCE_PAGE",
    "YV_03_CONTENT_SYSTEM",
    "YV_04_CAMPAIGN_CALENDAR",
)
CONTROL_SHEET = "_CONTROL_PLANE"
CONTROL_COLUMNS = (
    "type",
    "human_object",
    "machine_node",
    "sheet",
    "table_or_section",
    "binding_type",
    "binding",
    "semantic_path",
    "relation",
    "parent_node",
    "authority",
    "source_of_truth",
    "state_map",
    "version",
    "notes",
)
MACHINE_METADATA_LABELS = {
    "_key",
    "_audit",
    "machine_node",
    "semantic_path",
    "binding",
    "node",
    "hash",
    "sync_state",
    "readback_state",
}


BRAND_ROWS = [
    ["KHIẾT TÂM ĐƯỜNG — THƯƠNG HIỆU", "", ""],
    ["Dùng tab này để cập nhật sự thật thương hiệu hiện hành. Nội dung chưa có nguồn được ghi rõ là chưa xác nhận.", "", ""],
    ["", "", ""],
    ["CỐT LÕI THƯƠNG HIỆU", "", ""],
    ["Hạng mục", "Nội dung hiện tại", "Ghi chú"],
    ["Tên thương hiệu", "KHIẾT TÂM ĐƯỜNG", "Tên viết tắt: KTD"],
    ["Slogan", "Chưa xác nhận từ nguồn hiện hành", "Cần chủ thương hiệu bổ sung nguồn chính thức"],
    ["KTD là gì?", "Một hệ thống truyền thông lấy thực tế hiện hành, quá trình chuẩn bị, trải nghiệm, Dry Run và điều học được làm trung tâm", "Ranh giới truyền thông hiện hành"],
    ["KTD muốn được nhớ đến như thế nào?", "Chưa xác nhận từ nguồn hiện hành", "Không lấy định vị Toplink cũ để điền"],
    ["Giá trị cốt lõi", "Chưa xác nhận từ nguồn hiện hành", "Không suy diễn từ tài liệu legacy"],
    ["Triết lý Thân – Tâm – Trí", "Đã xác nhận là một chủ đề truyền thông; ý nghĩa và cách diễn đạt chính thức chưa được xác nhận", "Chờ nguồn KTD hiện hành"],
    ["Giai đoạn hiện tại", "Dry Run", "Ưu tiên sự kiện thật, chuẩn hóa và học hỏi vận hành"],
    ["Trạng thái thương hiệu hiện tại", "Đang được chuẩn bị và chuẩn hóa qua thực hành vận hành", "Suy luận giới hạn từ trạng thái Dry Run"],
    ["", "", ""],
    ["ĐỊNH VỊ", "", ""],
    ["Hạng mục", "Nội dung hiện tại", "Ghi chú"],
    ["KTD dành cho ai?", "Chưa đủ dữ liệu hiện hành để chốt chân dung; dùng nhóm nhu cầu và phản hồi quan sát được", "Không dùng độ tuổi, thu nhập hoặc tâm lý giả định như sự thật"],
    ["KTD khác gì?", "Chưa xác nhận từ bằng chứng vận hành hiện hành", "Cần sự thật về trải nghiệm, không gian, con người và tiêu chuẩn"],
    ["Khách nên cảm nhận điều gì?", "Chưa xác nhận từ nguồn hiện hành", "Cần chủ thương hiệu chốt"],
    ["KTD không muốn bị hiểu thành gì?", "Không định vị bằng giá, ưu đãi, điều kiện sử dụng, lời hứa hiệu quả hoặc thông điệp kiểm chứng/chứng minh", "Ranh giới đã khóa"],
    ["Điều KTD muốn sở hữu trong tâm trí khách", "Chưa xác nhận từ nguồn hiện hành", "Không kế thừa định vị Toplink cũ"],
    ["", "", ""],
    ["CÂU CHUYỆN", "", ""],
    ["Hạng mục", "Nội dung hiện tại", "Ghi chú"],
    ["Câu chuyện lớn", "Chưa có nguồn KTD hiện hành đủ để chốt", "Không sao chép câu chuyện Toplink"],
    ["Câu chuyện hiện tại", "KTD đang đi qua Dry Run để chuẩn hóa bằng sự kiện thật, điều chỉnh thật và điều học được", "Chỉ dùng các chi tiết đã được ghi nhận"],
    ["Nhân vật", "Chưa xác nhận", "Cần nguồn về founder và đội ngũ hiện hành"],
    ["Xung đột / chuyển đổi", "Từ chuẩn bị sang sẵn sàng thông qua Dry Run và học hỏi vận hành", "Khung kể; không phải tuyên bố kết quả"],
    ["Chất liệu thực tế đang có", "Chưa có danh mục asset hiện hành", "Ghi nhận asset và quyền sử dụng trước khi đưa vào pipeline"],
    ["Tone", "Rõ ràng, bình tĩnh, gần người thật việc thật, không hứa hẹn kết quả", ""],
]


AUDIENCE_PAGE_ROWS = [
    ["KHIẾT TÂM ĐƯỜNG — NHU CẦU KHÁCH & VAI TRÒ PAGE", "", "", "", "", ""],
    ["Chỉ biến quan sát hiện hành thành sự thật. Giả thuyết phải được ghi rõ và được cập nhật bằng phản hồi thực tế.", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["NHÓM NHU CẦU", "", "", "", "", ""],
    ["Nhóm nhu cầu", "Họ đang nghĩ gì?", "Họ quan tâm gì?", "Điều khiến họ tin?", "Nội dung phù hợp", "Dấu hiệu / feedback thực tế"],
    ["Khách đang tìm hiểu KTD", "KTD là gì và đang chuẩn bị đến đâu?", "Sự rõ ràng, trải nghiệm và mức độ chuẩn bị", "Sự kiện thật, chi tiết thật và điều chỉnh thật", "Dry Run, quá trình, không gian, con người và điều học được", "Chưa có dữ liệu phản hồi hiện hành — giả thuyết cần quan sát"],
    ["", "", "", "", "", ""],
    ["VAI TRÒ PAGE", "", "", "", "", ""],
    ["Hạng mục", "Nội dung hiện tại", "", "", "", ""],
    ["Page tồn tại để làm gì?", "Biến thực tế KTD hiện hành thành nội dung hữu ích và học từ phản hồi", "", "", "", ""],
    ["Page không dùng để làm gì?", "Không dùng để công bố giá, ưu đãi, điều kiện sử dụng, claim hiệu quả, lời hứa kết quả hoặc thông điệp kiểm chứng/chứng minh", "", "", "", ""],
    ["Nội dung chính", "Thương hiệu và triết lý; không gian và trải nghiệm; con người và tiêu chuẩn; quá trình chuẩn bị; Dry Run; hậu trường; hành trình founder; dưỡng sinh đời sống có giới hạn; học hỏi vận hành", "", "", "", ""],
    ["CTA", "Theo dõi, lưu, chia sẻ, nhắn KTD hoặc liên hệ để được hướng dẫn; đặt lịch qua Inbox/Zalo chỉ khi vận hành đã sẵn sàng", "", "", "", ""],
    ["Tone", "Rõ ràng, bình tĩnh, có căn cứ từ thực tế, không hứa hẹn kết quả", "", "", "", ""],
    ["Tần suất mong muốn", "Đi theo nhịp sự kiện thật và năng lực sản xuất hiện hành; chưa khóa theo tuần", "", "", "", ""],
    ["Kênh bổ trợ", "Chưa xác nhận từ nguồn hiện hành", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["RANH GIỚI TRUYỀN THÔNG", "", "", "", "", ""],
    ["Không đăng", "Tập trung", "", "", "", ""],
    ["Giá; ưu đãi; điều kiện sử dụng; claim; lời hứa hiệu quả; nội dung kiểm chứng/chứng minh; hồ sơ pháp lý; reviewer/approval background", "Thương hiệu; không gian; con người; quá trình; trải nghiệm; Dry Run; đời sống; giá trị; câu chuyện", "", "", "", ""],
]


CONTENT_SYSTEM_ROWS = [
    ["KHIẾT TÂM ĐƯỜNG — HỆ THỐNG NỘI DUNG", "", "", "", "", "", "", "", ""],
    ["Sự kiện thật hoặc nhu cầu ghi nhận có nguồn → cơ hội nội dung → phản hồi → điều học được.", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["VÙNG NỘI DUNG", "", "", "", "", "", "", "", ""],
    ["Vùng nội dung", "Mục tiêu", "Loại câu chuyện", "Ví dụ chất liệu", "Ưu tiên hiện tại", "Ghi chú học được", "", "", ""],
    ["Dry Run & chuẩn hóa", "Biến thực hành, điều chỉnh và bài học thật thành câu chuyện hữu ích", "Sự kiện → phát hiện → đã chỉnh gì → tốt hơn ở điểm nào", "Sự kiện Dry Run đã được ghi nhận", "Cao nhất", "" ,"", "", ""],
    ["KTD đang thành hình", "Cho thấy điều đang được hoàn thiện hoặc chuẩn bị", "Chi tiết đang thành hình → ý nghĩa", "Hình ảnh và sự thật hiện hành", "Cao", "", "", "", ""],
    ["Không gian KTD", "Giải thích một chi tiết không gian qua trải nghiệm dự kiến", "Chi tiết → ý nghĩa", "Asset hiện hành có quyền sử dụng", "Chờ bằng chứng", "", "", "", ""],
    ["Con người KTD", "Cho thấy nỗ lực con người và tiêu chuẩn làm việc hiện hành", "Hậu trường → nỗ lực con người", "Tiêu chuẩn đã được chủ vận hành xác nhận", "Chờ bằng chứng", "", "", "", ""],
    ["Thân – Tâm – Trí", "Diễn đạt triết lý nhất quán", "Ý nghĩa → hành động hoặc trải nghiệm", "Cách diễn giải được chủ thương hiệu duyệt", "Chờ bằng chứng", "", "", "", ""],
    ["Dưỡng sinh đời sống", "Giáo dục đời sống có giới hạn, không hứa kết quả dịch vụ", "Một thói quen nhỏ → ý nghĩa thực hành", "Nguồn phù hợp và ngôn ngữ không claim", "Trung bình", "", "", "", ""],
    ["Founder Journey", "Nối sự kiện thật với suy ngẫm founder và giá trị thương hiệu", "Sự kiện → suy ngẫm → giá trị", "Sự kiện và lời founder có nguồn", "Chọn lọc / chờ bằng chứng", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["DRY RUN → ĐẦU VÀO NỘI DUNG", "", "", "", "", "", "", "", ""],
    ["Ngày", "Sự kiện / việc thật xảy ra", "Phát hiện", "Đã chỉnh gì", "Giá trị truyền thông", "Góc kể", "Format phù hợp", "Có đưa sang pipeline không?", "Ghi chú"],
    ["", "", "", "", "", "", "", "Chưa quyết định", "Ghi sự kiện thật tại đây; không điền từ suy đoán"],
    ["", "", "", "", "", "", "", "", ""],
    ["CÔNG THỨC KỂ", "", "", "", "", "", "", "", ""],
    ["Tên grammar", "Khi nào dùng", "Cấu trúc kể", "Ví dụ", "Lưu ý", "", "", "", ""],
    ["Trước → Vấn đề → Điều chỉnh → Tốt hơn", "Khi có phát hiện thật trong Dry Run", "Trước → vấn đề → đã chỉnh gì → điều tốt hơn có thể quan sát", "Dùng sự kiện đã ghi ở phần trên", "Không biến cải thiện quy trình thành lời hứa kết quả", "", "", "", ""],
    ["Chi tiết → Ý nghĩa", "Khi một chi tiết nhỏ thể hiện tiêu chuẩn hoặc trải nghiệm", "Chi tiết thật → vì sao chi tiết đó có ý nghĩa", "Cần hình ảnh và ngữ cảnh hiện hành", "Không suy diễn công dụng", "", "", "", ""],
    ["Hậu trường → Nỗ lực con người", "Khi có hoạt động chuẩn bị thật", "Việc hậu trường → người thực hiện → nỗ lực", "Cần xác nhận người và quyền dùng hình ảnh", "", "", "", "", ""],
    ["Sự kiện → Suy ngẫm founder → Giá trị", "Khi có lời founder được ghi nhận", "Sự kiện thật → suy ngẫm có nguồn → giá trị", "Chỉ dùng khi có nguồn trực tiếp", "Không biến founder thành chuyên gia sức khỏe", "", "", "", ""],
    ["Quy trình → Trải nghiệm", "Khi mô tả cách chuẩn bị ảnh hưởng đến trải nghiệm dự kiến", "Quy trình thật → điều khách có thể cảm nhận", "Cần sự thật vận hành", "Không claim hiệu quả", "", "", "", ""],
]


CAMPAIGN_ROWS = [
    ["KHIẾT TÂM ĐƯỜNG — CHIẾN DỊCH & LỊCH NỘI DUNG", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["Lịch đi theo trạng thái kinh doanh và sự kiện thật; ngày dự kiến không phải nguồn sự thật duy nhất.", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["BRIEF CHIẾN DỊCH HIỆN TẠI", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["Hạng mục", "Nội dung hiện tại", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["Tên chiến dịch", "KTD Dry Run — Sẵn sàng qua thực hành thật", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["Phase", "Dry Run", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["Mục tiêu", "Làm quá trình chuẩn bị trở nên dễ hiểu và học từ phản hồi của người xem", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["Câu chuyện trung tâm", "KTD đang chuẩn hóa qua sự kiện thật, điều chỉnh thật và điều học được", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["Thời gian", "Theo trạng thái Dry Run; không khóa tuần 1–4 hoặc lịch 28 ngày", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["Nội dung ưu tiên", "Dry Run & chuẩn hóa; KTD đang thành hình", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["CTA chính", "Theo dõi, lưu, chia sẻ hoặc nhắn KTD", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["Trạng thái", "Khung đang dùng — chờ sự kiện và asset hiện hành", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["PIPELINE / LỊCH NỘI DUNG", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["Ngày dự kiến", "Phase", "Chủ đề", "Góc nội dung", "Format", "Hook / ý chính", "Asset cần có", "CTA", "Trạng thái", "Ngày đăng", "Kênh", "Link bài", "Reach / Views", "Save", "Share", "Comment", "Inbox / phản hồi đáng chú ý", "Điều học được", "Ghi chú"],
    ["", "Dry Run", "Dry Run & chuẩn hóa", "Một sự kiện thật và điều chỉnh phát sinh", "Video ngắn hoặc câu chuyện ảnh", "Ghi lại điều đã xảy ra, điều phát hiện và điều đã chỉnh", "Biên bản sự kiện hiện hành và asset có quyền sử dụng", "Theo dõi hoặc lưu", "Ý tưởng", "", "Facebook Page", "", "", "", "", "", "", "", "Nhu cầu ghi nhận — chưa phải sự kiện đã xảy ra"],
    ["", "Dry Run", "KTD đang thành hình", "Một chi tiết chuẩn bị đã được xác nhận và ý nghĩa của nó", "Câu chuyện ảnh hoặc video ngắn", "Từ một chi tiết thật đến trải nghiệm dự kiến", "Hình ảnh hiện hành và ngữ cảnh đã xác nhận", "Theo dõi hoặc chia sẻ", "Ý tưởng", "", "Facebook Page", "", "", "", "", "", "", "", "Nhu cầu ghi nhận — chưa xác nhận asset"],
    ["", "Dry Run", "Con người KTD", "Một tiêu chuẩn làm việc hiện hành qua nỗ lực con người", "Video hậu trường", "Cho thấy việc chuẩn bị phía sau trải nghiệm", "Tiêu chuẩn được chủ vận hành xác nhận và asset có quyền sử dụng", "Lưu hoặc nhắn KTD", "Ý tưởng", "", "Facebook Page", "", "", "", "", "", "", "", "Nhu cầu ghi nhận — chưa xác nhận tiêu chuẩn và con người"],
]


CONTROL_ROWS = [
    ["type", "human_object", "machine_node", "sheet", "table_or_section", "binding_type", "binding", "semantic_path", "relation", "parent_node", "authority", "source_of_truth", "state_map", "version", "notes"],
    ["TABLE", "Cốt lõi thương hiệu", "ktd.brand.core", "YV_01_BRAND", "CỐT LÕI THƯƠNG HIỆU", "section_header", "section:CỐT LÕI THƯƠNG HIỆU", "ktd.brand", "", "", "HUMAN_WRITE_MACHINE_READ", "YV_01_BRAND", "", "1.0", "Không sao chép giá trị kinh doanh vào Control Plane"],
    ["TABLE", "Định vị", "ktd.brand.positioning", "YV_01_BRAND", "ĐỊNH VỊ", "section_header", "section:ĐỊNH VỊ", "ktd.brand.positioning", "belongs_to", "ktd.brand.core", "HUMAN_WRITE_MACHINE_READ", "YV_01_BRAND", "", "1.0", ""],
    ["TABLE", "Câu chuyện", "ktd.brand.narrative", "YV_01_BRAND", "CÂU CHUYỆN", "section_header", "section:CÂU CHUYỆN", "ktd.brand.narrative", "belongs_to", "ktd.brand.core", "HUMAN_WRITE_MACHINE_READ", "YV_01_BRAND", "", "1.0", ""],
    ["TABLE", "Nhóm nhu cầu", "ktd.audience.need_states", "YV_02_AUDIENCE_PAGE", "NHÓM NHU CẦU", "section_header", "section:NHÓM NHU CẦU", "ktd.audience.need_states", "informs", "ktd.content.territories", "HUMAN_WRITE_MACHINE_READ", "YV_02_AUDIENCE_PAGE", "", "1.0", ""],
    ["TABLE", "Vai trò Page", "ktd.page.role", "YV_02_AUDIENCE_PAGE", "VAI TRÒ PAGE", "section_header", "section:VAI TRÒ PAGE", "ktd.page.role", "", "", "HUMAN_WRITE_MACHINE_READ", "YV_02_AUDIENCE_PAGE", "", "1.0", ""],
    ["TABLE", "Ranh giới truyền thông", "ktd.page.boundaries", "YV_02_AUDIENCE_PAGE", "RANH GIỚI TRUYỀN THÔNG", "section_header", "section:RANH GIỚI TRUYỀN THÔNG", "ktd.page.boundaries", "constrains", "ktd.content.pipeline", "HUMAN_WRITE_MACHINE_READ", "YV_02_AUDIENCE_PAGE", "", "1.0", ""],
    ["TABLE", "Vùng nội dung", "ktd.content.territories", "YV_03_CONTENT_SYSTEM", "VÙNG NỘI DUNG", "section_header", "section:VÙNG NỘI DUNG", "ktd.content.territories", "", "", "HUMAN_WRITE_MACHINE_READ", "YV_03_CONTENT_SYSTEM", "", "1.0", ""],
    ["TABLE", "Đầu vào Dry Run", "ktd.dryrun.events", "YV_03_CONTENT_SYSTEM", "DRY RUN → ĐẦU VÀO NỘI DUNG", "section_header", "section:DRY RUN → ĐẦU VÀO NỘI DUNG", "ktd.dryrun.events", "generates", "ktd.content.pipeline", "HUMAN_WRITE_MACHINE_READ", "YV_03_CONTENT_SYSTEM", "", "1.0", ""],
    ["TABLE", "Công thức kể", "ktd.content.grammars", "YV_03_CONTENT_SYSTEM", "CÔNG THỨC KỂ", "section_header", "section:CÔNG THỨC KỂ", "ktd.content.grammars", "supports", "ktd.content.pipeline", "HUMAN_WRITE_MACHINE_READ", "YV_03_CONTENT_SYSTEM", "", "1.0", ""],
    ["TABLE", "Brief chiến dịch", "ktd.campaign.current", "YV_04_CAMPAIGN_CALENDAR", "BRIEF CHIẾN DỊCH HIỆN TẠI", "section_header", "section:BRIEF CHIẾN DỊCH HIỆN TẠI", "ktd.campaign.current", "contains", "ktd.content.pipeline", "HUMAN_WRITE_MACHINE_READ", "YV_04_CAMPAIGN_CALENDAR", "", "1.0", ""],
    ["TABLE", "Pipeline nội dung", "ktd.content.pipeline", "YV_04_CAMPAIGN_CALENDAR", "PIPELINE / LỊCH NỘI DUNG", "section_header", "section:PIPELINE / LỊCH NỘI DUNG", "ktd.content.pipeline", "", "", "HUMAN_WRITE_MACHINE_READ", "YV_04_CAMPAIGN_CALENDAR", "", "1.0", ""],
    ["FIELD", "Tên thương hiệu", "ktd.brand.name", "YV_01_BRAND", "CỐT LÕI THƯƠNG HIỆU", "label_value", "label:Tên thương hiệu", "ktd.brand.name", "belongs_to", "ktd.brand.core", "HUMAN_WRITE_MACHINE_READ", "YV_01_BRAND", "", "1.0", ""],
    ["FIELD", "Giai đoạn hiện tại", "ktd.brand.phase", "YV_01_BRAND", "CỐT LÕI THƯƠNG HIỆU", "label_value", "label:Giai đoạn hiện tại", "ktd.brand.phase", "belongs_to", "ktd.brand.core", "HUMAN_WRITE_MACHINE_READ", "YV_01_BRAND", "Đang thành hình=FORMING;Đang chuẩn hóa=STANDARDIZING;Dry Run=DRY_RUN;Sẵn sàng đón khách=READY;Đang vận hành=OPERATING", "1.0", ""],
    ["FIELD", "Sự kiện thật", "ktd.dryrun.event.description", "YV_03_CONTENT_SYSTEM", "DRY RUN → ĐẦU VÀO NỘI DUNG", "column_header", "header:Sự kiện / việc thật xảy ra", "ktd.dryrun.event.description", "belongs_to", "ktd.dryrun.events", "HUMAN_WRITE_MACHINE_READ", "YV_03_CONTENT_SYSTEM", "", "1.0", ""],
    ["FIELD", "Quyết định đưa sang pipeline", "ktd.dryrun.event.pipeline_decision", "YV_03_CONTENT_SYSTEM", "DRY RUN → ĐẦU VÀO NỘI DUNG", "column_header", "header:Có đưa sang pipeline không?", "ktd.dryrun.event.pipeline_decision", "belongs_to", "ktd.dryrun.events", "HUMAN_WRITE_MACHINE_READ", "YV_03_CONTENT_SYSTEM", "Chưa quyết định=UNDECIDED;Có=YES;Không=NO", "1.0", ""],
    ["FIELD", "Trạng thái nội dung", "ktd.content.status", "YV_04_CAMPAIGN_CALENDAR", "PIPELINE / LỊCH NỘI DUNG", "column_header", "header:Trạng thái", "ktd.content.pipeline.status", "belongs_to", "ktd.content.pipeline", "HUMAN_WRITE_MACHINE_READ", "YV_04_CAMPAIGN_CALENDAR", "Ý tưởng=IDEA;Đang chuẩn bị=PREPARING;Đang quay/chụp=CAPTURING;Đang dựng=EDITING;Sẵn sàng=READY;Đã đăng=PUBLISHED;Tạm dừng=PAUSED;Bỏ=DROPPED", "1.0", ""],
    ["FIELD", "Điều học được", "ktd.content.learning", "YV_04_CAMPAIGN_CALENDAR", "PIPELINE / LỊCH NỘI DUNG", "column_header", "header:Điều học được", "ktd.content.pipeline.learning", "belongs_to", "ktd.content.pipeline", "HUMAN_WRITE_MACHINE_READ", "YV_04_CAMPAIGN_CALENDAR", "", "1.0", ""],
    ["VIEW", "Nội dung chờ nguồn", "ktd.view.pending_evidence", "YV_04_CAMPAIGN_CALENDAR", "PIPELINE / LỊCH NỘI DUNG", "derived_filter", "filter:Ghi chú contains chưa", "ktd.views.pending_evidence", "projects", "ktd.content.pipeline", "MACHINE_DERIVED", "YV_04_CAMPAIGN_CALENDAR", "", "1.0", "Không phải nguồn sự thật độc lập"],
    ["EDGE", "Dry Run tạo cơ hội nội dung", "ktd.edge.dryrun_generates_content", "", "", "semantic", "", "ktd.edges", "generates", "ktd.dryrun.events", "MACHINE_DERIVED", "_CONTROL_PLANE", "", "1.0", ""],
]


def build_workbook_plan() -> dict:
    """Return the deterministic Vietnamese workbook plan."""
    return {
        "schema_version": "1.0",
        "language": "vi",
        "sheets": deepcopy(
            [
                {"title": "YV_01_BRAND", "rows": BRAND_ROWS},
                {"title": "YV_02_AUDIENCE_PAGE", "rows": AUDIENCE_PAGE_ROWS},
                {"title": "YV_03_CONTENT_SYSTEM", "rows": CONTENT_SYSTEM_ROWS},
                {"title": "YV_04_CAMPAIGN_CALENDAR", "rows": CAMPAIGN_ROWS},
                {"title": "_CONTROL_PLANE", "rows": CONTROL_ROWS},
            ]
        ),
    }


def _sheet_map(plan: dict) -> dict[str, dict]:
    return {sheet["title"]: sheet for sheet in plan.get("sheets", [])}


def _control_records(plan: dict) -> list[dict]:
    control = _sheet_map(plan).get(CONTROL_SHEET)
    if not control or not control.get("rows"):
        return []
    header = control["rows"][0]
    return [dict(zip(header, row, strict=True)) for row in control["rows"][1:]]


def validate_workbook_plan(plan: dict) -> list[str]:
    """Return deterministic validation errors without mutating the plan."""
    errors: list[str] = []
    sheets = _sheet_map(plan)
    expected_titles = [*HUMAN_SHEETS, CONTROL_SHEET]
    if list(sheets) != expected_titles:
        errors.append("active sheet topology must contain exactly four human sheets and _CONTROL_PLANE")

    for title in HUMAN_SHEETS:
        sheet = sheets.get(title)
        if not sheet:
            continue
        rows = sheet.get("rows", [])
        widths = {len(row) for row in rows}
        if len(widths) > 1:
            errors.append(f"{title} has inconsistent row widths")
        for row in rows:
            for value in row:
                if str(value).strip().casefold() in MACHINE_METADATA_LABELS:
                    errors.append(f"{title} exposes machine metadata: {value}")

    control = sheets.get(CONTROL_SHEET)
    if not control or not control.get("rows"):
        errors.append("_CONTROL_PLANE is missing or empty")
        return errors
    if tuple(control["rows"][0]) != CONTROL_COLUMNS:
        errors.append("_CONTROL_PLANE header does not match the interface contract")
        return errors

    seen_nodes: set[str] = set()
    for record in _control_records(plan):
        node = record["machine_node"]
        if not node:
            errors.append("_CONTROL_PLANE contains an empty machine node")
        elif node in seen_nodes:
            errors.append(f"duplicate machine node: {node}")
        seen_nodes.add(node)

        title = record["sheet"]
        if not title:
            continue
        target = sheets.get(title)
        if not target:
            errors.append(f"binding references missing sheet: {title}")
            continue
        binding = record["binding"]
        if binding.startswith("section:"):
            expected = binding.removeprefix("section:")
        elif binding.startswith("header:"):
            expected = binding.removeprefix("header:")
        elif binding.startswith("label:"):
            expected = binding.removeprefix("label:")
        elif binding.startswith("filter:"):
            continue
        else:
            errors.append(f"unsupported binding for {node}: {binding}")
            continue
        if not any(expected in row for row in target["rows"]):
            errors.append(f"binding target not found for {node}: {expected}")
    return errors


def resolve_node(plan: dict, machine_node: str) -> dict:
    """Resolve exactly one Control Plane node or fail closed."""
    matches = [row for row in _control_records(plan) if row["machine_node"] == machine_node]
    if len(matches) != 1:
        raise ValueError(f"expected one node for {machine_node}, found {len(matches)}")
    return matches[0]


def machine_write_allowed(plan: dict, machine_node: str) -> bool:
    """Permit writes only for explicitly machine-derived objects."""
    return resolve_node(plan, machine_node)["authority"] == "MACHINE_DERIVED"


def build_runtime_context(plan: dict) -> dict:
    """Build the minimum active KTD context; archived legacy policy is excluded."""
    errors = validate_workbook_plan(plan)
    if errors:
        raise ValueError("invalid workbook plan: " + "; ".join(errors))
    return {
        "brand_name": "KHIẾT TÂM ĐƯỜNG",
        "brand_short_name": "KTD",
        "business_phase": "DRY_RUN",
        "human_sheets": list(HUMAN_SHEETS),
        "control_sheet": CONTROL_SHEET,
        "content_flow": [
            "REAL_EVENT",
            "CONTENT_OPPORTUNITY",
            "STORY_ANGLE",
            "FORMAT",
            "CTA",
            "RESPONSE",
            "LEARNING",
        ],
        "canonical_authority": "HUMAN_WRITE_MACHINE_READ",
        "publication_authorized": False,
    }


def plan_fingerprint(plan: dict) -> str:
    """Return a stable SHA-256 fingerprint for the exact workbook plan."""
    payload = json.dumps(plan, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Build and validate the KTD target workbook plan")
    parser.add_argument("command", choices=("emit-plan", "validate-plan", "fingerprint"))
    args = parser.parse_args()
    plan = build_workbook_plan()
    if args.command == "emit-plan":
        print(json.dumps(plan, ensure_ascii=False))
        return 0
    if args.command == "fingerprint":
        print(plan_fingerprint(plan))
        return 0
    errors = validate_workbook_plan(plan)
    print(json.dumps({"valid": not errors, "errors": errors}, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
