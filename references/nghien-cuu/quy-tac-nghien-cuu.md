# Quy tắc nghiên cứu: lấy mẫu, phân loại phát hiện, độ tin cậy, kiểm chứng

Áp dụng cho mọi skill nhóm A (thu thập), B (chuyển hoá), C (điều phối, kiểm chứng, kho). Đọc cùng `quy-tac.md`,
`quy-tac-bang-chung.md` và `kho-du-lieu.md`.

## 1. Tiêu chuẩn thu thập dữ liệu (ghi vào bản ghi MAU cho mỗi nguồn/lượt)
| Trường | Ghi gì |
| --- | --- |
| Phạm vi địa lý · Khoảng thời gian · Nhóm khách hàng | Đúng như Research Brief |
| Từ khóa · Phương pháp tìm kiếm | Từ khóa thực dùng, bộ lọc, cách sắp xếp, thời điểm tìm |
| Tiêu chí đưa vào · Tiêu chí loại trừ | Ví dụ "bình luận có nội dung về size/giá"; loại "spam, quảng cáo không liên quan, trùng" |
| Số bản ghi thu thập · đọc được · sử dụng (sau loại trùng) | Ba con số riêng |
| Nguồn không truy cập được | Tên + lý do (riêng tư, đăng nhập, CAPTCHA, bị chặn) |
| Giới hạn của mẫu | Thiên lệch nền tảng, khu vực, thời điểm, mẫu nhỏ |

**Phạm vi khởi tạo tham khảo** (nghiên cứu định tính, không phải mẫu đại diện thống kê, không bắt buộc):
| Hạng mục | Phạm vi khởi tạo |
| --- | --- |
| Đơn vị cùng ngành | 5–10 |
| Content | 30–50 |
| Quảng cáo | 20–30 mẫu |
| Review và bình luận | 50–100 bản ghi có ý nghĩa |
| Từ khóa | 30–50 cụm |
| Cộng đồng và Creator | 10–20 |
Điều chỉnh theo câu hỏi, độ đa dạng dữ liệu, quyền truy cập, thời gian. **Bão hoà**: khi 10–15 bản ghi liên tiếp không tạo nhóm phát hiện mới
và đã kiểm tra các nhóm dữ liệu còn thiếu (nhóm khách khác, nền tảng khác, phản hồi tiêu cực) thì có thể dừng; ghi `Mức bão hoà` vào MAU.
Quyết định lớn hoặc rủi ro cao (đổi định vị, ra sản phẩm, ngân sách lớn): yêu cầu thêm dữ liệu và kiểm chứng trực tiếp (khảo sát, phỏng vấn, thử nghiệm).
Số lượng mẫu không phải thước đo duy nhất của chất lượng.

**Lấy mẫu chống thiên lệch**: không chỉ lấy nội dung nổi bật. Với Content/quảng cáo lấy cả mức Nổi bật, Thông thường, Ít tương tác;
với review lấy cả tích cực, trung lập, tiêu cực; với khách lấy cả khách đã mua, chưa mua, chỉ tương tác.

## 2. Phân loại phát hiện (bắt buộc ghi)
| Loại | Định nghĩa | Nơi ghi |
| --- | --- | --- |
| Dữ kiện | Thông tin đã ghi nhận và xác minh trong phạm vi cụ thể | FIND `Phân loại = Dữ kiện` |
| Quan sát | Nội dung hoặc hành vi thực sự nhìn thấy (một hay vài lần) | FIND `Quan sát`, EVD |
| Mẫu lặp | Đặc điểm xuất hiện nhiều lần trong tập dữ liệu (ghi số lần / tổng) | FIND `Mẫu lặp` |
| Giả thuyết | Giải thích hoặc suy luận cần kiểm chứng | FIND `Giả thuyết`, GT |
| Insight | Hiểu biết về động lực, nhu cầu, mâu thuẫn có bằng chứng hỗ trợ | INS |
| Cơ hội | Khả năng khai thác Insight/khoảng trống phù hợp với doanh nghiệp | OPP |
| Ý tưởng | Phương án Marketing phát triển từ kết quả nghiên cứu | OFFER, TD, IDEA, FMT, ADS, CAM, CRO |
| Kết quả thử nghiệm | Dữ liệu thực tế sau khi triển khai kiểm chứng | GT `Kết quả thử nghiệm` |
Không tự động nâng Quan sát thành Insight, hay Ý tưởng thành kết luận đã xác nhận.

