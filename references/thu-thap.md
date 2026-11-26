# Thu thập số liệu kênh

Ưu tiên nguồn theo thứ tự: **connector** (Meta Ads, LadiPage) → **file người dùng xuất** trong `nhap/`
→ **Claude in Chrome** đọc trang quản trị đã đăng nhập → **trang công khai**.
Nguồn nào không lấy được thì ghi `null` + lý do vào `thieu`, đi tiếp, không đoán.

Chrome: chỉ ĐỌC. Không bấm nút đăng, xoá, trả lời, đổi cài đặt, bật/tắt quảng cáo.
Gặp trang đăng nhập hoặc xác minh (CAPTCHA, mã) thì dừng, nhờ người dùng tự làm trên Chrome rồi đi tiếp.
Chụp màn hình bảng số chính vào `bang-chung/` khi có thể.

## Kênh của mình (số nội bộ)

### Facebook Page
- **Meta Business Suite → Thông tin chi tiết (Insights)**, chọn đúng kỳ: reach (người tiếp cận), lượt xem,
  follower mới, tổng follower, tương tác nội dung.
- **Insights → Nội dung**: bảng từng bài (reach, cảm xúc, bình luận, chia sẻ, lượt click). Bảng dùng `role=row`,
  đọc bằng `get_page_text` hoặc `read_page` thay vì chụp ảnh.
- Người dùng có thể xuất CSV ở Insights → Xuất dữ liệu, bỏ vào `nhap/` rồi chạy `doc_file_xuat.py`.

### Facebook Group
- **Nhóm → Thông tin chi tiết về nhóm (Group insights)**, chọn "7/28 ngày qua" hoặc khoảng ngày: thành viên mới, bài viết,
  bình luận, cảm xúc, **người đã xem**, người đăng & bình luận. Dùng **người đã xem** làm `reach` (ghi rõ trong `ghi_chu`).
  KHÔNG dùng "thành viên hoạt động" làm reach: con số này nhỏ hơn số tương tác nên ER sẽ vượt 100%.
- Insights chỉ hiện % thay đổi so kỳ trước: tính ngược số kỳ trước = kỳ này / (1 + %), màu mũi tên cho biết tăng/giảm; ghi rõ là số tính ngược.
- Danh sách bài nổi bật: Insights → Tương tác → Bài viết hàng đầu (danh sách này lấy theo 28 ngày, phải lọc lại theo ngày đăng trong kỳ).
  Muốn đủ từng bài thì nhờ người dùng xuất CSV Insights vào `nhap/`.

### TikTok
- **TikTok Studio → Phân tích (Analytics)**: lượt xem video, lượt xem hồ sơ, thích, bình luận, chia sẻ,
  follower mới, tổng follower theo kỳ (tối đa 60 ngày; kỳ dài hơn thì lấy nhiều lần hoặc từ file xuất).
- Danh sách video: TikTok Studio → Bài đăng. Cách nhanh: bắt response mạng có `item_list`
  (`read_network_requests` lọc `item_list`) để lấy view, like, bình luận, chia sẻ, ngày đăng từng video.

### Instagram
- **Business Suite → Insights** (chọn Instagram) hoặc app Instagram → Bảng điều khiển chuyên nghiệp:
  reach, tương tác, follower mới. Bài: Insights → Nội dung.

### Threads
- **threads.net → Hồ sơ → Thông tin chi tiết**: lượt xem, lượt thích, trả lời, đăng lại, follower.
  Danh sách bài: cuộn hồ sơ, hoặc bắt response `graphql` để lấy số từng bài.

### YouTube
- **YouTube Studio → Số liệu phân tích**: lượt xem, thời gian xem, người đăng ký mới. Tab Nội dung cho từng video.
  Có thể xuất CSV từ Studio (nút Xuất) vào `nhap/`.

### Zalo OA
- **oa.zalo.me → Thống kê**: người quan tâm mới, tổng người quan tâm, lượt xem bài, tin nhắn.
  Zalo OA không có reach: dùng lượt xem bài, ghi rõ trong `ghi_chu`.

