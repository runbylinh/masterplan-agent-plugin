# Rà soát thương hiệu, Website và phản hồi công khai

Phần này thuộc **Review doanh nghiệp (Phần 1)**. Kênh social đo bằng `danh-gia-kenh`, Inbox bằng `lead-hoi-thoai`.
Skill `ra-soat-thuong-hieu` lo hai việc còn lại: hình ảnh thương hiệu mà khách nhìn thấy, và phản hồi công khai của khách.

## A. Thương hiệu và Website: 7 câu hỏi
| # | Câu hỏi | Xem ở đâu |
| --- | --- | --- |
| 1 | Khách có hiểu doanh nghiệp bán gì, cho ai không? (định vị, nhóm khách) | Trang chủ, giới thiệu, bio các kênh |
| 2 | Giá trị khác biệt có rõ và nhất quán không? | Trang chủ, landing page, bài ghim, ảnh bìa |
| 3 | Thông tin sản phẩm, giá, chính sách có đủ không? | Trang sản phẩm/dịch vụ, bảng giá, chính sách đổi trả/bảo hành |
| 4 | Có bằng chứng tạo niềm tin không? (đánh giá, case, số liệu, chứng nhận, báo chí) | Website, Google Maps, Social |
| 5 | Hình ảnh và thông điệp có thống nhất giữa Website và Social không? | So màu, logo, câu khẩu hiệu, giọng văn |
| 6 | Khách có dễ tìm thông tin và liên hệ không? (nút liên hệ, form, hotline, Zalo, tốc độ trang trên điện thoại) | Website trên khung điện thoại |
| 7 | Định vị doanh nghiệp **mong muốn** (company-context.md) khác gì với điều khách **quan sát được**? | Đối chiếu |

Ghi cho mỗi câu: Kết quả · Điểm mạnh · Điểm chưa rõ/thiếu · Bằng chứng (URL, ảnh chụp) · Hướng cải thiện.
Không tự kết luận tỷ lệ chuyển đổi khi không có số Analytics. Không khẳng định mức nhận biết thương hiệu toàn thị trường.

## B. Bình luận và đánh giá công khai: 5 câu hỏi
Nguồn:
- Facebook: Meta Business Suite → Nội dung → mở bài/Reels → Bình luận (ưu tiên bài nhiều bình luận trong kỳ).
- Google Maps: tìm tên doanh nghiệp → đúng địa điểm → Đánh giá → sắp xếp "Mới nhất" (và đọc thêm 1–2 sao).
- TikTok/YouTube: bình luận dưới video nhiều lượt xem.
- Shopee/TikTok Shop: đánh giá sản phẩm (ưu tiên 1 sao và 3–4 sao, vì có lý do cụ thể).
- Kết quả `lead-hoi-thoai` (câu hỏi thường gặp, lý do không chốt) nếu đã có.

Trả lời:
1. Khách khen điều gì?
2. Khách phàn nàn điều gì?
3. Câu hỏi hoặc vấn đề nào lặp lại?
4. Khách chưa hài lòng ở sản phẩm, giá, dịch vụ hay trải nghiệm nào?
5. Phản hồi nào ảnh hưởng đến niềm tin và quyết định mua?

Bảng: Chủ đề · Phản hồi tiêu biểu (viết lại ngắn, ẩn danh) · Số lần gặp / cỡ mẫu · Điểm tốt · Vấn đề · Hướng cải thiện · Nguồn.
Nhóm chủ đề gợi ý: giá, sản phẩm/chất lượng, chính sách, giao hàng/lịch, dịch vụ/tư vấn, kết quả sau mua, uy tín.

## C. Google Maps / Business Profile (nếu có quyền quản lý)
Business Profile → Hiệu suất: lượt xem hồ sơ, lượt gọi, chỉ đường, click website trong kỳ. Chỉ đọc.

## Bảng đầu ra (`ket-qua.json`, loai `thuong-hieu`)
| Phần | Cột | csv / tab |
| --- | --- | --- |
| Thương hiệu & Website | Câu hỏi · Kết quả · Điểm mạnh · Điểm chưa rõ · Bằng chứng · Hướng cải thiện | `thuong-hieu-website` / `TH – Website` |
| Phản hồi công khai | Chủ đề · Phản hồi tiêu biểu · Số lần / cỡ mẫu · Điểm tốt · Vấn đề · Hướng cải thiện · Nguồn | `phan-hoi-cong-khai` / `TH – Phản hồi` |
| Google Business Profile | Chỉ số · Kỳ này · Kỳ trước · Nguồn | `google-business` / `TH – Google Maps` (nếu có) |
