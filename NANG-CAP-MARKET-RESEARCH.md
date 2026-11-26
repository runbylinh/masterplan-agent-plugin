# Báo cáo nâng cấp Agent Market Research (0.6.0)

Nhánh `nang-cap-market-research`. Đặc tả: 20 năng lực nghiệp vụ (Master Prompt "Nâng cấp hệ thống Skill cho Agent Market Research | Run By Linh").
Mục tiêu: **một lần nghiên cứu → nhiều kết quả phân tích → nhiều tài nguyên Marketing → có bằng chứng → cập nhật và tái sử dụng được.**

## 1. Rà soát trước nâng cấp và quyết định
| Thành phần trước nâng cấp (0.5.0) | Phân loại | Quyết định |
| --- | --- | --- |
| 11 skill Masterplan năm (setup, danh-gia-kenh, lead-hoi-thoai, quet-doi-thu, bao-cao-kinh-doanh, chi-phi-ads, ra-soat-thuong-hieu, review-nam, nghien-cuu-thi-truong, du-bao-xu-huong, dinh-huong-chien-luoc) + dieu-phoi, huong-dan | Giữ nguyên | Không đổi lệnh/đầu ra; được dùng làm nguồn dữ liệu nội bộ cho năng lực 01, 06, 08, 17 |
| `research` (3C 5 giai đoạn) | Nâng cấp | Thành skill điều phối theo đầu ra (năng lực 18); quy trình 3C chuyển nguyên văn sang `references/nghien-cuu/che-do-3c.md`, vẫn gọi được bằng `research 3c <chủ đề>` |
| `company-analysis`, `customer-research`, `competitor-research`, `marketing-opportunities` | Nâng cấp | Năng lực 01, 03, 04, 11 đầy đủ; giữ "Chế độ 3C" và file 01–04 cũ |
| `marketing-recommendations` | Giữ nguyên | Giao việc của chế độ 3C |
| `quet-doi-thu` và `competitor-research` | Trùng một phần | Không gộp: `quet-doi-thu` theo dõi định kỳ offer/ads; `competitor-research` nghiên cứu cạnh tranh đầy đủ, dùng lại dữ liệu `quet-doi-thu` ≤ 30 ngày |
| `nghien-cuu-thi-truong` / `du-bao-xu-huong` và năng lực 02 | Trùng một phần | Tách ranh giới: hai skill năm theo bộ mẫu Masterplan; `xu-huong-mua-vu` cho xu hướng/mùa vụ hiện tại theo tháng/quý/dịp |
| Lưu kết quả rời rạc theo từng báo cáo | Điều chỉnh kết nối | Kho dữ liệu chung 3 lớp có mã và liên kết; báo cáo dựng lại từ kho |
| 2 subagent 3C | Nâng cấp + bổ sung | Thêm chế độ kho; thêm `market-researcher`, `content-researcher`, `research-verifier` (không trùng chức năng) |
| Năng lực 05–10, 12–17, 19, 20 | Bổ sung | 15 skill mới |

## 2. Sơ đồ kiến trúc
```
Yêu cầu tự nhiên ──► research (18) ── Research Brief RP · workflow 01–09 · mức Nhanh/Chuyên sâu/Cập nhật
                        │
        ┌───────────────┼──────────────────────────────────────────────┐
        ▼  Nhóm A — thu thập (subagent chạy song song)                  │
  01 company-analysis   02 xu-huong-mua-vu   03 customer-research       │  kiem-chung (19)
  04 competitor-research 05 tu-khoa  06 nghien-cuu-content              │  xuyên suốt,
  07 format-sang-tao    08 quang-cao-chuyen-doi  09 kenh-cong-dong       │  research-verifier
        │  ghi EVD · MAU · FIND · bản ghi lớp 2                         │
        ▼                                                               │
  ┌──────────── KHO (20) kho-du-lieu · scripts/kho.py ─────────────────┤
  │ Lớp 1 gốc: EVD, MAU                                                 │
  │ Lớp 2 phân tích: FIND, DN, TT, XH, MV, BD, RR, KH, SEG, HT, DV, UD, │
  │                  TN, KT, KEY, CNT, QC, LP, INS, OPP, GT, MT, TH     │
  │ Lớp 3 tài nguyên: OFFER, TD, IDEA, FMT, ADS, CAM, CRO, KEN          │
  └─────────────────────────────────────────────────────────────────────┘
        ▼  Nhóm B — chuyển hoá (đọc kho, không thu thập lại)
  10 insight → 11 marketing-opportunities → 12 san-pham-uu-dai · 13 dinh-vi-thong-diep
  · 14 y-tuong-content · 15 y-tuong-quang-cao · 16 y-tuong-chien-dich · 17 toi-uu-chuyen-doi
        ▼  Bàn giao
  Masterplan (dinh-huong-chien-luoc, nghien-cuu-thi-truong) · content-agent · design-agent · video-edit · Ads · Sales/CRM
```

