# Hướng dẫn theo nền tảng

Mỗi file mô tả cách thu thập trên một nền tảng: dùng cho skill nào, công cụ truy cập, các bước, cách chọn từ khóa/mẫu,
dữ liệu ghi vào loại bản ghi nào trong kho, giới hạn và điều cấm, đầu ra chuyển hoá.
Đọc cùng `../kho-du-lieu.md`, `../nghien-cuu/quy-tac-nghien-cuu.md`, `../quy-tac-bang-chung.md`.

## Bảng tra cứu
| Nền tảng | File | Dùng cho skill | Loại bản ghi tạo ra |
| --- | --- | --- | --- |
| Google Search | `google-search.md` | company-analysis, xu-huong-mua-vu, customer-research, tu-khoa, competitor-research, insight | EVD, MAU, FIND, KEY, KH, TT, XH, MV, RR |
| Google Trends | `google-trends.md` | xu-huong-mua-vu, tu-khoa, marketing-opportunities | EVD, MAU, MV, BD, XH, KEY |
| TikTok | `tiktok.md` | nghien-cuu-content, format-sang-tao, customer-research, tu-khoa, kenh-cong-dong, competitor-research | EVD, MAU, CNT, KH, KEY, KEN, FIND |
| Facebook | `facebook.md` | customer-research, nghien-cuu-content, competitor-research, kenh-cong-dong | EVD, MAU, KH, CNT, KEN, FIND |
| Threads | `threads.md` | customer-research, xu-huong-mua-vu, insight, nghien-cuu-content | EVD, MAU, KH, FIND, XH |
| YouTube | `youtube.md` | nghien-cuu-content, format-sang-tao, customer-research, tu-khoa, kenh-cong-dong | EVD, MAU, CNT, KH, KEY, KEN |
| Instagram | `instagram.md` | format-sang-tao, nghien-cuu-content, kenh-cong-dong, customer-research | EVD, MAU, CNT, FMT, KH, KEN |
| Meta Ads Library | `meta-ads-library.md` | quang-cao-chuyen-doi, competitor-research, format-sang-tao | EVD, MAU, QC, UD, FIND |
| TikTok Creative Center | `tiktok-creative-center.md` | quang-cao-chuyen-doi, format-sang-tao, xu-huong-mua-vu | EVD, MAU, QC, XH, FMT |
| Google Maps | `google-maps.md` | customer-research, competitor-research, company-analysis, xu-huong-mua-vu | EVD, MAU, KH, DV, FIND |
| Website / landing page | `website-landing-page.md` | quang-cao-chuyen-doi, competitor-research, company-analysis, toi-uu-chuyen-doi | EVD, MAU, LP, UD, TN, DV |
| Sàn TMĐT (Shopee, TikTok Shop, Lazada) | `san-tmdt.md` | customer-research, competitor-research, san-pham-uu-dai, tu-khoa | EVD, MAU, KH, UD, DV, KEY, FIND |
| CRM, hộp thư, dữ liệu nội bộ, Ads/GA4 qua connector | `crm-noi-bo.md` | company-analysis, customer-research, insight, toi-uu-chuyen-doi, lead-hoi-thoai, bao-cao-kinh-doanh, chi-phi-ads | EVD (Nội bộ), MAU, KH, DN, FIND |

## Quy tắc chung cho mọi nền tảng
1. Kiểm tra công cụ trước (WebSearch, Claude in Chrome `tabs_context_mcp`, connector); không giả định đã có.
2. Mỗi lượt thu thập có **một MAU**; mỗi nguồn đã mở và đọc có **một EVD** (Nguồn, Nền tảng, Ngày thu thập, Nội dung quan sát, Loại nguồn).
3. Lấy mẫu chống thiên lệch: nhiều mức tương tác, nhiều thời điểm đăng, cả phản hồi tích cực, trung lập, tiêu cực.
4. Chỉ đọc: không thích, bình luận, theo dõi, nhắn tin, điền form, thêm giỏ, thanh toán.
5. Đăng nhập, CAPTCHA, trang riêng tư: nhờ người dùng hoặc ghi TH; không vượt giới hạn.
6. Ẩn danh mọi người dùng, người bình luận, khách hàng; ví dụ trong tài liệu chỉ dùng tên giả định.
7. Không suy lượng tìm kiếm từ lượt xem/hashtag; không suy ngân sách, doanh thu, hiệu quả quảng cáo của đơn vị khác.
8. Ghi kho bằng `kho.py them` có mã đợt, rồi `kho.py kiem-tra --dot <RP>`.
