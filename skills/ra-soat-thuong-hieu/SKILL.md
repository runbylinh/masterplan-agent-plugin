---
name: ra-soat-thuong-hieu
description: Rà soát thương hiệu và Website như khách nhìn thấy (định vị, giá trị khác biệt, thông tin sản phẩm/giá/chính sách, bằng chứng niềm tin, nhất quán Website–Social, dễ liên hệ) và tổng hợp phản hồi công khai của khách (bình luận Facebook/TikTok/YouTube, đánh giá Google Maps, Shopee/TikTok Shop): khen gì, chê gì, hỏi gì lặp lại. Dùng Claude in Chrome, chỉ đọc. Xuất báo cáo .md + HTML + Google Sheets. Thuộc phần Review doanh nghiệp. Dùng khi người dùng gõ /masterplan-agent:ra-soat-thuong-hieu, nói "review website", "rà soát thương hiệu", "khách đánh giá gì về mình", "tổng hợp bình luận, review Google Maps".
argument-hint: "[thuong-hieu | phan-hoi | tat-ca] [kỳ]"
---

# /masterplan-agent:ra-soat-thuong-hieu

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/thuong-hieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/ket-qua-json.md`.
Cần `company-context.md` và `cau-hinh.json` (chạy `setup` nếu chưa có).

## Bước 0 – Chốt phạm vi
1. Phần cần làm: `thuong-hieu` (Website + hình ảnh), `phan-hoi` (bình luận, đánh giá), hoặc `tat-ca` (mặc định).
2. Nguồn: link Website/landing page chính, Google Maps (tên + địa chỉ), các kênh trong `cau-hinh.json`, gian hàng sàn nếu có.
   Thiếu link thì hỏi.
3. Kỳ cho phản hồi (mặc định năm review, hoặc 90 ngày gần nhất nếu ít dữ liệu); cỡ mẫu mặc định
   tối đa 15 bài nhiều bình luận nhất + 50 đánh giá Google Maps mới nhất + 30 đánh giá sàn.
4. Tạo `thuong-hieu/YYYY-MM-DD/`. Kiểm tra Chrome (`tabs_context_mcp`).

DỪNG. Tóm tắt phạm vi, hỏi "Bắt đầu chứ?"

## Bước 1 – Thương hiệu và Website
Mở từng trang bằng Claude in Chrome (chỉ đọc), trả lời 7 câu hỏi trong `thuong-hieu.md` mục A.
Xem cả khung điện thoại (`resize_window` 375 px) cho trang chủ và trang liên hệ/đăng ký.
Chụp màn hình bằng chứng vào `bang-chung/YYYY-MM-DD_thuong-hieu_<noi-dung>.png`.
Câu 7: đối chiếu định vị trong `company-context.md` với điều quan sát được.

## Bước 2 – Phản hồi công khai
Theo `thuong-hieu.md` mục B. Đọc bình luận/đánh giá, nhóm theo chủ đề, đếm số lần gặp trên cỡ mẫu.
Ví dụ viết lại ngắn, ẩn danh. Không trả lời, không bấm thích, không báo cáo bình luận.
Nếu đã có `lead-hoi-thoai`, đối chiếu chủ đề trùng với câu hỏi trong Inbox.

## Bước 3 – Báo cáo
Ghi `ket-qua.json` (loai `thuong-hieu`, các bảng theo `thuong-hieu.md`), rồi:
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/dung_bao_cao_nghien_cuu.py thuong-hieu/YYYY-MM-DD
```
Sửa đến khi hết CẢNH BÁO. Chỉnh `bao-cao.md` cho gọn: điểm mạnh, điểm chưa rõ, vấn đề ảnh hưởng niềm tin,
3 việc cải thiện ưu tiên, cỡ mẫu và phần thiếu.

DỪNG. Báo cáo 5 dòng, hỏi duyệt. Sau duyệt ghi Google Sheets các tab `TH – ...` (append, `Chờ duyệt`), như quy tắc chung.

## Không được
- Sửa Website, bài viết, hồ sơ Google; trả lời hay ẩn bình luận/đánh giá.
- Lưu tên, ảnh, link hồ sơ người bình luận. Suy rộng vài bình luận thành kết luận cho toàn bộ khách.
