---
name: company-analysis
description: Nghiên cứu nội bộ doanh nghiệp trước khi nghiên cứu thị trường — đọc hồ sơ, kiểm kê dữ liệu có/thiếu, chuẩn hoá doanh thu, đơn, AOV, sản phẩm, nhóm khách, kênh theo thời gian, phân tích đóng góp doanh thu và chi phí, so sánh giai đoạn tương đương, tách vấn đề với nguyên nhân giả định, xác định lợi thế, nguồn lực và giới hạn triển khai; dùng lại kết quả review-nam, bao-cao-kinh-doanh, chi-phi-ads, danh-gia-kenh, lead-hoi-thoai thay vì làm lại. Ghi kho DN (Hồ sơ doanh nghiệp, Ma trận sản phẩm, Đánh giá Marketing, Danh sách vấn đề, Kho lợi thế, Giới hạn triển khai) kèm EVD, MAU, FIND. Có chế độ 3C (giai đoạn Company của research, ra 01-brief.md). Dùng khi người dùng gõ /masterplan-agent:company-analysis, nói "phân tích doanh nghiệp", "nghiên cứu nội bộ", "doanh nghiệp đang có vấn đề gì", "sản phẩm nào đóng góp nhiều nhất", "lợi thế của mình là gì", "mình làm được tới đâu với nguồn lực hiện có", "lập brief nghiên cứu", "xác định bài toán".
argument-hint: "[mục tiêu hoặc chủ đề] [--ky 12-thang|quy|thang] [--dot RP-xxx] [--3c]"
---

# /masterplan-agent:company-analysis

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`,
`${CLAUDE_PLUGIN_ROOT}/references/nen-tang/crm-noi-bo.md` (đọc CRM, file bán hàng, Messenger, GA4, Meta Ads, TikTok Analytics).
Chế độ 3C đọc thêm `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-3c.md`. Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`.

**Chọn chế độ**: được gọi từ giai đoạn Company của Research 3C (`/masterplan-agent:research` chế độ 3C), có `--3c`, hoặc người dùng nói "lập brief 3C"
→ **Chế độ 3C** (cuối file). Được giao mã đợt RP, hoặc chạy lẻ → chế độ kho (A–H).

## A. Mục tiêu
Hiểu bối cảnh kinh doanh, vấn đề Marketing thật, lợi thế và giới hạn của doanh nghiệp **trước** khi nghiên cứu thị trường, để nghiên cứu ngoài
bám đúng bài toán (không bắt đầu từ trend). Phục vụ quyết định: chọn câu hỏi nghiên cứu, sản phẩm và nhóm khách ưu tiên, phạm vi đối thủ,
mức ngân sách và nhân sự khả thi cho cơ hội, chiến lược.

## B. Điều kiện kích hoạt
- **Dùng khi**: bắt đầu một đợt nghiên cứu (workflow 01, 04, 05, 06); người dùng hỏi về doanh thu, sản phẩm chủ lực, vấn đề, lợi thế, nguồn lực.
- **Không dùng khi**: chỉ cần số kinh doanh theo tháng → `bao-cao-kinh-doanh`; chỉ cần chi phí ads → `chi-phi-ads`; cần bản Audit năm đủ 5 phần
  → `review-nam`. Skill này **đọc kết quả** của các skill đó, không lấy lại số.
