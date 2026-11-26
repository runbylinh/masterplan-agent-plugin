# Dự báo xu hướng tiêu dùng năm kế hoạch (Phần 3)

Mục tiêu: kế thừa Marketing Audit + Market Research, kết hợp **những thay đổi có thể ảnh hưởng trực tiếp đến khách hàng
và ngành hàng**, để dự báo nhu cầu và hành vi năm kế hoạch. Không phân tích vĩ mô tràn lan, không chuyển thành Marketing Plan.

## Nguyên tắc chọn thông tin
Chỉ giữ thay đổi **giải thích được** tác động đến nhu cầu, sức mua, lựa chọn sản phẩm, hoặc cách khách tìm hiểu và mua hàng.
Ví dụ: lãi suất chỉ đáng xét nếu ngành bán sản phẩm giá trị cao cần vay/trả góp.

## 6 nhóm tín hiệu
| Nhóm | Nguồn tham khảo | Cần tìm |
| --- | --- | --- |
| Sức mua và chi tiêu | Cục Thống kê (nso.gov.vn), báo cáo bán lẻ, tin kinh tế | Khách có thắt chặt chi tiêu không? Nhóm hàng nào được ưu tiên? Độ nhạy giá thay đổi ra sao? |
| Giá và nguồn cung | Bộ Công Thương (moit.gov.vn), báo cáo ngành | Giá sản phẩm/nguyên liệu có thay đổi? Ảnh hưởng giá bán, gói, ưu đãi? |
| Chính sách liên quan ngành | Báo Chính phủ (baochinhphu.vn), bộ/ngành quản lý | Quy định mới về sản phẩm, quảng cáo, thuế, bán hàng, phân phối? |
| Thói quen và sở thích | Google Trends, TikTok Creative Center, Facebook Group | Khách bắt đầu quan tâm gì? Tiêu chí lựa chọn, cách tìm sản phẩm có đổi? |
| Sản phẩm và hành vi mua | Shopee, TikTok Shop, Lazada, đánh giá người mua | Khách ưu tiên sản phẩm, khoảng giá, trải nghiệm nào? Nhu cầu nào chưa được đáp ứng? |
| Nền tảng và công nghệ | Thông báo chính thức của Meta, TikTok, Google và nền tảng doanh nghiệp dùng | Cách tiếp cận, phân phối nội dung, quảng cáo, mua hàng có đổi? |
Thêm nhóm **Sự kiện** nếu có (lễ hội, sự kiện thể thao, mùa thi, chính sách theo mùa…) làm nhu cầu tăng/giảm/dịch chuyển.

## 5 bước
1. **Tóm tình hình hiện tại** từ Audit + Market Research (chỉ dùng tài liệu, không nghiên cứu lại): khách chính và nhu cầu;
   hành vi, tiêu chí, mức giá quan tâm; xu hướng sản phẩm đã ghi nhận; vấn đề chưa được đáp ứng; cơ hội và điểm cần lưu ý.
2. **Thu thập tín hiệu** (WebSearch chế độ extended + đọc nguồn gốc bằng Chrome): ưu tiên công bố trong năm review và thay đổi
   có hiệu lực/dự kiến trong năm kế hoạch. Mỗi tín hiệu ghi: điều gì đang đổi · thời điểm, nguồn công bố ·
   **Đã xảy ra / Đã có hiệu lực / Dự kiến** · nhóm khách/sản phẩm chịu ảnh hưởng · tác động Marketing có thể có.
3. **Kiểm tra phản ứng người tiêu dùng**: chỉ quay lại nguồn phù hợp với từng tín hiệu (không quét lại tất cả).
   Ví dụ sức mua chịu áp lực → Trends tìm kiếm sản phẩm giá thấp/thay thế có tăng? Social nhắc giá, ưu đãi nhiều hơn?
   Đánh giá trên sàn nói gì về giá trị nhận được? Market Research đã thấy dấu hiệu này chưa?
   Bảng: Yếu tố tác động · Phản ứng khách hàng · Bằng chứng + link · Nhận định · Điều cần kiểm chứng. Không khẳng định nhân quả.
