# Facebook (Fanpage, hội nhóm, tìm kiếm)

## 1. Dùng cho
| Skill | Mục đích |
| --- | --- |
| customer-research | Câu hỏi, nhu cầu, quan điểm, trải nghiệm trong bình luận và hội nhóm |
| nghien-cuu-content | Bài, video, Reels của Fanpage ngành |
| competitor-research | Nội dung, ưu đãi, phản hồi trên Page đơn vị cùng ngành (đọc cùng `references/quet-doi-thu.md`) |
| kenh-cong-dong | Hội nhóm, quy mô, mức hoạt động, quy định |

## 2. Công cụ truy cập
- Claude in Chrome (người dùng đăng nhập sẵn): `tabs_context_mcp` → `navigate`:
  - Tìm bài: `https://www.facebook.com/search/posts/?q=<từ khóa>` (bộ lọc Bài viết gần đây, Năm đăng).
  - Tìm nhóm: `https://www.facebook.com/search/groups/?q=<từ khóa>`; trong nhóm dùng ô Tìm kiếm của nhóm.
  - Page: `https://www.facebook.com/<page>` → tab Bài viết, Reels.
- `get_page_text` sau mỗi lần cuộn; ngày đăng thường ẩn sau rê chuột, đọc bằng `read_page`/`find`; mở "Xem thêm bình luận" bằng `find` + `computer` click.
- Nhóm **riêng tư** chưa tham gia: không xin vào nhóm thay người dùng. Nhờ người dùng (nếu họ đã là thành viên) hoặc ghi TH.
- Gặp checkpoint, xác minh danh tính: dừng, nhờ người dùng.

## 3. Các bước
1. Xác định nguồn: 3–5 Fanpage ngành, 3–5 hội nhóm liên quan (công khai hoặc người dùng đã là thành viên), 5–10 từ khóa.
2. Với mỗi nguồn, tìm bài, video, thảo luận trong khoảng thời gian của RP; ghi số bài đã lướt.
3. Chọn bài có thảo luận (≥ 10 bình luận thực chất) và cả bài ít tương tác; ưu tiên bài khách tự đăng hỏi ("Mọi người cho em hỏi...").
4. Đọc bình luận thực chất: câu hỏi, nhu cầu, quan điểm, kinh nghiệm, phàn nàn. Bỏ tag, chấm, quảng cáo chéo, seeding lộ liễu (ghi số đã loại).
5. Gắn nhãn KH và nhóm theo chủ đề (giá, chất lượng, địa điểm, so sánh, sau mua...).
6. So sánh giữa các cộng đồng: nhóm mẹ bỉm khác nhóm sinh viên ở câu hỏi, tiêu chí, mức giá chấp nhận.
7. Ghi kho đã ẩn danh; ảnh chụp chỉ lưu khi đã che tên và ảnh đại diện.

## 4. Chọn nguồn và từ khóa (ví dụ giả định: Cửa hàng A, quán cà phê làm việc)
| Lớp | Ví dụ |
| --- | --- |
| Từ khóa | "quán cà phê yên tĩnh làm việc", "cafe có ổ cắm", "cafe mở muộn Cầu Giấy" |
| Hội nhóm | Nhóm review ăn uống theo quận, nhóm freelancer, nhóm sinh viên khu vực |
| Fanpage | Page review địa điểm, Page của 3–5 quán cùng phân khúc |

## 5. Ghi vào kho
| Dữ liệu | Loại bản ghi / trường |
| --- | --- |
| URL bài, ngày đăng, ngày đọc, điều quan sát | EVD: Nguồn, Nền tảng = "Facebook Page" / "Facebook Group", Ngày đăng, Ngày thu thập, Nội dung quan sát, Loại nguồn = Công khai, Phạm vi mẫu ("62 bình luận, 18 dùng được") |
| Nguồn, từ khóa, khoảng thời gian, tiêu chí lọc | MAU: Nguồn, Từ khóa, Phương pháp tìm kiếm, Tiêu chí đưa vào/loại trừ, ba con số, Nguồn không truy cập được (nhóm riêng tư) |
| Bình luận/bài của khách | KH: Nhãn, Nội dung (viết lại ngắn), Nhóm khách, Bối cảnh, Loại khách = Quan sát công khai, Chủ đề |
| Bài của Page ngành | CNT: Hook, Góc khai thác, Format, CTA, Chỉ số công khai (cảm xúc, bình luận, chia sẻ), Mức mẫu |
| Hội nhóm | KEN: Bảng = Kho cộng đồng, Quy mô, Mức độ hoạt động, Quy định |
| Khác biệt giữa cộng đồng | FIND: Phân loại = Mẫu lặp/Quan sát, Nhóm = Khách hàng |

## 6. Giới hạn và điều cấm
- Thuật toán hiển thị khác nhau theo tài khoản; tìm kiếm Facebook không đầy đủ, ghi vào "Giới hạn của mẫu".
- Hội nhóm có seeding: đánh dấu bình luận nghi seeding, không tính vào mẫu lặp.
- Ẩn danh tuyệt đối: không ghi tên, ảnh, link hồ sơ, tên nhóm kín. Không chép nội dung nhóm riêng tư ra ngoài phạm vi người dùng cho phép.
- Không bấm thích, bình luận, chia sẻ, tham gia nhóm, nhắn tin, theo dõi Page.
- Lượt cảm xúc không phải nhu cầu mua.

## 7. Đầu ra chuyển hoá
KH → `customer-research` (SEG, HT), `insight`; CNT → `format-sang-tao`; KEN → `kenh-cong-dong`; câu hỏi lặp → `toi-uu-chuyen-doi` (Kho FAQ).