- **Chạy độc lập** được chỉ với `company-context.md`; chất lượng tăng nhiều khi đã có kết quả 5 skill Review trong ≤ 90 ngày.

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | `company-context.md`; mục tiêu hoặc chủ đề nghiên cứu; kỳ phân tích (mặc định 12 tháng gần nhất + cùng kỳ năm trước); mã RP |
| Tuỳ chọn | Sản phẩm/nhóm khách trọng tâm; kế hoạch nội bộ, tài liệu sản phẩm được cấp quyền |
| Dữ liệu nội bộ | CRM, file bán hàng/đơn, Messenger (đã ẩn danh), báo cáo Marketing, Meta Ads (connector), GA4, TikTok Analytics, file trong `nhap/` |
| Kế thừa | `review/<năm>/`, `kinh-doanh/*/chi-so-kd.json`, `chi-phi-ads/*/chi-so-chi-phi.json`, `danh-gia-kenh/*/chi-so.json` + `nhan-dinh.json`, `lead-hoi-thoai/*/chi-so-lead.json`; `kho.py tim --loai DN FIND --chu "<chủ đề>"` |
| Khi thiếu | Số liệu không có → ghi `null` + lý do, tạo TH (câu hỏi, dữ liệu cần có, người cung cấp). Không ước đoán, không lấy số kỳ khác. Thiếu cả hồ sơ → chạy `setup` |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Nội dung | (1) Mô hình, mục tiêu, ưu tiên · (2) Danh mục sản phẩm, giá, biên lợi nhuận, sản phẩm chủ lực · (3) Doanh thu, số đơn, AOV, biến động · (4) Khách hiện tại, chưa mua, tái mua, nguồn khách · (5) Kết quả Marketing theo kênh, nội dung, quảng cáo, chiến dịch · (6) Ngân sách, nhân sự, công cụ, năng lực · (7) Lợi thế sản phẩm, thương hiệu, phân phối, trải nghiệm |
| Nguồn | Ưu tiên kết quả skill Review đã có (đã chuẩn hoá) → file gốc nội bộ → `company-context.md` → lời người dùng (ghi "Người dùng cung cấp") |
| Kiểm kê | Bảng 7 nhóm nội dung × (Có / Một phần / Thiếu) × nguồn × kỳ dữ liệu. Đây là danh sách hỏi người dùng, không đoán phần thiếu |
| Chuẩn hoá | Thời gian theo tháng (dịp âm lịch như Tết so theo số ngày trước dịp, không theo tháng dương); sản phẩm theo một danh mục mã thống nhất; khách theo Mới / Cũ / Tái mua; kênh theo nguồn ghi nhận (utm, nhãn CRM). Ghi quy tắc chuẩn hoá vào MAU |
| Tính toán | AOV = doanh thu / số đơn; đóng góp = doanh thu nhóm / tổng; tỷ lệ tái mua = khách có ≥ 2 đơn / khách có đơn; chi phí/lead, chi phí/đơn lấy từ `chi-phi-ads`. Biên lợi nhuận chỉ khi có giá vốn; ROAS chỉ khi doanh thu được quy cho quảng cáo |
| So sánh | Giai đoạn tương đương: cùng kỳ năm trước, cùng số ngày, cùng dịp. Ghi rõ hai mốc và công thức % thay đổi |
| Vấn đề | Ba tầng tách riêng: **hiện tượng** có số (FIND Dữ kiện) → **nguyên nhân giả định** (FIND Giả thuyết) → **dữ liệu cần để kiểm chứng** (TH). Mức ảnh hưởng theo tỷ trọng doanh thu/khách bị ảnh hưởng |
| Lợi thế | Chỉ ghi lợi thế có căn cứ (số nội bộ, phản hồi khách, tài sản thực có). Lợi thế "tự nhận" chưa có bằng chứng → `do_tin_cay = Thấp` |
| Kiểm chứng | Đối chiếu số giữa hai nguồn nội bộ (CRM với file bán; Meta Ads với báo cáo Marketing). Lệch > 5% → ghi MT, hỏi người dùng nguồn nào đúng |
| Mâu thuẫn | Không tự chọn một bên; ghi MT (Nguồn A, Nguồn B, điểm khác biệt, cách xử lý) |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 1 | Đọc hồ sơ, xác định mục tiêu và quyết định cần hỗ trợ; tạo thư mục `nghien-cuu/<YYYY-MM-DD>-<chủ-đề>/` | `company-context.md`, RP | Mục tiêu, kỳ phân tích | Có mã RP (chưa có → tạo qua `research`) |
| 2 | Kiểm kê dữ liệu có/thiếu; đọc kho và kết quả 5 skill Review | Thư mục kết quả Review, `kho.py tim` | Bảng kiểm kê + danh sách cần hỏi | **DỪNG** nếu thiếu nhóm (2) hoặc (3): hỏi người dùng một lần |
| 3 | Chuẩn hoá theo thời gian, sản phẩm, nhóm khách, kênh | File nội bộ, chỉ số Review | Bảng chuẩn (nháp) + MAU cho mỗi nguồn + EVD | Mọi số có nguồn và kỳ |
| 4 | Phân tích đóng góp doanh thu, chi phí, kết quả theo sản phẩm, khách, kênh | Bảng chuẩn | DN Ma trận sản phẩm, DN Đánh giá Marketing | Đã ghi công thức |
| 5 | So sánh giai đoạn tương đương | Hai mốc | FIND Dữ kiện (biến động) | Cùng phạm vi đo |
| 6 | Xác định vấn đề, điểm nghẽn, nguyên nhân giả định | FIND, Review | DN Danh sách vấn đề, FIND Giả thuyết, TH | Mỗi vấn đề có bằng chứng |
| 7 | Xác định lợi thế, nguồn lực, giới hạn | Hồ sơ, phản hồi khách, nhân sự | DN Kho lợi thế, DN Hồ sơ doanh nghiệp, DN Giới hạn triển khai | — |
| 8 | Ghi kho: `kho.py them lo-dn.json --dot RP-xxx` → `kho.py kiem-tra --dot RP-xxx` | Lô | DN, EVD, MAU, FIND, TH | Không còn LỖI |
| 9 | Tổng hợp hồ sơ đầu vào cho nghiên cứu ngoài: câu hỏi cho khách hàng, cạnh tranh, thị trường; sản phẩm và nhóm khách ưu tiên | DN | Bảng trình người dùng | **DỪNG** chờ duyệt |

