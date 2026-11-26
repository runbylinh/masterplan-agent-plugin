---
name: huong-dan
description: Hướng dẫn cài đặt và thao tác Agent Masterplan Marketing — kiểm tra máy đã đủ chưa (plugin, Python + openpyxl, thư mục làm việc, cau-hinh.json, company-context.md, Claude in Chrome, connector Meta Ads, TikTok for Business, LadiPage, Google Drive, Google Sheets), chỉ ra bước còn thiếu và cách sửa, giải thích quy trình 4 phần, các lệnh, điểm duyệt, đầu ra và bộ mẫu. Chỉ đọc, không cài hay đổi gì khi chưa hỏi. Dùng khi người dùng gõ /masterplan-agent:huong-dan, hỏi "cài agent masterplan thế nào", "dùng agent này ra sao", "kiểm tra cài đặt", "lệnh nào làm gì", "agent bị lỗi không chạy".
argument-hint: "[kiem-tra | cai-dat | thao-tac | loi]"
---

# /masterplan-agent:huong-dan

Tài liệu đầy đủ: `${CLAUDE_PLUGIN_ROOT}/HUONG-DAN.md`. Đọc file đó trước, trả lời theo đúng nội dung, ngắn gọn bằng tiếng Việt.

## Chọn chế độ
- `kiem-tra` (mặc định khi không có tham số): kiểm tra máy rồi hướng dẫn bước tiếp.
- `cai-dat`: trình bày Phần A của HUONG-DAN.md theo từng bước, mỗi lệnh một khối `bash`.
- `thao-tac`: trình bày Phần B (quy trình 4 phần, bảng lệnh, cách duyệt, bộ mẫu, thư mục).
- `loi`: hỏi người dùng gặp hiện tượng gì, đối chiếu Phần D, kiểm tra đúng chỗ đó.
Người dùng hỏi một câu cụ thể thì trả lời đúng câu đó, trích phần liên quan, không dán cả tài liệu.

## Kiểm tra máy (chỉ đọc)
Chạy và ghi kết quả vào bảng **Hạng mục · Trạng thái (Có / Thiếu / Không kiểm được) · Cách sửa**:
| Hạng mục | Cách kiểm |
| --- | --- |
| Plugin và phiên bản | Đọc `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json` (version) |
| Python 3 + openpyxl | `python3 -c "import openpyxl; print(openpyxl.__version__)"` |
| Thư mục làm việc | Thư mục đang mở không phải thư mục mã nguồn plugin; có `cau-hinh.json`, `company-context.md`, `nhap/`, `bang-chung/` |
| Cấu hình đủ chưa | Trong `cau-hinh.json`: số kênh có link, đối thủ, `ads.meta_ad_account_id`, `google_sheets.spreadsheet_id`; trong `company-context.md`: mục còn để trống `[...]` |
| Claude in Chrome | `tabs_context_mcp` (nạp bằng ToolSearch nếu đang ẩn) |
| Meta Ads | `ads_get_ad_accounts` |
| TikTok for Business | Có công cụ TikTok Ads trong phiên không (ToolSearch "tiktok ads"); có thì liệt kê tài khoản nhà quảng cáo |
| LadiPage | `report_leads_by_campaign` kỳ 7 ngày gần nhất (chỉ đếm, không hiển thị thông tin khách) |
| Google Drive | `search_files` với một truy vấn nhỏ |
| Google Sheets | `get_spreadsheet` nếu đã có `spreadsheet_id` |
| Kết quả đã có | Các thư mục `danh-gia-kenh/`, `lead-hoi-thoai/`, `thuong-hieu/`, `kinh-doanh/`, `chi-phi-ads/`, `doi-thu/`, `review/`, `thi-truong/`, `du-bao/`, `chien-luoc/` |

Sau bảng:
1. Liệt kê việc còn thiếu theo thứ tự nên làm. Mỗi lệnh người dùng cần tự chạy để trong một khối `bash` riêng.
   Việc phải làm trên giao diện (cài tiện ích Chrome, thêm connector, đăng nhập) thì ghi đường đi ngắn theo HUONG-DAN.md.
2. Nói rõ skill nào **đã chạy được ngay** với nguồn hiện có, skill nào phải chờ bổ sung.
3. Gợi ý một lệnh tiếp theo phù hợp nhất (thường `/masterplan-agent:setup` nếu thiếu cấu hình, ngược lại `/masterplan-agent:dieu-phoi`).

## Không được
- Tự cài gói, thêm connector, đổi cài đặt, đăng nhập hộ, hay sửa `cau-hinh.json` khi người dùng chưa đồng ý.
- Hiển thị khoá, token, email khách hay dữ liệu lead chi tiết trong lúc kiểm tra kết nối.
