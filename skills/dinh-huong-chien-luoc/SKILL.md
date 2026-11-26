---
name: dinh-huong-chien-luoc
description: Xác định cơ hội và định hướng chiến lược Marketing cho năm kế hoạch — đối chiếu company-context, Marketing Audit, Market Research và Dự báo xu hướng để tìm 2–3 khoảng trống (nhu cầu chưa được đáp ứng tốt mà thương hiệu có thể khai thác), chấm theo 5 tiêu chí Nhu cầu / Tiềm năng / Cạnh tranh / Năng lực / Rủi ro, chọn MỘT cơ hội, viết thành một câu định hướng (khách ưu tiên, nhu cầu, giá trị, khác biệt), phản biện theo 4 tiêu chí rồi ra tài liệu một trang Strategic Marketing Direction. Không đặt KPI, ngân sách, chiến dịch. Dùng khi người dùng gõ /masterplan-agent:dinh-huong-chien-luoc, nói "cơ hội marketing 2027", "nên tập trung vào đâu năm sau", "định hướng chiến lược", "so sánh các cơ hội và chọn hướng đi".
argument-hint: "[năm kế hoạch, ví dụ 2027]"
---

# /masterplan-agent:dinh-huong-chien-luoc [năm]

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/chien-luoc.md`, `${CLAUDE_PLUGIN_ROOT}/references/ket-qua-json.md`.

## Bước 0 – Kiểm tra đầu vào
Cần: `company-context.md`, Marketing Audit (`review/*/`), Market Research (`thi-truong/*/`), Dự báo (`du-bao/*/`), đã duyệt.
Thiếu Dự báo hoặc Market Research: dừng, gợi ý skill tương ứng. Thiếu Audit: cho chạy tiếp nếu người dùng đồng ý, ghi rõ giới hạn.
Tạo `chien-luoc/<năm>_YYYY-MM-DD/`.

## Bước 1 – Tìm 2–3 khoảng trống
Theo `chien-luoc.md` bước 1. Mỗi khoảng trống phải trích bằng chứng từ ít nhất hai nguồn trong bốn tài liệu đầu vào
(ví dụ Inbox + đánh giá đối thủ). Không có bằng chứng thì không đưa vào, hoặc ghi rõ là giả định.

DỪNG. Trình 2–3 khoảng trống (bảng ngắn), hỏi người dùng có muốn thêm/bỏ cơ hội nào trước khi chấm.

## Bước 2 – Chấm và chọn
Chấm 5 tiêu chí theo `chien-luoc.md` bước 2, bảng so sánh, đề xuất MỘT cơ hội + lý do chọn/không chọn.
Tiêu chí thiếu dữ liệu: ghi "chưa đủ căn cứ" thay vì đoán.

## Bước 3 – Hướng đi và phản biện
- Viết câu định hướng và giải thích ngắn theo bước 3.
- Phản biện theo bước 4. Nên giao cho một subagent độc lập: chỉ đưa câu định hướng, bảng khoảng trống, bảng chấm và
  đường dẫn bốn tài liệu đầu vào, yêu cầu tìm điểm yếu (không đưa lập luận bảo vệ của mình).
- Có tiêu chí "Cần bổ sung": sửa hướng đi hoặc ghi điểm cần xác minh. Giữ nguyên tắc chỉ chốt MỘT hướng.

## Bước 4 – Tài liệu một trang
Ghi `ket-qua.json` (loai `chien-luoc`, `tieu_de` "Strategic Marketing Direction <năm> – <doanh nghiệp>",
`cau_chot` = câu định hướng, `nhan_cau_chot` = "Hướng đi chiến lược <năm>", 4 bảng theo `chien-luoc.md`,
`can_kiem_chung` = giả định còn mở), chạy:
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/dung_bao_cao_nghien_cuu.py chien-luoc/<năm>_YYYY-MM-DD
```
Hết CẢNH BÁO thì chỉnh `bao-cao.md` gọn trong một trang, mở `bao-cao.html`.

DỪNG. Trình câu định hướng + bảng so sánh + điểm cần kiểm chứng. Người dùng quyết định hướng đi; agent chỉ đề xuất.
Sau duyệt ghi Sheets tab `CL – ...` (append, `Chờ duyệt`). Nếu người dùng muốn bản Google Docs/Notion: hỏi nơi lưu, chỉ tạo khi được phép.
Bước tiếp (chưa có skill): lập Marketing Masterplan (mục tiêu, KPI, ngân sách, chiến dịch) từ tài liệu này.

## Không được
- Chọn ngay một hướng khi chưa so sánh 2–3 cơ hội. Đưa nhiều hướng chính cùng lúc.
- Biến hướng đi thành danh sách hoạt động, chiến dịch, kênh, KPI, ngân sách, phân công.
- Biến giả định thành dữ kiện, gán điểm số chính xác khi thiếu dữ liệu.
