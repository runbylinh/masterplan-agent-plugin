---
name: san-pham-uu-dai
description: Phát triển định hướng sản phẩm và ưu đãi từ kho nghiên cứu — đối chiếu nhu cầu và rào cản khách (KH, INS), ma trận sản phẩm và năng lực doanh nghiệp (DN), giá và ưu đãi thị trường (UD, DV), khoảng trống (KT) và cơ hội đã chọn (OPP) để xác định nhu cầu chưa được đáp ứng, sản phẩm hiện tại giải quyết được đến đâu, phương án cải tiến, kết hợp, đóng gói lại, combo, gói dịch vụ, ưu đãi, Lead Magnet, giả thuyết giá; kiểm tra định vị, điều kiện kinh tế (chi phí, biên lợi nhuận, cung ứng) và cách thử nhu cầu, khả năng chi trả. Đầu ra kho OFFER (6 loại). Không tự đề xuất giảm giá hay cam kết lợi nhuận khi chưa có dữ liệu kinh tế. Dùng khi người dùng gõ /masterplan-agent:san-pham-uu-dai, nói "ý tưởng combo", "nên ra sản phẩm gì", "gói dịch vụ mới", "ưu đãi gì cho dịp này", "Lead Magnet", "định giá gói", "cải tiến sản phẩm theo phản hồi khách".
argument-hint: "[sản phẩm, nhóm khách hoặc OPP-xxx] [--dot RP-xxx]"
---

# /masterplan-agent:san-pham-uu-dai

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`.
Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`. Skill này **không thu thập lại dữ liệu**; chỉ đọc kho và file người dùng đưa.

## A. Mục tiêu
Chuyển nhu cầu, rào cản và cơ hội đã có bằng chứng thành **phương án sản phẩm và ưu đãi có điều kiện kinh tế rõ ràng**: làm gì với sản phẩm
hiện có, nên ghép hoặc đóng gói thế nào, ưu đãi nào xử lý đúng rào cản, giả thuyết giá nào cần thử. Phục vụ quyết định: danh mục bán trong
kỳ, combo/gói theo dịp, ưu đãi của chiến dịch, Lead Magnet cho phễu, thử nghiệm giá.

## B. Điều kiện kích hoạt
- **Dùng khi**: kho có INS hoặc KH (nhu cầu, rào cản) và DN Ma trận sản phẩm; người dùng hỏi combo, gói, ưu đãi, sản phẩm mới; workflow 02, 05.
- **Không dùng khi**: chưa biết doanh nghiệp bán gì → `company-analysis`; chưa có dữ liệu khách → `customer-research`; chỉ cần thông điệp
  bán hàng cho sản phẩm có sẵn → `dinh-vi-thong-diep`.
