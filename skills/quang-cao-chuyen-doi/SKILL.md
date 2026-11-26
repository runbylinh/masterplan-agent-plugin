---
name: quang-cao-chuyen-doi
description: Nghiên cứu quảng cáo và hành trình chuyển đổi của thị trường — thu mẫu quảng cáo từ Meta Ads Library, TikTok Creative Center, Social; phân loại theo sản phẩm, khách, nhu cầu, góc, format; bóc Hook, lợi ích, bằng chứng, ưu đãi, giá, combo, CTA; mở điểm đến (website, landing page, form, inbox) để xem cấu trúc trang, bằng chứng, trải nghiệm đăng ký/đặt lịch/tư vấn (không giao dịch); kiểm tra nhất quán quảng cáo – landing page – offer; đối chiếu phản hồi khách và dữ liệu chuyển đổi nội bộ nếu được cấp; tìm góc đang khai thác nhiều và góc ít xuất hiện trong mẫu; lập giả thuyết quảng cáo và chuyển đổi cần thử. Ghi vào Thư viện quảng cáo (QC), Ma trận landing page / Bản đồ chuyển đổi (LP), Giả thuyết thử nghiệm (GT); kho góc, Hook, ưu đãi là các bảng lọc từ QC/UD. Dùng khi người dùng nói "nghiên cứu quảng cáo ngành", "đối thủ chạy ads góc nào", "bóc landing page", "kho hook quảng cáo", "vì sao khách bấm mà không đăng ký", "tìm góc quảng cáo mới", hoặc khi workflow 04 / 06 cần QC, LP.
argument-hint: "[sản phẩm hoặc nhóm khách] [--muc-tieu dang-ky|dat-lich|mua|tu-van] [--dot RP-xxx]"
---

# /masterplan-agent:quang-cao-chuyen-doi

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`.
Cách làm theo nguồn: `${CLAUDE_PLUGIN_ROOT}/references/nen-tang/` — `meta-ads-library.md`, `tiktok-creative-center.md`, `website-landing-page.md`,
`facebook.md`, `tiktok.md`, `san-tmdt.md` (điểm đến là gian hàng), `crm-noi-bo.md` (CRM, Sales, tài khoản quảng cáo nội bộ).
Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`. Thư mục đợt: `nghien-cuu/<YYYY-MM-DD>-<chủ-đề>/`.

## A. Mục tiêu
Hiểu **thị trường đang thuyết phục khách bằng gì và dẫn khách đi đâu**: sản phẩm được đẩy, nhu cầu được khai thác, góc, Hook, ưu đãi,
bằng chứng, điểm đến và các bước khách phải đi qua; tìm chỗ thiếu nhất quán và góc ít được khai thác. Phục vụ quyết định: chọn góc và
concept quảng cáo, cấu trúc landing page, ưu đãi cần thử, điểm nghẽn chuyển đổi cần kiểm chứng.

## B. Điều kiện kích hoạt
- **Dùng khi**: chuẩn bị chiến dịch quảng cáo mới, cần thư viện góc/Hook; tỷ lệ chuyển đổi thấp cần xem thị trường làm landing page và
  quy trình tư vấn thế nào; workflow 04 (Quảng cáo) hoặc 06 (Tối ưu chuyển đổi).
- **Không dùng khi**: chỉ cần theo dõi đối thủ có ads/offer mới so với lần quét trước → `quet-doi-thu`; chỉ cần tổng chi phí và
  chi phí/lead của chính doanh nghiệp → `chi-phi-ads`; cần phân tích inbox → `lead-hoi-thoai`; cần hồ sơ đối thủ đầy đủ → `competitor-research`.
