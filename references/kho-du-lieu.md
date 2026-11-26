# Kho dữ liệu nghiên cứu (dùng chung cho mọi skill nghiên cứu)

**Một lần nghiên cứu, nhiều tài nguyên có liên kết.** Mọi skill nghiên cứu và chuyển hoá ghi kết quả vào **kho**
(`kho/` trong thư mục làm việc) bằng `scripts/kho.py`, thay vì để rời rạc trong từng báo cáo. Báo cáo .md/.html
được dựng lại từ kho (`kho.py bao-cao`), nên một ý tưởng luôn truy ngược được về Insight, phát hiện và bằng chứng gốc.

## 1. Ba lớp dữ liệu và chuỗi liên kết
| Lớp | Nội dung | Mã |
| --- | --- | --- |
| 0 | Research Brief của đợt (dùng làm `dot`) | RP |
| 1 – Dữ liệu gốc | Nguồn đã đọc: báo cáo, bài viết, video, quảng cáo, bình luận, review, từ khóa, dữ liệu nội bộ; nhật ký lấy mẫu | EVD, MAU |
| 2 – Kết quả phân tích | Phát hiện, nội bộ doanh nghiệp, thị trường, xu hướng, mùa vụ, khách hàng, phân khúc, hành trình, đối thủ, ưu đãi, thông điệp thị trường, khoảng trống, từ khóa, Content, quảng cáo, landing page, Insight, cơ hội, giả thuyết, mâu thuẫn, dữ liệu thiếu | FIND, DN, TT, XH, MV, BD, RR, KH, SEG, HT, DV, UD, TN, KT, KEY, CNT, QC, LP, INS, OPP, GT, MT, TH |
| 3 – Tài nguyên Marketing | Sản phẩm và ưu đãi, định vị và thông điệp, ý tưởng Content, format, quảng cáo, chiến dịch, chuyển đổi, kênh/cộng đồng/Creator | OFFER, TD, IDEA, FMT, ADS, CAM, CRO, KEN |

```
EVD ─► FIND / KH / KEY / CNT / QC / DV ... ─► INS ─► OPP ─► OFFER · TD · IDEA · FMT · ADS · CAM · CRO
```
Không bắt buộc mọi tài nguyên đi qua đủ các tầng (ví dụ IDEA có thể dựa thẳng trên KEY + INS), nhưng **mọi tài nguyên phải truy được
về bằng chứng gốc** (EVD hoặc bản ghi có trường Nguồn). Một tài nguyên được liên kết nhiều bằng chứng, Insight, cơ hội.
`kho.py kiem-tra` báo **lỗi** khi thiếu cha bắt buộc và **cảnh báo** khi không truy được về bằng chứng gốc.
Khi người dùng hỏi "ý tưởng này từ đâu ra": `kho.py truy-vet <ID>`.

## 2. Các loại bản ghi
| Mã | Tên | Skill tạo | Cha bắt buộc |
| --- | --- | --- | --- |
| RP | Research Brief | research | — |
| MAU | Nhật ký lấy mẫu (mỗi nguồn/lượt thu thập) | mọi skill thu thập | — |
| EVD | Bằng chứng gốc | mọi skill thu thập | — |
| FIND | Phát hiện (Dữ kiện / Quan sát / Mẫu lặp / Giả thuyết) | mọi skill | EVD |
| DN | Nội bộ: Hồ sơ doanh nghiệp, Ma trận sản phẩm, Đánh giá Marketing, Danh sách vấn đề, Kho lợi thế, Giới hạn triển khai | company-analysis | (có Nguồn) |
| TT, XH, MV, BD, RR | Bản đồ thị trường, xu hướng, lịch mùa vụ, biến động nhu cầu, rủi ro | xu-huong-mua-vu | (có Nguồn) |
| KH, SEG, HT | Phát biểu khách đã gắn nhãn; phân khúc/chân dung; hành trình | customer-research | KH: Nguồn; SEG, HT: KH/FIND |
| DV, UD, TN, KT | Hồ sơ đối thủ; sản phẩm và ưu đãi thị trường; thông điệp thị trường; khoảng trống cạnh tranh | competitor-research | KT: DV/UD/TN/FIND/KH |
| KEY | Từ khóa | tu-khoa | (có Nguồn) |
| CNT | Content nghiên cứu | nghien-cuu-content | (có URL) |
| FMT | Format sáng tạo (Video / Hình ảnh) | format-sang-tao | CNT/QC/EVD |
| QC, LP | Thư viện quảng cáo; ma trận landing page / bản đồ chuyển đổi | quang-cao-chuyen-doi | (có Nguồn) |
| KEN | Bản đồ kênh, cộng đồng, Creator, kênh vệ tinh, cơ hội hợp tác, định hướng phân phối | kenh-cong-dong | (có Nguồn) |
| INS | Insight | insight | FIND/KH/SEG/CNT/KEY/QC/EVD |
| OPP | Cơ hội Marketing | marketing-opportunities | INS/FIND/KT/XH/MV |
| OFFER, TD, IDEA, ADS, CAM, CRO | Tài nguyên Marketing | skill chuyển hoá | INS/OPP (xem schema) |
| GT, MT, TH | Giả thuyết/thử nghiệm; mâu thuẫn; dữ liệu thiếu | kiem-chung | — |
Trường bắt buộc, giá trị cho phép, hạn dùng của từng loại: `${CLAUDE_PLUGIN_ROOT}/templates/kho/schema.json`.
Kho khách hàng (`KH`) xuất thành các kho riêng theo nhãn: nhu cầu, nỗi đau, động lực mua, rào cản, tiêu chí lựa chọn,
tình huống mua, câu hỏi, ngôn ngữ khách hàng, trải nghiệm sau mua.

