---
name: nghien-cuu-content
description: Nghiên cứu Content đa nền tảng (TikTok, Facebook, Instagram, Threads, YouTube, website/blog, kênh Social của chính doanh nghiệp) để tìm chủ đề, nhu cầu, góc khai thác và cấu trúc nội dung ứng dụng được — thu mẫu cả nổi bật, thông thường, ít tương tác của đơn vị cùng ngành, Creator/KOL/KOC, người dùng và ngành khác có nguyên lý phù hợp; bóc tách chủ đề, Hook, góc, thông điệp, cấu trúc, format, CTA, phản hồi người xem; so sánh chỉ số trong điều kiện tương đồng; tìm chủ đề và công thức lặp; đặt giả thuyết yếu tố thu hút và hướng ứng dụng cho thương hiệu (không sao chép). Ghi vào kho Content nghiên cứu (CNT) và phát hiện mẫu lặp (FIND), kèm bằng chứng EVD và nhật ký lấy mẫu MAU. Dùng khi người dùng nói "nghiên cứu content", "ngành mình đang làm content gì", "chủ đề nào đang được quan tâm", "bóc content đối thủ/creator", "content nào chạy tốt và vì sao", "tìm Content Pillar", "tìm hook hay trong ngành", hoặc khi workflow 03 / 07 cần CNT.
argument-hint: "[chủ đề hoặc nhóm khách] [--nen-tang tiktok,facebook,...] [--dot RP-xxx]"
---

# /masterplan-agent:nghien-cuu-content

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`.
Cách làm theo nền tảng (đọc đúng file của nền tảng sẽ thu): `${CLAUDE_PLUGIN_ROOT}/references/nen-tang/` — `tiktok.md`, `facebook.md`,
`instagram.md`, `threads.md`, `youtube.md`, `website-landing-page.md`, `google-search.md` (tìm bài blog, kênh), `crm-noi-bo.md` (số kênh nội bộ).
Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...` (chạy trong thư mục làm việc). Thư mục đợt: `nghien-cuu/<YYYY-MM-DD>-<chủ-đề>/`.

## A. Mục tiêu
Hiểu **thị trường đang nói gì, nói thế nào và người xem phản hồi ra sao** quanh nhu cầu của nhóm khách, để chọn Content Pillar, chủ đề,
góc khai thác, Hook, cấu trúc và format có căn cứ. Phục vụ quyết định: Content Pillar của kỳ, chủ đề ưu tiên, series, công thức nội dung
cần thử, cách tái định dạng giữa nền tảng. Skill chỉ **nghiên cứu và bàn giao**, không viết bài hay kịch bản hoàn chỉnh.

## B. Điều kiện kích hoạt
- **Dùng khi**: cần biết nội dung nào trong ngành thu hút, nhóm khách quan tâm chủ đề gì, công thức nào lặp lại; workflow 03 (Content
  Marketing) hoặc 07 (Phát triển kênh) tới bước Content. Yêu cầu tiêu biểu: "nghiên cứu content ngành mỹ phẩm", "creator nào làm tốt chủ đề X".
- **Không dùng khi**: chỉ cần đánh giá hiệu quả kênh của chính doanh nghiệp → `danh-gia-kenh`; theo dõi offer/ads đối thủ định kỳ →
  `quet-doi-thu`; cần bóc công thức dựng video/thiết kế chi tiết → `format-sang-tao` (chạy sau skill này); cần viết bài → plugin content-agent.
