# Agent Masterplan Marketing (masterplan-agent)

Plugin Claude Code của Run By Linh. Agent tự nghiên cứu kênh, lead, đối thủ, số kinh doanh và chi phí quảng cáo
để làm đầu vào cho **Marketing Masterplan** và **kế hoạch quý, tháng**. Mọi con số có nguồn và ngày lấy.
Sau mỗi bước, agent **dừng chờ bạn duyệt**.

## Cài đặt
```bash
claude plugin marketplace add runbylinh/masterplan-agent-plugin
claude plugin install masterplan-agent@rbl-masterplan-dev
```
Cài thêm thư viện đọc Excel: `python3 -m pip install openpyxl`. Sau khi cài, mở phiên Claude Code mới (hoặc chạy `/reload-plugins`).

**Cài lần đầu:** [CAI-DAT-LAN-DAU.md](CAI-DAT-LAN-DAU.md) — 14 bước có kiểm tra.
**Hướng dẫn đầy đủ** (chuẩn bị, kết nối Chrome/Meta/TikTok/LadiPage/Drive/Sheets, thao tác từng lệnh, lỗi thường gặp):
[HUONG-DAN.md](HUONG-DAN.md). Trong Claude Code gõ `/masterplan-agent:huong-dan` để agent tự kiểm tra máy và chỉ bước còn thiếu.

## Bắt đầu
Mở Claude Code trong một thư mục làm việc riêng cho doanh nghiệp (ví dụ `masterplan-brand/`), rồi gõ:
```
/masterplan-agent:setup
```
Agent hỏi thông tin doanh nghiệp (tạo `company-context.md`), kênh, đối thủ, tài khoản quảng cáo, hộp thư, thư mục báo cáo,
rồi tạo `cau-hinh.json`. Sau đó gõ `/masterplan-agent:dieu-phoi` để agent đọc trạng thái và đề xuất chạy gì tiếp.

## Quy trình 4 phần
```
1 Review doanh nghiệp  →  2 Market Research  →  3 Dự báo xu hướng  →  4 Định hướng chiến lược  →  Masterplan (sau)
   Marketing Audit         ngành · khách · đơn vị    tín hiệu · dự báo        2–3 cơ hội → 1 hướng đi
```

