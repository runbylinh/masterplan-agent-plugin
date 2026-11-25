"""Hàm dựng HTML dùng chung cho báo cáo các skill (nền trắng, xám trung tính, một màu nhấn)."""
import csv
import html
import os

CSS = """
:root{--bg:#fff;--fg:#1d1d1f;--muted:#6b6b70;--line:#e6e6e9;--soft:#f6f6f7;--accent:#6864AE;--up:#1f7a4d;--down:#b3261e}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#151517;--fg:#ededf0;--muted:#a0a0a8;--line:#2c2c31;--soft:#1e1e22;--accent:#a29fe0;--up:#5cc28e;--down:#f08080}}
:root[data-theme="dark"]{--bg:#151517;--fg:#ededf0;--muted:#a0a0a8;--line:#2c2c31;--soft:#1e1e22;--accent:#a29fe0;--up:#5cc28e;--down:#f08080}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:980px;margin:0 auto;padding:32px 16px 64px}h1{font-size:28px;margin:4px 0}h2{font-size:19px;margin:0 0 10px}h4{margin:18px 0 8px;font-size:14px}
.eyebrow{color:var(--accent);font-weight:600;margin:0;font-size:13px}.muted{color:var(--muted)}.small{font-size:13px}.lead{font-size:16px}
section{border-top:1px solid var(--line);padding:24px 0}a{color:var(--accent)}
.tbl{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:14px}th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}th{font-weight:600;color:var(--muted);font-size:12px}
td.r,th.r{text-align:right;font-variant-numeric:tabular-nums}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:10px;margin:14px 0}.tile{background:var(--soft);border-radius:6px;padding:10px 12px}.num{font-size:20px;font-weight:600}
.up{color:var(--up)}.down{color:var(--down)}.tag{display:inline-block;border:1px solid var(--line);border-radius:4px;padding:0 6px;font-size:12px;margin-right:4px}
.chart{width:100%;height:auto;max-width:680px}.chart .lbl{font-size:13px;fill:var(--fg)}.chart .val{font-size:11px;fill:var(--muted)}.bar-a{fill:var(--accent)}.bar-b{fill:var(--line)}
"""


def e(x):
    return html.escape("" if x is None else str(x))


def n(x, don_vi="", so_le=None):
    if x is None or x == "":
        return "–"
    if isinstance(x, str):
        return e(x)
    if isinstance(x, float):
        if so_le is None:
            so_le = 0 if abs(x) >= 100 else (1 if abs(x) >= 10 else 2)
        s = f"{x:,.{so_le}f}"
    else:
        s = f"{x:,}"
    return s.replace(",", "_").replace(".", ",").replace("_", ".") + don_vi


def doi(moi, cu):
    if moi is None or cu in (None, 0):
        return None
    return (moi - cu) / cu * 100


def the_doi(moi, cu, nhan="so kỳ trước", nguoc=False):
    d = doi(moi, cu)
    if d is None:
        return '<span class="muted">chưa có số so sánh</span>'
    tot = (d >= 0) != nguoc
    return f'<span class="{"up" if tot else "down"}">{"+" if d >= 0 else ""}{n(d, "%", 1)} {e(nhan)}</span>'


def tiles(o):
    """o: list (nhãn, giá trị đã định dạng, dòng phụ html)"""
    return '<div class="tiles">' + "".join(
        f'<div class="tile"><div class="muted small">{e(a)}</div><div class="num">{b}</div><div class="small">{c or ""}</div></div>'
        for a, b, c in o) + "</div>"


def bang(tieu_de, hang, cot_so=()):
    """tieu_de: list str; hang: list list (giá trị đã là html hoặc số); cot_so: chỉ số cột canh phải."""
    th = "".join(f'<th class="{"r" if i in cot_so else ""}">{e(t)}</th>' for i, t in enumerate(tieu_de))
    tr = "".join("<tr>" + "".join(
        f'<td class="{"r" if i in cot_so else ""}">{n(c) if isinstance(c, (int, float)) or c is None else c}</td>'
        for i, c in enumerate(r)) + "</tr>" for r in hang)
    return f'<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


def cot_ngang(nhan, gia_tri, don_vi="", gia_tri_b=None, chu_thich=None):
    if not nhan:
        return ""
    tat_ca = [v for v in list(gia_tri) + list(gia_tri_b or []) if v]
    lon = max(tat_ca or [1])
    cao = 46 if gia_tri_b else 26
    rn, rc = 150, 400
    h = cao * len(nhan) + (30 if chu_thich else 6)
    out = []
    for i, t in enumerate(nhan):
        y = i * cao + 4
        out.append(f'<text x="0" y="{y + 13}" class="lbl">{e(str(t)[:22])}</text>')
        cap = [(gia_tri[i], "bar-a")] + ([(gia_tri_b[i], "bar-b")] if gia_tri_b else [])
        for j, (v, lop) in enumerate(cap):
            yy = y + j * 17
            w = 0 if not v else max(2, v / lon * rc)
            out.append(f'<rect x="{rn}" y="{yy}" width="{w:.1f}" height="13" rx="2" class="{lop}"/>')
            out.append(f'<text x="{rn + w + 6:.1f}" y="{yy + 11}" class="val">{n(v, don_vi)}</text>')
    if chu_thich:
        out.append(f'<g transform="translate({rn},{h - 10})"><rect width="10" height="10" class="bar-a"/>'
                   f'<text x="14" y="9" class="val">{e(chu_thich[0])}</text>'
                   f'<rect x="150" width="10" height="10" class="bar-b"/><text x="164" y="9" class="val">{e(chu_thich[1])}</text></g>')
    return f'<svg viewBox="0 0 {rn + rc + 110} {h}" class="chart" role="img">' + "".join(out) + "</svg>"


def section(tieu_de, noi_dung, ghi_chu=None):
    return (f"<section><h2>{e(tieu_de)}</h2>" + (f'<p class="muted small">{e(ghi_chu)}</p>' if ghi_chu else "")
            + noi_dung + "</section>")


def trang(tieu_de_tab, eyebrow, h1, phu_de, cac_phan):
    return ('<!doctype html><html lang="vi"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f"<title>{e(tieu_de_tab)}</title><style>{CSS}</style></head><body><main>"
            f'<header><p class="eyebrow">{e(eyebrow)}</p><h1>{e(h1)}</h1><p class="muted">{e(phu_de)}</p></header>'
            + "".join(cac_phan) + "</main></body></html>")


def ghi_csv(duong_dan, tieu_de, hang):
    os.makedirs(os.path.dirname(duong_dan), exist_ok=True)
    with open(duong_dan, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(tieu_de)
        w.writerows(hang)


def ds(items):
    return "<ol>" + "".join(f"<li>{e(x)}</li>" for x in items) + "</ol>" if items else ""
