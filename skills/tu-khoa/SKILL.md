---
name: tu-khoa
description: Nghiên cứu từ khóa và nhu cầu tìm kiếm — xây từ khóa gốc theo ngành, sản phẩm, vấn đề, nhu cầu, tình huống; mở rộng bằng gợi ý tự động và câu hỏi liên quan trên Google Search, Google Trends, Keyword Planner (nếu được cấp quyền), TikTok Search, Facebook Search, YouTube Search và ô tìm kiếm trên sàn; chuẩn hoá, loại trùng, gom biến thể cùng nghĩa, nhóm chủ đề và mục đích tìm kiếm, phân loại theo hành trình (nhận biết vấn đề, tìm giải pháp, so sánh, cân nhắc mua, sau mua), ghi xu hướng, mùa vụ, mức quan tâm chỉ khi có dữ liệu thật, chấm mức phù hợp với sản phẩm và khách, đề xuất hướng khai thác theo nền tảng. Ghi kho KEY kèm EVD, MAU, FIND. Không suy lượng tìm kiếm từ lượt xem, hashtag hay gợi ý. Dùng khi người dùng gõ /masterplan-agent:tu-khoa, nói "nghiên cứu từ khóa", "khách tìm gì trên Google/TikTok", "bộ từ khóa cho SEO", "từ khóa chạy quảng cáo tìm kiếm", "câu hỏi khách hay tìm", "làm FAQ", "chủ đề video giải đáp".
argument-hint: "[ngành/sản phẩm] [--nen-tang google,tiktok,youtube,facebook,san] [--dot RP-xxx]"
---

# /masterplan-agent:tu-khoa

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`.
Cách thu theo nền tảng trong `${CLAUDE_PLUGIN_ROOT}/references/nen-tang/`: `google-search.md` (gợi ý, "Mọi người cũng hỏi", tìm kiếm liên quan,
Keyword Planner), `google-trends.md`, `tiktok.md`, `facebook.md`, `youtube.md`, `san-tmdt.md`. Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`.

## A. Mục tiêu
Biết khách **dùng chữ gì, hỏi câu gì, ở nền tảng nào và ở giai đoạn nào** của hành trình mua, để nội dung và quảng cáo xuất hiện đúng lúc khách
đang tìm. Phục vụ quyết định: SEO website, SEO Social, Content Pillar, video giải đáp, FAQ, nhóm từ khóa quảng cáo tìm kiếm, nội dung landing page.

## B. Điều kiện kích hoạt
- **Dùng khi**: workflow 03, 07; người dùng cần bộ từ khóa, câu hỏi khách tìm, chủ đề SEO/video giải đáp, từ khóa quảng cáo tìm kiếm.
- **Không dùng khi**: cần biết xu hướng/mùa vụ của cả thị trường → `xu-huong-mua-vu` (skill đó đọc lại KEY); cần phát biểu và rào cản của khách
  → `customer-research`; cần mổ Content đối thủ → `nghien-cuu-content`.
