---
name: competitor-research
description: Nghiên cứu cạnh tranh — chọn đơn vị theo tiêu chí, phân loại đối thủ trực tiếp, gián tiếp, sản phẩm/giải pháp thay thế; thu cùng một cấu trúc về danh mục, giá, combo, chính sách, định vị, lợi ích, khác biệt, bằng chứng, thông điệp, Content, quảng cáo, chiến dịch, kênh tiếp cận và chuyển đổi, phản hồi tích cực/tiêu cực của khách từ Google Search, website, landing page, TikTok, Facebook, Instagram, Meta Ads Library, Google Maps, sàn; so sánh, tìm lợi ích bị khai thác nhiều và nhu cầu chưa được phục vụ tốt, kiểm tra khoảng trống trong phạm vi mẫu và đối chiếu lợi thế doanh nghiệp. Ghi kho DV (hồ sơ đối thủ, bản đồ định vị), UD (sản phẩm và ưu đãi), TN (thông điệp), KT (khoảng trống và cơ hội khác biệt), dựng Ma trận cạnh tranh trong báo cáo. Dùng lại dữ liệu quet-doi-thu ≤ 30 ngày; không suy đoán doanh thu, ngân sách, ROAS đối thủ. Có chế độ 3C (nhánh Competitor của research, ra 03-competitor.md). Dùng khi người dùng gõ /masterplan-agent:competitor-research, nói "nghiên cứu đối thủ", "nghiên cứu cạnh tranh", "đối thủ định vị thế nào", "so giá với đối thủ", "khoảng trống cạnh tranh", "mình khác đối thủ ở đâu", "phân tích quảng cáo đối thủ".
argument-hint: "[ngành/sản phẩm hoặc danh sách đơn vị] [--dot RP-xxx] [--3c]"
---

# /masterplan-agent:competitor-research

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`.
Cách thu theo nền tảng trong `${CLAUDE_PLUGIN_ROOT}/references/nen-tang/`: `google-search.md`, `website-landing-page.md`, `tiktok.md`, `facebook.md`,
`instagram.md`, `meta-ads-library.md`, `google-maps.md`, `san-tmdt.md`. Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`.

**Chọn chế độ**: được giao `01-brief.md` (giai đoạn 2 của Research 3C, trực tiếp hoặc qua subagent `competitor-researcher` chế độ 3C) hoặc có `--3c`
→ **Chế độ 3C** (cuối file). Được giao mã đợt RP, hoặc chạy lẻ → chế độ kho (A–H).

## A. Mục tiêu
Biết những lựa chọn khách thực sự có thể chọn thay doanh nghiệp đang bán gì, giá và ưu đãi ra sao, nói gì, chứng minh bằng gì, tiếp cận và
chốt khách qua đâu, khách khen chê điều gì — để tìm **khoảng trống có bằng chứng** mà doanh nghiệp có lợi thế khai thác. Phục vụ quyết định:
định vị, khác biệt hoá, giá và ưu đãi, thông điệp, chọn kênh. Không phải để sao chép.

## B. Điều kiện kích hoạt
- **Dùng khi**: workflow 01, 02, 04, 05; người dùng hỏi đối thủ định vị, giá, thông điệp, khác biệt, khoảng trống.
- **Không dùng khi**: chỉ cần biết tuần này đối thủ có offer/ads mới → `quet-doi-thu`; cần phần đơn vị cùng ngành cho Market Research năm theo
  bộ mẫu → `nghien-cuu-thi-truong`; chỉ cần mổ xẻ quảng cáo và landing page → `quang-cao-chuyen-doi`.
