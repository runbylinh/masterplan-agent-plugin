---
name: kiem-chung
description: Kiểm chứng và đánh giá chất lượng nghiên cứu, chạy xuyên suốt đợt nghiên cứu chứ không chỉ ở cuối — kiểm tra nguồn có tồn tại và đã được đọc, thời gian, địa bàn, phạm vi, đơn vị đo, mức liên quan tới câu hỏi, dữ liệu trùng hoặc nhiều nguồn dẫn lại cùng một gốc, đối chiếu nguồn độc lập, thiên lệch chọn mẫu, bằng chứng phản bác, mối liên hệ giữa dữ liệu và kết luận; phân loại độ tin cậy (Cao / Trung bình / Thấp / Chưa xác định, luôn kèm lý do) và trạng thái kết luận (Có căn cứ / Cần bổ sung / Chưa đủ căn cứ / Bị phản bác) cho phát hiện, Insight, cơ hội, khoảng trống, xu hướng; ghi bảng mâu thuẫn (MT), dữ liệu thiếu (TH), giả thuyết và thử nghiệm (GT); đề xuất giữ, sửa, loại hoặc thử nghiệm. Dùng khi người dùng hỏi "insight này có căn cứ không", "kiểm chứng ý tưởng", "dữ liệu này đáng tin không", "nguồn nào mâu thuẫn", hoặc khi skill research tới điểm kiểm chứng (workflow 09 và giữa các bước).
argument-hint: "[mã bản ghi | --dot RP-xxx | chủ đề]"
---

