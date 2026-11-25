#!/usr/bin/env python3
"""Đọc file CSV/XLSX người dùng xuất (Meta Business Suite, TikTok Studio, YouTube Studio, Zalo OA,
file ngân sách, báo cáo bán hàng...).

Hai chế độ:
  1) Xem cấu trúc file (dùng cho mọi loại file: báo cáo kinh doanh, ngân sách, đơn hàng):
       python3 doc_file_xuat.py <file> --xem [--so-dong 15]
     In ra tên các sheet, dòng tiêu đề đoán được, vài dòng đầu dạng JSON.
  2) Chuyển file xuất bài đăng thành danh sách bài theo định dạng so-lieu.json:
       python3 doc_file_xuat.py <file> --nen-tang tiktok [--tu 2026-08-27 --den 2026-11-24]
     In JSON {"bai": [...], "tong": {...}, "cot_da_nhan": {...}, "cot_bo_qua": [...]}.
Không sửa file gốc.
"""
import argparse
import csv
import io
import json
import re
import sys
import unicodedata
from datetime import date, datetime

TU_DONG_NGHIA = {
    "url": ["permalink", "link", "url", "duong dan", "lien ket", "video link"],
    "ngay": ["publish time", "thoi gian dang", "ngay dang", "post time", "created", "date", "ngay", "time", "video publish time", "publish date"],
    "tieu_de": ["title", "tieu de", "noi dung", "description", "mo ta", "caption", "message", "video title"],
    "dinh_dang": ["post type", "loai bai", "loai", "type", "format", "dinh dang"],
    "luot_xem": ["video views", "views", "luot xem", "plays", "view", "luot phat"],
    "reach": ["reach", "luot tiep can", "nguoi tiep can", "accounts reached", "tiep can"],
    "thich": ["reactions", "likes", "luot thich", "cam xuc", "like", "thich"],
    "binh_luan": ["comments", "binh luan", "comment"],
    "chia_se": ["shares", "chia se", "share"],
    "luu": ["saves", "luu", "favorites", "yeu thich"],
}


def khong_dau(s):
    s = unicodedata.normalize("NFD", str(s or "")).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", s.replace("đ", "d").replace("Đ", "D")).strip().lower()


def doc_bang(duong_dan):
    """Trả về dict {ten_sheet: [hàng...]}"""
    if duong_dan.lower().endswith((".xlsx", ".xlsm")):
        import openpyxl
        wb = openpyxl.load_workbook(duong_dan, read_only=True, data_only=True)
        return {ws.title: [list(r) for r in ws.iter_rows(values_only=True)] for ws in wb.worksheets}
    with open(duong_dan, "rb") as f:
        raw = f.read()
    for enc in ("utf-8-sig", "utf-16", "cp1258", "latin-1"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    try:
        dialect = csv.Sniffer().sniff(text[:4000], delimiters=",;\t")
    except csv.Error:
        dialect = csv.excel
    return {"csv": [r for r in csv.reader(io.StringIO(text), dialect)]}


def tim_dong_tieu_de(hang):
    """Dòng tiêu đề = dòng đầu tiên trong 10 dòng có nhiều ô chữ nhất."""
    tot, idx = -1, 0
    for i, r in enumerate(hang[:10]):
        d = sum(1 for c in r if isinstance(c, str) and c.strip() and not re.fullmatch(r"[\d.,%\s-]+", c))
        if d > tot:
            tot, idx = d, i
    return idx


def so(x):
    if x is None or x == "":
        return None
    if isinstance(x, (int, float)):
        return x
    s = str(x).strip().replace(" ", "")
    if s in ("-", "--", "N/A"):
        return None
    s = re.sub(r"[^\d.,-]", "", s)
    if not s:
        return None
    if "," in s and "." in s:
        s = s.replace(",", "") if s.rfind(".") > s.rfind(",") else s.replace(".", "").replace(",", ".")
    elif s.count(".") > 1 or (s.count(".") == 1 and len(s.split(".")[1]) == 3):
        s = s.replace(".", "")
    elif s.count(",") >= 1 and all(len(p) == 3 for p in s.split(",")[1:]):
        s = s.replace(",", "")
    else:
        s = s.replace(",", ".")
    try:
        v = float(s)
        return int(v) if v.is_integer() else v
    except ValueError:
        return None


def ngay(x):
    if isinstance(x, datetime):
        return x.date()
    if isinstance(x, date):
        return x
    s = str(x or "").strip()
    for f in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%d/%m/%Y", "%d/%m/%Y %H:%M",
              "%m/%d/%Y %H:%M", "%m/%d/%Y", "%d-%m-%Y", "%b %d, %Y"):
        try:
            return datetime.strptime(s[:len(datetime.now().strftime(f))] if "%b" not in f else s, f).date()
        except ValueError:
            continue
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return None


