# Market Research năm review (Phần 2): ngành hàng, khách hàng, đơn vị cùng ngành

Mục tiêu: hiểu tình hình **năm review** (không dự báo năm sau ở đây). Đầu vào: `company-context.md` và Marketing Audit
(nếu đã có). Đầu ra: bảng Market Research gồm 3 tab + phần tổng hợp.

## 0. Phạm vi nghiên cứu (chốt trước khi tìm)
Ngành hàng · sản phẩm/dịch vụ trọng tâm · khu vực · nhóm khách cần tìm hiểu (nếu chưa rõ: đề xuất từ company-context rồi
**hỏi xác nhận**, không tự mặc định chân dung) · năm review · 3–5 câu hỏi doanh nghiệp muốn trả lời · nguồn sẽ dùng.

## 1. Ngành hàng: 6 nội dung
| Nội dung | Câu hỏi | Nguồn gợi ý |
| --- | --- | --- |
| Nhu cầu thị trường | Khách đang quan tâm, tìm kiếm, cần giải quyết vấn đề gì? | Google Search (gợi ý, "Mọi người cũng hỏi"), Google Trends, TikTok/YouTube Search |
| Sản phẩm/dịch vụ | Thị trường có những nhóm sản phẩm và cách cung cấp nào? | Website ngành, sàn TMĐT, báo chí |
| Phân khúc và giá | Các mức giá và giá trị cung cấp khác nhau ra sao? | Sàn TMĐT, website, bảng giá công khai |
| Mùa vụ | Thời điểm, dịp mua nào nhu cầu tăng? | Google Trends 12–24 tháng, lịch lễ/mùa |
| Kênh mua | Khách tìm hiểu và mua qua Google, Social, cửa hàng hay sàn? | Search, Social, sàn, báo cáo ngành |
| Thay đổi trong năm | Nhu cầu, sản phẩm, giá, cách mua có gì thay đổi? | Báo chí, hiệp hội, cơ quan quản lý, Trends |

Bảng: Góc độ · Phát hiện · Bằng chứng · Nguồn · Ngày · Loại · Tin cậy. Cuối: **5 phát hiện quan trọng nhất**.
Không tự tạo số quy mô thị trường, thị phần, doanh thu ngành.

## 2. Khách hàng: 6 nội dung
1. **Nhóm khách**: ai có nhu cầu với sản phẩm?
2. **Hoàn cảnh**: khi nào, vì sao họ bắt đầu tìm kiếm?
3. **Vấn đề**: họ muốn giải quyết khó khăn gì?
4. **Động lực mua**: điều gì khiến họ quyết định?
5. **Rào cản**: vì sao do dự, trì hoãn, từ chối hoặc chọn giải pháp khác?
6. **Tiêu chí lựa chọn**: giá, chất lượng, tiện lợi, uy tín, dịch vụ…?

Nguồn: Google Search (câu hỏi, từ khoá); Facebook Group (bài hỏi, thảo luận); bình luận TikTok/YouTube; Google Maps Reviews;
đánh giá Shopee/TikTok Shop; kết quả Inbox/bình luận/đánh giá nội bộ (skill `lead-hoi-thoai`, `ra-soat-thuong-hieu`).
Bảng: Nhóm khách · Hoàn cảnh · Vấn đề · Mong muốn · Động lực mua · Rào cản · Tiêu chí lựa chọn · Bằng chứng · Nguồn · Loại khách.
`Loại khách` = **Khách thực tế** (Inbox, đơn hàng của doanh nghiệp) hoặc **Quan sát công khai**.
Cuối: nhóm khách có nhu cầu rõ; vấn đề và mong muốn nhắc lại; yếu tố ảnh hưởng quyết định mua; nhu cầu chưa được đáp ứng tốt.
Ưu tiên lời nói cụ thể của khách (viết lại ngắn, ẩn danh). Không tự tạo chân dung hay insight từ dữ liệu ít ỏi.

## 3. Đơn vị cùng ngành: 6 nội dung
| Nội dung | Câu hỏi |
| --- | --- |
| Sản phẩm | Họ bán gì, có những dòng nào? |
| Khách hàng | Hướng đến nhóm khách nào? |
| Giá và ưu đãi | Giá bán, gói, khuyến mãi công khai? |
| Lợi ích và khác biệt | Họ thuyết phục khách bằng điều gì? |
| Marketing | Kênh nào, nội dung gì, quảng cáo ra sao? |
| Phản hồi khách | Khách khen, chê, phàn nàn điều gì? |

Cách chọn: 5–10 đơn vị (tối thiểu 3) theo ngành, sản phẩm, khu vực, phân khúc giá trong company-context.
Ghi **lý do chọn** và phân loại **Cạnh tranh trực tiếp** (cùng sản phẩm, cùng khách, cùng khu vực) hoặc
**Giải pháp thay thế** (khách có thể chọn để giải quyết cùng nhu cầu). Không khẳng định "trực tiếp" khi chưa có căn cứ.
Đơn vị đã có trong `cau-hinh.json → doi_thu`: dùng lại số mới nhất của `quet-doi-thu` (offer, khuyến mãi, ads) thay vì quét lại.
Nguồn: Google Search, Google Maps, Website/Landing page, Facebook, TikTok, Instagram, YouTube, Meta Ads Library, sàn TMĐT, Review.
Bảng: Đơn vị · Loại · Lý do chọn · Sản phẩm · Khách hàng · Giá & ưu đãi · Lợi ích/khác biệt · Kênh · Nội dung nổi bật · Quảng cáo · Phản hồi khách · Nguồn.
Không suy đoán doanh thu, thị phần, ngân sách; không kết luận đơn vị kinh doanh tốt chỉ dựa trên view/follower.

## 4. Tổng hợp Market Research
Đối chiếu 3 nhóm, trả lời:
1. Nhu cầu và vấn đề khách hàng.
2. Hành vi, động lực, tiêu chí mua.
3. Sản phẩm, phân khúc, mức giá.
4. Đơn vị cùng ngành đang làm gì; yếu tố họ dùng để thu hút khách.
5. Điểm khách chưa hài lòng (với mình và với thị trường).
6. Những thay đổi đã ghi nhận trong năm.
Mỗi phát hiện: bằng chứng, nguồn, ngày, **mức tin cậy**; tách phát hiện nhiều bằng chứng với giả thuyết.
Cuối: câu hỏi và tín hiệu cần theo dõi khi dự báo năm sau.

## Bảng đầu ra (`ket-qua.json`, loai `thi-truong`)
| Phần | csv / tab |
| --- | --- |
| 01. Ngành hàng | `mr-nganh-hang` / `MR – Ngành hàng` |
| 02. Khách hàng | `mr-khach-hang` / `MR – Khách hàng` |
| 03. Đơn vị cùng ngành | `mr-don-vi-cung-nganh` / `MR – Đơn vị cùng ngành` |
| 04. Tổng hợp | `mr-tong-hop` / `MR – Tổng hợp` (Phát hiện · Bằng chứng · Nguồn · Ngày · Loại · Tin cậy) |
