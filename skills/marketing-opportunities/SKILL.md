---
name: marketing-opportunities
description: Tìm kiếm và đánh giá cơ hội Marketing từ kho nghiên cứu — kết hợp dữ liệu doanh nghiệp (DN), thị trường và thời điểm (TT, XH, MV, BD), khách hàng (KH, SEG, HT, INS), cạnh tranh (DV, UD, TN, KT), từ khóa (KEY), Content (CNT, QC) và kênh (KEN) để tìm nhu cầu mới hoặc chưa được đáp ứng tốt, xác định khoảng trống trong phạm vi nghiên cứu, đối chiếu lợi thế và nguồn lực, viết giả thuyết cơ hội, đánh giá chất lượng bằng chứng, tiềm năng, khả thi, thời điểm (Cao/Trung bình/Thấp có lý do), xếp ưu tiên và đề xuất phương án thử nghiệm. Đầu ra là bản đồ cơ hội trong kho (OPP). Giữ chế độ 3C (ra 04-tong-hop-3c.md) khi gọi từ /masterplan-agent:research 3c. Dùng khi người dùng gõ /masterplan-agent:marketing-opportunities, nói "tìm cơ hội Marketing", "cơ hội dịp Tết", "nên khai thác nhu cầu nào", "khoảng trống thị trường", "bản đồ cơ hội", "tổng hợp 3C", "ghép khách, đối thủ, doanh nghiệp".
argument-hint: "[chủ đề hoặc dịp] [--dot RP-xxx] [3c]"
---

# /masterplan-agent:marketing-opportunities

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`,
`${CLAUDE_PLUGIN_ROOT}/references/chien-luoc.md` (để giữ nhất quán tiêu chí). Chế độ 3C đọc thêm `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-3c.md`.
Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...` (chạy trong thư mục làm việc). Skill này **không thu thập lại dữ liệu**.

## A. Mục tiêu
Biến dữ liệu đã có trong kho thành **bản đồ cơ hội Marketing có căn cứ**: nhu cầu nào đang mở, thị trường phục vụ đến đâu, doanh nghiệp
có lợi thế gì để khai thác, nên ưu tiên cơ hội nào và thử nghiệm ra sao. Phục vụ quyết định: chọn trọng tâm chiến dịch, sản phẩm/ưu đãi,
thông điệp, Content, kênh, chuyển đổi trong kỳ tới.

**Ranh giới với `dinh-huong-chien-luoc`**: skill đó chọn MỘT hướng đi chiến lược cho năm kế hoạch (5 tiêu chí Nhu cầu / Tiềm năng / Cạnh tranh /
Năng lực / Rủi ro, một trang Strategic Direction). Skill này ở **cấp chiến thuật**: nhiều cơ hội song song, mỗi cơ hội có loại, thời điểm và
thử nghiệm riêng. Hai skill dùng cùng logic: tiêu chí ở đây ánh xạ Nhu cầu → *chất lượng bằng chứng*, Cạnh tranh → *khoảng trống* (bước 4),
Năng lực → *khả thi*, Tiềm năng giữ nguyên, Rủi ro ghi trường `Rủi ro`. OPP loại "Phân khúc khách hàng" hoặc "Định vị" mức Cao được chuyển cho
`dinh-huong-chien-luoc` làm khoảng trống ứng viên; skill này không viết câu định hướng chiến lược năm.

## B. Điều kiện kích hoạt
- **Dùng khi**: kho đã có dữ liệu ít nhất hai trong ba nhóm khách hàng / cạnh tranh / doanh nghiệp; workflow 01, 02, 05 tới bước cơ hội;
  người dùng hỏi "cơ hội dịp X", "nên khai thác nhu cầu nào", "khoảng trống thị trường".
- **Không dùng khi**: chưa có dữ liệu khách → `customer-research`; chỉ cần một ý tưởng Content/quảng cáo cụ thể khi kho đã có OPP → gọi thẳng
  skill chuyển hoá; cần một hướng đi chiến lược năm → `dinh-huong-chien-luoc`.