- **Chạy độc lập** được (tự tạo RP mức Nhanh). Tốt nhất sau `marketing-opportunities` với OPP loại Sản phẩm và dịch vụ, Tình huống sử dụng,
  Tái mua, Mùa vụ đã được người dùng chọn.

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Sản phẩm/nhóm khách/OPP cần phát triển; mã đợt RP; DN Ma trận sản phẩm (sản phẩm, giá bán hiện tại) |
| Tuỳ chọn | Dịp bán; ngân sách ưu đãi tối đa; sản phẩm muốn đẩy; giới hạn tồn kho, công suất |
| Dữ liệu nội bộ | Giá vốn, biên lợi nhuận theo sản phẩm, tồn kho, công suất (`company-analysis`, `bao-cao-kinh-doanh`); câu hỏi giá và lý do không chốt (`lead-hoi-thoai`) |
| Kế thừa từ kho | `kho.py tim --loai KH INS SEG --chu "<chủ đề>"` (nhu cầu, rào cản, khả năng chi trả) · `--loai DN` (Ma trận sản phẩm, Kho lợi thế, Giới hạn triển khai) · `--loai UD DV KT` · `--loai OPP` · `--loai OFFER` (tránh trùng) |
| Khi thiếu | Thiếu giá vốn/biên lợi nhuận → vẫn viết OFFER nhưng `Điều kiện kinh tế` = "cần dữ liệu: giá vốn …, biên lợi nhuận …, công suất …" và ghi TH. Thiếu giá thị trường → TH, đề xuất `competitor-research`. Thiếu nhu cầu → dừng, đề xuất `customer-research` |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Kết hợp dữ liệu | Bảng **Nhu cầu × Sản phẩm hiện có**: mỗi nhu cầu/rào cản (KH, INS) đặt cạnh sản phẩm trong DN Ma trận sản phẩm; đánh dấu *Giải quyết tốt* · *Giải quyết một phần* (ghi thiếu gì) · *Chưa giải quyết*. Cột thứ ba: cách thị trường đang bán (UD, DV) |
| Chọn hướng phát triển | Theo thứ tự chi phí thấp → cao: (1) **đóng gói lại / trình bày lại** sản phẩm có sẵn; (2) **kết hợp** thành combo, gói; (3) **cải tiến** (thêm dịch vụ, đổi quy cách); (4) **sản phẩm mới**. Chỉ lên bậc sau khi bậc trước không giải quyết được nhu cầu |
| Ưu đãi | Ưu đãi phải xử lý một rào cản cụ thể (KH nhãn Rào cản, INS Rào cản): rủi ro → bảo hành, đổi trả, dùng thử; khó chọn → gói chọn sẵn; chi phí ban đầu → chia giai đoạn, gói nhỏ; thời gian → giao nhanh. Giảm giá chỉ đề xuất khi có biên lợi nhuận và ghi rõ mức sàn |
| Lead Magnet | Thứ khách nhận miễn phí để giải một câu hỏi thật (KH nhãn Câu hỏi, KEY mục đích Thông tin) và dẫn tới sản phẩm trả phí; ghi chi phí tạo và điều kiện nhận |
| Giả thuyết giá | Chỉ là giả thuyết cần thử: khoảng giá thị trường (UD) + giá hiện tại + tín hiệu khả năng chi trả (SEG "Khả năng chi trả (có căn cứ)", KH câu hỏi giá). Không phát biểu "khách sẵn sàng trả X" khi chưa thử |
| Định vị | Mỗi OFFER kiểm 3 câu: có làm lệch định vị hiện tại (DN, TD) không; có khác biệt so với UD không; có dùng đúng lợi thế DN không. Lệch định vị → ghi Rủi ro |
| Điều kiện kinh tế | Khi có dữ liệu: giá vốn ước tính của phương án, biên lợi nhuận dự kiến, mức ưu đãi tối đa giữ biên ≥ ngưỡng doanh nghiệp đặt, cung ứng/công suất. Không có: ghi "cần dữ liệu …". Không cam kết lợi nhuận |
| Kiểm chứng | Mỗi OFFER có `Phương án kiểm chứng`: đặt trước, landing page thử, khảo sát giá 2–3 mức, bán thử số lượng nhỏ; ghi chỉ số (tỷ lệ chốt, tỷ lệ chọn gói, số đặt trước) và ngưỡng kết luận |
| Xếp hạng | Theo **bằng chứng nhu cầu** (`do_tin_cay` của INS/OPP cha) và **khả thi** (vốn, công suất, thời gian). Ghi thứ tự và lý do trong báo cáo; không dùng điểm số |
| Mâu thuẫn | Khách đòi giá thấp nhưng phàn nàn chất lượng → không tự chọn; tách OFFER theo phân khúc hoặc ghi MT |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 0 | Đọc kho, liệt kê OFFER cũ, kiểm tra có giá vốn/biên lợi nhuận chưa | Kho | Bản ghi dùng được, TH kinh tế | Có nhu cầu (KH/INS) và Ma trận sản phẩm |
| 1 | Xác định nhu cầu chưa được đáp ứng | KH, INS, OPP, KT | Danh sách nhu cầu + mã | Mỗi nhu cầu có bằng chứng |
| 2 | Xác định sản phẩm hiện tại giải quyết được đến đâu | DN Ma trận sản phẩm | Bảng Nhu cầu × Sản phẩm (3 mức) | — |
| 3 | Tìm cách cải tiến, kết hợp, đóng gói lại theo thứ tự chi phí | Bảng bước 2, DN Kho lợi thế | Hướng phát triển cho mỗi nhu cầu | — |
| 4 | Viết phương án sản phẩm, combo, gói, ưu đãi, Lead Magnet, giả thuyết giá | Bước 3, UD | OFFER nháp (chọn Loại) | Mỗi OFFER gắn một nhu cầu/rào cản |
| 5 | Kiểm tra hợp định vị và khác biệt | DN, TD, UD, DV | Rủi ro định vị, Lợi thế cạnh tranh | — |
| 6 | Đánh giá chi phí, biên lợi nhuận, cung ứng nếu có dữ liệu | DN (giá vốn, công suất) | `Điều kiện kinh tế` | Có số hoặc đã ghi "cần dữ liệu …" + TH |
| 7 | Đề xuất thử nghiệm nhu cầu và khả năng chi trả | OFFER | `Phương án kiểm chứng` (+ GT cho giả thuyết giá) | — |
| 8 | Xếp theo bằng chứng và khả thi; ghi kho `kho.py them lo-offer.json --dot RP-xxx`, `kho.py kiem-tra --dot RP-xxx` | Lô | OFFER-xxx | Không còn LỖI |
| 9 | Trình bảng OFFER theo 6 loại, thứ tự ưu tiên, dữ liệu kinh tế còn thiếu | OFFER, TH | — | **DỪNG**: người dùng chọn phương án; xác nhận số kinh tế trước khi đưa vào chiến dịch |

