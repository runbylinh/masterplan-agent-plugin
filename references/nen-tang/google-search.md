# Google Search

## 1. Dùng cho
| Skill | Mục đích |
| --- | --- |
| company-analysis, xu-huong-mua-vu | Báo cáo ngành, số liệu thị trường, chính sách, sự kiện mùa vụ |
| customer-research, tu-khoa | Câu hỏi khách tìm (gợi ý, "Mọi người cũng hỏi"), thảo luận trên diễn đàn |
| competitor-research | Website, bài PR, trang so sánh của đơn vị cùng ngành |
| insight (kiểm chứng) | Đối chiếu nguồn độc lập cho phát hiện từ Social |

## 2. Công cụ truy cập
| Công cụ | Dùng khi | Kiểm tra trước |
| --- | --- | --- |
| WebSearch | Tìm nhanh danh sách nguồn | Có trong phiên chưa |
| Claude in Chrome: `navigate` google.com, `get_page_text`, `find` | Đọc gợi ý tìm kiếm, "Mọi người cũng hỏi", tìm kiếm liên quan, mở trang nguồn | `tabs_context_mcp` trả về tab hợp lệ |
| Google Ads → Keyword Planner (Chrome, tài khoản người dùng) | Khoảng lượng tìm kiếm tháng | Chỉ khi người dùng cấp quyền tài khoản Ads; không có thì ghi TH |
Gặp CAPTCHA "unusual traffic" hoặc trang yêu cầu đăng nhập/trả phí: dừng, nhờ người dùng tự xử lý hoặc dùng nguồn thay thế, ghi TH. Không vượt tường phí.

## 3. Các bước
1. Từ câu hỏi nghiên cứu trong RP, viết 3–5 từ khóa gốc (sản phẩm, nhu cầu, vấn đề, địa bàn).
2. Mở rộng biến thể: gõ từng từ khóa vào ô tìm kiếm, đọc **gợi ý tự động** (`find` "listbox" hoặc `get_page_text`); thêm tiền tố "cách", "có nên", "giá", "so sánh", "review", "ở đâu".
3. Trên trang kết quả: ghi **thứ tự** 10 kết quả đầu, mở rộng 3–4 câu trong **"Mọi người cũng hỏi"** (mỗi lần bấm sinh thêm câu), chép **"Tìm kiếm liên quan"** cuối trang.
4. Lọc nguồn theo ưu tiên: chính thống (cơ quan nhà nước, hiệp hội, báo cáo ngành) → báo chí uy tín → website ngành → diễn đàn, hội nhóm. Dùng toán tử: `site:gov.vn`, `filetype:pdf`, `"cụm chính xác"`, Công cụ → Thời gian (12 tháng qua).
5. **Mở và đọc trang gốc**, không kết luận từ đoạn tóm tắt hay AI Overview. Với báo dẫn số liệu, lần tới nguồn gốc (báo cáo, thông cáo).
6. Trích: phát hiện, con số, đơn vị, thời gian đo, phạm vi (địa bàn, mẫu khảo sát), đơn vị công bố, ngày đăng.
7. Đối chiếu ≥ 1 nguồn độc lập (khác tên miền, không dẫn lại cùng gốc). Lệch nhau → ghi MT.
8. Ghi kho bằng `kho.py them`: EVD mỗi nguồn, MAU cho lượt tìm, FIND/KEY/XH theo nội dung.

## 4. Xây từ khóa (ví dụ giả định: Brand mẫu bán đồ ăn dặm, Hà Nội)
| Lớp | Ví dụ |
| --- | --- |
| Gốc | "đồ ăn dặm cho bé" |
| Nhu cầu/vấn đề | "bé 7 tháng lười ăn", "ăn dặm kiểu Nhật hay BLW" |
| So sánh/giao dịch | "cháo tươi đóng hộp có tốt không", "giá cháo tươi cho bé" |
| Thị trường | "thị trường thực phẩm trẻ em Việt Nam 2026 báo cáo" filetype:pdf |

## 5. Ghi vào kho
| Dữ liệu | Loại bản ghi / trường |
| --- | --- |
| URL, tên miền, ngày đăng, ngày đọc, trích ý chính | EVD: Nguồn, Nền tảng = "Google Search", Ngày đăng, Ngày thu thập, Nội dung quan sát, Loại nguồn (Chính thống/Công khai), Nguồn gốc dẫn lại |
| Từ khóa, thời điểm tìm, số kết quả đọc/dùng | MAU: Từ khóa, Phương pháp tìm kiếm ("Google, không đăng nhập, vị trí VN, 26/11/2026 10:00"), Số bản ghi thu thập/đọc được/sử dụng |
| Gợi ý, "Mọi người cũng hỏi", tìm kiếm liên quan | KEY: Từ khóa, Mục đích tìm kiếm, Giai đoạn hành trình, Nền tảng = "Google", Chỉ số quan tâm (Keyword Planner nếu có, còn lại "không có số") |
| Câu hỏi của khách trên diễn đàn | KH: Nhãn = Câu hỏi, Loại khách = Quan sát công khai |
| Số liệu thị trường, sự kiện | FIND (Dữ kiện), TT, XH, MV, RR (kèm Nguồn) |

## 6. Giới hạn và điều cấm
- Kết quả Google cá nhân hoá theo vị trí, lịch sử: ghi điều kiện tìm vào MAU; ưu tiên cửa sổ ẩn danh nếu người dùng đồng ý.
- Thứ tự kết quả và số "khoảng N kết quả" **không phải** lượng tìm kiếm. Chỉ Keyword Planner cho khoảng lượng tìm kiếm, và đó vẫn là khoảng ước tính.
- Không trích số liệu từ AI Overview hoặc đoạn mô tả mà không mở nguồn.
- Không dùng số liệu cũ hơn phạm vi RP mà không ghi rõ năm.
- Không chép nguyên văn bài báo dài; tóm tắt và dẫn link.

## 7. Đầu ra chuyển hoá
FIND, KEY, TT, XH → `insight`, `marketing-opportunities`; KEY → `y-tuong-content` (chủ đề SEO, câu hỏi FAQ); KH (Câu hỏi) → `toi-uu-chuyen-doi` (Kho FAQ).