- **Chạy độc lập** được. Kế thừa DV/UD/TN của `competitor-research`, KH rào cản của `customer-research`, ảnh chụp quét của `quet-doi-thu`.

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Sản phẩm/dịch vụ cần nghiên cứu; nhóm khách; mục tiêu chuyển đổi (mua, đăng ký, đặt lịch, nhắn tin tư vấn); mã đợt RP |
| Tuỳ chọn | Danh sách đơn vị/trang cần xem; thị trường địa lý; landing page của chính doanh nghiệp để đối chiếu |
| Dữ liệu nội bộ | Kết quả `chi-phi-ads`; số Meta Ads/TikTok Ads qua connector (khi người dùng cho phép); CRM, lý do mất khách từ Sales; `lead-hoi-thoai` |
| Kế thừa từ kho | `kho.py tim --loai QC LP UD DV TN --chu "<sản phẩm>"`; `kho.py tim --loai KH --chu "rào cản"` |
| Khi thiếu | Không có dữ liệu chuyển đổi nội bộ → mọi điểm nghẽn ghi là "giả thuyết điểm nghẽn", ghi TH; Ads Library không hiển thị (khu vực, đăng nhập) → nhờ người dùng mở, hoặc dùng quảng cáo thấy trên Social, ghi MAU |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Nội dung | Sản phẩm được quảng bá · khách và nhu cầu khai thác · Hook, góc, thông điệp, lợi ích · hình/video, format, cấu trúc · ưu đãi, giá, combo, CTA · điểm đến · cấu trúc landing page và bằng chứng · trải nghiệm đăng ký/đặt/tư vấn · rào cản và lý do chưa mua · dữ liệu hiệu quả nội bộ |
| Nguồn và công cụ | Meta Ads Library (lọc quốc gia, trạng thái đang chạy), TikTok Creative Center (Top Ads theo ngành), Social, website, landing page; Claude in Chrome để mở và chụp; connector Meta Ads (`ads_library_search`, số nội bộ) chỉ khi có trong phiên |
| Xây từ khóa | Tên đơn vị từ DV; từ khóa sản phẩm và nhu cầu từ KEY ("khoá học excel cho người đi làm", "trà sữa giao tận nơi"); từ khóa ưu đãi ("ưu đãi", "tặng", "combo", "học thử") |
| Chọn và thu mẫu | Phạm vi khởi tạo 20–30 quảng cáo từ 5–10 đơn vị; mỗi đơn vị lấy cả quảng cáo chạy lâu (ghi ngày bắt đầu hiển thị) và quảng cáo mới; 5–10 điểm đến. Ghi "ngày bắt đầu chạy" là dữ kiện hiển thị, không suy ra hiệu quả |
| Trích xuất | Mỗi quảng cáo một QC: Hook (nguyên văn), góc, lợi ích, bằng chứng, ưu đãi, CTA, điểm đến, nhất quán với điểm đến. Mỗi section landing page một LP `Ma trận landing page`; mỗi bước từ quảng cáo đến hoàn tất một LP `Bản đồ chuyển đổi` (hành động, rào cản quan sát được) |
| Điểm đến | Mở trang/form/inbox tự động để xem bước, trường thông tin, thời gian phản hồi hiển thị. **Không** điền form, không gửi tin, không đặt lịch, không thanh toán; dừng ở bước trước khi gửi |
| Phân loại, đối chiếu | Ma trận góc × sản phẩm × nhóm khách: đếm số mẫu mỗi ô. Góc ≥ 30% mẫu = đang khai thác nhiều; góc 0–1 mẫu nhưng có nhu cầu trong KH/INS = ứng viên khoảng trống (chỉ "trong mẫu đã xem") |
| Kiểm chứng | So lời hứa quảng cáo với nội dung landing page và điều kiện ưu đãi (chữ nhỏ). Đối chiếu rào cản với phản hồi khách (bình luận, KH) và dữ liệu chuyển đổi nội bộ khi có |
| Cấm | Suy đoán ngân sách, ROAS, CPA, doanh thu, hiệu quả quảng cáo của đối thủ; khẳng định điểm nghẽn thực tế chỉ từ dữ liệu công khai |
| Mâu thuẫn | Ưu đãi khác nhau giữa quảng cáo và trang, hoặc thông tin nội bộ trái phản hồi khách → ghi MT, không tự chọn bên |

## E. Quy trình thực hiện
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| 1 | Xác định sản phẩm, nhóm khách, mục tiêu chuyển đổi; đọc kho | RP, DV, UD, KH | Câu hỏi nghiên cứu + danh sách đơn vị | **DỪNG** chờ người dùng duyệt danh sách đơn vị và quyền đọc dữ liệu nội bộ |
| 2 | Thu mẫu quảng cáo, ghi MAU mỗi nguồn | Ads Library, Creative Center, Social | URL + ảnh chụp + ngày | Đủ phạm vi hoặc ghi giới hạn |
| 3 | Phân loại theo sản phẩm, khách, nhu cầu, góc, format | Mẫu | Ma trận góc (nháp) | Mọi mẫu có góc |
| 4 | Bóc Hook, lợi ích, bằng chứng, ưu đãi, CTA | Mẫu | Lô QC (+ UD cho ưu đãi mới) | QC đủ trường bắt buộc |
| 5 | Mở điểm đến nếu được phép; bóc section và các bước | Landing page, form, inbox tự động | LP Ma trận landing page + Bản đồ chuyển đổi | Không thực hiện giao dịch |
| 6 | Kiểm tra nhất quán quảng cáo – landing page – offer | QC, LP, UD | Trường `Nhất quán với điểm đến` | Mỗi cặp có kết luận Nhất quán / Lệch (nêu điểm lệch) |
| 7 | Đối chiếu phản hồi khách và dữ liệu chuyển đổi thật | KH, bình luận, số nội bộ | Rào cản có bằng chứng / giả thuyết | Ghi rõ loại căn cứ |
| 8 | Xác định góc khai thác nhiều vs ít xuất hiện trong mẫu | Ma trận góc | FIND (Nhóm Quảng cáo/Chuyển đổi) | Đếm có số mẫu/tổng |
| 9 | Lập giả thuyết quảng cáo và chuyển đổi cần thử, ghi kho `kho.py them lo-qc.json --dot RP-xxx` → `kiem-tra` | FIND, LP | GT (+ TH, MT) | Không LỖI; **DỪNG** trình kho góc + giả thuyết chờ duyệt |

