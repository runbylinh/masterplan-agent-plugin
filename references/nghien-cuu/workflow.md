# Workflow nghiên cứu theo mục tiêu đầu ra

Skill `research` (điều phối) đọc file này để chọn workflow, mức nghiên cứu và skill. Người dùng không cần biết tên skill.
**Xác định đầu ra trước khi chạy, không mở rộng sang nhánh không cần thiết.**

## 1. Ba mức nghiên cứu
| Mức | Khi nào | Cách làm |
| --- | --- | --- |
| Nhanh | Một câu hỏi hoặc một đầu ra cụ thể; cần trong phiên | Ưu tiên kho và dữ liệu sẵn có; thu thập bổ sung tối thiểu; 1 điểm duyệt cuối |
| Chuyên sâu | Phục vụ chiến lược, chiến dịch lớn, nhiều đầu ra | Nhiều nhóm A song song (subagent), kiểm chứng giữa các bước, điểm duyệt sau Brief, sau Insight/cơ hội, sau tài nguyên |
| Cập nhật | Đã có đợt trước; theo tuần/tháng/quý | Kế thừa kho, chỉ thu thập phần lỗi thời hoặc còn thiếu, so sánh cùng phạm vi, báo cáo thay đổi (`kho.py thay-doi`) |

## 2. Chín workflow
| # | Workflow | Chuỗi skill (→ là chuyển giao qua kho) | Đầu ra cuối |
| --- | --- | --- | --- |
| 01 | Nghiên cứu toàn diện phục vụ chiến lược | company-analysis → xu-huong-mua-vu → customer-research → competitor-research → (tu-khoa, nghien-cuu-content, kenh-cong-dong khi cần) → kiem-chung → insight → marketing-opportunities → dinh-vi-thong-diep → kho | Bộ dữ liệu cho chiến lược và Masterplan (chuyển cho `nghien-cuu-thi-truong`, `du-bao-xu-huong`, `dinh-huong-chien-luoc`) |
| 02 | Chiến dịch theo mùa vụ | (mục tiêu kinh doanh) → xu-huong-mua-vu → customer-research → competitor-research → insight → marketing-opportunities → san-pham-uu-dai → y-tuong-chien-dich → y-tuong-content, y-tuong-quang-cao | Bản đồ cơ hội + kho ý tưởng chiến dịch theo thời điểm |
| 03 | Content Marketing | customer-research → tu-khoa → xu-huong-mua-vu → nghien-cuu-content → format-sang-tao → insight → y-tuong-content | Content Pillar, chủ đề, ý tưởng, Hook, format |
| 04 | Quảng cáo | company-analysis (sản phẩm) → customer-research (động lực, rào cản) → competitor-research → quang-cao-chuyen-doi → insight → y-tuong-quang-cao | Kho góc quảng cáo, concept, biến thể thử nghiệm |
| 05 | Phát triển sản phẩm | company-analysis → customer-research → xu-huong-mua-vu → competitor-research (cả giải pháp thay thế) → marketing-opportunities → san-pham-uu-dai → kiem-chung | Phương án sản phẩm, combo, ưu đãi có căn cứ |
| 06 | Tối ưu chuyển đổi | company-analysis (CRM, dữ liệu Marketing; dùng lại `lead-hoi-thoai`) → customer-research (hành trình, rào cản) → quang-cao-chuyen-doi (ads, landing page) → toi-uu-chuyen-doi | Kho rào cản, FAQ, xử lý từ chối, thử nghiệm |
| 07 | Phát triển kênh | customer-research (chân dung) → tu-khoa (hành vi tìm kiếm) → kenh-cong-dong → nghien-cuu-content | Bản đồ kênh, kho cơ hội phân phối |
| 08 | Cập nhật thị trường | kho-du-lieu (đọc cũ, liệt kê lỗi thời) → các skill nhóm A cần cập nhật (cùng phạm vi) → kiem-chung → cập nhật XH, INS, OPP, tài nguyên | Báo cáo thay đổi theo tuần/tháng/giai đoạn |
| 09 | Kiểm chứng Insight và ý tưởng | kiem-chung (câu hỏi kiểm chứng → bằng chứng ủng hộ và phản bác → độ tin cậy) | Bảng kiểm chứng + đề xuất giữ / sửa / loại / thử nghiệm |
Chế độ **3C** cũ (`/masterplan-agent:research <chủ đề>` 5 giai đoạn, file `01-brief.md` … `05-giao-viec.md`) vẫn giữ nguyên;
mỗi giai đoạn 3C ghi thêm vào kho.

