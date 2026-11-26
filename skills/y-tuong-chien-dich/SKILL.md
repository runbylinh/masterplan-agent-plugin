---
name: y-tuong-chien-dich
description: Phát triển ý tưởng chiến dịch Marketing từ kho nghiên cứu — kết hợp mục tiêu kinh doanh và nguồn lực (DN), xu hướng và mùa vụ (XH, MV), Insight (INS), cơ hội đã chọn (OPP), sản phẩm và ưu đãi (OFFER), kênh (KEN) để xác định cơ hội và thời điểm, nhóm khách, vấn đề/nhu cầu/động lực cần tác động, ý tưởng chủ đạo và thông điệp, sản phẩm và ưu đãi, hoạt động thu hút, tương tác, nuôi dưỡng, chuyển đổi, vai trò từng kênh, điều kiện triển khai và cơ chế tạo kết quả; so sánh 2–3 phương án, đề xuất hướng ưu tiên và chỉ số kiểm chứng. Đầu ra kho CAM. Không dừng ở đặt tên và liệt kê hoạt động phổ biến. Dùng khi người dùng gõ /masterplan-agent:y-tuong-chien-dich, nói "ý tưởng chiến dịch", "chiến dịch Tết", "big idea", "campaign cho dịp X", "chiến dịch ra mắt sản phẩm", "so sánh phương án chiến dịch".
argument-hint: "[dịp hoặc OPP-xxx] [mục tiêu] [--dot RP-xxx]"
---

# /masterplan-agent:y-tuong-chien-dich

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`.
Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`. Skill này **không thu thập lại dữ liệu**, không đặt ngân sách hay KPI chính thức.

## A. Mục tiêu
Chuyển cơ hội và Insight đã có bằng chứng thành **ý tưởng chiến dịch có cơ chế tạo kết quả**: vì sao chiến dịch này khiến đúng nhóm khách
hành động, mỗi hoạt động và mỗi kênh đóng vai trò gì, cần điều kiện gì để chạy. Phục vụ quyết định: chọn hướng chiến dịch cho một dịp/mục tiêu
trước khi lập kế hoạch chi tiết, ngân sách, KPI.

## B. Điều kiện kích hoạt
- **Dùng khi**: kho có ≥ 1 OPP (ưu tiên OPP người dùng đã chọn) và INS; workflow 02; người dùng hỏi chiến dịch cho dịp, mục tiêu, ra mắt.
- **Không dùng khi**: chưa có cơ hội → `marketing-opportunities`; cần lịch Content chi tiết → `content-agent:calendar`; cần kế hoạch ngân sách,
  KPI, phân công → bước lập Masterplan (sau skill này); chỉ cần một ý tưởng quảng cáo → `y-tuong-quang-cao`.
