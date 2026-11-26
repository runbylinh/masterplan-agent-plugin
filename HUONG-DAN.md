# Hướng dẫn cài đặt và sử dụng Agent Masterplan Marketing

**Cài lần đầu? Làm theo [CAI-DAT-LAN-DAU.md](CAI-DAT-LAN-DAU.md) (14 bước, có kiểm tra sau mỗi bước).**

Tài liệu cho người làm Marketing, không cần biết lập trình. Làm lần lượt Phần A (cài một lần), rồi dùng Phần B mỗi khi làm việc.
Đã cài xong nhưng chưa chắc đủ? Mở Claude Code và gõ `/masterplan-agent:huong-dan`. Agent tự kiểm tra máy và chỉ ra chỗ còn thiếu.

---

## A. Cài đặt (làm một lần)

### A1. Chuẩn bị
| Cần có | Ghi chú |
| --- | --- |
| Tài khoản Claude trả phí (Pro, Max, Team) | Để dùng Claude Code và Claude in Chrome |
| Máy Mac hoặc Windows, trình duyệt Google Chrome | |
| Quyền truy cập repo GitHub `runbylinh/masterplan-agent-plugin` | Repo riêng tư: nhờ Run By Linh mời tài khoản GitHub của bạn. Máy phải đăng nhập GitHub (`gh auth login`, hoặc GitHub Desktop) |
| Python 3 | Mac có sẵn. Windows: cài từ python.org, tick "Add Python to PATH" |

### A2. Cài Claude Code
Dùng **Claude Desktop → tab Code**, hoặc cài bản dòng lệnh theo hướng dẫn chính thức: https://code.claude.com/docs/en/setup.
Đăng nhập bằng tài khoản Claude.

### A3. Cài plugin
Mở Terminal (Mac: Command + Space, gõ Terminal. Windows: PowerShell), chạy lần lượt:
```bash
claude plugin marketplace add runbylinh/masterplan-agent-plugin
```
```bash
claude plugin install masterplan-agent@rbl-masterplan-dev
```
Cài thư viện đọc Excel (dùng cho file báo cáo và xuất bộ mẫu):
```bash
python3 -m pip install openpyxl
```
Mở phiên Claude Code mới. Gõ `/masterplan-agent:` sẽ thấy danh sách lệnh.

**Cập nhật khi có bản mới:**
```bash
claude plugin marketplace update rbl-masterplan-dev
```
```bash
claude plugin update masterplan-agent@rbl-masterplan-dev
```
Sau đó mở phiên mới.

### A4. Kết nối nguồn dữ liệu
Không bắt buộc nối hết. Thiếu nguồn nào, agent ghi rõ phần nào chưa có số, rồi làm tiếp phần còn lại.

| Nguồn | Dùng cho | Cách nối |
| --- | --- | --- |
| **Claude in Chrome** | Đọc Business Suite, TikTok Studio, Zalo, Google Maps, trang đối thủ, nghiên cứu web | Cài tiện ích Claude trên Chrome Web Store → đăng nhập → ghim lên thanh công cụ. Claude Desktop → Settings → Connectors → Claude in Chrome → bật |
| **Meta Ads** | Chi phí, kết quả quảng cáo Meta | Claude → Customize → Connectors → Add custom connector → URL `https://mcp.facebook.com/ads` → đăng nhập Meta → chọn tài khoản quảng cáo |
| **TikTok for Business** | Chi phí, kết quả TikTok Ads | Claude Marketplace → TikTok for Business → Add to Claude, hoặc custom connector URL `https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer`. Quyền hết hạn sau **30 ngày**, cần cấp lại |
| **LadiPage** | Lead theo utm, LadiWork (CRM) | Connector LadiPage trong Claude |
| **Google Drive** | Đọc báo cáo kinh doanh, file ngân sách; lưu bộ mẫu | Connector Google Drive |
| **Google Sheets** | Ghi kết quả "Chờ duyệt" | Connector Google Sheets |

Trên Chrome, đăng nhập sẵn các trang agent cần đọc: Meta Business Suite, TikTok Studio, TikTok Ads Manager, YouTube Studio,
Zalo OA, Zalo web (chat.zalo.me).

