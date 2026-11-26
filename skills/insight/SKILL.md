---
name: insight
description: Đúc kết Insight khách hàng từ dữ liệu đã thu thập trong kho nghiên cứu (phát biểu khách KH, phát hiện FIND, phân khúc SEG, từ khóa KEY, Content CNT, quảng cáo QC, CRM, review, bình luận) — nhóm phát biểu tương đồng, tìm bối cảnh, mong muốn, động lực, rào cản và mâu thuẫn, đối chiếu nguồn độc lập và bằng chứng trái chiều, viết Insight theo cấu trúc bối cảnh – mong muốn – rào cản – động lực, gắn độ tin cậy và cách kiểm chứng, ghi vào Kho Insight (INS) có liên kết bằng chứng. Không thu thập lại dữ liệu nếu kho đã đủ. Dùng khi người dùng nói "tìm insight", "đúc kết insight", "khách thực sự muốn gì", "vì sao khách mua / chưa mua", "kho insight", hoặc khi workflow cần INS cho cơ hội, thông điệp, Content, quảng cáo, chiến dịch.
argument-hint: "[nhóm khách hoặc chủ đề] [--dot RP-xxx]"
---

# /masterplan-agent:insight

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`.
Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...` (chạy trong thư mục làm việc).

## A. Mục tiêu
Biến dữ liệu khách hàng rời rạc thành **Insight có bằng chứng**: hiểu biết về điều khách thực sự muốn, điều đang ngăn họ và mâu thuẫn giữa hai
điều đó. Phục vụ quyết định: chọn cơ hội, định vị và thông điệp, Content Pillar, góc quảng cáo, ưu đãi, xử lý từ chối.

## B. Điều kiện kích hoạt
- **Dùng khi**: kho đã có ≥ 1 nhóm dữ liệu khách (KH, FIND nhóm Khách hàng, SEG) hoặc dữ liệu CRM/review người dùng đưa; người dùng hỏi
  "insight", "khách muốn gì", "vì sao chưa mua"; workflow 01–04 tới bước Insight.
- **Không dùng khi**: chưa có dữ liệu khách nào → chạy `customer-research` trước (hoặc workflow 03 từ đầu). Chỉ cần liệt kê nhu cầu → dùng
  kho nhu cầu của `customer-research`, không gọi là Insight.
