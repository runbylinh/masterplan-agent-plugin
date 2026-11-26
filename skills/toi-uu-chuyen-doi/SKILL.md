---
name: toi-uu-chuyen-doi
description: Phát triển định hướng tối ưu chuyển đổi từ kho nghiên cứu và dữ liệu nội bộ — đọc hành trình khách (HT), câu hỏi và rào cản (KH), dữ liệu lead và hội thoại (lead-hoi-thoai), dữ liệu quảng cáo (chi-phi-ads), landing page và bản đồ chuyển đổi (LP), dữ liệu Sales để xác định điểm chuyển đổi từ tiếp cận đến mua, số lượng và tỷ lệ thực tế nếu có, điểm nghẽn quan sát được, giả thuyết nguyên nhân, đề xuất thay đổi nội dung, thông điệp, bằng chứng, ưu đãi, CTA, trải nghiệm, thử nghiệm và mức ưu tiên. Đầu ra kho CRO (Bản đồ điểm nghẽn, Kho FAQ, Kho xử lý từ chối, Định hướng landing page, Định hướng Sales, Định hướng CRM, Kho thử nghiệm), phân biệt căn cứ đo được và giả thuyết định tính. Dùng khi người dùng gõ /masterplan-agent:toi-uu-chuyen-doi, nói "tối ưu chuyển đổi", "vì sao khách chưa mua", "tối ưu landing page", "nhiều lead mà ít chốt", "FAQ", "xử lý từ chối", "kịch bản tư vấn", "CRO".
argument-hint: "[sản phẩm, trang hoặc kênh] [--dot RP-xxx]"
---

# /masterplan-agent:toi-uu-chuyen-doi

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`,
`${CLAUDE_PLUGIN_ROOT}/references/lead-hoi-thoai.md` (khi dùng dữ liệu hội thoại). Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`.
Skill này **không thu thập lại dữ liệu** và **không sửa landing page, quảng cáo, CRM**.

## A. Mục tiêu
Tìm **nơi khách rơi khỏi hành trình mua và vì sao**, rồi đề xuất thay đổi thử nghiệm được cho landing page, Sales, CRM. Phục vụ quyết định:
sửa gì trước trên trang và trong kịch bản tư vấn, FAQ và câu xử lý từ chối nào cần chuẩn bị, thử nghiệm nào chạy trước.

## B. Điều kiện kích hoạt
- **Dùng khi**: có dữ liệu chuyển đổi nội bộ (lead, hội thoại, đơn, số quảng cáo) hoặc kho có HT/KH câu hỏi, rào cản/LP; workflow 06; người dùng hỏi
  "vì sao chưa mua", "nhiều lead ít chốt", "tối ưu landing page".
- **Không dùng khi**: chưa có cả dữ liệu nội bộ lẫn dữ liệu khách → `customer-research` (hành trình, rào cản) và `lead-hoi-thoai`; cần đọc landing
  page đối thủ → `quang-cao-chuyen-doi`; cần dựng trang → `design-agent:landing` sau skill này.
