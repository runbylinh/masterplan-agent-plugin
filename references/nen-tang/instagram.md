# Instagram

## 1. Dùng cho
| Skill | Mục đích |
| --- | --- |
| format-sang-tao | Nguyên lý hình ảnh: bố cục, màu, kể chuyện bằng carousel, nhịp Reels |
| nghien-cuu-content | Chủ đề, thông điệp, caption của tài khoản ngành |
| kenh-cong-dong | Creator, tài khoản vệ tinh |
| customer-research | Phản hồi trong bình luận (thường ít hơn TikTok/Facebook) |

## 2. Công cụ truy cập
- Claude in Chrome (Instagram web hầu như bắt buộc đăng nhập; nhờ người dùng đăng nhập sẵn): `tabs_context_mcp` → `navigate`:
  - Hồ sơ: `https://www.instagram.com/<tài khoản>/` → tab Bài viết, Reels.
  - Hashtag/từ khóa: ô Tìm kiếm của Instagram (kết quả gồm tài khoản, âm thanh, thẻ).
- Mở từng bài; carousel cần bấm mũi tên từng trang (`find` "Next"/"Tiếp" + `computer` click), chụp `computer` screenshot mỗi trang.
- `get_page_text` để lấy caption, số thích, bình luận; ngày đăng đọc bằng `read_page` (thẻ thời gian).
- Instagram chặn khi mở quá nhanh ("Thử lại sau"): dừng vài phút; vẫn chặn thì ghi TH.

## 3. Các bước
1. Chọn 5–10 tài khoản (ngành, đơn vị cùng ngành, Creator) và 3–5 chủ đề/hashtag.
2. Với mỗi tài khoản: lướt 30 bài gần nhất, ghi loại (Reels, carousel, ảnh đơn), ngày đăng, chỉ số hiển thị; chọn mẫu Nổi bật / Thông thường / Ít tương tác.
3. Với Reels: Hook (khung đầu + chữ), thời lượng, cấu trúc, chữ trên video, CTA.
4. Với carousel: đếm số trang, ghi chức năng từng trang (trang bìa, vấn đề, giải pháp, bằng chứng, CTA), cách chuyển trang.
5. Với ảnh đơn và lưới hồ sơ: bố cục, tỷ lệ, bảng màu, kiểu chữ, cách đặt sản phẩm/người, nhất quán lưới.
6. Đọc caption (độ dài, cấu trúc, hashtag) và bình luận thực chất.
7. Rút nguyên lý hình ảnh lặp (ví dụ "trang bìa carousel là câu hỏi + ảnh cận sản phẩm, 7/12 mẫu").

## 4. Chọn mẫu (ví dụ giả định: Brand mẫu thời trang công sở nữ)
| Nhóm | Ví dụ |
| --- | --- |
| Chủ đề | "phối đồ công sở", "outfit đi làm", "capsule wardrobe" |
| Tài khoản | 3 thương hiệu cùng phân khúc giá, 3 stylist cá nhân, 2 tài khoản tạp chí thời trang |
| Định dạng | Mỗi tài khoản lấy cả Reels và carousel để so sánh |

## 5. Ghi vào kho
| Dữ liệu | Loại bản ghi / trường |
| --- | --- |
| URL bài, ngày đăng, ngày xem, quan sát, ảnh chụp | EVD: Nguồn, Nền tảng = "Instagram", Ngày đăng, Ngày thu thập, Nội dung quan sát, Loại nguồn = Công khai, Ảnh chụp |
| Tài khoản, số bài đã lướt, tiêu chí chọn | MAU: Nguồn, Phương pháp tìm kiếm, Tiêu chí đưa vào/loại trừ, ba con số |
| Chủ đề, Hook, thông điệp, cấu trúc, format, CTA, chỉ số | CNT: Format ("Carousel 8 trang"/"Reels 25 giây"), Cấu trúc nội dung, Chỉ số công khai, Mức mẫu |
| Nguyên lý bố cục, màu, kể chuyện | FMT: Loại format = Hình ảnh/Video, Bố cục tổng thể, Thứ tự thông tin, Hình ảnh chủ đạo, Tỷ lệ khung hình, Mẫu tham khảo |
| Bình luận ẩn danh | KH: Loại khách = Quan sát công khai |
| Creator | KEN: Bảng = Kho Creator |

## 6. Giới hạn và điều cấm
- Instagram có thể ẩn số lượt thích; ghi "ẩn" thay vì đoán.
- Lượt xem Reels không so được trực tiếp với lượt thích ảnh; so trong cùng định dạng.
- Chỉ mô tả bố cục, màu, chữ thực sự thấy trên ảnh chụp; không suy đoán hiệu ứng chuyển cảnh chưa xem.
- Không sao chép hình ảnh để dùng lại; chỉ rút nguyên lý.
- Ẩn danh người bình luận. Không thích, theo dõi, bình luận, nhắn tin.

## 7. Đầu ra chuyển hoá
CNT, FMT → `format-sang-tao`, `y-tuong-content` (brief hình ảnh cho Agent Design); KEN → `kenh-cong-dong`; KH → `customer-research`.
