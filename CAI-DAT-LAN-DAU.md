# Cài đặt lần đầu, từng bước (cho người mới)

Làm **đúng thứ tự** từ Bước 1 đến Bước 14. Mỗi bước có phần **Kiểm tra**: làm đúng như mô tả thì mới sang bước sau.
Thời gian khoảng 45–60 phút. Không cần biết lập trình: mỗi lệnh chỉ cần chép và dán vào Terminal, rồi nhấn Enter.

> **Terminal là gì?** Là cửa sổ gõ lệnh.
> - Mac: nhấn `Command + Space`, gõ `Terminal`, Enter.
> - Windows: nhấn phím Windows, gõ `PowerShell`, Enter.
>
> Dán lệnh: Mac `Command + V`, Windows chuột phải. Mỗi khối lệnh dưới đây chạy riêng, đợi chạy xong mới dán khối tiếp.

---

## Bước 1. Chuẩn bị tài khoản
1. **Tài khoản Claude trả phí** (Pro, Max hoặc Team) tại claude.ai.
2. **Tài khoản GitHub** (miễn phí) tại github.com. Gửi tên tài khoản GitHub cho Run By Linh để được mời vào repo riêng của agent.
3. Mở email mời từ GitHub, bấm **Accept invitation**.

**Kiểm tra:** đăng nhập github.com, mở `github.com/runbylinh/masterplan-agent-plugin` và thấy được trang repo (không báo 404).

## Bước 2. Cài Claude Desktop
1. Tải tại `claude.ai/download`, cài như ứng dụng bình thường.
2. Mở Claude Desktop, đăng nhập tài khoản Claude.
3. Ở thanh trên cùng có tab **Code**: đây là nơi chạy agent.

**Kiểm tra:** bấm tab Code, chọn một thư mục bất kỳ, gõ `xin chào` và Claude trả lời.

## Bước 3. Cài Git và GitHub CLI (để tải agent từ repo riêng)
**Mac:** chạy lệnh dưới, bấm **Install** trong hộp thoại hiện ra và đợi cài xong (5–10 phút).
```bash
xcode-select --install
```
Sau đó tải GitHub CLI cho Mac tại `cli.github.com` (file .pkg), mở file và cài.

**Windows:** chạy lần lượt:
```bash
winget install --id Git.Git -e
```
```bash
winget install --id GitHub.cli -e
```
Đóng PowerShell rồi mở lại.

**Kiểm tra:** `git --version` và `gh --version` đều in ra số phiên bản.
```bash
git --version
```
```bash
gh --version
```

## Bước 4. Đăng nhập GitHub trên máy
```bash
gh auth login
```
Chọn lần lượt: **GitHub.com** → **HTTPS** → **Yes** (authenticate Git) → **Login with a web browser**.
Màn hình hiện một mã 8 ký tự: chép mã, nhấn Enter, trình duyệt mở ra, dán mã, bấm **Authorize**.
```bash
gh auth setup-git
```
**Kiểm tra:** lệnh dưới in "Logged in to github.com".
```bash
gh auth status
```