## 3. Bảng định tuyến yêu cầu tự nhiên
| Người dùng nói | Workflow | Mức | Đầu ra |
| --- | --- | --- | --- |
| "Tìm cơ hội Marketing dịp Tết" | 02 | Chuyên sâu | Bản đồ cơ hội + ý tưởng chiến dịch Tết |
| "Tìm nguyên nhân khách chưa mua" | 06 | Nhanh/Chuyên sâu | Kho rào cản + giả thuyết điểm nghẽn + thử nghiệm |
| "Tìm Insight khách hàng" | 03 (dừng ở insight) + kiem-chung | Chuyên sâu | Kho Insight có bằng chứng |
| "30 ý tưởng Content dựa trên nghiên cứu" | 03 (dùng kho nếu đã có) | Nhanh nếu kho đủ | Kho ý tưởng Content đa nền tảng |
| "10 format video phù hợp ngành hàng" | nghien-cuu-content → format-sang-tao | Nhanh | Thư viện format video |
| "Nghiên cứu quảng cáo, đề xuất góc mới" | 04 | Chuyên sâu | Kho góc quảng cáo, concept |
| "Ý tưởng combo sản phẩm" | 05 | Nhanh/Chuyên sâu | Đề xuất combo, ưu đãi cần thử nghiệm |
| "Tối ưu landing page" | 06 | Nhanh | Định hướng landing page |
| "Tìm kênh tiếp cận khách hàng" | 07 | Chuyên sâu | Bản đồ kênh, cộng đồng, Creator |
| "Xây đầu vào Masterplan" | 01 | Chuyên sâu | Bộ dữ liệu chiến lược |
| "Cập nhật thị trường tháng này" | 08 | Cập nhật | Báo cáo thay đổi + cơ hội mới |
| "Ý tưởng này có căn cứ không?" | 09 | Nhanh | Bảng kiểm chứng |

## 4. Subagent (giao song song khi Mức = Chuyên sâu)
| Subagent | Nhóm việc | Skill nó làm theo |
| --- | --- | --- |
| `market-researcher` | Thị trường, xu hướng, mùa vụ, từ khóa, kênh/cộng đồng/Creator | xu-huong-mua-vu, tu-khoa, kenh-cong-dong |
| `customer-researcher` | Khách hàng và hành vi mua | customer-research |
| `competitor-researcher` | Cạnh tranh, quảng cáo và hành trình chuyển đổi của thị trường | competitor-research, quang-cao-chuyen-doi |
| `content-researcher` | Content đa nền tảng, format hình ảnh/video | nghien-cuu-content, format-sang-tao |
| `research-verifier` | Kiểm chứng độc lập (không nhận lập luận của agent chính) | kiem-chung |
Mỗi subagent nhận: mã RP, đường dẫn kho, phần Research Brief của nó, danh sách nguồn được phép, giới hạn mẫu. Subagent ghi vào kho
bằng `kho.py them` (có `--dot`), không hỏi người dùng, trả tóm tắt ≤ 10 dòng. Skill chuyển hoá (nhóm B) do agent chính chạy sau khi
đã có dữ liệu và kiểm chứng.

## 5. Tiếp tục khi phiên bị gián đoạn
- Research Brief (RP) có trường `Tiến độ`: sau mỗi bước, agent cập nhật (`kho.py cap-nhat RP-xxx`) dòng "Bước n xong: ...".
- Mở phiên mới: `kho.py tim --loai RP` → chọn đợt → `kho.py tien-do --dot RP-xxx` → làm tiếp từ bước chưa xong, không thu thập lại.
- Thư mục đợt `nghien-cuu/<YYYY-MM-DD>-<chủ-đề>/` giữ `brief.md`, các lô `lo-*.json` đã nạp, báo cáo.
