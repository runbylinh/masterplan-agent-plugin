# YouTube

## 1. Dùng cho
| Skill | Mục đích |
| --- | --- |
| nghien-cuu-content, format-sang-tao | Tiêu đề, thumbnail, cấu trúc video dài và Shorts, format tái sử dụng |
| customer-research | Câu hỏi, trải nghiệm trong bình luận video review, hướng dẫn |
| tu-khoa | Gợi ý tìm kiếm YouTube (ý định "cách làm", "review") |
| kenh-cong-dong | Kênh chuyên gia, reviewer ngành |

## 2. Công cụ truy cập
- Claude in Chrome: `tabs_context_mcp` → `navigate` `https://www.youtube.com/results?search_query=<từ khóa>`; bộ lọc (Bộ lọc → Loại: Video/Shorts/Kênh; Ngày tải lên; Thời lượng; Sắp xếp theo Lượt xem/Ngày tải lên).
- Gợi ý tìm kiếm: gõ vào ô tìm kiếm, đọc danh sách bằng `get_page_text`/`find`.
- Transcript: dưới mô tả video bấm **Hiện bản chép lời** (`find` "transcript"/"bản chép lời") rồi `get_page_text`. Không có thì ghi "không có transcript".
- Thumbnail: `computer` screenshot lưới kết quả vào `bang-chung/`.
- Không cần đăng nhập cho nội dung công khai; video giới hạn độ tuổi/riêng tư: bỏ qua, ghi MAU.

## 3. Các bước
1. Từ khóa theo chủ đề và ý định (mục 4); chạy riêng cho Video dài và Shorts.
2. Mỗi từ khóa: ghi thời điểm tìm, thứ tự 20 kết quả đầu, tên kênh, lượt xem, ngày đăng hiển thị.
3. Chọn mẫu Nổi bật / Thông thường / Ít tương tác, và nhiều thời điểm đăng; thêm 3–5 kênh dẫn đầu chủ đề (tab Video, sắp xếp Phổ biến).
4. Với mỗi video: tiêu đề, thumbnail (chữ trên ảnh, gương mặt, sản phẩm), thời lượng, chương (chapters) trong mô tả.
5. Đọc transcript: Hook 30 giây đầu, cấu trúc theo chương, lời hứa và cách giữ chân, CTA (đăng ký, link mô tả, bình luận ghim).
6. Đọc bình luận (sắp Bình luận hàng đầu, 30–50 bình luận): câu hỏi chưa được trả lời, trải nghiệm, phản đối.
7. Gom nhu cầu, chủ đề lặp; xác định format có thể tái sử dụng (ví dụ "so sánh 3 sản phẩm theo 5 tiêu chí").

## 4. Xây từ khóa (ví dụ giả định: Brand mẫu bán máy lọc không khí)
| Ý định | Ví dụ |
| --- | --- |
| Hướng dẫn | "cách chọn máy lọc không khí cho phòng ngủ" |
| Review/so sánh | "review máy lọc không khí 2026", "máy lọc không khí loại nào tốt" |
| Vấn đề | "bụi mịn Hà Nội có nguy hiểm không", "dị ứng bụi nhà" |
| Sau mua | "vệ sinh màng lọc HEPA", "thay lõi lọc bao lâu" |

## 5. Ghi vào kho
| Dữ liệu | Loại bản ghi / trường |
| --- | --- |
| URL video, ngày đăng, ngày xem, quan sát | EVD: Nguồn, Nền tảng = "YouTube", Ngày đăng, Ngày thu thập, Nội dung quan sát, Loại nguồn = Công khai, Ảnh chụp (thumbnail) |
| Từ khóa, bộ lọc, thời điểm, thứ tự | MAU: Từ khóa, Phương pháp tìm kiếm, Tiêu chí đưa vào/loại trừ, ba con số |
| Tiêu đề, thumbnail, Hook, cấu trúc, CTA, chỉ số | CNT: Hook, Góc khai thác, Cấu trúc nội dung (theo chương), Format ("Video dài 12 phút"/"Shorts"), CTA, Chỉ số công khai, Mức mẫu |
| Bình luận ẩn danh | KH: Nhãn, Nội dung, Loại khách = Quan sát công khai |
| Gợi ý tìm kiếm | KEY: Nền tảng = "YouTube", Mục đích tìm kiếm |
| Kênh chuyên gia/reviewer | KEN: Bảng = Kho Creator, Chỉ số công khai (người đăng ký) |

## 6. Giới hạn và điều cấm
- Lượt xem tích luỹ theo thời gian: so sánh video phải ghi ngày đăng; không so lượt xem video 3 năm với video 1 tuần.
- Lượt xem và số người đăng ký không phải lượng tìm kiếm hay doanh số.
- Transcript tự động có lỗi tiếng Việt: trích ý, không trích nguyên văn khi câu sai rõ ràng.
- Không mô tả cảnh quay, dựng, âm thanh khi chưa xem đoạn đó.
- Ẩn danh người bình luận. Không thích, bình luận, đăng ký kênh.

## 7. Đầu ra chuyển hoá
CNT → `format-sang-tao` (FMT Video dài/Shorts), `y-tuong-content`; KH → `customer-research`, `insight`; KEY → `tu-khoa`; KEN → `kenh-cong-dong`.