### A5. Tạo thư mục làm việc cho doanh nghiệp
Mỗi doanh nghiệp một thư mục riêng, **không** để trong thư mục plugin. Ví dụ `Documents/masterplan-<ten-doanh-nghiep>/`.
Mở Claude Code tại thư mục đó (Claude Desktop → Code → chọn thư mục), gõ:
```
/masterplan-agent:setup
```
Agent hỏi lần lượt:
1. **Bối cảnh doanh nghiệp** (6 mục theo Mẫu bối cảnh doanh nghiệp). Có sẵn tài liệu thì gửi link hoặc file, agent điền từ đó.
2. Link các kênh (Page, Group, TikTok, IG, Threads, YouTube, Zalo OA) và vai trò mỗi kênh.
3. 3–5 đối thủ (chưa có thì để agent đề xuất sau).
4. Tài khoản quảng cáo Meta/TikTok, file ngân sách.
5. utm_source của từng kênh, hộp thư team dùng, tên nhãn "đã chốt / đang tư vấn / không phù hợp", file đơn hàng.
6. Thư mục báo cáo kinh doanh trên Drive hoặc trên máy, KPI nếu có.
7. Link Google Sheets để ghi kết quả, hoặc cho phép tạo mới.

Xong sẽ có `company-context.md` và `cau-hinh.json`. Muốn sửa sau này, chạy lại `/masterplan-agent:setup` và nói phần cần sửa.

---

## B. Thao tác hằng ngày

### B1. Không biết bắt đầu từ đâu
```
/masterplan-agent:dieu-phoi
```
Agent đọc thư mục, cho biết phần nào đã có, phần nào thiếu, phần nào đã cũ, rồi đề xuất chạy gì tiếp. Có thể nói bằng lời:
"nghiên cứu tổng thể để chuẩn bị Masterplan 2027", "đang tới đâu rồi?", "bước tiếp theo là gì?".

### B2. Quy trình 4 phần
```
0 Setup → 1 Đánh giá hiện trạng → 2 Nghiên cứu thị trường → 3 Dự báo xu hướng → 4 Định hướng chiến lược → (Masterplan)
```
| Phần | Lệnh | Khi nào dùng | Bạn cần chuẩn bị |
| --- | --- | --- | --- |
| 1 | `/masterplan-agent:danh-gia-kenh 90` | Kênh social nào hiệu quả, nên giữ/đẩy/tối ưu/bỏ | Đăng nhập Business Suite, TikTok Studio... |
| 1 | `/masterplan-agent:lead-hoi-thoai 30` | Số hội thoại, chất lượng lead, tỷ lệ chốt, khách hỏi gì — trên Messenger fanpage, Instagram, Zalo web, Zalo OA, TikTok tin nhắn web, TikTok Shop/Shopee chat | Mỗi hộp thư một tab Chrome đã đăng nhập (Zalo web quét QR); cho phép mở hội thoại |
| 1 | `/masterplan-agent:ra-soat-thuong-hieu` | Website, hình ảnh thương hiệu, review Google Maps, bình luận | Link website, tên trên Google Maps |
| 1 | `/masterplan-agent:bao-cao-kinh-doanh 2026` | Doanh thu, đơn, sản phẩm, kênh, so KPI | File/Sheet doanh thu (tối thiểu: Tháng – Doanh thu – Số đơn) |
| 1 | `/masterplan-agent:chi-phi-ads năm` | Đã chi bao nhiêu, CPL, ROAS, so ngân sách | Connector Meta/TikTok; bảng chi phí ngoài quảng cáo (Tháng – Khoản chi – Số tiền) |
| 1 | `/masterplan-agent:review-nam 2026` | Gom tất cả thành **một bản Đánh giá hiện trạng (Marketing Audit)** | Các skill phần 1 đã chạy (thiếu thì agent nói rõ) |
| 2 | `/masterplan-agent:nghien-cuu-thi-truong tat-ca 2026` | Ngành hàng, khách hàng, 5–10 đơn vị cùng ngành | Duyệt phạm vi + danh sách đơn vị agent đề xuất |
| 2 | `/masterplan-agent:quet-doi-thu tất cả` | Theo dõi offer, khuyến mãi, ads đối thủ hằng tuần/tháng | Danh sách đối thủ trong cấu hình |
| 3 | `/masterplan-agent:du-bao-xu-huong 2027` | Thị trường năm sau thay đổi gì, cần ứng phó thế nào | Đã có Nghiên cứu thị trường |
| 4 | `/masterplan-agent:dinh-huong-chien-luoc 2027` | Nên tập trung cơ hội nào, chốt một hướng đi | Đã có Dự báo (và nên có Audit) |

