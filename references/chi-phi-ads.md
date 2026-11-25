# Chi phí quảng cáo: nơi lấy, định dạng

## Meta Ads (connector, chỉ đọc)
- `ads_get_ad_accounts` → xác nhận tài khoản trong `cau-hinh.json → ads.meta_ad_account_id`.
- `ads_get_ad_entities` cấp `campaign`, có insights theo khoảng ngày từng tháng: `spend`, `impressions`, `reach`, `clicks`,
  `actions` (kết quả), `objective`. Kiểm trường bằng `ads_get_field_context` nếu chưa chắc.
- Kết quả chính theo mục tiêu: tin nhắn → `onsite_conversion.messaging_conversation_started_7d`;
  lead → `lead` / `onsite_conversion.lead_grouped`; chuyển đổi web → `offsite_conversion.fb_pixel_lead` hoặc `purchase`;
  nhận biết → reach; tương tác → `post_engagement`; lượt xem video → `video_view`.
- Tiền tệ: theo tài khoản (thường VND). Không cộng VAT trừ khi người dùng yêu cầu.

## TikTok Ads (Claude in Chrome hoặc file xuất)
- ads.tiktok.com → Quản lý quảng cáo → Báo cáo → tạo báo cáo theo Chiến dịch, chiều Ngày; chỉ số: Chi phí, Hiển thị,
  Click, Chuyển đổi, Mục tiêu. Đọc bảng bằng `get_page_text`; bảng dài thì nhờ người dùng bấm Xuất và để file vào `nhap/`.
- Chỉ đọc. Không bấm Bật/Tắt, Sửa, Nhân bản, Nạp tiền.

## File ngân sách (Drive / Finder)
Mỗi file một kiểu. Tìm các cột: tháng, hạng mục/nền tảng, kế hoạch (ngân sách), thực chi. Hỏi người dùng nếu không rõ cột nào.

## Định dạng `chi-phi.json`
```json
{
  "doanh_nghiep": "Brand mẫu",
  "ky": {"tu": "2026-06", "den": "2026-11"},
  "ngay_lay": "2026-11-25",
  "don_vi_tien": "VND",
  "da_gom_vat": false,
  "chien_dich": [
    {"thang": "2026-10", "nen_tang": "meta", "tai_khoan": "TKQC 1", "chien_dich": "Lead khoá Content AI",
     "muc_tieu": "lead", "chi_phi": 12500000, "hien_thi": 820000, "reach": 310000, "click": 9100,
     "ket_qua": 210, "loai_ket_qua": "lead"}
  ],
  "ngan_sach": [
    {"thang": "2026-10", "hang_muc": "Meta", "ke_hoach": 15000000, "thuc_chi": 14200000, "nguon": "Ngân sách 2026.xlsx"}
  ],
  "ket_qua_kinh_doanh": [
    {"thang": "2026-10", "nen_tang": "meta", "lead": 230, "don": 41, "doanh_thu": 205000000, "nguon": "chi-so-kd.json theo_kenh"}
  ],
  "nguon": [{"muc": "chien_dich meta", "noi_lay": "connector Meta Ads", "ngay_lay": "2026-11-25"}],
  "thieu": [{"muc": "TikTok 2026-06", "ly_do": "tài khoản chưa chạy"}]
}
```
- `nen_tang`: `meta`, `tiktok`, hoặc hạng mục khác trong file ngân sách.
- `muc_tieu`: `nhan_biet`, `tuong_tac`, `luot_xem_video`, `tin_nhan`, `lead`, `chuyen_doi`, `luot_truy_cap`, `khac`.
- `thuc_chi` trong file ngân sách có thể khác chi phí trên nền tảng (VAT, phí, chênh tỷ giá): báo cáo cả hai, không gộp.
