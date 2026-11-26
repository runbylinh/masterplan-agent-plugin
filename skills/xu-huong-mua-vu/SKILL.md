---
name: xu-huong-mua-vu
description: Nghiên cứu thị trường, xu hướng và mùa vụ cho một tháng, quý hoặc dịp — phát hiện xu hướng tiêu dùng, xu hướng sản phẩm/dịch vụ/mô hình/công nghệ, dịp lễ, sự kiện, mùa vụ và biến động nhu cầu hiện tại từ Google Search, Google Trends, báo cáo ngành, thống kê chính thức, TikTok, Facebook, Threads, YouTube, sàn và dữ liệu doanh nghiệp (CRM, doanh thu theo tháng); so sánh cùng kỳ, phân loại dài hạn / ngắn hạn / mùa vụ / tín hiệu mới, nêu nguyên nhân giả định và bằng chứng phản bác, đối chiếu khách, sản phẩm, nguồn lực và đánh giá Nên khai thác / Cần thử nghiệm / Chưa phù hợp. Ghi kho TT (bản đồ thị trường), XH (xu hướng), MV (lịch mùa vụ), BD (biến động nhu cầu), RR (rủi ro), OPP loại Mùa vụ (bản nháp cơ hội theo thời điểm). Khác nghien-cuu-thi-truong (Market Research năm theo bộ mẫu) và du-bao-xu-huong (dự báo năm sau). Dùng khi người dùng gõ /masterplan-agent:xu-huong-mua-vu, nói "xu hướng tháng này", "mùa vụ ngành mình", "dịp Tết nên bán gì", "lịch mùa vụ", "nhu cầu đang tăng hay giảm", "thị trường đang có gì mới", "cơ hội theo mùa".
argument-hint: "[ngành/sản phẩm] [tháng | quý | dịp, ví dụ Tết 2027] [--dot RP-xxx]"
---

# /masterplan-agent:xu-huong-mua-vu

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`.
Cách thu theo nền tảng trong `${CLAUDE_PLUGIN_ROOT}/references/nen-tang/`: `google-search.md`, `google-trends.md`, `tiktok.md`, `facebook.md`,
`threads.md`, `youtube.md`, `san-tmdt.md`, `crm-noi-bo.md`. Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`.

## A. Mục tiêu
Phát hiện **điều gì đang thay đổi** trong thị trường của doanh nghiệp và **khi nào** nhu cầu lên xuống, để chọn đúng thời điểm, sản phẩm, ưu đãi,
chủ đề Content và góc quảng cáo. Phục vụ quyết định: lịch chiến dịch theo tháng/mùa, sản phẩm đẩy theo dịp, thời gian chuẩn bị, xu hướng nên thử.

## B. Điều kiện kích hoạt
- **Dùng khi**: workflow 01, 02, 03, 05, 08; người dùng hỏi xu hướng, mùa vụ, dịp, nhu cầu tăng/giảm cho một tháng, quý hoặc dịp cụ thể.
- **Không dùng khi**: cần Market Research cả năm theo bộ mẫu 5 file → `nghien-cuu-thi-truong`; cần dự báo năm kế hoạch (Tiếp tục / Chững lại / Suy giảm
  / Xuất hiện mới) → `du-bao-xu-huong`; chỉ cần nhu cầu tìm kiếm theo từ khóa → `tu-khoa`. Hai skill kia đọc lại XH, MV, BD của skill này.
