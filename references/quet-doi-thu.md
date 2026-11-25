# Quét đối thủ: nơi xem, định dạng

## Nơi xem (Claude in Chrome, chỉ đọc)
| Mục | Nơi xem | Mẹo |
| --- | --- | --- |
| Nội dung Facebook | Trang Page, cuộn bài trong khoảng nhìn lại | `get_page_text` sau mỗi lần cuộn; ngày bài hiện khi rê chuột, đọc qua `read_page` |
| Nội dung TikTok | tiktok.com/@kenh | View hiện ở lưới video; mở video để xem ngày, thích, bình luận, chia sẻ |
| Instagram, YouTube | Trang hồ sơ, tab Reels / Video | Số view/like trên từng bài |
| Quảng cáo Meta | facebook.com/ads/library → Việt Nam → Tất cả quảng cáo → tìm Page | Ghi Library ID, "Bắt đầu chạy vào", số phiên bản, nền tảng; mở "Xem chi tiết" để lấy link đích |
| Quảng cáo Google | adstransparency.google.com → tìm tên miền | Số mẫu, định dạng, lần hiển thị gần nhất |
| Quảng cáo TikTok | Bài có nhãn Quảng cáo/Được tài trợ khi lướt; TikTok Creative Center (Top Ads) theo ngành | Thư viện quảng cáo TikTok chỉ có cho EU, Việt Nam không có: ghi rõ |
| Offer, giá | Website, landing page trong link ads, bài ghim, Shopee/TikTok Shop | Chụp bảng giá; ghi giá niêm yết và giá ưu đãi riêng |
| Khuyến mãi | Bài ghim, ảnh bìa, landing page, ads | Ghi ngày bắt đầu/kết thúc nếu có, không có thì "không ghi thời hạn" |

## Định dạng `quet.json`
```json
{
  "ngay_quet": "2026-11-25",
  "khoang_nhin_lai_ngay": 30,
  "doi_thu": [
    {
      "ten": "Đối thủ A",
      "kenh": [{"nen_tang": "tiktok", "url": "https://www.tiktok.com/@doithua", "follower": 85000,
                "so_bai_trong_ky": 24, "chu_de_chu_luc": ["case học viên", "mẹo ads"], "dinh_dang_chu_luc": ["video talking head 45s"],
                "bai_noi_bat": [{"url": "...", "ngay": "2026-11-10", "hook": "viết lại ngắn", "luot_xem": 120000, "tuong_tac": 5400}]}],
      "offer": [{"ma": "khoa-ads-co-ban", "ten": "Khoá Ads cơ bản", "gia_niem_yet": 4990000, "gia_uu_dai": 2990000,
                 "qua_tang": "tặng 1 buổi 1-1", "cam_ket": "hoàn tiền 7 ngày", "url": "https://...", "ngay_thay": "2026-11-25"}],
      "khuyen_mai": [{"ma": "black-friday-2026", "ten": "Black Friday", "muc_giam": "40%", "tu": "2026-11-20", "den": "2026-11-30",
                      "dieu_kien": "đăng ký trước 30/11", "kenh": ["facebook", "landing page"], "url": "https://..."}],
      "ads": [{"nen_tang": "meta", "library_id": "1234567890", "bat_dau": "2026-11-18", "dang_chay": true, "dinh_dang": "video",
               "thong_diep": "tóm tắt ngắn", "cta": "Đăng ký", "link_dich": "https://...", "so_phien_ban": 3}],
      "nguon": [{"muc": "ads", "url": "https://www.facebook.com/ads/library/?...", "ngay": "2026-11-25"}],
      "khong_thay": ["Google Ads: không có mẫu nào"]
    }
  ]
}
```
- `ma` của offer/khuyến mãi: chuỗi không dấu, ổn định giữa các lần quét (dùng để so mới/cũ).
- Ads Meta so theo `library_id`; nền tảng khác so theo `link_dich` + `thong_diep`.
