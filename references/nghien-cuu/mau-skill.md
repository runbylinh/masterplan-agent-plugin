# Khuôn SKILL.md cho skill nghiên cứu (dùng khi viết hoặc sửa skill)

Mỗi skill nghiên cứu theo đúng 8 phần A–H dưới đây. Kiến thức dài (cách làm theo nền tảng, schema, ví dụ) để ở `references/`
và `templates/`, SKILL.md chỉ trỏ tới. Tên kỹ thuật chữ thường có gạch ngang; nội dung tiếng Việt, formal, thực tế.
Không dùng câu chung chung ("nghiên cứu kỹ", "tìm Insight sâu sắc") mà không nói phương pháp.

```markdown
---
name: <ten-skill>
description: <Một đoạn: làm gì, phục vụ quyết định nào, đầu ra chính (mã kho), khi nào dùng — liệt kê các câu người dùng hay nói>
argument-hint: "<tham số>"
---

# /masterplan-agent:<ten-skill>

Đọc trước: quy-tac.md, quy-tac-bang-chung.md, kho-du-lieu.md, nghien-cuu/quy-tac-nghien-cuu.md, (tài liệu nền tảng liên quan).

## A. Mục tiêu
Giải quyết vấn đề gì; phục vụ quyết định Marketing nào.

## B. Điều kiện kích hoạt
- Dùng khi: …  · Yêu cầu tiêu biểu: "…", "…"
- Không dùng khi: … (dùng skill X thay)
- Chạy độc lập được không; cần kết quả skill nào trước (đọc từ kho).

## C. Đầu vào
| Loại | Nội dung |
| Bắt buộc | … |
| Tuỳ chọn | … |
| Dữ liệu nội bộ dùng được | … |
| Kế thừa từ kho | `kho.py tim --loai … --chu …` |
| Khi thiếu | hỏi gì / dùng nguồn thay thế / ghi TH |

## D. Phương pháp nghiên cứu
Nội dung nghiên cứu · Nguồn · Công cụ · Cách xây từ khóa · Cách chọn và thu mẫu · Cách trích xuất · Cách phân loại/đối chiếu/phân tích ·
Cách kiểm chứng · Cách xử lý mâu thuẫn. (Bảng, ngắn.)

## E. Quy trình thực hiện
| Bước | Hành động cụ thể | Dữ liệu xử lý | Kết quả của bước | Điều kiện sang bước sau |
Có các điểm DỪNG chờ duyệt khi cần.

## F. Đầu ra
Bảng/kho nào (mã loại trong kho), trường bắt buộc (theo schema), định dạng, mã định danh, liên kết dữ liệu gốc, trạng thái kiểm chứng và duyệt,
và **một ví dụ bản ghi hoàn chỉnh** (JSON lô `kho.py them`).

## G. Cơ chế bàn giao
Lưu vào kho nào · chuyển cho skill nào · dùng cho việc Marketing nào · lần sau kế thừa thế nào (hạn dùng, cập nhật).

## H. Kiểm tra chất lượng
Checklist (`- [ ]`) + điều kiện hoàn thành. Luôn có: `kho.py kiem-tra --dot <RP>` không còn LỖI.
```
