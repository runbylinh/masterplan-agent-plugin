---
name: bao-cao-kinh-doanh
description: Tự tìm báo cáo kinh doanh trên Google Drive và trong Finder (máy tính), đọc file Excel/CSV/Google Sheets/PDF/Docs, gom số về một bảng chuẩn rồi phân tích doanh thu và đơn theo tháng (xu hướng, mùa vụ, giá trị đơn TB), theo sản phẩm/khoá học (đóng góp, sản phẩm chủ lực), theo kênh/nguồn khách (khách mới, khách cũ, mua lại) và so mục tiêu/KPI. Xuất báo cáo .md + HTML + Google Sheets. Dùng khi người dùng gõ /masterplan-agent:bao-cao-kinh-doanh, nói "phân tích báo cáo kinh doanh", "doanh thu đang thế nào", "sản phẩm nào bán chạy", "đạt bao nhiêu % KPI", "tìm báo cáo trên drive".
argument-hint: "[kỳ: tháng | quý | năm, ví dụ 2026-Q3 hoặc 12 tháng]"
---

# /masterplan-agent:bao-cao-kinh-doanh [kỳ]

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/kinh-doanh.md`.
Cần `cau-hinh.json` mục `bao_cao_kinh_doanh`.

## Bước 0 – Chốt phạm vi
1. Kỳ phân tích (mặc định 12 tháng gần nhất, để thấy mùa vụ) và kỳ so sánh (cùng kỳ năm trước nếu có số).
2. Nơi tìm: thư mục Drive và thư mục trên máy trong cấu hình. Chưa có thì hỏi; người dùng có thể nói "tự tìm".
3. Tạo `kinh-doanh/YYYY-MM-DD_<ky>/`.

## Bước 1 – Tìm file
- **Google Drive** (connector): `search_files` trong từng thư mục đã khai và theo `tu_khoa`
  (báo cáo, doanh thu, kinh doanh, sales, KPI...), chỉ Sheets/Excel/CSV/PDF/Docs, sửa trong 18 tháng gần nhất.
- **Finder**: tìm trong các thư mục đã khai bằng
  `mdfind -onlyin "<thư mục>" 'kMDItemFSName == "*doanh*thu*"cd || kMDItemFSName == "*bao*cao*"cd'`
  và `find "<thư mục>" -maxdepth 4 \( -iname "*.xlsx" -o -iname "*.csv" -o -iname "*.pdf" \) -mtime -550`.
  Chỉ tìm trong thư mục người dùng đã cho; không quét toàn ổ đĩa.
- Liệt kê file tìm được: tên, nơi, ngày sửa, đoán nội dung. DỪNG, hỏi người dùng chọn file dùng (và file nào là số chính thức
  khi hai file trùng kỳ).

## Bước 2 – Đọc và gom số
- Excel/CSV trên máy: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/doc_file_xuat.py "<file>" --xem` để thấy sheet, cột, vài dòng.
- Google Sheets: `get_values`; file Drive khác: `read_file_content` hoặc tải về `nhap/` rồi đọc.
- PDF/Docs: đọc nội dung, lấy bảng số.
- Gom về `du-lieu.json` theo `references/kinh-doanh.md`. Ghi rõ mỗi dòng lấy từ file nào, sheet nào.
- Số mâu thuẫn giữa hai file: KHÔNG tự chọn, liệt kê và hỏi người dùng.
- Không đưa tên, SĐT khách vào `du-lieu.json`; chỉ số tổng hợp.

## Bước 3 – Tính và báo cáo
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tinh_kinh_doanh.py kinh-doanh/<kỳ>
```
Ra `chi-so-kd.json`, `bao-cao.html`, `sheets/*.csv`. Đọc kết quả, viết `nhan-dinh.json`
(`tom_tat`, `mua_vu`, `san_pham`, `kenh`, `kpi`, `uu_tien`), chạy lại script, rồi viết `bao-cao.md`:
- Doanh thu, đơn, giá trị đơn TB theo tháng; tăng/giảm so tháng trước và cùng kỳ; tháng cao điểm/thấp điểm.
- Sản phẩm: đóng góp %, nhóm tạo 80% doanh thu, sản phẩm tăng/giảm mạnh, biên lợi nhuận nếu có.
- Kênh/nguồn khách: doanh thu theo kênh, khách mới vs cũ, tỷ lệ mua lại.
- So KPI: % đạt từng kỳ, thiếu hụt bao nhiêu, cần bao nhiêu đơn/tháng để bù.
- Hệ quả cho marketing (đầu vào Masterplan): mùa cần đẩy, sản phẩm nên tập trung, kênh nên giữ.

DỪNG. Báo cáo 5 dòng, hỏi duyệt. Sau duyệt ghi Google Sheets tab `Kinh doanh` (append, `Chờ duyệt`).

## Không được
- Sửa, di chuyển, đổi tên, xoá file gốc trên Drive hoặc máy. Chia sẻ file cho ai.
- Bịa số tháng thiếu, nội suy cho đủ 12 tháng. Tháng thiếu để `null` và ghi rõ.
