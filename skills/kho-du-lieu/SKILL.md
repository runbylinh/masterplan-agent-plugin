---
name: kho-du-lieu
description: Quản lý và cập nhật kho dữ liệu nghiên cứu (3 lớp: dữ liệu gốc EVD/MAU, kết quả phân tích FIND/KH/SEG/KEY/INS/OPP..., tài nguyên Marketing OFFER/TD/IDEA/FMT/ADS/CAM/CRO/KEN) bằng scripts/kho.py — đọc danh mục hiện có trước mỗi nhiệm vụ, tìm dữ liệu tái sử dụng được, chuẩn hoá bản ghi mới theo schema, chống trùng theo mã/URL/nội dung, tạo liên kết dữ liệu gốc → phát hiện → Insight → cơ hội → tài nguyên, lưu ngày thu thập và lịch sử, đánh dấu dữ liệu lỗi thời, so sánh thay đổi giữa các lần nghiên cứu, truy vết nguồn gốc một ý tưởng, xuất CSV/XLSX cho Agent khác, Google Sheets hoặc Notion khi được phép, không ghi đè bản đã duyệt. Dùng khi người dùng nói "kho nghiên cứu có gì", "ý tưởng này từ đâu ra", "dữ liệu nào đã cũ", "xuất kho cho team content", "báo cáo thay đổi tháng này", "đồng bộ lên Sheets", "duyệt các insight này".
argument-hint: "[tim | truy-vet ID | kiem-tra | xuat | thay-doi | duyet]"
---

# /masterplan-agent:kho-du-lieu

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md` (cấu trúc, lệnh, quy tắc lưu trữ), schema
`${CLAUDE_PLUGIN_ROOT}/templates/kho/schema.json`. Lệnh: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...` trong thư mục làm việc (kho ở `kho/`).

## A. Mục tiêu
Giữ **một nguồn dữ liệu nghiên cứu duy nhất, có liên kết, có lịch sử, tái sử dụng được** cho toàn bộ hệ thống Fullstack Marketing,
để mỗi lần nghiên cứu sau kế thừa lần trước và mọi tài nguyên giải thích được nguồn gốc.

## B. Điều kiện kích hoạt
- **Dùng khi**: bắt đầu mọi nhiệm vụ nghiên cứu (đọc kho trước); người dùng hỏi kho có gì, nguồn gốc một ý tưởng, dữ liệu cũ; cần xuất cho
  Agent khác hoặc Sheets/Notion; workflow 08 cập nhật thị trường; người dùng duyệt/loại bản ghi.
- **Không dùng khi**: cần phân tích nội dung mới → skill nghiệp vụ tương ứng (skill đó tự ghi kho).
- Chạy độc lập. Các skill khác gọi `kho.py` trực tiếp theo cùng quy tắc.

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Thư mục làm việc có `kho/` (chưa có → `kho.py khoi-tao`) |
| Tuỳ chọn | Mã đợt RP, loại bản ghi, từ khoá, mốc ngày so sánh, đích xuất (thư mục, Sheets, Notion) |
| Khi thiếu | Không có Sheets/Notion → xuất CSV/XLSX và hướng dẫn dán; không tự tạo file Sheets/Notion khi chưa hỏi |