## 3. Liên kết dữ liệu
```
EVD-001 bằng chứng gốc ─┐
EVD-002 ────────────────┼─► FIND-001 phát hiện (Mẫu lặp) ─┐
KH-002 rào cản ─────────┘                                  ├─► INS-001 Insight ─► OPP-001 cơ hội ─┬─► OFFER-001 combo
KEY-001 từ khóa ───────────────────────────────────────────┘                                      ├─► IDEA-001 Content
                                                                                                   ├─► ADS-001 quảng cáo
                                                                                                   └─► CAM-001 chiến dịch
```
`kho.py truy-vet CAM-001` in toàn bộ cây phía trên và số nguồn độc lập. Một tài nguyên có thể liên kết nhiều Insight/bằng chứng;
không bắt buộc đi qua mọi tầng, nhưng phải truy được về bằng chứng gốc (kiem-tra cảnh báo nếu không).

## 4. Workflow và lệnh
| # | Workflow | Ví dụ lệnh |
| --- | --- | --- |
| 01 | Nghiên cứu toàn diện phục vụ chiến lược | `/masterplan-agent:research xây đầu vào Masterplan 2027` |
| 02 | Chiến dịch theo mùa vụ | `/masterplan-agent:research tìm cơ hội Marketing dịp Tết` |
| 03 | Content Marketing | `/masterplan-agent:research 30 ý tưởng Content dựa trên nghiên cứu` |
| 04 | Quảng cáo | `/masterplan-agent:research nghiên cứu quảng cáo, đề xuất góc mới` |
| 05 | Phát triển sản phẩm | `/masterplan-agent:research ý tưởng combo sản phẩm` |
| 06 | Tối ưu chuyển đổi | `/masterplan-agent:research vì sao khách chưa mua` |
| 07 | Phát triển kênh | `/masterplan-agent:research tìm kênh tiếp cận khách hàng` |
| 08 | Cập nhật thị trường | `/masterplan-agent:research cập nhật thị trường tháng này` |
| 09 | Kiểm chứng Insight và ý tưởng | `/masterplan-agent:kiem-chung INS-003 OPP-002` |
| 3C | Chế độ cũ | `/masterplan-agent:research 3c mùa lễ cuối năm` |
| — | Tiếp tục đợt dở | `/masterplan-agent:research tiep-tuc RP-004` |
Mỗi skill cũng gọi được lẻ: `/masterplan-agent:<tên-skill>`.

## 5. Kho dữ liệu và biểu mẫu
| File | Nội dung |
| --- | --- |
| `templates/kho/schema.json` | 34 loại bản ghi: trường bắt buộc, giá trị cho phép, cha bắt buộc, hạn dùng, khoá chống trùng |
| `scripts/kho.py` | `khoi-tao`, `them`, `cap-nhat`, `duyet`, `kiem-chung`, `tim`, `truy-vet`, `kiem-tra`, `thong-ke`, `xuat`, `bao-cao`, `thay-doi`, `tien-do` |
| `templates/kho/vi-du-secondhand.json` | Chuỗi ví dụ đầy đủ (giả định) RP → … → CAM |
| `templates/kho/vi-du/<skill>.json` | Ví dụ lô tự đủ cho từng skill, nhiều ngành (giả định) |
| `references/kho-du-lieu.md` | Cấu trúc 3 lớp, thuộc tính chung, lệnh, quy tắc lưu trữ, Sheets/Notion |
| `references/nghien-cuu/` | `quy-tac-nghien-cuu.md` (lấy mẫu, phân loại phát hiện, độ tin cậy, kiểm chứng), `workflow.md`, `mau-skill.md`, `che-do-3c.md` |
| `references/nen-tang/` | Google Search, Google Trends, TikTok, Facebook, Threads, YouTube, Instagram, Meta Ads Library, TikTok Creative Center, Google Maps, Website/landing page, sàn TMĐT, CRM/nội bộ |

