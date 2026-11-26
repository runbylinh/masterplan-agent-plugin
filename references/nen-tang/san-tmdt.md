# Sàn thương mại điện tử (Shopee, TikTok Shop, Lazada)

## 1. Dùng cho
| Skill | Mục đích |
| --- | --- |
| customer-research | Kỳ vọng, tiêu chí chọn, vấn đề sau mua trong đánh giá của khách đã mua |
| competitor-research | Sản phẩm, giá, ưu đãi, combo, cách trình bày của gian hàng cùng ngành |
| san-pham-uu-dai | Mức giá phổ biến, combo, quà tặng, sản phẩm thay thế |
| tu-khoa | Gợi ý tìm kiếm trong sàn (ý định mua rõ) |

## 2. Công cụ truy cập
- Claude in Chrome: `tabs_context_mcp` → `navigate`:
  - Shopee: `https://shopee.vn/search?keyword=<từ khóa>` (Sắp xếp: Liên quan, Mới nhất, Bán chạy, Giá).
  - Lazada: `https://www.lazada.vn/catalog/?q=<từ khóa>`.
  - TikTok Shop: tìm trong `https://www.tiktok.com/search?q=<từ khóa>` tab Cửa hàng/Sản phẩm (nếu hiện), hoặc link sản phẩm người dùng đưa.
- Trang sản phẩm: `get_page_text` cho mô tả, giá, phân loại; khu **Đánh giá sản phẩm** có bộ lọc theo sao, "Có bình luận", "Có hình ảnh/video".
- Shopee thường bắt đăng nhập hoặc xác minh trượt hình sau vài trang: dừng, nhờ người dùng; không được thì ghi TH và dùng sàn khác.

## 3. Các bước
1. Từ ngành, nhu cầu, sản phẩm, viết 5–8 từ khóa; ghi gợi ý tìm kiếm của sàn.
2. Mỗi từ khóa: ghi thời điểm tìm, cách sắp xếp, 20 sản phẩm đầu (tên, giá, "Đã bán", điểm sao, gian hàng Mall/thường).
3. Chọn 8–15 sản phẩm: bán chạy, tầm trung, mới; cùng nhóm và **sản phẩm thay thế** (giải pháp khác cho cùng nhu cầu).
4. Trang sản phẩm: giá niêm yết/giá bán, voucher, combo, quà tặng, phân loại, chính sách đổi trả, cách trình bày (ảnh đầu, video, tiêu đề chứa từ khóa gì).
5. Đọc đánh giá cân bằng: lọc **1–2 sao** (10 bài), **3 sao** (5–10 bài), **5 sao có bình luận** (10 bài); bỏ đánh giá chỉ khen chung chung hoặc nghi đổi xu.
6. Gắn nhãn: Nhu cầu, Kỳ vọng (Tiêu chí lựa chọn), Vấn đề sau mua (giao hàng, đóng gói, chất lượng khác mô tả, size), Lý do mua lại.
7. So sánh theo nhóm sản phẩm và mức giá: kỳ vọng nào xuất hiện ở mọi nhóm, vấn đề nào chỉ ở nhóm giá thấp.
8. Ghi giả thuyết sản phẩm và thông điệp (ví dụ "nhấn bảng size chi tiết vì 9/40 đánh giá tiêu cực về size").

## 4. Xây từ khóa (ví dụ giả định: Brand mẫu bán bình giữ nhiệt)
| Lớp | Ví dụ |
| --- | --- |
| Sản phẩm | "bình giữ nhiệt 500ml", "ly giữ nhiệt có ống hút" |
| Nhu cầu | "bình giữ nhiệt văn phòng", "bình nước cho bé đi học" |
| Thay thế | "bình nhựa tritan", "cốc sứ có nắp" |
| Ưu đãi | "combo bình giữ nhiệt quà tặng" |

## 5. Ghi vào kho
| Dữ liệu | Loại bản ghi / trường |
| --- | --- |
| Link sản phẩm, ngày xem, quan sát | EVD: Nguồn, Nền tảng = "Shopee"/"TikTok Shop"/"Lazada", Ngày đăng (của đánh giá), Ngày thu thập, Nội dung quan sát, Loại nguồn = Công khai, Phạm vi mẫu |
| Từ khóa, sắp xếp, bộ lọc, số bài | MAU: Từ khóa, Phương pháp tìm kiếm, Tiêu chí đưa vào/loại trừ, ba con số, Giới hạn của mẫu |
| Giá, voucher, combo, chính sách | UD: Đơn vị, Sản phẩm, Giá, Combo, Chính sách, Thời gian, Quà tặng, Cách trình bày |
| Đánh giá đã ẩn danh | KH: Nhãn, Nội dung, Loại khách = Đã mua (quan sát công khai), Nguồn |
| Gian hàng cùng ngành | DV: Tên, Phân loại (Trực tiếp/Thay thế), Giá, Phản hồi tích cực/tiêu cực |
| Gợi ý tìm kiếm trong sàn | KEY: Nền tảng, Mục đích tìm kiếm = Giao dịch |
| Mẫu lặp | FIND: Nhóm = Khách hàng/Cạnh tranh, Số lần xuất hiện |

## 6. Giới hạn và điều cấm
- "Đã bán" là số sàn hiển thị (có thể làm tròn, cộng dồn nhiều phân loại, nhiều năm): ghi đúng như hiển thị, không quy ra doanh thu hay thị phần.
- Thứ tự kết quả chịu ảnh hưởng quảng cáo trong sàn (nhãn "Tài trợ"): ghi rõ.
- Đánh giá có thể được khuyến khích bằng xu/quà: ưu tiên đánh giá có chi tiết cụ thể.
- Ẩn danh người đánh giá (sàn đã che một phần tên, vẫn không ghi).
- Không thêm giỏ, không đặt hàng, không lưu voucher, không chat với gian hàng, không theo dõi shop.

## 7. Đầu ra chuyển hoá
KH → `customer-research`, `insight`; UD → `san-pham-uu-dai` (OFFER), `competitor-research` (KT); vấn đề sau mua → `toi-uu-chuyen-doi` (Kho FAQ, xử lý từ chối).