- **Chạy độc lập** được. Tốt hơn nếu kho đã có SEG/KH (`customer-research`) và KEY (`tu-khoa`) để xây bộ từ khóa sát nhu cầu.

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Nhóm khách cần tiếp cận; mục tiêu nghiên cứu (Thu hút / Nhận diện / Niềm tin / Chuyển đổi); mã đợt RP (tạo bằng `research` nếu chưa có) |
| Tuỳ chọn | Nền tảng ưu tiên; danh sách kênh tham khảo người dùng biết; khoảng thời gian (mặc định 90 ngày gần nhất); ngành khác muốn học nguyên lý |
| Dữ liệu nội bộ | Kết quả `danh-gia-kenh` (bài tốt/kém của chính doanh nghiệp), file xuất Business Suite/TikTok Studio trong `nhap/` |
| Kế thừa từ kho | `kho.py tim --loai CNT FIND --chu "<chủ đề>"` (tránh thu lại URL đã có); `kho.py tim --loai SEG KH KEY INS --chu "<nhóm khách>"` |
| Khi thiếu | Không có SEG/KH → hỏi người dùng 3 câu (khách là ai, họ hay hỏi gì, mua khi nào) và ghi TH; nền tảng cần đăng nhập/CAPTCHA → nhờ người dùng mở hoặc dùng nền tảng khác, ghi MAU `Nguồn không truy cập được` |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Phạm vi mẫu | 4 nhóm nguồn: đơn vị cùng ngành · Creator/KOL/KOC/người dùng · ngành khác có nguyên lý phù hợp (ghi rõ nguyên lý gì) · nội dung của chính doanh nghiệp kèm số thật từ `danh-gia-kenh` |
| Nguồn và công cụ | Tìm kiếm trong ứng dụng/web của TikTok, Facebook, Instagram, Threads, YouTube; Google Search cho blog/website; Claude in Chrome để mở bài và đọc bình luận; file nội bộ. Kiểm tra công cụ có trong phiên trước khi thu (quy-tac-nghien-cuu.md mục 7) |
| Xây từ khóa | 3 lớp: (1) từ khóa nhu cầu từ KEY/KH ("da dầu mụn nên dùng gì"); (2) từ khóa chủ đề/format ("review", "routine", "so sánh"); (3) hashtag và tên kênh tìm được ở lớp 1–2. Ghi bộ từ khóa thực dùng vào MAU |
| Chọn và thu mẫu | Phạm vi khởi tạo 30–50 Content, 3–5 nền tảng, 8–15 kênh. Mỗi chủ đề lấy đủ 3 mức `Mức mẫu`: Nổi bật (top theo tương tác trong kênh), Thông thường (quanh trung vị của kênh), Ít tương tác. Ghi ngày đăng, chỉ lấy trong khoảng thời gian Brief. Bão hoà: 10–15 mẫu liên tiếp không tạo chủ đề/công thức mới |
| Trích xuất | Mỗi mẫu một CNT: chủ đề, Content Pillar, Hook (nguyên văn câu/khung đầu), góc khai thác, thông điệp, cấu trúc (các phần theo thứ tự), format, CTA, chỉ số công khai (số + thời điểm đọc), phản hồi đáng chú ý (câu hỏi, phản đối, khen). Bình luận có ý nghĩa đồng thời ghi EVD để `customer-research`/`insight` dùng lại |
| Phân loại, đối chiếu | Gom theo chủ đề × góc × format × mục tiêu. **So sánh chỉ số chỉ trong điều kiện tương đồng**: cùng kênh, hoặc kênh cùng cỡ (chênh ≤ 3 lần người theo dõi), cùng nền tảng, cùng khoảng thời gian; dùng tỷ lệ so với trung vị của kênh, không so lượt xem tuyệt đối giữa kênh lớn và nhỏ |
| Mẫu lặp | Một chủ đề/công thức xuất hiện ≥ 3 lần ở ≥ 2 kênh → FIND `Mẫu lặp` (ghi số lần / tổng mẫu). Chỉ xuất hiện ở nhóm Nổi bật mà không có ở nhóm Ít tương tác → mới là ứng viên "yếu tố thu hút" |
| Giả thuyết | Yếu tố thu hút luôn ghi là giả thuyết (FIND `Giả thuyết` hoặc trường `Giả thuyết cần kiểm chứng`), kèm cách kiểm chứng (đăng thử 2 phiên bản, đo tỷ lệ xem hết/lưu) |
| Kiểm chứng | Mở thật từng bài; không kết luận từ ảnh bìa/tiêu đề. Chỉ số ghi đúng số hiển thị và ngày đọc; nền tảng ẩn số → "không hiển thị". Không suy diễn lượt tiếp cận, doanh thu, hiệu quả bán hàng từ lượt xem |
| Mâu thuẫn | Cùng công thức nhưng kết quả trái nhau giữa nền tảng/nhóm khách → ghi MT, tách FIND theo nền tảng, không gộp |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 1 | Xác định nhóm khách, mục tiêu nghiên cứu (Thu hút / Nhận diện / Niềm tin / Chuyển đổi), đọc kho | RP, SEG, KH, KEY, CNT cũ | Câu hỏi nghiên cứu Content + danh sách URL đã có | Người dùng xác nhận nhóm khách và mục tiêu |
| 2 | Lập bộ từ khóa 3 lớp và danh sách kênh theo 4 nhóm nguồn | KEY, KH, tìm kiếm thử | Bảng từ khóa + 8–15 kênh | **DỪNG** trình danh sách kênh, chờ duyệt (người dùng thêm/bớt) |
| 3 | Thu mẫu theo chủ đề, nền tảng, thời gian | Nền tảng đã duyệt | Danh sách URL + ngày đăng | Mỗi nền tảng có mẫu hoặc ghi lý do không thu được |
| 4 | Cân bằng mẫu: đủ Nổi bật, Thông thường, Ít tương tác cho mỗi chủ đề chính | Danh sách URL | Mẫu cân bằng; MAU cho mỗi nền tảng | Mỗi chủ đề chính có ≥ 2 mức |
| 5 | Bóc tách từng mẫu: chủ đề, Hook, góc, thông điệp, cấu trúc, format, CTA | Bài/video đã mở | Nháp CNT | Mọi CNT đủ trường bắt buộc |
| 6 | Đọc phản hồi: câu hỏi lặp, phản đối, dấu hiệu quan tâm (hỏi giá, xin link, tag bạn, lưu) | Bình luận | `Phản hồi đáng chú ý` + EVD bình luận | Đã đọc ≥ 20 bình luận/mẫu nổi bật (hoặc toàn bộ nếu ít hơn) |
| 7 | So sánh chỉ số trong điều kiện tương đồng | CNT + trung vị kênh | Bảng tỷ lệ so với trung vị | Mỗi so sánh ghi rõ điều kiện |
| 8 | Tìm chủ đề và công thức lặp | Bảng CNT | FIND `Mẫu lặp` (số lần/tổng) | Đã đối chiếu cả nhóm Ít tương tác |
| 9 | Đặt giả thuyết yếu tố thu hút | FIND, so sánh bước 7 | FIND `Giả thuyết` + GT nếu cần thử | Mỗi giả thuyết có cách kiểm chứng |
| 10 | Viết hướng ứng dụng cho thương hiệu (nguyên lý, không sao chép câu chữ/hình) rồi ghi kho: `kho.py them lo-cnt.json --dot RP-xxx` → `kho.py kiem-tra --dot RP-xxx` | CNT, FIND | Lô EVD, MAU, CNT, FIND (+ GT, TH, MT) | Không còn LỖI; **DỪNG** trình bảng chủ đề/công thức chờ duyệt |