Gõ lệnh không kèm tham số cũng được, agent sẽ hỏi kỳ.

### B3. Mỗi skill chạy thế nào
1. **Chốt phạm vi.** Agent hỏi kỳ, kênh, nguồn rồi DỪNG chờ bạn trả lời "Bắt đầu".
2. **Lấy số.** Agent mở trang trên Chrome (chỉ đọc), gọi connector, đọc file. Gặp đăng nhập, mã OTP hay CAPTCHA thì agent nhờ bạn tự làm.
3. **Tính toán và nhận định.** Mọi số có nguồn và ngày lấy. Agent tách rõ **dữ kiện / nhận định / giả định** và ghi **mức tin cậy Cao / Trung bình / Thấp**.
4. **Báo cáo.** Mỗi lần chạy có thư mục riêng (ví dụ `danh-gia-kenh/2026-11-25_7d/`), gồm:
   - `bao-cao.md`: bản chữ;
   - `bao-cao.html`: có bảng và biểu đồ, agent mở cho bạn xem;
   - `sheets/*.csv`: dữ liệu để ghi vào Google Sheets.
5. **DỪNG chờ duyệt.** Bạn trả lời duyệt, hoặc nói chỗ cần sửa (ví dụ "đổi kết luận kênh TikTok sang Giữ vì…").
6. **Sau khi duyệt:**
   - ghi Google Sheets với cột Duyệt = `Chờ duyệt`; bạn tự đổi thành `Đã duyệt` hoặc `Loại`;
   - xuất **bộ mẫu .xlsx** đúng khuôn của khoá học;
   - đưa lên Drive nếu bạn cho phép.

### B4. Bộ mẫu Masterplan (file kết quả cuối)
| Giai đoạn | File | Lệnh xuất (agent tự chạy sau khi duyệt) |
| --- | --- | --- |
| Bối cảnh | `company-context.md` | — |
| Đánh giá hiện trạng | Đánh giá hiện trạng marketing {năm}.xlsx | `xuat_bo_mau.py danh-gia-hien-trang` |
| Nghiên cứu thị trường | Nghiên cứu thị trường {năm}.xlsx | `xuat_bo_mau.py nghien-cuu-thi-truong` |
| Dự báo và định hướng | Dự báo xu hướng và định hướng marketing {năm sau}.xlsx | `xuat_bo_mau.py du-bao-dinh-huong` |
| Kế hoạch tổng thể | Kế hoạch marketing tổng thể {năm sau}.xlsx | Chưa có skill. Xin mẫu trống để tự điền |

Chỉ cần mẫu trống để tự điền? Nói với agent: "cho tôi mẫu trống đánh giá hiện trạng 2026".

Các ưu tiên trong bản Đánh giá được đánh mã **UT1–UT5**. Nghiên cứu thị trường và Định hướng chiến lược ghi lại mã này,
nên lần ra được mỗi quyết định dựa trên vấn đề nào.

### B5. Thư mục làm việc sau một vòng đầy đủ
```
masterplan-<doanh-nghiep>/
├── company-context.md        bối cảnh doanh nghiệp
├── cau-hinh.json             kênh, đối thủ, tài khoản, nguồn số
├── nhap/                     file bạn tự xuất (CSV/XLSX) để agent đọc
├── bang-chung/               ảnh chụp màn hình số liệu
├── danh-gia-kenh/ lead-hoi-thoai/ thuong-hieu/ kinh-doanh/ chi-phi-ads/ doi-thu/
├── review/<năm>/             Đánh giá hiện trạng (Marketing Audit)
├── thi-truong/<ngày>/        Nghiên cứu thị trường
├── du-bao/<năm>_<ngày>/      Dự báo xu hướng
├── chien-luoc/<năm>_<ngày>/  Định hướng chiến lược
└── tong-hop/                 tóm tắt khi chạy tổng thể
```

