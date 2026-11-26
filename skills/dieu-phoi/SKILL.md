---
name: dieu-phoi
description: Bộ điều phối Agent Masterplan — đọc company-context.md và kết quả đã có trong thư mục làm việc, hiểu yêu cầu (review doanh nghiệp năm qua, nghiên cứu thị trường/khách hàng/đơn vị cùng ngành, dự báo xu hướng năm sau, xác định cơ hội và định hướng chiến lược, hoặc nghiên cứu tổng thể chuẩn bị Masterplan), chọn đúng skill, chạy theo thứ tự Review → Market Research → Dự báo → Định hướng, kiểm tra đầu ra từng bước trước khi chuyển bước và không chạy lại phần đã có kết quả còn dùng được. Dùng khi người dùng gõ /masterplan-agent:dieu-phoi, nói "chạy agent masterplan", "nghiên cứu tổng thể để chuẩn bị masterplan 2027", "đang tới đâu rồi", "bước tiếp theo là gì", hoặc yêu cầu một việc nghiên cứu Marketing mà chưa rõ skill nào.
argument-hint: "[yêu cầu, ví dụ: tổng thể 2027]"
---

# /masterplan-agent:dieu-phoi [yêu cầu]

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/bo-mau.md` (bộ mẫu 5 file là chuẩn đầu ra của từng giai đoạn).

## Bản đồ skill
| Phần | Skill | Đầu ra |
| --- | --- | --- |
| 0 · Chuẩn bị | `setup` | `cau-hinh.json`, `company-context.md` |
| 1 · Review doanh nghiệp | `danh-gia-kenh` · `lead-hoi-thoai` · `ra-soat-thuong-hieu` · `bao-cao-kinh-doanh` · `chi-phi-ads` → `review-nam` | Marketing Audit năm review |
| 2 · Market Research | `nghien-cuu-thi-truong` (dùng `quet-doi-thu` cho đơn vị cùng ngành đang theo dõi) | MR: ngành, khách hàng, đơn vị cùng ngành |
| 3 · Dự báo | `du-bao-xu-huong` | Tín hiệu + dự báo năm kế hoạch |
| 4 · Định hướng | `dinh-huong-chien-luoc` | Strategic Marketing Direction |
| Market Research theo đầu ra | `research` (điều phối 20 năng lực: thu thập 01–09, chuyển hoá 10–17, kiểm chứng, kho; 9 workflow; còn chế độ 3C) | Insight, cơ hội, sản phẩm/ưu đãi, thông điệp, ý tưởng Content/quảng cáo/chiến dịch, tối ưu chuyển đổi — có bằng chứng trong kho |
| Sau | Lập Masterplan, plan quý/tháng | (chưa có skill) |

| Người dùng nói | Chạy |
| --- | --- |
| "Review hoạt động năm nay", "marketing audit" | Phần 1 (skill thiếu trước, rồi `review-nam`) |
| "Kênh nào hiệu quả", "lead chất lượng không", "đã chi bao nhiêu ads" | Skill lẻ tương ứng của Phần 1 |
| "Nghiên cứu khách hàng / ngành / đơn vị cùng ngành" | `nghien-cuu-thi-truong` với phần tương ứng |
| "Dự báo xu hướng năm sau" | `du-bao-xu-huong` |
| "Nên tập trung cơ hội nào", "chọn hướng đi" | `dinh-huong-chien-luoc` |
| "Nghiên cứu tổng thể để chuẩn bị Masterplan" | Phần 1 → 4 theo thứ tự |
| "Tìm cơ hội dịp Tết", "vì sao khách chưa mua", "30 ý tưởng Content", "format video cho ngành", "góc quảng cáo mới", "ý tưởng combo", "kênh tiếp cận khách", "cập nhật thị trường tháng này", "insight này có căn cứ không" | `research` (tự chọn workflow 01–09, dùng lại kho và kết quả Audit/Market Research cùng kỳ) |
| "Kho nghiên cứu có gì", "ý tưởng này từ đâu ra" | `kho-du-lieu` |

## Bước 1 – Đọc trạng thái
1. Có `cau-hinh.json` và `company-context.md` chưa? Chưa → chạy `setup` trước.
2. Quét thư mục làm việc: `danh-gia-kenh/`, `lead-hoi-thoai/`, `thuong-hieu/`, `kinh-doanh/`, `chi-phi-ads/`, `doi-thu/`,
   `review/`, `thi-truong/`, `du-bao/`, `chien-luoc/`, `research-3c/`, `nghien-cuu/`, `kho/` (`kho.py thong-ke`). Mỗi mục: lần chạy mới nhất, kỳ dữ liệu, có `bao-cao.md` chưa.
3. Kết quả **còn dùng được** khi: cùng năm review/kế hoạch, kỳ phủ đủ (Review: ưu tiên cả năm), không quá 60 ngày
   (riêng `doi-thu` không quá 30 ngày). Nếu người dùng nói đã có thay đổi lớn thì coi là cũ.
4. Mẫu trống để người dùng tự điền: `xuat_bo_mau.py <mau> --nam <năm>` (không `--ket-qua`); bối cảnh dùng `templates/company-context-mau.md`.
5. Kiểm tra nguồn: Chrome, Meta Ads, TikTok Ads (connector hoặc Chrome), LadiPage, Google Drive, Google Sheets.

## Bước 2 – Trình kế hoạch chạy
Bảng: Phần · Skill · Trạng thái (Đã có / Cũ / Thiếu) · Việc sẽ làm · Nguồn cần. Ghi rõ phần chạy được ngay, phần cần người dùng chuẩn bị
(đăng nhập Chrome, file doanh thu, file chi phí khác).

DỪNG. Hỏi xác nhận trước khi chạy.

## Bước 3 – Chạy lần lượt
- Gọi từng skill theo đúng thứ tự; mỗi skill vẫn giữ các điểm DỪNG duyệt của nó.
- Trước khi chuyển phần: kiểm tra đầu ra phần trước có `ket-qua.json`/`bao-cao.md`, không còn CẢNH BÁO, đã được duyệt.
- Không chuyển sang dự báo khi chưa có Market Research; không xác định cơ hội khi chưa có dự báo và bằng chứng.
- Phần 2 có thể giao song song cho subagent (ngành, khách hàng, đơn vị cùng ngành) như hướng dẫn trong skill đó.

## Bước 4 – Báo cáo tổng
Khi chạy tổng thể: xuất đủ bộ mẫu (`xuat_bo_mau.py` cho đánh giá hiện trạng, nghiên cứu thị trường, dự báo và định hướng)
và tóm tắt 1 trang ở `tong-hop/<năm>_YYYY-MM-DD/bao-cao.md` gồm đường dẫn 4 báo cáo, kết luận chính mỗi phần,
câu định hướng chiến lược, giới hạn dữ liệu và việc cần kiểm chứng. Không tự lập Marketing Plan, phân bổ ngân sách hay chốt chiến dịch.

## Không được
- Tự gửi tin, đăng bài, sửa quảng cáo, đổi ngân sách, xoá dữ liệu trên nền tảng.
- Bỏ qua điểm DỪNG của skill con. Biến giả định thành dữ kiện.
- Chạy liên tục hoặc tự cập nhật khi không có yêu cầu; lịch định kỳ chỉ tạo khi người dùng đồng ý.
