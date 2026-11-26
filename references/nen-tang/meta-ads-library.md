# Meta Ads Library (Thư viện quảng cáo Meta)

## 1. Dùng cho
| Skill | Mục đích |
| --- | --- |
| quang-cao-chuyen-doi | Thư viện quảng cáo ngành: thông điệp, Hook, ưu đãi, format, CTA, điểm đến |
| competitor-research | Đơn vị cùng ngành đang chạy gì, từ khi nào, bao nhiêu phiên bản (đọc cùng `references/quet-doi-thu.md`) |
| format-sang-tao | Format quảng cáo hình ảnh/video lặp lại |

## 2. Công cụ truy cập
- Claude in Chrome: `tabs_context_mcp` → `navigate` `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=VN&q=<từ khóa>&search_type=keyword_unordered`.
- Connector Meta Ads (nếu phiên có `ads_library_search`): kiểm tra bằng ToolSearch trước; dùng để tìm theo từ khóa/Page, sau đó vẫn mở thư viện web để xem nội dung đầy đủ khi cần.
- `get_page_text` sau mỗi lần cuộn (danh sách tải dần); `find` "Xem chi tiết quảng cáo" rồi `computer` click để mở chi tiết; `computer` screenshot từng mẫu vào `bang-chung/`.
- Không cần đăng nhập để xem; gặp giới hạn truy cập thì dừng, nhờ người dùng, ghi TH.

## 3. Các bước
1. Xác định cách tìm: theo **từ khóa ngành** (sản phẩm, nhu cầu, ưu đãi phổ biến như "freeship", "mua 1 tặng 1") hoặc theo **nhà quảng cáo** (gõ tên Page, chọn đúng Page trong danh sách gợi ý).
2. Đặt **Quốc gia = Việt Nam**, **Danh mục = Tất cả quảng cáo**; bộ lọc thêm khi cần: Nền tảng (Facebook, Instagram, Messenger, Audience Network), Loại phương tiện (Hình ảnh, Video, Meme), Ngày hiển thị.
3. Thu mẫu truy cập được: 20–30 mẫu một đợt; lấy cả mẫu mới bắt đầu (< 7 ngày) và mẫu chạy lâu (> 30 ngày, thường là mẫu được giữ lại); với mỗi Page lấy tối đa 5 mẫu để tránh lệch.
4. Với mỗi mẫu ghi: **Library ID**, **"Bắt đầu chạy vào"**, trạng thái Đang hoạt động, nền tảng, số phiên bản ("N quảng cáo dùng nội dung và nội dung quảng cáo này"), tên Page.
5. Phân loại nội dung: sản phẩm, thông điệp chính, Hook (dòng đầu văn bản + khung đầu hình/video), lợi ích, bằng chứng, ưu đãi, format, CTA (nút).
6. Đọc **điểm đến** nếu truy cập được: mở link đích trong chi tiết, ghi tiêu đề trang, ưu đãi trên trang có khớp quảng cáo không (theo `website-landing-page.md`, không điền form).
7. So sánh: thông điệp/ưu đãi/format nào lặp giữa nhiều Page, góc tiếp cận nào chỉ một đơn vị dùng, mẫu nào chạy lâu.
8. Ghi giả thuyết quảng cáo (ví dụ "góc sợ mua nhầm size đang được 4/6 Page dùng"), không ghi là kết luận hiệu quả.

## 4. Xây từ khóa (ví dụ giả định: Brand mẫu bán khoá học kế toán online)
| Lớp | Ví dụ |
| --- | --- |
| Sản phẩm | "khoá học kế toán", "kế toán thuế" |
| Nhu cầu | "làm báo cáo thuế", "chuyển nghề kế toán" |
| Ưu đãi | "học thử miễn phí", "giảm 50% học phí" |
| Nhà quảng cáo | Tên Page của 5–8 đơn vị cùng ngành đã xác định ở competitor-research |

## 5. Ghi vào kho
| Dữ liệu | Loại bản ghi / trường |
| --- | --- |
| Link chi tiết quảng cáo, Library ID, ngày bắt đầu, ngày xem | EVD: Nguồn (URL có `id=<Library ID>`), Nền tảng = "Meta Ads Library", Ngày đăng = ngày bắt đầu chạy, Ngày thu thập, Nội dung quan sát, Loại nguồn = Công khai, Ảnh chụp |
| Từ khóa/Page, bộ lọc, số mẫu | MAU: Từ khóa, Phương pháp tìm kiếm ("VN, Tất cả quảng cáo, Đang hoạt động, 26/11/2026"), Tiêu chí đưa vào/loại trừ, ba con số, Giới hạn của mẫu |
| Nội dung quảng cáo | QC: URL, Đơn vị, Sản phẩm, Thời gian ("bắt đầu 12/11/2026, còn chạy 26/11"), Format, Nội dung, Hook, Lợi ích, Bằng chứng, Ưu đãi, CTA, Điểm đến, Nhất quán với điểm đến, Góc tiếp cận |
| Ưu đãi thấy trong quảng cáo | UD: Đơn vị, Sản phẩm, Giá, Combo, Chính sách, Thời gian |
| Mẫu lặp, góc tiếp cận | FIND: Nhóm = Quảng cáo, Phân loại = Mẫu lặp, Số lần xuất hiện |

## 6. Giới hạn và điều cấm
- Ở Việt Nam, thư viện chỉ hiển thị đủ quảng cáo thương mại **đang chạy**; quảng cáo thương mại đã dừng **không được lưu đầy đủ** (chỉ quảng cáo về vấn đề xã hội, bầu cử, chính trị được lưu dài hạn). Không kết luận "đơn vị X chưa từng chạy quảng cáo".
- Thư viện **không có ngân sách, lượt hiển thị, đối tượng** cho quảng cáo thương mại ở Việt Nam. Không suy đoán ngân sách, ROAS, CPA, hiệu quả.
- "Chạy lâu" hoặc "nhiều phiên bản" chỉ là tín hiệu để kiểm chứng, không chứng minh quảng cáo hiệu quả.
- Quảng cáo động (catalog) hiển thị nhiều biến thể; ghi đúng biến thể đã xem.
- Không bấm nút CTA thay khách để gửi form, không nhắn tin cho Page, không chép nguyên văn để dùng lại.

## 7. Đầu ra chuyển hoá
QC → `insight`, `y-tuong-quang-cao` (ADS), `format-sang-tao` (FMT); UD → `competitor-research` (KT), `san-pham-uu-dai`; điểm đến → `quang-cao-chuyen-doi` (LP).
