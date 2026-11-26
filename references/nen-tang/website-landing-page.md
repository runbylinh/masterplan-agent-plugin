# Website và landing page

## 1. Dùng cho
| Skill | Mục đích |
| --- | --- |
| quang-cao-chuyen-doi | Ma trận landing page, bản đồ chuyển đổi, độ nhất quán quảng cáo → điểm đến |
| competitor-research | Sản phẩm, giá, chính sách, định vị, thông điệp của đơn vị cùng ngành |
| company-analysis | Website của chính doanh nghiệp (thông tin, luồng chuyển đổi hiện tại) |
| toi-uu-chuyen-doi | Giả thuyết điểm nghẽn, đề xuất cải thiện |

## 2. Công cụ truy cập
- WebSearch để tìm trang; Claude in Chrome để đọc: `tabs_context_mcp` → `navigate` → `get_page_text` (nội dung), `read_page` (cấu trúc, nút, form), `find` (bảng giá, CTA), `computer` screenshot từng màn.
- **Xem trên khung điện thoại**: `resize_window` 390 × 844 rồi tải lại trang, chụp màn đầu tiên và các section chính; trả lại kích thước sau khi xong.
- Trang của doanh nghiệp làm trên LadiPage: connector LadiPage (`get_landing_page_html`, `report_landing_page_performance`) nếu có trong phiên và người dùng đồng ý.
- Trang cần đăng nhập, tường phí, CAPTCHA: dừng, ghi TH.

## 3. Các bước
1. Xác định trang: trang chủ, trang sản phẩm, landing page lấy từ link quảng cáo (Meta Ads Library "Xem chi tiết"), link trong bio, bài ghim.
2. Ghi sản phẩm, giá niêm yết và giá ưu đãi (riêng), combo, quà tặng, chính sách (đổi trả, bảo hành, hoàn tiền, vận chuyển, thanh toán).
3. Ghi **thứ tự thông tin** theo section từ trên xuống: tiêu đề màn đầu, vấn đề, giải pháp, lợi ích, bằng chứng, giá, FAQ, CTA. Đây là ma trận landing page.
4. Đánh giá định vị: lời hứa chính, khách mục tiêu được gọi tên, khác biệt được nêu.
5. Ghi bằng chứng (đánh giá, số khách, chứng nhận, trước/sau), ưu đãi (hạn, điều kiện), CTA (chữ nút, vị trí, số lần lặp).
6. Quan sát **luồng chuyển đổi đến bước trước khi gửi**: nút dẫn tới đâu (form, Messenger, Zalo, giỏ hàng, thanh toán), form hỏi những trường nào, có bao nhiêu bước. **Không điền form, không thêm giỏ, không thanh toán, không bấm Gửi.**
7. Xem lại trên khung điện thoại: màn đầu có thấy CTA không, chữ có đọc được, nút nổi có che nội dung.
8. So sánh giữa các trang; ghi giả thuyết cải thiện (ví dụ "đưa chính sách hoàn tiền lên màn đầu") là giả thuyết, không phải điểm nghẽn đã chứng minh.

## 4. Chọn trang (ví dụ giả định: Brand mẫu bán khoá học thiết kế)
| Nguồn trang | Số lượng |
| --- | --- |
| Landing page từ quảng cáo đang chạy của 5 đơn vị cùng ngành | 5–8 trang |
| Trang sản phẩm chính của từng đơn vị | 5 trang |
| Landing page của chính doanh nghiệp | 1–2 trang (đối chiếu) |

## 5. Ghi vào kho
| Dữ liệu | Loại bản ghi / trường |
| --- | --- |
| URL, ngày xem, ảnh chụp desktop và điện thoại | EVD: Nguồn, Nền tảng = "Website", Ngày thu thập, Nội dung quan sát, Loại nguồn = Công khai (hoặc Nội bộ với trang của doanh nghiệp), Ảnh chụp |
| Danh sách trang, cách tìm | MAU: Nguồn, Phương pháp tìm kiếm (từ quảng cáo/tìm kiếm), Tiêu chí đưa vào, ba con số, Nguồn không truy cập được |
| Section, thông điệp, bằng chứng, CTA | LP: Bảng = Ma trận landing page, Trang hoặc điểm chạm, Section, Mục đích, Thông điệp, Bằng chứng, CTA |
| Các bước từ quảng cáo đến chuyển đổi | LP: Bảng = Bản đồ chuyển đổi, Hành động, Rào cản (giả thuyết) |
| Giá, combo, chính sách | UD: Đơn vị, Sản phẩm, Giá, Combo, Chính sách, Thời gian, Cách trình bày |
| Định vị, lời hứa | TN: Thông điệp, Lợi ích, Nhóm khách, Bằng chứng; DV: Định vị |

## 6. Giới hạn và điều cấm
- Giá và ưu đãi đổi nhanh: luôn ghi ngày xem; giá có thể khác theo khu vực, thiết bị, mã giới thiệu.
- Không biết tỷ lệ chuyển đổi của trang đối thủ: chỉ ghi "giả thuyết điểm nghẽn".
- Không điền form, không gửi thông tin thử, không tạo tài khoản, không thêm giỏ, không thanh toán, không chat với tư vấn.
- Không dùng script tải toàn bộ trang hay vượt tường phí.

## 7. Đầu ra chuyển hoá
LP → `toi-uu-chuyen-doi` (CRO: Định hướng landing page, Bản đồ điểm nghẽn); UD → `san-pham-uu-dai`; TN, DV → `competitor-research` (KT), `dinh-vi-thong-diep`.
