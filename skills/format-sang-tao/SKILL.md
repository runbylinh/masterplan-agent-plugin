---
name: format-sang-tao
description: Nghiên cứu format hình ảnh và video để đúc kết công thức sáng tạo tái sử dụng được — thu video/ảnh/carousel/banner/mẫu quảng cáo theo mục tiêu, ngành, nền tảng; đọc video, lời thoại, transcript khi công cụ cho phép; bóc theo phân đoạn (Hook, giữ chú ý, diễn biến, CTA), cảnh quay, góc máy, nhịp dựng, chữ, âm thanh, hiệu ứng chỉ khi quan sát được; với hình ảnh bóc tiêu đề, bố cục, hình chủ đạo, thứ tự thông tin, cách trình bày lợi ích, giá, bằng chứng, CTA; so sánh mẫu cùng cấu trúc, tách yếu tố tái sử dụng và yếu tố phụ thuộc ngữ cảnh, chuẩn hoá thành công thức và brief. Ghi vào kho Format sáng tạo (FMT) liên kết CNT/QC/EVD, bàn giao cho agent viết kịch bản, thiết kế, dựng video. Dùng khi người dùng nói "bóc format video", "10 format video cho ngành", "công thức carousel", "cấu trúc video này là gì", "thư viện format", "làm brief hình ảnh từ mẫu", hoặc khi workflow 03 cần FMT.
argument-hint: "[video | hinh-anh | ca-hai] [chủ đề hoặc mục tiêu] [--dot RP-xxx]"
---

# /masterplan-agent:format-sang-tao

