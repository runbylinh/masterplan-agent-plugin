# Lead và hội thoại: nơi lấy số, tiêu chí, định dạng

## Nơi lấy số (Claude in Chrome, chỉ đọc)
Nguyên tắc chung cho mọi hộp thư:
- Người dùng đăng nhập sẵn trên Chrome. Gặp đăng nhập, mã QR, OTP, CAPTCHA: dừng, nhờ người dùng tự làm, rồi làm tiếp.
- Chỉ đọc. Không gõ vào ô soạn tin, không bấm Gửi, Trả lời nhanh, Gắn nhãn, Lưu trữ, Đánh dấu chưa đọc, Chặn, Xoá.
- **Đếm tổng trước** bằng bộ lọc, danh sách, thống kê (không cần mở hội thoại). **Đọc mẫu sau**, chỉ trong cỡ mẫu đã duyệt.
- Mở hội thoại chưa đọc sẽ làm nó thành "đã đọc" với cả team: mặc định chỉ mở hội thoại đã đọc; chưa đọc chỉ mở khi được phép.
- Danh sách dài là bảng cuộn ảo: cuộn từng đoạn, sau mỗi lần cuộn đọc bằng `get_page_text` hoặc `find`/`read_page`,
  ghi mốc ngày cuối cùng đã thấy để biết đã đi hết kỳ chưa. Không dùng script tự động cuộn hàng loạt hay tải dữ liệu ẩn.
- Mỗi tài khoản (2 fanpage, 2 số Zalo...) là một dòng riêng trong `tong_theo_kenh` với `kenh` khác nhau (ví dụ `messenger_2`) và `ten`.
- Ghi `nguon` (trang + bộ lọc đã dùng + ngày lấy) và `thieu` (chỉ số không lấy được + lý do) cho từng hộp thư.

### 1. Facebook Messenger của fanpage (và Instagram Direct) — mã `messenger`, `instagram`
Cách A – **Meta Business Suite** (khuyên dùng): `business.facebook.com` → chọn đúng Business Portfolio và **đúng Page** (góc trên trái)
→ **Hộp thư (Inbox)** → tab **Messenger** (hoặc **Instagram**).
1. Bộ lọc (biểu tượng phễu): chọn **khoảng ngày** của kỳ → đếm số hội thoại.
2. Lọc theo **nhãn** (Labels) đã khai trong `hop_thu.nhan_chot`, `nhan_dang_tu_van`, `nhan_khong_phu_hop` → đếm từng nhãn.
3. Lọc **Chưa đọc / Chưa trả lời / Cần theo dõi** → đếm hội thoại chưa xử lý.
4. Lọc **Quảng cáo** (hội thoại bắt đầu từ quảng cáo Click-to-Messenger) → đếm `tu_quang_cao`.
5. **Hộp thư → Thông tin chi tiết (Insights)** hoặc **Thông tin chi tiết → Tin nhắn**: tỷ lệ phản hồi, thời gian phản hồi trung bình, số hội thoại mới.
Cách B – Page trên Facebook: chuyển sang trang cá nhân của Page (`facebook.com/<page>` → Chuyển sang Trang) → **Hộp thư** (`facebook.com/latest/inbox`).
Giao diện giống Business Suite; dùng khi người dùng không có quyền Business Suite.
Cách C – Meta Ads MCP: số "bắt đầu cuộc trò chuyện" từ quảng cáo (`onsite_conversion.messaging_conversation_started_7d`) để đối chiếu `tu_quang_cao`.

### 2. Zalo cá nhân bản web (số bán hàng, số tư vấn) — mã `zalo_web`
Dùng cho các số Zalo **cá nhân** mà sale/tư vấn dùng để chat với khách (khác Zalo OA ở mục 3). Một doanh nghiệp có thể có cả hai:
đếm riêng từng số Zalo cá nhân và riêng OA.
`chat.zalo.me` → người dùng quét mã QR bằng ứng dụng Zalo trên điện thoại **của đúng số đó**.
1. **Đồng bộ tin nhắn trước khi đếm**: Zalo web có thể chỉ hiện tin gần đây. Nếu Zalo hỏi "Đồng bộ tin nhắn" thì nhờ người dùng bấm
   đồng bộ trên điện thoại và đợi xong. Không đồng bộ được: ghi `thieu` = "Zalo web chỉ hiện tin từ <ngày>".
2. **Tin nhắn từ người lạ**: Zalo gom tin của người chưa kết bạn vào mục riêng (Tin nhắn từ người lạ / Người lạ). Đây thường là khách mới:
   đếm riêng (`tu_nguoi_la`) rồi cộng vào tổng hội thoại.
