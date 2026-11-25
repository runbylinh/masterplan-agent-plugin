# Khung đánh giá kênh: Phễu + vai trò kênh

Mỗi kênh được giao MỘT vai trò chính trong phễu, rồi chấm theo đúng việc của vai trò đó.
Không chê kênh nhận biết vì ít lead, không khen kênh chuyển đổi chỉ vì nhiều view.

## 1. Vai trò kênh
| Vai trò | Mã | Việc của kênh | Chỉ số chính | Chỉ số phụ |
| --- | --- | --- | --- | --- |
| Nhận biết | `nhan_biet` | Đưa thương hiệu tới người chưa biết | Reach/lượt xem, mức tăng follower | Tỷ lệ tương tác, tần suất đăng |
| Tương tác | `tuong_tac` | Nuôi người đã biết, tạo niềm tin, cộng đồng | Tỷ lệ tương tác | Reach, bình luận + chia sẻ, tần suất |
| Chuyển đổi | `chuyen_doi` | Ra lead, inbox, đơn | Lead, chi phí/lead (CPL), lead / 1.000 reach | Tỷ lệ tương tác, reach |

Gợi ý vai trò mặc định (người dùng có quyền đổi trong `cau-hinh.json`):
TikTok, YouTube, Instagram → Nhận biết · Facebook Group, Threads → Tương tác · Facebook Page, Zalo OA → Chuyển đổi.

## 2. Chỉ số tính cho mỗi kênh
| Chỉ số | Cách tính | Ghi chú |
| --- | --- | --- |
| Tăng trưởng follower | follower mới trong kỳ / follower đầu kỳ | Thiếu follower đầu kỳ thì dùng (cuối kỳ − follower mới) |
| Reach / lượt xem | số trong kỳ, so kỳ trước (%) | TikTok, YouTube dùng lượt xem; Facebook, IG, Threads dùng reach (người tiếp cận) |
| Tỷ lệ tương tác (ER) | tương tác / reach (hoặc / lượt xem) × 100 | Đối thủ: trung bình (tương tác / lượt xem) mỗi bài nếu có view; nếu không thì tương tác trung bình mỗi bài / follower |
| Tần suất đăng | số bài / số tuần trong kỳ | So với ngưỡng tối thiểu ở `nguong.json` |
| Lead | lead theo utm_source của kênh (LadiPage) | Lead Paid tách riêng |
| CPL | chi phí ads của kênh / lead Paid | Chỉ khi có cả hai số |
| Lead / 1.000 reach | lead organic / reach × 1.000 | Đo kênh organic ra lead tốt cỡ nào |
| Nội dung thắng | top 5 bài theo tương tác (hoặc view), định dạng và chủ đề chạy tốt | Từ danh sách bài trong kỳ |

## 3. Chấm từng chỉ số: Tốt / Trung bình / Yếu
Mỗi chỉ số so với **3 mốc** (mốc nào thiếu số thì bỏ, không đoán):
1. Kỳ trước của chính kênh: tăng ≥ 10% là Tốt, giảm quá 10% là Yếu.
2. Trung vị đối thủ cùng nền tảng (chỉ số công khai): ≥ trung vị là Tốt, dưới nửa trung vị là Yếu.
3. Ngưỡng ngành ở `nguong.json` (chỉ cho tỷ lệ tương tác và tần suất).

Điểm mỗi chỉ số = trung bình các mốc có số (Tốt = 2, Trung bình = 1, Yếu = 0).
Ngưỡng nằm ở `${CLAUDE_PLUGIN_ROOT}/references/nguong.json`, sửa ở đó.

## 4. Kết luận đề xuất cho kênh
Script đưa ra kết luận sơ bộ theo luật dưới, agent đọc lại cùng bối cảnh (nguồn lực, mục tiêu) rồi viết lý do.
| Kết luận | Khi nào |
| --- | --- |
| **Đẩy mạnh** | Chỉ số chính Tốt, và không chỉ số phụ nào Yếu. Kênh đang chạy, đáng thêm nguồn lực |
| **Giữ** | Chỉ số chính Trung bình hoặc Tốt, có chỉ số phụ Yếu. Giữ nhịp, sửa điểm yếu nhỏ |
| **Tối ưu** | Chỉ số chính Yếu nhưng có ít nhất một chỉ số khác Trung bình trở lên, hoặc có bài thắng rõ. Kênh có tiềm năng nhưng đang làm sai cách |
| **Bỏ / tạm dừng** | Chỉ số chính Yếu và không còn chỉ số nào khá, trong khi kênh vẫn tốn nguồn lực. Chỉ đề xuất, người dùng quyết |
| **Chưa đủ dữ liệu** | Dưới 5 bài trong kỳ, hoặc thiếu chỉ số chính |

Agent được đổi kết luận sơ bộ khi có lý do (ví dụ kênh mới mở 1 tháng, mục tiêu kỳ khác),
nhưng phải ghi rõ "đổi từ X sang Y vì ...".

## 5. Mỗi kênh trả lời đủ 5 câu
1. Kênh đang làm đúng vai trò chưa? (số chính so 3 mốc)
2. Đang tăng hay giảm so với kỳ trước?
3. Đứng ở đâu so với đối thủ cùng nền tảng?
4. Nội dung nào thắng, nội dung nào nên bỏ? (định dạng, chủ đề, hook)
5. Kết luận + 2–3 việc cụ thể kỳ tới (làm được với nguồn lực hiện có).

## 6. Phần tổng hợp toàn hệ kênh
- Phễu đang hở ở đâu: nhiều nhận biết mà ít chuyển đổi, hay ngược lại.
- Kênh nào đang ăn nhiều nguồn lực mà đóng góp ít (số bài cao, kết quả thấp).
- Đối thủ mạnh ở kênh nào mà mình đang bỏ trống.
- 3 ưu tiên cho kỳ tới. Đây là đầu vào cho Masterplan và plan quý/tháng.