- **Chạy độc lập** được trên kho sẵn có (Case tái sử dụng kho). Cần kết quả từ `customer-research`; tốt hơn nếu có `tu-khoa`,
  `nghien-cuu-content`, `quang-cao-chuyen-doi`, `competitor-research`.

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Nhóm khách hoặc chủ đề cần đúc kết; mã đợt RP (tạo bằng `research` nếu chưa có) |
| Tuỳ chọn | Sản phẩm/dịp trọng tâm; số Insight tối đa cần (mặc định 3–7, không ép số) |
| Dữ liệu nội bộ | Inbox/CRM đã ẩn danh (kết quả `lead-hoi-thoai`), review của doanh nghiệp, khảo sát |
| Kế thừa từ kho | `kho.py tim --loai KH FIND SEG KEY CNT QC --chu "<chủ đề>"`; `kho.py tim --loai INS` để không tạo Insight trùng |
| Khi thiếu | < 2 nguồn độc lập cho một cụm → vẫn viết nhưng `do_tin_cay = Thấp`, ghi TH (dữ liệu cần bổ sung) và GT (cách kiểm chứng). Không có dữ liệu khách nào → dừng, đề xuất `customer-research` |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Nội dung phân tích | Phát biểu và hành vi của khách: nhu cầu, nỗi đau, động lực, rào cản, tiêu chí, tình huống, ngôn ngữ, phản hồi sau mua |
| Nguồn | Chỉ dữ liệu trong kho và file người dùng đưa; không tự thu thập mới (nếu thiếu, ghi TH và đề xuất skill thu thập) |
| Nhóm dữ liệu | **Mã hoá mở**: đọc từng bản ghi KH/FIND, gán 1–3 nhãn ý nghĩa ngắn ("sợ không vừa", "ngại chọn lâu"). **Gom cụm**: các nhãn cùng ý vào một cụm; ghi số bản ghi và số nền tảng của mỗi cụm |
| Tìm bối cảnh | Với mỗi cụm: ai (phân khúc), khi nào/ở đâu (tình huống), đang cố đạt điều gì (mong muốn), điều gì cản (rào cản), vì sao muốn (động lực) |
| Tìm mâu thuẫn | Đặt mong muốn cạnh rào cản: "muốn X nhưng sợ/không thể Y". Không có mâu thuẫn rõ → đó là nhu cầu, chưa phải Insight |
| Đối chiếu | Mỗi Insight cần cụm dữ liệu từ ≥ 2 nguồn độc lập (khác nền tảng/miền). Tìm chủ động **bằng chứng trái chiều** trong kho (KH nhãn ngược, review tích cực khi Insight nói về nỗi lo...) |
| Viết | Cấu trúc: *[Nhóm khách] trong [bối cảnh] muốn [mong muốn] vì [động lực], nhưng [rào cản/mâu thuẫn]*. Dùng ngôn ngữ khách (từ kho Ngôn ngữ khách hàng) |
| Kiểm chứng | Gắn `do_tin_cay` + lý do; `kiem_chung` để mặc định "Cần bổ sung" — chỉ skill `kiem-chung` đổi sang "Có căn cứ". Ghi cách kiểm chứng (khảo sát, phỏng vấn 5–10 khách, A/B thông điệp) |
| Mâu thuẫn dữ liệu | Hai nguồn trái ngược → ghi MT, viết Insight theo phân khúc riêng nếu do khác nhóm khách; không gộp |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 1 | Đọc kho theo chủ đề, liệt kê INS đã có | KH, FIND, SEG, KEY, CNT, QC, INS | Danh sách bản ghi dùng được (mã) + INS cũ | Có ≥ 10 bản ghi khách hoặc người dùng chấp nhận mẫu nhỏ |
| 2 | Mã hoá mở từng bản ghi | Nội dung KH/FIND | Bảng nhãn ý nghĩa (nháp, không ghi kho) | Mọi bản ghi đã có nhãn |
| 3 | Gom cụm, đếm tần suất và số nền tảng | Bảng nhãn | Cụm + số lần + nguồn | Có cụm ≥ 2 nguồn hoặc đã ghi rõ giới hạn |
| 4 | Điền bối cảnh, mong muốn, động lực, rào cản, mâu thuẫn cho mỗi cụm | Cụm | Khung Insight | Mỗi cụm có mâu thuẫn rõ (không có → giữ là nhu cầu) |
| 5 | Tìm bằng chứng trái chiều trong kho | Kho | Bằng chứng trái chiều hoặc "chưa thấy trong mẫu" | Đã tìm có chủ đích |
| 6 | Viết Insight, độ tin cậy + lý do, hướng ứng dụng, nội dung cần kiểm chứng | Khung | Lô INS (+ TH, GT nếu cần) | — |
| 7 | Ghi kho: `kho.py them lo-ins.json --dot RP-xxx` rồi `kho.py kiem-tra --dot RP-xxx` | Lô | INS-xxx có liên kết | Không còn LỖI |
| 8 | Trình bảng Insight cho người dùng | INS | — | **DỪNG** chờ duyệt; gợi ý `kiem-chung` cho INS quan trọng |