# /masterplan-agent:kiem-chung

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`, `${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`,
`${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md` (mục 2–5). Cách đọc lại nguồn theo nền tảng:
`${CLAUDE_PLUGIN_ROOT}/references/nen-tang/`. Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`.

## A. Mục tiêu
Bảo đảm mọi kết luận dùng để ra quyết định Marketing **có căn cứ đúng mức**, nói rõ giới hạn, và chỉ ra dữ liệu cần bổ sung hoặc thử nghiệm
trước khi đầu tư. Ngăn quan sát lẻ bị nâng thành Insight, giả thuyết bị trình bày như dữ kiện.

## B. Điều kiện kích hoạt
- **Dùng khi**: sau mỗi nhóm thu thập (kiểm FIND, KT, XH); trước khi dùng INS/OPP làm căn cứ cho tài nguyên; người dùng hỏi về độ tin cậy;
  workflow 09 (kiểm chứng Insight và ý tưởng); `kho.py kiem-tra` có cảnh báo cần xử lý.
- **Không dùng khi**: cần thu thập dữ liệu mới quy mô lớn → trả TH và đề xuất skill thu thập; kiểm chứng ở đây chỉ đọc lại nguồn và
  tìm bổ sung có giới hạn (tối đa 5 nguồn mới cho mỗi kết luận).
- Chạy độc lập trên kho. Khi cần góc nhìn độc lập, giao subagent `research-verifier` (chỉ đưa mã bản ghi và đường dẫn kho, không đưa lập luận).

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Danh sách mã cần kiểm (FIND/INS/OPP/KT/XH, hoặc tài nguyên lớp 3 để kiểm chuỗi căn cứ) hoặc `--dot RP-xxx` |
| Tuỳ chọn | Mức rủi ro của quyết định (cao → yêu cầu kiểm chứng trực tiếp); câu hỏi kiểm chứng cụ thể |
| Kế thừa từ kho | `kho.py truy-vet <ID>` (chuỗi bằng chứng), `kho.py kiem-tra --dot`, MT/TH/GT cũ |
| Khi thiếu | Không mở lại được nguồn → ghi "không truy cập lại được", hạ độ tin cậy, không xoá EVD |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Tồn tại và đã đọc | Với EVD quan trọng: mở lại URL (WebSearch/Chrome); kiểm nội dung quan sát có đúng trên trang; nguồn nội bộ: đối chiếu file gốc |
| Phạm vi | So thời gian, địa bàn, nhóm khách, đơn vị đo của EVD với phạm vi RP; lệch → ghi giới hạn |
| Liên quan | Bằng chứng có trả lời đúng câu hỏi nghiên cứu không, hay chỉ gần chủ đề |
| Trùng và dẫn lại | Nhiều EVD cùng một nguồn gốc (báo đăng lại, repost) → tính là **một** nguồn; ghi `Nguồn gốc dẫn lại` |
| Độc lập | `kho.py truy-vet <ID>` cho số nguồn độc lập; "Có căn cứ" cần ≥ 2 (khác nền tảng hoặc tên miền) và không có phản bác mạnh |
| Thiên lệch mẫu | Đọc MAU: chỉ một nền tảng? chỉ nội dung nổi bật? thiếu khách chưa mua? thiếu phản hồi tiêu cực? → ghi giới hạn |
| Bằng chứng phản bác | Tìm chủ động: từ khóa ngược ("…không cần", "…không đáng"), review tích cực khi kết luận nói về nỗi lo, nhóm khách khác |
| Dữ liệu – kết luận | Kết luận có vượt dữ liệu? (một bình luận → "khách lo…"; view cao → "bán chạy"; Trends → "lượng tìm kiếm") |
| Phân loại | Độ tin cậy theo bảng mục 3 và trạng thái kết luận theo mục 4 `quy-tac-nghien-cuu.md`; **luôn ghi lý do** |
| Mâu thuẫn | Ghi MT (Phát hiện, Nguồn A, Nguồn B, Điểm khác biệt, Cách xử lý: tách theo phân khúc / thời điểm / cần thêm dữ liệu / ưu tiên nguồn chính thống có lý do) |
| Đề xuất thử nghiệm | Giả thuyết còn mở → GT (bằng chứng ủng hộ, phản bác, phương pháp kiểm chứng, chỉ số, điều kiện kết luận) |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 1 | Lập danh sách cần kiểm: ưu tiên bản ghi được tài nguyên lớp 3 dùng làm căn cứ, rồi FIND/KT/XH mới | `kho.py tim`, `truy-vet` | Danh sách + chuỗi căn cứ | — |
| 2 | Kiểm tồn tại, phạm vi, liên quan, trùng/dẫn lại cho EVD trong chuỗi | EVD, MAU | Ghi chú từng EVD | Đã xem hết EVD trong chuỗi (hoặc ghi không truy cập lại được) |
| 3 | Đếm nguồn độc lập; tìm bằng chứng phản bác (≤ 5 nguồn mới/kết luận, ghi EVD + MAU mới) | Kho, web | Số nguồn, phản bác | — |
| 4 | Kiểm thiên lệch mẫu và quan hệ dữ liệu – kết luận | MAU, nội dung bản ghi | Giới hạn | — |
| 5 | Ghi kết quả: `kho.py kiem-chung <ID> --muc "..." --tin-cay ... --ly-do "..."`; MT/TH/GT qua `kho.py them` | Kết luận | Trạng thái + lý do trong kho | Mỗi bản ghi đã kiểm có lý do |
| 6 | Kiểm chuỗi: `kho.py kiem-tra --dot`; tài nguyên dựa trên bản ghi "Bị phản bác"/"Loại" → đề xuất sửa hoặc loại | Kho | Danh sách xử lý | Không LỖI |
| 7 | Trình bảng kiểm chứng + đề xuất **giữ / sửa / loại / thử nghiệm** cho từng mục | Kết quả | Báo cáo | **DỪNG** chờ người dùng quyết định |

## F. Đầu ra
| Bảng | Nguồn trong kho | Trường |
| --- | --- | --- |
| Bảng kiểm chứng | `kiem_chung`, `do_tin_cay` + lý do trên FIND/INS/OPP/KT/XH | Phát hiện · Bằng chứng · Nguồn · Phạm vi · Giới hạn · Độ tin cậy · Trạng thái kết luận · Lý do |
| Bảng mâu thuẫn | MT | Phát hiện · Nguồn A · Nguồn B · Điểm khác biệt · Cách xử lý |
| Bảng thiếu dữ liệu | TH | Câu hỏi · Dữ liệu cần có · Nguồn bổ sung |
| Kho giả thuyết | GT | Giả thuyết · Bằng chứng ủng hộ · Bằng chứng phản bác · Phương pháp kiểm chứng · Chỉ số · Điều kiện kết luận |
Báo cáo: `kho.py bao-cao --dot RP-xxx --loai FIND INS OPP KT XH MT TH GT --ra nghien-cuu/<thư mục>/kiem-chung --tieu-de "Kiểm chứng ..."`.

Ví dụ lô (giả định):
```json
[{"loai": "MT", "tieu_de": "Mức giá khách chấp nhận", "du_lieu": {"Phát hiện": "FIND-007: khách chấp nhận combo 500k",
   "Nguồn A": "EVD-012 Group: nhiều người nói 500k hợp lý", "Nguồn B": "EVD-019 Shopee: đánh giá chê đắt ở mức 450k",
   "Điểm khác biệt": "Nhóm Group là nhân viên văn phòng, Shopee là sinh viên", "Cách xử lý": "Tách theo phân khúc SEG-002/SEG-003; không gộp kết luận"}},
 {"loai": "GT", "tieu_de": "Combo 500k phù hợp dân văn phòng", "du_lieu": {"Giả thuyết": "Nhân viên văn phòng chấp nhận combo 500k",
   "Bằng chứng ủng hộ": "EVD-012", "Bằng chứng phản bác": "Chưa có cho nhóm này", "Phương pháp kiểm chứng": "Đặt trước 2 tuần, 2 mức giá",
   "Chỉ số": "Tỷ lệ đặt trước mỗi mức", "Điều kiện kết luận": "≥ 30 lượt hỏi mỗi mức"}}]
```
Ghi trạng thái: `kho.py kiem-chung FIND-007 --muc "Cần bổ sung" --tin-cay Thấp --ly-do "Hai nguồn mâu thuẫn theo phân khúc (MT-001)"`.

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| Trạng thái + lý do trên bản ghi; MT, TH, GT | `research` (quyết định đi tiếp), skill nhóm B (chỉ dùng căn cứ không bị phản bác), skill thu thập (theo TH) | Quyết định giữ/sửa/loại/thử nghiệm; kế hoạch thử nghiệm | GT có `Kết quả thử nghiệm` → cập nhật INS/OPP liên quan; workflow 08 kiểm lại bản ghi lỗi thời |

## H. Kiểm tra chất lượng
- [ ] Mọi bản ghi đã kiểm có độ tin cậy và trạng thái kết luận **kèm lý do**.
- [ ] "Có căn cứ" chỉ khi ≥ 2 nguồn độc lập và đã tìm phản bác; nguồn dẫn lại tính là một.
- [ ] Đã đọc MAU và ghi thiên lệch mẫu nếu có.
- [ ] Mâu thuẫn được ghi MT, không tự chọn một bên khi chưa có lý do.
- [ ] Không xoá bản ghi; bản ghi bị phản bác vẫn giữ lịch sử.
- [ ] Không sửa bản ghi Đã duyệt khi người dùng chưa đồng ý.
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi có bảng kiểm chứng, MT/TH/GT (nếu có) và đề xuất giữ/sửa/loại/thử nghiệm cho từng mục, chờ người dùng quyết định.