4. **Dự báo**: mỗi dự báo gồm xu hướng hiện tại · yếu tố làm thay đổi · nhu cầu/hành vi tăng, giảm hay dịch chuyển ·
   nhóm khách chịu ảnh hưởng · tác động đến sản phẩm, giá, ưu đãi, thông điệp, kênh · cơ hội có thể xem xét ·
   mức tin cậy · dấu hiệu cần theo dõi. Phân loại: **Tiếp tục** · **Chững lại** · **Suy giảm** · **Xuất hiện mới** · **Chưa đủ căn cứ**.
5. **Phản biện** từng dự báo:
   bằng chứng có thật sự ủng hộ? nguồn đủ tin và đủ mới? có nhầm lượt quan tâm với nhu cầu mua?
   yếu tố nào khiến xu hướng không xảy ra hoặc đảo chiều? dữ liệu có lệch về một nền tảng/nhóm khách?
   dấu hiệu nào xác nhận hoặc bác bỏ? → chấm lại tin cậy; chưa đủ căn cứ thì ghi "Chưa đủ căn cứ", không cố kết luận.

## Bảng đầu ra (`ket-qua.json`, loai `du-bao`) — khớp mẫu "Dự báo xu hướng và định hướng marketing", tab Dự báo xu hướng
| Phần | `muc_mau` | Cột (đúng tên mẫu) | csv / tab Sheets |
| --- | --- | --- | --- |
| Tín hiệu và phản ứng | `Dự báo xu hướng/Tín hiệu và phản ứng quan sát được` | Thay đổi có thể tác động · Nhóm khách · Phản ứng đã quan sát · Nguồn và thời điểm · Thông tin cần kiểm chứng (+ `Nhóm tín hiệu`, `Trạng thái`, `Tin cậy` cho báo cáo) | `db-tin-hieu` / `DB – Tín hiệu` |
| Kiểm tra tín hiệu (phụ) | `Kiểm tra tín hiệu` | Thay đổi cần theo dõi · Nhóm khách · Nguồn và ngày · Phản ứng đã quan sát · Bằng chứng đối chiếu · Điều còn thiếu · Kết luận để đưa vào dự báo | `db-kiem-tra` / `DB – Kiểm tra tín hiệu` |
| Dự báo và phương án ứng phó | `Dự báo xu hướng/Dự báo, tác động và phương án ứng phó` | Xu hướng hiện tại · Yếu tố tác động · Bằng chứng · Dự báo và kỳ dự kiến · Nhóm khách chịu ảnh hưởng · Tác động và cơ hội marketing · Mức tin cậy và lý do · Dấu hiệu để triển khai phương án · Phương án thực hiện khi xuất hiện tín hiệu | `db-du-bao` / `DB – Dự báo` |

- **Bằng chứng đối chiếu** gồm cả nguồn **khác chiều** (không ủng hộ dự báo) nếu có.
- **Dự báo và kỳ dự kiến**: Tiếp tục / Chững lại / Suy giảm / Xuất hiện mới / Chưa đủ căn cứ + khoảng thời gian (ví dụ "Quý II–III").
- **Mức tin cậy và lý do**: bắt đầu bằng Cao / Trung bình / Thấp rồi lý do ngắn.
- **Dấu hiệu để triển khai phương án** + **Phương án thực hiện khi xuất hiện tín hiệu**: khi thấy dấu hiệu X (đo được, nguồn nào)
  thì làm gì ở mức hướng xử lý (đổi gói, đẩy kênh, đổi thông điệp…), không lập chiến dịch chi tiết.
Không gán xác suất chính xác, không dự báo doanh thu khi không có dữ liệu và phương pháp phù hợp.
