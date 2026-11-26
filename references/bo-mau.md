# Bộ mẫu Marketing Masterplan (template chuẩn đầu ra)

Mọi kết quả nghiên cứu cuối cùng phải điền được vào **bộ mẫu 5 file** của khoá Masterplan. Khuôn chi tiết (tab, mục,
tên cột, dòng cố định) nằm ở `${CLAUDE_PLUGIN_ROOT}/templates/bo-mau/bo-mau.json`. Báo cáo .md/.html có thể thêm cột
(Loại, Tin cậy...), nhưng **tên cột trùng với mẫu phải viết đúng như mẫu** để xuất được.

| Giai đoạn | File mẫu | Tab | Skill điền |
| --- | --- | --- | --- |
| Bối cảnh doanh nghiệp | Mẫu bối cảnh doanh nghiệp (.md) | 6 mục: Tổng quan · Sản phẩm và dịch vụ · Khách hàng hiện tại · Mục tiêu và vấn đề · Kênh và quy trình mua · Nguồn lực và tài liệu | `setup` → `company-context.md` (`templates/company-context-mau.md`) |
| Đánh giá hiện trạng | Mẫu đánh giá hiện trạng marketing {năm} | Đánh giá hiện trạng (6 mục) | `review-nam` (lấy số từ `danh-gia-kenh`, `lead-hoi-thoai`, `ra-soat-thuong-hieu`, `bao-cao-kinh-doanh`, `chi-phi-ads`) |
| Nghiên cứu thị trường | Mẫu nghiên cứu thị trường {năm} | Ngành hàng · Khách hàng · Đơn vị cùng ngành | `nghien-cuu-thi-truong` |
| Dự báo và định hướng | Mẫu dự báo xu hướng và định hướng marketing {năm kế hoạch} | Dự báo xu hướng · Định hướng chiến lược · (phụ) Kiểm tra tín hiệu | `du-bao-xu-huong`, `dinh-huong-chien-luoc` |
| Chiến lược → Nguồn lực → KPI → Triển khai → Theo dõi | Mẫu kế hoạch marketing tổng thể {năm kế hoạch} | Danh mục biểu mẫu · Chiến lược marketing · Nguồn lực và ngân sách · KPI số lượng và chất lượng · Kế hoạch triển khai · Theo dõi kết quả | Chưa có skill (các buổi sau). Chỉ dùng làm khuôn khi người dùng yêu cầu |

## Sợi chỉ "Vấn đề hoặc việc ưu tiên"
Bộ mẫu nối các giai đoạn bằng cột **Vấn đề hoặc việc ưu tiên (liên quan)**:
1. `review-nam` đặt mã cho 3–5 ưu tiên: **UT1 … UT5** (mục "Kết luận đánh giá và các ưu tiên"), mỗi mã một câu ngắn.
2. `nghien-cuu-thi-truong` ghi mã UT liên quan ở các bảng kết luận ("Phát hiện có ảnh hưởng đến quyết định",
   "Kết luận về nhu cầu và quyết định mua", "Kết luận về các lựa chọn trên thị trường"). Phát hiện mới không gắn UT nào: ghi "Mới".
3. `dinh-huong-chien-luoc` ghi các UT và phát hiện làm căn cứ ở dòng "Phát hiện hoặc vấn đề ưu tiên làm căn cứ".
4. Kế hoạch tổng thể (sau này): cột "Vấn đề ưu tiên liên quan" ở Chiến lược và Chiến thuật.
Chưa có Audit: dùng "Vấn đề marketing đang ảnh hưởng đến mục tiêu" trong `company-context.md` và ghi rõ.

## Ghi vào bảng mẫu từ `ket-qua.json`
Mỗi phần cần đưa vào mẫu thêm khoá `"muc_mau": "<Tên tab>/<Tên mục>"` (mục không tên: chỉ `"<Tên tab>"`),
ví dụ `"Đánh giá hiện trạng/Kết quả quảng cáo"`, `"Ngành hàng"`, `"Ngành hàng/Phát hiện có ảnh hưởng đến quyết định"`.
Mục có **dòng cố định** (ví dụ "Nhu cầu, Sản phẩm, Giá, Mùa vụ, Kênh mua, Thay đổi trong ngành"): giá trị cột đầu phải đúng nhãn đó.
Tiền ghi số nguyên (đồng), không ghi "12,5 triệu".

## Xuất file
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/xuat_bo_mau.py --liet-ke
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/xuat_bo_mau.py <mau> --nam <năm review> --doanh-nghiep "<tên>" \
        --ket-qua <thư mục>/ket-qua.json [...] -o <thư mục>/<tên>.xlsx
```
- Không có `--ket-qua`: ra mẫu trống đúng khuôn (dùng khi người dùng muốn tự điền).
- `du-bao-dinh-huong` nhận cả `du-bao/*/ket-qua.json` và `chien-luoc/*/ket-qua.json` trong một lần.
- Sau khi người dùng duyệt: hỏi có muốn đưa file lên Google Drive (thư mục người dùng chỉ định, chuyển thành Google Sheets) không.
  Chỉ tạo file trên Drive khi được phép. Không ghi đè file mẫu gốc của người khác.
