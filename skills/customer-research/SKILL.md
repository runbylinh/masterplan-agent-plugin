---
name: customer-research
description: Nghiên cứu khách hàng và hành vi mua — thu phát biểu, câu hỏi, phản hồi và hành vi của khách từ CRM, Messenger, bình luận Social, review, Google Maps, sàn, hội nhóm, từ khóa, khảo sát, phỏng vấn; phân biệt khách đã mua, chưa mua, khách cũ, chỉ tương tác; gắn nhãn nhu cầu, nỗi đau, động lực, rào cản, tiêu chí lựa chọn, tình huống mua, câu hỏi, ngôn ngữ khách hàng, trải nghiệm sau mua; đếm tần suất, so sánh giữa nhóm khách và nguồn; phân khúc theo nhu cầu và hành vi (không chỉ tuổi, giới); dựng hành trình mua và chỉ ra chỗ thiếu bằng chứng. Ghi kho KH (các kho theo nhãn), SEG (chân dung), HT (hành trình) kèm EVD, MAU, FIND, rồi chuyển cho insight. Có chế độ 3C (nhánh Customer của research, ra 02-customer.md). Dùng khi người dùng gõ /masterplan-agent:customer-research, nói "nghiên cứu khách hàng", "khách đang phân vân gì", "vì sao khách chưa mua", "khách hỏi gì nhiều nhất", "chân dung khách hàng", "hành trình mua của khách", "khách nói về sản phẩm thế nào".
argument-hint: "[nhóm khách hoặc sản phẩm] [--dot RP-xxx] [--3c]"
---

# /masterplan-agent:customer-research

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`.
Cách thu theo nền tảng (chỉ đọc file cần dùng) trong `${CLAUDE_PLUGIN_ROOT}/references/nen-tang/`: `crm-noi-bo.md`, `facebook.md`, `tiktok.md`,
`youtube.md`, `instagram.md`, `threads.md`, `google-maps.md`, `san-tmdt.md`, `google-search.md`. Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`.

**Chọn chế độ**: được giao `01-brief.md` (giai đoạn 2 của Research 3C, trực tiếp hoặc qua subagent `customer-researcher` chế độ 3C) hoặc có `--3c`
→ **Chế độ 3C** (cuối file). Được giao mã đợt RP, hoặc chạy lẻ → chế độ kho (A–H).

## A. Mục tiêu
Hiểu khách **trong tình huống nào** phát sinh nhu cầu, họ muốn gì, cân nhắc bằng tiêu chí nào, điều gì làm họ trì hoãn, đang dùng giải pháp gì
thay thế, tìm và mua ra sao, sau mua cảm nhận gì và có quay lại không. Phục vụ quyết định: chọn phân khúc ưu tiên, thông điệp theo giai đoạn,
xử lý rào cản trong Content/tư vấn, ưu đãi, điểm chạm cần đầu tư. Kết quả là dữ liệu đã gắn nhãn có bằng chứng — **chưa phải Insight**.

## B. Điều kiện kích hoạt
- **Dùng khi**: workflow 01–07 cần dữ liệu khách; người dùng hỏi về nhu cầu, rào cản, chân dung, hành trình mua.
- **Không dùng khi**: kho đã có ≥ 50 KH còn hạn cho cùng nhóm khách và chỉ cần đúc kết → `insight`; chỉ cần đếm lead, tỷ lệ chốt inbox →
  `lead-hoi-thoai`; cần bức tranh khách cả năm cho Market Research theo bộ mẫu → `nghien-cuu-thi-truong`.
