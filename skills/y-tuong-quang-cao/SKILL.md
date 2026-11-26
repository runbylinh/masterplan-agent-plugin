---
name: y-tuong-quang-cao
description: Phát triển ý tưởng quảng cáo từ kho nghiên cứu — kết hợp Insight (INS), động lực và rào cản khách (KH), thông điệp (TD), sản phẩm và ưu đãi (DN, OFFER), quảng cáo tham khảo (QC) và dữ liệu quảng cáo nội bộ (chi-phi-ads) để xác định sản phẩm và mục tiêu, nhóm khách, nhu cầu/động lực/rào cản cần tác động, nhiều góc tiếp cận khác nhau về bản chất, Hook, thông điệp, lợi ích, bằng chứng, CTA, concept hình ảnh/video, biến thể thử nghiệm, giả thuyết và chỉ số đánh giá. Đầu ra kho ADS. Không hứa kết quả, không dùng bằng chứng chưa có thật. Dùng khi người dùng gõ /masterplan-agent:y-tuong-quang-cao, nói "ý tưởng quảng cáo", "góc quảng cáo mới", "concept ads", "Hook quảng cáo", "biến thể thử nghiệm", "test creative", "quảng cáo cho sản phẩm X".
argument-hint: "[sản phẩm hoặc OFFER-xxx] [mục tiêu] [--dot RP-xxx]"
---

# /masterplan-agent:y-tuong-quang-cao

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`,
`${CLAUDE_PLUGIN_ROOT}/references/chi-phi-ads.md` (khi dùng số Ads nội bộ). Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`.
Skill này **không thu thập lại dữ liệu** và **không tạo, sửa, bật quảng cáo**.

## A. Mục tiêu
Tạo **kho góc quảng cáo có giả thuyết kiểm chứng được**: mỗi góc tác động một nhu cầu, động lực hoặc rào cản cụ thể đã có bằng chứng, có
concept, biến thể và chỉ số để đội chạy quảng cáo thử nghiệm có chủ đích thay vì đổi câu chữ ngẫu nhiên. Phục vụ quyết định: chọn góc và
concept để sản xuất, thiết kế bộ thử nghiệm creative, chỉ số dừng/giữ.

## B. Điều kiện kích hoạt
- **Dùng khi**: kho có INS hoặc KH (động lực, rào cản) và biết sản phẩm cần quảng cáo; workflow 04; người dùng hỏi góc, concept, Hook, biến thể.
- **Không dùng khi**: chưa có dữ liệu khách → `customer-research`; cần đọc quảng cáo thị trường → `quang-cao-chuyen-doi`; cần đánh giá chi phí,
  CPL, ROAS hiện tại → `chi-phi-ads`; cần viết hoàn chỉnh kịch bản → `content-agent:write`.
