# TikTok (nội dung công khai)

## 1. Dùng cho
| Skill | Mục đích |
| --- | --- |
| nghien-cuu-content, format-sang-tao | Hook, góc, thông điệp, format, CTA của video ngành |
| customer-research | Nhu cầu, câu hỏi, ngôn ngữ khách trong bình luận |
| tu-khoa | Gợi ý tìm kiếm TikTok ("Người khác tìm kiếm") |
| kenh-cong-dong | Creator, kênh vệ tinh trong ngành |
| competitor-research | Kênh đơn vị cùng ngành (đọc cùng `references/quet-doi-thu.md`) |

## 2. Công cụ truy cập
- Claude in Chrome: `tabs_context_mcp` → `navigate` `https://www.tiktok.com/search?q=<từ khóa>` (tab **Video**, **Người dùng**, **Hashtag**).
- `get_page_text` sau mỗi lần cuộn để lấy caption, tên kênh, lượt thích ở lưới; mở từng video để đọc ngày đăng, thích, bình luận, lưu, chia sẻ; `find` "comment" để mở khung bình luận.
- Transcript: dùng phụ đề tự động nếu video có (nút CC), không có thì ghi "không có transcript" và chỉ mô tả phần đã xem được qua `computer` screenshot từng khung.
- TikTok đòi đăng nhập sau vài lượt cuộn hoặc hiện CAPTCHA kéo hình: dừng, nhờ người dùng đăng nhập/giải trên Chrome rồi làm tiếp. Không tự giải CAPTCHA.

## 3. Các bước
1. Lập danh sách từ khóa theo 4 lớp: ngành, nhu cầu, sản phẩm, tình huống (mục 4).
2. Với mỗi từ khóa: tìm, ghi **thời điểm tìm** và **thứ tự** 20 kết quả đầu tab Video (vị trí 1–20); tab Người dùng để tìm kênh; ghi các cụm "Người khác tìm kiếm".
3. Lấy mẫu **nhiều mức tương tác**: trong mỗi từ khóa chọn video Nổi bật (lượt thích cao nhất trong 20), Thông thường (trung vị), Ít tương tác; và **nhiều thời điểm đăng** (trong 30 ngày, 1–6 tháng, cũ hơn). Mục tiêu 30–50 video cho một đợt.
4. Mở từng video: ghi URL, kênh, ngày đăng, thời lượng, thích/bình luận/lưu/chia sẻ (đúng số hiển thị), caption, hashtag.
5. Xem video: ghi Hook 3 giây đầu (lời nói + chữ trên màn hình), cấu trúc theo đoạn, cách quay quan sát được, CTA.
6. Đọc bình luận: sắp mặc định, đọc 20–40 bình luận đầu + mở các trả lời có nội dung; chỉ giữ bình luận thực chất (hỏi giá, hỏi size, kể trải nghiệm, phản đối). Bỏ tag bạn bè, emoji, spam.
7. Phân loại phản hồi: Nhu cầu, Câu hỏi, Rào cản, Trải nghiệm sau mua, Ngôn ngữ khách hàng; đếm số lần lặp.
8. Phân tích theo video: nhu cầu được khai thác, Hook, góc, thông điệp, format, CTA; video nào lặp cùng công thức.
9. Ghi kho; lưu video tham chiếu là URL + ảnh chụp khung chính trong `bang-chung/`, không tải video.

## 4. Xây từ khóa (ví dụ giả định: Brand mẫu bán kem chống nắng)
| Lớp | Ví dụ |
| --- | --- |
| Ngành | "skincare da dầu", "review kem chống nắng" |
| Nhu cầu | "kem chống nắng không bết", "chống nắng cho da mụn" |
| Sản phẩm | "kem chống nắng nâng tông", "xịt chống nắng" |
| Tình huống | "đi biển nên dùng kem chống nắng gì", "chống nắng khi chạy xe máy" |

## 5. Ghi vào kho
| Dữ liệu | Loại bản ghi / trường |
| --- | --- |
| URL video, ngày đăng, ngày xem, điều quan sát | EVD: Nguồn, Nền tảng = "TikTok", Ngày đăng, Ngày thu thập, Nội dung quan sát, Loại nguồn = Công khai, Phạm vi mẫu |
| Từ khóa, thời điểm tìm, thứ tự, tiêu chí chọn | MAU: Từ khóa, Phương pháp tìm kiếm ("TikTok web, đã đăng nhập, 26/11/2026 14:00, vị trí 1–20"), Tiêu chí đưa vào/loại trừ, ba con số bản ghi, Mức bão hoà |
| Hook, góc, thông điệp, cấu trúc, format, CTA, chỉ số | CNT: URL, Kênh, Hook, Góc khai thác, Thông điệp, Cấu trúc nội dung, Format, CTA, Chỉ số công khai, Mức mẫu |
| Bình luận đã ẩn danh | KH: Nhãn, Nội dung (viết lại ngắn), Loại khách = Quan sát công khai, Nguồn = URL video |
| Gợi ý tìm kiếm | KEY: Nền tảng = "TikTok", Chỉ số quan tâm = "không có số" |
| Creator, kênh vệ tinh | KEN: Bảng = Kho Creator, Chỉ số công khai |
| Công thức lặp | FIND: Phân loại = Mẫu lặp, Số lần xuất hiện ("9/40 video") |

## 6. Giới hạn và điều cấm
- Kết quả tìm kiếm cá nhân hoá theo tài khoản và vị trí: ghi rõ trong MAU.
- Lượt xem, lượt thích, số video dưới hashtag **không phải** lượng tìm kiếm hay nhu cầu mua.
- TikTok **không có thư viện quảng cáo công khai cho Việt Nam**; video gắn nhãn "Quảng cáo/Được tài trợ" chỉ ghi là quan sát lẻ. Dùng `tiktok-creative-center.md` cho mẫu quảng cáo.
- Không mô tả hiệu ứng, âm thanh, cảnh quay chưa thực sự xem được.
- Ẩn danh người bình luận: không ghi tên, @, ảnh, link hồ sơ.
- Không bấm theo dõi, thích, bình luận, chia sẻ, lưu, nhắn tin.

## 7. Đầu ra chuyển hoá
CNT → `format-sang-tao` (FMT), `insight`; KH → `customer-research` (SEG, HT), `insight`; KEY → `tu-khoa`; KEN → `kenh-cong-dong`.
