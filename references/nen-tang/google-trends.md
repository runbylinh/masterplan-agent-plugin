# Google Trends

## 1. Dùng cho
| Skill | Mục đích |
| --- | --- |
| xu-huong-mua-vu | Xu hướng dài hạn, đỉnh mùa vụ, biến động nhu cầu, tín hiệu mới |
| tu-khoa | So sánh mức quan tâm tương đối giữa các cụm, truy vấn liên quan đang tăng |
| marketing-opportunities | Chọn thời điểm chiến dịch (thời gian chuẩn bị trước đỉnh) |

## 2. Công cụ truy cập
- Claude in Chrome: `tabs_context_mcp` → `navigate` tới `https://trends.google.com/trends/explore?geo=VN&q=<từ khóa>&date=today%2012-m`.
- Đọc biểu đồ: `get_page_text` thường không lấy được từng điểm; dùng `read_page` cho bảng truy vấn liên quan và `computer` screenshot cho biểu đồ (lưu ảnh vào `bang-chung/`). Nút **Tải xuống (CSV)** ở góc mỗi khối chỉ bấm khi người dùng đồng ý tải file.
- WebSearch không thay được Trends (không có số liệu chỉ số).
- Lỗi "429 / Đã xảy ra lỗi" do giới hạn truy cập: chờ, tải lại một lần; vẫn lỗi thì nhờ người dùng mở hoặc ghi TH.

## 3. Các bước
1. Chọn tối đa **5 từ khóa hoặc chủ đề** để so sánh cùng lúc (ưu tiên mục "Chủ đề" khi Trends gợi ý, vì gộp được các cách viết).
2. Đặt **địa bàn** (Việt Nam hoặc tỉnh/thành), **thời gian** (5 năm cho dài hạn, 12 tháng cho mùa vụ, 90 ngày cho biến động gần), **danh mục** (ví dụ Ăn uống, Mua sắm), **loại tìm kiếm** (Tìm kiếm web, Google Shopping, YouTube).
3. So sánh các chủ đề **trong cùng một biểu đồ** (cùng điều kiện). Không so chỉ số của hai lần tìm riêng.
4. Đọc xu hướng: tăng/giảm dài hạn (5 năm), đỉnh lặp lại theo năm (mùa vụ: tháng nào, bắt đầu tăng từ tuần nào), đỉnh đột biến không lặp (sự kiện).
5. Xem **Mức độ quan tâm theo tiểu vùng** khi cần chọn địa bàn.
6. Đọc **Truy vấn liên quan** và **Chủ đề liên quan**, cả hai chế độ **Hàng đầu** và **Tăng** (ghi "Đột phá" nếu có).
7. Đối chiếu nguồn khác: lịch sự kiện, báo chí, TikTok/Shopee cùng thời điểm, số liệu bán nội bộ nếu có.
8. Lưu **toàn bộ thiết lập** (từ khóa, địa bàn, thời gian, danh mục, loại tìm kiếm, ngày xem) và ảnh chụp vào EVD.

## 4. Chọn từ khóa (ví dụ giả định: Cửa hàng A bán bánh trung thu)
| Mục đích | Bộ so sánh |
| --- | --- |
| Mùa vụ | "bánh trung thu" · "hộp quà trung thu", VN, 5 năm, Tìm kiếm web |
| Xu hướng sản phẩm | "bánh trung thu ít đường" · "bánh trung thu handmade" · "bánh trung thu lạnh" |
| Kênh | Cùng từ khóa, đổi loại tìm kiếm sang YouTube hoặc Google Shopping |

## 5. Ghi vào kho
| Dữ liệu | Loại bản ghi / trường |
| --- | --- |
| URL explore (có tham số), ảnh biểu đồ, thiết lập, ngày xem | EVD: Nguồn, Nền tảng = "Google Trends", Ngày thu thập, Nội dung quan sát ("Đỉnh tuần 08–14/9 các năm 2022–2026, chỉ số 100"), Loại nguồn = Công khai, Ảnh chụp |
| Bộ từ khóa, điều kiện so sánh | MAU: Từ khóa, Phạm vi địa lý, Khoảng thời gian, Phương pháp tìm kiếm (danh mục, loại tìm kiếm), Giới hạn của mẫu |
| Đỉnh mùa vụ, thời gian chuẩn bị | MV: Thời điểm, Sự kiện, Nhu cầu, Thời gian chuẩn bị, Nguồn |
| Thay đổi giữa giai đoạn | BD: Chủ đề, Giai đoạn, Chỉ số ("Chỉ số Trends tương đối 0–100"), Biến động, Nguyên nhân giả định |
| Chủ đề đang tăng | XH: Phân loại = Tín hiệu mới/Mùa vụ, Đánh giá, Nguồn |
| Truy vấn liên quan | KEY: Chỉ số quan tâm = "Trends tương đối, <thiết lập>"; Tính mùa vụ |

## 6. Giới hạn và điều cấm
- Chỉ số 0–100 là **mức quan tâm tương đối** trong đúng bộ so sánh và khoảng thời gian; 100 là điểm cao nhất của bộ đó. **Không** phải lượng tìm kiếm tuyệt đối, không quy ra số người tìm hay số người mua.
- Từ khóa ít người tìm hiển thị 0 hoặc "không đủ dữ liệu": ghi đúng như vậy, không kết luận "không có nhu cầu".
- "Tăng +X%" trong truy vấn liên quan là so với kỳ trước của chính truy vấn đó, không so giữa các truy vấn.
- Trends lấy mẫu dữ liệu: cùng truy vấn xem hai ngày có thể lệch nhẹ; ghi ngày xem.
- Không suy ra nguyên nhân tăng/giảm khi chưa có nguồn đối chiếu (ghi "Nguyên nhân giả định").

## 7. Đầu ra chuyển hoá
MV, BD, XH → `marketing-opportunities` (thời điểm), `y-tuong-chien-dich`; KEY → `tu-khoa`, `y-tuong-content`; xu hướng dài hạn → `du-bao-xu-huong`.