- **Chạy độc lập** được (tự tạo RP mức Nhanh) nhưng thiếu OPP thì chỉ ra phương án nháp mức tin cậy Thấp.

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Dịp hoặc mục tiêu chiến dịch; mục tiêu kinh doanh (DN Mục tiêu hoặc người dùng nói); mã đợt RP; ≥ 1 OPP hoặc INS |
| Tuỳ chọn | Khung thời gian; nguồn lực (nhân sự, thời gian chuẩn bị, ngân sách người dùng đặt); kênh đang có; đối tác khả dĩ |
| Dữ liệu nội bộ | Doanh thu cùng kỳ năm trước theo sản phẩm (`bao-cao-kinh-doanh`), chi phí và kết quả quảng cáo dịp trước (`chi-phi-ads`), lead và tỷ lệ chốt (`lead-hoi-thoai`), hiệu quả kênh (`danh-gia-kenh`) |
| Kế thừa từ kho | `kho.py tim --loai OPP INS --chu "<dịp>"` · `--loai XH MV BD` · `--loai DN` (Mục tiêu, Nguồn lực, Giới hạn triển khai) · `--loai OFFER TD` · `--loai KEN` · `--loai IDEA ADS` · `--loai CAM` (tránh trùng) |
| Khi thiếu | Thiếu MV/XH → không khẳng định thời điểm, ghi TH, đề xuất `xu-huong-mua-vu`. Thiếu OFFER → `Ưu đãi` = "chưa xác định – cần `san-pham-uu-dai`". Thiếu KEN → vai trò kênh chỉ dùng kênh doanh nghiệp đang có, đề xuất `kenh-cong-dong`. Thiếu nguồn lực → hỏi người dùng, không tự đặt ngân sách |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Cơ hội và thời điểm | Mỗi phương án dựa trên ≥ 1 OPP; thời điểm từ MV (`Thời gian chuẩn bị`) và XH; tính ngược mốc chuẩn bị từ ngày cao điểm. Không còn đủ thời gian chuẩn bị → ghi Rủi ro |
| Nhóm khách và yếu tố tác động | Một nhóm khách chính (SEG/INS) và **một** vấn đề/nhu cầu/động lực trung tâm; chiến dịch thay đổi hành vi nào của khách (tìm hiểu, thử, mua, mua lại, giới thiệu) |
| Ý tưởng chủ đạo | Một câu nối Insight với hành động mong muốn: *Vì [nhóm khách] [mâu thuẫn trong INS], chiến dịch [cơ chế] để họ [hành động]*. Không chỉ là tên hay khẩu hiệu. Thông điệp lấy từ TD khi có |
| Sản phẩm và ưu đãi | Từ OFFER/DN; ưu đãi phải gỡ đúng rào cản của INS; không tự đặt giảm giá khi chưa có biên lợi nhuận |
| Hoạt động theo phễu | Thu hút → Tương tác → Nuôi dưỡng → Chuyển đổi (+ Hợp tác nếu có). **Mỗi hoạt động ghi kèm lý do** sau dấu "–": nó phục vụ yếu tố tác động nào, liên kết IDEA/ADS/KEN nào. Hoạt động phổ biến (minigame, livestream, giảm giá) chỉ giữ khi giải thích được cơ chế với nhóm khách này |
| Vai trò kênh | Gán vai trò Thu hút / Nuôi dưỡng / Xây dựng niềm tin / Chuyển đổi cho từng kênh theo KEN hoặc dữ liệu `danh-gia-kenh`; kênh không có vai trò rõ thì bỏ |
| Cơ chế tạo kết quả | Chuỗi nhân quả giả định: *hoạt động → thay đổi nhận thức/hành vi → chỉ số trung gian → kết quả kinh doanh*. Ghi rõ là giả định cần kiểm chứng |
| Điều kiện triển khai | Nguồn lực sơ bộ (người, thời gian chuẩn bị, sản phẩm/tồn kho, ngân sách thử do người dùng đặt), điều kiện tiên quyết (bằng chứng cần có, đối tác cần xác nhận) |
| So sánh phương án | 2–3 phương án khác nhau về ý tưởng chủ đạo hoặc nhóm khách (không chỉ khác tên). Bảng so sánh: Cơ hội · Nhóm khách · Cơ chế · Độ mạnh bằng chứng · Khả thi · Rủi ro · Kết luận (Cao/Trung bình/Thấp có lý do, không điểm số) |
| Chỉ số kiểm chứng | Chỉ số trung gian (lượt hỏi, đăng ký, đặt trước) và kết quả (đơn, doanh thu từ sản phẩm chiến dịch); mốc so sánh cùng kỳ nếu có dữ liệu nội bộ; không đặt KPI chính thức |
| Mâu thuẫn | Mục tiêu kinh doanh vượt nguồn lực → nêu rõ, đề xuất thu hẹp phạm vi; không tự hạ mục tiêu |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 0 | Đọc kho, CAM cũ, kiểm tra OPP đã chọn và nguồn lực | Kho | Bản ghi dùng được, TH | Có OPP/INS và mục tiêu kinh doanh |
| 1 | Xác định cơ hội và thời điểm, tính mốc chuẩn bị | OPP, MV, XH, BD | Khung thời gian + cơ hội | Còn đủ thời gian chuẩn bị hoặc đã ghi rủi ro |
| 2 | Xác định nhóm khách | SEG, INS | Nhóm khách chính | — |
| 3 | Chọn vấn đề/nhu cầu/động lực tác động và hành vi muốn đổi | INS, KH | Yếu tố trung tâm | Có bằng chứng |
| 4 | Viết ý tưởng chủ đạo và thông điệp (2–3 phương án) | INS, TD | Ý tưởng chủ đạo mỗi phương án | Các phương án khác nhau về bản chất |
| 5 | Chọn sản phẩm và ưu đãi | OFFER, DN | Sản phẩm, ưu đãi | Ưu đãi gỡ đúng rào cản hoặc ghi "cần xác nhận" |
| 6 | Thiết kế hoạt động thu hút, tương tác | IDEA, ADS, KEN | Hoạt động + lý do | Mỗi hoạt động có lý do |
| 7 | Thiết kế nuôi dưỡng và chuyển đổi | HT, CRO, TD | Hoạt động + lý do | — |
| 8 | Gán vai trò từng kênh | KEN, `danh-gia-kenh` | Vai trò kênh | — |
| 9 | Điều kiện triển khai, cơ chế tạo kết quả, rủi ro | DN nguồn lực | CAM nháp đủ trường | — |
| 10 | So sánh 2–3 phương án, đề xuất hướng ưu tiên và chỉ số kiểm chứng; ghi kho `kho.py them lo-cam.json --dot RP-xxx`, `kho.py kiem-tra --dot RP-xxx`, `kho.py truy-vet CAM-xxx` | CAM | CAM-xxx + bảng so sánh | **DỪNG**: người dùng chọn phương án; không tự lập kế hoạch chi tiết |

