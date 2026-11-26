---
name: y-tuong-content
description: Phát triển ý tưởng và định hướng Content từ kho nghiên cứu — kết hợp phân khúc (SEG), Insight (INS), từ khóa (KEY), xu hướng (XH), Content thị trường (CNT), format (FMT) và thông điệp (TD) để xác định mục tiêu Content, chuyển nhóm nhu cầu và từ khóa thành Content Pillar, tạo chủ đề, nhiều góc khai thác, ghép Hook, thông điệp, format, triển khai theo nền tảng, kiểm trùng với ý tưởng cũ và khả năng sản xuất, liên kết dữ liệu gốc. Đầu ra kho IDEA (dựng hệ thống Content Pillar, kho chủ đề, góc, Hook, series). Không tạo hàng loạt ý tưởng chỉ khác tiêu đề. Dùng khi người dùng gõ /masterplan-agent:y-tuong-content, nói "ý tưởng Content", "30 ý tưởng Content dựa trên nghiên cứu", "Content Pillar", "chủ đề Content tháng tới", "góc khai thác", "Hook", "series video", "Content SEO từ từ khóa".
argument-hint: "[nhóm khách, chủ đề hoặc số ý tưởng] [--dot RP-xxx]"
---

# /masterplan-agent:y-tuong-content

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`.
Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`. Skill này **không thu thập lại dữ liệu**.

## A. Mục tiêu
Biến nhu cầu, Insight và từ khóa đã có bằng chứng thành **hệ thống Content có cấu trúc**: Pillar → chủ đề → góc khai thác → Hook → format →
nền tảng, mỗi ý tưởng truy được về dữ liệu gốc. Phục vụ quyết định: Content Pillar của kỳ, chủ đề ưu tiên, series, phân bổ nền tảng; là đầu vào
cho Content Strategy và Calendar của Agent Content.

## B. Điều kiện kích hoạt
- **Dùng khi**: kho có INS hoặc KEY/KH; workflow 03; người dùng xin ý tưởng, Pillar, chủ đề, Hook, series.
- **Không dùng khi**: cần lịch đăng, viết bài hoàn chỉnh → `content-agent:calendar`, `content-agent:write`; cần cấu trúc format chi tiết →
  `format-sang-tao`; chưa có dữ liệu khách hay từ khóa → `customer-research`, `tu-khoa`.
- **Chạy độc lập** được (tự tạo RP mức Nhanh). Tốt hơn khi đã có `nghien-cuu-content`, `format-sang-tao`, `dinh-vi-thong-diep`.

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Nhóm khách hoặc chủ đề; mã đợt RP; mục tiêu Content (Thu hút, Nuôi dưỡng, Xây dựng niềm tin, Chuyển đổi) hoặc để agent đề xuất theo HT |
| Tuỳ chọn | Số ý tưởng cần (không ép số; ưu tiên đa dạng chủ đề + góc); nền tảng; nguồn lực sản xuất (người quay, thời gian, ngân sách) |
| Dữ liệu nội bộ | Bài đã đăng và hiệu quả (Agent Content tab 05–06 nếu có), câu hỏi khách trong Inbox (`lead-hoi-thoai`) |
| Kế thừa từ kho | `kho.py tim --loai SEG INS KH HT --chu "<chủ đề>"` · `--loai KEY XH MV` · `--loai CNT FMT` · `--loai TD OPP OFFER` · `--loai IDEA` (ý tưởng cũ để kiểm trùng) |
| Khi thiếu | Thiếu KEY → Pillar dựa trên INS/KH, ghi TH, đề xuất `tu-khoa`. Thiếu CNT → không ghi "đã bão hoà", đề xuất `nghien-cuu-content`. Thiếu FMT → ghi format chung (video ngắn, carousel), đề xuất `format-sang-tao`. Thiếu TD → thông điệp tạm từ INS, ghi "chưa đối chiếu TD" |

## D. Phương pháp
**Phân biệt khái niệm** (bắt buộc dùng đúng):
| Khái niệm | Là gì | Ví dụ (thời trang công sở) |
| --- | --- | --- |
| Content Pillar | Nhóm nội dung lớn, gắn một nhóm nhu cầu và từ khóa, kéo dài nhiều kỳ | Phối đồ công sở theo vóc dáng |
| Chủ đề | Vấn đề cụ thể trong Pillar, trả lời một nhu cầu/câu hỏi | Chọn quần cho người thấp dưới 1m55 |
| Góc khai thác | Cách nhìn vào chủ đề, gắn một Insight, rào cản hoặc động lực | Sai lầm khiến chân trông ngắn hơn |
| Hook | Câu/khung hình mở đầu 1–3 giây theo góc | "3 kiểu quần đang làm bạn thấp đi" |
| Format | Hình thức trình bày (FMT) | Video thử đồ trước–sau 30 giây |
| Ý tưởng (IDEA) | Tổ hợp Pillar + Chủ đề + Góc + Hook + Format + Nền tảng + CTA cho một nhóm khách và mục tiêu | Một bản ghi IDEA |