Đọc trước: `${CLAUDE_PLUGIN_ROOT}/references/quy-tac.md`, `${CLAUDE_PLUGIN_ROOT}/references/quy-tac-bang-chung.md`,
`${CLAUDE_PLUGIN_ROOT}/references/kho-du-lieu.md`, `${CLAUDE_PLUGIN_ROOT}/references/nghien-cuu/quy-tac-nghien-cuu.md`.
Cách làm theo nguồn: `${CLAUDE_PLUGIN_ROOT}/references/nen-tang/` — `tiktok.md`, `youtube.md`, `instagram.md`, `facebook.md`, `threads.md`,
`meta-ads-library.md`, `tiktok-creative-center.md` (mẫu quảng cáo), `website-landing-page.md` (banner).
Lệnh kho: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/kho.py ...`. Thư mục đợt: `nghien-cuu/<YYYY-MM-DD>-<chủ-đề>/`.

## A. Mục tiêu
Biến các mẫu video và hình ảnh rời rạc thành **công thức sáng tạo có thể dùng lại** (trình tự, nhịp, bố cục, nguyên liệu cần chuẩn bị),
tách rõ phần tái sử dụng được và phần chỉ đúng trong ngữ cảnh của mẫu gốc. Phục vụ quyết định: chọn format cho kỳ Content/quảng cáo,
lên brief cho người viết kịch bản, thiết kế, dựng video, ước nguồn lực sản xuất. Skill chỉ nghiên cứu và bàn giao, không viết kịch bản hay thiết kế.

## B. Điều kiện kích hoạt
- **Dùng khi**: cần thư viện format theo ngành/mục tiêu; người dùng gửi video/ảnh mẫu muốn bóc cấu trúc; workflow 03 sau `nghien-cuu-content`.
  Yêu cầu tiêu biểu: "10 format video phù hợp quán cafe", "carousel ngành đào tạo hay trình bày thế nào".
- **Không dùng khi**: cần tìm chủ đề, nhu cầu, góc nội dung → `nghien-cuu-content`; cần góc quảng cáo, ưu đãi, landing page → `quang-cao-chuyen-doi`;
  cần viết kịch bản/bài/thiết kế cho thương hiệu từ một mẫu → plugin content-agent (`content-reference`), design-agent, video-edit.
- **Chạy độc lập** được với mẫu người dùng đưa; tốt hơn khi kho đã có CNT (từ `nghien-cuu-content`) hoặc QC (từ `quang-cao-chuyen-doi`).

## C. Đầu vào
| Loại | Nội dung |
| --- | --- |
| Bắt buộc | Loại format (Video / Hình ảnh / cả hai); mục tiêu (Thu hút / Nhận diện / Niềm tin / Chuyển đổi); ngành; mã đợt RP |
| Tuỳ chọn | Nền tảng; mẫu người dùng gửi (file, link); nguồn lực sản xuất hiện có (người quay, người dựng, thiết bị, ngân sách thời gian) |
| Dữ liệu nội bộ | Video/ảnh đã đăng của doanh nghiệp kèm số từ `danh-gia-kenh`; Brand Kit nếu có (chỉ để đánh giá mức phù hợp) |
| Kế thừa từ kho | `kho.py tim --loai CNT QC --chu "<chủ đề>"` (mẫu đã bóc nội dung); `kho.py tim --loai FMT` (không tạo format trùng tên) |
| Khi thiếu | Không mở được video/không có transcript → chỉ bóc phần nhìn thấy, ghi "không quan sát được" cho phần còn lại; không có CNT/QC → tự thu mẫu theo bước 1 và ghi EVD + MAU |

## D. Phương pháp
| Hạng mục | Cách làm |
| --- | --- |
| Nguồn và công cụ | Video: TikTok, Reels, Shorts, YouTube, mẫu TikTok Creative Center, Meta Ads Library. Hình ảnh: bài Social, carousel, banner website, quảng cáo hình. Claude in Chrome để xem và chụp khung; đọc file video người dùng gửi; transcript/phụ đề khi nền tảng hiển thị |
| Xây từ khóa | Từ khóa format ("review 30 giây", "trước sau", "POV", "carousel 5 bước", "so sánh") ghép với từ khóa ngành/nhu cầu từ KEY và chủ đề từ CNT |
| Chọn và thu mẫu | Phạm vi khởi tạo 15–30 mẫu mỗi loại format; mỗi cấu trúc định đúc kết cần ≥ 3 mẫu ở ≥ 2 kênh. Lấy cả Nổi bật, Thông thường, Ít tương tác để thấy cùng cấu trúc nhưng kết quả khác |
| Trích xuất video | Bóc theo mốc thời gian (giây): Hook 0–3 giây, đoạn giữ chú ý, diễn biến, CTA. Ghi cảnh quay, góc máy, nhịp dựng (số lần cắt/10 giây nếu đếm được), chữ trên video, âm thanh, hiệu ứng **chỉ khi thực sự quan sát/nghe được**; còn lại ghi "không quan sát được" |
| Trích xuất hình ảnh | Tiêu đề (nguyên văn), bố cục (vùng nào chứa gì), hình chủ đạo, thứ tự đọc thông tin, cách trình bày lợi ích, sản phẩm, giá, bằng chứng, CTA, tỷ lệ khung hình |
| Đối chiếu | Đặt các mẫu cùng cấu trúc cạnh nhau: phần giống nhau ở mọi mẫu = **yếu tố tái sử dụng**; phần chỉ có ở một mẫu (nhân vật nổi tiếng, trend âm thanh, sự kiện) = **yếu tố phụ thuộc ngữ cảnh** |
| Chuẩn hoá | Viết công thức: tên format, công thức Hook/tiêu đề dạng khuôn ("[Số] lỗi khi [việc] khiến [hậu quả]"), trình tự phân đoạn + thời lượng tham khảo, yêu cầu nguyên liệu, mức khó và nguồn lực |
| Kiểm chứng | Mỗi FMT liên kết ≥ 2 mẫu CNT/QC/EVD; công thức chỉ từ 1 mẫu → `do_tin_cay = Thấp`. Không gắn hiệu quả cho format; chỉ ghi kết quả công khai của mẫu |
| Mâu thuẫn | Cùng cấu trúc, kết quả trái nhau giữa nền tảng → ghi trong `Yếu tố phụ thuộc ngữ cảnh` và MT nếu ảnh hưởng quyết định |

## E. Quy trình thực hiện
**Video (9 bước)**
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| V1 | Thu video theo mục tiêu, ngành, nền tảng, format | CNT/QC trong kho, tìm kiếm | Danh sách mẫu + MAU | **DỪNG** trình danh sách nhóm cấu trúc dự kiến, chờ duyệt phạm vi |
| V2 | Xem video, đọc lời thoại/transcript nếu công cụ cho phép | Video, phụ đề | Ghi chú lời thoại theo mốc | Ghi rõ mẫu nào không đọc được tiếng/transcript |
| V3 | Bóc theo phân đoạn có mốc giây | Ghi chú V2 | Bảng phân đoạn | Mỗi mẫu có mốc đầu/cuối từng đoạn |
| V4 | Xác định Hook, cách giữ chú ý, diễn biến, CTA | Bảng phân đoạn | Khung câu chuyện | Đủ 4 thành phần hoặc ghi "không có" |
| V5 | Ghi cảnh quay, góc máy, nhịp dựng, chuyển cảnh, chữ, âm thanh, hiệu ứng **nếu quan sát được** | Video | Bảng kỹ thuật | Phần không thấy/nghe ghi "không quan sát được" |
| V6 | So sánh video cùng cấu trúc | Các bảng | Nhóm cấu trúc ≥ 3 mẫu | Mỗi nhóm có mẫu ở ≥ 2 kênh |
| V7 | Tách yếu tố tái sử dụng vs phụ thuộc ngữ cảnh | Nhóm cấu trúc | Hai danh sách | — |
| V8 | Chuẩn hoá thành công thức (FMT Loại = Video) | V7 | Nháp FMT | Đủ trường bắt buộc |
| V9 | Ghi hướng ứng dụng theo sản phẩm, thương hiệu, nguồn lực; ghi kho `kho.py them lo-fmt.json --dot RP-xxx` → `kiem-tra` | FMT | FMT-xxx | Không LỖI; **DỪNG** trình thư viện format chờ duyệt |

**Hình ảnh (6 bước)**
| Bước | Hành động | Dữ liệu | Kết quả | Sang bước sau khi |
| --- | --- | --- | --- | --- |
| H1 | Thu ảnh Social, carousel, banner, mẫu quảng cáo hình | Kho, tìm kiếm | Danh sách mẫu + MAU | Đủ phạm vi đã duyệt |
| H2 | Phân loại theo mục tiêu (Thu hút / Nhận diện / Niềm tin / Chuyển đổi) | Mẫu | Nhóm mẫu | Mỗi nhóm ≥ 3 mẫu hoặc ghi giới hạn |
| H3 | Bóc tiêu đề, bố cục, hình chủ đạo, thứ tự thông tin | Ảnh | Bảng bố cục | Mỗi mẫu có thứ tự đọc |
| H4 | Bóc cách trình bày lợi ích, sản phẩm, giá, bằng chứng, CTA | Ảnh | Bảng nội dung | — |
| H5 | Rút cấu trúc bố cục tái sử dụng | H3–H4 | Khuôn bố cục | Lặp ở ≥ 2 kênh |
| H6 | Viết công thức brief hình ảnh (FMT Loại = Hình ảnh), ghi kho và `kiem-tra` | Khuôn | FMT-xxx | Không LỖI; **DỪNG** chờ duyệt |

## F. Đầu ra — Kho Format sáng tạo (`FMT`)
Trường bắt buộc: Loại format (Video / Hình ảnh) · Tên format · Mục tiêu · Nhóm khách hàng · Công thức Hook hoặc tiêu đề · Cấu trúc · CTA ·
Mẫu tham khảo (mã CNT/QC/EVD) · Yêu cầu nguyên liệu · Mức độ khó và nguồn lực · Hướng ứng dụng. Tuỳ chọn — Video: Trình tự phân đoạn và
thời lượng · Cảnh quay và góc máy · Nhịp dựng · Chữ trên video · Âm thanh và hiệu ứng. Hình ảnh: Bố cục tổng thể · Thứ tự thông tin ·
Hình ảnh chủ đạo · Cách thể hiện lợi ích và bằng chứng. Chung: Nhu cầu hoặc tình huống · Tỷ lệ khung hình · Yếu tố phụ thuộc ngữ cảnh.
`lien_ket` ≥ 1 CNT/QC/EVD (bắt buộc theo schema), `do_tin_cay` + lý do. Ví dụ kiểm thử: `${CLAUDE_PLUGIN_ROOT}/templates/kho/vi-du/format-sang-tao.json`.

Ví dụ bản ghi (giả định):
```json
{"tam": "f1", "loai": "FMT", "tieu_de": "POV khách bước vào quán 30 giây", "lien_ket": ["@c1", "@c2", "@c3"],
 "do_tin_cay": "Trung bình", "ly_do_tin_cay": "Cấu trúc lặp ở 3 mẫu thuộc 3 kênh; chưa xem được âm thanh gốc của 1 mẫu",
 "du_lieu": {"Loại format": "Video", "Tên format": "POV khách bước vào quán", "Mục tiêu": "Thu hút", "Nhóm khách hàng": "Sinh viên, nhân viên văn phòng tìm quán ngồi lâu",
   "Công thức Hook hoặc tiêu đề": "POV: [tình huống của khách] + cảnh cửa quán trong 2 giây đầu", "Cấu trúc": "Cửa quán → đi qua quầy → món chính cận cảnh → góc ngồi → chữ địa chỉ",
   "Trình tự phân đoạn và thời lượng": "0–2s cửa; 2–8s quầy; 8–18s món; 18–26s góc ngồi; 26–30s địa chỉ", "Cảnh quay và góc máy": "Cầm tay ngang tầm mắt, đi liên tục",
   "Nhịp dựng": "Cắt theo nhịp nhạc, khoảng 1 lần mỗi 2 giây (đếm ở 2/3 mẫu)", "Chữ trên video": "Một dòng chữ nhỏ đầu video, địa chỉ cuối video",
   "Âm thanh và hiệu ứng": "Nhạc nền không lời ở 2 mẫu; mẫu còn lại không quan sát được (tắt tiếng)", "CTA": "Lưu lại để đi cuối tuần", "Tỷ lệ khung hình": "9:16",
   "Mẫu tham khảo": "CNT-001, CNT-002, CNT-003", "Yêu cầu nguyên liệu": "Điện thoại có chống rung, quán vắng khách, 1 món chủ lực",
   "Mức độ khó và nguồn lực": "Thấp: 1 người quay và dựng trong 2 giờ", "Yếu tố phụ thuộc ngữ cảnh": "Trend âm thanh tại thời điểm đăng",
   "Hướng ứng dụng": "Mỗi tuần một POV theo khung giờ khác nhau (sáng làm việc, tối hẹn bạn)"}}