- **Chạy độc lập** được. Bước 9 cần DN Kho lợi thế (`company-analysis`); bước 6 tốt hơn khi có KH (`customer-research`).

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Ngành/sản phẩm, địa bàn, phân khúc giá, nhóm khách; mã RP |
| Tuỳ chọn | Danh sách đối thủ đã biết (`cau-hinh.json → doi_thu`); tiêu chí riêng cần so |
| Dữ liệu nội bộ | Lý do khách nói đã chọn bên khác (`lead-hoi-thoai`), DN Ma trận sản phẩm và Kho lợi thế |
| Kế thừa | `kho.py tim --loai DV UD TN KT --chu "<ngành>"`; `doi-thu/<YYYY-MM-DD>/quet.json` và `doi-thu/lich-su/` của `quet-doi-thu` nếu ≤ 30 ngày (dùng làm EVD, không quét lại); `kho.py tim --loai KH DN` |
| Khi thiếu | Chưa rõ địa bàn → ghi phạm vi là giả định, không nói "đối thủ gần". Trang bị chặn → ghi vào MAU `Nguồn không truy cập được` và TH |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Nội dung | Danh mục, giá, combo, chính sách · định vị, lợi ích, khác biệt, bằng chứng · thông điệp · Content, quảng cáo, chiến dịch · kênh tiếp cận và chuyển đổi · phản hồi tích cực/tiêu cực |
| Tiêu chí chọn | Cùng nhu cầu khách + cùng địa bàn phục vụ + phân khúc giá ±30% + xuất hiện khi khách tìm (Search, Maps, sàn) hoặc được khách nhắc. Ghi `Lý do chọn` cho mỗi DV |
| Phân loại | **Trực tiếp** (cùng sản phẩm, cùng khách) · **Gián tiếp** (sản phẩm khác, cùng nhu cầu và ngân sách) · **Thay thế** (cách giải quyết khác: tự làm, không mua, sản phẩm khác ngành) |
| Xây từ khóa | [sản phẩm] + [địa bàn] · [nhu cầu] + tốt nhất/nên mua · [tên đơn vị] + review/giá/khuyến mãi · từ khóa KEY ưu tiên của `tu-khoa` |
| Chọn và thu mẫu | Phạm vi khởi tạo 5–10 đơn vị (≥ 1 gián tiếp hoặc thay thế); mỗi đơn vị cùng một khung thu (bảng F) và cùng khoảng thời gian; Content/quảng cáo lấy cả mức nổi bật và thông thường; phản hồi lấy cả khen và chê. Mỗi nguồn một MAU |
| Trích xuất | Giá chỉ ghi khi thấy rõ (kèm ngày, điều kiện); thông điệp chép đúng câu chính (ngắn); bằng chứng thương hiệu ghi loại (số khách, chứng nhận, review, KOL) và nơi thấy |
| So sánh | Ma trận tiêu chí × (doanh nghiệp + từng đơn vị); đếm lợi ích nào được bao nhiêu đơn vị nhấn mạnh; đặt cạnh nhu cầu/rào cản trong KH để thấy nhu cầu **chưa được phục vụ tốt** |
| Kiểm chứng khoảng trống | KT chỉ hợp lệ khi: đã xem đủ mẫu đã định, nhu cầu có bằng chứng từ khách (KH/FIND), và ghi `Giới hạn` "trong mẫu N đơn vị". Không có KH → FIND Giả thuyết, chưa tạo KT |
| Cấm | Suy đoán doanh thu, ngân sách, ROAS, CPA, hiệu quả quảng cáo đối thủ; coi nhiều view là bán tốt; coi quảng cáo chạy lâu là quảng cáo hiệu quả |
| Mâu thuẫn | Giá website khác giá sàn, hay thông điệp khác trải nghiệm trong review → ghi cả hai (MT), không chọn một bên |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 1 | Xác định tiêu chí chọn đơn vị nghiên cứu; đọc kho, `quet-doi-thu` | RP, DN, kho | Tiêu chí + phạm vi | — |
| 2 | Lập danh sách và phân loại trực tiếp/gián tiếp/thay thế | Search, Maps, sàn, KH | Danh sách + lý do chọn | **DỪNG**: người dùng duyệt danh sách |
| 3 | Thu dữ liệu từng đơn vị theo cùng cấu trúc | Website, landing page, Social, Ads Library, Maps, sàn | EVD + MAU; DV, UD, TN nháp | Mọi đơn vị đủ khung hoặc ghi rõ ô thiếu |
| 4 | So sánh sản phẩm, giá, lợi ích, định vị | DV, UD | Ma trận phần sản phẩm; `Phân khúc giá` | — |
| 5 | So sánh thông điệp, Marketing, kênh | TN, DV, EVD | Ma trận phần truyền thông; FIND Quan sát/Mẫu lặp | — |
| 6 | Đối chiếu phản hồi khách | Review, bình luận, KH | `Phản hồi tích cực/tiêu cực` trong DV | Mỗi đơn vị có phản hồi hoặc "chưa thấy" |
| 7 | Tách lợi ích được khai thác nhiều với nhu cầu chưa phục vụ tốt | Ma trận, KH | FIND (số đơn vị nhấn mạnh / tổng) | — |
| 8 | Kiểm tra khoảng trống có thật trong phạm vi mẫu | FIND, KH, EVD | KT nháp có `Giới hạn` | Đạt điều kiện ở D |
| 9 | Đối chiếu lợi thế doanh nghiệp, ghi điều kiện khai thác; ghi kho `kho.py them lo-dt.json --dot RP-xxx` → `kiem-tra` | DN Kho lợi thế, KT | KT hoàn chỉnh; báo cáo `bao-cao-canh-tranh.md` | Không LỖI; **DỪNG** chờ duyệt |