## Bước 5. Cài Claude Code bản dòng lệnh (để cài plugin)
**Mac:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```
**Windows (PowerShell):**
```bash
irm https://claude.ai/install.ps1 | iex
```
Đóng Terminal và mở lại. Chạy `claude` một lần, làm theo hướng dẫn đăng nhập, rồi gõ `/exit` để thoát.
```bash
claude
```
Nếu cách trên không chạy, làm theo hướng dẫn chính thức: `code.claude.com/docs/en/setup`.

**Kiểm tra:** lệnh dưới in ra số phiên bản Claude Code.
```bash
claude --version
```

## Bước 6. Cài agent Masterplan
```bash
claude plugin marketplace add runbylinh/masterplan-agent-plugin
```
```bash
claude plugin install masterplan-agent@rbl-masterplan-dev
```
**Kiểm tra:** trong danh sách in ra có `masterplan-agent`.
```bash
claude plugin list
```
Nếu báo không tìm thấy repo: quay lại Bước 1 (đã chấp nhận lời mời chưa) và Bước 4 (đã đăng nhập GitHub chưa).

## Bước 7. Cài Python và thư viện đọc Excel
**Mac:** Python 3 có sẵn sau Bước 3.
**Windows:**
```bash
winget install --id Python.Python.3.12 -e
```
Đóng PowerShell và mở lại. Sau đó, cả Mac và Windows chạy:
```bash
python3 -m pip install openpyxl
```
(Windows nếu báo không có `python3` thì dùng `python -m pip install openpyxl`.)

**Kiểm tra:** lệnh dưới in ra số phiên bản (ví dụ 3.1.5).
```bash
python3 -c "import openpyxl; print(openpyxl.__version__)"
```

## Bước 8. Cài Claude in Chrome (để agent đọc trang web đã đăng nhập)
1. Mở Google Chrome → vào Chrome Web Store → tìm **Claude** (nhà phát hành Anthropic) → **Add to Chrome**.
2. Bấm biểu tượng mảnh ghép trên Chrome → ghim **Claude** lên thanh công cụ → bấm vào và đăng nhập tài khoản Claude.
3. Claude Desktop → góc dưới bên trái bấm tên tài khoản → **Settings** → **Connectors** → **Claude in Chrome** → bật.

**Kiểm tra:** trong tab Code gõ "mở trang google.com trên Chrome". Chrome mở tab Google.

## Bước 9. Kết nối dữ liệu quảng cáo và lead (làm được bao nhiêu thì làm)
Vào claude.ai (hoặc Claude Desktop) → **Settings / Customize** → **Connectors**:
| Kết nối | Cách thêm | Đăng nhập |
| --- | --- | --- |
| Meta Ads | **Add custom connector** → tên `Meta Ads MCP` → URL `https://mcp.facebook.com/ads` | Facebook có quyền tài khoản quảng cáo → chọn Business Portfolio, tài khoản quảng cáo |
| TikTok for Business | Tìm **TikTok for Business** trong danh sách connector, hoặc custom connector URL `https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer` | TikTok for Business → chọn tài khoản quảng cáo → Authorize. Hết hạn sau 30 ngày, phải kết nối lại |
| LadiPage | Tìm **LadiPage** trong danh sách connector | Tài khoản LadiPage |
| Google Drive | Tìm **Google Drive** | Tài khoản Google chứa báo cáo |
| Google Sheets | Tìm **Google Sheets** | Cùng tài khoản Google |

Chỉ cấp quyền **đọc** khi được hỏi, nếu nền tảng cho chọn. Agent không sửa quảng cáo hay ngân sách.

**Kiểm tra:** trong tab Code gõ "liệt kê tài khoản quảng cáo Meta tôi có quyền, chỉ đọc". Claude trả về tên và ID tài khoản.

## Bước 10. Đăng nhập sẵn các trang agent sẽ đọc (trên Chrome)
Mở mỗi trang một tab và đăng nhập, chọn đúng Page hoặc tài khoản doanh nghiệp:
- `business.facebook.com` (Meta Business Suite: fanpage, Messenger, Instagram, Insights)
- `chat.zalo.me` (Zalo web: quét mã QR bằng điện thoại của số bán hàng)
- `oa.zalo.me` (Zalo OA, nếu có)
- `tiktok.com/tiktokstudio` và `tiktok.com/messages` (TikTok Studio và tin nhắn)
- `ads.tiktok.com` (nếu chạy TikTok Ads và chưa kết nối ở Bước 9)
- `studio.youtube.com` (nếu có YouTube)

**Kiểm tra:** mở từng tab đều thấy trang quản trị, không bị bắt đăng nhập lại.

## Bước 11. Tạo thư mục làm việc cho doanh nghiệp
1. Tạo thư mục mới, ví dụ `Documents/masterplan-<ten-doanh-nghiep>` (mỗi doanh nghiệp một thư mục).
2. Claude Desktop → tab **Code** → chọn thư mục đó → **mở phiên mới**.