- **Chạy độc lập** được trên kho sẵn có (tự tạo RP mức Nhanh nếu chưa có đợt). Tốt nhất sau `insight` và `kiem-chung`.
- **Chế độ 3C**: khi gọi từ `research` chế độ 3C (giai đoạn 3) hoặc người dùng thêm `3c` → xem mục cuối.

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Chủ đề/dịp/sản phẩm cần tìm cơ hội; mã đợt RP; hồ sơ doanh nghiệp (`company-context.md` hoặc DN trong kho) |
| Tuỳ chọn | Mục tiêu kinh doanh kỳ tới; loại cơ hội quan tâm (trong 10 loại); giới hạn nguồn lực; mốc thời gian triển khai |
| Dữ liệu nội bộ | Doanh thu theo sản phẩm (`bao-cao-kinh-doanh`), lead và lý do không chốt (`lead-hoi-thoai`), chi phí và kết quả Ads (`chi-phi-ads`) |
| Kế thừa từ kho | `kho.py tim --loai DN TT XH MV BD RR --chu "<chủ đề>"` · `--loai KH SEG HT INS FIND` · `--loai DV UD TN KT` · `--loai KEY CNT QC KEN` · `--loai OPP` (tránh trùng cơ hội cũ) |
| Khi thiếu | Ghi TH cho từng phần và đề xuất skill thu thập: khách → `customer-research`; cạnh tranh → `competitor-research`; thời điểm, xu hướng → `xu-huong-mua-vu`; nội bộ → `company-analysis`; tìm kiếm → `tu-khoa`; Content → `nghien-cuu-content`; quảng cáo, landing page → `quang-cao-chuyen-doi`; kênh → `kenh-cong-dong`. Vẫn viết OPP nếu có ≥ 1 INS/FIND nhưng Mức ưu tiên tối đa Thấp |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Kết hợp dữ liệu | Lập **ma trận ba cột** cho mỗi nhu cầu: *Khách cần gì* (KH, INS, KEY, HT) · *Thị trường phục vụ ra sao* (DV, UD, TN, CNT, QC, KT) · *Doanh nghiệp có gì* (DN Kho lợi thế, Ma trận sản phẩm, Giới hạn triển khai). Thời điểm lấy từ XH, MV, BD |
| Nhu cầu mới hoặc chưa đáp ứng tốt | Nguồn tín hiệu: KH nhãn Nỗi đau/Rào cản/Câu hỏi lặp lại; KEY tăng theo mùa; XH "Tín hiệu mới"; phản hồi tiêu cực về đơn vị cùng ngành (DV). Một câu nói đơn lẻ không đủ |
| Cấp thiết và thời điểm | Cấp thiết: khách đang tìm giải pháp ngay (câu hỏi, so sánh, giao dịch) hay chỉ quan tâm chung. Thời điểm: MV (thời gian chuẩn bị), XH (ngắn/dài hạn). Hết thời gian chuẩn bị → Thời điểm Thấp |
| Khoảng trống | Trong mẫu đã xem, xếp mỗi nhu cầu vào một mức: *Chưa đơn vị nào đáp ứng* · *Đáp ứng chưa tốt* (phản hồi tiêu cực) · *Đáp ứng tốt nhưng còn cách tiếp cận khác* · *Đã bão hoà* (bỏ). Luôn ghi "trong mẫu N đơn vị", không khẳng định cho toàn thị trường |
| Đối chiếu năng lực | Mỗi khoảng trống phải khớp ≥ 1 lợi thế, sản phẩm hoặc nguồn lực có thật trong DN; không có → ghi "cần đầu tư: …" và khả thi Thấp |
| Giả thuyết cơ hội | Câu: *Nếu [doanh nghiệp] [cách khai thác] cho [nhóm khách] trong [thời điểm], thì [kết quả kỳ vọng], vì [INS/KT/XH]*. Kết quả kỳ vọng là giả thuyết, không phải cam kết |
| Đánh giá 4 tiêu chí | **Chất lượng bằng chứng**: Cao = ≥ 2 nguồn độc lập cùng hướng và có dữ liệu nội bộ hoặc FIND "Có căn cứ"; Trung bình = nhiều nguồn cùng loại hoặc một nguồn tốt; Thấp = gián tiếp, ít quan sát. **Tiềm năng**: quy mô nhóm khách, giá trị đơn, tần suất mua — chỉ dùng số có nguồn; không có số → tối đa Trung bình. **Khả thi**: sản phẩm, nhân sự, ngân sách, thời gian chuẩn bị. **Thời điểm**: còn kịp chuẩn bị và đúng nhu cầu mùa. Mỗi mức kèm một lý do; **không dùng điểm số** |
| Xếp ưu tiên | Cao: bằng chứng ≥ Trung bình, khả thi Cao, thời điểm còn kịp. Thấp: bằng chứng Thấp (bất kể tiềm năng) hoặc khả thi Thấp. Còn lại Trung bình. Ghi 4 mức vào `Lý do ưu tiên` theo mẫu "Bằng chứng: … · Tiềm năng: … · Khả thi: … · Thời điểm: …" |
| Loại cơ hội | Chọn 1 trong 10 giá trị schema: Phân khúc khách hàng, Sản phẩm và dịch vụ, Tình huống sử dụng, Mùa vụ, Định vị, Truyền thông, Content và quảng cáo, Hệ thống kênh, Chuyển đổi, Tái mua. Một nhu cầu có thể sinh nhiều OPP khác loại, nhưng không tách nhỏ chỉ để tăng số lượng |
| Kiểm chứng | `kiem_chung` để mặc định Cần bổ sung (chỉ `kiem-chung` đổi). `do_tin_cay` = chất lượng bằng chứng, kèm lý do. Phương án thử nghiệm nhỏ, có chỉ số và ngưỡng kết luận; ghi GT cho cơ hội ưu tiên Cao |
| Mâu thuẫn | Hai nguồn trái nhau về nhu cầu hoặc mức phục vụ → ghi MT, tách cơ hội theo phân khúc nếu do khác nhóm khách; không tự chọn một bên |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 0 | Đọc kho theo chủ đề, liệt kê OPP cũ còn hạn, ghi TH cho nhóm dữ liệu thiếu | Toàn kho | Danh sách bản ghi dùng được + phần thiếu | Có ≥ 2 trong 3 nhóm khách/cạnh tranh/doanh nghiệp, hoặc người dùng chấp nhận giới hạn |
| 1 | Liệt kê nhu cầu mới hoặc chưa được đáp ứng tốt | KH, INS, KEY, XH, FIND | Danh sách nhu cầu + mã bằng chứng | Mỗi nhu cầu có ≥ 1 bản ghi gốc |
| 2 | Đánh giá mức cấp thiết và thời điểm | KH (giai đoạn mua), KEY (mục đích tìm), MV, XH, BD | Nhu cầu × cấp thiết × thời điểm | — |
| 3 | Mô tả thị trường đang phục vụ nhu cầu ra sao | DV, UD, TN, CNT, QC | Cột "thị trường phục vụ" của ma trận | Đã ghi phạm vi mẫu |
| 4 | Xác định khoảng trống trong phạm vi nghiên cứu (4 mức) | Ma trận, KT | Khoảng trống còn lại; loại nhu cầu "Đã bão hoà" | — |
| 5 | Đối chiếu lợi thế, sản phẩm, nguồn lực | DN | Khoảng trống khớp năng lực / cần đầu tư | — |
| 6 | Viết giả thuyết cơ hội, chọn Loại cơ hội | Bước 1–5 | OPP nháp | Mỗi OPP có Insight hoặc khoảng trống làm căn cứ |
| 7 | Đánh giá 4 tiêu chí Cao/Trung bình/Thấp có lý do | OPP nháp | Lý do ưu tiên, `do_tin_cay` | Không còn tiêu chí chưa có lý do |
| 8 | Xếp ưu tiên theo quy tắc mục D; ghi Rủi ro | OPP nháp | Mức ưu tiên | — |
| 9 | Phương án thử nghiệm: làm gì, bao lâu, chỉ số, ngưỡng giữ/đổi | OPP | `Phương án thử nghiệm` (+ GT cho OPP Cao) | — |
| 10 | Ghi kho `kho.py them lo-opp.json --dot RP-xxx`, `kho.py kiem-tra --dot RP-xxx`, `kho.py bao-cao --dot RP-xxx --loai OPP --ra <thư mục đợt>` | Lô | OPP-xxx có liên kết | Không còn LỖI |
| 11 | Trình bản đồ cơ hội: bảng Loại cơ hội × Mức ưu tiên, mỗi ô ghi mã OPP + một dòng | OPP | Bản đồ cơ hội | **DỪNG**: người dùng chọn cơ hội đi tiếp; không tự chọn |