## F. Đầu ra
**Kho Content nghiên cứu (`CNT`)** — trường bắt buộc: URL · Nền tảng · Kênh · Ngày đăng · Ngày thu thập · Nhóm khách hàng · Mục tiêu ·
Chủ đề · Hook · Góc khai thác · Thông điệp · Cấu trúc nội dung · Format · Chỉ số công khai · Mức mẫu (Nổi bật / Thông thường / Ít tương tác)
· Yếu tố có thể học hỏi · Hướng ứng dụng. Tuỳ chọn (nên điền): Content Pillar · Nhu cầu hoặc Insight giả định · CTA · Phản hồi đáng chú ý ·
Điểm mạnh · Hạn chế · Giả thuyết cần kiểm chứng. Kênh ghi dạng mô tả ("Creator review mỹ phẩm ~50k theo dõi"), tên thật chỉ để ở URL.
**Phát hiện (`FIND`, Nhóm = Content)**: chủ đề/công thức lặp, liên kết EVD. Mỗi lượt thu một **MAU**. Báo cáo:
`kho.py bao-cao --dot RP-xxx --loai CNT FIND --ra nghien-cuu/<thư mục đợt>`. Ví dụ đầy đủ kiểm thử được:
`${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/nghien-cuu-content.json`.

Ví dụ bản ghi (giả định, rút gọn từ file ví dụ):
```json
{"tam": "c1", "loai": "CNT", "tieu_de": "Video routine da dầu 3 bước buổi sáng", "lien_ket": ["@e1"],
 "do_tin_cay": "Trung bình", "ly_do_tin_cay": "Đã xem toàn bộ video và 40 bình luận; chỉ số một thời điểm",
 "du_lieu": {"URL": "https://www.tiktok.com/@vidu-creator/video/101", "Nền tảng": "TikTok", "Kênh": "Creator chăm sóc da ~80k theo dõi",
   "Ngày đăng": "2026-10-28", "Ngày thu thập": "2026-11-26", "Nhóm khách hàng": "Nữ 20–28, da dầu mụn", "Mục tiêu": "Thu hút",
   "Content Pillar": "Kiến thức chăm sóc da", "Chủ đề": "Routine buổi sáng cho da dầu", "Nhu cầu hoặc Insight giả định": "Muốn routine ngắn, sợ bôi nhiều lớp gây bí",
   "Hook": "Da dầu thì sáng chỉ cần 3 bước thôi", "Góc khai thác": "Rút gọn, ít mà đúng", "Thông điệp": "Ít bước nhưng đúng thứ tự thì da vẫn ổn",
   "Cấu trúc nội dung": "Hook phủ định thói quen → 3 bước có tên sản phẩm loại → lỗi hay gặp → CTA lưu video", "Format": "Video dọc 45 giây, nói thẳng camera",
   "CTA": "Lưu lại để làm theo", "Chỉ số công khai": "182k xem, 9,1k lưu, 310 bình luận (đọc 26/11/2026)", "Mức mẫu": "Nổi bật",
   "Phản hồi đáng chú ý": "Nhiều câu hỏi da dầu có cần kem dưỡng không", "Điểm mạnh": "Hook đi thẳng vào nỗi lo bôi nhiều lớp",
   "Hạn chế": "Không nêu thời gian thấy kết quả", "Yếu tố có thể học hỏi": "Khung số bước cụ thể + lỗi hay gặp",
   "Giả thuyết cần kiểm chứng": "Hook có con số bước tăng tỷ lệ lưu", "Hướng ứng dụng": "Series routine theo loại da, mỗi video một lỗi hay gặp"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| `CNT`, `FIND` (Nhóm Content), `EVD`, `MAU`; GT/TH/MT nếu có | `format-sang-tao` (bóc công thức dựng từ CNT), `insight` (phản hồi người xem), `y-tuong-content` (Content Pillar, chủ đề, Hook, series, góc, tái định dạng); plugin content-agent nhận qua `kho.py xuat --loai CNT FIND --ra nghien-cuu/<đợt>/xuat` | Content Pillar, lịch chủ đề, Hook, series, tái định dạng giữa nền tảng | Hạn dùng CNT 120 ngày; workflow 08 chỉ thu lại nền tảng/chủ đề quá hạn; URL trùng tự gộp liên kết |

## H. Kiểm tra chất lượng
- [ ] Mỗi CNT đã mở và xem/đọc thật; Hook ghi đúng nguyên văn hoặc mô tả khung đầu quan sát được.
- [ ] Mẫu có đủ 3 mức Nổi bật / Thông thường / Ít tương tác; có ít nhất 2 nhóm nguồn (ngành, Creator, ngành khác, nội bộ).
- [ ] Chỉ số công khai có ngày đọc; mọi so sánh ghi điều kiện tương đồng; không suy diễn doanh thu, tiếp cận, hiệu quả bán hàng.
- [ ] FIND `Mẫu lặp` có số lần / tổng mẫu; yếu tố thu hút ghi là giả thuyết, có cách kiểm chứng.
- [ ] Hướng ứng dụng là nguyên lý cho thương hiệu, không chép câu chữ, hình ảnh, nhân vật của kênh khác.
- [ ] Mỗi nền tảng có MAU (3 con số thu thập / đọc được / sử dụng, giới hạn mẫu); không có thông tin cá nhân người bình luận.
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi CNT + FIND ở trạng thái Chờ duyệt, người dùng có bảng chủ đề/công thức lặp và danh sách đề xuất chuyển `format-sang-tao`, `y-tuong-content`.
