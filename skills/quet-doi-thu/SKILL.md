---
name: quet-doi-thu
description: Tự quét và phân tích các kênh của đối thủ để nắm nội dung, offer (sản phẩm, giá, gói, quà), chương trình khuyến mãi và quảng cáo đang chạy (Meta Ads Library, TikTok, Google Ads Transparency, landing page) bằng Claude in Chrome; lưu ảnh chụp mỗi lần quét để so "đối thủ có gì mới" (offer mới, khuyến mãi mới, ads mới, ads đã tắt); xuất báo cáo .md + HTML + Google Sheets. Có thể hẹn giờ quét định kỳ. Dùng khi người dùng gõ /masterplan-agent:quet-doi-thu, nói "quét đối thủ", "đối thủ đang chạy khuyến mãi gì", "đối thủ đang chạy ads gì", "theo dõi đối thủ", "tuần này đối thủ có gì mới".
argument-hint: "[tên đối thủ | tất cả]"
---

# /masterplan-agent:quet-doi-thu [đối thủ]

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quet-doi-thu.md`.
Cần `cau-hinh.json` mục `doi_thu`. Trống thì đề xuất 3–5 đối thủ (có lý do), chờ duyệt, rồi ghi vào cấu hình.

Skill này để **theo dõi đều đặn** nội dung, offer, khuyến mãi, ads. Muốn nghiên cứu sâu 3C (khách hàng, định vị, cơ hội)
thì dùng `/masterplan-agent:research` (3C theo chủ đề) hoặc `/masterplan-agent:nghien-cuu-thi-truong` (Market Research năm).

## Bước 0 – Chốt phạm vi
1. Đối thủ (mặc định tất cả trong cấu hình) và kênh của từng đối thủ: Facebook Page, TikTok, Instagram, YouTube,
   website/landing page, Shopee/TikTok Shop nếu có.
2. Khoảng nhìn lại cho nội dung: mặc định 30 ngày gần nhất (tối đa 20 bài mỗi kênh).
3. Đọc lần quét gần nhất trong `doi-thu/lich-su/` (nếu có) để biết đang so với ngày nào.
4. Tạo `doi-thu/YYYY-MM-DD/`.

## Bước 1 – Quét từng đối thủ (Claude in Chrome, chỉ đọc)
Theo `references/quet-doi-thu.md`, mỗi đối thủ ghi:
- **Nội dung**: bài trong khoảng nhìn lại — ngày, định dạng, chủ đề, hook (câu mở đầu, viết lại ngắn, không chép nguyên),
  số công khai (view, thích, bình luận, chia sẻ). Rút ra chủ đề/định dạng chủ lực và tần suất.
- **Offer**: sản phẩm/gói, giá niêm yết, giá ưu đãi, quà tặng, bảo hành/cam kết, điều kiện; nơi thấy (URL).
- **Khuyến mãi**: tên chương trình, mức giảm, thời gian bắt đầu–kết thúc (nếu ghi), điều kiện, kênh.
- **Quảng cáo**: Meta Ads Library (lọc Việt Nam, tất cả quảng cáo, đúng Page): số mẫu đang chạy, ngày bắt đầu,
  định dạng, thông điệp chính, CTA, link đích; mã thư viện (Library ID) để theo dõi. Google Ads Transparency nếu có website.
  TikTok: ghi bài có nhãn "Được tài trợ"/"Quảng cáo" thấy được; không có thư viện công khai cho Việt Nam thì ghi rõ.
- Chụp màn hình offer/khuyến mãi/ads tiêu biểu vào `bang-chung/YYYY-MM-DD_<doi-thu>_<noi-dung>.png`.
- Ghi `nguon` (URL + ngày) cho từng mục; không thấy thì ghi "không thấy" chứ không đoán.

Ghi `doi-thu/YYYY-MM-DD/quet.json` (định dạng ở `references/quet-doi-thu.md`).

## Bước 2 – So với lần trước và dựng báo cáo
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/so_sanh_doi_thu.py doi-thu/YYYY-MM-DD
```
Script tự tìm lần quét gần nhất trước đó, ghi `thay-doi.json`, `bao-cao.html`, `sheets/*.csv`,
và chép `quet.json` vào `doi-thu/lich-su/YYYY-MM-DD.json`.
Đọc kết quả, viết `nhan-dinh.json` (`tom_tat`, `doi_thu`: {tên: nhận xét}, `goi_y_cho_minh`: [...]), chạy lại script,
rồi viết `bao-cao.md`:
- Mỗi đối thủ: đang đẩy gì (sản phẩm, thông điệp), offer/khuyến mãi hiện tại, ads đang chạy, nội dung chủ lực.
- **Có gì mới từ lần trước**: offer mới/đổi giá, khuyến mãi mới/kết thúc, ads mới/đã tắt, chủ đề mới.
- Bảng so offer và giá giữa các đối thủ (và của mình nếu `cau-hinh.json` có).
- Gợi ý cho mình: khoảng trống, mùa khuyến mãi đối thủ hay chạy, thông điệp nên tránh trùng. Không gợi ý giảm giá theo.

DỪNG. Báo cáo 5 dòng, hỏi duyệt. Sau duyệt ghi Google Sheets tab `Đối thủ – Offer & Ads` (append, `Chờ duyệt`).

## Bước 3 – Theo dõi định kỳ (chỉ khi người dùng muốn)
Hỏi người dùng có muốn hẹn quét tự động không (ví dụ thứ Hai 8:00 hằng tuần). Đồng ý thì tạo lịch bằng
công cụ hẹn giờ (scheduled task) với lệnh `/masterplan-agent:quet-doi-thu tất cả` chạy trong đúng thư mục làm việc.
Nhắc: lịch chạy trên máy này, cần máy mở và Chrome đăng nhập.

## Không được
- Bình luận, nhắn tin, theo dõi, bấm quảng cáo hay điền form của đối thủ.
- Suy đoán ngân sách, doanh thu đối thủ. Chép nguyên văn bài/kịch bản của đối thủ vào báo cáo.