**Kiểm tra:** gõ `/masterplan-agent:` trong ô chat và thấy danh sách lệnh (huong-dan, setup, dieu-phoi…).
Không thấy: đóng phiên, mở phiên mới. Vẫn không thấy: chạy lại Bước 6.

## Bước 12. Để agent tự kiểm tra máy
```
/masterplan-agent:huong-dan
```
Agent lập bảng **Có / Thiếu** cho Python, Chrome, Meta Ads, TikTok, LadiPage, Drive, Sheets, kèm cách sửa từng mục còn thiếu.

**Kiểm tra:** ít nhất Chrome và Python là **Có**. Những mục khác còn thiếu vẫn chạy tiếp được, agent sẽ ghi rõ phần thiếu số.

## Bước 13. Khai báo doanh nghiệp
```
/masterplan-agent:setup
```
Trả lời lần lượt các câu agent hỏi:
1. bối cảnh doanh nghiệp (6 mục);
2. link kênh và vai trò từng kênh;
3. đối thủ;
4. tài khoản quảng cáo;
5. hộp thư: từng fanpage, từng số Zalo, kênh TikTok, và tên nhãn/thẻ đang dùng cho "đã chốt / đang tư vấn / không phù hợp";
6. thư mục báo cáo kinh doanh;
7. link Google Sheets.

Có sẵn tài liệu giới thiệu doanh nghiệp thì gửi link hoặc kéo file vào, agent tự điền từ đó.

**Kiểm tra:** thư mục làm việc có thêm `company-context.md`, `cau-hinh.json`, `nhap/`, `bang-chung/`.

## Bước 14. Chạy thử lần đầu
Bắt đầu bằng một việc nhỏ, ví dụ:
```
/masterplan-agent:danh-gia-kenh 30
```
hoặc
```
/masterplan-agent:lead-hoi-thoai 7
```
Agent hỏi phạm vi, rồi **DỪNG** chờ bạn trả lời "Bắt đầu". Agent lấy số, làm báo cáo (`bao-cao.html` mở cho bạn xem),
rồi **DỪNG** chờ bạn duyệt. Duyệt xong mới ghi Google Sheets.

**Kiểm tra:** có thư mục kết quả (ví dụ `danh-gia-kenh/2026-11-26_30d/`) chứa `bao-cao.md` và `bao-cao.html`.

---

## Sau khi cài xong
- Cách dùng hằng ngày, bảng lệnh và quy trình 4 phần: [HUONG-DAN.md](HUONG-DAN.md).
- Không biết làm gì tiếp: gõ `/masterplan-agent:dieu-phoi`.
- Cập nhật agent khi có bản mới:
```bash
claude plugin marketplace update rbl-masterplan-dev
```
```bash
claude plugin update masterplan-agent@rbl-masterplan-dev
```
Sau đó mở phiên Code mới.

## Bị kẹt ở đâu?
| Đang ở bước | Hiện tượng | Xử lý |
| --- | --- | --- |
| 3 | `xcode-select` báo đã cài | Bình thường, sang bước tiếp |
| 4 | Trình duyệt không mở | Mở `github.com/login/device` bằng tay, dán mã 8 ký tự |
| 5 | `claude: command not found` | Đóng và mở lại Terminal; vẫn lỗi thì làm theo `code.claude.com/docs/en/setup` |
| 6 | `Repository not found` / 404 | Chưa chấp nhận lời mời GitHub, hoặc `gh auth status` chưa đăng nhập |
| 7 | `pip` báo quyền | Thêm `--user`: `python3 -m pip install --user openpyxl` |
| 8 | Agent không điều khiển được Chrome | Tiện ích Claude chưa đăng nhập, hoặc chưa bật connector Claude in Chrome trong Settings |
| 9 | Không thấy mục thêm custom connector | Gói tài khoản không hỗ trợ: bỏ qua, agent sẽ đọc Ads Manager qua Chrome hoặc file xuất |
| 10 | Zalo web đòi quét lại QR | Zalo web tự đăng xuất sau một thời gian: quét lại trước khi chạy skill hội thoại |
| 11 | Không thấy lệnh `/masterplan-agent:` | Mở phiên Code mới; kiểm tra `claude plugin list` |
