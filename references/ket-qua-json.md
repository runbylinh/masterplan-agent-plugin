# Định dạng `ket-qua.json` (các skill nghiên cứu)

Các skill `ra-soat-thuong-hieu`, `review-nam`, `nghien-cuu-thi-truong`, `du-bao-xu-huong`, `dinh-huong-chien-luoc`
ghi kết quả vào `<thư mục kỳ>/ket-qua.json`, rồi chạy:
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/dung_bao_cao_nghien_cuu.py <thư mục kỳ>
```
Script ra `bao-cao.html`, `sheets/<csv>.csv` (mỗi bảng có `csv` là một tab Sheets), và `bao-cao.md` nếu chưa có
(thêm `--ghi-md` để viết đè). Script in **CẢNH BÁO** khi dòng bảng thiếu nguồn/bằng chứng hoặc mức tin cậy sai.
Sửa `ket-qua.json` đến khi hết cảnh báo, hoặc ghi lý do vào `thieu`.

```json
{
  "loai": "thi-truong",
  "tieu_de": "Market Research 2026 – Brand mẫu",
  "doanh_nghiep": "Brand mẫu",
  "pham_vi": "Đào tạo Marketing online · Việt Nam · năm 2026",
  "ngay": "2026-11-26",
  "tom_tat": "3–5 câu: điều quan trọng nhất người đọc cần biết.",
  "diem_chinh": ["Phát hiện 1", "Phát hiện 2"],
  "cau_chot": "Chỉ dùng khi skill có một câu kết luận (ví dụ câu định hướng chiến lược).",
  "nhan_cau_chot": "Hướng đi chiến lược 2027",
  "phan": [
    {
      "tieu_de": "01. Ngành hàng",
      "ghi_chu": "Phạm vi: 14 nguồn, kiểm tra 20–25/11/2026",
      "doan": ["Đoạn nhận xét ngắn."],
      "bang": {
        "cot": ["Góc độ", "Phát hiện", "Bằng chứng", "Nguồn", "Ngày", "Loại", "Tin cậy"],
        "dong": [["Mùa vụ", "Nhu cầu tăng tháng 8–9", "Trends 'học marketing' cao nhất tháng 9", "https://trends.google.com/...", "2026-11-25", "Dữ kiện", "Trung bình"]]
      },
      "ds": ["Gạch đầu dòng nếu cần"],
      "csv": "nganh-hang",
      "muc_mau": "Ngành hàng",
      "tab_sheets": "MR – Ngành hàng"
    }
  ],
  "uu_tien": ["Điều cần ưu tiên / đưa sang bước sau"],
  "nhan_uu_tien": "Chuyển sang Phần 3",
  "can_kiem_chung": ["Giả định cần kiểm chứng + cách kiểm"],
  "nguon": [{"ten": "Google Trends – học marketing, VN, 12 tháng", "url": "https://trends.google.com/...", "ngay": "2026-11-25"}],
  "thieu": [{"muc": "Quy mô thị trường", "ly_do": "không có nguồn công khai đáng tin"}]
}
```

Quy ước:
- `muc_mau`: vị trí trong bộ mẫu (`<Tab>/<Mục>`), để `xuat_bo_mau.py` điền vào file .xlsx đúng khuôn. Xem `bo-mau.md`.
- `loai`: `thuong-hieu` · `review-nam` · `thi-truong` · `du-bao` · `chien-luoc`.
- Ô bảng có thể là chữ, số, danh sách hoặc URL (tự thành link).
- Cột có chữ "Nguồn", "Bằng chứng" hoặc "Căn cứ" phải có giá trị ở ít nhất một cột mỗi dòng.
- Cột có chữ "Tin cậy": bắt đầu bằng `Cao` / `Trung bình` / `Thấp` (có thể thêm lý do sau, ví dụ "Trung bình – 1 nguồn").
- Giá trị `Cao`, `Đạt`, `Dữ kiện`, `Tiếp tục` hiện màu xanh; `Trung bình`, `Nhận định`, `Tín hiệu`, `Cần bổ sung`,
  `Chững lại` hiện màu nhấn; `Thấp`, `Giả định`, `Suy giảm`, `Chưa đủ căn cứ` hiện màu đỏ.
- Không đưa tên, SĐT, email khách vào bất kỳ ô nào.