- **Chạy độc lập** được (tự tạo RP mức Nhanh). Không có dữ liệu đo được thì chỉ ra giả thuyết điểm nghẽn, nói rõ với người dùng.

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Sản phẩm/trang/kênh cần tối ưu; mã đợt RP; ≥ 1 nguồn: dữ liệu chuyển đổi nội bộ HOẶC KH (Câu hỏi, Rào cản) / HT |
| Tuỳ chọn | Mục tiêu chuyển đổi (đặt lịch, để lại thông tin, mua); kịch bản tư vấn hiện tại; giới hạn sửa trang |
| Dữ liệu nội bộ | `lead-hoi-thoai/*/chi-so-lead.json` (số hội thoại, chất lượng lead, tỷ lệ chốt, lý do không chốt, câu hỏi hay gặp); `chi-phi-ads/*/chi-so-chi-phi.json` (lượt nhấp, chi phí mỗi kết quả); số liệu landing page qua connector LadiPage (chỉ đọc); file CRM/đơn đã ẩn danh trong `nhap/` |
| Kế thừa từ kho | `kho.py tim --loai HT KH SEG --chu "<sản phẩm>"` (giai đoạn, câu hỏi, rào cản) · `--loai LP QC` · `--loai INS OPP TD OFFER` · `--loai CRO` (tránh trùng) |
| Khi thiếu | Không có dữ liệu chuyển đổi → mọi CRO `Loại căn cứ` = "Định tính – giả thuyết điểm nghẽn", ghi TH "cần số lượt xem trang, số lead, số đơn theo bước", đề xuất `lead-hoi-thoai`, `chi-phi-ads`. Thiếu HT → dựng bản đồ điểm chạm từ LP và KH, ghi giới hạn |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Điểm chuyển đổi | Liệt kê bước từ tiếp cận đến mua theo kênh thực tế: xem quảng cáo/bài → nhấp → xem trang → để lại thông tin/nhắn tin → được tư vấn → báo giá/đặt lịch → mua → mua lại. Nguồn: HT, LP Bản đồ chuyển đổi, cấu hình kênh |
| Số lượng và tỷ lệ | Chỉ dùng số đọc được, kèm nguồn, kỳ, đơn vị. Tỷ lệ bước = số bước sau / số bước trước cùng kỳ, cùng kênh. Không ghép số khác kỳ hay khác kênh; không tự ước lượng bước thiếu |
| Điểm nghẽn | **Đo được**: bước có tỷ lệ giảm mạnh so với các bước khác hoặc so với kỳ trước (ghi cả hai số). **Quan sát định tính**: câu hỏi, rào cản lặp ở một giai đoạn (KH, HT, lý do không chốt). Luôn ghi `Loại căn cứ` |
| Đối chiếu câu hỏi, rào cản | Đặt mỗi điểm nghẽn cạnh KH nhãn Câu hỏi/Rào cản và lý do không chốt cùng giai đoạn; kiểm trang/kịch bản hiện tại đã trả lời chưa (LP Section, Thông điệp) |
| Giả thuyết nguyên nhân | Câu: *Khách rời ở [bước] vì [nguyên nhân], căn cứ [mã]*. Mỗi điểm nghẽn có thể nhiều giả thuyết; không chọn một khi chưa thử |
| Đề xuất thay đổi | Theo 6 nhóm: nội dung, thông điệp, bằng chứng, ưu đãi, CTA, trải nghiệm (tốc độ, form, số bước, kênh liên hệ). Bằng chứng lấy từ TD Kho bằng chứng/DN; ưu đãi từ OFFER, không tự đặt giảm giá |
| Kho FAQ | Mỗi câu hỏi lặp (KH Câu hỏi, câu hỏi hay gặp trong hội thoại): câu trả lời ngắn, bằng chứng, nơi đặt (trang, kịch bản, tin nhắn tự động) |
| Kho xử lý từ chối | Mỗi lý do từ chối: điều khách thực sự lo (từ INS/KH), cách trả lời, bằng chứng, bước tiếp theo đề nghị. Không gây áp lực, không hứa điều không làm được |
| Định hướng landing page, Sales, CRM | Landing page: thứ tự section, thông điệp, bằng chứng, CTA. Sales: kịch bản theo giai đoạn, câu hỏi khai thác nhu cầu, thời gian phản hồi. CRM: nhãn lead, chuỗi chăm sóc, thời điểm nhắc |
| Thử nghiệm | Mỗi thay đổi lớn có thử nghiệm: biến thể, chỉ số, điều kiện đánh giá (số lượt tối thiểu, thời gian). Một lần đổi một yếu tố chính |
| Ưu tiên | **Tác động tiềm năng** (bước nghẽn càng gần mua và càng nhiều khách đi qua → cao) × **khả năng làm** (sửa chữ, thêm FAQ → cao; đổi quy trình, công nghệ → thấp). Mức Cao/Trung bình/Thấp kèm lý do, không điểm số |
| Cấm | Khẳng định điểm nghẽn thực tế khi chỉ có dữ liệu công khai/định tính (ghi "giả thuyết điểm nghẽn"); lưu thông tin cá nhân hay nguyên văn hội thoại |
| Mâu thuẫn | Số đo được trái với phản hồi định tính → ghi MT, ưu tiên thử nghiệm phân định |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 0 | Đọc kho và dữ liệu nội bộ, CRO cũ; xác định có số chuyển đổi hay không | Kho, `lead-hoi-thoai/`, `chi-phi-ads/`, connector | Danh sách nguồn + loại căn cứ khả dụng | Có ≥ 1 nguồn; báo người dùng nếu chỉ có định tính |
| 1 | Xác định điểm chuyển đổi từ tiếp cận đến mua | HT, LP | Bản đồ bước theo kênh | — |
| 2 | Ghi số lượng và tỷ lệ thực tế nếu có | Dữ liệu nội bộ | Tỷ lệ từng bước + nguồn, kỳ | Số cùng kỳ, cùng kênh |
| 3 | Xác định điểm nghẽn quan sát được | Bước 2, KH, HT | CRO "Bản đồ điểm nghẽn" (Loại căn cứ) | — |
| 4 | Đối chiếu câu hỏi, rào cản cùng giai đoạn | KH, lý do không chốt, LP | Câu hỏi/rào cản chưa được trả lời | — |
| 5 | Viết giả thuyết nguyên nhân | Bước 3–4 | `Nguyên nhân giả định` | Mỗi giả thuyết có mã căn cứ |
| 6 | Đề xuất thay đổi nội dung, thông điệp, bằng chứng, ưu đãi, CTA, trải nghiệm | TD, OFFER, DN | CRO Kho FAQ, Kho xử lý từ chối, Định hướng landing page/Sales/CRM | — |
| 7 | Chuyển thay đổi lớn thành thử nghiệm | CRO | CRO "Kho thử nghiệm" (+ GT) | Có chỉ số, điều kiện đánh giá |
| 8 | Xếp ưu tiên theo tác động × khả năng làm; ghi kho `kho.py them lo-cro.json --dot RP-xxx`, `kho.py kiem-tra --dot RP-xxx` | Lô | CRO-xxx | Không còn LỖI |
| 9 | Trình theo 7 bảng, nêu rõ phần nào đo được, phần nào là giả thuyết | CRO | — | **DỪNG** chờ duyệt; agent không sửa trang, quảng cáo, CRM |