| Hạng mục | Cách làm |
| --- | --- |
| Mục tiêu Content | Gắn giai đoạn HT: Nhận biết → Thu hút; Tìm hiểu/So sánh → Nuôi dưỡng, Xây dựng niềm tin; Cân nhắc mua → Chuyển đổi. Ghi vào trường `Mục tiêu` |
| Dựng Pillar | Gom KEY theo `Nhóm chủ đề` + `Nhu cầu`, gộp với cụm nhu cầu từ KH/INS; mỗi cụm đủ lớn (≥ 3 chủ đề khả dĩ) thành một Pillar. Thường 3–5 Pillar; ghi lý do mỗi Pillar (nhu cầu + bằng chứng) |
| Chủ đề | Mỗi chủ đề trả lời một KEY, một KH nhãn Câu hỏi/Nỗi đau hoặc một XH/MV; ghi mã nguồn |
| Góc khai thác | Mỗi chủ đề 2–4 góc, mỗi góc gắn **một** yếu tố khác nhau: rào cản, động lực, sai lầm phổ biến, so sánh, trải nghiệm, số liệu có nguồn, câu chuyện khách (đã ẩn danh). Góc chỉ đổi câu chữ không tính |
| Kết hợp | Góc + Hook (công thức từ FMT/CNT nổi bật) + thông điệp (TD, hoặc INS) + format (FMT) + CTA phù hợp mục tiêu |
| Theo nền tảng | Nền tảng chọn theo nơi KEY/CNT xuất hiện; ghi `Tái định dạng` (ví dụ video TikTok → carousel Instagram → bài Facebook) thay vì tạo ý tưởng mới |
| Series | Chủ đề lặp được theo cấu trúc cố định (cùng format, khác trường hợp) → điền `Series`; mỗi tập vẫn là một IDEA có chủ đề hoặc góc riêng |
| Kiểm trùng | **Hai ý tưởng trùng cặp Chủ đề + Góc khai thác là trùng** (dù khác Hook, tiêu đề, nền tảng). So với IDEA cũ trong kho (`kho.py tim --loai IDEA --chu "<chủ đề>"`) và trong lô; trùng → gộp thành biến thể Hook hoặc Tái định dạng |
| Đã bão hoà | Chủ đề + góc mà CNT cho thấy nhiều đơn vị đã làm giống nhau → chỉ giữ khi có góc khác hoặc bằng chứng riêng |
| Khả năng sản xuất | Đối chiếu `Yêu cầu nguyên liệu`, `Mức độ khó và nguồn lực` của FMT với nguồn lực người dùng; vượt nguồn lực → Mức ưu tiên Thấp hoặc đổi format |
| Mức ưu tiên | Cao: gắn INS/KEY ưu tiên Cao, chưa bão hoà, làm được ngay. Thấp: bằng chứng yếu hoặc khó sản xuất. Lý do ghi trong báo cáo |
| Kiểm chứng | IDEA là giả thuyết Content; đo sau khi đăng (Agent Content `track`). Không hứa lượt xem |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 0 | Đọc kho, liệt kê IDEA cũ (cặp Chủ đề + Góc), nguồn lực sản xuất | Kho | Bản ghi dùng được, danh sách cặp đã có | Có INS hoặc KEY/KH |
| 1 | Xác định mục tiêu Content theo hành trình | HT, OPP, yêu cầu | Mục tiêu từng nhóm khách | — |
| 2 | Xác định nhóm khách và nhu cầu | SEG, INS, KH | Nhóm khách × nhu cầu | — |
| 3 | Gom nhu cầu và từ khóa thành Content Pillar | KEY, KH, INS | 3–5 Pillar + lý do + mã nguồn | **DỪNG**: trình Pillar, người dùng duyệt/sửa trước khi tạo ý tưởng |
| 4 | Tạo chủ đề từ mỗi Pillar | KEY, KH câu hỏi, XH, MV | Kho chủ đề | Mỗi chủ đề có mã nguồn |
| 5 | Tạo 2–4 góc khai thác mỗi chủ đề | INS, KH rào cản/động lực | Kho góc | Mỗi góc gắn một yếu tố khác nhau |
| 6 | Ghép góc với Hook, thông điệp, format, CTA | FMT, CNT, TD | IDEA nháp | — |
| 7 | Triển khai theo nền tảng, ghi Tái định dạng, Series | KEY (nền tảng), CNT | IDEA nháp đủ trường | — |
| 8 | Kiểm trùng (Chủ đề + Góc, trong lô và kho), kiểm phù hợp nhóm khách, khả năng sản xuất; xếp mức ưu tiên | IDEA cũ, FMT, nguồn lực | Lô IDEA sạch | Không còn cặp trùng |
| 9 | Liên kết dữ liệu gốc; ghi kho `kho.py them lo-idea.json --dot RP-xxx`, `kho.py kiem-tra --dot RP-xxx` | Lô | IDEA-xxx | Không còn LỖI |
| 10 | Dựng báo cáo: `kho.py xuat --loai IDEA --ra <thư mục>/xuat` rồi trình bảng nhóm theo Content Pillar → Chủ đề → Góc → Hook, danh sách Series; `kho.py bao-cao --loai IDEA` cho truy vết | IDEA | Hệ thống Pillar, kho chủ đề, góc, Hook, series | **DỪNG** chờ duyệt; chọn ý tưởng chuyển sang Agent Content |

