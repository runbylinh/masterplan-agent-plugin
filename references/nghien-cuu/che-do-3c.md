# Chế độ 3C theo chủ đề (quy trình 5 giai đoạn, giữ nguyên từ research-agent)

Skill `research` dùng quy trình này khi người dùng chọn **chế độ 3C** (ví dụ `/masterplan-agent:research 3c mùa lễ cuối năm`) hoặc khi đã có thư mục `research-3c/` đang làm dở. Mỗi giai đoạn vẫn ra đúng các file cũ, đồng thời **ghi thêm vào kho** (`kho.py them --dot <RP>`) theo bảng ở cuối file.

Đầu vào: chủ đề người dùng đưa (ví dụ "mùa lễ cuối năm") + `ho-so-doanh-nghiep.md` (ở thư mục làm việc) + `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-3c.md`.
Nếu người dùng không đưa chủ đề, dùng "Bài toán và dịp cần nghiên cứu" trong hồ sơ.

## Bước 0 – Kiểm tra trước khi chạy
0. **Hồ sơ doanh nghiệp.** Tìm theo thứ tự ở thư mục làm việc (thư mục người dùng đang mở):
   - `company-context.md` (bối cảnh doanh nghiệp của agent Masterplan, tạo bởi `/masterplan-agent:setup`): dùng làm hồ sơ.
     Phần hồ sơ 3C cần mà bối cảnh chưa có (mốc thời gian nghiên cứu, bài toán và dịp, danh sách đối thủ, số liệu 2 mốc) thì hỏi bổ sung,
     ghi vào `ho-so-doanh-nghiep.md` (chỉ phần bổ sung, kèm dòng "Bối cảnh chung: xem company-context.md").
     Nếu có `review/`, `thi-truong/`, `cau-hinh.json → doi_thu`: đọc để không hỏi lại điều đã có.
   - `ho-so-doanh-nghiep.md` có rồi: dùng tiếp, sang mục 1.
   - Chưa có: hỏi người dùng chọn MỘT trong hai (không tự chọn):
     (a) **Dùng case mẫu LÁ É QUÁN** để chạy thử: chép `${CLAUDE_PLUGIN_ROOT}/templates/3c/ho-so-case-la-e-quan.md`
         thành `ho-so-doanh-nghiep.md`. Nhắc rõ đây là case giả định, số liệu không phải của nhà hàng thật.
     (b) **Doanh nghiệp của bạn**: chép `${CLAUDE_PLUGIN_ROOT}/templates/3c/ho-so-trong.md` thành
         `ho-so-doanh-nghiep.md`, rồi hỏi người dùng từng nhóm thông tin để điền (sản phẩm, khách, Marketing, bán hàng,
         nguồn lực, số liệu thật, đối thủ). Không tự điền số liệu.
1. Đọc `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md` (quy tắc chung của agent), `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-3c.md`
   (quy tắc riêng Research 3C) và hồ sơ ở mục 0.
2. Liệt kê các mục trong hồ sơ còn trống mà ảnh hưởng đến nghiên cứu (khu vực cụ thể, danh sách đối thủ,
   menu/giá, Content Calendar, kênh đặt bàn). HỎI người dùng bổ sung hoặc xác nhận "chưa có, cứ tiếp tục".
   Không tự điền.
3. Xác nhận 3 điều với người dùng (hỏi một lần, ngắn):
   - Hai mốc so sánh (mặc định lấy ở mục "Mốc thời gian nghiên cứu" trong hồ sơ).
   - Những trang/nguồn người dùng đã mở sẵn và cho phép đọc (TikTok, Facebook, Google Maps, Ads Library, website).
   - Chạy Customer và Competitor song song (subagent) hay tuần tự (tiết kiệm lượt dùng).
4. Tạo thư mục `research-3c/YYYY-MM-DD-[chủ-đề-không-dấu]/` và thư mục `bang-chung/` nếu chưa có.

## Giai đoạn 1 – Company
Chạy skill `masterplan-agent:company-analysis`. Lưu `01-brief.md`.
DỪNG. Hỏi: "Bạn duyệt Brief này để sang bước nghiên cứu khách hàng và đối thủ chứ?"

