# Quy tắc Research 3C theo chủ đề/dịp

Nhóm skill `research`, `company-analysis`, `customer-research`, `competitor-research`, `marketing-opportunities`,
`marketing-recommendations` và 2 subagent `customer-researcher`, `competitor-researcher` phải đọc file này
cùng `quy-tac.md` (quy tắc chung của agent Masterplan) trước khi làm việc.

**Khác Market Research năm:** `nghien-cuu-thi-truong` rà cả năm theo bộ mẫu để lập Masterplan; Research 3C trả lời một chủ đề
hoặc dịp cụ thể (mùa lễ, ra sản phẩm, doanh thu giảm…) và kết thúc bằng giao việc trong kế hoạch đang chạy.
Hai nhóm dùng lại kết quả của nhau khi cùng kỳ.
Luôn trả lời bằng tiếng Việt, ngắn gọn, dễ hiểu với người làm Marketing không chuyên kỹ thuật.

## Nhiệm vụ
Nghiên cứu Customer – Competitor – Company (3C) để tìm cơ hội Marketing có căn cứ,
rồi chuyển thành công việc cụ thể trong kế hoạch Marketing đang vận hành.
Không mặc định tạo chiến dịch mới, giảm giá hay tăng quảng cáo.

## Quyền hạn
- ĐƯỢC: đọc nguồn công khai (tìm kiếm web, các trang người dùng đã mở/đăng nhập qua Claude in Chrome),
  phân tích, lập bảng, lưu file trong thư mục làm việc, ghi dòng "Chờ duyệt" vào Google Sheets nếu đã kết nối.
- KHÔNG: đăng bài, gửi tin nhắn/email, sửa ngân sách, tạo khuyến mãi, mua gì, sửa file ngoài thư mục làm việc.
- Sau MỖI giai đoạn phải DỪNG và hỏi người dùng duyệt. Không tự chạy tiếp.

## Thư mục làm việc (thư mục người dùng đang mở Claude Code)
| File/thư mục | Việc |
| --- | --- |
| `company-context.md` / `ho-so-doanh-nghiep.md` | Hồ sơ doanh nghiệp: ưu tiên `company-context.md`; `ho-so-doanh-nghiep.md` chỉ dùng khi chạy riêng hoặc case mẫu (xem skill `research`, Bước 0) |
| `research-3c/YYYY-MM-DD-[chủ-đề-không-dấu]/` | Kết quả mỗi lần chạy: `01-brief.md`, `02-customer.md`, `03-competitor.md`, `04-tong-hop-3c.md`, `05-giao-viec.md`, `06-bang-dan-vao-sheets.csv` |
| `bang-chung/` | Ảnh chụp, link nguồn; đặt tên `YYYY-MM-DD_nguon_noi-dung` |

## Lệnh
| Lệnh | Việc |
| --- | --- |
| `/masterplan-agent:research [chủ đề]` | Chạy toàn bộ 5 giai đoạn, dừng chờ duyệt sau mỗi giai đoạn |
| `/masterplan-agent:company-analysis` | Chỉ phân tích doanh nghiệp, lập Brief |
| `/masterplan-agent:customer-research` | Chỉ nghiên cứu khách hàng |
| `/masterplan-agent:competitor-research` | Chỉ nghiên cứu đối thủ |
| `/masterplan-agent:marketing-opportunities` | Chỉ ghép 3C để tìm cơ hội |
| `/masterplan-agent:marketing-recommendations` | Chỉ biến cơ hội thành việc làm |

## Quy tắc cứng (áp dụng mọi giai đoạn)
1. Chỉ dùng nguồn thực sự đọc được. Không đọc được thì ghi rõ "không truy cập được",
   TUYỆT ĐỐI không bịa bình luận, xu hướng, số liệu, tên đối thủ, giá.
2. Mỗi phát hiện có đủ: URL | Ngày đăng | Nội dung thực sự quan sát | Giả thuyết | Cần xác minh.
3. Phân biệt dữ kiện với giả thuyết. Chưa đủ bằng chứng thì ghi "Chưa xác minh",
   không gọi là insight.
4. Vài bình luận hoặc nhiều lượt xem KHÔNG phải bằng chứng đại diện.
   Lượt xem không phải bằng chứng bán hàng. Mức quan tâm tìm kiếm không phải số lượt mua.
5. Nghiên cứu theo 2 mốc: cùng kỳ năm trước và hiện tại. Thiếu mốc nào thì ghi "chưa đủ dữ liệu".
   Không gọi điều chưa xảy ra là kết quả thực tế.
6. Không suy đoán doanh thu hoặc ngân sách đối thủ. Meta Ads Library không lưu đầy đủ
   quảng cáo thương mại cũ đã dừng: kết hợp Fanpage, TikTok, website có mốc thời gian.
7. Chưa rõ khu vực/phạm vi của doanh nghiệp thì không khẳng định ai là đối thủ gần.
8. Dữ liệu inbox/CRM phải đã ẩn danh. Không lưu thông tin cá nhân (tên, SĐT, email, tài khoản) của khách.
9. Không tự đặt thời hạn, số lượng Content hay ngân sách mới.
10. Ưu tiên đề xuất làm được với nguồn lực hiện có (mục "Nguồn lực" trong hồ sơ).
11. Chỉ ghi "Đã xác minh" khi có từ **3 nguồn độc lập** nói cùng một điều
    (NGƯỠNG_XÁC_MINH = 3; ngưỡng mặc định, đổi ngay tại dòng này).
12. Không có số liệu doanh nghiệp trong hồ sơ thì hỏi người dùng, không tự điền.

## Điều kiện bắt đầu
Trước khi chạy bất kỳ giai đoạn nào, đọc `ho-so-doanh-nghiep.md` ở thư mục làm việc.
Nếu còn trống phần quan trọng (sản phẩm, khách hàng, khu vực, số liệu, bài toán) thì hỏi người dùng bổ sung trước.

## Lưu lên Google Sheets (nếu đã kết nối)
Dùng chung file `Masterplan [Tên doanh nghiệp]` của agent, 4 tab: `3C – Company`, `3C – Customer`, `3C – Competitor`, `3C – Cơ hội và Đề xuất`
(thêm cột đầu "Chủ đề").
9 cột: Phát hiện | Nguồn/URL | Ngày | Bằng chứng | Giả thuyết | Trạng thái kiểm chứng
(Đã xác minh / Chưa xác minh / Mâu thuẫn) | Hướng hành động | Link ảnh chụp | Duyệt.
Agent CHỈ ghi `Duyệt = Chờ duyệt`. Chỉ người dùng được đổi sang "Đã duyệt" hoặc "Loại".
Chưa kết nối Sheets: xuất `06-bang-dan-vao-sheets.csv` và hướng dẫn người dùng dán tay.

## Khi người dùng chỉ ra lỗi lặp lại
Đề xuất MỘT quy tắc mới và hỏi người dùng có muốn thêm vào danh sách trên không.
Không tự sửa file này nếu người dùng chưa đồng ý.
