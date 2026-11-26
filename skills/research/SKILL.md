---
name: research
description: Lập kế hoạch và điều phối nghiên cứu Marketing (Agent Market Research) — từ yêu cầu tự nhiên của người dùng ("tìm cơ hội Marketing dịp Tết", "tìm nguyên nhân khách chưa mua", "30 ý tưởng Content dựa trên nghiên cứu", "10 format video cho ngành", "nghiên cứu quảng cáo đề xuất góc mới", "ý tưởng combo", "cập nhật thị trường tháng này", "xây đầu vào Masterplan") xác định bài toán, quyết định cần hỗ trợ, đầu ra, mức nghiên cứu (Nhanh / Chuyên sâu / Cập nhật), đọc kho nghiên cứu sẵn có, lập Research Brief (RP) với ma trận câu hỏi – dữ liệu – nguồn – phương pháp, chọn workflow (01–09) và skill, giao subagent chạy song song, đặt điểm kiểm chứng và điểm chờ duyệt, tổng hợp và bàn giao qua kho có liên kết EVD → FIND → INS → OPP → IDEA/ADS/CAM. Vẫn giữ chế độ 3C cũ (5 giai đoạn, file 01–05). Dùng khi người dùng gõ /masterplan-agent:research hoặc yêu cầu bất kỳ việc nghiên cứu thị trường, khách hàng, đối thủ, Content, quảng cáo, kênh mà chưa nói rõ skill.
argument-hint: "[yêu cầu tự nhiên | 3c <chủ đề> | tiep-tuc RP-xxx]"
---

