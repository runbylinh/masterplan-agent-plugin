---
name: danh-gia-kenh
description: Đánh giá hiệu quả các kênh social của doanh nghiệp (Facebook Page, Facebook Group, TikTok, Instagram, Threads, YouTube, Zalo OA) theo khung Phễu + vai trò kênh, so kỳ trước và so đối thủ bằng số công khai, kết luận Giữ / Đẩy mạnh / Tối ưu / Bỏ có lý do, xuất báo cáo .md + HTML và bảng Google Sheets. Tự lấy số qua Claude in Chrome (Business Suite, TikTok Studio, trang công khai), file xuất trong nhap/, connector Meta Ads và LadiPage. Dùng khi người dùng gõ /masterplan-agent:danh-gia-kenh, nói "đánh giá kênh", "kênh nào hiệu quả", "audit fanpage/tiktok", "nên bỏ kênh nào", "so kênh với đối thủ".
argument-hint: "[kỳ: 30 | 90 | 180 ngày, hoặc từ YYYY-MM-DD đến YYYY-MM-DD]"
---

# /masterplan-agent:danh-gia-kenh [kỳ]

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/khung-danh-gia.md`,
`${CLAUDE_PLUGIN_ROOT}/references/thu-thap.md`.
Thư mục làm việc = thư mục người dùng đang mở. Cần `cau-hinh.json`; chưa có thì chạy skill `masterplan-agent:setup` trước.

## Bước 0 – Chốt phạm vi (hỏi một lần, ngắn)
1. Đọc `cau-hinh.json`. Liệt kê kênh của mình + vai trò, đối thủ. Kênh nào thiếu link hoặc vai trò thì hỏi.
2. **Kỳ**: lấy từ tham số; không có thì hỏi 30 / 90 / 180 ngày (hoặc khoảng ngày cụ thể).
   Kỳ kết thúc hôm qua. Kỳ trước = cùng độ dài, liền trước.
3. **Đối thủ**: nếu `doi_thu` trống, đề xuất 3–5 đối thủ (tìm trên TikTok/Facebook theo ngành, khu vực trong cấu hình),
   ghi lý do chọn, chờ người dùng duyệt. Không tự thêm vào cấu hình khi chưa được duyệt.
4. **Nguồn sẵn sàng**: kiểm tra Claude in Chrome (`tabs_context_mcp`), connector Meta Ads, LadiPage, file trong `nhap/`.
   Nói rõ nguồn nào có, nguồn nào thiếu và ảnh hưởng gì. Nhờ người dùng đăng nhập sẵn Business Suite, TikTok Studio,
   YouTube Studio, Zalo OA trên Chrome nếu cần.
5. Tạo thư mục `danh-gia-kenh/YYYY-MM-DD_<so-ngay>d/` (ngày chạy) và `bang-chung/` nếu chưa có.

DỪNG. Tóm tắt phạm vi (kỳ, kênh, đối thủ, nguồn) và hỏi "Bắt đầu lấy số chứ?"

## Bước 1 – Lấy số kênh của mình
Theo `thu-thap.md`, lần lượt từng kênh, cả kỳ này và kỳ trước:
- File trong `nhap/` trước: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/doc_file_xuat.py <file> --nen-tang <nen_tang> --tu <ngày> --den <ngày>`
  ra danh sách bài + tổng, dán vào kênh tương ứng.
- Thiếu thì đọc qua Chrome (trang quản trị, chỉ đọc). Chụp màn hình bảng số chính vào `bang-chung/`.
- Chi phí ads: connector Meta Ads. Lead: LadiPage `report_leads_by_campaign`, chia theo `lead.utm_source_theo_kenh`.
- Mỗi kênh ghi `nguon` (nơi lấy, ngày lấy) và `thieu` (chỉ số không lấy được + lý do).

## Bước 2 – Lấy số công khai của đối thủ
Mỗi kênh đối thủ cùng nền tảng với kênh của mình: follower, các bài trong kỳ (tối đa 20 bài gần nhất)
với ngày đăng, lượt xem nếu hiển thị, thích, bình luận, chia sẻ. Ghi `cua = "doi_thu"`, `doi_thu = <tên>`.
Đồng thời bổ sung số công khai từng bài cho kênh của mình (để so cùng thước đo).