## 6. Yêu cầu công cụ và quyền
| Công cụ | Dùng cho | Bắt buộc? |
| --- | --- | --- |
| Python 3 (+ openpyxl để xuất .xlsx) | `kho.py`, script báo cáo | Có (openpyxl tuỳ chọn) |
| WebSearch | Google Search, nguồn chính thống | Nên có |
| Claude in Chrome | TikTok, Facebook, Threads, YouTube, Instagram, Google Maps, Trends, Ads Library, sàn, landing page, trang quản trị | Nên có |
| Connector Meta Ads, TikTok for Business, LadiPage | Dữ liệu quảng cáo/lead nội bộ | Tuỳ chọn |
| Google Drive, Google Sheets, Notion | Đọc tài liệu nội bộ; xuất kho khi được phép | Tuỳ chọn |
Thiếu công cụ nào, skill ghi vào Brief và kho (TH) và dùng nguồn thay thế; không giả định đã có.

## 7. Danh sách skill Market Research sau nâng cấp
Mỗi skill có 8 phần A–H (mục tiêu, kích hoạt, đầu vào, phương pháp, quy trình dạng bảng Bước → Hành động → Dữ liệu → Kết quả → Điều kiện,
đầu ra kèm ví dụ bản ghi, bàn giao, checklist). Ví dụ lô tự đủ cho từng skill: `templates/kho/vi-du/<skill>.json` (dữ liệu giả định).
| # | Skill | Đầu vào chính | Quy trình (tóm tắt) | Đầu ra (kho) |
| --- | --- | --- | --- | --- |
| 01 | `company-analysis` | company-context, CRM, báo cáo bán hàng, kết quả review-nam / bao-cao-kinh-doanh / chi-phi-ads / danh-gia-kenh / lead-hoi-thoai | Kiểm kê dữ liệu → chuẩn hoá → đóng góp doanh thu, chi phí → so giai đoạn → vấn đề, lợi thế, giới hạn | DN (6 bảng), EVD, MAU, FIND; chế độ 3C `01-brief.md` |
| 02 | `xu-huong-mua-vu` | Ngành, địa bàn, thời gian; Trends, báo cáo, Social, sàn, doanh thu theo tháng | Bộ từ khóa 5 lớp → nguồn chính thống + tín hiệu → so cùng kỳ → phân loại xu hướng → nguyên nhân + phản bác → khai thác/thử nghiệm/chưa phù hợp | TT, XH, MV, BD, RR, OPP (Mùa vụ, nháp) |
| 03 | `customer-research` | Nhóm khách; CRM, inbox, review, hội nhóm, bình luận, từ khóa | Phân biệt loại khách → trích phát biểu → gắn 10 nhãn → đếm, loại trùng → phân khúc theo nhu cầu, hành vi → hành trình | KH (kho theo nhãn), SEG, HT; chế độ 3C `02-customer.md` |
| 04 | `competitor-research` | Tiêu chí chọn đơn vị; website, Social, Ads Library, Maps, sàn, quet-doi-thu | Phân loại trực tiếp/gián tiếp/thay thế → thu cùng cấu trúc → so sánh → đối chiếu phản hồi → khoảng trống có thật trong mẫu | DV, UD, TN, KT, ma trận cạnh tranh; chế độ 3C `03-competitor.md` |
| 05 | `tu-khoa` | Từ khóa gốc; Google, Trends, Keyword Planner, TikTok/Facebook/YouTube/sàn Search | Mở rộng → chuẩn hoá, gộp biến thể → nhóm chủ đề, mục đích, giai đoạn → ưu tiên → hướng khai thác theo nền tảng | KEY |
| 06 | `nghien-cuu-content` | Nhóm khách, mục tiêu; kênh đơn vị cùng ngành, Creator, ngành khác, nội bộ | Mẫu 3 mức tương tác → bóc Hook, góc, thông điệp, cấu trúc, CTA → phản hồi → công thức lặp → hướng ứng dụng | CNT, FIND |
| 07 | `format-sang-tao` | CNT/QC; video, ảnh, carousel, banner | Bóc phân đoạn (chỉ điều quan sát được) → so cấu trúc → tách tái sử dụng / phụ thuộc ngữ cảnh → công thức | FMT (Video, Hình ảnh) |
| 08 | `quang-cao-chuyen-doi` | Sản phẩm, mục tiêu chuyển đổi; Ads Library, Creative Center, landing page, ads nội bộ, CRM | Thu mẫu → phân loại → bóc Hook, lợi ích, bằng chứng, ưu đãi, CTA → nhất quán ads–landing → góc ít khai thác → giả thuyết | QC, LP, GT |
| 09 | `kenh-cong-dong` | SEG; nền tảng, hội nhóm, Creator, kênh vệ tinh, kênh bán | Nơi khách xuất hiện → danh sách → chất lượng tương tác → mức phù hợp có lý do → vai trò → cách tiếp cận, cần xác minh | KEN (6 bảng) |
| 10 | `insight` | KH, FIND, SEG, KEY, CNT, QC | Mã hoá mở → gom cụm → bối cảnh, mong muốn, động lực, rào cản, mâu thuẫn → phản bác → viết Insight | INS |
| 11 | `marketing-opportunities` | Kho nhóm A + INS | Nhu cầu chưa đáp ứng → khoảng trống → lợi thế → giả thuyết → đánh giá 4 mặt (Cao/TB/Thấp có lý do) → ưu tiên → thử nghiệm | OPP; chế độ 3C `04-tong-hop-3c.md` |
| 12 | `san-pham-uu-dai` | KH, INS, DN, DV/UD/KT, OPP | Nhu cầu → sản phẩm hiện có → cải tiến/kết hợp/đóng gói → phương án → định vị, kinh tế → thử nghiệm | OFFER (6 loại) |
| 13 | `dinh-vi-thong-diep` | SEG, INS, DV/TN/KT, DN | Khách ưu tiên → lợi ích → đối thủ nói gì → khác biệt chứng minh được → 2–3 phương án → thông điệp theo nhóm, hành trình | TD (5 bảng) |
| 14 | `y-tuong-content` | SEG, INS, KEY, XH, CNT, FMT, TD | Pillar → chủ đề → nhiều góc → Hook, format → nền tảng → kiểm trùng (Chủ đề + Góc) | IDEA (+ `kho.py nhom` dựng hệ thống Pillar) |
| 15 | `y-tuong-quang-cao` | INS, KH, TD, OFFER, QC, ads nội bộ | Yếu tố tác động → góc → Hook, thông điệp, bằng chứng, CTA → concept → biến thể → giả thuyết, chỉ số | ADS |
| 16 | `y-tuong-chien-dich` | DN, XH, MV, INS, OPP, OFFER, KEN | Cơ hội, thời điểm → ý tưởng chủ đạo → hoạt động thu hút/tương tác/nuôi dưỡng/chuyển đổi có lý do → kênh → so 2–3 phương án | CAM |
| 17 | `toi-uu-chuyen-doi` | HT, KH, CRM, ads, LP | Điểm chuyển đổi → số thực tế → điểm nghẽn → đối chiếu rào cản → giả thuyết → đề xuất → ưu tiên | CRO (7 bảng) |
| 18 | `research` | Yêu cầu tự nhiên, company-context, kho | Đầu ra → workflow, mức → đọc kho → Brief → nhóm A song song → kiểm chứng → nhóm B → báo cáo | RP, báo cáo đợt, file xuất |
| 19 | `kiem-chung` | Mã bản ghi / đợt | Tồn tại, phạm vi, dẫn lại, nguồn độc lập, phản bác, thiên lệch, dữ liệu – kết luận → phân loại có lý do | Trạng thái kết luận, MT, TH, GT |
| 20 | `kho-du-lieu` | Kho | Đọc → tái sử dụng → chuẩn hoá → chống trùng → liên kết → lịch sử → lỗi thời → so sánh → xuất | Kho 3 lớp, báo cáo thay đổi, file xuất |
Giao việc theo chế độ 3C: `marketing-recommendations` (giữ nguyên).