## 3. Độ tin cậy (luôn ghi `ly_do_tin_cay`)
| Mức | Khi nào |
| --- | --- |
| Cao | Nguồn phù hợp, trực tiếp, đáng tin; kiểm tra lại được; kết luận nằm trong phạm vi dữ liệu |
| Trung bình | Có bằng chứng liên quan nhưng mẫu, phạm vi hoặc khả năng đối chiếu còn hạn chế |
| Thấp | Dữ liệu gián tiếp, ít quan sát, chưa kiểm chứng đủ hoặc còn mâu thuẫn đáng kể |
| Chưa xác định | Không đủ dữ liệu để đánh giá |

## 4. Trạng thái kết luận (`kiem_chung`, do skill `kiem-chung` ghi kèm lý do)
`Có căn cứ` (≥ 2 nguồn độc lập cùng hướng, không có bằng chứng phản bác mạnh) · `Cần bổ sung` (mặc định) ·
`Chưa đủ căn cứ` · `Bị phản bác`. "Nguồn độc lập" = khác nền tảng hoặc khác tên miền, và không phải dẫn lại cùng một nguồn gốc
(ghi `Nguồn gốc dẫn lại` trong EVD khi biết).

## 5. Kiểm chứng xuyên suốt
Mỗi skill thu thập tự kiểm sau khi ghi kho: `kho.py kiem-tra --dot <RP>` (không còn LỖI) và tự hỏi 5 câu:
1. Nguồn có thực sự đã mở và đọc? (không kết luận từ tiêu đề/đoạn tóm tắt)
2. Thời gian, địa bàn, đơn vị đo có khớp phạm vi?
3. Có phải nhiều nguồn chỉ dẫn lại một nguồn gốc?
4. Có bằng chứng trái chiều không? Đã tìm chưa?
5. Kết luận có vượt quá dữ liệu không?
Gặp mâu thuẫn: ghi MT (Nguồn A, Nguồn B, điểm khác biệt, cách xử lý), không tự chọn một bên. Thiếu dữ liệu: ghi TH.

## 6. Những điều cấm (bổ sung cho `quy-tac-bang-chung.md`)
- Suy diễn lượng tìm kiếm từ lượt xem video, hashtag hay gợi ý từ khóa. Chỉ ghi chỉ số thực sự truy cập được (kèm đơn vị, địa bàn, thời gian).
- Coi chỉ số Google Trends 0–100 là lượng tìm kiếm tuyệt đối.
- Suy đoán ngân sách, ROAS, CPA, doanh thu, hiệu quả quảng cáo của đối thủ.
- Mô tả cảnh quay, hiệu ứng, âm thanh, bố cục chưa thực sự quan sát được.
- Khẳng định điểm nghẽn chuyển đổi thực tế khi chỉ có dữ liệu công khai/định tính (ghi "giả thuyết điểm nghẽn").
- Tự đề xuất giảm giá, cam kết lợi nhuận khi chưa có dữ liệu kinh tế.
- Gọi một nhu cầu chung chung hoặc một câu nói đơn lẻ là Insight đã xác nhận.
- Tạo hàng loạt ý tưởng chỉ khác tiêu đề.
- Lưu thông tin đăng nhập, API key, dữ liệu khách có thể nhận diện vào kho hay repo.

## 7. Công cụ: kiểm tra trước khi dùng
Trước khi thu thập, kiểm tra công cụ thực có trong phiên: WebSearch, Claude in Chrome (`tabs_context_mcp`), connector (Meta Ads,
TikTok for Business, LadiPage, Google Drive, Google Sheets, Notion), file người dùng đưa. Không giả định connector đã cài,
không tuyên bố đã đọc dữ liệu chưa truy cập được, không vượt giới hạn truy cập (CAPTCHA, đăng nhập, trang riêng tư → nhờ người dùng hoặc
dùng nguồn thay thế, ghi TH).