### B6. Theo dõi định kỳ
- Quét đối thủ hằng tuần: chạy `/masterplan-agent:quet-doi-thu`, khi agent hỏi thì đồng ý hẹn giờ (ví dụ thứ Hai 8:00).
  Lịch chạy trên máy này, cần máy mở và Chrome đăng nhập.
- Cập nhật tín hiệu thị trường hằng quý: đồng ý khi `du-bao-xu-huong` hỏi.
- Đánh giá kênh hằng tháng: `/masterplan-agent:danh-gia-kenh 30`. Kết quả mỗi kỳ ghi thêm dòng mới vào Sheets, không đè kỳ cũ.

---

## C. Agent làm gì và không làm gì
| Agent làm | Agent không làm |
| --- | --- |
| Đọc trang quản trị đã đăng nhập, trang công khai, connector, file bạn cho | Đăng bài, trả lời bình luận/tin nhắn, gắn nhãn hội thoại |
| Tính chỉ số, so kỳ trước, so đối thủ bằng số công khai | Sửa, bật, tắt quảng cáo, đổi ngân sách |
| Đề xuất kết luận, ưu tiên, hướng đi | Tự quyết định thay bạn, tự dừng hay xoá kênh |
| Ghi Sheets dòng `Chờ duyệt`, xuất file vào thư mục làm việc | Tạo file Sheets/Drive mới khi chưa hỏi, sửa file gốc |
| Đếm và phân loại hội thoại (mã `HT-...`) | Lưu tên, SĐT, email, nội dung chat của khách |
| Ghi "chưa có dữ liệu" khi không lấy được số | Bịa số, suy đoán doanh thu/ngân sách đối thủ |

## D. Lỗi thường gặp
| Hiện tượng | Cách xử lý |
| --- | --- |
| Gõ `/masterplan-agent:` không thấy lệnh | Mở phiên Claude Code mới, hoặc chạy `/reload-plugins`. Vẫn không thấy: chạy lại lệnh cài ở A3 |
| `marketplace add` báo không tìm thấy repo | Tài khoản GitHub chưa được mời vào repo riêng tư, hoặc máy chưa đăng nhập GitHub (`gh auth login`) |
| Agent nói chưa có `cau-hinh.json` | Đang mở sai thư mục. Mở đúng thư mục làm việc, hoặc chạy `/masterplan-agent:setup` |
| Agent không mở được Chrome | Kiểm tra tiện ích Claude in Chrome đã bật và đăng nhập; trong Claude Desktop bật connector Claude in Chrome |
| Trang yêu cầu đăng nhập, OTP, CAPTCHA | Bạn tự đăng nhập trên Chrome rồi bảo agent "làm tiếp" |
| Không lấy được số TikTok Ads | Quyền TikTok for Business MCP hết hạn sau 30 ngày: kết nối lại. Hoặc xuất báo cáo CSV bỏ vào `nhap/` |
| Báo `Cần openpyxl` | Chạy `python3 -m pip install openpyxl` |
| Script báo `CẢNH BÁO: thiếu nguồn` | Agent sẽ tự bổ sung nguồn hoặc ghi vào mục "Thiếu dữ liệu" trước khi trình duyệt |
| Số Facebook Group "kỳ trước" lệch nhẹ | Insights chỉ cho %, agent tính ngược nên có thể lệch ±1. Muốn chính xác thì xuất CSV Insights vào `nhap/` |

## E. Mẹo dùng hiệu quả
- Chạy phần 1 với kỳ dài (90 ngày hoặc cả năm) trước khi làm Đánh giá hiện trạng. Kỳ 7–30 ngày chỉ là ảnh chụp ngắn.
- Bỏ sẵn file xuất (Insights CSV, báo cáo TikTok, doanh thu) vào `nhap/`. Agent đọc file nhanh và đủ hơn đọc trên trang.
- Khi duyệt, nói lý do nếu đổi kết luận. Agent ghi "đổi từ X sang Y vì…" vào báo cáo.
- Sai sót lặp lại thì nói "thêm quy tắc …". Agent sẽ đề xuất một quy tắc mới và hỏi trước khi ghi.