## F. Đầu ra — Bản đồ cơ hội (`OPP`)
Trường bắt buộc: Loại cơ hội · Nhu cầu thị trường · Nhóm khách hàng · Khoảng trống cạnh tranh · Lợi thế doanh nghiệp · Cách khai thác ·
Tiềm năng kinh doanh · Điều kiện và nguồn lực · Rủi ro · Mức ưu tiên · Lý do ưu tiên · Phương án thử nghiệm. Tuỳ chọn: Thời điểm.
`lien_ket` ≥ 1 bản ghi INS/FIND/KT/XH/MV (thêm DN, KEY... để truy vết). `trang_thai` Chờ duyệt; `kiem_chung` Cần bổ sung.
Bản đồ cơ hội: `kho.py bao-cao --loai OPP` (bảng + truy vết) và bảng Loại × Mức ưu tiên do agent viết trong `bao-cao.md`.
Ví dụ lô kiểm thử đủ chuỗi (giả định, F&B Tết): `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/marketing-opportunities.json`.

```json
{"loai": "OPP", "tieu_de": "Hộp quà Tết giao đúng ngày cho văn phòng đặt số lượng", "lien_ket": ["INS-001", "KT-001", "MV-001", "DN-001"],
 "do_tin_cay": "Trung bình", "ly_do_tin_cay": "Nhu cầu lặp ở 2 nền tảng công khai, chưa có đơn nội bộ cùng kỳ",
 "du_lieu": {"Loại cơ hội": "Mùa vụ", "Nhu cầu thị trường": "Văn phòng cần quà Tết số lượng, giao đúng ngày, xuất hoá đơn",
   "Nhóm khách hàng": "Nhân sự hành chính văn phòng 20–100 người", "Khoảng trống cạnh tranh": "KT-001: trong 6 đơn vị đã xem, 4 không cam kết ngày giao",
   "Lợi thế doanh nghiệp": "Bếp tự sản xuất, có xe giao nội thành (DN-001)", "Cách khai thác": "Gói đặt trước cho văn phòng, lịch giao chọn trước, mẫu thiệp in tên",
   "Tiềm năng kinh doanh": "Giả thuyết: đơn giá trị cao hơn khách lẻ; chưa có số đơn văn phòng năm trước", "Điều kiện và nguồn lực": "Chốt đơn trước 20 tháng Chạp, thêm 1 người điều phối giao",
   "Rủi ro": "Quá tải bếp tuần cuối; chưa rõ biên lợi nhuận theo hộp", "Mức ưu tiên": "Cao",
   "Lý do ưu tiên": "Bằng chứng: Trung bình (2 nền tảng) · Tiềm năng: Trung bình (chưa có số) · Khả thi: Cao (có bếp, xe) · Thời điểm: Cao (còn 8 tuần)",
   "Phương án thử nghiệm": "Mở đặt trước 2 tuần cho 30 văn phòng quen, đo số yêu cầu báo giá; ≥ 8 yêu cầu thì mở rộng", "Thời điểm": "Tháng 12 – trước Tết 2 tuần"}}
```

