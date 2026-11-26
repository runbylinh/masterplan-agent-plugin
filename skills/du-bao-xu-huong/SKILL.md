---
name: du-bao-xu-huong
description: Dự báo xu hướng tiêu dùng của ngành hàng cho năm kế hoạch — kế thừa Marketing Audit và Market Research, thu thập tín hiệu thay đổi có liên quan trực tiếp (sức mua, giá và nguồn cung, chính sách ngành, thói quen, sản phẩm và hành vi mua, nền tảng và công nghệ, sự kiện), kiểm tra phản ứng người tiêu dùng (Google Trends, Social, đánh giá sàn), dự báo Tiếp tục / Chững lại / Suy giảm / Xuất hiện mới kèm tác động Marketing, mức tin cậy, dấu hiệu cần theo dõi, rồi tự phản biện. Không biến thành Marketing Plan. Dùng khi người dùng gõ /masterplan-agent:du-bao-xu-huong, nói "dự báo xu hướng 2027", "xu hướng tiêu dùng năm sau", "thị trường năm sau thay đổi gì", "tín hiệu thị trường".
argument-hint: "[năm kế hoạch, ví dụ 2027]"
---

# /masterplan-agent:du-bao-xu-huong [năm]

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/du-bao.md`, `${CLAUDE_PLUGIN_ROOT}/references/ket-qua-json.md`, `${CLAUDE_PLUGIN_ROOT}/references/bo-mau.md` (khuôn bảng đầu ra).

## Bước 0 – Kiểm tra đầu vào
1. Năm kế hoạch: từ tham số, mặc định năm sau.
2. Cần Market Research (`thi-truong/*/ket-qua.json`) đã duyệt; Marketing Audit (`review/*/`) nên có.
   Thiếu Market Research: dừng, gợi ý `/masterplan-agent:nghien-cuu-thi-truong` (không dự báo khi chưa có dữ liệu nghiên cứu).
3. Bước 1 của `du-bao.md`: tóm tình hình hiện tại từ tài liệu (không nghiên cứu lại), liệt kê nhóm tín hiệu sẽ tìm
   và vì sao liên quan đến ngành này.
4. Tạo `du-bao/<năm>_YYYY-MM-DD/`.

DỪNG. Trình bản tóm tắt + danh sách nhóm tín hiệu, hỏi có thêm/bỏ nhóm nào không.

## Bước 1 – Thu thập tín hiệu
WebSearch (chế độ extended cho báo cáo, chính sách, tin mới) + mở nguồn gốc bằng Chrome để đọc và kiểm ngày công bố.
Ghi bảng tín hiệu: nhóm · phát hiện · bằng chứng · nguồn · ngày công bố · trạng thái (Đã xảy ra / Đã có hiệu lực / Dự kiến) ·
tác động có thể có · tin cậy. Bỏ tín hiệu không giải thích được tác động đến khách hàng/ngành.

## Bước 2 – Kiểm tra phản ứng người tiêu dùng
Với 3–6 tín hiệu quan trọng nhất, quay lại nguồn phù hợp (Trends, Social, đánh giá sàn, Market Research) theo `du-bao.md` bước 3.
Ghi bảng phản ứng khách hàng. Không khẳng định nhân quả.

## Bước 3 – Dự báo và phản biện
Viết dự báo theo `du-bao.md` bước 4 (kèm dấu hiệu để triển khai và phương án thực hiện khi xuất hiện tín hiệu), rồi tự phản biện từng dự báo theo bước 5 và chấm lại tin cậy.
Dự báo không qua được phản biện: chuyển thành "Chưa đủ căn cứ" + dấu hiệu cần theo dõi.
Nếu người dùng muốn một góc nhìn độc lập: giao phản biện cho một subagent chỉ nhận bảng dự báo và nguồn (không nhận lập luận của mình).

## Bước 4 – Báo cáo
Ghi `ket-qua.json` (loai `du-bao`, 3 bảng đúng khuôn mẫu Dự báo, `diem_chinh` = 3–5 dự báo quan trọng nhất), chạy:
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/dung_bao_cao_nghien_cuu.py du-bao/<năm>_YYYY-MM-DD
```
Hết CẢNH BÁO thì chỉnh `bao-cao.md`, mở `bao-cao.html`.

DỪNG. Báo cáo 5 dòng, hỏi duyệt. Sau duyệt ghi Sheets các tab `DB – ...` (append, `Chờ duyệt`). File .xlsx theo mẫu xuất chung với định hướng chiến lược (skill `dinh-huong-chien-luoc`),
hoặc xuất riêng ngay: `xuat_bo_mau.py du-bao-dinh-huong --nam <năm review> --ket-qua du-bao/<thư mục>/ket-qua.json`.
Hỏi người dùng có muốn hẹn cập nhật tín hiệu định kỳ (ví dụ đầu mỗi quý) không; chỉ tạo lịch khi đồng ý.
Gợi ý bước tiếp: `/masterplan-agent:dinh-huong-chien-luoc`.

## Không được
- Trình bày dự báo như sự thật, gán xác suất, dự báo doanh thu khi không có dữ liệu và phương pháp.
- Tổng hợp chỉ số vĩ mô không liên quan trực tiếp. Chuyển kết quả thành Marketing Plan.
