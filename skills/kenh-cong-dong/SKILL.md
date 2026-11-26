---
name: kenh-cong-dong
description: Nghiên cứu kênh, cộng đồng và Creator nơi nhóm khách tìm kiếm, trao đổi, tham khảo — nền tảng khách dùng, hội nhóm, diễn đàn, Creator/KOL/KOC, kênh vệ tinh, website, sàn, điểm bán và phân phối; phân tích nội dung, nhóm người xem, chỉ số và chất lượng tương tác công khai (bình luận thực chất, dấu hiệu tương tác ảo); chấm mức phù hợp Cao / Trung bình / Thấp có lý do; phân vai Thu hút, Nuôi dưỡng, Xây dựng niềm tin, Chuyển đổi; ghi cách tiếp cận/hợp tác phù hợp quy định từng kênh và thông tin cần xác minh trước khi triển khai. Ghi vào kho KEN (Bản đồ kênh, Kho cộng đồng, Kho Creator, Kho kênh vệ tinh, Kho cơ hội hợp tác, Định hướng phân phối). Không liên hệ, nhắn tin, theo dõi hay tham gia nhóm thay người dùng. Dùng khi người dùng nói "tìm kênh tiếp cận khách", "khách hay ở hội nhóm nào", "tìm creator/KOC phù hợp", "nên booking ai", "bản đồ kênh", "phân phối content ở đâu", hoặc khi workflow 07 cần KEN.
argument-hint: "[nhóm khách hoặc ngành] [--bang creator|cong-dong|ban-do|...] [--dot RP-xxx]"
---

# /masterplan-agent:kenh-cong-dong

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`.
Cách làm theo nguồn: `${CLAUDE_PLUGIN_ROOT}/references/nen-tang/` — `facebook.md` (Page, Group), `tiktok.md`, `youtube.md`, `instagram.md`,
`threads.md`, `google-search.md` (diễn đàn, blog, website), `google-maps.md` (điểm bán), `san-tmdt.md`, `crm-noi-bo.md` (nguồn khách nội bộ).
Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`. Thư mục đợt: `nghien-cuu/<YYYY-MM-DD>-<chủ-đề>/`.

## A. Mục tiêu
Trả lời **khách ở đâu, làm gì ở từng điểm chạm và doanh nghiệp nên có mặt ở đâu với vai trò gì**: kênh nào để thu hút, nuôi dưỡng,
xây niềm tin, chuyển đổi; cộng đồng và Creator nào phù hợp; cần xác minh gì trước khi hợp tác. Phục vụ quyết định: phát triển hệ thống
kênh, phân phối Content, chọn Creator booking/UGC, tham gia hoặc xây cộng đồng, mở điểm bán/sàn.

## B. Điều kiện kích hoạt
- **Dùng khi**: cần mở rộng kênh, tìm cộng đồng/Creator, lập kế hoạch booking hoặc phân phối; workflow 07 (Phát triển kênh) hoặc 01 khi cần.
- **Không dùng khi**: đánh giá hiệu quả kênh của chính doanh nghiệp → `danh-gia-kenh` (skill này đọc lại kết quả đó, không làm lại);
  cần bóc nội dung từng bài → `nghien-cuu-content`; theo dõi kênh đối thủ định kỳ → `quet-doi-thu`.
