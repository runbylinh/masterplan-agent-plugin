"""Kho dữ liệu nghiên cứu (Skill 20): lưu, liên kết, kiểm tra, truy vết, xuất và báo cáo bản ghi nghiên cứu.

Mỗi bản ghi có mã (EVD-001, FIND-001, INS-001, OPP-001, IDEA-001, ADS-001, CAM-001...), liên kết tới bản ghi cha,
trạng thái duyệt, độ tin cậy, lịch sử cập nhật. Cấu trúc ở templates/kho/schema.json, hướng dẫn ở references/kho-du-lieu.md.

Lệnh (chạy trong thư mục làm việc, kho mặc định ./kho):
  kho.py khoi-tao
  kho.py them <file.json>            danh sách bản ghi; "tam": "x" + liên kết "@x" để nối trong cùng lô
  kho.py cap-nhat <ID> <file.json>   gộp trường mới vào du_lieu / thuộc tính, ghi lịch sử
  kho.py duyet <ID...> --trang-thai "Đã duyệt"|"Loại"   (chỉ khi người dùng yêu cầu)
  kho.py kiem-chung <ID...> --muc "Có căn cứ"|"Cần bổ sung"|"Chưa đủ căn cứ"|"Bị phản bác" [--ghi-chu ...]
  kho.py tim [--loai X] [--chu "..."] [--dot RP-001] [--trang-thai ...]
  kho.py truy-vet <ID>               chuỗi bằng chứng phía trên và tài nguyên phía dưới
  kho.py kiem-tra [--dot RP-001]     lỗi (thoát 1) và cảnh báo
  kho.py thong-ke
  kho.py xuat --ra <thư mục> [--xlsx] [--dot ...] [--loai ...]
  kho.py bao-cao --ra <thư mục> [--dot ...] [--tieu-de "..."]
  kho.py thay-doi --tu YYYY-MM-DD    báo cáo thay đổi từ một ngày
  kho.py tien-do --dot RP-001        tiến độ đợt (tiếp tục khi gián đoạn)
  kho.py nhom --loai IDEA --theo "Content Pillar" [--dot] [--ra file.md]   gom bản ghi theo một trường
"""
import argparse
import csv
import datetime as dt
import json
import os
import re
import sys

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SCHEMA_FILE = os.path.join(GOC, "templates", "kho", "schema.json")
RE_SDT = re.compile(r"(?<!\d)(?:\+?84|0)(?:[\s.\-]?\d){9,10}(?!\d)")
RE_EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")


def hom_nay():
    return os.environ.get("KHO_HOM_NAY") or dt.date.today().isoformat()


def nap_schema():
    with open(SCHEMA_FILE, encoding="utf-8") as f:
        return json.load(f)


def chuan(s):
    return " ".join(str(s or "").lower().split())


