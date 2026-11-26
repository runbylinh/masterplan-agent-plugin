---
name: nghien-cuu-thi-truong
description: Nghiên cứu thị trường năm review (Market Research) — ngành hàng (nhu cầu, sản phẩm, phân khúc giá, mùa vụ, kênh mua, thay đổi trong năm), khách hàng (nhóm khách, hoàn cảnh, vấn đề, động lực, rào cản, tiêu chí chọn) và 5–10 đơn vị cùng ngành (sản phẩm, khách, giá, khác biệt, Marketing, quảng cáo, phản hồi; phân loại cạnh tranh trực tiếp / giải pháp thay thế), rồi tổng hợp có nguồn, ngày và mức tin cậy. Tự tìm và đọc nguồn công khai (Google, Google Trends, Facebook Group, TikTok, YouTube, Google Maps, sàn TMĐT, Meta Ads Library) qua WebSearch và Claude in Chrome. Không dự báo năm sau. Dùng khi người dùng gõ /masterplan-agent:nghien-cuu-thi-truong, nói "market research", "nghiên cứu ngành hàng", "nghiên cứu khách hàng", "tìm và so sánh đơn vị cùng ngành".
argument-hint: "[nganh | khach-hang | don-vi | tong-hop | tat-ca] [năm]"
---

# /masterplan-agent:nghien-cuu-thi-truong [phần] [năm]

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/thi-truong.md`, `${CLAUDE_PLUGIN_ROOT}/references/ket-qua-json.md`.
Đối thủ: `${CLAUDE_PLUGIN_ROOT}/references/quet-doi-thu.md` (cách xem offer, ads).

## Bước 0 – Chốt phạm vi
1. Đọc `company-context.md`, Marketing Audit mới nhất (`review/<năm>/`) nếu có.
2. Đề xuất phạm vi theo `thi-truong.md` mục 0 (ngành, sản phẩm trọng tâm, khu vực, nhóm khách, năm review, 3–5 câu hỏi, nguồn).
   Nhóm khách chưa rõ: đề xuất rồi hỏi xác nhận. Hỏi từng câu ngắn nếu thiếu.
3. Đơn vị cùng ngành: đề xuất 5–10 đơn vị (có lý do chọn, phân loại trực tiếp/thay thế); đơn vị đã có trong `doi_thu` giữ nguyên.
4. Tạo `thi-truong/YYYY-MM-DD/`, ghi `pham-vi.md`.

DỪNG. Trình phạm vi + danh sách đơn vị, chờ duyệt (người dùng có thể bỏ/thêm đơn vị).

## Bước 1 – Thu thập (chạy song song được)
Ba phần độc lập. Khi làm `tat-ca`, có thể giao song song cho subagent (general-purpose), mỗi subagent một phần,
truyền đường dẫn `thi-truong.md`, `quy-tac-bang-chung.md`, `pham-vi.md` và yêu cầu trả bảng đúng cột kèm nguồn.
- **Ngành hàng** (mục 1): WebSearch (extended khi cần báo cáo ngành) + mở nguồn gốc bằng Chrome. Google Trends: khu vực Việt Nam,
  12 tháng (và 5 năm nếu cần mùa vụ), ghi từ khoá và so sánh tương đối.
- **Khách hàng** (mục 2): đọc thảo luận, bình luận, đánh giá thật; ghi cỡ mẫu từng nguồn; dùng kết quả `lead-hoi-thoai`,
  `ra-soat-thuong-hieu` làm nhóm **Khách thực tế**.
- **Đơn vị cùng ngành** (mục 3): đơn vị đã có `doi-thu/lich-su/` gần (≤ 30 ngày) thì dùng lại; còn lại mở Website, kênh Social,
  Meta Ads Library, Google Maps/sàn. Chụp bằng chứng vào `bang-chung/YYYY-MM-DD_<don-vi>_<noi-dung>.png`.
Không truy cập được thì ghi `thieu`; gặp CAPTCHA/đăng nhập thì nhờ người dùng hoặc bỏ qua.

## Bước 2 – Tổng hợp và báo cáo
Đối chiếu ba phần theo mục 4, ghi `ket-qua.json` (loai `thi-truong`, 4 bảng), chạy:
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/dung_bao_cao_nghien_cuu.py thi-truong/YYYY-MM-DD
```
Hết CẢNH BÁO thì chỉnh `bao-cao.md`: 5 phát hiện ngành, nhu cầu chưa được đáp ứng, bảng so sánh đơn vị,
điểm khách chưa hài lòng, câu hỏi và tín hiệu cần theo dõi cho dự báo. Mở `bao-cao.html` cho người dùng xem.

DỪNG. Báo cáo 5 dòng, hỏi duyệt. Sau duyệt ghi Sheets tab `MR – Ngành hàng`, `MR – Khách hàng`,
`MR – Đơn vị cùng ngành`, `MR – Tổng hợp` (append, `Chờ duyệt`). Đơn vị mới được duyệt: hỏi có thêm vào `cau-hinh.json → doi_thu`
để `quet-doi-thu` theo dõi định kỳ không.
Gợi ý bước tiếp: `/masterplan-agent:du-bao-xu-huong`.

## Không được
- Dự báo năm sau ở skill này. Tự tạo số quy mô thị trường, thị phần, doanh thu đối thủ.
- Kết luận từ tiêu đề/đoạn mô tả Google mà không mở nguồn. Chép nguyên văn nội dung đối thủ.
- Bình luận, nhắn tin, theo dõi, bấm quảng cáo, điền form của đơn vị khác.