## F. Đầu ra — Tối ưu chuyển đổi (`CRO`)
Trường bắt buộc: Bảng · Giai đoạn · Vấn đề · Đề xuất · Căn cứ. `Bảng` thuộc 7 giá trị: **Bản đồ điểm nghẽn · Kho FAQ · Kho xử lý từ chối ·
Định hướng landing page · Định hướng Sales · Định hướng CRM · Kho thử nghiệm**. Tuỳ chọn: Nhóm khách · Dữ liệu · Nguyên nhân giả định · Chỉ số ·
Điều kiện đánh giá · Mức ưu tiên · **Loại căn cứ** = "Đo được (dữ liệu chuyển đổi)" hoặc "Định tính – giả thuyết điểm nghẽn" (bắt buộc ghi
trong skill này). `lien_ket` ≥ 1 INS/OPP/KH/LP/HT (thêm EVD nội bộ, TD, OFFER). Báo cáo: `kho.py bao-cao --dot RP-xxx --loai CRO`.
Ví dụ lô kiểm thử (giả định, dịch vụ đào tạo, có cả dữ liệu đo được và định tính): `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/toi-uu-chuyen-doi.json`.

```json
{"loai": "CRO", "tieu_de": "Lead đăng ký học thử nhưng không đến buổi học thử", "lien_ket": ["EVD-001", "HT-001", "KH-002"],
 "do_tin_cay": "Cao", "ly_do_tin_cay": "Số đo từ CRM nội bộ 60 ngày, cùng kênh, đủ lớn",
 "du_lieu": {"Bảng": "Bản đồ điểm nghẽn", "Giai đoạn": "Đăng ký học thử → Tham dự", "Vấn đề": "Tỷ lệ tham dự học thử thấp nhất trong các bước",
   "Đề xuất": "Nhắc lịch 2 lần (trước 1 ngày, trước 1 giờ), gửi trước nội dung buổi thử và link tham gia", "Căn cứ": "EVD-001: CRM 60 ngày; KH-002 câu hỏi về lịch",
   "Dữ liệu": "120 đăng ký → 42 tham dự (35%); các bước khác ≥ 55%", "Nguyên nhân giả định": "Quên lịch; chưa rõ buổi thử học gì",
   "Chỉ số": "Tỷ lệ tham dự học thử", "Điều kiện đánh giá": "So 2 tuần trước/sau, ≥ 60 đăng ký mỗi giai đoạn", "Mức ưu tiên": "Cao",
   "Loại căn cứ": "Đo được (dữ liệu chuyển đổi)"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| Kho `CRO` (+ GT thử nghiệm, TH số liệu cần đo) | Landing page: `design-agent:landing` (Định hướng landing page, Kho FAQ); Sales: kịch bản tư vấn (Định hướng Sales, Kho xử lý từ chối); CRM: nhãn, chuỗi chăm sóc (Định hướng CRM); `y-tuong-quang-cao` (đồng bộ thông điệp với điểm đến); `marketing-recommendations` (đưa vào kế hoạch đang chạy) | Sửa trang, kịch bản tư vấn, FAQ, chăm sóc lead | Hạn dùng 180 ngày; sau thử nghiệm ghi kết quả vào GT; chạy lại `lead-hoi-thoai`, `chi-phi-ads` cùng kỳ để đo trước–sau |

## H. Kiểm tra chất lượng
- [ ] Mỗi CRO ghi `Loại căn cứ`; điểm nghẽn "Đo được" có số, nguồn, kỳ, cùng kênh; điểm nghẽn định tính ghi là giả thuyết.
- [ ] Không khẳng định điểm nghẽn thực tế khi chỉ có dữ liệu công khai/định tính; không tự ước lượng số bước thiếu.
- [ ] Mỗi FAQ và câu xử lý từ chối dựa trên câu hỏi, rào cản thật trong kho; bằng chứng dùng là bằng chứng có thật.
- [ ] Không tự đề xuất giảm giá; không lưu tên, số điện thoại, nguyên văn hội thoại của khách.
- [ ] Mỗi thay đổi lớn có thử nghiệm với chỉ số và điều kiện đánh giá; mức ưu tiên có lý do tác động × khả năng làm.
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi 7 bảng CRO (hoặc phần có dữ liệu) đã trình, người dùng biết phần nào đo được, phần nào cần đo thêm, và đã chọn thay đổi ưu tiên.
