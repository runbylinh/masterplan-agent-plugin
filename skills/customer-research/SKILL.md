---
name: customer-research
description: Nghiên cứu nhu cầu, hành vi, rào cản mua/đặt chỗ và giả thuyết insight của khách hàng từ TikTok, Google Search/Trends, Facebook Group, review, bình luận và inbox ẩn danh, theo hai mốc thời gian. Dùng cho nhánh Customer của quy trình 3C hoặc khi người dùng gõ /masterplan-agent:customer-research, nói "nghiên cứu khách hàng", "tìm insight", "khách đang phân vân gì".
---

# Nghiên cứu khách hàng (Customer)

## Mục đích
Biết khách muốn đi ăn/mua trong tình huống nào, tìm thế nào, đang nghi ngại điều gì và vì sao chưa quyết định.
Kết quả là bảng nhu cầu, rào cản và GIẢ THUYẾT insight có dẫn chứng, chưa phải kết luận.

## Đầu vào
- `01-brief.md` (câu hỏi cho Customer), sản phẩm, dịp, khu vực
- Hai mốc thời gian (Mốc A: cùng kỳ năm trước, Mốc B: hiện tại)
- Danh sách nguồn người dùng đã mở/cho phép đọc

## Nguồn và cách tìm
| Nguồn | Cách làm | Cần lưu |
| --- | --- | --- |
| TikTok Search | Tìm theo [sản phẩm + dịp], [nhu cầu/tình huống], [vấn đề thường gặp]; mở video có liên quan và phần bình luận | Video, ngày, bối cảnh, bình luận nghi ngờ/hỏi giá/phản hồi sau khi dùng |
| Google Search / Trends | Từ khóa, câu hỏi tìm kiếm, thay đổi theo mùa (so hai mốc) | Từ khóa, mức quan tâm, ngày |
| Facebook Group | Tìm bài xin tư vấn, so sánh, tìm mua/tìm quán | Tiêu chí chọn, vấn đề chưa được giải |
| Review / Comment (Google Maps, Fanpage) | Đọc cả khen và chê, ưu tiên phản hồi mới và trái chiều | Điều khách khen, chê, phân vân |
| Inbox / lịch đặt chỗ (đã ẩn danh) | Đọc nhật ký tư vấn, đối chiếu hỏi → xác nhận → hủy | Câu hỏi lặp lại, điểm rơi rụng |

Nếu không có công cụ đọc trang (Claude in Chrome) hoặc trang bị chặn: ghi rõ "không truy cập được",
hỏi người dùng cung cấp nội dung công khai đã lấy được kèm link. KHÔNG tự điền.

## Gợi ý từ khóa và tình huống mẫu (ví dụ case LÁ É QUÁN, đổi theo ngành khác)
Từ khóa TikTok/Maps: `lẩu gà lá é Hà Nội`, `review lẩu gà lá é`, `lẩu gà lá é có ngon không`,
`quán lẩu đi nhóm Hà Nội`, `ăn lẩu mùa đông Hà Nội`, `liên hoan cuối năm Hà Nội`, `ăn gì trời lạnh Hà Nội`.

Tình huống cần dò (là GIẢ THUYẾT để kiểm chứng, chưa phải insight đã xác thực):
| Tình huống | Dấu hiệu cần tìm |
| --- | --- |
| Không tin review, nghi seeding | Comment "review có thật không?", ý kiến trái chiều giữa review và khách đã đến |
| Không tin video booking/KOL | Người xem nghi quảng cáo, hỏi trải nghiệm thật, bình luận sau khi đi ăn |
| Đi nhóm sợ tốn hoặc phát sinh phí | Hỏi tổng tiền nhóm 4–6 người, giá combo, lượng đồ ăn, phụ phí |
| Sợ thực tế khác ảnh quảng bá | Review về không gian, gửi xe, chờ món, chất lượng và khẩu phần |
| Không biết có hợp khẩu vị cả nhóm | Hỏi vị lá é, độ cay, phần ăn, trẻ nhỏ, cách chọn món |

## Cách làm
1. Chọn tình huống và từ khóa từ Brief. Mở từng nguồn, đọc nội dung thật.
2. Sàng lọc: ưu tiên phản hồi cụ thể, có ngữ cảnh và ngày đăng; đọc cả khen lẫn chê. Ghi lý do bỏ nguồn nào.
3. Ghi nhận: nhu cầu, tình huống (đi với ai, dịp nào), câu hỏi, rào cản, lý do chọn hoặc chưa mua.
4. Chia dữ liệu theo hai mốc: Mốc A (cùng kỳ năm trước) và Mốc B (hiện tại). Đối chiếu:
   nhu cầu nào tiếp diễn? có tình huống mới không? rào cản có đổi không? điều gì liên quan trực tiếp sản phẩm?
5. Với nguồn quan trọng: chụp ảnh vào `bang-chung/` (nếu có khả năng) hoặc ghi rõ URL và ngày.
6. Đánh dấu trạng thái từng phát hiện: Đã xác minh / Chưa xác minh / Mâu thuẫn
   (theo NGƯỠNG_XÁC_MINH trong quy tắc chung).

## Quy tắc kiểm chứng
- Một bình luận riêng lẻ là ý kiến cá nhân, KHÔNG gộp thành insight.
- Trích dẫn nguyên văn, có URL và ngày đăng. Không diễn đạt lại rồi coi như trích dẫn.
- Nêu cả phản hồi trái chiều.
- Lượt xem không phải bằng chứng bán hàng. Mức quan tâm tìm kiếm không phải số lượt mua.
- Không gán review là "giả" hoặc kết luận "mọi khách đều mất niềm tin".
- Không coi tháng chưa diễn ra là dữ liệu đã có.

## Xử lý thiếu và mâu thuẫn
- Thiếu bằng chứng: "Chưa xác minh".
- Nguồn mâu thuẫn: ghi cả hai, đánh dấu "Mâu thuẫn", hỏi người dùng.
- Thiếu một mốc: "chưa đủ dữ liệu".
- Nguồn không đọc được: ghi rõ, không suy đoán.

## Đầu ra: `02-customer.md`
**Bảng 1 – Nhu cầu và rào cản**
Nhu cầu/vấn đề | Bằng chứng quan sát được (trích nguyên văn) | Ngữ cảnh khách | URL và ngày | Mức tin cậy | Cần kiểm chứng thêm

**Bảng 2 – Đối chiếu hai mốc**
Chủ đề | Bằng chứng Mốc A | Bằng chứng Mốc B | Tiếp diễn hay thay đổi | Hàm ý cần kiểm chứng

**Phần cuối**: danh sách nguồn không truy cập được; các giả thuyết insight (đánh dấu rõ là giả thuyết);
câu hỏi cần kiểm chứng thêm.

## Tiêu chuẩn kiểm tra trước khi giao
- [ ] Mọi dòng có URL và ngày.
- [ ] Không có bình luận bịa; trích dẫn nguyên văn.
- [ ] Dữ kiện tách khỏi giả thuyết.
- [ ] Có ghi rõ nguồn không đọc được.
- [ ] Có đủ hai mốc hoặc ghi "chưa đủ dữ liệu".

Kết thúc: dừng, hỏi người dùng duyệt.