class Kho:
    def __init__(self, thu_muc):
        self.thu_muc = thu_muc
        self.sc = nap_schema()
        self.ban_ghi = {}
        if os.path.isdir(thu_muc):
            for ten in sorted(os.listdir(thu_muc)):
                if ten.endswith(".jsonl"):
                    with open(os.path.join(thu_muc, ten), encoding="utf-8") as f:
                        for dong in f:
                            if dong.strip():
                                r = json.loads(dong)
                                self.ban_ghi[r["id"]] = r

    # ---------- lưu ----------
    def luu(self):
        os.makedirs(self.thu_muc, exist_ok=True)
        theo_loai = {}
        for r in self.ban_ghi.values():
            theo_loai.setdefault(r["loai"], []).append(r)
        for loai in self.sc["loai"]:
            p = os.path.join(self.thu_muc, f"{loai}.jsonl")
            ds = sorted(theo_loai.get(loai, []), key=lambda x: so_thu_tu(x["id"]))
            if ds:
                with open(p, "w", encoding="utf-8") as f:
                    for r in ds:
                        f.write(json.dumps(r, ensure_ascii=False) + "\n")
            elif os.path.exists(p):
                os.remove(p)

    def ma_moi(self, loai):
        n = max([so_thu_tu(i) for i, r in self.ban_ghi.items() if r["loai"] == loai] or [0])
        return f"{loai}-{n + 1:03d}"

    def khoa(self, r):
        truong = self.sc["khoa_trung"].get(r["loai"])
        if not truong:
            gt = [chuan(r.get("tieu_de"))]
        else:
            gt = [chuan(r.get("du_lieu", {}).get(t)) for t in truong]
        return (r["loai"],) + tuple(gt) if any(gt) else None

    def tim_trung(self, r):
        k = self.khoa(r)
        if not k:
            return None
        for x in self.ban_ghi.values():
            if x["id"] != r.get("id") and self.khoa(x) == k:
                return x["id"]
        return None

    # ---------- thêm / cập nhật ----------
    def them(self, ds, dot_mac_dinh=""):
        tam = {}
        ket_qua = {"them": [], "trung": [], "loi": []}
        moi = []
        for r in ds:
            loai = r.get("loai")
            if loai not in self.sc["loai"]:
                ket_qua["loi"].append(f'loại "{loai}" không có trong schema')
                continue
            ban = {
                "id": None, "loai": loai, "tieu_de": r.get("tieu_de") or "",
                "du_lieu": r.get("du_lieu") or {}, "lien_ket": list(r.get("lien_ket") or []),
                "trang_thai": "Chờ duyệt", "do_tin_cay": r.get("do_tin_cay") or "Chưa xác định", "ly_do_tin_cay": r.get("ly_do_tin_cay") or "",
                "dot": r.get("dot") or (dot_mac_dinh if loai != "RP" else ""), "skill": r.get("skill") or self.sc["loai"][loai]["skill"],
                "ngay_tao": hom_nay(), "ngay_cap_nhat": hom_nay(), "lich_su": [{"ngay": hom_nay(), "thay_doi": "tạo mới"}],
            }
            if loai in self.sc["co_kiem_chung"]:
                ban["kiem_chung"] = r.get("kiem_chung") or "Cần bổ sung"
                ban["ly_do_kiem_chung"] = r.get("ly_do_kiem_chung") or ""
            trung = self.tim_trung(ban)
            if trung:
                ket_qua["trung"].append((r.get("tam") or ban["tieu_de"], trung))
                if r.get("tam"):
                    tam[r["tam"]] = trung
                moi.append((self.ban_ghi[trung], ban["lien_ket"], True))
                continue
            ban["id"] = self.ma_moi(loai)
            self.ban_ghi[ban["id"]] = ban
            if r.get("tam"):
                tam[r["tam"]] = ban["id"]
            moi.append((ban, None, False))
            ket_qua["them"].append(ban["id"])
        # giải @tạm (liên kết và mã đợt)
        for ban, _, la_cu in moi:
            if not la_cu and str(ban.get("dot", "")).startswith("@"):
                ban["dot"] = tam.get(ban["dot"][1:], "")
                if not ban["dot"]:
                    ket_qua["loi"].append(f'{ban["id"]}: không tìm thấy mã đợt tạm')
        for ban, them_lk, la_cu in moi:
            nguon = them_lk if la_cu else ban["lien_ket"]
            giai = []
            for x in nguon:
                if isinstance(x, str) and x.startswith("@"):
                    if x[1:] in tam:
                        giai.append(tam[x[1:]])
                    else:
                        ket_qua["loi"].append(f'{ban["id"]}: không tìm thấy liên kết tạm {x}')
                else:
                    giai.append(x)
            if la_cu:
                them_lk = [g for g in dict.fromkeys(giai) if g not in ban["lien_ket"] and g != ban["id"]]
                if them_lk:
                    ban["lien_ket"] += them_lk
                    ban["lich_su"].append({"ngay": hom_nay(), "thay_doi": "thêm liên kết " + ", ".join(them_lk)})
                    ban["ngay_cap_nhat"] = hom_nay()
            else:
                ban["lien_ket"] = list(dict.fromkeys(giai))
        return ket_qua

    def cap_nhat(self, ma, thay, sua_da_duyet=False):
        r = self.ban_ghi[ma]
        if r["trang_thai"] == "Đã duyệt" and not sua_da_duyet:
            raise PermissionError(f"{ma} đã được duyệt: không ghi đè. Dùng --sua-ban-da-duyet khi người dùng đồng ý (bản ghi quay về Chờ duyệt)")
        doi = []
        for k, v in (thay.get("du_lieu") or {}).items():
            if r["du_lieu"].get(k) != v:
                doi.append(f"{k}: {r['du_lieu'].get(k)!r} → {v!r}")
                r["du_lieu"][k] = v
        for k in ("tieu_de", "do_tin_cay", "ly_do_tin_cay", "dot"):
            if k in thay and thay[k] != r.get(k):
                doi.append(f"{k}: {r.get(k)!r} → {thay[k]!r}")
                r[k] = thay[k]
        for x in thay.get("lien_ket") or []:
            if x not in r["lien_ket"]:
                r["lien_ket"].append(x)
                doi.append(f"liên kết + {x}")
        if doi:
            r["ngay_cap_nhat"] = hom_nay()
            r["lich_su"].append({"ngay": hom_nay(), "thay_doi": "; ".join(doi)})
            if r["trang_thai"] == "Đã duyệt":
                r["trang_thai"] = "Chờ duyệt"
                r["lich_su"].append({"ngay": hom_nay(), "thay_doi": "sửa bản đã duyệt → Chờ duyệt"})
        return doi

    def dat(self, ma, truong, gia_tri, ghi_chu=""):
        r = self.ban_ghi[ma]
        if r.get(truong) != gia_tri:
            r["lich_su"].append({"ngay": hom_nay(), "thay_doi": f"{truong}: {r.get(truong)!r} → {gia_tri!r}" + (f" ({ghi_chu})" if ghi_chu else "")})
            r[truong] = gia_tri
            r["ngay_cap_nhat"] = hom_nay()

    # ---------- truy vết ----------
    def tren(self, ma, da=None):
        da = da if da is not None else set()
        for c in self.ban_ghi.get(ma, {}).get("lien_ket", []):
            if c not in da and c in self.ban_ghi:
                da.add(c)
                self.tren(c, da)
        return da

    def duoi(self, ma):
        kq, hang = set(), [ma]
        while hang:
            x = hang.pop()
            for r in self.ban_ghi.values():
                if x in r["lien_ket"] and r["id"] not in kq:
                    kq.add(r["id"])
                    hang.append(r["id"])
        return kq

    def nguon_doc_lap(self, ma):
        evd = [self.ban_ghi[x] for x in self.tren(ma) | {ma} if self.ban_ghi.get(x, {}).get("loai") == "EVD"]
        ten = set()
        for e in evd:
            n = e["du_lieu"].get("Nguồn", "")
            mien = re.sub(r"^https?://(www\.)?", "", str(n)).split("/")[0] if str(n).startswith("http") else chuan(n)
            ten.add((chuan(e["du_lieu"].get("Nền tảng")), mien))
        return len(ten)

    # ---------- kiểm tra ----------
    def kiem_tra(self, chi_dot=None):
        loi, cb = [], []
        sc = self.sc
        for r in self.ban_ghi.values():
            if chi_dot and r.get("dot") != chi_dot:
                continue
            ma, loai = r["id"], r["loai"]
            dn = sc["loai"][loai]
            thieu = [t for t in dn["bat_buoc"] if not str(r["du_lieu"].get(t, "")).strip()]
            if thieu:
                loi.append(f"{ma}: thiếu trường bắt buộc: {', '.join(thieu)}")
            for t, ds in (dn.get("gia_tri") or {}).items():
                v = r["du_lieu"].get(t)
                if v and v not in ds:
                    loi.append(f'{ma}: "{t}" = "{v}" không thuộc {ds}')
            if r["trang_thai"] not in sc["trang_thai_duyet"]:
                loi.append(f'{ma}: trạng thái duyệt "{r["trang_thai"]}" không hợp lệ')
            if r["do_tin_cay"] not in sc["do_tin_cay"]:
                loi.append(f'{ma}: độ tin cậy "{r["do_tin_cay"]}" không hợp lệ')
            if loai in sc["co_kiem_chung"] and r.get("kiem_chung") not in sc["kiem_chung"]:
                loi.append(f'{ma}: kết quả kiểm chứng "{r.get("kiem_chung")}" không hợp lệ')
            if r["do_tin_cay"] != "Chưa xác định" and not str(r.get("ly_do_tin_cay", "")).strip():
                cb.append(f'{ma}: độ tin cậy "{r["do_tin_cay"]}" chưa ghi lý do (ly_do_tin_cay)')
            if loai in sc["co_kiem_chung"] and r.get("kiem_chung") in ("Có căn cứ", "Bị phản bác") and not str(r.get("ly_do_kiem_chung", "")).strip():
                cb.append(f'{ma}: kết luận kiểm chứng "{r.get("kiem_chung")}" chưa ghi lý do')
            for c in r["lien_ket"]:
                if c not in self.ban_ghi:
                    loi.append(f"{ma}: liên kết tới {c} không tồn tại")
            if dn["cha"]:
                cha_hop_le = [c for c in r["lien_ket"] if self.ban_ghi.get(c, {}).get("loai") in dn["cha"]]
                if not cha_hop_le:
                    loi.append(f'{ma}: cần liên kết ít nhất một bản ghi loại {"/".join(dn["cha"])}')
            if loai == "EVD" and not str(r["du_lieu"].get("Nguồn", "")).strip():
                loi.append(f"{ma}: bằng chứng gốc thiếu Nguồn")
            van_ban = json.dumps(r["du_lieu"], ensure_ascii=False)
            if RE_EMAIL.search(van_ban) or RE_SDT.search(van_ban):
                loi.append(f"{ma}: có dấu hiệu email hoặc số điện thoại, phải ẩn danh")
            if dn["lop"] == 3 or loai in ("FIND", "SEG", "HT", "INS", "OPP", "KT"):
                tren = self.tren(ma)
                co_goc = any(self.ban_ghi[x]["loai"] == "EVD" or self.ban_ghi[x]["loai"] in sc["can_nguon"] for x in tren)
                if not co_goc:
                    cb.append(f"{ma}: không truy được về bằng chứng gốc (EVD hoặc bản ghi có nguồn)")
            if loai in sc["co_kiem_chung"] and r.get("kiem_chung") == "Có căn cứ":
                n = self.nguon_doc_lap(ma)
                if n < sc["nguong_co_can_cu"]:
                    cb.append(f'{ma}: ghi "Có căn cứ" nhưng chỉ có {n} nguồn độc lập (cần ≥ {sc["nguong_co_can_cu"]})')
            for c in r["lien_ket"]:
                cr = self.ban_ghi.get(c)
                if cr and cr.get("kiem_chung") == "Bị phản bác":
                    cb.append(f"{ma}: dựa trên {c} đã bị phản bác")
                if cr and cr.get("trang_thai") == "Loại":
                    cb.append(f"{ma}: dựa trên {c} đã bị Loại")
            han = dn.get("han_dung") or 0
            moc = r["du_lieu"].get("Ngày thu thập") or r["ngay_cap_nhat"]
            try:
                if han and (dt.date.fromisoformat(hom_nay()) - dt.date.fromisoformat(str(moc)[:10])).days > han:
                    cb.append(f"{ma}: có nguy cơ lỗi thời (mốc {moc}, hạn {han} ngày)")
            except ValueError:
                cb.append(f'{ma}: ngày "{moc}" sai định dạng YYYY-MM-DD')
            t = self.tim_trung(r)
            if t and so_thu_tu(t) < so_thu_tu(ma):
                cb.append(f"{ma}: trùng nội dung với {t}")
        return loi, cb

    def loc(self, loai=None, dot=None, chu=None, trang_thai=None):
        ds = list(self.ban_ghi.values())
        if loai:
            ds = [r for r in ds if r["loai"] in loai]
        if dot:
            ds = [r for r in ds if r.get("dot") == dot]
        if trang_thai:
            ds = [r for r in ds if r["trang_thai"] == trang_thai]
        if chu:
            c = chuan(chu)
            ds = [r for r in ds if c in chuan(json.dumps(r, ensure_ascii=False))]
        return sorted(ds, key=lambda r: (list(self.sc["loai"]).index(r["loai"]), so_thu_tu(r["id"])))