- **Chạy độc lập** được nếu người dùng mô tả được nhóm khách; tốt hơn khi kho có SEG/HT (`customer-research`) và KEY (`tu-khoa`).

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Nhóm khách cần tiếp cận (mã SEG hoặc mô tả); mục tiêu kênh (thu hút, nuôi dưỡng, niềm tin, chuyển đổi); địa bàn; mã đợt RP |
| Tuỳ chọn | Bảng cần làm (một hoặc nhiều trong 6 bảng KEN); ngân sách hợp tác dự kiến (chỉ để lọc quy mô Creator); kênh/Creator người dùng đã biết |
| Dữ liệu nội bộ | Kết quả `danh-gia-kenh` (kênh nào của mình đang hiệu quả); nguồn khách trong CRM ("biết qua đâu"); kết quả `lead-hoi-thoai` |
| Kế thừa từ kho | `kho.py tim --loai SEG HT KEY CNT --chu "<nhóm khách>"`; `kho.py tim --loai KEN` (không tạo trùng, cập nhật chỉ số cũ) |
| Khi thiếu | Không có SEG/HT → hỏi người dùng khách thường biết đến doanh nghiệp qua đâu, ghi TH; nhóm riêng tư → chỉ ghi thông tin công khai (tên mô tả, số thành viên, quy định nhóm), không xin tham gia |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Nội dung | Nền tảng khách dùng · hội nhóm, cộng đồng, diễn đàn · Creator, KOL/KOC, kênh vệ tinh · website, sàn, điểm bán, phân phối · hành vi tại từng điểm chạm · chủ đề, định dạng, hoạt động phù hợp |
| Xây từ khóa | Từ KEY/KH: nhu cầu + "group", "hội", "review", "cộng đồng", tên địa bàn ("hội mẹ bỉm quận X", "review quán Hà Nội"); hashtag ngành; tên Creator xuất hiện lặp trong CNT |
| Chọn và thu mẫu | Phạm vi khởi tạo 10–20 cộng đồng và Creator, 5–10 kênh/điểm bán khác. Mỗi Creator xem ≥ 10 bài gần nhất (không chỉ bài nổi bật); mỗi cộng đồng đọc ≥ 20 bài gần nhất |
| Trích xuất | Chủ đề chính, format, nhóm người xem quan sát được (qua bình luận, không đoán nhân khẩu học), quy mô, mức hoạt động (bài/tuần), chỉ số công khai có ngày đọc, quy định nhóm/kênh về quảng cáo |
| Chất lượng tương tác | Tỷ lệ bình luận thực chất = bình luận có nội dung liên quan / tổng bình luận đã đọc (ghi số). Dấu hiệu tương tác ảo: lượt xem cao bất thường so với bình luận, bình luận chung chung lặp lại, tài khoản trống, tăng người theo dõi đột biến. Ghi dấu hiệu, không kết luận gian lận |
| Mức phù hợp | Chấm **Cao / Trung bình / Thấp** theo 4 tiêu chí: (1) người xem trùng nhóm khách, (2) chủ đề gần nhu cầu, (3) chất lượng tương tác, (4) giọng điệu hợp thương hiệu. Cao = đạt cả 4; Trung bình = 2–3; Thấp = ≤ 1. Ghi lý do theo tiêu chí, không dùng điểm số giả |
| Phân vai | Thu hút (tiếp cận người chưa biết) · Nuôi dưỡng (nội dung lặp lại, theo dõi) · Xây dựng niềm tin (review, hỏi đáp, cộng đồng) · Chuyển đổi (sàn, điểm bán, inbox, landing page) |
| Cách tiếp cận | Theo quy định từng kênh: nhóm cấm quảng cáo → chỉ chia sẻ kiến thức với tư cách thành viên do người dùng tự làm; Creator → ghi kênh liên hệ công khai (mục "liên hệ hợp tác"), không ghi email/số điện thoại vào kho |
| Kiểm chứng | Đối chiếu kênh khách nói (KH, CRM "biết qua đâu") với kênh quan sát công khai; giá booking, nhân khẩu học người xem, tỷ lệ chuyển đổi ghi vào `Cần xác minh` — chỉ hỏi trực tiếp Creator, không đoán |
| Mâu thuẫn | Khách nói dùng kênh A nhưng công khai thấy hoạt động ở B → ghi MT, giữ cả hai |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 1 | Xác định chân dung khách cần tiếp cận từ SEG/HT | SEG, HT, KH | Mô tả nhóm khách + điểm chạm đã biết | Người dùng xác nhận nhóm khách |
| 2 | Tìm nơi khách tìm kiếm, trao đổi, tham khảo | KEY, KH, CRM, tìm kiếm | Danh sách loại nơi (nền tảng, nhóm, diễn đàn, sàn, điểm bán) | Mỗi loại có ≥ 1 bằng chứng |
| 3 | Lập danh sách nền tảng, kênh, cộng đồng, Creator | Tìm kiếm, CNT | Danh sách ứng viên + MAU | **DỪNG** trình danh sách, chờ duyệt phạm vi |
| 4 | Phân tích nội dung, nhóm người xem, chỉ số, chất lượng tương tác | Bài gần nhất, bình luận | EVD + chỉ số có ngày đọc | Mỗi ứng viên có tỷ lệ bình luận thực chất |
| 5 | Chấm mức phù hợp theo 4 tiêu chí | Bước 4 | Mức + lý do | Mọi ứng viên có lý do |
| 6 | Phân vai Thu hút / Nuôi dưỡng / Xây dựng niềm tin / Chuyển đổi | Bước 5, `danh-gia-kenh` | Bản đồ kênh | Mỗi vai trò có ≥ 1 kênh hoặc ghi khoảng trống |
| 7 | Ghi cách tiếp cận/hợp tác phù hợp quy định từng kênh | Quy định nhóm/nền tảng | Kho cơ hội hợp tác, Định hướng phân phối | — |
| 8 | Liệt kê thông tin cần xác minh; ghi kho `kho.py them lo-ken.json --dot RP-xxx` → `kiem-tra` | KEN | KEN (+ TH, MT) | Không LỖI; **DỪNG** trình bản đồ kênh chờ duyệt |

