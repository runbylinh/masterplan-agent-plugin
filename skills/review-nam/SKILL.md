---
name: review-nam
description: Tổng hợp một bản Marketing Audit cho năm review từ kết quả các skill rà soát (đánh giá kênh, lead và hội thoại, thương hiệu và phản hồi công khai, báo cáo kinh doanh, chi phí quảng cáo và chi phí Marketing khác) cùng company-context.md — 5 phần Khách hàng, Thương hiệu & kênh, Quảng cáo, Kinh doanh & chi phí, Nguồn lực; chỉ ra 3 điểm mạnh và 3–5 vấn đề ưu tiên, kèm bằng chứng và dữ liệu còn thiếu. Không lập chiến lược hay phân bổ ngân sách. Dùng khi người dùng gõ /masterplan-agent:review-nam, nói "review năm 2026", "marketing audit", "tổng hợp review doanh nghiệp", "nhìn lại năm qua".
argument-hint: "[năm review, ví dụ 2026]"
---

# /masterplan-agent:review-nam [năm]

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/review-nam.md`, `${CLAUDE_PLUGIN_ROOT}/references/ket-qua-json.md`.

## Bước 0 – Kiểm kê đầu vào
1. Năm review: từ tham số, mặc định năm hiện tại (tính từ 01/01 đến hôm qua).
2. Liệt kê kết quả đã có theo bảng "Đầu vào" trong `review-nam.md`: thư mục, kỳ dữ liệu, đã duyệt chưa.
3. Bảng 3 cột cho người dùng: **Đã có** · **Thiếu** · **Lệnh để bổ sung** (ví dụ `/masterplan-agent:chi-phi-ads năm`).
   Kỳ ngắn (dưới 90 ngày) ghi chú "chỉ là ảnh chụp kỳ ngắn".

DỪNG. Hỏi: chạy bổ sung skill còn thiếu trước, hay tổng hợp ngay với dữ liệu đang có (phần thiếu ghi rõ)?

## Bước 1 – Tổng hợp
- Đọc file đầu vào, không lấy lại số từ nền tảng. Số nào dùng phải trích đúng file nguồn và kỳ.
- Viết 5 phần theo `review-nam.md`; mỗi phần: Kết quả · Đang làm tốt · Vấn đề · Bằng chứng · Kỳ dữ liệu · Còn thiếu.
- Tổng chi Marketing: chỉ cộng khi các nguồn không trùng (đã kiểm ở `chi-phi-ads`).
- Mối liên hệ Marketing – kinh doanh: chỉ nêu khi có dữ liệu ghép (lead → đơn → doanh thu theo kênh).
- Kết luận: 3 điểm mạnh, 3–5 vấn đề ưu tiên (bảng `review-van-de`), câu hỏi chuyển sang Market Research.

## Bước 2 – Báo cáo
Tạo `review/<năm>/`, ghi `ket-qua.json` (loai `review-nam`, `tieu_de` "Marketing Audit <năm> – <doanh nghiệp>"), chạy:
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/dung_bao_cao_nghien_cuu.py review/<năm>
```
Hết CẢNH BÁO thì chỉnh `bao-cao.md` cho chủ doanh nghiệp đọc nhanh (bảng tổng hợp + kết luận lên đầu).
Mở `bao-cao.html` cho người dùng xem.

DỪNG. Báo cáo 5 dòng: điểm mạnh, vấn đề ưu tiên, phần thiếu, đường dẫn. Hỏi duyệt.
Sau duyệt: ghi Sheets tab `Audit – Tổng quan`, `Audit – Vấn đề` (append, `Chờ duyệt`). Nếu người dùng muốn bản Google Docs/Sheets
"MARKETING AUDIT <năm> — <doanh nghiệp>" trong thư mục Drive riêng: hỏi thư mục, chỉ tạo khi được phép.
Gợi ý bước tiếp: `/masterplan-agent:nghien-cuu-thi-truong`.

## Không được
- Tự tạo số, lấy số kỳ khác thay cho năm review, kết luận nguyên nhân khi chưa có bằng chứng.
- Lập chiến lược, KPI, phân bổ ngân sách năm sau ở bước này.
