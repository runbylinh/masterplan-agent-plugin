# Changelog

## 0.3.1 – 2026-11-26
- `HUONG-DAN.md`: cài đặt từng bước (Claude Code, plugin, openpyxl, Chrome, Meta Ads, TikTok for Business, LadiPage, Drive, Sheets),
  tạo thư mục làm việc, thao tác 4 phần, cách duyệt, bộ mẫu, theo dõi định kỳ, việc agent làm/không làm, lỗi thường gặp, mẹo.
- Skill mới `huong-dan`: kiểm tra máy (plugin, Python, cấu hình, connector), chỉ bước còn thiếu, giải thích lệnh.

## 0.3.0 – 2026-11-26
Đưa bộ mẫu Marketing Masterplan (5 file) vào agent làm chuẩn đầu ra.
- `templates/bo-mau/bo-mau.json`: khuôn Đánh giá hiện trạng, Nghiên cứu thị trường, Dự báo và định hướng, Kế hoạch tổng thể
  (tab, mục, tên cột, dòng cố định).
- `templates/company-context-mau.md` thay bằng Mẫu bối cảnh doanh nghiệp (6 mục, "Chưa có dữ liệu" / "Cần kiểm chứng", lưu ý cho AI).
- Script mới `xuat_bo_mau.py`: xuất .xlsx đúng khuôn từ `ket-qua.json` (khoá `muc_mau`) hoặc mẫu trống.
- `references/bo-mau.md`: bảng giai đoạn → file mẫu → skill; sợi chỉ mã ưu tiên UT1–UT5 nối Audit → Research → Định hướng.
- Khớp cột với mẫu: `review-nam` (6 mục), `nghien-cuu-thi-truong` (thêm 3 bảng kết luận: quyết định có thể thay đổi, lựa chọn marketing
  cần xem xét), `du-bao-xu-huong` (dấu hiệu triển khai + phương án ứng phó, bảng kiểm tra tín hiệu), `dinh-huong-chien-luoc`
  (8 dòng, thêm lý do khách chọn và phương án thử nghiệm).
- `setup` hỏi theo 6 mục của mẫu bối cảnh; `dieu-phoi` xuất đủ bộ mẫu khi chạy tổng thể.
- Kiểm tra mức tin cậy chấp nhận "Cao/Trung bình/Thấp + lý do".

## 0.2.0 – 2026-11-26
Bổ sung quy trình nghiên cứu 4 phần (Review → Market Research → Dự báo → Định hướng chiến lược).
- Skill mới `dieu-phoi`: đọc trạng thái thư mục làm việc, chọn và chạy skill đúng thứ tự, kiểm đầu ra trước khi chuyển bước.
- Skill mới `ra-soat-thuong-hieu`: thương hiệu, Website, bình luận và đánh giá công khai.
- Skill mới `review-nam`: tổng hợp một bản Marketing Audit năm.
- Skill mới `nghien-cuu-thi-truong`: ngành hàng, khách hàng, 5–10 đơn vị cùng ngành (trực tiếp / thay thế), tổng hợp.
- Skill mới `du-bao-xu-huong`: 6 nhóm tín hiệu, kiểm phản ứng khách, dự báo, tự phản biện.
- Skill mới `dinh-huong-chien-luoc`: 2–3 khoảng trống, chấm 5 tiêu chí, một câu định hướng, phản biện 4 tiêu chí, tài liệu một trang.
- `references/quy-tac-bang-chung.md` (dữ kiện / nhận định / giả định, mức tin cậy, nhầm lẫn bị cấm), `ket-qua-json.md`,
  và hướng dẫn `thuong-hieu.md`, `review-nam.md`, `thi-truong.md`, `du-bao.md`, `chien-luoc.md`.
- Script `dung_bao_cao_nghien_cuu.py`: dựng HTML, CSV, bản nháp .md từ `ket-qua.json`, cảnh báo dòng thiếu nguồn.
- `setup` tạo `company-context.md` (mẫu `templates/company-context-mau.md`), kiểm thêm TikTok for Business MCP.
- `chi-phi-ads`: TikTok MCP, Google Ads, chi Marketing ngoài quảng cáo, kiểm trùng trước khi cộng, không gọi chi/doanh thu là ROAS.
- `lead-hoi-thoai`: bảng phản hồi khách, lý do mua, ghi phạm vi mẫu.
- Sửa: reach của Facebook Group là "người đã xem" (không phải thành viên hoạt động); cách tính ngược số kỳ trước từ %.

## 0.1.0 – 2026-11-25
- Skill `setup`: tạo thư mục làm việc và `cau-hinh.json`, kiểm tra Chrome và connector.
- Skill 1 `danh-gia-kenh`: đánh giá 7 kênh social theo khung Phễu + vai trò, so kỳ trước, so đối thủ bằng số công khai,
  kết luận Giữ / Đẩy mạnh / Tối ưu / Bỏ. Script `tinh_chi_so.py`, `dung_bao_cao.py`, `doc_file_xuat.py`.
- Skill 2 `lead-hoi-thoai`: hội thoại, phản hồi, chất lượng lead, tỷ lệ chốt theo nhãn / mẫu đọc chat / file đơn. Script `tinh_lead.py`.
- Skill 3 `quet-doi-thu`: nội dung, offer, khuyến mãi, ads đối thủ; lưu lịch sử để báo thay đổi. Script `so_sanh_doi_thu.py`.
- Skill 4 `bao-cao-kinh-doanh`: tìm báo cáo trên Drive/Finder, phân tích theo tháng, sản phẩm, kênh, KPI. Script `tinh_kinh_doanh.py`.
- Skill 5 `chi-phi-ads`: chi phí Meta + TikTok Ads, so ngân sách, CPL, ROAS. Script `tinh_chi_phi.py`.
