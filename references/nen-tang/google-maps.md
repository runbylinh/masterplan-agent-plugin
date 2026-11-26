# Google Maps (địa điểm và đánh giá)

## 1. Dùng cho
| Skill | Mục đích |
| --- | --- |
| customer-research | Trải nghiệm thực tế, tiêu chí lựa chọn, điểm hài lòng/không hài lòng của khách đã đến |
| competitor-research | Hồ sơ địa điểm cùng ngành: giờ mở, khoảng giá, ảnh, điểm sao, phản hồi chủ địa điểm |
| company-analysis | Đánh giá về chính doanh nghiệp (khi doanh nghiệp có địa điểm) |
| xu-huong-mua-vu | Thời gian đông khách (Giờ cao điểm) theo khu vực |

## 2. Công cụ truy cập
- Claude in Chrome: `tabs_context_mcp` → `navigate` `https://www.google.com/maps/search/<ngành>+<khu vực>`.
- Mở địa điểm → tab **Bài đánh giá**: nút **Sắp xếp** (Liên quan nhất, Mới nhất, Cao nhất, Thấp nhất); thanh **chủ đề** gợi ý (ví dụ "giá", "phục vụ").
- Danh sách đánh giá là khung cuộn riêng: cuộn từng đoạn bằng `computer` scroll trong khung, sau mỗi lần đọc bằng `get_page_text`; bấm "Thêm" để mở đánh giá dài (`find` "Thêm"/"More").
- Không cần đăng nhập để đọc; gặp CAPTCHA dừng, nhờ người dùng.

## 3. Các bước
1. Xác định ngành và khu vực theo RP (quận, bán kính); tìm, ghi thứ tự 10–20 địa điểm đầu.
2. Chọn 5–10 địa điểm: gồm điểm sao cao/thấp, nhiều/ít đánh giá, cả đơn vị cùng phân khúc và khác phân khúc.
3. Với mỗi địa điểm, ghi hồ sơ: điểm sao, tổng số đánh giá, khoảng giá, giờ mở, phân loại, ngày xem.
4. Đọc mẫu đánh giá cân bằng: sắp **Mới nhất** (10–15 bài trong khoảng thời gian RP), rồi **Thấp nhất** (5–10 bài 1–2 sao), **Cao nhất** (5–10 bài), và 3–4 sao (trung lập, thường nêu cụ thể nhất). Chỉ giữ đánh giá có chữ.
5. Gắn nhóm: Sản phẩm, Giá, Vị trí (gửi xe, dễ tìm), Dịch vụ (thái độ, tốc độ), Trải nghiệm (không gian, vệ sinh, tiếng ồn).
6. Ghi phản hồi của chủ địa điểm (có trả lời không, cách xử lý phàn nàn).
7. Tìm mẫu lặp (cùng phàn nàn ở nhiều địa điểm) và ngoại lệ; đối chiếu với bình luận Facebook/TikTok cùng khu vực.

## 4. Chọn mẫu (ví dụ giả định: Cửa hàng A, spa chăm sóc da)
| Lớp | Ví dụ |
| --- | --- |
| Tìm kiếm | "spa chăm sóc da Đống Đa", "spa trị mụn gần đây" |
| Địa điểm | 3 spa ≥ 4,7 sao nhiều đánh giá, 3 spa 4,0–4,4 sao, 2 spa mới (< 50 đánh giá) |
| Đánh giá | Mỗi spa 20–30 bài: Mới nhất + 1–2 sao + 3–4 sao + 5 sao |

## 5. Ghi vào kho
| Dữ liệu | Loại bản ghi / trường |
| --- | --- |
| Link địa điểm, ngày xem, quan sát | EVD: Nguồn, Nền tảng = "Google Maps", Ngày đăng (của đánh giá, "khoảng 2 tuần trước" ghi đúng như hiển thị), Ngày thu thập, Nội dung quan sát, Loại nguồn = Công khai, Phạm vi mẫu |
| Từ khóa, khu vực, cách sắp xếp, số bài | MAU: Phạm vi địa lý, Từ khóa, Phương pháp tìm kiếm ("Mới nhất + Thấp nhất"), Tiêu chí đưa vào (có chữ) / loại trừ (chỉ sao, nghi đánh giá ảo), ba con số |
| Nội dung đánh giá đã ẩn danh | KH: Nhãn (Trải nghiệm sau mua, Tiêu chí lựa chọn, Nỗi đau), Nội dung, Loại khách = Quan sát công khai, Chủ đề (Sản phẩm/Giá/Vị trí/Dịch vụ/Trải nghiệm) |
| Hồ sơ địa điểm cùng ngành | DV: Tên, Giá, Định vị, Phản hồi tích cực, Phản hồi tiêu cực, Nguồn |
| Mẫu lặp và ngoại lệ | FIND: Nhóm = Khách hàng/Cạnh tranh, Số lần xuất hiện ("12/80 đánh giá nhắc chỗ gửi xe") |

## 6. Giới hạn và điều cấm
- Điểm sao trung bình và số đánh giá không đại diện toàn bộ khách; khách hài lòng ít viết hơn khách bực bội.
- Có đánh giá ảo hoặc đổi quà lấy đánh giá: loại bài chung chung lặp mẫu, ghi số đã loại.
- Ngày đánh giá chỉ hiển thị tương đối ("1 tháng trước"): ghi đúng như vậy kèm ngày xem.
- Ẩn danh: không ghi tên người đánh giá, ảnh, cấp "Local Guide".
- Không viết đánh giá, không bấm "Hữu ích", không đặt lịch, không gọi điện.

## 7. Đầu ra chuyển hoá
KH → `customer-research` (HT, SEG), `insight`; DV → `competitor-research` (KT); phàn nàn lặp → `toi-uu-chuyen-doi`, `san-pham-uu-dai`.