def slug(s):
    import unicodedata
    s = unicodedata.normalize("NFD", str(s).replace("đ", "d").replace("Đ", "D"))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def so_thu_tu(ma):
    m = re.search(r"(\d+)$", ma or "")
    return int(m.group(1)) if m else 0


def cot_cua(sc, loai):
    dn = sc["loai"][loai]
    return dn["bat_buoc"] + dn.get("tuy_chon", [])


def hang_xuat(sc, r):
    meta = [r["id"], r["tieu_de"], r["trang_thai"], r["do_tin_cay"], r.get("ly_do_tin_cay", ""), r.get("kiem_chung", ""),
            r.get("ly_do_kiem_chung", ""), ", ".join(r["lien_ket"]),
            r.get("dot", ""), r["ngay_tao"], r["ngay_cap_nhat"]]
    return meta + [gia_tri_o(r["du_lieu"].get(c)) for c in cot_cua(sc, r["loai"])]


def gia_tri_o(v):
    if isinstance(v, list):
        return "; ".join(str(x) for x in v)
    return "" if v is None else v


META = ["Mã", "Tiêu đề", "Duyệt", "Độ tin cậy", "Lý do tin cậy", "Kiểm chứng", "Lý do kiểm chứng", "Liên kết", "Đợt", "Ngày tạo", "Ngày cập nhật"]
TEN_FILE_KH = {"Nhu cầu": "kho-nhu-cau", "Nỗi đau": "kho-noi-dau", "Động lực": "kho-dong-luc-mua", "Rào cản": "kho-rao-can",
               "Tiêu chí lựa chọn": "kho-tieu-chi-lua-chon", "Tình huống mua": "kho-tinh-huong-mua", "Câu hỏi": "kho-cau-hoi",
               "Ngôn ngữ khách hàng": "kho-ngon-ngu-khach-hang", "Trải nghiệm sau mua": "kho-trai-nghiem-sau-mua",
               "Mong muốn": "kho-mong-muon"}


