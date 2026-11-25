---
name: lead-hoi-thoai
description: Đánh giá hiệu quả lead và tư vấn qua tin nhắn — tự mở Meta Business Suite (Messenger + Instagram), Zalo OA, Zalo web (chat.zalo.me), TikTok tin nhắn trên Chrome để đếm số hội thoại theo kênh, tốc độ phản hồi, chất lượng lead (nóng/ấm/lạnh/không phù hợp), tỷ lệ chốt qua tin nhắn (theo nhãn, theo nội dung chat, đối chiếu file đơn/CRM), lý do không chốt và câu hỏi khách hay hỏi. Xuất báo cáo .md + HTML + Google Sheets, không lưu thông tin cá nhân khách. Dùng khi người dùng gõ /masterplan-agent:lead-hoi-thoai, nói "đánh giá lead", "chất lượng lead", "tỷ lệ chốt inbox", "sale chốt qua mess thế nào", "bao nhiêu hội thoại".
argument-hint: "[kỳ: 7 | 30 | 90 ngày]"
---

# /masterplan-agent:lead-hoi-thoai [kỳ]

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/lead-hoi-thoai.md`.
Cần `cau-hinh.json` (mục `hop_thu`, `lead`); chưa có thì chạy `masterplan-agent:setup`.

## Bước 0 – Chốt phạm vi (hỏi một lần)
1. **Kỳ** (mặc định 30 ngày, kết thúc hôm qua) và kỳ trước cùng độ dài.
2. **Hộp thư** sẽ đọc: Business Suite (Messenger, Instagram), Zalo OA, Zalo cá nhân (chat.zalo.me), TikTok tin nhắn.
   Nhờ người dùng đăng nhập sẵn trên Chrome.
3. **Cách xác định chốt** (dùng cả ba nếu có, ghi rõ con số đến từ cách nào):
   (a) nhãn trong hộp thư theo `hop_thu.nhan_chot`; (b) agent đọc nội dung chat; (c) đối chiếu file đơn / LadiWork.
4. **Đọc nội dung chat**: hỏi cỡ mẫu (mặc định tối đa 40 hội thoại mỗi kênh, chia đều theo nhãn) và
   xin phép mở hội thoại. Mở hội thoại có thể làm tin **chưa đọc** thành **đã đọc** với cả team:
   mặc định CHỈ mở hội thoại đã đọc; hội thoại chưa đọc chỉ mở khi người dùng cho phép.
5. Tạo `lead-hoi-thoai/YYYY-MM-DD_<so-ngay>d/`.

DỪNG. Tóm tắt phạm vi, hỏi "Bắt đầu chứ?"

## Bước 1 – Đếm tổng (không cần mở từng hội thoại)
Mỗi hộp thư, cả kỳ này và kỳ trước, theo `references/lead-hoi-thoai.md`:
- Số hội thoại mới, số theo từng nhãn, số chưa trả lời. Dùng bộ lọc ngày + nhãn của hộp thư.
- Business Suite: thêm số liệu ở **Hộp thư → Thông tin chi tiết** (tỷ lệ phản hồi, thời gian phản hồi) nếu có.
- Hội thoại đến từ quảng cáo (Business Suite gắn nhãn quảng cáo / Click-to-Messenger): đếm riêng.
- Lead form/landing page: LadiPage `report_leads_by_campaign` theo kênh (như skill đánh giá kênh).

## Bước 2 – Đọc mẫu hội thoại
Với từng hội thoại trong mẫu (chỉ đọc, không gõ, không gửi, không gắn/bỏ nhãn):
- Gán mã `HT-<kênh>-<số>`. KHÔNG ghi tên, SĐT, email, ảnh đại diện, link hồ sơ khách.
- Ghi: kênh, nguồn (quảng cáo / tự nhiên / không rõ), ngày bắt đầu, thời gian phản hồi đầu (phút),
  số tin, nhãn hiện có, nhu cầu (sản phẩm quan tâm), mức lead, trạng thái, lý do không chốt, câu hỏi chính,
  điểm tư vấn tốt/chưa tốt (1 câu, không trích nguyên văn dài).
- Phân loại theo bảng tiêu chí trong `references/lead-hoi-thoai.md`. Không chắc thì ghi `khong_ro`.

## Bước 3 – Đối chiếu đơn
Nếu có `hop_thu.file_don_hang` hoặc LadiWork: đếm số đơn theo kênh/nguồn trong kỳ.
Chỉ đối chiếu ở mức tổng theo kênh. Nếu phải khớp từng khách (theo SĐT) thì làm trong bộ nhớ, không ghi SĐT ra file.

## Bước 4 – Tính và báo cáo
Ghi `hoi-thoai.json` (định dạng ở `references/lead-hoi-thoai.md`), rồi:
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tinh_lead.py lead-hoi-thoai/<kỳ>
```
Ra `chi-so-lead.json`, `bao-cao.html`, `sheets/*.csv`. Đọc kết quả, viết `nhan-dinh.json` (`tom_tat`, `diem_nghen`,
`kich_ban_tot`, `uu_tien`) rồi chạy lại script để HTML có phần nhận định. Viết `bao-cao.md`:
- Phễu tin nhắn: hội thoại → lead đủ thông tin → đang tư vấn → chốt, theo kênh.
- Chất lượng lead theo kênh và theo nguồn (quảng cáo vs tự nhiên).
- Tốc độ phản hồi và tác động lên tỷ lệ chốt (nếu mẫu đủ).
- Top lý do không chốt, top câu hỏi, gợi ý sửa kịch bản tư vấn / FAQ / nội dung.
- Số nào đến từ nhãn, số nào từ mẫu đọc chat (ghi cỡ mẫu), số nào từ file đơn.

DỪNG. Báo cáo 5 dòng, hỏi duyệt. Sau duyệt ghi Google Sheets tab `Lead & hội thoại` (append, `Duyệt = Chờ duyệt`).

## Không được
- Gửi, trả lời, xoá, lưu trữ, gắn/bỏ nhãn tin nhắn; đánh dấu chưa đọc/đã đọc có chủ đích.
- Lưu tên, SĐT, email, ảnh, link hồ sơ, nội dung chat nguyên văn của khách vào file.
- Suy ra tỷ lệ chốt toàn kênh từ mẫu quá nhỏ (< 20 hội thoại) mà không ghi rõ.