## F. Đầu ra — kho `DN` (trường `Bảng`)
Bắt buộc mọi DN: `Bảng`, `Nội dung`, `Nguồn`; nên có `Kỳ dữ liệu`. Trường riêng theo bảng (đều là `tuy_chon` trong schema):
| Bảng | Trường dùng |
| --- | --- |
| Hồ sơ doanh nghiệp | Mô hình, Mục tiêu, Ngành hàng, Địa bàn, Khách hàng, Nguồn lực |
| Ma trận sản phẩm | Sản phẩm, Giá, Lợi ích, Doanh thu, Biên lợi nhuận (null nếu thiếu giá vốn), Khách hàng, Lợi thế |
| Đánh giá Marketing | Kênh, Mục tiêu, Chi phí, Kết quả, Vấn đề |
| Danh sách vấn đề | Vấn đề, Bằng chứng, Mức ảnh hưởng (Cao/Trung bình/Thấp + lý do), Nguyên nhân giả định |
| Kho lợi thế | Lợi thế, Căn cứ, Khách hàng liên quan, Hướng khai thác |
| Giới hạn triển khai | Ngân sách, Nhân sự, Thời gian, Năng lực, Điều kiện |
Kèm: EVD (Loại nguồn `Nội bộ` hoặc `Người dùng cung cấp`, Nguồn = đường dẫn file/kết quả skill), MAU cho mỗi nguồn, FIND nhóm `Doanh nghiệp`,
TH cho dữ liệu thiếu, MT khi số lệch. Báo cáo: `kho.py bao-cao --dot RP-xxx --loai DN FIND TH --ra nghien-cuu/<thư mục đợt>`.
Ví dụ lô đầy đủ (giả định, trung tâm đào tạo): `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/company-analysis.json`. Một bản ghi:
```json
{"loai": "DN", "tieu_de": "Khoá giao tiếp 3 tháng đóng góp 58% doanh thu", "lien_ket": ["@e1"], "do_tin_cay": "Cao",
 "ly_do_tin_cay": "Số từ file bán hàng nội bộ, khớp CRM",
 "du_lieu": {"Bảng": "Ma trận sản phẩm", "Nội dung": "Khoá chủ lực, AOV cao nhất", "Sản phẩm": "Giao tiếp 3 tháng", "Giá": "6,5 triệu",
   "Doanh thu": "1,51 tỷ (58%)", "Biên lợi nhuận": null, "Khách hàng": "Người đi làm 24–32 tuổi", "Lợi thế": "Lớp tối, sĩ số nhỏ",
   "Kỳ dữ liệu": "01/2026–10/2026", "Nguồn": "kinh-doanh/2026-11-20_12-thang/chi-so-kd.json"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| Kho `DN` + EVD/MAU/FIND/TH; báo cáo trong thư mục đợt | `xu-huong-mua-vu` (sản phẩm, địa bàn), `customer-research` (nhóm khách, câu hỏi), `competitor-research` (phạm vi, lợi thế để đối chiếu), `marketing-opportunities` (Lợi thế doanh nghiệp, Điều kiện và nguồn lực), `san-pham-uu-dai`, `dinh-huong-chien-luoc` | Chọn câu hỏi nghiên cứu, sản phẩm ưu tiên, xét tính khả thi của cơ hội và chiến lược | Hạn dùng 120 ngày; cập nhật khi có kỳ dữ liệu mới (workflow 08) bằng `kho.py cap-nhat`, không tạo bản trùng |

## H. Kiểm tra chất lượng
- [ ] Mọi số có nguồn và kỳ dữ liệu; số không có ghi `null` + TH, không ước đoán.
- [ ] Hiện tượng, nguyên nhân giả định và dữ liệu cần kiểm chứng tách riêng; không có kết luận nhân quả chưa chứng minh.
- [ ] So sánh dùng giai đoạn tương đương, ghi hai mốc và công thức.
- [ ] Biên lợi nhuận và ROAS chỉ ghi khi đủ dữ liệu; chi phí/doanh thu không gọi là ROAS.
- [ ] Đã dùng lại kết quả skill Review còn hạn, không lấy lại số.
- [ ] Mỗi lợi thế có căn cứ; không có thông tin cá nhân khách.
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi đủ 6 bảng DN (bảng nào thiếu dữ liệu có TH), danh sách câu hỏi cho nghiên cứu ngoài được người dùng duyệt.

## Chế độ 3C (giai đoạn Company của `/masterplan-agent:research`)
Đầu vào: `company-context.md` (và `ho-so-doanh-nghiep.md`), tài liệu bổ sung, chủ đề hoặc dịp. Làm bước 1–7 ở dạng rút gọn, rồi viết
`research-3c/<YYYY-MM-DD>-<chủ-đề>/01-brief.md` đủ 8 mục:
1. **Tóm tắt tình hình** (5–8 dòng): sản phẩm, khách, Marketing, bán hàng, nguồn lực, số liệu — chỉ số có trong tài liệu.
2. **Bảng so sánh hai mốc** (cùng kỳ năm trước và hiện tại): Chỉ số | Mốc A | Mốc B | Thay đổi (doanh thu, khách/đơn, chi phí vận hành, chi phí quảng cáo).
3. **Bảng vấn đề**: Vấn đề | Dữ liệu đã biết | Giả thuyết cần kiểm chứng | Nguồn cần tìm thêm.
4. **Hành trình khách**: thấy nội dung → hỏi → xác nhận → mua/đến → hoá đơn → quay lại; khúc nào có dữ liệu, khúc nào chưa.
5. **Câu hỏi nghiên cứu cho Customer** (≥ 3). 6. **Câu hỏi nghiên cứu cho Competitor** (≥ 3).
7. **Phạm vi nghiên cứu**: ngành, khu vực (hoặc "chưa rõ, cần hỏi"), mức giá, hai mốc thời gian.
8. **Thông tin còn thiếu cần người dùng bổ sung** (gợi ý: khách theo ngày/ca, khách mới/quay lại, hỏi giá → xác nhận → huỷ, thời gian trả lời).
Quy tắc 3C: không tự đặt số; không kết luận nguyên nhân chắc chắn; tách hiện tượng với nguyên nhân; **không đề xuất giải pháp** ở giai đoạn này.
Nếu thư mục làm việc có `kho/`: ghi thêm các dòng bảng vấn đề thành DN `Danh sách vấn đề` và số liệu thành EVD (Loại nguồn `Nội bộ`).
Kiểm tra: mọi số có trong tài liệu gốc · hiện tượng tách nguyên nhân · ≥ 3 câu hỏi mỗi nhánh · không có kết luận nguyên nhân chắc chắn.
**DỪNG**, hỏi người dùng duyệt Brief.