def xuat(kho, ra, ds, xlsx=False):
    import html_chung as H
    sc = kho.sc
    os.makedirs(ra, exist_ok=True)
    nhom = {}
    for r in ds:
        nhom.setdefault(r["loai"], []).append(r)
    files = []
    for loai, rs in nhom.items():
        ten = f'{loai}-{slug(sc["loai"][loai]["ten"])}'
        tieu_de = META + cot_cua(sc, loai)
        if loai == "KH":
            for nhan, ten_kh in TEN_FILE_KH.items():
                con = [r for r in rs if r["du_lieu"].get("Nhãn") == nhan]
                if con:
                    p = os.path.join(ra, f"KH-{ten_kh}.csv")
                    H.ghi_csv(p, tieu_de, [hang_xuat(sc, r) for r in con])
                    files.append(p)
        p = os.path.join(ra, f"{ten}.csv")
        H.ghi_csv(p, tieu_de, [hang_xuat(sc, r) for r in rs])
        files.append(p)
    if xlsx:
        try:
            from openpyxl import Workbook
            from openpyxl.styles import Font
        except ImportError:
            print("Không có openpyxl: bỏ qua .xlsx")
            return files
        wb = Workbook()
        wb.remove(wb.active)
        for loai, rs in nhom.items():
            ws = wb.create_sheet(re.sub(r"[\[\]:*?/\\]", "-", f'{loai} {sc["loai"][loai]["ten"]}')[:31])
            ws.append(META + cot_cua(sc, loai))
            for c in ws[1]:
                c.font = Font(bold=True)
            for r in rs:
                ws.append([str(x) if isinstance(x, (list, dict)) else x for x in hang_xuat(sc, r)])
        p = os.path.join(ra, "kho-nghien-cuu.xlsx")
        wb.save(p)
        files.append(p)
    return files


