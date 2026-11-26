"""Hàm dùng chung cho bộ kiểm thử (chạy: python3 -m unittest discover -s tests -v)."""
import json
import os
import subprocess
import sys
import tempfile

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KHO_PY = os.path.join(GOC, "scripts", "kho.py")


class KhoTam:
    """Một thư mục làm việc tạm với kho riêng; chạy kho.py qua subprocess như agent thật."""

    def __init__(self, hom_nay="2026-11-26"):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = self.tmp.name
        self.hom_nay = hom_nay

    def chay(self, *args, hom_nay=None):
        env = dict(os.environ, KHO_HOM_NAY=hom_nay or self.hom_nay)
        p = subprocess.run([sys.executable, KHO_PY, *args], cwd=self.dir, env=env, capture_output=True, text=True)
        return p.returncode, p.stdout + p.stderr

    def them(self, lo, dot=None, hom_nay=None):
        path = os.path.join(self.dir, f"lo-{abs(hash(json.dumps(lo, ensure_ascii=False)))}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(lo, f, ensure_ascii=False)
        args = ["them", path] + (["--dot", dot] if dot else [])
        return self.chay(*args, hom_nay=hom_nay)

    def them_file(self, path, hom_nay=None):
        return self.chay("them", path, hom_nay=hom_nay)

    def ban_ghi(self):
        kq = {}
        kdir = os.path.join(self.dir, "kho")
        if os.path.isdir(kdir):
            for ten in os.listdir(kdir):
                if ten.endswith(".jsonl"):
                    with open(os.path.join(kdir, ten), encoding="utf-8") as f:
                        for d in f:
                            if d.strip():
                                r = json.loads(d)
                                kq[r["id"]] = r
        return kq

    def kiem_tra(self, *extra):
        code, out = self.chay("kiem-tra", *extra)
        loi = [l for l in out.splitlines() if l.startswith("LỖI")]
        cb = [l for l in out.splitlines() if l.startswith("CẢNH BÁO")]
        return code, loi, cb

    def dong(self):
        self.tmp.cleanup()


def evd(tam, nguon, nen_tang, noi_dung, **them):
    d = {"Nguồn": nguon, "Nền tảng": nen_tang, "Ngày thu thập": "2026-11-26", "Nội dung quan sát": noi_dung, "Loại nguồn": "Công khai"}
    d.update(them)
    return {"tam": tam, "loai": "EVD", "tieu_de": noi_dung[:60], "du_lieu": d}