## Các skill
| Phần | Lệnh | Việc | Nguồn số |
| --- | --- | --- | --- |
| – | `/masterplan-agent:huong-dan` | Kiểm tra cài đặt, giải thích cách dùng, xử lý lỗi | Máy, connector |
| – | `/masterplan-agent:dieu-phoi` | Đọc trạng thái, chọn skill, chạy đúng thứ tự, không chạy lại phần còn dùng được | Thư mục làm việc |
| 0 | `/masterplan-agent:setup` | Khai báo doanh nghiệp (`company-context.md`), kênh, đối thủ, nguồn số | — |
| 1 | `/masterplan-agent:danh-gia-kenh [kỳ]` | Đánh giá Page, Group, TikTok, IG, Threads, YouTube, Zalo OA theo vai trò trong phễu, so kỳ trước và đối thủ, kết luận Giữ / Đẩy mạnh / Tối ưu / Bỏ | Chrome (Business Suite, TikTok Studio...), file xuất, Meta Ads, LadiPage |
| 1 | `/masterplan-agent:lead-hoi-thoai [kỳ]` | Số hội thoại, tốc độ phản hồi, chất lượng lead, tỷ lệ chốt, lý do mua / chưa mua, câu hỏi lặp lại | Chrome: Messenger fanpage, Instagram, Zalo cá nhân bản web, Zalo OA, TikTok tin nhắn web, TikTok Shop/Shopee chat; nhãn hộp thư; file đơn / LadiWork |
| 1 | `/masterplan-agent:ra-soat-thuong-hieu` | Thương hiệu và Website như khách thấy; bình luận, đánh giá Google Maps, sàn | Chrome, trang công khai |
| 1 | `/masterplan-agent:bao-cao-kinh-doanh [kỳ]` | Doanh thu, đơn theo tháng, sản phẩm, kênh, so KPI | Google Drive, thư mục trên máy |
| 1 | `/masterplan-agent:chi-phi-ads [kỳ]` | Chi phí Meta/TikTok/Google Ads + chi Marketing khác (KOC, sản xuất, công cụ), so ngân sách, CPL, ROAS | Meta Ads MCP, TikTok for Business MCP / Ads Manager, file ngân sách |
| 1 | `/masterplan-agent:review-nam [năm]` | Tổng hợp một bản Marketing Audit: 3 điểm mạnh, 3–5 vấn đề ưu tiên | Kết quả các skill phần 1 |
| 2 | `/masterplan-agent:nghien-cuu-thi-truong` | Ngành hàng, khách hàng, 5–10 đơn vị cùng ngành, tổng hợp có mức tin cậy | Web, Google Trends, Social, Google Maps, sàn, Meta Ads Library |
| 2 | `/masterplan-agent:quet-doi-thu` | Theo dõi nội dung, offer, khuyến mãi, quảng cáo đối thủ; báo "có gì mới" | Chrome (trang đối thủ, Meta Ads Library, Google Ads Transparency) |
| 3 | `/masterplan-agent:du-bao-xu-huong [năm]` | Tín hiệu thị trường → phản ứng khách → dự báo → tự phản biện | Nguồn chính thức, báo cáo ngành, Trends, Social, sàn |
| 4 | `/masterplan-agent:dinh-huong-chien-luoc [năm]` | 2–3 khoảng trống → chấm 5 tiêu chí → một câu định hướng → phản biện → tài liệu một trang | Kết quả phần 1–3 |

Mỗi skill xuất: `bao-cao.md` (bản chữ), `bao-cao.html` (có biểu đồ/bảng), `sheets/*.csv` (ghi vào Google Sheets sau khi bạn duyệt).

## Agent Market Research (20 năng lực)
Nói yêu cầu bằng lời, agent tự chọn quy trình: `/masterplan-agent:research tìm cơ hội Marketing dịp Tết`.
Một lần nghiên cứu → nhiều kết quả phân tích → nhiều tài nguyên Marketing → có bằng chứng → cập nhật và tái sử dụng được.

| Nhóm | Skill | Đầu ra chính (mã trong kho) |
| --- | --- | --- |
| Điều phối | `research` (9 workflow, mức Nhanh / Chuyên sâu / Cập nhật, chế độ 3C cũ) | Research Brief `RP` |
| A · Thu thập | `company-analysis` (01 nội bộ) · `xu-huong-mua-vu` (02) · `customer-research` (03) · `competitor-research` (04) · `tu-khoa` (05) · `nghien-cuu-content` (06) · `format-sang-tao` (07) · `quang-cao-chuyen-doi` (08) · `kenh-cong-dong` (09) | `EVD`, `MAU`, `FIND`, `DN`, `TT/XH/MV/BD/RR`, `KH/SEG/HT`, `DV/UD/TN/KT`, `KEY`, `CNT`, `FMT`, `QC/LP`, `KEN` |
| B · Chuyển hoá | `insight` (10) · `marketing-opportunities` (11) · `san-pham-uu-dai` (12) · `dinh-vi-thong-diep` (13) · `y-tuong-content` (14) · `y-tuong-quang-cao` (15) · `y-tuong-chien-dich` (16) · `toi-uu-chuyen-doi` (17) · `marketing-recommendations` (giao việc 3C) | `INS`, `OPP`, `OFFER`, `TD`, `IDEA`, `ADS`, `CAM`, `CRO` |
| C · Hệ thống | `kiem-chung` (19) · `kho-du-lieu` (20) | Trạng thái kiểm chứng, `MT`, `TH`, `GT`; kho 3 lớp |
| Subagent | `market-researcher` · `customer-researcher` · `competitor-researcher` · `content-researcher` · `research-verifier` | Chạy song song khi nghiên cứu chuyên sâu |

