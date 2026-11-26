# TikTok Creative Center

## 1. Dùng cho
| Skill | Mục đích |
| --- | --- |
| quang-cao-chuyen-doi | Mẫu quảng cáo TikTok nổi bật theo ngành (thay cho thư viện quảng cáo không có ở Việt Nam) |
| format-sang-tao | Cấu trúc, cách thể hiện, CTA của quảng cáo video ngắn |
| xu-huong-mua-vu | Hashtag, bài hát, Creator, video đang lên theo thị trường |

## 2. Công cụ truy cập
- Claude in Chrome: `tabs_context_mcp` → `navigate` `https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/vi` (Top Ads) và `https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/vi` (Trend).
- Một số bộ lọc và trang chi tiết yêu cầu đăng nhập tài khoản TikTok for Business: nhờ người dùng đăng nhập; không có tài khoản thì ghi phần nào xem được, phần nào không (TH).
- `get_page_text`/`read_page` để đọc danh sách và chỉ số; mở video chi tiết, `computer` screenshot khung chính. Không tải video.
- Kiểm tra trước: nếu thị trường **Việt Nam** không có trong bộ lọc của mục đang xem, ghi rõ và chọn thị trường gần nhất kèm ghi chú (hoặc bỏ mục đó).

## 3. Các bước
1. Đặt **phạm vi**: Thị trường (Việt Nam nếu có), **Ngành** (ví dụ Làm đẹp & Chăm sóc cá nhân, Thực phẩm & Đồ uống, Giáo dục), **Mục tiêu chiến dịch** (Lưu lượng truy cập, Chuyển đổi, Doanh số sản phẩm…), **Khoảng thời gian** (7/30/180 ngày), Định dạng, Ngôn ngữ.
2. **Top Ads**: lướt danh sách, chọn 15–25 mẫu, gồm mẫu có chỉ số cao và mẫu ở giữa danh sách; mở chi tiết từng mẫu.
3. **Trend**: xem Hashtag, Bài hát, Creator, Video đang lên ở cùng thị trường và khoảng thời gian; ghi thứ hạng và nhãn "Mới vào bảng xếp hạng".
4. Với mỗi mẫu quảng cáo: Hook 3 giây đầu, cấu trúc theo đoạn (vấn đề → sản phẩm → bằng chứng → ưu đãi → CTA), cách thể hiện (người thật nói, cận sản phẩm, trước/sau, UGC), chữ trên video, CTA.
5. **Ghi rõ chỉ số nào nền tảng thực sự cung cấp** ở trang đó (ví dụ: lượt thích, CTR xếp hạng, ngân sách theo mức, "tỷ lệ xem 6 giây", điểm nóng tương tác theo giây). Chỉ số không hiển thị thì ghi "không có".
6. Rút nguyên lý sáng tạo lặp và đề xuất hướng thử nghiệm (ghi là giả thuyết).

## 4. Chọn mẫu (ví dụ giả định: Cửa hàng A bán đồ gia dụng nhà bếp)
| Bộ lọc | Giá trị |
| --- | --- |
| Ngành | Nhà cửa & Đời sống / Gia dụng |
| Mục tiêu | Doanh số sản phẩm và Chuyển đổi (chạy hai lượt riêng) |
| Thời gian | 30 ngày (hiện tại) và 180 ngày (so mẫu bền) |
| Trend | Hashtag ngành bếp, bài hát đang lên trong 7 ngày |

## 5. Ghi vào kho
| Dữ liệu | Loại bản ghi / trường |
| --- | --- |
| Link chi tiết mẫu, ngày xem, quan sát, ảnh chụp | EVD: Nguồn, Nền tảng = "TikTok Creative Center", Ngày thu thập, Nội dung quan sát, Loại nguồn = Công khai, Ảnh chụp, Ghi chú (chỉ số nền tảng cung cấp) |
| Bộ lọc, số mẫu | MAU: Phạm vi địa lý (thị trường), Khoảng thời gian, Phương pháp tìm kiếm (ngành, mục tiêu, định dạng), ba con số, Giới hạn của mẫu |
| Nội dung quảng cáo | QC: URL, Đơn vị (nếu hiển thị, không thì "không hiển thị"), Sản phẩm, Thời gian (khoảng lọc), Format, Nội dung, Hook, CTA |
| Hashtag, bài hát, video đang lên | XH: Phân loại = Ngắn hạn/Tín hiệu mới, Nền tảng = "TikTok", Nguồn |
| Nguyên lý sáng tạo | FMT: Loại format = Video, Công thức Hook, Cấu trúc, Trình tự phân đoạn và thời lượng, CTA, Mẫu tham khảo |

## 6. Giới hạn và điều cấm
- TikTok **không có thư viện quảng cáo công khai cho Việt Nam** (thư viện quảng cáo đầy đủ chỉ áp dụng EU). Creative Center chỉ là **mẫu do nền tảng chọn hiển thị**, không phải toàn bộ quảng cáo thị trường.
- Chỉ số trên Creative Center là chỉ số tương đối hoặc theo mức do nền tảng tính; không quy ra doanh thu, ROAS, ngân sách cụ thể của đơn vị chạy.
- Thứ hạng hashtag là mức sử dụng trên TikTok, không phải lượng tìm kiếm.
- Không mô tả âm thanh, hiệu ứng chưa thực sự xem/nghe; không sao chép nguyên kịch bản.

## 7. Đầu ra chuyển hoá
QC, FMT → `y-tuong-quang-cao` (ADS: concept, biến thể thử nghiệm), `format-sang-tao`; XH → `xu-huong-mua-vu`, `y-tuong-content`.