3. **Phân loại (thẻ màu)**: bấm biểu tượng thẻ/bộ lọc ở danh sách → chọn từng thẻ (Khách hàng, Trả lời sau hoặc thẻ team tự đặt như
   "Đã chốt", "Đang tư vấn") → đếm. Tên thẻ khai trong `hop_thu.nhan_chot`, `nhan_dang_tu_van`, `nhan_khong_phu_hop`.
4. Bộ lọc **Chưa đọc** → đếm hội thoại chưa xử lý.
5. Không có lọc theo ngày: cuộn danh sách, đếm hội thoại có tin cuối trong kỳ (mốc thời gian bên phải). Kỳ dài (> 30 ngày) hoặc quá nhiều
   hội thoại: đếm theo thẻ, ghi rõ "đếm theo thẻ, không lọc được ngày".
6. Bỏ qua: nhóm chat, cộng đồng, chat nội bộ (đồng nghiệp, gia đình), tài khoản OA/hệ thống, "Cloud của tôi".
7. Không có thống kê phản hồi: lấy `phan_hoi_dau_phut` từ mẫu đọc chat (giờ tin đầu của khách → giờ trả lời đầu tiên).
8. **Nhiều số Zalo**: mỗi lần trình duyệt chỉ đăng nhập một số. Làm xong số này, nhờ người dùng đăng xuất trên chat.zalo.me và quét QR số tiếp theo
   (hoặc dùng hồ sơ Chrome khác cho mỗi số). Mỗi số một dòng: `zalo_web`, `zalo_web_2`... kèm `"ten": "Zalo tư vấn 1"`.
9. Chỉ đọc: không gửi tin, không thả cảm xúc, không gắn/bỏ thẻ, không ghim, không xoá, không chấp nhận lời mời kết bạn.
Bản Zalo PC đang mở cùng số vẫn đọc qua web được, không cần đóng.

### 3. Zalo Official Account — mã `zalo_oa`
`oa.zalo.me` → chọn đúng OA → **Tin nhắn** (hoặc Zalo OA Chat `oa.zalo.me/chat`).
1. Lọc theo **thời gian** và **nhãn/tag** khách → đếm.
2. **Thống kê → Tin nhắn**: số người nhắn, tin nhắn đến/đi, (nếu có) thời gian phản hồi.
3. Ghi riêng hội thoại đến từ quảng cáo Zalo (nếu OA gắn nguồn).

### 4. TikTok tin nhắn bản web — mã `tiktok`
Cách A – tài khoản thường/doanh nghiệp: `tiktok.com/messages` (đăng nhập đúng tài khoản kênh).
1. Danh sách hội thoại bên trái: cuộn, đếm hội thoại có tin trong kỳ (mốc thời gian dưới tên). Có mục **Yêu cầu tin nhắn (Message requests)**:
   đếm riêng, đây thường là người lạ (khách mới).
2. TikTok không có nhãn: phân loại bằng đọc mẫu (mức lead, trạng thái).
Cách B – **TikTok Business Suite / Business Center inbox** (nếu doanh nghiệp dùng): xem hộp thư hợp nhất, có lọc theo thời gian.
Cách C – hội thoại từ quảng cáo nhắn tin TikTok: đối chiếu số "Conversations"/"Tin nhắn" trong TikTok Ads (MCP hoặc Ads Manager).
Bình luận hỏi giá dưới video không phải hội thoại: chỉ đếm nếu người dùng muốn, ghi riêng.

### 5. Kênh chat khác (nếu doanh nghiệp dùng)
| Kênh | Mã | Nơi xem |
| --- | --- | --- |
| TikTok Shop chat | `tiktok_shop` | TikTok Shop Seller Center → Chăm sóc khách hàng / Tin nhắn; số liệu dịch vụ khách hàng (tỷ lệ phản hồi) |
| Shopee chat | `shopee` | Shopee Seller Centre → Chat; Dữ liệu → Hiệu quả chat (tỷ lệ phản hồi, chuyển đổi chat) |
| Chat trên website | `website_chat` | Trang quản trị công cụ chat (Messenger plugin, Zalo widget, LiveChat...) |
| Form / landing page | `lead_form` | Connector LadiPage `report_leads_by_campaign`; LadiWork `lw_report_deals` (deal theo trạng thái) |

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
    {"kenh": "messenger", "hien_tai": {"hoi_thoai": 420, "tu_quang_cao": 300, "tu_nguoi_la": null, "chua_tra_loi": 12,
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
`kenh`: `messenger`, `instagram`, `zalo_web` (cũ: `zalo_ca_nhan`), `zalo_oa`, `tiktok`, `tiktok_shop`, `shopee`, `website_chat`, `lead_form`.
Nhiều tài khoản cùng loại: thêm hậu tố (`messenger_2`) và ghi `"ten": "Fanpage B"`.
Mọi số không có để `null`. `don`, `doanh_thu` chỉ điền khi có file đơn/CRM.
