---
name: dinh-vi-thong-diep
description: Phát triển định hướng định vị và thông điệp từ kho nghiên cứu — xác định nhóm khách ưu tiên (SEG), lợi ích họ quan tâm nhất (INS, KH), cách đối thủ đang truyền thông lợi ích (DV, TN), điểm khác biệt chứng minh được (DN Kho lợi thế, KT, bằng chứng doanh nghiệp), đề xuất 2–3 phương án định vị (không chốt), viết thông điệp theo nhóm khách và theo hành trình (HT), kiểm tra nhất quán và khả năng chứng minh. Đầu ra kho TD (Phương án định vị, Ma trận thông điệp, Kho thông điệp bán hàng, Kho bằng chứng, Thông điệp theo hành trình), mọi phương án ở trạng thái Chờ duyệt. Dùng khi người dùng gõ /masterplan-agent:dinh-vi-thong-diep, nói "định vị thương hiệu", "thông điệp chính", "khác biệt so với đối thủ", "nói gì với khách", "ma trận thông điệp", "thông điệp bán hàng", "lý do khách chọn mình".
argument-hint: "[nhóm khách hoặc sản phẩm] [--dot RP-xxx]"
---

# /masterplan-agent:dinh-vi-thong-diep

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`,
`${CLAUDE_PLUGIN_ROOT}/references/chien-luoc.md` (nếu đã có Strategic Direction). Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`.
Skill này **không thu thập lại dữ liệu**.

## A. Mục tiêu
Từ Insight, phân khúc và bối cảnh cạnh tranh, tạo **các phương án định vị và hệ thống thông điệp chứng minh được** để Content, quảng cáo,
landing page và Sales nói cùng một điều. Phục vụ quyết định: chọn định vị (người dùng quyết), thông điệp chính cho từng nhóm khách, bằng chứng
cần chuẩn bị, thông điệp ở mỗi giai đoạn hành trình.

## B. Điều kiện kích hoạt
- **Dùng khi**: kho có SEG hoặc INS và có dữ liệu cạnh tranh (DV/TN/KT); workflow 01 sau `marketing-opportunities`; người dùng hỏi định vị,
  thông điệp, khác biệt.
- **Không dùng khi**: chưa có dữ liệu đối thủ → `competitor-research` trước (thiếu TN thì không viết được bối cảnh cạnh tranh);
  cần một hướng đi chiến lược năm → `dinh-huong-chien-luoc` (skill này tạo phương án định vị, không thay quyết định chiến lược).