## F. Đầu ra — Kho Insight (`INS`)
Trường bắt buộc: Nhóm khách hàng · Bối cảnh · Hành vi quan sát · Nhu cầu · Mong muốn · Động lực · Rào cản · Mâu thuẫn · Insight đúc kết ·
Bằng chứng ủng hộ · Bằng chứng trái chiều · Hướng ứng dụng Marketing · Nội dung cần kiểm chứng. Thuộc tính: `do_tin_cay` + `ly_do_tin_cay`,
`kiem_chung` (mặc định Cần bổ sung), `lien_ket` tới KH/FIND/SEG/... (≥ 1), `trang_thai` Chờ duyệt. Báo cáo: `kho.py bao-cao --dot RP-xxx --loai INS`.

Ví dụ bản ghi (giả định):
```json
{"loai": "INS", "tieu_de": "Muốn phong cách riêng, chi phí hợp lý, ngại chọn lâu và lo chất lượng",
 "lien_ket": ["FIND-001", "KH-001", "KH-002"], "do_tin_cay": "Trung bình",
 "ly_do_tin_cay": "Mẫu lặp ở 3 nền tảng, chưa có khảo sát trực tiếp",
 "du_lieu": {"Nhóm khách hàng": "Sinh viên, người mới đi làm tại Hà Nội", "Bối cảnh": "Đi tiệc cuối năm",
   "Hành vi quan sát": "Hỏi chỗ mua, hỏi size, hỏi đồ có sạch không", "Nhu cầu": "Có bộ đồ hợp dịp",
   "Mong muốn": "Có phong cách riêng với chi phí hợp lý", "Động lực": "Dịp đặc biệt, muốn nổi bật",
   "Rào cản": "Mất thời gian chọn, lo chất lượng và vừa size", "Mâu thuẫn": "Muốn khác biệt nhưng ngại rủi ro của đồ cũ",
   "Insight đúc kết": "Muốn có phong cách riêng với chi phí hợp lý, nhưng không muốn mất nhiều thời gian lựa chọn và lo đồ secondhand thiếu chất lượng",
   "Bằng chứng ủng hộ": "FIND-001 (31/115 bản ghi, 3 nền tảng), KH-001, KH-002", "Bằng chứng trái chiều": "Một số bình luận chỉ quan tâm giá thấp nhất",
   "Hướng ứng dụng Marketing": "Thông điệp, Content phối đồ, bộ phối sẵn", "Nội dung cần kiểm chứng": "Khảo sát 30 khách về mức sẵn lòng trả cho bộ phối sẵn"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| Kho `INS` (lớp 2), TH/GT/MT nếu có | `kiem-chung` (kiểm chứng), `marketing-opportunities`, `dinh-vi-thong-diep`, `y-tuong-content`, `y-tuong-quang-cao`, `y-tuong-chien-dich`, `san-pham-uu-dai`, `toi-uu-chuyen-doi`; chiến lược Masterplan (`dinh-huong-chien-luoc`) | Thông điệp, Content Pillar, góc quảng cáo, ưu đãi, kịch bản tư vấn | Hạn dùng 365 ngày; workflow 08 kiểm tra lại khi có dữ liệu mới; INS bị phản bác giữ lịch sử, không xoá |

## H. Kiểm tra chất lượng
- [ ] Mỗi INS có mâu thuẫn rõ giữa mong muốn và rào cản (không phải nhu cầu chung chung).
- [ ] Mỗi INS liên kết ≥ 1 bản ghi khách; Insight độ tin cậy Cao/Trung bình có ≥ 2 nguồn độc lập.
- [ ] Đã tìm bằng chứng trái chiều và ghi kết quả (kể cả "chưa thấy trong mẫu").
- [ ] Không có câu nói đơn lẻ nào được gọi là Insight; không có Insight trùng INS cũ (đã `kho.py tim`).
- [ ] Ngôn ngữ dùng lời khách, không bịa trích dẫn; không có thông tin cá nhân.
- [ ] `do_tin_cay` có lý do; `kiem_chung` không tự nâng lên "Có căn cứ".
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi các INS ở trạng thái Chờ duyệt, có bảng trình người dùng và danh sách INS cần chạy `kiem-chung`.