## F. Đầu ra — Kho Kênh, cộng đồng, Creator (`KEN`)
Trường bắt buộc: Bảng · Tên · Nhóm khách hàng · Vai trò · Mức độ phù hợp · Nguồn. `Bảng` ∈ Bản đồ kênh / Kho cộng đồng / Kho Creator /
Kho kênh vệ tinh / Kho cơ hội hợp tác / Định hướng phân phối; `Vai trò` ∈ Thu hút / Nuôi dưỡng / Xây dựng niềm tin / Chuyển đổi.
Tuỳ chọn: URL · Chủ đề · Lĩnh vực · Format · Quy mô · Mức độ hoạt động · Quy định · Chỉ số công khai · Hành vi · Hình thức hợp tác · Điều kiện ·
Cách tiếp cận · Cần xác minh. `Mức độ phù hợp` ghi "Cao/Trung bình/Thấp — lý do theo 4 tiêu chí". `Tên` là mô tả ("Creator review quán
~120k theo dõi"), tên thật chỉ ở URL. KEN liên kết EVD để truy được bằng chứng. Ví dụ kiểm thử: `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/kenh-cong-dong.json`.

Ví dụ bản ghi (giả định):
```json
{"tam": "k1", "loai": "KEN", "tieu_de": "Creator review quán ngồi làm việc Hà Nội", "lien_ket": ["@e1"],
 "do_tin_cay": "Trung bình", "ly_do_tin_cay": "Đã xem 12 bài gần nhất và 180 bình luận; chưa có số nhân khẩu học người xem",
 "du_lieu": {"Bảng": "Kho Creator", "Tên": "Creator review quán ngồi làm việc ~120k theo dõi (ví dụ)", "URL": "https://www.tiktok.com/@vidu-review-quan",
   "Nhóm khách hàng": "Sinh viên, freelancer tìm quán ngồi lâu", "Vai trò": "Thu hút", "Lĩnh vực": "F&B", "Chủ đề": "Quán yên tĩnh, có ổ cắm, wifi",
   "Format": "Video POV 30–45 giây", "Quy mô": "~120k theo dõi (26/11/2026)", "Mức độ hoạt động": "4–5 video/tuần",
   "Chỉ số công khai": "Trung vị 12 video gần nhất: 35k xem, 140 bình luận", "Hành vi": "Người xem hỏi địa chỉ, giờ mở cửa, có ồn không",
   "Mức độ phù hợp": "Cao — người xem trùng nhóm khách; chủ đề đúng nhu cầu ngồi lâu; 62% bình luận thực chất; giọng nhẹ nhàng hợp thương hiệu",
   "Hình thức hợp tác": "Booking review hoặc gửi trải nghiệm", "Cách tiếp cận": "Người dùng tự liên hệ qua mục liên hệ hợp tác trên hồ sơ",
   "Cần xác minh": "Giá booking, tỷ lệ người xem tại Hà Nội, điều kiện quyền sử dụng video", "Nguồn": "TikTok, hồ sơ công khai"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| `KEN` (6 bảng), EVD, MAU; TH/MT nếu có | `dinh-huong-chien-luoc` (hệ thống kênh), `y-tuong-chien-dich` (hoạt động hợp tác, vai trò kênh), `y-tuong-content` (phân phối Content theo kênh), plugin content-agent (lịch phân phối); `danh-gia-kenh` dùng lại để đo kênh của mình sau triển khai | Phát triển hệ thống kênh, phân phối Content, Booking, UGC, cộng đồng, hợp tác Creator | Hạn dùng 90 ngày (chỉ số Creator đổi nhanh); xuất từng bảng: `kho.py xuat --loai KEN --ra nghien-cuu/<đợt>/xuat` rồi lọc cột `Bảng`; lần sau cập nhật chỉ số bằng `kho.py cap-nhat KEN-xxx` |

## H. Kiểm tra chất lượng
- [ ] Không liên hệ, nhắn tin, theo dõi, bình luận, xin tham gia nhóm thay người dùng; không lưu email/số điện thoại Creator vào kho.
- [ ] Mỗi KEN có mức phù hợp kèm lý do theo 4 tiêu chí; không có điểm số tự chế.
- [ ] Chỉ số công khai có ngày đọc; tỷ lệ bình luận thực chất có số đã đọc; dấu hiệu tương tác ảo ghi là dấu hiệu, không kết luận.
- [ ] Giá booking, nhân khẩu học người xem, tỷ lệ chuyển đổi nằm ở `Cần xác minh`, không đoán.
- [ ] Bản đồ kênh có đủ 4 vai trò hoặc ghi rõ vai trò còn trống; đã đối chiếu `danh-gia-kenh` cho kênh của mình.
- [ ] Mỗi KEN liên kết ≥ 1 EVD; MAU cho mỗi nền tảng.
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi các bảng KEN được yêu cầu ở trạng thái Chờ duyệt, người dùng có bản đồ kênh theo vai trò và danh sách việc cần xác minh trước khi liên hệ.