### Quảng cáo Meta (connector Meta Ads)
- `ads_get_ad_accounts` để xác nhận tài khoản trong `cau-hinh.json → ads.meta_ad_account_id`.
- `ads_get_ad_entities` lấy chi phí, reach, kết quả theo chiến dịch trong kỳ và kỳ trước.
- Ghi chi phí vào kênh `fb-page` (hoặc `instagram` nếu chiến dịch chỉ chạy IG) ở trường `chi_phi_ads`.
- Chỉ đọc. Không tạo, sửa, bật, tắt chiến dịch.

### Lead (connector LadiPage)
- `report_leads_by_campaign` theo kỳ và kỳ trước; chia lead về kênh theo `cau-hinh.json → lead.utm_source_theo_kenh`.
- `utm_source` chứa `fbads` là lead Paid (trường `lead_paid`), kể cả khi đi kèm `fanpage`.
- Bỏ các dòng có từ trong `lead.loai_tru` (ví dụ `test`). Lead không rõ nguồn ghi riêng, không chia về kênh nào.
- Không lưu tên, SĐT, email của lead, chỉ đếm số.

## Đối thủ (chỉ số công khai)
Mỗi kênh đối thủ lấy: follower hiện tại, số bài trong kỳ, và 10–20 bài gần nhất với ngày đăng, view (nếu hiển thị),
thích, bình luận, chia sẻ. Ghi `nguon = "trang công khai"`.
- **TikTok**: trang hồ sơ hiển thị view từng video; mở video để xem thích, bình luận, chia sẻ, ngày đăng.
- **Facebook Page**: số người theo dõi ở đầu trang; cuộn bài trong kỳ, ghi cảm xúc, bình luận, chia sẻ.
  Có thể xem thêm Meta Ads Library để biết đối thủ có đang chạy quảng cáo (chỉ ghi có/không + số mẫu đang chạy).
- **Instagram, Threads, YouTube**: follower trên hồ sơ, số trên từng bài.
- Không có số follower đầu kỳ của đối thủ thì để `null`, không tính tăng trưởng.

## Định dạng `so-lieu.json`
Ghi vào `danh-gia-kenh/<thư mục kỳ>/so-lieu.json`. Mọi số không có thì để `null`.
```json
{
  "doanh_nghiep": "Brand mẫu",
  "ky": {"tu": "2026-08-27", "den": "2026-11-24", "ky_truoc_tu": "2026-05-29", "ky_truoc_den": "2026-08-26"},
  "ngay_lay": "2026-11-25",
  "kenh": [
    {
      "id": "tiktok",
      "nen_tang": "tiktok",
      "ten": "@brandmau",
      "url": "https://www.tiktok.com/@brandmau",
      "cua": "minh",
      "doi_thu": null,
      "vai_tro": "nhan_biet",
      "hien_tai": {
        "follower": 12000, "follower_dau_ky": 10500, "follower_moi": 1500,
        "reach": null, "luot_xem": 350000,
        "tuong_tac": 18000, "so_bai": 36,
        "lead": 12, "lead_paid": 0, "chi_phi_ads": 0
      },
      "ky_truoc": {"follower": 10500, "follower_moi": 900, "reach": null, "luot_xem": 280000, "tuong_tac": 15000, "so_bai": 30, "lead": 8, "lead_paid": 0, "chi_phi_ads": 0},
      "bai": [
        {"url": "https://www.tiktok.com/@brandmau/video/1", "ngay": "2026-10-02", "dinh_dang": "video ngắn",
         "chu_de": "Mẹo viết hook", "tieu_de": "3 lỗi viết hook", "luot_xem": 52000, "reach": null,
         "thich": 2100, "binh_luan": 140, "chia_se": 230, "luu": 400}
      ],
      "nguon": [{"chi_so": "luot_xem, tuong_tac", "noi_lay": "TikTok Studio → Phân tích", "ngay_lay": "2026-11-25"}],
      "thieu": [{"chi_so": "reach", "ly_do": "TikTok không có reach, dùng lượt xem"}],
      "ghi_chu": ""
    }
  ]
}
```
- `cua`: `minh` hoặc `doi_thu`. Kênh đối thủ: `doi_thu` = tên đối thủ, `vai_tro` = vai trò cùng nền tảng của mình.
- `tuong_tac` = thích + bình luận + chia sẻ (+ lưu nếu nền tảng có). Nếu chỉ có từng bài, script tự cộng từ `bai`.
- Group dùng `reach` = người đã xem; Zalo OA dùng `luot_xem` = lượt xem bài. Ghi vào `ghi_chu`.