## D. Phương pháp
| Việc | Cách làm |
| --- | --- |
| Đọc danh mục | `kho.py thong-ke`; `kho.py tim --chu "<chủ đề>" --loai ...` |
| Xác định tái sử dụng | Bản ghi còn hạn (`han_dung` theo loại) và cùng phạm vi → dùng lại; lỗi thời → đánh dấu cần cập nhật |
| Chuẩn hoá | Tên trường đúng schema; ngày `YYYY-MM-DD`; tiền là số nguyên (đồng); giá trị trong danh sách cho phép |
| Chống trùng | Script tự so theo khoá (URL, từ khóa + nền tảng, nội dung...) hoặc tiêu đề; trùng thì chỉ bổ sung liên kết |
| Liên kết | `lien_ket` tới cha; trong cùng lô dùng `"tam"` + `"@tam"`; một tài nguyên liên kết nhiều Insight/bằng chứng |
| Lịch sử, không ghi đè | Mọi thay đổi ghi `lich_su`; bản Đã duyệt chỉ sửa với `--sua-ban-da-duyet` khi người dùng đồng ý (quay về Chờ duyệt) |
| Lỗi thời | `kho.py kiem-tra` (cảnh báo "nguy cơ lỗi thời"); `kho.py thay-doi --tu <ngày>` mục "Cần cập nhật" |
| So sánh giữa các lần | `kho.py thay-doi --tu <ngày đợt trước>`: bản ghi mới, bản ghi cập nhật, cần kiểm chứng lại; kết hợp `kho.py tim --loai XH INS OPP` hai đợt |
| Xuất | `kho.py xuat --ra <thư mục> --xlsx [--dot] [--loai]`; Sheets: tải XLSX lên Drive dạng Google Sheets hoặc ghi từng tab từ CSV (hỏi trước); Notion: tạo database theo cột CSV khi người dùng cho phép |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 1 | `kho.py thong-ke` và `kho.py kiem-tra` | Kho | Danh mục, lỗi, cảnh báo | — |
| 2 | Theo yêu cầu: `tim` / `truy-vet` / `thay-doi` / `tien-do` | Kho | Kết quả tra cứu | — |
| 3 | Nếu nạp dữ liệu: chuẩn hoá lô JSON → `kho.py them <lô> --dot RP-xxx` | Lô | Mã mới, bản ghi trùng | Không LỖI |
| 4 | Nếu sửa: `kho.py cap-nhat <ID> <thay-doi>.json`; duyệt/loại chỉ theo lời người dùng: `kho.py duyet <ID...> --trang-thai ...` | Kho | Lịch sử cập nhật | — |
| 5 | Nếu xuất/đồng bộ: `kho.py xuat`/`bao-cao`; hỏi trước khi ghi lên Sheets/Notion | Kho | File xuất | **DỪNG** chờ người dùng xác nhận đích |
| 6 | Báo cáo: số bản ghi theo lớp/loại, lỗi đã sửa, bản ghi lỗi thời, đường dẫn file | — | Tóm tắt | — |

## F. Đầu ra
| Đầu ra | Cách tạo |
| --- | --- |
| Kho dữ liệu nghiên cứu gốc (lớp 1) | `kho/EVD.jsonl`, `kho/MAU.jsonl` |
| Kho kết quả đã phân tích (lớp 2) | `kho/FIND.jsonl`, `KH`, `SEG`, `HT`, `KEY`, `CNT`, `QC`, `LP`, `DV`, `UD`, `TN`, `KT`, `TT`, `XH`, `MV`, `BD`, `RR`, `DN`, `INS`, `OPP`, `GT`, `MT`, `TH` |
| Kho tài nguyên triển khai (lớp 3) | `OFFER`, `TD`, `IDEA`, `FMT`, `ADS`, `CAM`, `CRO`, `KEN` |
| Báo cáo thay đổi | `kho.py thay-doi --tu <ngày>` (lưu vào `nghien-cuu/<thư mục>/thay-doi.md`) |
| Danh sách cần cập nhật/kiểm chứng lại | Mục cuối của `thay-doi`, cảnh báo `kiem-tra` |
| File cho Agent khác | `kho.py xuat` (CSV từng loại, KH tách theo nhãn, `kho-nghien-cuu.xlsx`) |
Mỗi bản ghi: `id`, `loai`, `tieu_de`, `du_lieu`, `lien_ket`, `trang_thai`, `do_tin_cay` + `ly_do_tin_cay`, `kiem_chung` + lý do (với FIND/INS/OPP/KT/XH),
`dot`, `ngay_tao`, `ngay_cap_nhat`, `lich_su`. Ví dụ chuỗi đầy đủ: `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du-secondhand.json`.

## G. Cơ chế bàn giao
Mọi skill đọc/ghi qua kho. Xuất cho content-agent (IDEA, FMT, KEY, TD), design-agent và video-edit (FMT), Agent quảng cáo (ADS, QC, OFFER),
Masterplan (INS, OPP, CAM, TD → `dinh-huong-chien-luoc`, `nghien-cuu-thi-truong`), Sales/CRM (CRO, KH câu hỏi và rào cản).
Lần sau: kế thừa bản ghi còn hạn; bản ghi lỗi thời đưa vào workflow 08.

## H. Kiểm tra chất lượng
- [ ] Đã đọc kho trước khi nạp mới; không tạo bản ghi trùng.
- [ ] `kho.py kiem-tra` không còn LỖI; cảnh báo lỗi thời đã liệt kê cho người dùng.
- [ ] Không ghi đè bản Đã duyệt; không tự đổi sang Đã duyệt.
- [ ] Không có email, số điện thoại, tên khách trong kho (script báo lỗi nếu có).
- [ ] Xuất lên Sheets/Notion chỉ khi người dùng cho phép; kho không đưa lên GitHub.
**Hoàn thành** khi yêu cầu tra cứu/nạp/xuất được thực hiện, kho sạch lỗi và người dùng có đường dẫn kết quả.