- **Chạy độc lập** được. Tốt hơn khi đã có `company-analysis` (nhóm khách, sản phẩm ưu tiên) và `lead-hoi-thoai` (câu hỏi, lý do không chốt).

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Nhóm khách hoặc sản phẩm; địa bàn; khoảng thời gian; mã RP |
| Tuỳ chọn | Danh sách nguồn người dùng cho phép (hội nhóm, trang quản trị); câu hỏi riêng; file khảo sát/phỏng vấn |
| Dữ liệu nội bộ | CRM, đơn hàng (khách mới/cũ/tái mua), Messenger đã ẩn danh (kết quả `lead-hoi-thoai`), review của doanh nghiệp, khảo sát |
| Kế thừa | `kho.py tim --loai KH SEG HT FIND DN --chu "<nhóm khách>"`; `kho.py tim --loai KEY` (câu hỏi tìm kiếm của `tu-khoa`); `lead-hoi-thoai/*/chi-so-lead.json` |
| Khi thiếu | Không có dữ liệu nội bộ → chỉ dùng nguồn công khai, mọi KH ghi `Loại khách = Quan sát công khai`, ghi TH "chưa có phát biểu khách đã mua". Trang riêng tư/CAPTCHA → nhờ người dùng hoặc bỏ qua, ghi vào MAU |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Nội dung | Bối cảnh sống/làm việc/tiêu dùng · tình huống phát sinh nhu cầu · vấn đề, mong muốn, động lực · tiêu chí lựa chọn · rào cản, nghi ngại, lý do trì hoãn · giải pháp hiện tại/thay thế · khả năng chi trả (chỉ khi có căn cứ: giá đã mua, ngân sách khách tự nói) · hành vi tìm, tham khảo, so sánh, mua · trải nghiệm sau mua · tái mua |
| Nguồn | Nội bộ: CRM, Messenger, đơn, review riêng. Công khai: bình luận TikTok/Facebook/YouTube/Instagram/Threads, review Google Maps và sàn, bài hỏi trong hội nhóm, câu hỏi tìm kiếm. Trực tiếp: khảo sát, phỏng vấn (nếu người dùng có) |
| Xây từ khóa | 4 nhóm: [sản phẩm] + review/có tốt không · [vấn đề/tình huống] + cách/nên · [sản phẩm] + so sánh/thay thế · [sản phẩm] + sau khi dùng/đổi trả. Dùng lại KEY nếu có |
| Chọn và thu mẫu | Phạm vi khởi tạo 50–100 bản ghi có ý nghĩa, ≥ 3 nguồn khác loại. Chống thiên lệch: đủ review tích cực/trung lập/tiêu cực; đủ khách đã mua/chưa mua/chỉ tương tác; cả nội dung nổi bật và thông thường. Mỗi nguồn một MAU; dừng khi bão hoà (10–15 bản ghi liên tiếp không ra nhãn mới) |
| Trích xuất | Mỗi phát biểu một bản ghi: viết lại ngắn giữ nguyên ý và từ khách dùng, kèm bối cảnh (dịp, đi với ai, đã mua chưa). Không ghép hai ý vào một KH. Ẩn danh hoàn toàn |
| Gắn nhãn | `Nhãn` theo schema (Nhu cầu, Nỗi đau, Động lực, Rào cản, Tiêu chí lựa chọn, Tình huống mua, Câu hỏi, Ngôn ngữ khách hàng, Trải nghiệm sau mua); `Giai đoạn mua`, `Giải pháp hiện tại`, `Yếu tố kích thích`, `Điều kiện mua` khi có. Mong muốn ghi dưới nhãn Nhu cầu hoặc Động lực |
| Đếm và so sánh | Gom KH cùng ý, ghi `Tần suất quan sát` = số lần / tổng bản ghi đọc + số nền tảng. So giữa nhóm khách (đã mua vs chưa mua), giữa nguồn (nội bộ vs công khai), giữa giai đoạn. Khác biệt đáng kể → FIND Mẫu lặp |
| Phân khúc | Theo **nhu cầu + bối cảnh + hành vi** (ví dụ "mua làm quà, cần nhanh"), không chia chỉ theo tuổi/giới. Mỗi SEG cần ≥ 1 cụm KH từ ≥ 2 nguồn |
| Hành trình | Mỗi SEG: Nhận biết → Tìm hiểu → So sánh → Mua → Sau mua → Tái mua; mỗi giai đoạn ghi hành vi, điểm chạm, câu hỏi, rào cản. Giai đoạn không có dữ liệu ghi "Thiếu bằng chứng" |
| Kiểm chứng | Một câu nói đơn lẻ không thành phát hiện. FIND Mẫu lặp cần ≥ 2 nguồn độc lập. Không suy khả năng chi trả từ tuổi hay nghề |
| Mâu thuẫn | Nội bộ và công khai trái nhau (ví dụ khách đã mua khen giao nhanh, review sàn chê giao chậm) → ghi MT, kiểm tra có phải khác nhóm khách; không gộp |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 1 | Xác định nhóm khách cần nghiên cứu, đọc kho và DN | RP, DN, KH cũ | Danh sách nhóm khách + câu hỏi | Người dùng xác nhận nhóm khách (**DỪNG** nếu chưa rõ) |
| 2 | Phân biệt đã mua / chưa mua / khách cũ / chỉ tương tác; chọn nguồn cho từng loại | CRM, nguồn công khai | Kế hoạch nguồn + MAU nháp | Mỗi loại khách có ≥ 1 nguồn hoặc đã ghi TH |
| 3 | Thu phát biểu, câu hỏi, phản hồi, hành vi theo nền tảng | Nguồn đã chọn | EVD (mỗi bài/nhóm bình luận/file) + MAU | Đạt phạm vi khởi tạo hoặc bão hoà |
| 4 | Trích từng bản ghi, giữ ý nghĩa và bối cảnh | EVD | KH nháp | Mỗi KH có Nguồn, Loại khách, Bối cảnh |
| 5 | Gắn nhãn | KH nháp | KH có Nhãn, Giai đoạn mua | Mọi KH có nhãn hợp lệ |
| 6 | Nhóm, đếm số lần, loại trùng | KH | Tần suất quan sát; KH trùng gộp liên kết | — |
| 7 | So sánh giữa nhóm khách, nguồn, giai đoạn | KH | FIND Mẫu lặp/Quan sát (+ MT) | Mỗi FIND có ≥ 1 EVD |
| 8 | Phân khúc theo nhu cầu và hành vi | KH, FIND | SEG | Mỗi SEG liên kết KH/FIND |
| 9 | Dựng hành trình mua, đánh dấu chỗ thiếu bằng chứng | SEG, KH | HT + TH | Ghi kho: `kho.py them lo-kh.json --dot RP-xxx`, `kho.py kiem-tra --dot RP-xxx` không LỖI |
| 10 | Trình bảng nhãn × tần suất, SEG, HT; chuyển cho `insight` | KH, SEG, HT | Báo cáo `kho.py bao-cao --dot RP-xxx --loai KH SEG HT` | **DỪNG** chờ duyệt |