def map_cot(tieu_de):
    cot = {}
    da_dung = set()
    for truong, tu in TU_DONG_NGHIA.items():
        for t in tu:
            for i, h in enumerate(tieu_de):
                if i in da_dung:
                    continue
                if khong_dau(h) == t or (len(t) > 3 and t in khong_dau(h)):
                    cot[truong] = i
                    da_dung.add(i)
                    break
            if truong in cot:
                break
    return cot


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--xem", action="store_true")
    ap.add_argument("--so-dong", type=int, default=10)
    ap.add_argument("--nen-tang")
    ap.add_argument("--tu")
    ap.add_argument("--den")
    a = ap.parse_args()

    bang = doc_bang(a.file)
    if a.xem or not a.nen_tang:
        ra = {}
        for ten, hang in bang.items():
            if not hang:
                continue
            i = tim_dong_tieu_de(hang)
            td = [str(c) if c is not None else "" for c in hang[i]]
            mau = [dict(zip(td, [str(c) if isinstance(c, (datetime, date)) else c for c in r])) for r in hang[i + 1:i + 1 + a.so_dong]]
            ra[ten] = {"so_dong": len(hang) - i - 1, "dong_tieu_de": i + 1, "cot": td, "mau": mau}
        print(json.dumps(ra, ensure_ascii=False, indent=2, default=str))
        return 0

    tu = ngay(a.tu) if a.tu else None
    den = ngay(a.den) if a.den else None
    ten, hang = max(bang.items(), key=lambda kv: len(kv[1]))
    i = tim_dong_tieu_de(hang)
    td = hang[i]
    cot = map_cot(td)
    bai = []
    for r in hang[i + 1:]:
        if not any(c not in (None, "") for c in r):
            continue
        get = lambda k: r[cot[k]] if k in cot and cot[k] < len(r) else None
        d = ngay(get("ngay"))
        if (tu and d and d < tu) or (den and d and d > den):
            continue
        b = {"url": get("url"), "ngay": d.isoformat() if d else None,
             "dinh_dang": get("dinh_dang"), "chu_de": None,
             "tieu_de": (str(get("tieu_de"))[:120] if get("tieu_de") else None)}
        for k in ("luot_xem", "reach", "thich", "binh_luan", "chia_se", "luu"):
            b[k] = so(get(k))
        bai.append(b)
    tong = {k: sum(b[k] for b in bai if b[k] is not None) if any(b[k] is not None for b in bai) else None
            for k in ("luot_xem", "reach", "thich", "binh_luan", "chia_se", "luu")}
    tong["so_bai"] = len(bai)
    print(json.dumps({
        "nen_tang": a.nen_tang, "sheet": ten, "bai": bai, "tong": tong,
        "cot_da_nhan": {k: str(td[v]) for k, v in cot.items()},
        "cot_bo_qua": [str(h) for j, h in enumerate(td) if j not in cot.values()],
        "luu_y": "Reach cộng từ từng bài có thể lớn hơn reach thật của trang (một người thấy nhiều bài). Ưu tiên reach tổng ở Insights.",
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