## F. Đầu ra
| Mã / bảng | Trường (schema) | Cách dựng |
| --- | --- | --- |
| DV – Hồ sơ đối thủ | Tên, Phân loại, Khách hàng, Sản phẩm, Giá, Định vị, Kênh, Nguồn · tuỳ chọn Lý do chọn, Lợi ích, Điểm khác biệt, Bằng chứng thương hiệu, Phản hồi tích cực, Phản hồi tiêu cực, Phân khúc giá | Một bản ghi mỗi đơn vị |
| Bản đồ định vị | Trong DV: Phân khúc giá, Khách hàng, Lợi ích (trọng tâm), Điểm khác biệt | Báo cáo dựng bảng 4 cột này cho doanh nghiệp + mọi DV; nếu cần hình, trục X = phân khúc giá, trục Y = lợi ích trọng tâm |
| UD – Sản phẩm và ưu đãi | Đơn vị, Sản phẩm, Giá, Combo, Chính sách, Thời gian, Nguồn · Quà tặng, Điều kiện, Cách trình bày | Một bản ghi mỗi ưu đãi/gói; hạn 45 ngày |
| TN – Thông điệp | Thông điệp, Đơn vị, Lợi ích, Nhóm khách, Kênh, Bằng chứng, Nguồn | Một bản ghi mỗi thông điệp chính |
| KT – Khoảng trống | Nhu cầu, Mức độ được phục vụ, Bằng chứng, Giới hạn, Lợi thế doanh nghiệp, Điều kiện khai thác | Cha DV/UD/TN/FIND/KH; cơ hội khác biệt ghi trong Lợi thế doanh nghiệp + Điều kiện khai thác |
| Ma trận cạnh tranh | Báo cáo, không phải loại kho | `kho.py xuat --ra nghien-cuu/<thư mục đợt>/xuat --dot RP-xxx` lấy DV.csv, UD.csv, TN.csv; viết `bao-cao-canh-tranh.md`: hàng = tiêu chí (sản phẩm, giá, combo, chính sách, định vị, lợi ích, khác biệt, bằng chứng, thông điệp, kênh chuyển đổi, phản hồi), cột = Doanh nghiệp (từ DN) + từng đơn vị; mỗi ô ghi mã nguồn (DV-xxx/UD-xxx/EVD-xxx); ô không có dữ liệu ghi "chưa thấy" |
Ví dụ lô đầy đủ (giả định, thời trang công sở): `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/competitor-research.json`.
```json
{"loai": "KT", "tieu_de": "Chưa đơn vị nào tư vấn size theo số đo cho dáng người thấp", "lien_ket": ["@d1", "@d2", "@k1"], "kiem_chung": "Cần bổ sung",
 "du_lieu": {"Nhu cầu": "Mua online vừa dáng người dưới 1m55", "Mức độ được phục vụ": "Thấp: 0/6 đơn vị có bảng size theo chiều cao",
   "Bằng chứng": "DV-001, DV-002, KH-001", "Giới hạn": "Trong mẫu 6 đơn vị, 11/2026", "Lợi thế doanh nghiệp": "Có thợ may sửa độ dài tại xưởng",
   "Điều kiện khai thác": "Đo được 3 size chiều dài cho 10 mẫu bán chạy"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| Kho DV, UD, TN, KT (+ EVD, MAU, FIND, MT, TH); `bao-cao-canh-tranh.md` | `marketing-opportunities` (Khoảng trống cạnh tranh), `dinh-vi-thong-diep` (bối cảnh cạnh tranh), `san-pham-uu-dai` (UD), `quang-cao-chuyen-doi` (đơn vị cần mổ quảng cáo), `quet-doi-thu` (danh sách theo dõi định kỳ), `insight` | Định vị, khác biệt, giá và ưu đãi, thông điệp | DV/TN 90 ngày, UD 45 ngày, KT 120 ngày. Lần sau đọc `quet-doi-thu` mới nhất, chỉ cập nhật ô thay đổi bằng `kho.py cap-nhat` |

## H. Kiểm tra chất lượng
- [ ] Mỗi DV có phân loại, lý do chọn và nguồn; có ≥ 1 đơn vị gián tiếp hoặc thay thế (hoặc ghi vì sao không có).
- [ ] Mọi đơn vị thu theo cùng khung, cùng khoảng thời gian; ô thiếu ghi "chưa thấy", không bỏ trống im lặng.
- [ ] Giá có ngày và điều kiện; không có doanh thu, ngân sách, ROAS đoán.
- [ ] Mỗi KT có bằng chứng nhu cầu từ khách, giới hạn mẫu và lợi thế doanh nghiệp đối chiếu.
- [ ] Không đề xuất sao chép nội dung đối thủ; không khẳng định "gần" khi chưa rõ địa bàn.
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI; Ma trận cạnh tranh có mã nguồn mỗi ô.
**Hoàn thành** khi đủ DV cho mẫu đã duyệt, có Ma trận cạnh tranh, bản đồ định vị và danh sách KT chờ duyệt.

## Chế độ 3C (nhánh Competitor của `/masterplan-agent:research`)
Đầu vào: `01-brief.md` (câu hỏi Competitor, phạm vi), đối thủ trong hồ sơ, khu vực, mức giá, hai mốc (A: cùng kỳ năm trước, B: hiện tại).
1. **Phạm vi cạnh tranh**: chưa có khu vực cụ thể → ghi phạm vi là giả định, hỏi người dùng. Tìm trên Google Maps: đối thủ trực tiếp (cùng sản phẩm,
   giá, khách) và lựa chọn thay thế (cùng nhu cầu, khác sản phẩm, cùng vùng và mức chi). Lưu tên, địa chỉ/URL, link Maps, menu/giá, lý do khách có thể chọn.
2. **Dò từng đối thủ**: TikTok (hook, format, món/sản phẩm đẩy, CTA, bình luận) · Fanpage (giá, ưu đãi, bằng chứng, cách đặt) · Google Maps (khen/chê,
   ảnh, menu) · Meta Ads Library (tìm đúng tên Page, chọn Việt Nam) · Website/menu (giá, chính sách, đường đặt chỗ).
3. **Hai mốc**: Mốc A họ ưu tiên gì; Mốc B đang đẩy gì, đổi gì. Meta Ads Library không lưu đủ quảng cáo thương mại đã dừng → kết hợp Fanpage,
   TikTok, website có ngày rõ; thiếu mốc → "chưa đủ dữ liệu".
Quy tắc: không đoán doanh thu/ngân sách; view cao không phải bán tốt; chỉ ghi giá thấy rõ; ghi nguồn không truy cập được; không sao chép.
Đầu ra `03-competitor.md`:
- **Bảng 1 – Đối thủ**: Đối thủ (trực tiếp/thay thế) | Sản phẩm/giá | Content nổi bật | Cách chuyển đổi | Phản hồi khách | URL/ngày
- **Bảng 2 – Điểm hấp dẫn và điểm còn gây phân vân**: Đối thủ | Điểm hấp dẫn | Điểm còn gây phân vân | Bài học cần kiểm chứng cho doanh nghiệp
- **Bảng 3 – Đối chiếu hai mốc**: Đối thủ | Mốc A | Mốc B | Tiếp diễn hay thay đổi | Hướng cần xem xét
- **Phần cuối**: cách làm đáng tham khảo; khoảng trống có bằng chứng; nguồn không truy cập được.
Nếu có `kho/`: ghi thêm mỗi dòng Bảng 1 thành DV (+ UD khi thấy giá/ưu đãi, + EVD theo URL) với `--dot` của đợt 3C.
Kiểm tra: mỗi đối thủ có phân loại · mọi dòng có URL và ngày · không số doanh thu/ngân sách đoán · không "gần quán" khi chưa có khu vực ·
ghi nguồn không đọc được. **DỪNG**, hỏi người dùng duyệt.