- **Chạy độc lập** được. Tốt hơn khi có DN (sản phẩm), KH nhãn Câu hỏi/Ngôn ngữ khách hàng (từ gốc lấy từ lời khách).

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Ngành, sản phẩm, địa bàn, ngôn ngữ; nền tảng cần nghiên cứu (mặc định Google + TikTok + YouTube + sàn nếu bán trên sàn); mã RP |
| Tuỳ chọn | Danh sách từ khóa doanh nghiệp đang dùng; nhóm khách ưu tiên; mục đích (SEO, quảng cáo, Content) |
| Dữ liệu nội bộ | Google Search Console, Keyword Planner, báo cáo từ khóa Google Ads, từ khóa tìm kiếm trong website/sàn — chỉ khi người dùng cấp quyền |
| Kế thừa | `kho.py tim --loai KEY --chu "<sản phẩm>"` (không thu lại KEY còn hạn); `kho.py tim --loai KH --chu "Câu hỏi"`; `kho.py tim --loai XH MV` |
| Khi thiếu | Không có Keyword Planner/Search Console → `Chỉ số quan tâm` = "Không có số (chỉ ghi nhận gợi ý tự động)", ghi TH nếu quyết định cần số |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Từ khóa gốc | 5 nhóm: ngành · sản phẩm · vấn đề (khách gặp gì) · nhu cầu (khách muốn gì) · tình huống (dịp, đối tượng, địa điểm). Lấy chữ từ KH Ngôn ngữ khách hàng trước, chữ của doanh nghiệp sau |
| Mở rộng | Gợi ý tự động (gõ gốc + từng chữ cái a–z, + "cho", "có", "nên", "giá", "ở đâu"), "Mọi người cũng hỏi", tìm kiếm liên quan, gợi ý ô tìm kiếm TikTok/YouTube/Facebook/sàn. Ghi ngày, địa bàn, chế độ đăng xuất/ẩn danh nếu có |
| Chọn và thu mẫu | Phạm vi khởi tạo 30–50 cụm sau loại trùng; mỗi nền tảng một MAU; đủ 5 giai đoạn hành trình (giai đoạn trống ghi rõ) |
| Chuẩn hoá | Viết thường, bỏ dấu câu thừa, giữ dấu tiếng Việt; gom biến thể cùng nghĩa (không dấu, đảo trật tự, viết tắt, số ít/nhiều) vào `Biến thể` của một KEY; khác ý định thì tách KEY |
| Nhóm | `Nhóm chủ đề` theo vấn đề/sản phẩm; `Mục đích tìm kiếm`: Thông tin · So sánh · Giao dịch · Điều hướng · Sau mua |
| Hành trình | `Giai đoạn hành trình`: Nhận biết vấn đề · Tìm giải pháp · So sánh · Cân nhắc mua · Sau mua. Dấu hiệu: "là gì, vì sao" → Nhận biết; "cách, nên" → Tìm giải pháp; "so sánh, hay, loại nào" → So sánh; "giá, mua ở đâu, review" → Cân nhắc mua; "cách dùng, bảo hành" → Sau mua |
| Chỉ số | Chỉ ghi số thực sự truy cập được: Keyword Planner (khoảng lượng tìm kiếm tháng), Search Console (lượt hiển thị), Trends (chỉ số tương đối 0–100). Luôn ghi `Đơn vị, địa bàn, thời gian đo` |
| Cấm | Suy lượng tìm kiếm từ lượt xem video, số bài theo hashtag, thứ tự gợi ý; coi Trends là lượng tuyệt đối; gộp số của hai nền tảng |
| Mùa vụ | `Tính mùa vụ` chỉ khi Trends ≥ 2 năm lặp cùng thời điểm hoặc có MV; còn lại "Chưa xác định" |
| Ưu tiên | Cao: khớp sản phẩm + nhóm khách ưu tiên + (có chỉ số quan tâm hoặc xuất hiện ≥ 2 nền tảng). Trung bình: khớp nhưng một nền tảng. Thấp: lệch sản phẩm hoặc chỉ điều hướng tới thương hiệu khác. Luôn ghi `Lý do ưu tiên` |
| Kiểm chứng | Mở trang kết quả của từ khóa ưu tiên Cao để xác nhận ý định (kết quả là bài hướng dẫn, trang bán hay video?) — ghi vào EVD |
| Mâu thuẫn | Gợi ý nhiều nhưng Keyword Planner rất thấp (hoặc ngược lại) → ghi cả hai, không chọn một; ghi MT nếu ảnh hưởng ưu tiên |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 1 | Lập từ khóa gốc 5 nhóm; đọc KEY, KH cũ | DN, KH, KEY | 10–20 từ gốc | **DỪNG**: người dùng duyệt từ gốc và nền tảng |
| 2 | Mở rộng bằng gợi ý tự động và câu hỏi liên quan | Google Search, ô tìm kiếm nền tảng | Danh sách thô + EVD ảnh chụp/ghi chép | — |
| 3 | Thu theo từng nền tảng | Google, TikTok, YouTube, Facebook, sàn, Keyword Planner | EVD + MAU mỗi nền tảng | Đạt phạm vi khởi tạo hoặc bão hoà |
| 4 | Chuẩn hoá, loại trùng, gom biến thể cùng nghĩa | Danh sách thô | Danh sách sạch (số thô → số sạch ghi MAU) | — |
| 5 | Nhóm chủ đề và mục đích tìm kiếm | Danh sách sạch | KEY nháp | Mọi KEY có giá trị hợp lệ |
| 6 | Phân loại giai đoạn hành trình | KEY | Giai đoạn | Ghi giai đoạn còn trống |
| 7 | Xu hướng, mùa vụ, mức quan tâm (chỉ khi có dữ liệu) | Trends, Planner, MV | Chỉ số + đơn vị/địa bàn/thời gian | Không có số nào bị suy diễn |
| 8 | Chấm mức phù hợp với sản phẩm và khách; ưu tiên + lý do | DN, SEG | Mức ưu tiên | — |
| 9 | Hướng khai thác theo nền tảng; FIND tổng hợp (giai đoạn nào nhiều câu hỏi, nền tảng nào khác biệt); ghi kho `kho.py them lo-key.json --dot RP-xxx` → `kiem-tra` | KEY | KEY hoàn chỉnh, FIND; báo cáo `kho.py bao-cao --dot RP-xxx --loai KEY FIND` | Không LỖI; **DỪNG** chờ duyệt |

