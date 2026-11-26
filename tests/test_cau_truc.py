"""Kiểm thử CẤU TRÚC repo: frontmatter skill/subagent, đủ 8 phần A–H cho skill nghiên cứu, đường dẫn tham chiếu tồn tại,
schema nhất quán, mọi ví dụ trong templates/kho nạp sạch vào kho, phiên bản plugin khớp, không có dữ liệu nhạy cảm."""
import glob
import json
import os
import re
import unittest

from tro_giup import GOC, KhoTam

SKILL_NGHIEN_CUU = ["research", "company-analysis", "xu-huong-mua-vu", "customer-research", "competitor-research", "tu-khoa",
                    "nghien-cuu-content", "format-sang-tao", "quang-cao-chuyen-doi", "kenh-cong-dong", "insight",
                    "marketing-opportunities", "san-pham-uu-dai", "dinh-vi-thong-diep", "y-tuong-content", "y-tuong-quang-cao",
                    "y-tuong-chien-dich", "toi-uu-chuyen-doi", "kiem-chung", "kho-du-lieu"]
NEN_TANG = ["google-search", "google-trends", "tiktok", "facebook", "threads", "youtube", "instagram", "meta-ads-library",
            "tiktok-creative-center", "google-maps", "website-landing-page", "san-tmdt", "crm-noi-bo"]