## 8. Kết quả kiểm thử thực tế
Chạy: `python3 -m unittest discover -s tests -v` (Python 3.9, macOS) — **31/31 đạt**. `claude plugin validate .` — đạt.
| Bộ | Loại kiểm thử | Nội dung | Kết quả |
| --- | --- | --- | --- |
| `tests/test_kho.py` (13) | Kiểm thử đơn vị | Cấp mã, liên kết tạm, chống trùng, thiếu trường/giá trị sai, thiếu cha, liên kết hỏng, chặn email/SĐT, ngưỡng "Có căn cứ" 2 nguồn độc lập, không ghi đè bản đã duyệt, tin cậy cần lý do, lỗi thời, truy vết/xuất/báo cáo, tiến độ/thay đổi | Đạt |
| `tests/test_cau_truc.py` (9) | Kiểm thử cấu trúc | Frontmatter mọi skill; 20 skill nghiên cứu đủ A–H, quy trình bảng, checklist; 5 subagent; mọi đường dẫn `${CLAUDE_PLUGIN_ROOT}` tồn tại; 13 tài liệu nền tảng; schema nhất quán; **mọi ví dụ (17 file: chuỗi secondhand + 16 ví dụ theo skill) nạp sạch vào kho**; phiên bản khớp; không dữ liệu nhạy cảm | Đạt |
| `tests/test_luong.py` (9) | Kiểm thử mô phỏng | Case 01 F&B Tết · 02 Thời trang · 03 Đào tạo · 04 Quảng cáo · 05 Cập nhật thị trường · 06 Thiếu dữ liệu · 07 Mâu thuẫn · 08 Tái sử dụng kho · 09 Tương thích ngược (script cũ, 19 skill cũ, 5 file 3C) | Đạt |
**Chưa kiểm thử trực tiếp** bằng công cụ thật (Claude in Chrome trên TikTok/Meta Ads Library/Google Trends..., connector, kích hoạt skill bằng câu
nói tự nhiên trong phiên Claude Code). Kiểm thử trên là cấu trúc và mô phỏng dữ liệu; chưa tuyên bố skill chạy đúng trên nền tảng thật.