Kho dữ liệu (`kho/` trong thư mục làm việc, công cụ `scripts/kho.py`) giữ chuỗi liên kết
`EVD → FIND → INS → OPP → IDEA / ADS / CAM`: mở một ý tưởng là truy ngược được Insight, phát hiện, bằng chứng gốc (`kho.py truy-vet IDEA-004`).
Chi tiết: `references/kho-du-lieu.md`, `references/nghien-cuu/workflow.md`, hướng dẫn 13 nền tảng ở `references/nen-tang/`,
báo cáo nâng cấp ở `NANG-CAP-MARKET-RESEARCH.md`.

## Luồng chung
```
Chốt phạm vi → Lấy số (có nguồn, ngày) → Script tính / dựng bảng → Agent nhận định
→ Báo cáo .md + .html → [bạn duyệt] → Ghi Google Sheets ("Chờ duyệt")
```
Đầu ra cuối mỗi giai đoạn khớp **bộ mẫu Marketing Masterplan** (`references/bo-mau.md`):
`scripts/xuat_bo_mau.py` dựng file .xlsx đúng tab, mục, tên cột của mẫu (hoặc mẫu trống để tự điền).
Các skill nghiên cứu tách rõ **dữ kiện / nhận định / giả định** và chấm **mức tin cậy Cao / Trung bình / Thấp**;
script báo cảnh báo khi một dòng thiếu nguồn.

## Cần chuẩn bị
- **Claude in Chrome**, đăng nhập sẵn Meta Business Suite, TikTok Studio, TikTok Ads, Zalo OA, Zalo web, YouTube Studio.
- Connector **Meta Ads** (`https://mcp.facebook.com/ads`), **TikTok for Business** (`https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer`,
  cấp lại quyền sau 30 ngày), **LadiPage** (lead), **Google Drive**, **Google Sheets** (không bắt buộc đủ hết; thiếu nguồn nào agent ghi rõ).
- Python 3 có `openpyxl` (đọc file Excel).

## Cấu trúc plugin
```
.claude-plugin/   plugin.json, marketplace.json
skills/           dieu-phoi, huong-dan, setup, 11 skill Masterplan năm, 20 skill Market Research
agents/           market-, customer-, competitor-, content-researcher, research-verifier
scripts/kho.py    kho dữ liệu nghiên cứu (mã, liên kết, kiểm tra, truy vết, xuất, báo cáo)
tests/            kiểm thử cấu trúc, kho và 9 case mô phỏng: python3 -m unittest discover -s tests
references/       quy-tac.md, quy-tac-bang-chung.md, ket-qua-json.md, khung-danh-gia.md, nguong.json,
                  hướng dẫn từng skill (thu-thap, thuong-hieu, review-nam, thi-truong, du-bao, chien-luoc...)
scripts/          tính chỉ số và dựng báo cáo (Python, không cần thư viện ngoài trừ openpyxl)
templates/        cau-hinh-mau.json, company-context-mau.md (Mẫu bối cảnh doanh nghiệp),
                  bo-mau/bo-mau.json (khuôn bộ mẫu 5 file: đánh giá hiện trạng, nghiên cứu thị trường,
                  dự báo và định hướng, kế hoạch tổng thể)
```

## Lưu ý
- Agent chỉ đọc: không đăng bài, không trả lời tin nhắn, không sửa quảng cáo hay ngân sách, không sửa file gốc.
- Tin nhắn khách chỉ được đếm và phân loại; không lưu tên, SĐT, email, nội dung chat.
- Kết luận về kênh, chiến dịch là đề xuất; bạn quyết.
- Repo chỉ chứa mẫu. Dữ liệu thật nằm trong thư mục làm việc của bạn.