## F. Đầu ra
| Mã | Trường bắt buộc (schema) | Ghi chú |
| --- | --- | --- |
| KH | Nhãn, Nội dung, Nhóm khách, Bối cảnh, Loại khách, Nguồn | Tuỳ chọn: Giai đoạn mua, Tần suất quan sát, Giải pháp hiện tại, Yếu tố kích thích, Điều kiện mua, Lý do, Ý nghĩa Marketing. `xuat` tách thành kho theo nhãn: kho-nhu-cau, kho-noi-dau, kho-dong-luc-mua, kho-rao-can, kho-tieu-chi-lua-chon, kho-tinh-huong-mua, kho-cau-hoi, kho-ngon-ngu-khach-hang, kho-trai-nghiem-sau-mua |
| SEG | Phân khúc, Bối cảnh, Nhu cầu, Động lực, Rào cản, Hành vi | Cha KH/FIND. Tuỳ chọn: Khả năng chi trả (có căn cứ), Giải pháp thay thế, Nhu cầu tái mua |
| HT | Phân khúc, Giai đoạn, Hành vi, Điểm chạm, Câu hỏi, Rào cản | Cha KH/FIND/SEG. Mỗi giai đoạn một bản ghi; `Thiếu bằng chứng` khi chưa có dữ liệu |
Kèm EVD, MAU, FIND (nhóm Khách hàng), TH, MT. Ví dụ lô đầy đủ (giả định, mỹ phẩm chăm sóc da): `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/customer-research.json`.
```json
{"loai": "KH", "tieu_de": "Sợ kích ứng khi đổi sang serum mới", "lien_ket": ["@e1", "@e2"],
 "du_lieu": {"Nhãn": "Rào cản", "Nội dung": "Da nhạy cảm, từng bị đỏ khi dùng sản phẩm có cồn nên ngại thử loại mới",
   "Nhóm khách": "Nữ văn phòng da nhạy cảm", "Bối cảnh": "Đang tìm serum thay sản phẩm cũ", "Loại khách": "Chưa mua",
   "Giai đoạn mua": "So sánh", "Tần suất quan sát": "17/86 bản ghi, 3 nền tảng", "Nguồn": "Bình luận TikTok; review sàn; Messenger"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| Kho KH, SEG, HT (+ EVD, MAU, FIND, TH, MT) | `insight` (đúc kết), `kiem-chung`, `marketing-opportunities`, `dinh-vi-thong-diep`, `toi-uu-chuyen-doi` (rào cản, câu hỏi → FAQ, xử lý từ chối), `y-tuong-content` (ngôn ngữ khách), `tu-khoa` (câu hỏi làm từ khóa gốc) | Phân khúc ưu tiên, thông điệp theo giai đoạn, kịch bản tư vấn, ưu đãi | KH hạn 180 ngày, SEG/HT 365 ngày. Lần sau chỉ thu bổ sung nguồn/nhóm khách còn thiếu; KH trùng tự gộp liên kết |

## H. Kiểm tra chất lượng
- [ ] Mỗi KH có Nguồn, Loại khách, Bối cảnh; không có tên, số điện thoại, email, link hồ sơ.
- [ ] Mẫu có cả phản hồi tích cực và tiêu cực, cả khách đã mua và chưa mua (hoặc TH ghi rõ thiếu).
- [ ] Không có câu nói bịa; phát biểu viết lại vẫn giữ nghĩa gốc.
- [ ] Tần suất ghi dạng số lần / tổng; mẫu lặp có ≥ 2 nguồn độc lập.
- [ ] SEG chia theo nhu cầu và hành vi; khả năng chi trả có căn cứ hoặc bỏ trống.
- [ ] HT ghi rõ giai đoạn thiếu bằng chứng; không gọi KH hay FIND là Insight.
- [ ] Mỗi nguồn có MAU (thu thập / đọc được / sử dụng, giới hạn); `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi KH đủ phạm vi khởi tạo hoặc bão hoà, có ≥ 1 SEG và HT cho SEG ưu tiên, người dùng duyệt và đã chuyển cho `insight`.