# /masterplan-agent:research

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`,
`${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/workflow.md` (workflow, định tuyến, subagent, tiếp tục khi gián đoạn).
Chế độ 3C: `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/che-do-3c.md`. Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`.

## A. Mục tiêu
Biến một yêu cầu tự nhiên thành một đợt nghiên cứu **có phạm vi, có điều kiện hoàn thành và đúng đầu ra**, chỉ chạy các skill cần thiết,
dùng lại tối đa kho sẵn có, để **một lần nghiên cứu tạo nhiều tài nguyên Marketing có bằng chứng và tái sử dụng được**.

## B. Điều kiện kích hoạt
- **Dùng khi**: người dùng yêu cầu nghiên cứu mà chưa chỉ định skill; cần phối hợp ≥ 2 skill; cần tiếp tục đợt đang dở (`tiep-tuc RP-xxx`);
  cần chế độ 3C (`3c <chủ đề>`); `dieu-phoi` chuyển các yêu cầu nghiên cứu sang đây.
- **Không dùng khi**: người dùng gọi thẳng một skill lẻ cho việc nhỏ (ví dụ chỉ cần `tu-khoa`) — skill đó tự tạo RP mức Nhanh;
  việc thuộc quy trình Masterplan năm theo bộ mẫu (Review → Market Research năm → Dự báo → Định hướng) → `dieu-phoi`.
- Chạy độc lập; cần `company-context.md` (chưa có → `setup` hoặc hỏi tối thiểu: ngành, sản phẩm, khu vực, nhóm khách, mục tiêu).

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Yêu cầu của người dùng; `company-context.md` |
| Tuỳ chọn | Hạn thời gian, giới hạn chi phí/lượt dùng, nguồn bắt buộc hoặc cấm, mức nghiên cứu mong muốn |
| Dữ liệu nội bộ | Kết quả `review-nam`, `bao-cao-kinh-doanh`, `chi-phi-ads`, `lead-hoi-thoai`, `danh-gia-kenh`, `quet-doi-thu`, `nghien-cuu-thi-truong` |
| Kế thừa từ kho | `kho.py tim --loai RP` (đợt cũ), `kho.py tim --chu "<chủ đề>"`, `kho.py kiem-tra` (bản ghi lỗi thời) |
| Khi thiếu | Thiếu hồ sơ → hỏi 5 câu tối thiểu; thiếu công cụ (Chrome, connector) → ghi vào Brief "nguồn thay thế", không giả định đã có |

## D. Phương pháp điều phối
| Hạng mục | Cách làm |
| --- | --- |
| Xác định đầu ra | Viết một câu "Sau đợt này người dùng nhận được: … để quyết định: …". Không mở rộng ngoài câu này |
| Chọn workflow và mức | Tra bảng định tuyến trong `workflow.md`; Nhanh nếu một câu hỏi và kho đã có ≥ 50% dữ liệu; Cập nhật nếu có RP cùng chủ đề; còn lại Chuyên sâu |
| Ma trận nghiên cứu | Mỗi câu hỏi: Dữ liệu cần có · Đã có trong kho (mã) · Còn thiếu · Nguồn · Phương pháp và mẫu (theo phạm vi khởi tạo trong `quy-tac-nghien-cuu.md`) · Skill/subagent |
| Kiểm kê công cụ | `tabs_context_mcp` (Chrome), WebSearch, connector (Meta Ads, TikTok, LadiPage, Drive, Sheets, Notion); ghi cái nào có |
| Song song | Chuyên sâu: giao subagent theo nhóm (`market-researcher`, `customer-researcher`, `competitor-researcher`, `content-researcher`) trong cùng một lượt; mỗi subagent nhận mã RP, đường dẫn kho, phần Brief của nó, nguồn được phép, giới hạn mẫu |
| Kiểm chứng xuyên suốt | Sau mỗi nhóm A: `kho.py kiem-tra --dot`; trước nhóm B: chạy `kiem-chung` (hoặc subagent `research-verifier`) cho FIND/KT/XH quan trọng; sau nhóm B: `kiem-chung` cho INS/OPP được dùng làm căn cứ |
| Tránh trùng | Không chạy lại skill có bản ghi còn hạn; Cập nhật chỉ thu thập phần lỗi thời/thiếu, cùng phạm vi để so sánh |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 0 | Nhận yêu cầu. `3c …` → chạy `che-do-3c.md`. `tiep-tuc RP-xxx` → `kho.py tien-do --dot RP-xxx`, làm tiếp bước dở. Chủ đề/dịp chung chung không rõ đầu ra → hỏi một lần: "Chế độ 3C cổ điển (5 file) hay theo đầu ra (đề xuất workflow …)?" | Yêu cầu | Chế độ | Đã rõ chế độ |
| 1 | Xác định bài toán, quyết định cần hỗ trợ, đầu ra cuối cùng, mức nghiên cứu, workflow | Yêu cầu, company-context | Câu đầu ra + workflow | — |
| 2 | Đọc kho: đợt cũ, bản ghi theo chủ đề, bản ghi lỗi thời | Kho | Dữ liệu đã có / còn thiếu | — |
| 3 | Lập ma trận câu hỏi – dữ liệu – nguồn – phương pháp; chọn skill, subagent; quy mô mẫu, giới hạn thời gian; điểm chờ duyệt; tiêu chuẩn hoàn thành | Bước 1–2 | Research Brief (bản nháp) | — |
| 4 | Ghi RP vào kho (`kho.py them`), tạo thư mục `nghien-cuu/<YYYY-MM-DD>-<chủ-đề>/brief.md` | Brief | RP-xxx | **DỪNG** — người dùng duyệt Brief (mức Nhanh: gộp vào báo cáo cuối nếu người dùng cho phép chạy luôn) |
| 5 | Chạy nhóm A theo workflow (song song khi Chuyên sâu); sau mỗi skill cập nhật `Tiến độ` trong RP | Brief | EVD, MAU, FIND, bản ghi lớp 2 | `kho.py kiem-tra --dot` không LỖI |
| 6 | Kiểm chứng giữa chừng (`kiem-chung` / `research-verifier`) | FIND, KT, XH | Trạng thái kết luận, MT, TH | Phát hiện dùng làm căn cứ không còn "Bị phản bác" chưa xử lý |
| 7 | Nhóm B theo workflow (insight → marketing-opportunities → tài nguyên) | Kho | INS, OPP, OFFER/TD/IDEA/FMT/ADS/CAM/CRO | **DỪNG** sau INS/OPP (Chuyên sâu) để người dùng chọn cơ hội trước khi phát triển tài nguyên |
| 8 | Kiểm chứng cuối cho INS/OPP làm căn cứ; `kho.py kiem-tra --dot` | Kho | Bảng kiểm chứng | Không LỖI; cảnh báo đã giải thích |
| 9 | Báo cáo và bàn giao: `kho.py bao-cao --dot RP-xxx --ra nghien-cuu/<thư mục>`; `kho.py xuat --dot RP-xxx --ra .../xuat --xlsx`; cập nhật `Tiến độ` = Hoàn thành | Kho | `bao-cao.md/.html`, CSV/XLSX | **DỪNG** — người dùng duyệt; chỉ khi người dùng bảo mới `kho.py duyet` |

## F. Đầu ra
1. **Research Brief** (`RP`, trường bắt buộc theo schema): Mục tiêu nghiên cứu · Quyết định cần hỗ trợ · Câu hỏi nghiên cứu · Phạm vi ·
   Mức nghiên cứu · Workflow · Dữ liệu đã có · Dữ liệu còn thiếu · Nguồn nghiên cứu · Phương pháp lấy mẫu · Skill và Subagent ·
   Đầu ra cuối cùng · Điểm chờ duyệt · Tiêu chuẩn hoàn thành; tuỳ chọn: Kết quả trung gian, Giới hạn chi phí và thời gian, Tiến độ.
   `brief.md` trình bày thêm **ma trận câu hỏi – dữ liệu – nguồn – phương pháp**.
2. **Báo cáo đợt** dựng từ kho: tổng quan, bảng theo từng loại, **truy vết tài nguyên → bằng chứng**, kết quả kiểm tra.
3. **File xuất** cho Agent khác: CSV từng kho (KH tách theo nhãn), `kho-nghien-cuu.xlsx`.
Ví dụ RP: bản ghi đầu tiên trong `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du-secondhand.json`.

## G. Cơ chế bàn giao
| Đầu ra | Chuyển cho |
| --- | --- |
| INS, OPP, TD | `dinh-huong-chien-luoc`, `nghien-cuu-thi-truong` (Masterplan năm), chiến lược thương hiệu |
| IDEA, FMT | content-agent (lịch, viết), design-agent, video-edit |
| ADS, OFFER | Agent quảng cáo, `chi-phi-ads` để đo sau triển khai |
| CAM | Lập kế hoạch chiến dịch, ngân sách, KPI (Masterplan) |
| CRO | Landing page, Sales, CRM, `lead-hoi-thoai` để đo lại |
| Toàn bộ kho | Lần nghiên cứu sau: kế thừa theo hạn dùng; workflow 08 cập nhật |

## H. Kiểm tra chất lượng
- [ ] Đầu ra cuối cùng đã chốt bằng một câu và đúng yêu cầu; không chạy nhánh thừa.
- [ ] Đã đọc kho trước khi thu thập; không thu thập lại bản ghi còn hạn.
- [ ] Brief có đủ trường bắt buộc và ma trận câu hỏi – dữ liệu – nguồn – phương pháp; công cụ đã kiểm tra thực tế.
- [ ] Mỗi lượt thu thập có MAU; mọi tài nguyên lớp 3 truy được về EVD (`kho.py truy-vet`).
- [ ] Đã chạy kiểm chứng giữa chừng và cuối; không Insight/cơ hội nào "Bị phản bác" còn được dùng làm căn cứ.
- [ ] Điểm DỪNG đã dừng thật; agent không tự đổi trạng thái sang Đã duyệt.
- [ ] `Tiến độ` trong RP cập nhật sau mỗi bước (tiếp tục được khi gián đoạn).
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi đạt "Tiêu chuẩn hoàn thành" của Brief, có báo cáo đợt + file xuất, và người dùng đã được hỏi duyệt.