## F. Đầu ra — kho `KEY`
Trường bắt buộc: Từ khóa (gốc) · Nhóm chủ đề · Nhu cầu · Mục đích tìm kiếm · Giai đoạn hành trình · Nền tảng · Chỉ số quan tâm · Tính mùa vụ ·
Nhóm khách hàng · Mức ưu tiên · Lý do ưu tiên · Hướng ứng dụng · Nguồn. Tuỳ chọn: `Biến thể` (danh sách), `Đơn vị, địa bàn, thời gian đo`.
Mã tự cấp `KEY-xxx`; khoá chống trùng = Từ khóa + Nền tảng (cùng từ ở hai nền tảng là hai KEY). Liên kết EVD của trang/ảnh gợi ý.
`Hướng ứng dụng` chọn trong: SEO website · SEO Social · Content Pillar · video giải đáp · FAQ · nhóm từ khóa quảng cáo tìm kiếm · nội dung landing page.
Xuất bảng: `kho.py xuat --ra nghien-cuu/<thư mục đợt>/xuat --xlsx --dot RP-xxx`. Ví dụ lô đầy đủ (giả định, nội thất căn hộ nhỏ):
`${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/tu-khoa.json`.
```json
{"loai": "KEY", "tieu_de": "sofa cho phòng khách nhỏ", "lien_ket": ["@e1", "@e2"],
 "du_lieu": {"Từ khóa": "sofa cho phòng khách nhỏ", "Biến thể": ["sofa phòng khách nhỏ", "sofa nhỏ gọn chung cư"], "Nhóm chủ đề": "Sofa",
   "Nhu cầu": "Chọn sofa vừa diện tích căn hộ", "Mục đích tìm kiếm": "So sánh", "Giai đoạn hành trình": "So sánh", "Nền tảng": "Google Search",
   "Chỉ số quan tâm": "1.000–10.000 lượt/tháng", "Đơn vị, địa bàn, thời gian đo": "Keyword Planner, Việt Nam, 11/2025–10/2026",
   "Tính mùa vụ": "Chưa xác định", "Nhóm khách hàng": "Cặp đôi mới nhận căn hộ", "Mức ưu tiên": "Cao",
   "Lý do ưu tiên": "Khớp dòng sofa 1m6, có số tìm kiếm, xuất hiện cả YouTube", "Hướng ứng dụng": "SEO website, nội dung landing page",
   "Nguồn": "Google Keyword Planner (tài khoản doanh nghiệp)"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| Kho KEY (+ EVD, MAU, FIND, TH, MT); file xuất xlsx | `y-tuong-content` (chủ đề, Hook theo câu hỏi), `insight` (KEY làm bằng chứng nhu cầu), `toi-uu-chuyen-doi` (FAQ, landing page), `y-tuong-quang-cao` (nhóm từ khóa quảng cáo tìm kiếm), `kenh-cong-dong` (nền tảng khách tìm), `xu-huong-mua-vu` (từ khóa mùa vụ), `customer-research` (câu hỏi làm đầu mối thu phát biểu) | SEO website, SEO Social, Content Pillar, video giải đáp, FAQ, quảng cáo tìm kiếm, landing page | Hạn dùng 120 ngày; lần sau chỉ chạy lại bước 3 và 7 cho KEY ưu tiên Cao, cập nhật chỉ số bằng `kho.py cap-nhat`, thêm KEY mới |

**Hướng khai thác theo nền tảng** (ghi vào `Hướng ứng dụng`, báo cáo gom thành bảng):
| Nền tảng của KEY | Khai thác chính | Ghi chú |
| --- | --- | --- |
| Google Search | SEO website (bài hướng dẫn, trang danh mục), FAQ, nhóm từ khóa quảng cáo tìm kiếm | Mục đích Giao dịch/Cân nhắc mua → landing page; Thông tin → bài hướng dẫn |
| YouTube Search | Video giải đáp dài, video so sánh | Tiêu đề chứa nguyên cụm từ khóa |
| TikTok Search | SEO Social: chữ trên video, caption, lời nói có cụm từ khóa; series theo Content Pillar | Ưu tiên giai đoạn Nhận biết vấn đề, Tìm giải pháp |
| Facebook Search / hội nhóm | Bài giải đáp trong cộng đồng, FAQ cho tư vấn Inbox | Câu hỏi lặp → kịch bản tư vấn |
| Ô tìm kiếm sàn | Tên sản phẩm, thuộc tính, mô tả gian hàng | Chỉ dùng chữ khách thực sự gõ |
Gom KEY theo `Nhóm chủ đề` × `Giai đoạn hành trình` để đề xuất Content Pillar; KEY Cân nhắc mua + Giao dịch của Google là ứng viên nhóm quảng cáo tìm kiếm.

## H. Kiểm tra chất lượng
- [ ] Từ khóa gốc phủ đủ 5 nhóm; KEY phủ đủ 5 giai đoạn hành trình hoặc ghi rõ giai đoạn trống.
- [ ] Biến thể cùng nghĩa đã gom; khác ý định đã tách.
- [ ] Mỗi chỉ số có nguồn, đơn vị, địa bàn, thời gian đo; không có lượng tìm kiếm suy từ view, hashtag, gợi ý.
- [ ] `Tính mùa vụ` chỉ ghi khi có dữ liệu lặp; còn lại "Chưa xác định".
- [ ] Mỗi KEY có mức ưu tiên + lý do và hướng ứng dụng cụ thể theo nền tảng.
- [ ] Mỗi nền tảng có MAU (thu thập / đọc được / sử dụng); `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi có 30–50 KEY (hoặc bão hoà) đã phân nhóm, hành trình và ưu tiên, kèm bảng hướng khai thác theo nền tảng được người dùng duyệt.