## F. Đầu ra — Kho sản phẩm và ưu đãi đề xuất (`OFFER`)
Trường bắt buộc: Loại · Nhóm khách hàng · Nhu cầu · Sản phẩm liên quan · Đề xuất · Lợi ích · Lợi thế cạnh tranh · Điều kiện kinh tế · Rủi ro ·
Phương án kiểm chứng. `Loại` chia 6 kho: **Sản phẩm mới · Cải tiến sản phẩm · Combo và gói dịch vụ · Ưu đãi và quà tặng · Lead Magnet · Giả thuyết giá**.
`lien_ket` ≥ 1 INS/OPP/KH/KT (thêm DN, UD để truy vết). `trang_thai` Chờ duyệt. Báo cáo: `kho.py bao-cao --dot RP-xxx --loai OFFER`;
xuất theo kho: `kho.py xuat --loai OFFER --ra <thư mục>` rồi lọc cột `Loại`.
Ví dụ lô kiểm thử (giả định, dịch vụ đào tạo): `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/san-pham-uu-dai.json`.

```json
{"loai": "OFFER", "tieu_de": "Gói lớp Excel kèm 4 buổi hỗ trợ bài tập thật của công ty", "lien_ket": ["INS-001", "OPP-001", "DN-001"],
 "do_tin_cay": "Trung bình", "ly_do_tin_cay": "Nhu cầu lặp ở review và hội nhóm; chưa thử bán",
 "du_lieu": {"Loại": "Combo và gói dịch vụ", "Nhóm khách hàng": "Nhân viên văn phòng 1–3 năm kinh nghiệm",
   "Nhu cầu": "Áp dụng được ngay vào file công việc, không chỉ học lý thuyết", "Sản phẩm liên quan": "Khoá Excel cơ bản (DN-001) + giờ hỗ trợ của trợ giảng",
   "Đề xuất": "Khoá Excel + 4 buổi hỗ trợ 1-1 xử lý file thật đã ẩn dữ liệu", "Lợi ích": "Làm được báo cáo của chính mình sau khoá",
   "Lợi thế cạnh tranh": "Trong 6 khoá đã xem, chưa khoá nào hỗ trợ file thật (UD-001)",
   "Điều kiện kinh tế": "Cần dữ liệu: chi phí giờ trợ giảng, số học viên tối đa mỗi trợ giảng, biên lợi nhuận khoá hiện tại",
   "Rủi ro": "Quá tải trợ giảng nếu nhiều học viên chọn gói", "Phương án kiểm chứng": "Mở 20 suất gói thử, đo tỷ lệ chọn gói so với khoá lẻ; ≥ 25% thì giữ"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| Kho `OFFER` (+ TH dữ liệu kinh tế, GT giả thuyết giá) | `y-tuong-chien-dich` (sản phẩm và ưu đãi của chiến dịch), `y-tuong-quang-cao` (Offer trong quảng cáo), `dinh-vi-thong-diep` (lý do lựa chọn), `toi-uu-chuyen-doi` (ưu đãi xử lý từ chối), `y-tuong-content` (Lead Magnet); lập Masterplan (danh mục, ngân sách ưu đãi) | Danh mục bán, combo theo dịp, Lead Magnet, thử nghiệm giá | Hạn dùng 180 ngày; cập nhật khi có giá vốn hoặc kết quả thử (`kho.py cap-nhat`, ghi `Kết quả thử nghiệm` vào GT) |

## H. Kiểm tra chất lượng
- [ ] Mỗi OFFER gắn một nhu cầu hoặc rào cản cụ thể có bằng chứng; ưu đãi nói rõ rào cản nó xử lý.
- [ ] Đã xét đóng gói lại/kết hợp trước khi đề xuất sản phẩm mới.
- [ ] Không có đề xuất giảm giá hay cam kết lợi nhuận khi chưa có giá vốn, biên lợi nhuận; thiếu thì `Điều kiện kinh tế` ghi "cần dữ liệu …" và có TH.
- [ ] Giả thuyết giá ghi là giả thuyết, có cách thử và ngưỡng; không suy diễn khả năng chi trả từ lượt xem.
- [ ] Đã kiểm tra hợp định vị và khác biệt so với UD; Loại đúng 1 trong 6 giá trị.
- [ ] Không trùng OFFER cũ; `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi bảng OFFER đã trình, người dùng chọn phương án và biết rõ số kinh tế nào cần bổ sung trước khi triển khai.