- **Chạy độc lập** được. Bước 8 cần DN (`company-analysis`) và tốt hơn khi có KH/SEG (`customer-research`).

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Ngành, sản phẩm, địa bàn, khoảng thời gian (tháng/quý/dịp) và mốc so sánh (mặc định cùng kỳ năm trước); mã RP |
| Tuỳ chọn | Dịp cụ thể; danh sách nguồn chính thống người dùng tin dùng |
| Dữ liệu nội bộ | Doanh thu, đơn theo tháng ≥ 13 tháng (`bao-cao-kinh-doanh`), lead theo tháng (`lead-hoi-thoai`, CRM) |
| Kế thừa | `kho.py tim --loai TT XH MV BD RR KEY DN --chu "<ngành>"`; `thi-truong/*/ket-qua.json` (`nghien-cuu-thi-truong`), `du-bao/*` (`du-bao-xu-huong`) để không thu lại |
| Khi thiếu | Không có số nội bộ theo tháng → chỉ dùng tín hiệu ngoài, ghi TH; quy mô ngành không có nguồn tin cậy → bỏ trống trường quy mô, không ước tính |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Nội dung | Quy mô và cấu trúc ngành (chỉ khi có nguồn tin cậy) · phân khúc · xu hướng tiêu dùng · biến động nhu cầu · xu hướng sản phẩm, dịch vụ, mô hình, công nghệ · dịp lễ, sự kiện, mùa vụ · yếu tố kinh tế, xã hội, chính sách · ngành liên quan và thay thế |
| Nguồn | Chính thống trước (cơ quan thống kê, bộ ngành, hiệp hội, báo cáo ngành có phương pháp) → báo chí uy tín → nền tảng (Trends, sàn) → Social. Chính sách ghi trạng thái đã có hiệu lực / mới dự kiến |
| Xây từ khóa | 5 nhóm: ngành · sản phẩm · nhu cầu · tình huống · mùa vụ (ví dụ "quà tết", "giỏ quà tết công ty", "quà tết healthy"). Dùng lại KEY nếu có |
| Chọn và thu mẫu | Trends: cùng địa bàn, cùng khoảng 5 năm và 12 tháng, so ≤ 5 cụm cùng lúc. Social: mỗi nền tảng 10–20 nội dung ở 3 mức tương tác trong kỳ. Báo cáo: 3–5 nguồn chính thống. Mỗi nguồn một MAU |
| Trích xuất | Mỗi tín hiệu một EVD: nội dung quan sát, ngày đăng, đơn vị đo. Trends ghi là **chỉ số tương đối 0–100**, không phải lượng tìm kiếm. Lượt xem không phải nhu cầu mua |
| So sánh | Giai đoạn tương đương: cùng kỳ năm trước, cùng số ngày trước dịp (dịp âm lịch lệch ngày dương). Thời điểm biến động = tuần/tháng chỉ số bắt đầu tăng, đỉnh, về nền |
| Phân loại XH | **Dài hạn** (tăng đều ≥ 2 năm, nhiều nguồn) · **Ngắn hạn** (tăng nhanh < 6 tháng, chưa lặp) · **Mùa vụ** (lặp cùng thời điểm ≥ 2 năm) · **Tín hiệu mới** (mới xuất hiện, ít nguồn) |
| Nguyên nhân | Mỗi XH/BD ghi nguyên nhân giả định **và** chủ động tìm bằng chứng phản bác (nguồn nói ngược, chỉ số không đổi ở địa bàn khác). Không khẳng định nhân quả |
| Đánh giá | Đối chiếu nhóm khách (KH/SEG), sản phẩm và nguồn lực (DN): **Nên khai thác** (khớp + đủ bằng chứng + làm được) · **Cần thử nghiệm** (khớp nhưng bằng chứng mỏng) · **Chưa phù hợp** (lệch khách/sản phẩm hoặc vượt nguồn lực) |
| Tin cậy | Cao: ≥ 2 nguồn độc lập trong đó có chính thống hoặc nội bộ · Trung bình: nhiều nguồn cùng loại · Thấp: Social lẻ, tín hiệu mới |
| Mâu thuẫn | Trends tăng nhưng doanh thu nội bộ giảm, hoặc hai báo cáo khác số → ghi MT, nêu khác phạm vi/đơn vị đo nếu có |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 1 | Chốt ngành, địa bàn, sản phẩm, khoảng thời gian và mốc so sánh; đọc kho | RP, DN, kho | Phạm vi | **DỪNG** nếu chưa rõ dịp/kỳ |
| 2 | Lập bộ từ khóa 5 nhóm | KEY, DN | Danh sách từ khóa (ghi vào MAU) | ≥ 3 cụm mỗi nhóm hoặc đã ghi lý do |
| 3 | Tìm nguồn chính thống: quy mô, cấu trúc, chính sách, sự kiện | Báo cáo, thống kê | EVD Chính thống; TT | Mỗi số có đơn vị, phạm vi, ngày |
| 4 | Thu tín hiệu nhu cầu từ tìm kiếm, Social, phản hồi khách, số nội bộ | Trends, Search, Social, sàn, CRM | EVD + MAU | Đủ mẫu đã định |
| 5 | So sánh giai đoạn tương đương, cùng kỳ; xác định thời điểm biến động | EVD | BD, MV | Mỗi BD có chỉ số + đơn vị + giai đoạn |
| 6 | Phân loại xu hướng | EVD, BD | XH nháp | Mỗi XH có phân loại |
| 7 | Nguyên nhân giả định và bằng chứng phản bác; rủi ro | XH, BD | XH đủ trường; RR | Đã tìm phản bác có chủ đích |
| 8 | Đối chiếu khách, sản phẩm, nguồn lực | KH, SEG, DN | `Đánh giá` cho XH | — |
| 9 | Đánh giá Nên khai thác / Cần thử nghiệm / Chưa phù hợp; nháp OPP Mùa vụ cho mục Nên khai thác; ghi kho `kho.py them lo-xh.json --dot RP-xxx` → `kiem-tra` | XH, MV, DN | OPP (Mùa vụ) Chờ duyệt; báo cáo `kho.py bao-cao --dot RP-xxx --loai TT XH MV BD RR OPP` | Không LỖI; **DỪNG** chờ duyệt |