## F. Đầu ra — Kho ý tưởng Content (`IDEA`)
Trường bắt buộc: Nhóm khách hàng · Content Pillar · Chủ đề · Góc khai thác · Hook · Mục tiêu · Thông điệp · Format · Nền tảng · CTA · Mức ưu tiên.
Tuỳ chọn: Từ khóa · Series · Tái định dạng. `lien_ket` ≥ 1 INS/OPP/KEY/CNT/FIND (thêm FMT, TD). Tiêu đề bản ghi = "Chủ đề – Góc" để
kho tự chống trùng theo tiêu đề. Hệ thống Content Pillar, kho chủ đề, kho góc, kho Hook, series **dựng từ IDEA** (không tạo loại bản ghi riêng):
nhóm file CSV xuất theo cột `Content Pillar`, `Chủ đề`, `Góc khai thác`, `Hook`, `Series`.
Ví dụ lô kiểm thử (giả định, thời trang): `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/y-tuong-content.json`.

```json
{"loai": "IDEA", "tieu_de": "Chọn quần cho người thấp – Sai lầm khiến chân trông ngắn", "lien_ket": ["INS-001", "KEY-001", "FMT-001"],
 "du_lieu": {"Nhóm khách hàng": "Nữ văn phòng 25–32 tuổi, cao dưới 1m55", "Content Pillar": "Phối đồ công sở theo vóc dáng",
   "Chủ đề": "Chọn quần cho người thấp dưới 1m55", "Góc khai thác": "Sai lầm phổ biến khiến chân trông ngắn hơn",
   "Hook": "3 kiểu quần đang làm bạn thấp đi mà không biết", "Mục tiêu": "Thu hút", "Thông điệp": "Mặc đúng dáng thì không cần cao mới đẹp",
   "Format": "Video thử đồ trước–sau 30 giây", "Nền tảng": "TikTok, Instagram Reels", "CTA": "Lưu lại để đi mua không chọn sai",
   "Mức ưu tiên": "Cao", "Từ khóa": "quần cho người thấp", "Series": "Mặc đúng dáng", "Tái định dạng": "Carousel 5 trang cho Instagram"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| Kho `IDEA` (+ TH) | Agent Content: `content-agent:strategy` (Pillar), `content-agent:calendar` (chọn ý tưởng lên lịch), `content-agent:write` (bài, caption, kịch bản video); kịch bản video → plugin video-edit; thiết kế → `design-agent:design`; quảng cáo từ IDEA hiệu quả → `y-tuong-quang-cao` | Content Pillar, lịch Content, kịch bản, carousel | Hạn dùng 180 ngày; IDEA đã đăng ghi kết quả vào GT; lần sau kiểm trùng theo cặp Chủ đề + Góc trước khi tạo mới |

## H. Kiểm tra chất lượng
- [ ] Dùng đúng khái niệm Pillar / Chủ đề / Góc / Hook / Format / Ý tưởng; mỗi Pillar có nhu cầu và bằng chứng.
- [ ] Không có hai IDEA trùng cặp Chủ đề + Góc khai thác (trong lô và so với kho); không có ý tưởng chỉ khác tiêu đề hay Hook.
- [ ] Mỗi góc gắn một Insight, rào cản, động lực hoặc câu hỏi cụ thể; Hook khớp góc, không câu kéo sai sự thật.
- [ ] Mỗi IDEA liên kết ≥ 1 INS/KEY/CNT/OPP/FIND; số liệu trong Hook/thông điệp có nguồn.
- [ ] Ý tưởng vượt nguồn lực sản xuất đã hạ ưu tiên hoặc đổi format; không hứa lượt xem.
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi Pillar đã được duyệt, kho IDEA đã trình theo Pillar → Chủ đề → Góc và người dùng chọn ý tưởng chuyển sang Agent Content.
