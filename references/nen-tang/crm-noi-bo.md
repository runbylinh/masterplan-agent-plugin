# CRM, hộp thư và dữ liệu nội bộ

Gồm: CRM (LadiWork, Google Sheets, file xuất), hộp thư Messenger/Zalo/TikTok, dữ liệu đơn hàng, Meta Ads, TikTok Ads, GA4 qua connector.
Cách đọc từng hộp thư (bộ lọc, nhãn, thẻ Zalo, quy tắc chỉ đọc, mức lead, trạng thái, lý do không chốt): **xem `references/lead-hoi-thoai.md`**, không lặp lại ở đây.

## 1. Dùng cho
| Skill | Mục đích |
| --- | --- |
| company-analysis | Kết quả Marketing và bán hàng thực tế, danh sách vấn đề (DN) |
| customer-research | Nhu cầu, câu hỏi, lý do mua và từ chối của **khách thực tế** |
| insight, toi-uu-chuyen-doi | Đối chiếu Insight với hành vi mua; điểm nghẽn có dữ liệu |
| lead-hoi-thoai, bao-cao-kinh-doanh, chi-phi-ads | Dùng lại số đã có thay vì thu thập lại |

## 2. Công cụ truy cập (kiểm tra trước, chỉ đọc)
| Nguồn | Công cụ | Kiểm tra |
| --- | --- | --- |
| LadiPage / LadiWork | Connector: `report_leads_by_campaign`, `lw_list_deals`, `lw_report_deals`, `lw_report_lost_reasons` | ToolSearch tìm "LadiPage"/"lw_" |
| Meta Ads | Connector: `ads_get_ad_accounts`, `ads_get_ad_entities` | Đúng tài khoản trong `cau-hinh.json` |
| TikTok Ads, GA4 | Connector nếu có; không có thì file xuất người dùng để trong `nhap/` | Không giả định đã cài |
| Hộp thư | Claude in Chrome theo `lead-hoi-thoai.md` | Người dùng đăng nhập sẵn |
| File CRM, đơn hàng | `nhap/` (CSV, XLSX), Google Sheets connector | Hỏi người dùng đường dẫn |
Gặp đăng nhập, OTP, mã QR: nhờ người dùng tự làm. Không xin mật khẩu, không lưu khoá API vào kho hay repo.

## 3. Các bước
1. **Quyền và phạm vi**: hỏi người dùng nguồn nào được đọc, khoảng thời gian, cỡ mẫu hội thoại; ghi vào RP và MAU.
2. **Ẩn danh ngay khi đọc**: thay tên bằng mã (`HT-messenger-001`, `KH-don-014`); bỏ SĐT, email, địa chỉ, ảnh, link hồ sơ, số tài khoản.
3. **Chuẩn hoá**: nhóm khách (theo sản phẩm quan tâm, nguồn, khu vực), trạng thái bán và mức lead theo đúng mã trong `lead-hoi-thoai.md`.
4. **Trích nội dung**: nhu cầu, câu hỏi lặp, lý do mua, lý do từ chối (chọn 1 chính), câu nói tiêu biểu viết lại ngắn.
5. **Đối chiếu hành vi**: lead → hội thoại → đơn → doanh thu; khách nói "đắt" có thật sự không mua, hay mua gói thấp hơn.
6. **Phân tích theo lát cắt**: nhóm khách, sản phẩm, nguồn (quảng cáo, organic, giới thiệu), thời gian (tuần, tháng, mùa vụ).
7. **Rút Insight và điểm nghẽn**: điểm nghẽn ở đây có dữ liệu thực, ghi kèm tỷ lệ và cỡ mẫu.
8. **Lưu theo quy định bảo mật**: chỉ số tổng hợp và câu nói đã ẩn danh vào kho; file gốc giữ trong `nhap/` của workspace, không đưa lên GitHub.

## 4. Chọn mẫu (ví dụ giả định: Brand mẫu bán khoá học online)
| Lát cắt | Mẫu |
| --- | --- |
| Hội thoại Messenger 30 ngày | 40 hội thoại: 15 đã chốt, 15 mất, 10 đang tư vấn |
| Deal CRM | Toàn bộ deal 90 ngày, đọc lý do mất ở `lw_report_lost_reasons` |
| Quảng cáo | Chi phí, kết quả theo chiến dịch cùng kỳ (Meta Ads) |

## 5. Ghi vào kho
| Dữ liệu | Loại bản ghi / trường |
| --- | --- |
| Nguồn nội bộ, kỳ, điều quan sát | EVD: Nguồn ("LadiWork → Deals, lọc 01/09–30/11/2026"), Nền tảng, Ngày thu thập, Nội dung quan sát, Loại nguồn = Nội bộ |
| Phạm vi, cỡ mẫu, cách chọn | MAU: Nhóm khách hàng, Khoảng thời gian, Tiêu chí đưa vào/loại trừ, ba con số, Giới hạn của mẫu |
| Câu nói, lý do mua/từ chối | KH: Nhãn (Động lực, Rào cản, Câu hỏi…), Loại khách = Đã mua/Chưa mua/Khách cũ, Lý do, Giai đoạn mua |
| Kết quả bán, chi phí, vấn đề | DN: Bảng = Đánh giá Marketing / Danh sách vấn đề, Kết quả, Chi phí, Kỳ dữ liệu |
| Tỷ lệ theo giai đoạn | FIND: Phân loại = Dữ kiện, Nhóm = Chuyển đổi, Phạm vi |
| Điểm nghẽn, FAQ, xử lý từ chối | (qua `toi-uu-chuyen-doi`) CRO: Loại căn cứ = Nội bộ |

## 6. Giới hạn và điều cấm
- Không lưu tên, SĐT, email, địa chỉ, ảnh khách; `kho.py kiem-tra` báo lỗi nếu còn email/SĐT.
- Không gửi tin, gắn nhãn, đổi trạng thái deal, sửa chiến dịch quảng cáo.
- Mẫu hội thoại nhỏ không đại diện cả năm; ghi kỳ và cỡ mẫu.
- Chi phí quảng cáo / doanh thu **không phải ROAS** khi chưa quy doanh thu cho quảng cáo; không kết luận lợi nhuận khi thiếu giá vốn.
- Phân biệt khách thực tế (nguồn này) với người dùng quan sát công khai (các nền tảng khác).

## 7. Đầu ra chuyển hoá
KH → `customer-research` (SEG, HT), `insight`; DN → `company-analysis`; điểm nghẽn → `toi-uu-chuyen-doi`; số lead, chi phí → `lead-hoi-thoai`, `bao-cao-kinh-doanh`, `chi-phi-ads`.
