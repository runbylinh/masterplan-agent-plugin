---
name: setup
description: Cài Agent Masterplan cho một doanh nghiệp — tạo thư mục làm việc, file cau-hinh.json (kênh social + vai trò, đối thủ, tài khoản Meta/TikTok Ads, nguồn lead theo utm, hộp thư và nhãn chốt đơn, thư mục báo cáo kinh doanh và file ngân sách trên Drive/Finder, Google Sheets), kiểm tra Claude in Chrome và các connector. Dùng khi người dùng gõ /masterplan-agent:setup, nói "cài agent masterplan", "thêm doanh nghiệp", "khai báo kênh", "thêm đối thủ", hoặc khi skill khác báo chưa có cau-hinh.json.
---

# /masterplan-agent:setup

Đọc `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md` trước.

## Bước 1 – Thư mục làm việc
- Thư mục làm việc là thư mục người dùng đang mở. Nếu đang ở thư mục mã nguồn plugin thì hỏi nơi tạo
  (gợi ý một thư mục riêng, ví dụ `masterplan-<ten-doanh-nghiep>/`). Dữ liệu thật KHÔNG để trong thư mục plugin.
- Tạo `nhap/`, `bang-chung/`.
- Có `cau-hinh.json` rồi: hỏi người dùng muốn sửa phần nào, chỉ sửa phần đó.
- Chưa có: chép `${CLAUDE_PLUGIN_ROOT}/templates/cau-hinh-mau.json` thành `cau-hinh.json`, xoá dữ liệu mẫu.

## Bước 2 – Hỏi theo nhóm (mỗi nhóm một lần hỏi, không tự điền)
1. **Doanh nghiệp**: tên, ngành, khu vực, mục tiêu kinh doanh năm/quý, nguồn lực marketing (người, ngân sách).
2. **Kênh của mình**: link từng kênh đang dùng (Page, Group, TikTok, IG, Threads, YouTube, Zalo OA)
   và vai trò (gợi ý mặc định theo `khung-danh-gia.md`, người dùng sửa).
3. **Đối thủ**: 3–5 đối thủ + link kênh. Chưa có thì để trống, skill `danh-gia-kenh` / `quet-doi-thu` sẽ đề xuất.
4. **Quảng cáo**: ID tài khoản Meta Ads (gọi `ads_get_ad_accounts` để người dùng chọn), TikTok Ads advertiser ID,
   file ngân sách/chi tiêu (link Drive hoặc đường dẫn trên máy).
5. **Lead và hộp thư**: utm_source của từng kênh trên landing page, các hộp thư team dùng
   (Business Suite, Zalo OA, Zalo cá nhân trên chat.zalo.me, TikTok), tên nhãn đang gắn cho
   "đã chốt", "đang tư vấn", "không phù hợp"; file đơn hàng / Sheet sale / LadiWork để đối chiếu.
6. **Báo cáo kinh doanh**: thư mục Drive và thư mục trên máy chứa báo cáo, mục tiêu (KPI) từng kỳ nếu có.
7. **Google Sheets**: link file để ghi kết quả, hoặc cho phép tạo mới khi chạy lần đầu.

## Bước 3 – Kiểm tra kết nối (chỉ đọc)
| Nguồn | Cách kiểm | Dùng cho skill |
| --- | --- | --- |
| Claude in Chrome | `tabs_context_mcp` | 1, 2, 3, 5 |
| Meta Ads | `ads_get_ad_accounts` | 1, 2, 5 |
| LadiPage (lead, LadiWork) | `report_leads_by_campaign` kỳ 7 ngày | 1, 2 |
| Google Drive | `search_files` một từ khoá trong thư mục đã khai | 4, 5 |
| Google Sheets | `get_spreadsheet` nếu đã có link | mọi skill |
Ghi bảng trạng thái: nguồn nào sẵn sàng, nguồn nào thiếu và hệ quả. Không bắt người dùng nối hết mới chạy.

## Bước 4 – Kết thúc
Đọc lại `cau-hinh.json` cho người dùng xác nhận (tóm tắt, không dán cả file).
Gợi ý lệnh tiếp: `/masterplan-agent:danh-gia-kenh 90`.