## F. Đầu ra — Kho ý tưởng chiến dịch (`CAM`)
Trường bắt buộc: Tên chiến dịch · Bối cảnh · Cơ hội khai thác · Mục tiêu · Nhóm khách hàng · Ý tưởng chủ đạo · Thông điệp · Sản phẩm · Ưu đãi ·
Hoạt động thu hút · Hoạt động tương tác · Hoạt động nuôi dưỡng · Hoạt động chuyển đổi · Vai trò từng kênh · Cơ chế tạo kết quả · Nguồn lực sơ bộ ·
Rủi ro · Chỉ số kiểm chứng. Tuỳ chọn: Hoạt động hợp tác · Thời điểm. `lien_ket` ≥ 1 OPP/INS (thêm OFFER, KEN, IDEA, ADS, MV).
Mỗi phương án là một CAM; bảng so sánh và đề xuất ưu tiên viết trong `bao-cao.md` (`kho.py bao-cao --dot RP-xxx --loai CAM`).
Ví dụ lô kiểm thử (giả định, F&B dịp Tết, 2 phương án): `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/y-tuong-chien-dich.json`.

```json
{"loai": "CAM", "tieu_de": "Phương án A – Tết đủ đầy cho văn phòng", "lien_ket": ["OPP-001", "INS-001", "OFFER-001", "KEN-001"],
 "du_lieu": {"Tên chiến dịch": "Tết đủ đầy cho văn phòng (tên tạm)", "Bối cảnh": "Văn phòng đặt quà Tết cho nhân viên, cao điểm 3 tuần trước Tết (MV-001)",
   "Cơ hội khai thác": "OPP-001 – hộp quà giao đúng ngày cho văn phòng", "Mục tiêu": "Tăng đơn văn phòng so với Tết trước (cần số cùng kỳ)",
   "Nhóm khách hàng": "Nhân sự hành chính văn phòng 20–100 người", "Ý tưởng chủ đạo": "Vì người lo quà Tết sợ giao trễ và phải gọi nhiều nơi, chiến dịch biến việc đặt quà thành một lần chốt có lịch giao cố định",
   "Thông điệp": "Chốt một lần, quà đến đúng ngày", "Sản phẩm": "Hộp quà Tết 3 mức", "Ưu đãi": "In thiệp tên công ty miễn phí từ 20 hộp (OFFER-001, cần xác nhận chi phí)",
   "Hoạt động thu hút": "Bài LinkedIn và nhóm hành chính nhân sự về lịch đặt quà – tiếp cận đúng người quyết định (KEN-001)",
   "Hoạt động tương tác": "Bảng tính số hộp theo số nhân viên – giải câu hỏi 'đặt bao nhiêu'", "Hoạt động nuôi dưỡng": "Gửi mẫu thử cho văn phòng quen – xử lý lo ngại chất lượng",
   "Hoạt động chuyển đổi": "Báo giá trong 2 giờ, chọn lịch giao khi đặt cọc – xử lý rào cản giao trễ", "Vai trò từng kênh": "Nhóm cộng đồng thu hút, Zalo OA nuôi dưỡng, Sales chuyển đổi",
   "Cơ chế tạo kết quả": "Giảm lo giao trễ → chốt sớm hơn → đơn dồn về trước cao điểm → bếp chủ động công suất", "Nguồn lực sơ bộ": "1 Sales B2B, 1 điều phối giao; ngân sách thử do người dùng đặt",
   "Rủi ro": "Quá tải bếp tuần cuối; chưa có biên lợi nhuận theo hộp", "Chỉ số kiểm chứng": "Số yêu cầu báo giá, tỷ lệ báo giá → đặt cọc, số hộp đặt trước ngày 20 tháng Chạp",
   "Thời điểm": "Mở đặt từ 15/12, chốt trước 20 tháng Chạp"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| Kho `CAM` (+ GT cho cơ chế tạo kết quả, TH) | Lập kế hoạch chiến dịch, ngân sách, KPI (bước lập Masterplan sau `dinh-huong-chien-luoc`); `marketing-recommendations` (đưa vào kế hoạch đang chạy); Agent Content (`content-agent:strategy`, `content-agent:calendar`); `y-tuong-content`, `y-tuong-quang-cao` cho hoạt động còn thiếu ý tưởng | Kế hoạch chiến dịch, lịch Content, brief quảng cáo | Hạn dùng 180 ngày; sau chiến dịch ghi kết quả vào GT; dịp năm sau đọc CAM cũ + kết quả trước khi tạo mới |

## H. Kiểm tra chất lượng
- [ ] Có 2–3 phương án khác nhau về ý tưởng chủ đạo hoặc nhóm khách, có bảng so sánh và đề xuất ưu tiên có lý do (không điểm số).
- [ ] Ý tưởng chủ đạo nối được Insight với hành vi muốn đổi; không chỉ là tên hoặc khẩu hiệu.
- [ ] Mỗi hoạt động có lý do và liên kết mục tiêu, nhóm khách hoặc cơ hội; không liệt kê hoạt động phổ biến không có cơ chế.
- [ ] Mỗi kênh có vai trò; ưu đãi không tự đặt giảm giá; nguồn lực, ngân sách không tự đặt.
- [ ] Cơ chế tạo kết quả ghi là giả định, có chỉ số kiểm chứng trung gian và kết quả.
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI; `kho.py truy-vet` mỗi CAM về tới bằng chứng gốc.
**Hoàn thành** khi các phương án CAM đã trình kèm bảng so sánh và người dùng chọn hướng để lập kế hoạch chi tiết.
