# Marketing Audit năm (tổng hợp Review doanh nghiệp – Phần 1)

Mục tiêu: một bản **Marketing Audit <năm>** duy nhất cho chủ doanh nghiệp: khách hàng phản hồi gì, các kênh ra sao,
nội dung nào hiệu quả, quảng cáo đã chi bao nhiêu, kết quả kinh doanh thế nào. Đây là đầu vào cho Market Research,
dự báo và định hướng chiến lược. **Không** lập chiến lược, không phân bổ ngân sách ở bước này.

## Đầu vào (đọc kết quả mới nhất đã duyệt trong thư mục làm việc)
| Mảng | File | Skill tạo |
| --- | --- | --- |
| Thông tin doanh nghiệp | `company-context.md`, `cau-hinh.json` | setup |
| Kênh social | `danh-gia-kenh/*/chi-so.json`, `nhan-dinh.json` | danh-gia-kenh |
| Hội thoại, lead | `lead-hoi-thoai/*/chi-so-lead.json`, `nhan-dinh.json` | lead-hoi-thoai |
| Thương hiệu, phản hồi công khai | `thuong-hieu/*/ket-qua.json` | ra-soat-thuong-hieu |
| Doanh thu, đơn, sản phẩm | `kinh-doanh/*/chi-so-kd.json` | bao-cao-kinh-doanh |
| Chi phí quảng cáo + chi phí khác | `chi-phi-ads/*/chi-so-chi-phi.json` | chi-phi-ads |
| Nguồn lực | `company-context.md` mục nhân sự | setup |

Ưu tiên kết quả phủ cả năm review (hoặc kỳ dài nhất có). Kết quả kỳ ngắn (7–30 ngày) ghi rõ là "ảnh chụp kỳ ngắn",
không suy rộng thành cả năm. Mảng nào chưa có: ghi vào `thieu` và gợi ý lệnh để bổ sung.

## Cấu trúc báo cáo (5 phần)
1. **Khách hàng**: khách hỏi và quan tâm gì; lý do mua, chưa mua; vấn đề lặp lại; nhu cầu chưa được đáp ứng.
2. **Thương hiệu & kênh**: hình ảnh, giá trị khác biệt; tình hình từng kênh (vai trò, kết luận); kênh/nội dung nổi bật; điểm cần cải thiện.
3. **Kết quả quảng cáo**: chi Meta/TikTok/Google theo tháng; kết quả và chi phí/kết quả; chiến dịch, giai đoạn đáng chú ý.
4. **Kinh doanh & chi phí**: doanh thu, đơn, sản phẩm nổi bật; tổng chi Marketing (quảng cáo + khác, đã kiểm trùng);
   mối liên hệ Marketing – kinh doanh **chỉ khi có bằng chứng**.
5. **Nguồn lực & giới hạn vận hành**: người, thời gian, công cụ; điểm nghẽn.

Mỗi phần: Kết quả · Đang làm tốt · Vấn đề · Bằng chứng (nguồn, kỳ) · Dữ liệu còn thiếu.

## Kết luận cuối
- **3 điểm mạnh** cần phát huy.
- **3–5 vấn đề** cần ưu tiên nghiên cứu hoặc cải thiện năm sau (mỗi vấn đề kèm bằng chứng).
- **Câu hỏi chuyển sang Market Research**: khách đang đổi nhu cầu thế nào, thị trường và đơn vị cùng ngành có diễn biến gì,
  vấn đề Marketing nào cần giải quyết, cơ hội nào đáng xem.

## Bảng đầu ra (`ket-qua.json`, loai `review-nam`)
| Phần | Cột | csv / tab |
| --- | --- | --- |
| Tổng quan theo mảng | Mảng · Kết quả · Đang làm tốt · Vấn đề · Bằng chứng · Kỳ dữ liệu · Còn thiếu | `review-tong-quan` / `Audit – Tổng quan` |
| Vấn đề ưu tiên | Vấn đề · Bằng chứng · Ảnh hưởng · Cần nghiên cứu thêm | `review-van-de` / `Audit – Vấn đề` |