## F. Đầu ra
| Mã | Trường bắt buộc (schema) | Ghi chú |
| --- | --- | --- |
| TT – Bản đồ thị trường | Phân khúc, Đặc điểm, Nhu cầu, Mức độ cạnh tranh, Nguồn | Tuỳ chọn `Quy mô (nếu có nguồn tin cậy)`, `Sản phẩm thay thế` |
| XH – Xu hướng | Xu hướng, Mô tả, Thời điểm, Nhóm khách, Phân loại, Đánh giá, Nguồn | Tuỳ chọn Nền tảng, Nguyên nhân giả định, Bằng chứng phản bác; luôn có `do_tin_cay` + lý do; hạn 60 ngày |
| MV – Lịch mùa vụ | Thời điểm, Sự kiện, Nhu cầu, Sản phẩm, Thời gian chuẩn bị, Nguồn | Một bản ghi mỗi dịp; thời gian chuẩn bị tính ngược từ lúc chỉ số bắt đầu tăng |
| BD – Biến động nhu cầu | Chủ đề, Giai đoạn, Chỉ số, Biến động, Nguyên nhân giả định, Nguồn | Chỉ số ghi đơn vị, địa bàn, thời gian đo |
| RR – Rủi ro | Yếu tố thay đổi, Tác động, Dấu hiệu theo dõi, Nguồn | Chính sách, giá nguyên liệu, nguồn cung, thời tiết... |
| OPP – loại `Mùa vụ` | Đủ trường OPP; `Thời điểm` | **Ranh giới**: skill này chỉ tạo bản nháp từ XH/MV + DN; `marketing-opportunities` ghép với INS, KT để hoàn thiện, xếp ưu tiên cuối cùng và có thể sửa bằng `kho.py cap-nhat` |
Kèm EVD, MAU, FIND (nhóm Thị trường), MT, TH. Ví dụ lô đầy đủ (giả định, F&B quà Tết): `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/xu-huong-mua-vu.json`.
```json
{"loai": "XH", "tieu_de": "Giỏ quà Tết ít đường, nguyên liệu tự nhiên", "lien_ket": ["@e2", "@e3"], "do_tin_cay": "Trung bình",
 "ly_do_tin_cay": "Trends và sàn cùng hướng 2 năm; chưa có báo cáo chính thống", "kiem_chung": "Cần bổ sung",
 "du_lieu": {"Xu hướng": "Quà Tết ít đường, healthy", "Mô tả": "Tìm kiếm và sản phẩm giỏ quà healthy tăng hai mùa Tết liên tiếp",
   "Thời điểm": "Tăng từ giữa tháng 12, đỉnh 2–3 tuần trước Tết", "Nhóm khách": "Người đi làm mua biếu gia đình", "Phân loại": "Mùa vụ",
   "Đánh giá": "Nên khai thác", "Nền tảng": "Google Trends, sàn TMĐT", "Nguyên nhân giả định": "Quan tâm sức khoẻ người lớn tuổi",
   "Bằng chứng phản bác": "Giỏ quà truyền thống vẫn chiếm phần lớn sản phẩm bán chạy trên sàn", "Nguồn": "Google Trends; sàn TMĐT"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| Kho TT, XH, MV, BD, RR, OPP (Mùa vụ) + EVD, MAU, FIND, MT, TH | `marketing-opportunities` (hoàn thiện OPP), `y-tuong-chien-dich` (chiến dịch theo tháng/mùa), `san-pham-uu-dai` (sản phẩm, ưu đãi theo dịp), `y-tuong-content` (chủ đề theo thời điểm), `y-tuong-quang-cao` (góc theo mùa), `du-bao-xu-huong` và `nghien-cuu-thi-truong` (tín hiệu đầu vào) | Lịch chiến dịch, sản phẩm theo dịp, chủ đề Content, góc quảng cáo | XH 60 ngày, BD/RR 90 ngày, MV/TT 365 ngày. Workflow 08: `kho.py thay-doi --tu <ngày>`, so cùng phạm vi, cập nhật XH bằng `cap-nhat` |

**Chuyển hoá** (gợi ý trong báo cáo, skill nhóm B làm chi tiết; mỗi gợi ý ghi mã XH/MV/BD làm căn cứ):
| Từ | Thành | Ví dụ (giả định, quà Tết) |
| --- | --- | --- |
| MV + BD | Lịch chiến dịch theo tháng/mùa: mốc chuẩn bị, mở bán, cao điểm, kết thúc | Chốt mẫu 05/12 → mở đặt trước 10/12 → cao điểm 3 tuần trước Tết |
| XH Nên khai thác + DN | Sản phẩm hoặc dòng sản phẩm theo dịp | Giỏ quà ít đường 3 mức giá |
| BD + RR | Ưu đãi theo thời điểm (không tự đề xuất giảm giá khi chưa có biên lợi nhuận) | Ưu đãi đặt sớm có điều kiện, chờ xác nhận giá vốn |
| XH + MV | Chủ đề Content theo thời điểm | "Quà Tết cho bố mẹ đang kiêng đường" |
| XH Cần thử nghiệm | Góc quảng cáo thử nghiệm nhỏ | Quà Tết công ty in logo cho 20–50 hộp |

## H. Kiểm tra chất lượng
- [ ] Quy mô ngành chỉ ghi khi có nguồn tin cậy, kèm đơn vị, phạm vi, năm; không tự ước tính.
- [ ] Google Trends ghi là chỉ số tương đối; không suy lượng tìm kiếm hay doanh số từ view, hashtag.
- [ ] So sánh dùng giai đoạn tương đương; dịp âm lịch so theo số ngày trước dịp.
- [ ] Mỗi XH có phân loại, đánh giá, nguyên nhân giả định và kết quả tìm bằng chứng phản bác; độ tin cậy có lý do.
- [ ] Chính sách ghi trạng thái hiệu lực; không trình bày dự báo như đã xảy ra.
- [ ] OPP Mùa vụ chỉ tạo khi có XH/MV + DN, trạng thái Chờ duyệt.
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi có lịch mùa vụ cho kỳ đã chọn, kho xu hướng có đánh giá, biến động nhu cầu có chỉ số, và người dùng duyệt danh sách Nên khai thác.
