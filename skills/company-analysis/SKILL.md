---
name: company-analysis
description: Đọc hồ sơ doanh nghiệp, xác định vấn đề Marketing, dữ liệu còn thiếu và lập Brief nghiên cứu cho giai đoạn Company của quy trình 3C. Dùng khi người dùng gõ /masterplan-agent:company-analysis hoặc nói "phân tích doanh nghiệp", "lập brief nghiên cứu", "xác định bài toán".
---

# Phân tích doanh nghiệp (Company)

## Mục đích
Hiểu vấn đề kinh doanh thật trước khi đi tìm trend. Kết quả là Brief nghiên cứu bám bài toán kinh doanh,
không bắt đầu từ trend không liên quan.

## Đầu vào
- `company-context.md` (và `ho-so-doanh-nghiep.md` nếu có)
- Tài liệu bổ sung nếu có (menu, Content Calendar, báo cáo quảng cáo, hội thoại đã ẩn danh)
- Chủ đề hoặc dịp cần nghiên cứu

## Cách làm
1. Tóm tắt tình hình: sản phẩm, khách hàng, Marketing hiện tại, bán hàng, nguồn lực, số liệu.
   Chỉ dùng số liệu CÓ trong tài liệu.
2. So sánh số liệu hai mốc (cùng kỳ năm trước và hiện tại): doanh thu, lượng khách/đơn, chi phí vận hành,
   chi phí quảng cáo. Tính mức thay đổi bằng phép tính rõ ràng, nêu công thức nếu cần.
3. Tách ba nhóm:
   - (a) Vấn đề đã có số liệu chứng minh.
   - (b) Nguyên nhân mới chỉ là giả thuyết, chưa kiểm chứng.
   - (c) Dữ liệu cần lấy thêm để kiểm chứng.
4. Xem hành trình khách và tìm điểm rơi rụng:
   thấy nội dung → hỏi → xác nhận (đặt chỗ/đơn) → khách thực đến/mua → hóa đơn → quay lại.
   Ghi rõ khúc nào đã có dữ liệu, khúc nào chưa.
5. Gợi ý dữ liệu nội bộ nên thu thập nếu có: lượng khách theo ngày/ca; khách mới và quay lại; số hỏi giá,
   xác nhận, hủy/không đến; thời gian trả lời; phản hồi về sản phẩm và phục vụ.
6. Đề xuất phạm vi nghiên cứu cho dịp được giao: ngành, khu vực, mức giá, hai mốc thời gian,
   nhóm khách ưu tiên, sản phẩm ưu tiên.

## Quy tắc
- Không tự đặt số liệu. Thiếu số liệu thì ghi vào cột "Nguồn cần tìm thêm".
- Không kết luận nguyên nhân chắc chắn (ví dụ "do kinh tế khó khăn", "do đối thủ giảm giá") khi chưa có bằng chứng.
- Phân biệt hiện tượng (doanh thu giảm) với nguyên nhân (chưa biết).
- Không đề xuất giải pháp ở giai đoạn này.

## Đầu ra: `01-brief.md`
1. **Tóm tắt tình hình** (5 đến 8 dòng).
2. **Bảng so sánh hai mốc**: Chỉ số | Mốc A | Mốc B | Thay đổi.
3. **Bảng vấn đề**: Vấn đề | Dữ liệu đã biết | Giả thuyết cần kiểm chứng | Nguồn cần tìm thêm.
4. **Hành trình khách**: khúc nào đã có dữ liệu, khúc nào chưa.
5. **Câu hỏi nghiên cứu cho Customer** (ít nhất 3).
6. **Câu hỏi nghiên cứu cho Competitor** (ít nhất 3).
7. **Phạm vi nghiên cứu**: ngành, khu vực (hoặc "chưa rõ, cần hỏi"), mức giá, hai mốc thời gian.
8. **Thông tin còn thiếu cần người dùng bổ sung**.

## Tiêu chuẩn kiểm tra trước khi giao
- [ ] Mọi số liệu có trong tài liệu gốc.
- [ ] Hiện tượng và nguyên nhân được tách riêng.
- [ ] Có ít nhất 3 câu hỏi cho mỗi nhánh nghiên cứu.
- [ ] Không có kết luận nguyên nhân chắc chắn.

Kết thúc: dừng, hỏi người dùng duyệt Brief.