- **Chạy độc lập** được (tự tạo RP mức Nhanh). Nếu đã có `chien-luoc/*/ket-qua.json` hoặc TD Đã duyệt: phương án mới phải nhất quán hoặc
  ghi rõ điểm khác và lý do.

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Nhóm khách hoặc sản phẩm cần định vị; mã đợt RP; ≥ 1 INS hoặc SEG; dữ liệu thông điệp thị trường (TN hoặc DV) |
| Tuỳ chọn | Định hướng chiến lược đã duyệt; tone thương hiệu; sản phẩm/OFFER trọng tâm |
| Dữ liệu nội bộ | Bằng chứng doanh nghiệp: số khách đã phục vụ, chứng nhận, quy trình, đánh giá thật, case (chỉ dùng khi có nguồn); DN Kho lợi thế |
| Kế thừa từ kho | `kho.py tim --loai SEG INS KH HT --chu "<nhóm khách>"` · `--loai DV TN KT UD` · `--loai DN` (Kho lợi thế, Hồ sơ doanh nghiệp) · `--loai OPP OFFER` · `--loai TD` (thông điệp cũ, tránh trùng và giữ nhất quán) |
| Khi thiếu | Thiếu TN → ghi TH, đề xuất `competitor-research`, phương án định vị ghi "chưa đối chiếu thị trường". Thiếu HT → bỏ bảng Thông điệp theo hành trình, đề xuất `customer-research`. Thiếu bằng chứng doanh nghiệp → `Khả năng chứng minh` = "Chưa có – cần …" |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Nhóm khách ưu tiên | Lấy từ SEG + OPP đã chọn; ưu tiên nhóm có INS độ tin cậy ≥ Trung bình. Mỗi phương án chỉ một nhóm chính |
| Lợi ích quan tâm nhất | Đếm trong KH nhãn Nhu cầu, Tiêu chí lựa chọn, Động lực; xếp 3 lợi ích lặp nhiều nhất và nền tảng xuất hiện. Phân biệt lợi ích chức năng (làm được gì) và cảm xúc (cảm thấy gì) |
| Bản đồ thông điệp thị trường | Từ TN: mỗi đơn vị nói lợi ích nào, cho ai, bằng chứng gì. Lợi ích đã bị nhiều đơn vị nói giống nhau → "đã bão hoà", không làm trục định vị nếu không có bằng chứng mạnh hơn |
| Khác biệt chứng minh được | Giao của ba tập: lợi ích khách quan tâm (KH/INS) ∩ lợi ích thị trường nói yếu hoặc chưa nói (TN, KT) ∩ lợi thế doanh nghiệp có bằng chứng (DN). Khác biệt không có bằng chứng → không đưa vào lời hứa |
| Phương án định vị | 2–3 phương án, mỗi phương án: Nhóm khách · Nhu cầu · Bối cảnh cạnh tranh · Khác biệt · Lời hứa · Lý do tin (bằng chứng) · Rủi ro. Câu định vị: *Với [nhóm khách] đang [nhu cầu/bối cảnh], [thương hiệu] là [hạng mục] mang lại [lợi ích khác biệt], vì [bằng chứng]*. Không chốt, không gọi là định vị chính thức |
| Ma trận thông điệp | Hàng = nhóm khách; cột = Insight · Lợi ích · Thông điệp chính · 2–3 thông điệp hỗ trợ · Bằng chứng. Thông điệp dùng ngôn ngữ khách (KH nhãn Ngôn ngữ khách hàng) |
| Kho thông điệp bán hàng | Câu dùng trực tiếp cho quảng cáo, landing page, Sales: mỗi câu gắn một lợi ích + một bằng chứng + sản phẩm |
| Kho bằng chứng | Mỗi bằng chứng: loại (số liệu, chứng nhận, quy trình, đánh giá, case, demo), đang có hay cần chuẩn bị, nguồn. Không bịa đánh giá, số khách |
| Theo hành trình | Theo HT: mỗi giai đoạn (nhận biết, tìm hiểu, cân nhắc, mua, sau mua) có câu hỏi và rào cản → thông điệp trả lời đúng câu hỏi đó |
| Nhất quán | Kiểm: thông điệp nhóm khách không mâu thuẫn lời hứa định vị; không mâu thuẫn TD Đã duyệt hay Strategic Direction; tone thống nhất |
| Khả năng chứng minh | Mỗi lời hứa ghi *Có (nguồn)* / *Một phần (thiếu …)* / *Chưa có – cần …*. Lời hứa "Chưa có" không đưa vào kho thông điệp bán hàng |
| Mâu thuẫn | Hai nhóm khách cần lợi ích trái nhau (giá rẻ và cao cấp) → tách phương án; ghi MT nếu dữ liệu trái chiều |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 0 | Đọc kho, TD cũ, Strategic Direction nếu có | Kho, `chien-luoc/` | Bản ghi dùng được + ràng buộc nhất quán | Có INS/SEG và TN/DV |
| 1 | Xác định nhóm khách ưu tiên | SEG, OPP, INS | 1–3 nhóm khách | — |
| 2 | Xác định lợi ích họ quan tâm nhất | KH, INS | Top lợi ích mỗi nhóm + tần suất | — |
| 3 | Lập bản đồ cách đối thủ truyền thông lợi ích | TN, DV | Lợi ích đã bão hoà / còn trống | Đã ghi phạm vi mẫu |
| 4 | Tìm khác biệt chứng minh được (giao ba tập) | Bước 2–3, DN, KT | Danh sách khác biệt + bằng chứng | Mỗi khác biệt có ≥ 1 bằng chứng hoặc đã ghi "cần …" |
| 5 | Viết 2–3 phương án định vị | Bước 1–4 | TD Bảng "Phương án định vị" | **DỪNG**: trình phương án, hỏi người dùng giữ phương án nào để viết thông điệp (có thể giữ 2 để so) |
| 6 | Viết thông điệp theo nhóm khách | Phương án được giữ, KH ngôn ngữ | TD "Ma trận thông điệp", "Kho thông điệp bán hàng", "Kho bằng chứng" | — |
| 7 | Viết thông điệp theo hành trình | HT | TD "Thông điệp theo hành trình" | — |
| 8 | Kiểm tra nhất quán và khả năng chứng minh; ghi kho `kho.py them lo-td.json --dot RP-xxx`, `kho.py kiem-tra --dot RP-xxx` | Toàn bộ TD | TD-xxx | Không còn LỖI; không lời hứa "Chưa có" trong kho bán hàng |
| 9 | Trình bảng theo 5 bảng TD + danh sách bằng chứng cần chuẩn bị | TD | — | **DỪNG** chờ duyệt; agent không tự đổi sang Đã duyệt |