## Chế độ 3C (nhánh Customer của `/masterplan-agent:research`)
Đầu vào: `01-brief.md` (câu hỏi Customer), sản phẩm, dịp, khu vực; hai mốc (A: cùng kỳ năm trước, B: hiện tại); nguồn người dùng cho phép.
Nguồn: TikTok Search (video + bình luận nghi ngờ/hỏi giá/phản hồi sau dùng), Google Search/Trends (câu hỏi, mùa vụ, so hai mốc), Facebook Group
(bài xin tư vấn, so sánh), review Google Maps/Fanpage (cả khen và chê), Inbox/lịch đặt đã ẩn danh (hỏi → xác nhận → huỷ).
Từ khóa ví dụ case LÁ É QUÁN (đổi theo ngành): `lẩu gà lá é Hà Nội`, `review lẩu gà lá é`, `quán lẩu đi nhóm Hà Nội`, `liên hoan cuối năm Hà Nội`.
Tình huống dò là **giả thuyết**: không tin review/KOL, đi nhóm sợ phát sinh phí, sợ thực tế khác ảnh, không chắc hợp khẩu vị cả nhóm.
Cách làm: đọc nguồn thật → sàng lọc (ghi lý do bỏ) → ghi nhu cầu, tình huống, câu hỏi, rào cản → chia theo Mốc A/B → lưu URL, ngày, ảnh vào
`bang-chung/` → trạng thái Đã xác minh (≥ 3 nguồn độc lập theo `quy-tac-3c.md`) / Chưa xác minh / Mâu thuẫn.
Quy tắc: trích nguyên văn có URL và ngày; một bình luận không thành insight; lượt xem không phải bán hàng; không gán review là "giả";
không coi tháng chưa diễn ra là dữ liệu; thiếu một mốc → "chưa đủ dữ liệu"; nguồn không đọc được → ghi rõ, không suy đoán.
Đầu ra `02-customer.md`:
- **Bảng 1 – Nhu cầu và rào cản**: Nhu cầu/vấn đề | Bằng chứng (trích nguyên văn) | Ngữ cảnh khách | URL và ngày | Mức tin cậy | Cần kiểm chứng thêm
- **Bảng 2 – Đối chiếu hai mốc**: Chủ đề | Bằng chứng Mốc A | Bằng chứng Mốc B | Tiếp diễn hay thay đổi | Hàm ý cần kiểm chứng
- **Phần cuối**: nguồn không truy cập được; giả thuyết insight (ghi rõ là giả thuyết); câu hỏi cần kiểm chứng thêm.
Nếu có `kho/`: ghi thêm mỗi dòng Bảng 1 thành KH (+ EVD theo URL) với `--dot` của đợt 3C.
Kiểm tra: mọi dòng có URL và ngày · không bình luận bịa · dữ kiện tách giả thuyết · ghi nguồn không đọc được · đủ hai mốc hoặc "chưa đủ dữ liệu".
**DỪNG**, hỏi người dùng duyệt.