```

## G. Cơ chế bàn giao
| Lưu | Chuyển cho | Dùng cho | Lần sau |
| --- | --- | --- | --- |
| `FMT` (lớp 3), EVD/MAU của mẫu tự thu | Agent viết kịch bản/bài (plugin content-agent: `write`, `content-reference`), thiết kế hình ảnh (design-agent), dựng video (video-edit); `y-tuong-content`, `y-tuong-quang-cao` | Brief sản xuất, chọn format cho lịch Content và biến thể quảng cáo | Xuất cho agent khác: `kho.py xuat --loai FMT --ra nghien-cuu/<đợt>/xuat` (CSV/xlsx), gửi kèm mã FMT; hạn dùng 365 ngày nhưng kiểm lại yếu tố phụ thuộc ngữ cảnh mỗi quý |

## H. Kiểm tra chất lượng
- [ ] Không mô tả cảnh quay, góc máy, hiệu ứng, âm thanh, bố cục chưa thực sự quan sát; phần thiếu ghi "không quan sát được".
- [ ] Mỗi FMT liên kết ≥ 2 mẫu (CNT/QC/EVD) ở ≥ 2 kênh, hoặc `do_tin_cay = Thấp` có lý do.
- [ ] Đã tách yếu tố tái sử dụng và yếu tố phụ thuộc ngữ cảnh; công thức không chép nguyên câu, hình, nhân vật của mẫu gốc.
- [ ] Trình tự phân đoạn có mốc thời lượng (video) hoặc thứ tự thông tin (hình ảnh); yêu cầu nguyên liệu và mức khó cụ thể (người, thiết bị, thời gian).
- [ ] Không gắn hiệu quả bán hàng cho format; không có FMT trùng `Loại format` + `Tên format` với kho cũ.
- [ ] `kho.py kiem-tra --dot RP-xxx` không còn LỖI.
**Hoàn thành** khi thư viện FMT ở trạng thái Chờ duyệt, người dùng có bảng format (tên, mục tiêu, mức khó) và đã biết lệnh xuất để giao sản xuất.
