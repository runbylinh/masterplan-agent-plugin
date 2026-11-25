# Báo cáo kinh doanh: định dạng chuẩn

Mọi báo cáo (mỗi doanh nghiệp một kiểu file) được gom về `du-lieu.json`. Dòng nào không có số thì bỏ trường hoặc để `null`.

```json
{
  "doanh_nghiep": "Brand mẫu",
  "ky": {"tu": "2025-12", "den": "2026-11"},
  "ngay_lay": "2026-11-25",
  "don_vi_tien": "VND",
  "theo_thang": [
    {"thang": "2026-10", "doanh_thu": 820000000, "don": 190, "khach_moi": 150, "khach_cu": 40, "chi_phi_marketing": null}
  ],
  "theo_san_pham": [
    {"thang": "2026-10", "san_pham": "Khoá Content AI", "doanh_thu": 400000000, "don": 80, "loi_nhuan_gop": null}
  ],
  "theo_kenh": [
    {"thang": "2026-10", "kenh": "Facebook Ads", "doanh_thu": 300000000, "don": 70}
  ],
  "muc_tieu": [
    {"ky": "2026-10", "doanh_thu": 900000000, "don": 200}
  ],
  "nguon": [{"file": "Báo cáo KD 2026.xlsx", "noi": "Drive › Kinh doanh", "sheet": "Tổng hợp", "ngay_sua": "2026-11-20", "dung_cho": "theo_thang"}],
  "thieu": [{"muc": "theo_kenh 2025-12 → 2026-03", "ly_do": "file chưa tách kênh"}]
}
```
- `thang` dạng `YYYY-MM`. `muc_tieu.ky` là tháng (`YYYY-MM`) hoặc quý (`YYYY-Q4`) hoặc năm (`YYYY`).
- `khach_cu` = khách đã mua trước đó. Tỷ lệ mua lại = khach_cu / (khach_moi + khach_cu).
- Nếu báo cáo chỉ có danh sách đơn (mỗi dòng một đơn), tự cộng theo tháng/sản phẩm/kênh trước khi ghi; không ghi từng đơn.
