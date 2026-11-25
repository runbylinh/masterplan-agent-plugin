---
name: chi-phi-ads
description: Tổng hợp chi phí quảng cáo đã chi — đọc Meta Ads qua connector, TikTok Ads Manager qua Claude in Chrome hoặc file xuất, file ngân sách/chi tiêu trên Google Drive và Finder; gom theo tháng, nền tảng, mục tiêu, chiến dịch; so ngân sách kế hoạch với thực chi; ghép với lead (skill lead-hoi-thoai / danh-gia-kenh) và doanh thu (skill bao-cao-kinh-doanh) để ra chi phí/lead, chi phí/đơn, ROAS. Xuất báo cáo .md + HTML + Google Sheets. Dùng khi người dùng gõ /masterplan-agent:chi-phi-ads, nói "tổng hợp chi phí quảng cáo", "đã chi bao nhiêu tiền ads", "so ngân sách với thực chi", "ROAS", "chi phí mỗi lead".
argument-hint: "[kỳ: tháng | quý | 6 tháng | năm]"
---

# /masterplan-agent:chi-phi-ads [kỳ]

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/chi-phi-ads.md`.
Cần `cau-hinh.json` mục `ads`.

## Bước 0 – Chốt phạm vi
1. Kỳ (mặc định 6 tháng gần nhất, theo tháng dương lịch; tháng hiện tại ghi "đang chạy").
2. Nguồn: Meta Ads (connector, tài khoản trong cấu hình; nhiều tài khoản thì hỏi gộp những tài khoản nào),
   TikTok Ads (Chrome hoặc file xuất trong `nhap/`), file ngân sách (Drive/Finder trong `ads.file_ngan_sach`).
3. Hỏi: số trên nền tảng là **chưa gồm VAT**; có cộng VAT/phí thanh toán (thẻ, đại lý) khi so với ngân sách không.
4. Tạo `chi-phi-ads/YYYY-MM-DD_<ky>/`.

## Bước 1 – Lấy số (chỉ đọc)
- **Meta**: `ads_get_ad_entities` theo tháng, cấp chiến dịch: chi phí, hiển thị, reach, click, kết quả + loại kết quả,
  mục tiêu chiến dịch. Theo `references/chi-phi-ads.md`.
- **TikTok Ads**: ads.tiktok.com → Báo cáo (Reporting) → theo chiến dịch, theo ngày/tháng; hoặc file xuất CSV
  (đọc bằng `doc_file_xuat.py --xem`). Gặp đăng nhập/xác minh: nhờ người dùng.
- **File ngân sách**: Drive (`read_file_content`/`get_values`) hoặc Finder (`doc_file_xuat.py --xem`).
  Lấy kế hoạch và thực chi theo tháng, hạng mục (Meta, TikTok, KOC, khác). Hạng mục ngoài quảng cáo chỉ ghi nếu file có.
- **Ghép kết quả kinh doanh** (nếu đã có): lead từ `lead-hoi-thoai/*/chi-so-lead.json` hoặc LadiPage,
  doanh thu/đơn từ `kinh-doanh/*/chi-so-kd.json` (`theo_kenh`). Không có thì bỏ, không ước tính.
Ghi `chi-phi.json` theo `references/chi-phi-ads.md`.

## Bước 2 – Tính và báo cáo
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tinh_chi_phi.py chi-phi-ads/<kỳ>
```
Ra `chi-so-chi-phi.json`, `bao-cao.html`, `sheets/*.csv`. Đọc kết quả, viết `nhan-dinh.json`
(`tom_tat`, `phan_bo`, `hieu_qua`, `lech_ngan_sach`, `uu_tien`), chạy lại script, rồi viết `bao-cao.md`:
- Tổng chi theo tháng và nền tảng; tỷ trọng theo mục tiêu (nhận biết / tương tác / tin nhắn / lead / chuyển đổi).
- Kế hoạch vs thực chi: lệch bao nhiêu, tháng nào vượt/thiếu.
- Hiệu quả: chi phí/kết quả theo nền tảng và mục tiêu; CPL, chi phí/đơn, ROAS khi ghép được. Ghi rõ ROAS tính trên doanh thu
  nào (doanh thu kênh quảng cáo trong báo cáo kinh doanh) vì doanh thu có thể đến từ nhiều nguồn.
- Chiến dịch tốn nhiều mà kết quả thấp (top 5), chiến dịch hiệu quả nhất.
- Đầu vào cho plan: mức chi đề xuất theo tháng/nền tảng dựa trên hiệu quả thực tế (chỉ đề xuất, người dùng quyết).

DỪNG. Báo cáo 5 dòng, hỏi duyệt. Sau duyệt ghi Google Sheets tab `Chi phí ads` (append, `Chờ duyệt`).

## Không được
- Tạo, sửa, bật, tắt chiến dịch; đổi ngân sách; thêm phương thức thanh toán.
- Sửa file ngân sách gốc. Ước tính chi phí khi không đọc được số.