- **Chạy độc lập** được (tự tạo RP mức Nhanh). Tốt hơn khi đã có `dinh-vi-thong-diep` (TD) và `san-pham-uu-dai` (OFFER).

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Sản phẩm/dịch vụ; mục tiêu quảng cáo (nhận biết, tin nhắn, lead, đơn hàng); mã đợt RP; ≥ 1 INS hoặc KH nhãn Động lực/Rào cản |
| Tuỳ chọn | Ngân sách thử nghiệm (do người dùng đặt); nền tảng (Meta, TikTok, Google); OFFER đang có; giới hạn sản xuất |
| Dữ liệu nội bộ | Kết quả chiến dịch cũ theo creative (`chi-phi-ads/*/chi-so-chi-phi.json`, connector Meta Ads/TikTok Ads chỉ đọc): góc nào đã chạy, CTR, chi phí mỗi kết quả; câu hỏi và lý do không chốt (`lead-hoi-thoai`) |
| Kế thừa từ kho | `kho.py tim --loai INS KH SEG --chu "<sản phẩm>"` · `--loai TD OFFER OPP` · `--loai QC LP` · `--loai DN` (Ma trận sản phẩm, bằng chứng) · `--loai ADS` (ADS cũ để kiểm trùng) |
| Khi thiếu | Thiếu QC → không ghi "góc đã bão hoà", đề xuất `quang-cao-chuyen-doi`. Thiếu TD → thông điệp tạm từ INS, ghi "chưa đối chiếu TD". Thiếu OFFER → `Offer` = "Không dùng ưu đãi" hoặc "cần xác nhận …", không tự đặt giảm giá. Thiếu dữ liệu Ads nội bộ → giả thuyết không có mốc so sánh, ghi TH |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Sản phẩm và mục tiêu | Mục tiêu quyết định CTA và chỉ số: nhận biết → tỷ lệ xem 3 giây/ThruPlay; tin nhắn → chi phí mỗi hội thoại, tỷ lệ hội thoại thành lead; lead → CPL, tỷ lệ lead đạt; đơn → chi phí mỗi đơn, tỷ lệ chốt |
| Nhóm khách | Từ SEG/INS; mỗi ADS một nhóm khách. Nhóm khách khác nhau về giai đoạn hành trình → góc khác nhau |
| Chọn yếu tố tác động | Liệt kê nhu cầu, động lực, rào cản từ KH/INS kèm tần suất và nguồn; ưu tiên yếu tố lặp ở ≥ 2 nguồn hoặc xuất hiện trong lý do không chốt nội bộ. Ghi vào trường `Nhu cầu, động lực hoặc rào cản` dạng "Rào cản: …" / "Động lực: …" / "Nhu cầu: …" |
| Góc tiếp cận | Mỗi góc khai thác **một yếu tố khác nhau về bản chất**. Kiểu góc: vấn đề–giải pháp, gỡ rào cản (rủi ro, giá, thời gian), so sánh trước–sau, bằng chứng xã hội, chuyên gia/quy trình, tình huống sử dụng, ưu đãi có thời hạn. **Quy tắc trùng**: hai ADS cùng `Nhu cầu, động lực hoặc rào cản` + cùng `Góc tiếp cận` là trùng → gộp thành biến thể Hook |
| Hook, thông điệp, lợi ích | Hook từ ngôn ngữ khách (KH) hoặc công thức Hook của QC nổi bật; thông điệp lấy từ TD Kho thông điệp bán hàng khi có; lợi ích là kết quả khách nhận, không phải tính năng |
| Bằng chứng | Chỉ dùng bằng chứng đang có thật (DN, TD Kho bằng chứng: đánh giá, video thật, quy trình, chứng nhận). Chưa có → ghi "cần chuẩn bị: …" và không đưa vào bản sản xuất |
| Offer, CTA | Offer lấy từ OFFER/DN; không tự đặt giảm giá. CTA khớp mục tiêu và điểm đến (LP) |
| Concept | Mô tả hình ảnh/video đủ để sản xuất: bối cảnh, nhân vật, cảnh mở đầu, diễn biến, cảnh kết; định dạng (FMT nếu có), thời lượng, tỷ lệ khung |
| Biến thể thử nghiệm | Mỗi lần chỉ đổi **một biến**: Hook, hình mở đầu, thông điệp, Offer hoặc CTA. Ghi rõ biến nào đổi và giữ nguyên gì |
| Giả thuyết và chỉ số | Câu: *Góc [X] tác động [yếu tố] sẽ [chỉ số] tốt hơn góc [Y] với [nhóm khách]*. Chỉ số chính + điều kiện kết luận (số kết quả tối thiểu, thời gian). Có dữ liệu Ads cũ → lấy làm mốc; không có → ghi "chưa có mốc" |
| Tuân thủ | Không hứa kết quả (giảm cân, khỏi mụn, thu nhập), không so sánh nêu tên đối thủ, không bằng chứng giả; mỹ phẩm, sức khoẻ, tài chính, giáo dục kiểm thêm chính sách quảng cáo của nền tảng |
| Mâu thuẫn | Dữ liệu Ads nội bộ trái với Insight công khai (góc rào cản giá chạy kém) → ghi MT, giữ cả hai góc trong thử nghiệm, không tự loại |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 0 | Đọc kho, ADS cũ (cặp yếu tố + góc), kết quả Ads nội bộ nếu có | Kho, `chi-phi-ads/` | Bản ghi dùng được, góc đã chạy | Có INS/KH và sản phẩm |
| 1 | Xác định sản phẩm và mục tiêu, chỉ số chính | DN, OFFER, yêu cầu | Mục tiêu + chỉ số | — |
| 2 | Xác định nhóm khách | SEG, INS | 1–3 nhóm khách | — |
| 3 | Chọn nhu cầu/động lực/rào cản cần tác động, kèm tần suất và nguồn | KH, INS, lý do không chốt | Danh sách yếu tố có mã | Mỗi yếu tố có bằng chứng |
| 4 | Tạo nhiều góc tiếp cận, mỗi góc một yếu tố khác nhau | Bước 3, QC | Kho góc | Không có cặp yếu tố + góc trùng |
| 5 | Viết Hook, thông điệp, lợi ích, bằng chứng, Offer, CTA | TD, OFFER, DN, KH ngôn ngữ | ADS nháp | Bằng chứng có thật hoặc ghi "cần chuẩn bị" |
| 6 | Viết concept hình ảnh/video, format | FMT, QC | Concept | — |
| 7 | Thiết kế biến thể (đổi một biến mỗi lần) | ADS nháp | Biến thể thử nghiệm | — |
| 8 | Viết giả thuyết, chỉ số, điều kiện kết luận; ghi kho `kho.py them lo-ads.json --dot RP-xxx`, `kho.py kiem-tra --dot RP-xxx` | Lô | ADS-xxx | Không còn LỖI |
| 9 | Trình bảng ADS theo nhóm khách × yếu tố tác động + kế hoạch thử | ADS | — | **DỪNG** chờ duyệt; người dùng chọn góc để sản xuất; agent không tạo quảng cáo |