## F. Đầu ra — Định vị và thông điệp (`TD`)
Trường bắt buộc: Bảng · Nhóm khách · Nội dung. `Bảng` thuộc 5 giá trị: **Phương án định vị · Ma trận thông điệp · Kho thông điệp bán hàng ·
Kho bằng chứng · Thông điệp theo hành trình**. Trường tuỳ chọn dùng theo bảng: Phương án định vị (Nhu cầu, Bối cảnh cạnh tranh, Khác biệt,
Lời hứa, Bằng chứng, Khả năng chứng minh) · Ma trận (Insight, Lợi ích, Thông điệp, Bằng chứng) · Kho bán hàng (Lợi ích, Sản phẩm, Lý do lựa chọn,
Khả năng chứng minh) · Kho bằng chứng (Bằng chứng, Khả năng chứng minh) · Hành trình (Giai đoạn, Câu hỏi, Rào cản, Thông điệp).
`lien_ket` ≥ 1 INS/OPP/SEG/KT (thêm TN, DN, HT). Mọi phương án Chờ duyệt. Báo cáo: `kho.py bao-cao --dot RP-xxx --loai TD`.
Ví dụ lô kiểm thử (giả định, mỹ phẩm): `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/dinh-vi-thong-diep.json`.

```json
{"loai": "TD", "tieu_de": "Phương án A: chống nắng cho da dầu mụn dùng hằng ngày không bí", "lien_ket": ["INS-001", "SEG-001", "KT-001", "TN-001"],
 "do_tin_cay": "Trung bình", "ly_do_tin_cay": "Lợi ích lặp ở review sàn và hội nhóm; bằng chứng kiểm nghiệm còn thiếu",
 "du_lieu": {"Bảng": "Phương án định vị", "Nhóm khách": "Nữ 18–25, da dầu mụn, đi học/đi làm cả ngày",
   "Nội dung": "Với người da dầu mụn phải dùng kem chống nắng cả ngày, [thương hiệu] là kem chống nắng mỏng nhẹ không gây bí, vì có kết quả thử trên da dầu",
   "Nhu cầu": "Chống nắng hằng ngày mà không bí, không nổi mụn", "Bối cảnh cạnh tranh": "TN-001: đơn vị cùng ngành nói chỉ số SPF, ít nói cảm giác trên da dầu",
   "Khác biệt": "Thử nghiệm trên da dầu, kết cấu gel", "Lời hứa": "Dùng cả ngày không bí da", "Bằng chứng": "Kết quả thử nội bộ 30 người (cần bản xác nhận)",
   "Khả năng chứng minh": "Một phần – cần văn bản kết quả thử"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| Kho `TD` (+ TH bằng chứng cần chuẩn bị) | Chiến lược thương hiệu và `dinh-huong-chien-luoc` (phương án định vị), `y-tuong-content` (thông điệp, Pillar), `y-tuong-quang-cao` (thông điệp, bằng chứng), landing page (`toi-uu-chuyen-doi`, design-agent landing), Sales (kho thông điệp bán hàng, theo hành trình), `y-tuong-chien-dich` | Thông điệp chính, câu bán hàng, bằng chứng, nội dung theo giai đoạn | Hạn dùng 365 ngày; TD Đã duyệt là chuẩn nhất quán cho các skill sau; đổi định vị tạo bản ghi mới, giữ lịch sử |

## H. Kiểm tra chất lượng
- [ ] Có 2–3 phương án định vị, mỗi phương án một nhóm khách chính, không chốt thay người dùng.
- [ ] Mỗi khác biệt và lời hứa có bằng chứng hoặc ghi rõ "Chưa có – cần …"; không bịa đánh giá, số liệu, chứng nhận.
- [ ] Không dùng lợi ích đã bão hoà làm trục định vị khi không có bằng chứng mạnh hơn.
- [ ] Thông điệp dùng ngôn ngữ khách, nhất quán giữa ma trận, kho bán hàng, hành trình và với TD/Strategic Direction đã duyệt.
- [ ] Không nêu tên đối thủ trong thông điệp dùng ra ngoài; so sánh chỉ ở bối cảnh cạnh tranh nội bộ.
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi 5 bảng TD (hoặc phần có dữ liệu) đã trình, người dùng đã chọn phương án định vị để dùng tiếp và có danh sách bằng chứng cần chuẩn bị.