## 9. Chưa hoàn thiện và lý do
| Hạng mục | Tình trạng | Lý do / hướng xử lý |
| --- | --- | --- |
| Chạy thử trực tiếp từng workflow trên dữ liệu thật | Chưa làm | Cần Chrome đăng nhập, connector và người dùng duyệt từng điểm DỪNG; đề xuất chạy thử workflow 03 hoặc 02 trên Run By Linh sau khi gộp |
| Ma trận cạnh tranh, bản đồ định vị | Agent tự dựng trong báo cáo từ DV | `kho.py` chưa có lệnh dựng ma trận tự động |
| Đồng bộ trực tiếp Google Sheets / Notion | Qua xuất CSV/XLSX + hỏi người dùng | Tránh tạo file ngoài khi chưa được phép; chưa viết script đồng bộ hai chiều |
| Đường dẫn chi tiết một số nền tảng (Threads search, TikTok Creative Center thị trường VN, tham số Meta Ads Library) | Viết theo cấu trúc đã biết | Cần mở trang thật để xác nhận; tài liệu đã dặn kiểm tra và ghi lại |
| "Mức độ phù hợp" (KEN), "Loại căn cứ" (CRO) | Chữ tự do "Cao — lý do" | Giữ lý do trong cùng ô; chưa ép danh sách giá trị để không làm hỏng dữ liệu cũ |
| Lệnh cài trong tài liệu dùng tên repo cũ | GitHub tự chuyển hướng | Chờ người dùng quyết đổi sang `researchmasterplan-agent-plugin` |