## 3. Thuộc tính chung của mọi bản ghi
| Thuộc tính | Ý nghĩa |
| --- | --- |
| `id` | Tự cấp: `<LOẠI>-<số 3 chữ số>`, không đặt tay |
| `tieu_de` | Một dòng dễ đọc |
| `du_lieu` | Các trường nghiệp vụ theo schema (tên trường tiếng Việt, đúng chính tả như schema) |
| `lien_ket` | Danh sách mã cha. Trong cùng một lô thêm mới dùng `"tam": "x"` và `"@x"` |
| `trang_thai` | `Chờ duyệt` (mặc định) · `Đã duyệt` · `Loại`. Agent không tự đổi sang Đã duyệt. Bản ghi Đã duyệt không bị ghi đè: `cap-nhat` từ chối trừ khi có `--sua-ban-da-duyet` (người dùng đồng ý), khi đó bản ghi quay về Chờ duyệt |
| `do_tin_cay`, `ly_do_tin_cay` | `Cao` · `Trung bình` · `Thấp` · `Chưa xác định` (mặc định); luôn ghi lý do (xem `nghien-cuu/quy-tac-nghien-cuu.md`) |
| `kiem_chung`, `ly_do_kiem_chung` | Riêng FIND, INS, OPP, KT, XH: `Có căn cứ` · `Cần bổ sung` (mặc định) · `Chưa đủ căn cứ` · `Bị phản bác`. Do skill `kiem-chung` ghi, kèm lý do |
| `dot` | Mã RP của đợt nghiên cứu |
| `ngay_tao`, `ngay_cap_nhat`, `lich_su` | Tự ghi; mọi thay đổi có dòng lịch sử |

"Có căn cứ" cần **≥ 2 nguồn độc lập** (khác nền tảng hoặc khác tên miền) phía trên bản ghi (`nguong_co_can_cu` trong schema).
Chế độ 3C cũ vẫn giữ quy tắc riêng "Đã xác minh" cần 3 nguồn (`quy-tac-3c.md`).

## 4. Lệnh
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py khoi-tao
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py tim --loai INS OPP --chu "tết"        # kiểm tra kho trước mỗi nhiệm vụ
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py them <lô>.json                          # thêm; tự chống trùng, tự cấp mã
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py cap-nhat INS-003 <thay-doi>.json
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py kiem-chung FIND-004 --muc "Có căn cứ" --tin-cay Cao --ghi-chu "3 nền tảng"
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py truy-vet CAM-002
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py kiem-tra [--dot RP-004]
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py bao-cao --dot RP-004 --ra nghien-cuu/<thư mục đợt> --tieu-de "..."
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py xuat --ra nghien-cuu/<thư mục đợt>/xuat --xlsx [--dot RP-004]
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py thay-doi --tu 2026-11-01                 # báo cáo thay đổi theo giai đoạn
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py tien-do --dot RP-004                      # tiếp tục khi phiên bị gián đoạn
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py nhom --loai IDEA --theo "Content Pillar"   # dựng hệ thống Pillar, kho Hook, nhóm theo một trường
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py duyet IDEA-004 IDEA-005 --trang-thai "Đã duyệt"   # chỉ khi người dùng bảo
```
Lô thêm mới (`<lô>.json`) là danh sách bản ghi, hoặc `{"dot": "RP-004", "ban_ghi": [...]}` để gắn mã đợt cho cả lô
(trong lô tạo RP mới dùng `"dot": "@rp"`):
```json
[
  {"tam": "e1", "loai": "EVD", "tieu_de": "Bình luận video phối đồ", "dot": "RP-004",
   "du_lieu": {"Nguồn": "https://...", "Nền tảng": "TikTok", "Ngày đăng": "2026-11-10", "Ngày thu thập": "2026-11-26",
               "Nội dung quan sát": "Nhiều bình luận hỏi size", "Loại nguồn": "Công khai", "Phạm vi mẫu": "40 bình luận"}},
  {"tam": "f1", "loai": "FIND", "tieu_de": "Khách lo không vừa size", "dot": "RP-004", "lien_ket": ["@e1"],
   "du_lieu": {"Phát hiện": "...", "Phân loại": "Mẫu lặp", "Nhóm": "Khách hàng", "Bằng chứng tóm tắt": "...", "Phạm vi": "Hà Nội, 11/2026"}}
]
```
Ví dụ đầy đủ một chuỗi (giả định): `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du-secondhand.json`.

## 5. Quy tắc lưu trữ
- **Trước mỗi nhiệm vụ**: `kho.py tim` theo chủ đề để dùng lại bản ghi còn hạn; chỉ thu thập phần thiếu hoặc đã lỗi thời.
- **Chống trùng**: kho tự nhận bản ghi trùng (theo khoá trong schema hoặc tiêu đề) và chỉ bổ sung liên kết.
- **Hạn dùng**: mỗi loại có `han_dung` (ngày). Quá hạn → `kiem-tra` cảnh báo "có nguy cơ lỗi thời", `thay-doi` liệt kê cần cập nhật.
- **Không dữ liệu cá nhân**: `kiem-tra` báo lỗi khi thấy email hoặc số điện thoại. Câu nói của khách viết lại ngắn, ẩn danh.
- **Nơi lưu khác**: kho gốc là file `kho/*.jsonl`. Muốn Google Sheets: `xuat --xlsx` rồi tải lên (hỏi trước), hoặc ghi từng tab
  theo file CSV xuất ra. Muốn Notion: tạo database theo cột của file CSV khi người dùng cho phép.
- Kho là dữ liệu thật của doanh nghiệp: không đưa lên GitHub (đã có trong `.gitignore`).