Ghi tất cả vào `so-lieu.json` đúng định dạng trong `thu-thap.md`. Số nào không có để `null`.

## Bước 3 – Tính chỉ số
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tinh_chi_so.py danh-gia-kenh/<kỳ>/so-lieu.json
```
Ra `chi-so.json`: chỉ số từng kênh, so kỳ trước, trung vị đối thủ, chấm tiêu chí, kết luận sơ bộ.
Script lỗi hoặc số trông vô lý (ER > 100%, reach âm) thì kiểm lại `so-lieu.json`, không sửa số cho đẹp.

## Bước 4 – Nhận định
Đọc `chi-so.json` cùng `cau-hinh.json` (mục tiêu, nguồn lực), trả lời đủ 5 câu cho mỗi kênh và phần toàn hệ kênh
(`khung-danh-gia.md` mục 5–6). Ghi `nhan-dinh.json`:
```json
{
  "tom_tat": "3–4 câu: kênh nào gánh, kênh nào hụt, phễu hở ở đâu",
  "pheu": "Nhận xét toàn hệ kênh theo phễu",
  "khoang_trong_doi_thu": "Đối thủ mạnh ở đâu mà mình đang bỏ trống",
  "uu_tien": ["Ưu tiên 1", "Ưu tiên 2", "Ưu tiên 3"],
  "kenh": {
    "<id kênh>": {
      "ket_luan": "Đẩy mạnh | Giữ | Tối ưu | Bỏ / tạm dừng | Chưa đủ dữ liệu",
      "doi_tu": "kết luận sơ bộ nếu đã đổi, không đổi thì null",
      "ly_do": "1–2 câu có số",
      "noi_dung_thang": "định dạng, chủ đề, kiểu hook chạy tốt; cái nên bỏ",
      "viec_tiep": ["việc 1", "việc 2"]
    }
  }
}
```
Lý do luôn kèm số (ví dụ "reach giảm 32% trong khi tần suất giữ nguyên"). Việc kỳ tới làm được với nguồn lực hiện có.

## Bước 5 – Báo cáo
1. `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/dung_bao_cao.py danh-gia-kenh/<kỳ>` → `bao-cao.html` + `sheets/*.csv`.
2. Viết `bao-cao.md` (bản chữ, đọc nhanh): tóm tắt, bảng kết luận, từng kênh (5 câu), so đối thủ, toàn hệ kênh,
   3 ưu tiên, phần thiếu dữ liệu, nguồn.
3. Mở `bao-cao.html` cho người dùng xem. Nếu người dùng muốn chia sẻ link, xuất bản thành Artifact (riêng tư).

DỪNG. Báo cáo gọn: kết luận từng kênh (1 dòng), 3 ưu tiên, chỗ thiếu số. Hỏi người dùng duyệt hoặc sửa kết luận.

## Bước 6 – Ghi Google Sheets (sau khi duyệt)
- Có `google_sheets.spreadsheet_id`: ghi thêm dòng (append) vào 3 tab `Chỉ số kênh`, `Top bài`, `Đối thủ`
  từ `sheets/*.csv`, bỏ dòng tiêu đề nếu tab đã có. Tab chưa có thì tạo tab với dòng tiêu đề.
- Chưa có: hỏi người dùng (a) gửi link file có sẵn, (b) cho phép tạo file mới `Masterplan <Doanh nghiệp>` (dùng chung cho mọi skill),
  hoặc (c) chỉ dùng CSV để tự dán. Không tự tạo file khi chưa được phép.
- Cột `Duyệt` luôn ghi `Chờ duyệt`.

## Báo cáo cuối (5 dòng)
1. Kỳ và các kênh đã đánh giá.
2. Kết luận từng kênh.
3. 3 ưu tiên kỳ tới.
4. Số còn thiếu và cách bổ sung lần sau.
5. Đường dẫn `bao-cao.md`, `bao-cao.html`, link Sheets.

## Không được
- Bấm bất cứ nút thay đổi nào trên trang quản trị (đăng, xoá, trả lời, sửa quảng cáo, đổi cài đặt).
- Bịa số, lấy số kỳ khác điền vào, so số nội bộ của mình với số công khai của đối thủ.
- Tự dừng, ẩn, xoá kênh. Kết luận chỉ là đề xuất.
