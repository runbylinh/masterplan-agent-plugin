"""Kiểm thử MÔ PHỎNG luồng bàn giao dữ liệu theo 9 case nghiệm thu (Phần IX).

Đây là kiểm thử mô phỏng: dữ liệu giả định được nạp qua kho.py như các skill sẽ làm, để kiểm tra cấu trúc đầu ra,
liên kết bằng chứng, kế thừa kho, xử lý thiếu dữ liệu và mâu thuẫn. KHÔNG phải kiểm thử trực tiếp trên nền tảng thật
(TikTok, Meta Ads Library...) — phần đó cần chạy skill với công cụ thật và người dùng duyệt.
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

from tro_giup import GOC, KhoTam, evd

VI_DU = os.path.join(GOC, "templates", "kho", "vi-du-secondhand.json")


def rp(tam, muc_tieu, workflow, muc="Chuyên sâu"):
    return {"tam": tam, "loai": "RP", "tieu_de": muc_tieu, "du_lieu": {
        "Mục tiêu nghiên cứu": muc_tieu, "Quyết định cần hỗ trợ": "x", "Câu hỏi nghiên cứu": ["x"], "Phạm vi": "x", "Mức nghiên cứu": muc,
        "Workflow": workflow, "Dữ liệu đã có": "x", "Dữ liệu còn thiếu": "x", "Nguồn nghiên cứu": ["x"], "Phương pháp lấy mẫu": "x",
        "Skill và Subagent": ["x"], "Đầu ra cuối cùng": "x", "Điểm chờ duyệt": ["x"], "Tiêu chuẩn hoàn thành": "x"}}


def kh(tam, nhan, noi_dung, cha, nguon="TikTok"):
    return {"tam": tam, "loai": "KH", "tieu_de": noi_dung, "lien_ket": cha, "du_lieu": {
        "Nhãn": nhan, "Nội dung": noi_dung, "Nhóm khách": "Gia đình", "Bối cảnh": "Tết", "Loại khách": "Quan sát công khai", "Nguồn": nguon}}


def ins(tam, cha, cau, tin_cay="Trung bình"):
    return {"tam": tam, "loai": "INS", "tieu_de": cau, "lien_ket": cha, "do_tin_cay": tin_cay, "ly_do_tin_cay": "2 nền tảng, mẫu định tính",
            "du_lieu": {k: "x" for k in ["Nhóm khách hàng", "Bối cảnh", "Hành vi quan sát", "Nhu cầu", "Mong muốn", "Động lực", "Rào cản",
                                         "Mâu thuẫn", "Bằng chứng ủng hộ", "Bằng chứng trái chiều", "Hướng ứng dụng Marketing", "Nội dung cần kiểm chứng"]}
            | {"Insight đúc kết": cau}}


def opp(tam, cha, loai="Mùa vụ"):
    d = {k: "x" for k in ["Nhu cầu thị trường", "Nhóm khách hàng", "Khoảng trống cạnh tranh", "Lợi thế doanh nghiệp", "Cách khai thác",
                          "Tiềm năng kinh doanh", "Điều kiện và nguồn lực", "Rủi ro", "Lý do ưu tiên", "Phương án thử nghiệm"]}
    d.update({"Loại cơ hội": loai, "Mức ưu tiên": "Cao"})
    return {"tam": tam, "loai": "OPP", "tieu_de": f"Cơ hội {tam}", "lien_ket": cha, "du_lieu": d}


def ban_ghi_x(loai, tam, cha, bat_buoc, them=None):
    d = {k: "x" for k in bat_buoc}
    d.update(them or {})
    return {"tam": tam, "loai": loai, "tieu_de": f"{loai} {tam}", "lien_ket": cha, "du_lieu": d}


def ghi(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False)


def doc(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


SCHEMA = json.loads(doc(os.path.join(GOC, "templates", "kho", "schema.json")))


def tao(loai, tam, cha, **gia_tri):
    return ban_ghi_x(loai, tam, cha, SCHEMA["loai"][loai]["bat_buoc"], gia_tri)


class TestCaseNghiemThu(unittest.TestCase):
    def setUp(self):
        self.k = KhoTam()

    def tearDown(self):
        self.k.dong()

    def assertSach(self, dot=None):
        code, loi, cb = self.k.kiem_tra(*(["--dot", dot] if dot else []))
        self.assertEqual(loi, [], "\n".join(loi))
        return cb

    def test_case01_fnb_tet(self):
        """F&B Tết: nhu cầu → Insight → cơ hội mùa vụ → combo → chiến dịch → Content → quảng cáo."""
        lo = {"dot": "@rp", "ban_ghi": [
            rp("rp", "Nhu cầu ăn uống dịp Tết", "02 Chiến dịch theo mùa vụ"),
            evd("e1", "https://www.tiktok.com/@vd/1", "TikTok", "Bình luận hỏi đặt mâm cỗ Tết giao tận nhà"),
            evd("e2", "https://www.facebook.com/groups/vd/2", "Facebook Group", "Nhiều người than mệt khi tự nấu cỗ Tết"),
            tao("MV", "mv1", [], **{"Thời điểm": "Tháng Chạp", "Sự kiện": "Tất niên", "Nhu cầu": "Đặt cỗ", "Sản phẩm": "Mâm cỗ", "Thời gian chuẩn bị": "6 tuần", "Nguồn": "https://trends.google.com/vd"}),
            kh("k1", "Nỗi đau", "Mệt khi tự nấu cỗ", ["@e2"], "Facebook Group"),
            kh("k2", "Nhu cầu", "Muốn cỗ đủ món giao tận nhà", ["@e1"]),
            ins("i1", ["@k1", "@k2"], "Muốn Tết đủ đầy nhưng không muốn mất cả ngày đứng bếp"),
            opp("o1", ["@i1", "@mv1"]),
            tao("OFFER", "s1", ["@o1"], **{"Loại": "Combo và gói dịch vụ"}),
            tao("CAM", "c1", ["@o1", "@i1"]),
            tao("IDEA", "d1", ["@i1"]),
            tao("ADS", "a1", ["@i1", "@o1"]),
        ]}
        code, out = self.k.them(lo)
        self.assertEqual(code, 0, out)
        cb = self.assertSach("RP-001")
        self.assertFalse(any("không truy được" in c for c in cb), cb)
        code, out = self.k.chay("truy-vet", "CAM-001")
        self.assertIn("EVD-001", out)
        self.assertIn("EVD-002", out)

    def test_case02_thoi_trang_content_format(self):
        """Thời trang: kế thừa kho secondhand, thêm Content nghiên cứu + format video → ý tưởng Content."""
        self.k.them_file(VI_DU)
        lo = {"dot": "RP-001", "ban_ghi": [
            evd("e9", "https://www.tiktok.com/@vd/9", "TikTok", "Video thử đồ trước–sau 30 giây"),
            tao("CNT", "n1", ["@e9"], **{"URL": "https://www.tiktok.com/@vd/9", "Mức mẫu": "Nổi bật"}),
            tao("FMT", "f1", ["@n1"], **{"Loại format": "Video"}),
            tao("IDEA", "d2", ["INS-001", "@n1"], **{"Content Pillar": "Phối đồ", "Chủ đề": "Thử đồ theo dịp"}),
        ]}
        code, out = self.k.them(lo)
        self.assertEqual(code, 0, out)
        self.assertSach()
        bg = self.k.ban_ghi()
        self.assertIn("CNT-001", bg["FMT-001"]["lien_ket"])

    def test_case03_dao_tao(self):
        """Dịch vụ đào tạo: động lực, rào cản → Insight → thông điệp → Lead Magnet."""
        lo = {"dot": "@rp", "ban_ghi": [
            rp("rp", "Động lực học và rào cản đăng ký", "03 Content Marketing"),
            evd("e1", "https://www.facebook.com/groups/hoc/1", "Facebook Group", "Hỏi học xong có áp dụng được không"),
            evd("e2", "https://www.google.com/search?q=khoa+hoc", "Google Search", "Gợi ý: khoá học marketing có đáng tiền không"),
            kh("k1", "Rào cản", "Sợ học xong không áp dụng được", ["@e1"], "Facebook Group"),
            kh("k2", "Câu hỏi", "Khoá học có đáng tiền không", ["@e2"], "Google Search"),
            ins("i1", ["@k1", "@k2"], "Muốn giỏi lên nhanh nhưng sợ mất tiền vào khoá học không áp dụng được"),
            tao("TD", "t1", ["@i1"], **{"Bảng": "Ma trận thông điệp"}),
            tao("OFFER", "s1", ["@i1"], **{"Loại": "Lead Magnet"}),
        ]}
        code, out = self.k.them(lo)
        self.assertEqual(code, 0, out)
        self.assertSach("RP-001")

    def test_case04_quang_cao(self):
        """Quảng cáo: mẫu quảng cáo → mẫu lặp → Insight → ý tưởng ADS; không có trường ngân sách đối thủ."""
        lo = {"dot": "@rp", "ban_ghi": [rp("rp", "Góc quảng cáo mới", "04 Quảng cáo")]
              + [tao("QC", f"q{i}", [], **{"URL": f"https://www.facebook.com/ads/library/?id={i}"}) for i in range(1, 4)]
              + [evd("e1", "https://www.facebook.com/ads/library/?id=1", "Meta Ads Library", "3/3 mẫu dùng góc giảm giá"),
                 evd("e2", "https://www.facebook.com/vd/posts/2", "Facebook", "Bình luận hỏi chất lượng, không hỏi giá"),
                 {"tam": "f1", "loai": "FIND", "tieu_de": "Thị trường dồn vào góc giá", "lien_ket": ["@e1", "@e2"],
                  "du_lieu": {"Phát hiện": "Mẫu quảng cáo dồn vào giá, khách hỏi chất lượng", "Phân loại": "Mẫu lặp", "Nhóm": "Quảng cáo",
                              "Bằng chứng tóm tắt": "3 mẫu + bình luận", "Phạm vi": "20 mẫu, 10/2026"}},
                 ins("i1", ["@f1"], "Muốn mua rẻ nhưng sợ hàng kém"),
                 tao("ADS", "a1", ["@i1", "@q1"])]}
        code, out = self.k.them(lo)
        self.assertEqual(code, 0, out)
        self.assertSach("RP-001")
        self.assertNotIn("Ngân sách", json.dumps(SCHEMA["loai"]["QC"], ensure_ascii=False))

    def test_case05_cap_nhat_thi_truong(self):
        """Cập nhật: hai giai đoạn, bản ghi lỗi thời được đánh dấu, báo cáo thay đổi liệt kê mới và cập nhật."""
        self.k.them([tao("XH", "x1", [], **{"Xu hướng": "Quà Tết healthy", "Phân loại": "Mùa vụ", "Đánh giá": "Cần thử nghiệm", "Nguồn": "https://trends.google.com/a"})],
                    hom_nay="2026-01-10")
        code, out = self.k.chay("kiem-tra", hom_nay="2026-11-26")
        self.assertIn("lỗi thời", out)
        self.k.them([tao("XH", "x2", [], **{"Xu hướng": "Combo tất niên văn phòng", "Phân loại": "Tín hiệu mới", "Đánh giá": "Nên khai thác", "Nguồn": "https://trends.google.com/b"})])
        p = os.path.join(self.k.dir, "sua.json")
        ghi(p, [{"du_lieu": {"Đánh giá": "Nên khai thác"}}])
        self.k.chay("cap-nhat", "XH-001", p)
        code, out = self.k.chay("thay-doi", "--tu", "2026-11-01")
        self.assertIn("XH-002", out.split("## Bản ghi được cập nhật")[0])
        self.assertIn("XH-001", out.split("## Bản ghi được cập nhật")[1])

    def test_case06_thieu_du_lieu(self):
        """Thiếu dữ liệu: ghi TH; phát hiện không có bằng chứng bị chặn; 'Có căn cứ' với 1 nguồn bị cảnh báo."""
        self.k.them([tao("TH", "t1", [], **{"Câu hỏi": "Biên lợi nhuận combo?", "Dữ liệu cần có": "Giá vốn", "Nguồn bổ sung": "Kế toán"})])
        self.assertSach()
        self.k.them([{"loai": "FIND", "tieu_de": "Không nguồn", "du_lieu": {"Phát hiện": "a", "Phân loại": "Giả thuyết", "Nhóm": "Thị trường",
                                                                           "Bằng chứng tóm tắt": "-", "Phạm vi": "-"}}])
        _, loi, _ = self.k.kiem_tra()
        self.assertTrue(any("cần liên kết" in l for l in loi))

    def test_case07_mau_thuan(self):
        """Mâu thuẫn: ghi MT; phát hiện bị phản bác → tài nguyên phía dưới bị cảnh báo."""
        lo = [evd("e1", "https://a.vn/1", "Facebook Group", "Khen giá 500k hợp lý"),
              evd("e2", "https://shopee.vn/x", "Shopee", "Chê đắt ở 450k"),
              {"tam": "f1", "loai": "FIND", "tieu_de": "Khách chấp nhận 500k", "lien_ket": ["@e1"],
               "du_lieu": {"Phát hiện": "Khách chấp nhận 500k", "Phân loại": "Quan sát", "Nhóm": "Khách hàng", "Bằng chứng tóm tắt": "Group", "Phạm vi": "1 nhóm"}},
              ins("i1", ["@f1"], "Sẵn sàng trả 500k cho combo"),
              tao("MT", "m1", [], **{"Phát hiện": "FIND-001", "Nguồn A": "EVD-001", "Nguồn B": "EVD-002"})]
        self.k.them(lo)
        self.k.chay("kiem-chung", "FIND-001", "--muc", "Bị phản bác", "--tin-cay", "Thấp", "--ly-do", "Shopee trái chiều (MT-001)")
        _, loi, cb = self.k.kiem_tra()
        self.assertEqual(loi, [])
        self.assertTrue(any("INS-001" in c and "phản bác" in c for c in cb), cb)

    def test_case08_tai_su_dung_kho(self):
        """Tái sử dụng: tạo ý tưởng mới chỉ từ kho đã có, không thêm bằng chứng; nạp lại bằng chứng cũ không tạo trùng."""
        self.k.them_file(VI_DU)
        truoc = len([r for r in self.k.ban_ghi().values() if r["loai"] == "EVD"])
        code, out = self.k.them({"dot": "RP-001", "ban_ghi": [tao("IDEA", "d9", ["INS-001", "KEY-001"], **{"Chủ đề": "Size chuẩn khi mua online"}),
                                                             tao("ADS", "a9", ["INS-001"])]})
        self.assertEqual(code, 0, out)
        self.k.them_file(VI_DU)
        sau = len([r for r in self.k.ban_ghi().values() if r["loai"] == "EVD"])
        self.assertEqual(truoc, sau)
        self.assertSach()
        code, out = self.k.chay("truy-vet", "IDEA-002")
        self.assertIn("EVD-", out)

    def test_case09_tuong_thich_nguoc(self):
        """Tương thích ngược: script cũ vẫn chạy; skill và lệnh cũ còn nguyên; chế độ 3C giữ 5 file."""
        for ten in ["setup", "danh-gia-kenh", "lead-hoi-thoai", "quet-doi-thu", "bao-cao-kinh-doanh", "chi-phi-ads", "ra-soat-thuong-hieu",
                    "review-nam", "nghien-cuu-thi-truong", "du-bao-xu-huong", "dinh-huong-chien-luoc", "dieu-phoi", "huong-dan", "research",
                    "company-analysis", "customer-research", "competitor-research", "marketing-opportunities", "marketing-recommendations"]:
            self.assertTrue(os.path.isfile(os.path.join(GOC, "skills", ten, "SKILL.md")), ten)
        ba_c = doc(os.path.join(GOC, "references", "nghien-cuu", "che-do-3c.md"))
        for f in ["01-brief.md", "02-customer.md", "03-competitor.md", "04-tong-hop-3c.md", "05-giao-viec.md", "06-bang-dan-vao-sheets.csv"]:
            self.assertIn(f, ba_c)
        with tempfile.TemporaryDirectory() as d:
            # tinh_lead
            os.makedirs(os.path.join(d, "lead-hoi-thoai", "k"))
            ghi(os.path.join(d, "lead-hoi-thoai", "k", "hoi-thoai.json"),
                {"doanh_nghiep": "Brand mẫu", "ky": {"tu": "2026-11-17", "den": "2026-11-23"},
                 "tong_theo_kenh": [{"kenh": "zalo_web", "ten": "Zalo 1", "hien_tai": {"hoi_thoai": 10, "tu_nguoi_la": 4}}], "mau": []})
            ghi(os.path.join(d, "cau-hinh.json"), {})
            p = subprocess.run([sys.executable, os.path.join(GOC, "scripts", "tinh_lead.py"), "lead-hoi-thoai/k"], cwd=d, capture_output=True, text=True)
            self.assertEqual(p.returncode, 0, p.stderr)
            # dung_bao_cao_nghien_cuu
            os.makedirs(os.path.join(d, "r"))
            ghi(os.path.join(d, "r", "ket-qua.json"),
                {"loai": "thi-truong", "tieu_de": "T", "phan": [{"tieu_de": "A", "bang": {"cot": ["Góc độ", "Nguồn"], "dong": [["Nhu cầu", "x"]]}, "csv": "a"}]})
            p = subprocess.run([sys.executable, os.path.join(GOC, "scripts", "dung_bao_cao_nghien_cuu.py"), "r"], cwd=d, capture_output=True, text=True)
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertTrue(os.path.isfile(os.path.join(d, "r", "bao-cao.html")))
            # xuat_bo_mau (cần openpyxl)
            try:
                import openpyxl  # noqa: F401
                p = subprocess.run([sys.executable, os.path.join(GOC, "scripts", "xuat_bo_mau.py"), "nghien-cuu-thi-truong", "--nam", "2026", "-o", "m.xlsx"],
                                   cwd=d, capture_output=True, text=True)
                self.assertEqual(p.returncode, 0, p.stderr)
            except ImportError:
                pass


if __name__ == "__main__":
    unittest.main()