## G. Cơ chế bàn giao
| Loại cơ hội / nhu cầu | Chuyển cho | Dùng cho |
| --- | --- | --- |
| Phân khúc khách hàng, Định vị (mức Cao) | `dinh-huong-chien-luoc` (Masterplan), `dinh-vi-thong-diep` | Khoảng trống ứng viên cho hướng đi năm; phương án định vị |
| Sản phẩm và dịch vụ, Tình huống sử dụng, Tái mua | `san-pham-uu-dai` | Sản phẩm, combo, ưu đãi, Lead Magnet |
| Mùa vụ | `y-tuong-chien-dich` | Ý tưởng chiến dịch theo thời điểm |
| Truyền thông, Content và quảng cáo | `y-tuong-content`, `y-tuong-quang-cao` | Content Pillar, góc quảng cáo |
| Hệ thống kênh | `kenh-cong-dong` | Bản đồ kênh, cộng đồng, Creator |
| Chuyển đổi | `toi-uu-chuyen-doi` | Điểm nghẽn, FAQ, xử lý từ chối |
Lưu kho `OPP` (+ GT, TH, MT). Hạn dùng 180 ngày; workflow 08 cập nhật khi XH/MV đổi. OPP bị người dùng loại giữ lịch sử, không xoá.
Chỉ chuyển cơ hội người dùng đã chọn; ghi lựa chọn bằng `kho.py duyet OPP-xxx --trang-thai "Đã duyệt"` khi người dùng bảo.

