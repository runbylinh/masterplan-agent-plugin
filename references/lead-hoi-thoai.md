# Lead và hội thoại: nơi lấy số, tiêu chí, định dạng

## Nơi lấy số (Claude in Chrome, chỉ đọc)
| Hộp thư | Trang | Đếm tổng | Ghi chú |
| --- | --- | --- | --- |
| Messenger + Instagram | business.facebook.com → Hộp thư | Bộ lọc ngày, nhãn, "Quảng cáo"; Hộp thư → Thông tin chi tiết (phản hồi) | Danh sách hội thoại là bảng ảo, cuộn để tải thêm; ưu tiên `get_page_text` |
| Zalo OA | oa.zalo.me → Tin nhắn; Thống kê | Lọc theo ngày, nhãn | Tin nhắn OA có giới hạn phản hồi 7 ngày, không ảnh hưởng việc đọc |
| Zalo cá nhân | chat.zalo.me | Phân loại (thẻ màu), lọc "Chưa đọc" | Không có thống kê; chỉ đếm theo thẻ trong kỳ |
| TikTok | tiktok.com/messages hoặc TikTok Business Center inbox | Đếm thủ công trong kỳ | Không có nhãn: dựa vào đọc nội dung |
| LadiPage | connector `report_leads_by_campaign`, LadiWork `lw_report_deals` | Lead form, deal theo trạng thái | Chỉ lấy số đếm |

Gặp đăng nhập, mã xác minh, CAPTCHA: dừng, nhờ người dùng tự làm.

## Mức lead (đọc nội dung)
| Mức | Mã | Dấu hiệu |
| --- | --- | --- |
| Nóng | `nong` | Hỏi giá + lịch/cách thanh toán, xin STK, đã để SĐT để chốt, so sánh gói cụ thể |
| Ấm | `am` | Quan tâm sản phẩm cụ thể, hỏi chi tiết nội dung/lợi ích, chưa hỏi thanh toán |
| Lạnh | `lanh` | Hỏi chung chung, chỉ "giá bao nhiêu" rồi im, xin tài liệu miễn phí |
| Không phù hợp | `khong_phu_hop` | Sai nhu cầu, spam, đối tác/tuyển dụng, ngoài khu vực phục vụ |
| Không rõ | `khong_ro` | Quá ít tin để kết luận |

## Trạng thái
`chot` (đã chuyển khoản / xác nhận mua / có đơn) · `dang_tu_van` · `mat` (khách im ≥ 3 ngày sau báo giá hoặc từ chối)
· `chua_tra_loi` (team chưa phản hồi) · `khong_phu_hop`.

## Lý do không chốt (chọn 1 chính)
`gia` · `thoi_gian_lich` · `chua_tin` (cần thêm bằng chứng/feedback) · `chua_ro_loi_ich` · `so_sanh_doi_thu`
· `phan_hoi_cham` · `tu_van_chua_toi` (không hỏi nhu cầu, không chốt bước tiếp) · `chua_co_nhu_cau_ngay` · `khac`.

## Định dạng `hoi-thoai.json`
```json
{
  "doanh_nghiep": "Brand mẫu",
  "ky": {"tu": "2026-10-26", "den": "2026-11-24", "ky_truoc_tu": "2026-09-26", "ky_truoc_den": "2026-10-25"},
  "ngay_lay": "2026-11-25",
  "tong_theo_kenh": [
    {"kenh": "messenger", "hien_tai": {"hoi_thoai": 420, "tu_quang_cao": 300, "chua_tra_loi": 12,
       "theo_nhan": {"Đã chốt": 38, "Đang tư vấn": 60}, "ty_le_phan_hoi_pct": 96, "phan_hoi_tb_phut": 18,
       "lead_form": 85, "don": 41, "doanh_thu": 205000000},
     "ky_truoc": {"hoi_thoai": 380, "theo_nhan": {"Đã chốt": 30}, "don": 33},
     "nguon": [{"chi_so": "hoi_thoai, theo_nhan", "noi_lay": "Business Suite → Hộp thư", "ngay_lay": "2026-11-25"}],
     "thieu": []}
  ],
  "mau": [
    {"ma": "HT-messenger-001", "kenh": "messenger", "nguon": "quang_cao", "ngay": "2026-11-02",
     "phan_hoi_dau_phut": 6, "so_tin": 14, "nhan": ["Đã chốt"], "nhu_cau": "Khoá Content AI",
     "muc": "nong", "trang_thai": "chot", "ly_do_khong_chot": null,
     "cau_hoi": ["học online hay offline", "có trả góp không"], "nhan_xet_tu_van": "hỏi nhu cầu trước khi báo giá"}
  ]
}
```
`kenh`: `messenger`, `instagram`, `zalo_oa`, `zalo_ca_nhan`, `tiktok`, `lead_form`.
Mọi số không có để `null`. `don`, `doanh_thu` chỉ điền khi có file đơn/CRM.