## Giai đoạn 2 – Customer và Competitor
Sau khi người dùng duyệt Brief:
- Song song: giao subagent `masterplan-agent:customer-researcher` và `masterplan-agent:competitor-researcher`
  cùng lúc (hai lệnh gọi trong cùng một lượt), mỗi bên nhận đường dẫn Brief, hai mốc thời gian,
  danh sách nguồn được phép, đường dẫn thư mục kết quả.
- Tuần tự: chạy skill `masterplan-agent:customer-research` rồi `masterplan-agent:competitor-research`.
Lưu `02-customer.md` và `03-competitor.md`.
DỪNG. Báo cáo gọn: số nguồn đã đọc, số nguồn không truy cập được, vài phát hiện nổi bật, chỗ "Chưa xác minh".
Hỏi người dùng duyệt từng bảng hoặc yêu cầu đọc thêm nguồn.

## Giai đoạn 3 – Tổng hợp 3C
Chạy skill `masterplan-agent:marketing-opportunities` với `01`, `02`, `03`. Lưu `04-tong-hop-3c.md`.
DỪNG. Hỏi người dùng chọn các cơ hội muốn đi tiếp (không tự chọn thay).

## Giai đoạn 4 – Giao việc
Chạy skill `masterplan-agent:marketing-recommendations` cho các cơ hội đã chọn. Lưu `05-giao-viec.md`.
DỪNG. Liệt kê rõ những việc cần người dùng xác nhận trước khi triển khai.

## Giai đoạn 5 – Lưu
Sau khi người dùng duyệt:
1. Nếu có công cụ Google Sheets (connector): ghi các phát hiện vào file Sheets chung của agent (`cau-hinh.json → google_sheets`,
   file `Masterplan [Tên doanh nghiệp]`), đúng tab `3C – Company`, `3C – Customer`, `3C – Competitor`, `3C – Cơ hội và Đề xuất`,
   9 cột như trong `quy-tac-3c.md`, thêm cột đầu "Chủ đề" để phân biệt các lần research,
   `Duyệt = Chờ duyệt`. Hỏi người dùng link bảng nếu chưa biết. Không tạo bảng mới nếu chưa được phép.
2. Nếu chưa nối Sheets: xuất `06-bang-dan-vao-sheets.csv` (9 cột, mỗi dòng một phát hiện, thêm cột đầu "Tab")
   và hướng dẫn người dùng dán vào Sheets.
3. Ảnh chụp bằng chứng: nhắc người dùng đưa vào thư mục Bằng chứng trên Drive, dán link vào cột "Link ảnh chụp".
Chỉ người dùng được đổi "Chờ duyệt" thành "Đã duyệt" hoặc "Loại".

## Báo cáo cuối (5 dòng)
1. Đã làm những giai đoạn nào.
2. Cơ hội nổi bật (tối đa 3).
3. Phần thiếu dữ liệu hoặc không truy cập được.
4. Việc cần người dùng xác nhận.
5. Đường dẫn các file kết quả.

## Không được
- Tự chạy sang giai đoạn sau khi chưa được duyệt.
- Đăng bài, gửi tin, đổi ngân sách, tạo khuyến mãi.
- Bịa dữ liệu khi nguồn không đọc được.

## Ghi vào kho khi chạy chế độ 3C
| Giai đoạn | File cũ | Ghi thêm vào kho |
| --- | --- | --- |
| Bước 0 | — | RP (Research Brief) cho đợt 3C; `Workflow` = "3C" |
| 1 Company | `01-brief.md` | DN (Danh sách vấn đề, Kho lợi thế, Giới hạn triển khai) |
| 2 Customer | `02-customer.md` | EVD + MAU cho nguồn đã đọc; KH (nhu cầu, rào cản, câu hỏi...) |
| 2 Competitor | `03-competitor.md` | EVD + MAU; DV, UD, TN, KT |
| 3 Tổng hợp 3C | `04-tong-hop-3c.md` | INS (nếu đủ căn cứ), OPP |
| 4 Giao việc | `05-giao-viec.md` | Không bắt buộc (việc là kế hoạch, không phải bản ghi nghiên cứu) |
Trạng thái "Đã xác minh" của 3C (≥ 3 nguồn) tương ứng `kiem_chung = Có căn cứ` trong kho; "Chưa xác minh" → `Cần bổ sung`; "Mâu thuẫn" → ghi MT.
