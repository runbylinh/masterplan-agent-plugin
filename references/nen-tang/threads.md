# Threads

## 1. Dùng cho
| Skill | Mục đích |
| --- | --- |
| customer-research | Ngôn ngữ khách, quan điểm, mâu thuẫn, bối cảnh đời sống |
| xu-huong-mua-vu | Tín hiệu xu hướng sớm (chủ đề mới nổi trong thảo luận) |
| insight | Giả thuyết Insight từ mâu thuẫn và cảm xúc trong thảo luận |
| nghien-cuu-content | Cách viết bài dạng chữ ngắn, chuỗi bài |

## 2. Công cụ truy cập
- Claude in Chrome: `tabs_context_mcp` → `navigate` `https://www.threads.com/search?q=<từ khóa>` (tab **Hàng đầu** và **Gần đây**); mở bài để đọc phần trả lời.
- `get_page_text` sau mỗi lần cuộn; ngày đăng hiện dạng "3 ngày", rê chuột hoặc `read_page` để lấy ngày cụ thể.
- Tìm kiếm Threads có thể yêu cầu đăng nhập Instagram: nhờ người dùng đăng nhập; không được thì ghi TH.
- WebSearch với `site:threads.com <từ khóa>` làm nguồn phụ khi tìm kiếm trong ứng dụng hạn chế.

## 3. Các bước
1. Lập 5–10 từ khóa theo chủ đề, nhu cầu, cách nói đời thường (Threads dùng nhiều văn nói, viết tắt).
2. Tìm ở cả **Hàng đầu** (thảo luận nhiều tương tác) và **Gần đây** (tín hiệu mới); ghi thời điểm tìm và số bài đã lướt.
3. Chọn bài khởi xướng thảo luận (có ≥ 5 trả lời thực chất) và đọc toàn bộ phần trả lời, gồm trả lời lồng.
4. Phân loại từng ý: Quan điểm (đồng ý/phản đối), Bối cảnh (ai, khi nào, ở đâu), Mâu thuẫn (muốn A nhưng sợ B), Nhu cầu, Câu hỏi.
5. Gom chủ đề mới chưa có trong kho (`kho.py tim --chu`): đánh dấu là tín hiệu, chưa phải xu hướng.
6. Đối chiếu tín hiệu trên nền tảng khác (TikTok, Facebook, Google Trends) trước khi ghi XH.

## 4. Xây từ khóa (ví dụ giả định: Brand mẫu dạy tiếng Anh cho người đi làm)
| Lớp | Ví dụ |
| --- | --- |
| Chủ đề | "học tiếng anh khi đi làm", "IELTS cho người đi làm" |
| Nhu cầu | "phỏng vấn bằng tiếng anh", "họp với sếp nước ngoài" |
| Cách nói đời thường | "mất gốc tiếng anh", "học mãi không nói được" |
| Mâu thuẫn | "không có thời gian học", "học app không hiệu quả" |

## 5. Ghi vào kho
| Dữ liệu | Loại bản ghi / trường |
| --- | --- |
| URL bài, ngày đăng, ngày đọc, ý chính | EVD: Nguồn, Nền tảng = "Threads", Ngày đăng, Ngày thu thập, Nội dung quan sát, Loại nguồn = Công khai, Phạm vi mẫu |
| Từ khóa, tab, thời điểm tìm | MAU: Từ khóa, Phương pháp tìm kiếm ("Threads web, tab Gần đây, 26/11/2026"), ba con số, Giới hạn của mẫu |
| Câu nói của người dùng (ẩn danh) | KH: Nhãn = Ngôn ngữ khách hàng / Nhu cầu / Rào cản, Nội dung, Bối cảnh, Loại khách = Quan sát công khai |
| Chủ đề thảo luận lặp | FIND: Phân loại = Mẫu lặp, Nhóm = Khách hàng, Số lần xuất hiện |
| Tín hiệu mới đã đối chiếu | XH: Phân loại = Tín hiệu mới, Đánh giá = Cần thử nghiệm, Nền tảng |
| Mâu thuẫn gợi Insight | FIND: Phân loại = Giả thuyết (chuyển cho `insight`) |

## 6. Giới hạn và điều cấm
- Người dùng Threads ở Việt Nam lệch về nhóm trẻ, thành thị, nhân viên văn phòng: ghi vào "Giới hạn của mẫu".
- Bài lan truyền thường mang tính tranh luận, cảm xúc mạnh; không coi là quan điểm số đông.
- Một chủ đề nóng trên Threads chưa phải xu hướng thị trường cho đến khi đối chiếu được nguồn khác.
- Ẩn danh người viết; không ghi @, tên, ảnh.
- Không thích, trả lời, đăng lại, theo dõi.

## 7. Đầu ra chuyển hoá
Ngôn ngữ khách (KH) → `y-tuong-content`, `dinh-vi-thong-diep`; chủ đề thảo luận (FIND) → `nghien-cuu-content`; tín hiệu xu hướng (XH) → `xu-huong-mua-vu`; giả thuyết Insight (FIND Giả thuyết) → `insight`.