def bao_cao(kho, ra, ds, tieu_de, loi, cb):
    import html_chung as H
    sc = kho.sc
    os.makedirs(ra, exist_ok=True)
    phan, md = [], [f"# {tieu_de}", "", f"Lập ngày {hom_nay()} · {len(ds)} bản ghi", ""]
    dem = {}
    for r in ds:
        dem[r["loai"]] = dem.get(r["loai"], 0) + 1
    phan.append(H.section("Tổng quan", H.tiles([(sc["loai"][k]["ten"], H.n(v), k) for k, v in dem.items()])))
    md += ["## Tổng quan"] + [f"- {sc['loai'][k]['ten']} ({k}): {v}" for k, v in dem.items()] + [""]
    dinh = [r for r in ds if sc["loai"][r["loai"]]["lop"] == 3 or r["loai"] in ("INS", "OPP")]
    if dinh:
        hang, md_c = [], ["## Truy vết tài nguyên → bằng chứng", ""]
        for r in dinh:
            tren = sorted(kho.tren(r["id"]), key=lambda x: (list(sc["loai"]).index(kho.ban_ghi[x]["loai"]), so_thu_tu(x)))
            hang.append([f'<b>{H.e(r["id"])}</b> {H.e(r["tieu_de"])}', H.e(", ".join(tren) or "—"), H.e(r.get("kiem_chung", "")), H.e(r["trang_thai"])])
            md_c.append(f'- **{r["id"]}** {r["tieu_de"]} ← {", ".join(tren) or "—"}')
        phan.append(H.section("Truy vết tài nguyên → bằng chứng", H.bang(["Tài nguyên", "Dựa trên", "Kiểm chứng", "Duyệt"], hang)))
        md += md_c + [""]
    for loai in sc["loai"]:
        rs = [r for r in ds if r["loai"] == loai]
        if not rs:
            continue
        cot = cot_cua(sc, loai)[:7]
        hang = [[f'<b>{H.e(r["id"])}</b>'] + [H.e(gia_tri_o(r["du_lieu"].get(c))) for c in cot]
                + [H.e(", ".join(r["lien_ket"])), H.e(r["do_tin_cay"])] for r in rs]
        phan.append(H.section(f'{sc["loai"][loai]["ten"]} ({loai})', H.bang(["Mã"] + cot + ["Liên kết", "Tin cậy"], hang)))
        md += [f'## {sc["loai"][loai]["ten"]} ({loai})', "", "| Mã | " + " | ".join(cot) + " | Liên kết | Tin cậy |", "|" + " --- |" * (len(cot) + 3)]
        md += ["| " + " | ".join([r["id"]] + [str(gia_tri_o(r["du_lieu"].get(c))).replace("|", "/").replace("\n", " ") for c in cot]
                                + [", ".join(r["lien_ket"]), r["do_tin_cay"]]) + " |" for r in rs] + [""]
    if loi or cb:
        phan.append(H.section("Kiểm tra kho", "<ul>" + "".join(f'<li class="down">{H.e(x)}</li>' for x in loi)
                              + "".join(f"<li>{H.e(x)}</li>" for x in cb) + "</ul>"))
        md += ["## Kiểm tra kho"] + [f"- LỖI: {x}" for x in loi] + [f"- {x}" for x in cb] + [""]
    with open(os.path.join(ra, "bao-cao.html"), "w", encoding="utf-8") as f:
        f.write(H.trang(tieu_de, "Kho nghiên cứu", tieu_de, f"Lập ngày {hom_nay()}", phan))
    with open(os.path.join(ra, "bao-cao.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    return [os.path.join(ra, "bao-cao.html"), os.path.join(ra, "bao-cao.md")]


def doc_json(p, kem_dot=False):
    with open(p, encoding="utf-8") as f:
        d = json.load(f)
    ds = d if isinstance(d, list) else d.get("ban_ghi", [d])
    if kem_dot:
        return ds, ("" if isinstance(d, list) else d.get("dot", ""))
    return ds


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kho", default="kho")
    sub = ap.add_subparsers(dest="lenh")
    sub.add_parser("khoi-tao")
    p = sub.add_parser("them"); p.add_argument("file"); p.add_argument("--dot", default="")
    p = sub.add_parser("cap-nhat"); p.add_argument("ma"); p.add_argument("file"); p.add_argument("--sua-ban-da-duyet", action="store_true")
    p = sub.add_parser("duyet"); p.add_argument("ma", nargs="+"); p.add_argument("--trang-thai", required=True)
    p = sub.add_parser("kiem-chung"); p.add_argument("ma", nargs="+"); p.add_argument("--muc", required=True); p.add_argument("--tin-cay"); p.add_argument("--ly-do", default=""); p.add_argument("--ghi-chu", default="")
    p = sub.add_parser("tim"); p.add_argument("--loai", nargs="*"); p.add_argument("--chu"); p.add_argument("--dot"); p.add_argument("--trang-thai")
    p = sub.add_parser("truy-vet"); p.add_argument("ma")
    p = sub.add_parser("kiem-tra"); p.add_argument("--dot")
    sub.add_parser("thong-ke")
    p = sub.add_parser("xuat"); p.add_argument("--ra", required=True); p.add_argument("--xlsx", action="store_true"); p.add_argument("--dot"); p.add_argument("--loai", nargs="*")
    p = sub.add_parser("bao-cao"); p.add_argument("--ra", required=True); p.add_argument("--dot"); p.add_argument("--loai", nargs="*"); p.add_argument("--tieu-de", default="Kết quả nghiên cứu")
    p = sub.add_parser("thay-doi"); p.add_argument("--tu", required=True)
    p = sub.add_parser("tien-do"); p.add_argument("--dot", required=True)
    p = sub.add_parser("nhom"); p.add_argument("--loai", required=True); p.add_argument("--theo", required=True); p.add_argument("--dot"); p.add_argument("--ra")
    a = ap.parse_args(argv)
    kho = Kho(a.kho)
    sc = kho.sc

    if a.lenh == "khoi-tao":
        os.makedirs(a.kho, exist_ok=True)
        print(f"Kho ở {a.kho}/ ({len(kho.ban_ghi)} bản ghi). Mỗi loại một file <LOẠI>.jsonl.")
        return 0
    if a.lenh == "them":
        ds, dot_file = doc_json(a.file, kem_dot=True)
        kq = kho.them(ds, a.dot or dot_file)
        if kq["loi"]:
            for x in kq["loi"]:
                print("LỖI:", x)
            return 1
        kho.luu()
        print("Đã thêm:", ", ".join(kq["them"]) or "—")
        for t, m in kq["trung"]:
            print(f"Trùng (không thêm, dùng {m}): {t}")
        loi, cb = kho.kiem_tra()
        moi = set(kq["them"])
        for x in loi:
            if x.split(":")[0] in moi:
                print("LỖI:", x)
        for x in cb:
            if x.split(":")[0] in moi:
                print("CẢNH BÁO:", x)
        return 0
    if a.lenh == "cap-nhat":
        if a.ma not in kho.ban_ghi:
            print("Không có", a.ma); return 1
        d = doc_json(a.file)[0]
        try:
            doi = kho.cap_nhat(a.ma, d, a.sua_ban_da_duyet)
        except PermissionError as loi_q:
            print("LỖI:", loi_q); return 1
        kho.luu()
        print(f"{a.ma}: " + ("; ".join(doi) if doi else "không đổi"))
        return 0
    if a.lenh == "duyet":
        if a.trang_thai not in sc["trang_thai_duyet"]:
            print("Trạng thái phải là", sc["trang_thai_duyet"]); return 1
        for m in a.ma:
            kho.dat(m, "trang_thai", a.trang_thai, "người dùng duyệt")
        kho.luu(); print("Đã cập nhật:", ", ".join(a.ma)); return 0
    if a.lenh == "kiem-chung":
        if a.muc not in sc["kiem_chung"]:
            print("Mức phải là", sc["kiem_chung"]); return 1
        for m in a.ma:
            if kho.ban_ghi[m]["loai"] not in sc["co_kiem_chung"]:
                print(f"{m}: loại này không có trường kiểm chứng"); continue
            kho.dat(m, "kiem_chung", a.muc, a.ghi_chu)
            if a.ly_do:
                kho.dat(m, "ly_do_kiem_chung", a.ly_do)
            if a.tin_cay:
                if a.tin_cay not in sc["do_tin_cay"]:
                    print("Độ tin cậy phải là", sc["do_tin_cay"]); return 1
                kho.dat(m, "do_tin_cay", a.tin_cay, a.ghi_chu)
                if a.ly_do:
                    kho.dat(m, "ly_do_tin_cay", a.ly_do)
        kho.luu(); print("Đã ghi kết quả kiểm chứng:", ", ".join(a.ma)); return 0
    if a.lenh == "tim":
        for r in kho.loc(a.loai, a.dot, a.chu, a.trang_thai):
            print(f'{r["id"]:9s} {r["trang_thai"]:9s} {r["do_tin_cay"]:14s} {r["tieu_de"]}  ← {", ".join(r["lien_ket"])}')
        return 0
    if a.lenh == "truy-vet":
        if a.ma not in kho.ban_ghi:
            print("Không có", a.ma); return 1

        def in_cay(m, muc=0, da=None):
            da = da or set()
            r = kho.ban_ghi[m]
            print("  " * muc + f'{m} [{sc["loai"][r["loai"]]["ten"]}] {r["tieu_de"]}' + (f' · {r.get("kiem_chung")}' if r.get("kiem_chung") else ""))
            for c in r["lien_ket"]:
                if c in kho.ban_ghi and c not in da:
                    da.add(c)
                    in_cay(c, muc + 1, da)
        print("Dựa trên:")
        in_cay(a.ma)
        d = sorted(kho.duoi(a.ma), key=so_thu_tu)
        print("Được dùng bởi:", ", ".join(d) if d else "—")
        print(f"Nguồn độc lập phía trên: {kho.nguon_doc_lap(a.ma)}")
        return 0
    if a.lenh == "kiem-tra":
        loi, cb = kho.kiem_tra(a.dot)
        for x in loi:
            print("LỖI:", x)
        for x in cb:
            print("CẢNH BÁO:", x)
        print(f"{len(kho.ban_ghi)} bản ghi · {len(loi)} lỗi · {len(cb)} cảnh báo")
        return 1 if loi else 0
    if a.lenh == "thong-ke":
        dem = {}
        for r in kho.ban_ghi.values():
            k = (r["loai"], r["trang_thai"])
            dem[k] = dem.get(k, 0) + 1
        for (l, t), v in sorted(dem.items()):
            print(f'{l:5s} {sc["loai"][l]["ten"]:32s} {t:10s} {v}')
        return 0
    if a.lenh == "xuat":
        for p in xuat(kho, a.ra, kho.loc(a.loai, a.dot), a.xlsx):
            print("Đã ghi", p)
        return 0
    if a.lenh == "bao-cao":
        ds = kho.loc(a.loai, a.dot)
        loi, cb = kho.kiem_tra(a.dot)
        for p in bao_cao(kho, a.ra, ds, a.tieu_de, loi, cb):
            print("Đã ghi", p)
        return 0
    if a.lenh == "thay-doi":
        moi = [r for r in kho.ban_ghi.values() if r["ngay_tao"] >= a.tu]
        sua = [(r, [h for h in r["lich_su"] if h["ngay"] >= a.tu and h["thay_doi"] != "tạo mới"]) for r in kho.ban_ghi.values()]
        sua = [(r, h) for r, h in sua if h]
        print(f"# Thay đổi trong kho từ {a.tu}\n\n## Bản ghi mới ({len(moi)})")
        for r in sorted(moi, key=lambda r: (r["loai"], so_thu_tu(r["id"]))):
            print(f'- {r["id"]} {r["tieu_de"]}')
        print(f"\n## Bản ghi được cập nhật ({len(sua)})")
        for r, h in sua:
            print(f'- {r["id"]} {r["tieu_de"]}: ' + " | ".join(f'{x["ngay"]} {x["thay_doi"]}' for x in h))
        _, cb = kho.kiem_tra()
        cu = [x for x in cb if "lỗi thời" in x]
        print(f"\n## Cần cập nhật hoặc kiểm chứng lại ({len(cu)})")
        for x in cu:
            print("-", x)
        return 0
    if a.lenh == "nhom":
        nhom = {}
        for r in kho.loc([a.loai], a.dot):
            nhom.setdefault(str(gia_tri_o(r["du_lieu"].get(a.theo))) or "(chưa có)", []).append(r)
        out = [f"# {sc['loai'][a.loai]['ten']} theo {a.theo}", ""]
        for k, rs in sorted(nhom.items()):
            out += [f"## {k} ({len(rs)})"] + [f'- {r["id"]} {r["tieu_de"]} ← {", ".join(r["lien_ket"])}' for r in rs] + [""]
        txt = "\n".join(out)
        if a.ra:
            with open(a.ra, "w", encoding="utf-8") as f:
                f.write(txt)
            print("Đã ghi", a.ra)
        else:
            print(txt)
        return 0
    if a.lenh == "tien-do":
        rp = kho.ban_ghi.get(a.dot)
        if not rp:
            print("Không có", a.dot); return 1
        print(f'# Tiến độ {a.dot}: {rp["tieu_de"]}')
        for k in ("Mức nghiên cứu", "Workflow", "Đầu ra cuối cùng", "Tiêu chuẩn hoàn thành", "Tiến độ"):
            if rp["du_lieu"].get(k):
                print(f"- {k}: {gia_tri_o(rp['du_lieu'][k])}")
        dem = {}
        for r in kho.loc(dot=a.dot):
            dem.setdefault(r["loai"], {"tong": 0, "duyet": 0})
            dem[r["loai"]]["tong"] += 1
            dem[r["loai"]]["duyet"] += r["trang_thai"] == "Đã duyệt"
        print("\n| Loại | Số bản ghi | Đã duyệt |\n| --- | --- | --- |")
        for l, v in dem.items():
            print(f'| {l} {sc["loai"][l]["ten"]} | {v["tong"]} | {v["duyet"]} |')
        loi, cb = kho.kiem_tra(a.dot)
        print(f"\nKiểm tra đợt: {len(loi)} lỗi, {len(cb)} cảnh báo")
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