## F. Đầu ra
| Mã | Nội dung | Trường bắt buộc (schema) |
| --- | --- | --- |
| `QC` | Thư viện quảng cáo | URL · Đơn vị · Sản phẩm · Thời gian · Format · Nội dung · Nguồn; nên điền Khách hàng, Nhu cầu, Góc tiếp cận, Hook, Lợi ích, Bằng chứng, Ưu đãi, CTA, Điểm đến, Nhất quán với điểm đến |
| `LP` | `Bảng` = Ma trận landing page (Section, Mục đích, Thông điệp, Bằng chứng, CTA) hoặc Bản đồ chuyển đổi (Hành động, Rào cản, Dữ liệu) | Bảng · Trang hoặc điểm chạm · Nội dung · Nguồn |
| `GT` | Giả thuyết thử nghiệm: biến thể ghi trong `Phương pháp kiểm chứng` | Giả thuyết · Bằng chứng ủng hộ · Bằng chứng phản bác · Phương pháp kiểm chứng · Chỉ số · Điều kiện kết luận |
| `UD`, `FIND`, `EVD`, `MAU` | Ưu đãi mới thấy; góc khai thác nhiều/ít; ảnh chụp; nhật ký mẫu | Theo schema |
**Bảng lọc** (không phải loại riêng): *Kho góc quảng cáo* và *Kho Hook quảng cáo* = `kho.py xuat --loai QC --ra nghien-cuu/<đợt>/xuat` rồi
dùng cột `Góc tiếp cận` / `Hook`; tra nhanh: `kho.py tim --loai QC --chu "<góc>"`. *Kho ưu đãi* = `kho.py xuat --loai UD QC` (cột `Ưu đãi`, `Combo`, `Giá`).
Ví dụ kiểm thử: `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/quang-cao-chuyen-doi.json`.

Ví dụ bản ghi (giả định):
```json
{"tam": "q1", "loai": "QC", "tieu_de": "Ads học thử Excel 0đ – nỗi sợ báo cáo cuối tháng", "lien_ket": ["@e1"],
 "do_tin_cay": "Cao", "ly_do_tin_cay": "Mở trực tiếp trên Ads Library, đã xem cả điểm đến",
 "du_lieu": {"URL": "https://www.facebook.com/ads/library/?id=vidu-201", "Đơn vị": "Trung tâm tin học A (ví dụ)", "Sản phẩm": "Khoá Excel cho người đi làm",
   "Thời gian": "Hiển thị từ 2026-10-05, còn chạy ngày 2026-11-26", "Format": "Video dọc 20 giây", "Nội dung": "Người đi làm ngồi muộn làm báo cáo, chuyển sang dùng hàm có sẵn",
   "Khách hàng": "Nhân viên văn phòng 22–30", "Nhu cầu": "Làm báo cáo nhanh", "Góc tiếp cận": "Nỗi đau ở lại muộn cuối tháng", "Hook": "Cuối tháng lại ngồi đến 9 giờ tối?",
   "Lợi ích": "Giảm thời gian làm báo cáo", "Bằng chứng": "Ảnh chụp màn hình nhận xét học viên", "Ưu đãi": "Học thử 1 buổi 0đ", "CTA": "Đăng ký học thử",
   "Điểm đến": "Landing page form 3 trường", "Nhất quán với điểm đến": "Lệch: trang không nhắc nội dung báo cáo cuối tháng", "Nguồn": "Meta Ads Library"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| `QC`, `LP`, `GT`, `UD`, `FIND`, `EVD`, `MAU` | `y-tuong-quang-cao` (góc, Hook, concept, biến thể), `toi-uu-chuyen-doi` (LP, rào cản, GT), `insight` (rào cản và phản hồi), `format-sang-tao` (bóc công thức video/hình quảng cáo) | Concept quảng cáo, định hướng landing page, FAQ/xử lý từ chối, kế hoạch A/B | Hạn dùng QC 60 ngày, LP 90 ngày; lần sau chạy `quet-doi-thu` để thấy ads mới/tắt rồi chỉ bóc phần mới; GT nhận `Kết quả thử nghiệm` sau khi chạy |

## H. Kiểm tra chất lượng
- [ ] Không có con số ngân sách, ROAS, CPA, doanh thu, hiệu quả ads của đối thủ; "chạy lâu" chỉ ghi là thời gian hiển thị.
- [ ] Mỗi QC có URL, ngày, nguồn; Hook nguyên văn; đã ghi `Nhất quán với điểm đến` khi mở được điểm đến.
- [ ] Không điền form, nhắn tin, đặt lịch, thanh toán thay người dùng.
- [ ] Điểm nghẽn chỉ từ dữ liệu công khai ghi là giả thuyết; khi có số nội bộ, ghi rõ kỳ và nguồn.
- [ ] Góc "ít xuất hiện" ghi kèm "trong mẫu N quảng cáo của M đơn vị", không gọi là khoảng trống thị trường.
- [ ] Mỗi GT có biến thể, chỉ số, điều kiện kết luận (ngưỡng, thời gian, cỡ mẫu tối thiểu).
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi QC/LP/GT ở trạng thái Chờ duyệt, người dùng có ma trận góc (nhiều/ít), bảng nhất quán ads – landing page – offer và danh sách giả thuyết cần thử.