## H. Kiểm tra chất lượng
- [ ] Mỗi OPP có nhu cầu từ dữ liệu khách, khoảng trống ghi phạm vi mẫu, lợi thế có thật trong DN.
- [ ] Không có OPP dựa trên lượt xem, trend đơn thuần hoặc một câu nói đơn lẻ.
- [ ] Bốn tiêu chí đều có mức và lý do; không có điểm số tuỳ ý; bằng chứng Thấp thì ưu tiên không quá Thấp.
- [ ] Không mặc định giảm giá, tăng ngân sách quảng cáo, mở kênh mới khi chưa có căn cứ vận hành và lợi nhuận.
- [ ] Mỗi OPP có phương án thử nghiệm có chỉ số và ngưỡng; OPP Cao có GT.
- [ ] Phần thiếu dữ liệu đã ghi TH kèm skill thu thập đề xuất; không trùng OPP cũ (đã `kho.py tim`).
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi bản đồ cơ hội đã trình và người dùng đã chọn (hoặc loại) từng cơ hội.

## Chế độ 3C (giữ nguyên quy trình cũ)
Khi gọi từ `research` chế độ 3C (`${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/che-do-3c.md`, giai đoạn 3): đầu vào `01-brief.md`,
`02-customer.md`, `03-competitor.md` + hồ sơ doanh nghiệp. Với mỗi cơ hội trả lời ba câu: **Customer** (khách cần/băn khoăn gì, URL, ngày) ·
**Competitor** (đối thủ đáp ứng ra sao, bỏ sót gì) · **Company** (sản phẩm, dịch vụ, nguồn lực tận dụng; thiếu dữ liệu gì). Chỉ giữ cơ hội có đủ
nhu cầu khách + bằng chứng + doanh nghiệp đủ khả năng; không áp đặt số lượng; không mặc định giảm giá, combo, tăng quảng cáo.
Ghi `04-tong-hop-3c.md`, **bảng cơ hội** giữ đúng cột cũ:
Phát hiện từ Customer | Phát hiện từ Competitor | Năng lực Company | Cơ hội cụ thể | Bằng chứng (trích dẫn nguồn trong 02/03) | Điều kiện cần kiểm tra | Mức ưu tiên (Cao/Vừa/Thấp, kèm lý do).
Phần cuối: điều CHƯA đủ dữ liệu · câu hỏi cần xác nhận với doanh nghiệp · gợi ý nghiên cứu bổ sung. Đồng thời ghi OPP (và INS nếu đủ căn cứ)
vào kho theo bảng cuối `che-do-3c.md` ("Vừa" ghi thành "Trung bình"). Kiểm tra: mỗi cơ hội trích được bằng chứng từ 02 hoặc 03; ngưỡng
"Đã xác minh" 3 nguồn theo `quy-tac-3c.md`. **DỪNG**, hỏi người dùng chọn cơ hội đi tiếp sang `marketing-recommendations`.