def doc(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def frontmatter(p):
    s = doc(p)
    m = re.match(r"^---\n(.*?)\n---\n", s, re.S)
    if not m:
        return {}
    kq = {}
    for dong in m.group(1).splitlines():
        if ":" in dong and not dong.startswith(" "):
            k, v = dong.split(":", 1)
            kq[k.strip()] = v.strip()
    return kq


class TestCauTruc(unittest.TestCase):
    def test_frontmatter_skill(self):
        for p in glob.glob(os.path.join(GOC, "skills", "*", "SKILL.md")):
            ten = os.path.basename(os.path.dirname(p))
            fm = frontmatter(p)
            self.assertEqual(fm.get("name"), ten, p)
            self.assertGreater(len(fm.get("description", "")), 80, f"{ten}: description quá ngắn")
            self.assertRegex(ten, r"^[a-z0-9]+(-[a-z0-9]+)*$")

    def test_skill_nghien_cuu_du_8_phan(self):
        for ten in SKILL_NGHIEN_CUU:
            p = os.path.join(GOC, "skills", ten, "SKILL.md")
            self.assertTrue(os.path.isfile(p), f"thiếu skill {ten}")
            s = doc(p)
            for chu in "ABCDEFGH":
                self.assertRegex(s, rf"\n## {chu}\. ", f"{ten}: thiếu phần {chu}")
            self.assertIn("kho.py", s, f"{ten}: không nói cách ghi/đọc kho")
            self.assertRegex(s, r"\| *Bước *\|", f"{ten}: quy trình chưa ở dạng bảng Bước")
            self.assertIn("- [ ]", s, f"{ten}: thiếu checklist")
            so_dong = s.count("\n")
            self.assertGreater(so_dong, 60, f"{ten}: SKILL.md quá sơ sài ({so_dong} dòng)")

    def test_subagent(self):
        mong_doi = {"customer-researcher", "competitor-researcher", "market-researcher", "content-researcher", "research-verifier"}
        co = set()
        for p in glob.glob(os.path.join(GOC, "agents", "*.md")):
            fm = frontmatter(p)
            ten = os.path.basename(p)[:-3]
            self.assertEqual(fm.get("name"), ten)
            self.assertTrue(fm.get("description"))
            co.add(ten)
        self.assertEqual(co, mong_doi)

    def test_duong_dan_tham_chieu_ton_tai(self):
        thieu = []
        files = glob.glob(os.path.join(GOC, "skills", "*", "SKILL.md")) + glob.glob(os.path.join(GOC, "agents", "*.md")) \
            + glob.glob(os.path.join(GOC, "references", "**", "*.md"), recursive=True) + [os.path.join(GOC, "README.md"), os.path.join(GOC, "HUONG-DAN.md")]
        for p in files:
            for m in re.finditer(r"\$\{CLAUDE_PLUGIN_ROOT\}/([\w./\-]+)", doc(p)):
                rel = m.group(1).rstrip(".,;:)")
                if "<" in rel or rel.endswith("/"):
                    if not os.path.exists(os.path.join(GOC, rel.split("<")[0])):
                        thieu.append(f"{os.path.relpath(p, GOC)} → {rel}")
                    continue
                if not os.path.exists(os.path.join(GOC, rel)):
                    thieu.append(f"{os.path.relpath(p, GOC)} → {rel}")
        self.assertEqual(thieu, [], "\n".join(thieu))

    def test_tai_lieu_nen_tang(self):
        for t in NEN_TANG:
            p = os.path.join(GOC, "references", "nen-tang", f"{t}.md")
            self.assertTrue(os.path.isfile(p), t)
            self.assertIn("EVD", doc(p), f"{t}: không nói ghi bằng chứng gốc")

    def test_schema_nhat_quan(self):
        sc = json.loads(doc(os.path.join(GOC, "templates", "kho", "schema.json")))
        loai = sc["loai"]
        for k, v in loai.items():
            for c in v["cha"]:
                self.assertIn(c, loai, f"{k}: cha {c} không tồn tại")
            for t in v.get("gia_tri", {}):
                self.assertIn(t, v["bat_buoc"] + v.get("tuy_chon", []), f"{k}: trường giá trị {t} không có")
            if v["skill"] != "*":
                self.assertTrue(os.path.isfile(os.path.join(GOC, "skills", v["skill"], "SKILL.md")), f"{k}: skill {v['skill']} không có")
        for k, ds in sc["khoa_trung"].items():
            for t in ds:
                self.assertIn(t, loai[k]["bat_buoc"] + loai[k].get("tuy_chon", []), f"khoá trùng {k}.{t}")
        for ma in ["EVD", "FIND", "SEG", "INS", "OPP", "KEY", "IDEA", "FMT", "ADS", "CAM", "OFFER", "CRO"]:
            self.assertIn(ma, loai, f"thiếu mã bắt buộc {ma}")

    def test_vi_du_nap_sach(self):
        files = glob.glob(os.path.join(GOC, "templates", "kho", "vi-du*.json")) + glob.glob(os.path.join(GOC, "templates", "kho", "vi-du", "*.json"))
        self.assertGreater(len(files), 1)
        for p in files:
            k = KhoTam()
            try:
                code, out = k.them_file(p)
                self.assertEqual(code, 0, f"{os.path.basename(p)}: {out}")
                _, loi, _ = k.kiem_tra()
                self.assertEqual(loi, [], f"{os.path.basename(p)}:\n" + "\n".join(loi))
            finally:
                k.dong()

    def test_phien_ban_khop(self):
        pj = json.loads(doc(os.path.join(GOC, ".claude-plugin", "plugin.json")))
        mk = json.loads(doc(os.path.join(GOC, ".claude-plugin", "marketplace.json")))
        self.assertEqual(pj["version"], mk["plugins"][0]["version"])
        self.assertIn(f"## {pj['version']}", doc(os.path.join(GOC, "CHANGELOG.md")))

    def test_khong_du_lieu_nhay_cam(self):
        mau = re.compile(r"drive\.google\.com/|notion\.(so|com)/|docs\.google\.com/spreadsheets/d/1|@runbylinh\.com|linhtran", re.I)
        vi_pham = []
        for p in glob.glob(os.path.join(GOC, "**", "*"), recursive=True):
            if "/.git/" in p or not os.path.isfile(p) or p.endswith((".pyc", ".png", ".jpg", "test_cau_truc.py")):
                continue
            try:
                s = doc(p)
            except UnicodeDecodeError:
                continue
            for m in mau.finditer(s):
                vi_pham.append(f"{os.path.relpath(p, GOC)}: {m.group(0)}")
        self.assertEqual(vi_pham, [], "\n".join(vi_pham))


if __name__ == "__main__":
    unittest.main()