## F. Đầu ra — Kho ý tưởng quảng cáo (`ADS`)
Trường bắt buộc: Sản phẩm · Khách hàng · Nhu cầu, động lực hoặc rào cản · Góc tiếp cận · Hook · Thông điệp · Lợi ích · Bằng chứng · Offer ·
Concept · Format · CTA · Giả thuyết · Biến thể thử nghiệm · Chỉ số đánh giá. `lien_ket` ≥ 1 INS/OPP/QC/KH (thêm TD, OFFER, DN).
Tiêu đề bản ghi = "Yếu tố – Góc" để kho tự chống trùng theo tiêu đề. Báo cáo: `kho.py bao-cao --dot RP-xxx --loai ADS`.
Ví dụ lô kiểm thử (giả định, mỹ phẩm): `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/y-tuong-quang-cao.json`.

```json
{"loai": "ADS", "tieu_de": "Rào cản sợ kích ứng – Dùng thử trên vùng nhỏ trước", "lien_ket": ["INS-001", "KH-001", "OFFER-001"],
 "du_lieu": {"Sản phẩm": "Serum phục hồi da (ví dụ)", "Khách hàng": "Nữ 22–30, da nhạy cảm từng kích ứng khi đổi sản phẩm",
   "Nhu cầu, động lực hoặc rào cản": "Rào cản: sợ kích ứng khi thử sản phẩm mới", "Góc tiếp cận": "Gỡ rủi ro: thử trên vùng nhỏ bằng mẫu dùng thử trước khi mua chai lớn",
   "Hook": "Da từng bị kích ứng thì đừng mua chai lớn ngay", "Thông điệp": "Thử 7 ngày bằng mẫu nhỏ rồi mới quyết định",
   "Lợi ích": "Yên tâm thử, không phí tiền nếu không hợp", "Bằng chứng": "Quy trình thử trên vùng da nhỏ do dược sĩ hướng dẫn (video có sẵn)",
   "Offer": "Mẫu dùng thử 7 ngày (OFFER-001, chi phí đã xác nhận)", "Concept": "Cận cảnh thoa thử sau tai, lịch 7 ngày đánh dấu, kết thúc bằng chai lớn",
   "Format": "Video dọc 20 giây", "CTA": "Nhận mẫu dùng thử", "Giả thuyết": "Góc gỡ rủi ro có tỷ lệ đăng ký mẫu thử cao hơn góc thành phần với nhóm da nhạy cảm",
   "Biến thể thử nghiệm": "Chỉ đổi Hook: 'Da từng bị kích ứng…' vs 'Thử trước, mua sau'", "Chỉ số đánh giá": "Chi phí mỗi đăng ký mẫu thử, tỷ lệ mua chai lớn sau 14 ngày; kết luận khi mỗi biến thể ≥ 50 đăng ký"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| Kho `ADS` (+ GT cho giả thuyết, TH bằng chứng cần chuẩn bị) | Đội quảng cáo (người dùng tự tạo quảng cáo); `content-agent:write` (kịch bản quảng cáo), plugin video-edit, `design-agent:design` (sản xuất creative); `toi-uu-chuyen-doi` (đồng bộ điểm đến); `y-tuong-chien-dich` (hoạt động thu hút) | Bộ thử nghiệm creative, brief sản xuất | Hạn dùng 180 ngày; sau khi chạy ghi kết quả vào GT (`Kết quả thử nghiệm`, `Quyết định`) để lần sau không lặp góc đã thua |

## H. Kiểm tra chất lượng
- [ ] Mỗi ADS khai thác một nhu cầu/động lực/rào cản cụ thể có bằng chứng; không có hai ADS trùng yếu tố + góc.
- [ ] Các góc khác nhau về bản chất, không chỉ đổi câu chữ; biến thể đổi đúng một biến.
- [ ] Bằng chứng đều có thật; bằng chứng chưa có ghi "cần chuẩn bị" và không đưa vào bản sản xuất.
- [ ] Không hứa kết quả, không giảm giá tự đặt, không nêu tên đối thủ; đã lưu ý chính sách quảng cáo ngành nhạy cảm.
- [ ] Mỗi ADS có giả thuyết, chỉ số chính và điều kiện kết luận; số Ads nội bộ (nếu dùng) có nguồn và kỳ.
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi kho ADS đã trình theo nhóm khách × yếu tố tác động, người dùng chọn góc sản xuất và có kế hoạch thử với chỉ số rõ.
