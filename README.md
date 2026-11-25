# Agent Masterplan Marketing (masterplan-agent)

Plugin Claude Code của Run By Linh. Agent tự nghiên cứu kênh, lead, đối thủ, số kinh doanh và chi phí quảng cáo
để làm đầu vào cho **Marketing Masterplan** và **kế hoạch quý, tháng**. Mọi con số có nguồn và ngày lấy.
Sau mỗi bước, agent **dừng chờ bạn duyệt**.

## Cài đặt
```bash
claude plugin marketplace add runbylinh/masterplan-agent-plugin
claude plugin install masterplan-agent@rbl-masterplan-dev
```
Sau khi cài, mở phiên Claude Code mới (hoặc chạy `/reload-plugins`).

## Bắt đầu
Mở Claude Code trong một thư mục làm việc riêng cho doanh nghiệp (ví dụ `masterplan-brand/`), rồi gõ:
```
/masterplan-agent:setup
```
Agent hỏi kênh, đối thủ, tài khoản quảng cáo, hộp thư, thư mục báo cáo, rồi tạo `cau-hinh.json`.

## Các skill
| Lệnh | Việc | Nguồn số |
| --- | --- | --- |
| `/masterplan-agent:setup` | Khai báo doanh nghiệp, kênh, đối thủ, nguồn số | — |
| `/masterplan-agent:danh-gia-kenh [kỳ]` | 1 · Đánh giá Page, Group, TikTok, IG, Threads, YouTube, Zalo OA theo vai trò trong phễu, so kỳ trước và đối thủ, kết luận Giữ / Đẩy mạnh / Tối ưu / Bỏ | Chrome (Business Suite, TikTok Studio...), file xuất, Meta Ads, LadiPage |
| `/masterplan-agent:lead-hoi-thoai [kỳ]` | 2 · Số hội thoại, tốc độ phản hồi, chất lượng lead, tỷ lệ chốt qua tin nhắn, lý do không chốt | Chrome (Business Suite, Zalo OA, Zalo web, TikTok), nhãn hộp thư, file đơn / LadiWork |
| `/masterplan-agent:quet-doi-thu` | 3 · Nội dung, offer, khuyến mãi, quảng cáo đối thủ; báo "có gì mới" so với lần quét trước | Chrome (trang đối thủ, Meta Ads Library, Google Ads Transparency) |
| `/masterplan-agent:bao-cao-kinh-doanh [kỳ]` | 4 · Doanh thu, đơn theo tháng, theo sản phẩm, theo kênh, so KPI | Google Drive, thư mục trên máy |
| `/masterplan-agent:chi-phi-ads [kỳ]` | 5 · Chi phí Meta + TikTok Ads theo tháng/mục tiêu/chiến dịch, so ngân sách, CPL, ROAS | Meta Ads, TikTok Ads Manager, file ngân sách |

Mỗi skill xuất: `bao-cao.md` (bản chữ), `bao-cao.html` (có biểu đồ), `sheets/*.csv` (ghi vào Google Sheets sau khi bạn duyệt).

## Luồng chung
```
Chốt phạm vi → Lấy số (có nguồn, ngày) → Script tính chỉ số → Agent nhận định
→ Báo cáo .md + .html → [bạn duyệt] → Ghi Google Sheets ("Chờ duyệt")
```

## Cần chuẩn bị
- **Claude in Chrome**, đăng nhập sẵn Meta Business Suite, TikTok Studio, TikTok Ads, Zalo OA, Zalo web, YouTube Studio.
- Connector **Meta Ads**, **LadiPage** (lead), **Google Drive**, **Google Sheets** (không bắt buộc đủ hết; thiếu nguồn nào agent ghi rõ).
- Python 3 có `openpyxl` (đọc file Excel).

## Cấu trúc plugin
```
.claude-plugin/   plugin.json, marketplace.json
skills/           setup + 5 skill
references/       quy-tac.md (quy tắc chung), khung-danh-gia.md, nguong.json, và hướng dẫn lấy số từng skill
scripts/          tính chỉ số và dựng báo cáo (Python, không cần thư viện ngoài trừ openpyxl)
templates/        cau-hinh-mau.json (ví dụ Brand mẫu)
```

## Lưu ý
- Agent chỉ đọc: không đăng bài, không trả lời tin nhắn, không sửa quảng cáo hay ngân sách, không sửa file gốc.
- Tin nhắn khách chỉ được đếm và phân loại; không lưu tên, SĐT, email, nội dung chat.
- Kết luận về kênh, chiến dịch là đề xuất; bạn quyết.
- Repo chỉ chứa mẫu. Dữ liệu thật nằm trong thư mục làm việc của bạn.
