"""Kiểm thử đơn vị scripts/kho.py (Skill 20 – kho dữ liệu)."""
import os
import unittest

from tro_giup import GOC, KhoTam, evd

VI_DU = os.path.join(GOC, "templates", "kho", "vi-du-secondhand.json")


def find(tam, cha, phat_hien="Khách lo không vừa size", **kw):
    r = {"tam": tam, "loai": "FIND", "tieu_de": phat_hien, "lien_ket": cha,
         "du_lieu": {"Phát hiện": phat_hien, "Phân loại": "Mẫu lặp", "Nhóm": "Khách hàng", "Bằng chứng tóm tắt": "x", "Phạm vi": "Hà Nội"}}
    r.update(kw)
    return r


class TestKho(unittest.TestCase):
    def setUp(self):
        self.k = KhoTam()

    def tearDown(self):
        self.k.dong()

    def test_vi_du_day_du_sach(self):
        code, out = self.k.them_file(VI_DU)
        self.assertEqual(code, 0, out)
        code, loi, cb = self.k.kiem_tra()
        self.assertEqual(code, 0)
        self.assertEqual(loi, [])
        self.assertEqual(cb, [])
        bg = self.k.ban_ghi()
        self.assertIn("CAM-001", bg)
        self.assertTrue(all(r["dot"] == "RP-001" for r in bg.values() if r["loai"] != "RP"))

    def test_cap_ma_va_lien_ket_tam(self):
        self.k.them([evd("e1", "https://a.vn/1", "TikTok", "Bình luận hỏi size"), find("f1", ["@e1"])])
        bg = self.k.ban_ghi()
        self.assertEqual(bg["FIND-001"]["lien_ket"], ["EVD-001"])

    def test_chong_trung(self):
        lo = [evd("e1", "https://a.vn/1", "TikTok", "Bình luận hỏi size"), find("f1", ["@e1"])]
        self.k.them(lo)
        code, out = self.k.them(lo)
        self.assertIn("Trùng", out)
        self.assertEqual(len(self.k.ban_ghi()), 2)

    def test_thieu_truong_va_gia_tri_sai(self):
        self.k.them([{"loai": "KEY", "tieu_de": "x", "du_lieu": {"Từ khóa": "x", "Mục đích tìm kiếm": "Mua bán"}}])
        code, loi, _ = self.k.kiem_tra()
        self.assertEqual(code, 1)
        self.assertTrue(any("thiếu trường bắt buộc" in l for l in loi))
        self.assertTrue(any("Mục đích tìm kiếm" in l and "không thuộc" in l for l in loi))

    def test_thieu_cha_bat_buoc(self):
        self.k.them([find("f1", [])])
        _, loi, _ = self.k.kiem_tra()
        self.assertTrue(any("cần liên kết" in l for l in loi))

    def test_lien_ket_hong(self):
        self.k.them([find("f1", ["EVD-099"])])
        _, loi, _ = self.k.kiem_tra()
        self.assertTrue(any("không tồn tại" in l for l in loi))

    def test_du_lieu_ca_nhan_bi_chan(self):
        self.k.them([evd("e1", "https://a.vn/1", "Facebook", "Khách để lại số 0912 345 678 hỏi giá")])
        _, loi, _ = self.k.kiem_tra()
        self.assertTrue(any("ẩn danh" in l for l in loi))
        self.k.them([evd("e2", "https://a.vn/2", "Facebook", "liên hệ abc@vidu.vn")])
        _, loi, _ = self.k.kiem_tra()
        self.assertGreaterEqual(sum("ẩn danh" in l for l in loi), 2)

    def test_co_can_cu_can_hai_nguon_doc_lap(self):
        self.k.them([evd("e1", "https://a.vn/1", "TikTok", "A"), evd("e2", "https://a.vn/2", "TikTok", "B"),
                     find("f1", ["@e1", "@e2"])])
        self.k.chay("kiem-chung", "FIND-001", "--muc", "Có căn cứ", "--ly-do", "2 video")
        _, _, cb = self.k.kiem_tra()
        self.assertTrue(any("nguồn độc lập" in l for l in cb), cb)
        self.k.them([evd("e3", "https://b.vn/1", "Shopee", "C")])
        self.k.chay("cap-nhat", "FIND-001", self._ghi({"lien_ket": ["EVD-003"]}))
        _, _, cb = self.k.kiem_tra()
        self.assertFalse(any("nguồn độc lập" in l for l in cb), cb)

    def test_khong_ghi_de_ban_da_duyet(self):
        self.k.them([evd("e1", "https://a.vn/1", "TikTok", "A"), find("f1", ["@e1"])])
        self.k.chay("duyet", "FIND-001", "--trang-thai", "Đã duyệt")
        code, out = self.k.chay("cap-nhat", "FIND-001", self._ghi({"du_lieu": {"Phạm vi": "Toàn quốc"}}))
        self.assertEqual(code, 1)
        self.assertIn("đã được duyệt", out)
        code, _ = self.k.chay("cap-nhat", "FIND-001", self._ghi({"du_lieu": {"Phạm vi": "Toàn quốc"}}), "--sua-ban-da-duyet")
        self.assertEqual(code, 0)
        r = self.k.ban_ghi()["FIND-001"]
        self.assertEqual(r["trang_thai"], "Chờ duyệt")
        self.assertTrue(any("sửa bản đã duyệt" in h["thay_doi"] for h in r["lich_su"]))

    def test_tin_cay_can_ly_do(self):
        self.k.them([evd("e1", "https://a.vn/1", "TikTok", "A"), find("f1", ["@e1"], do_tin_cay="Cao")])
        _, _, cb = self.k.kiem_tra()
        self.assertTrue(any("chưa ghi lý do" in l for l in cb))

    def test_loi_thoi(self):
        self.k.them([{"tam": "x", "loai": "XH", "tieu_de": "Xu hướng A", "du_lieu": {"Xu hướng": "A", "Mô tả": "a", "Thời điểm": "11/2026",
                     "Nhóm khách": "SV", "Phân loại": "Ngắn hạn", "Đánh giá": "Cần thử nghiệm", "Nguồn": "https://trends.google.com/x"}}])
        _, _, cb = self.k.kiem_tra()
        self.assertFalse(any("lỗi thời" in l for l in cb))
        code, out = self.k.chay("kiem-tra", hom_nay="2027-03-01")
        self.assertIn("lỗi thời", out)

    def test_truy_vet_va_xuat_bao_cao(self):
        self.k.them_file(VI_DU)
        code, out = self.k.chay("truy-vet", "CAM-001")
        self.assertEqual(code, 0)
        self.assertIn("EVD-001", out)
        self.assertIn("Nguồn độc lập phía trên: 3", out)
        code, out = self.k.chay("xuat", "--ra", "xuat")
        files = os.listdir(os.path.join(self.k.dir, "xuat"))
        self.assertIn("KH-kho-rao-can.csv", files)
        self.assertIn("INS-insight.csv", files)
        code, out = self.k.chay("bao-cao", "--dot", "RP-001", "--ra", "bc")
        with open(os.path.join(self.k.dir, "bc", "bao-cao.md"), encoding="utf-8") as f:
            md = f.read()
        self.assertIn("Truy vết tài nguyên", md)
        self.assertIn("CAM-001", md)

    def test_tien_do_va_thay_doi(self):
        self.k.them_file(VI_DU)
        code, out = self.k.chay("tien-do", "--dot", "RP-001")
        self.assertIn("Chuyên sâu", out)
        code, out = self.k.chay("thay-doi", "--tu", "2026-11-26")
        self.assertIn("Bản ghi mới (24)", out)

    def _ghi(self, obj):
        import json
        p = os.path.join(self.k.dir, f"sua-{abs(hash(json.dumps(obj, ensure_ascii=False)))}.json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump([obj], f, ensure_ascii=False)
        return p


if __name__ == "__main__":
    unittest.main()
