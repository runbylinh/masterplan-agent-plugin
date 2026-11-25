#!/usr/bin/env python3
"""Dựng báo cáo HTML và file CSV cho Google Sheets từ chi-so.json (+ nhan-dinh.json nếu có).

Cách dùng:
    python3 dung_bao_cao.py <thu-muc-ky>
Đọc:  chi-so.json, nhan-dinh.json (không bắt buộc)
Ghi:  bao-cao.html, sheets/chi-so-kenh.csv, sheets/top-bai.csv, sheets/doi-thu.csv
"""
import csv
import html
import json
import os
import sys

MAU_KET_LUAN = {
    "Đẩy mạnh": "#1f7a4d", "Giữ": "#3b5bab", "Tối ưu": "#b26a00",
    "Bỏ / tạm dừng": "#b3261e", "Chưa đủ dữ liệu": "#6b6b6b",
}
MAU_MUC = {"Tốt": "#1f7a4d", "Trung bình": "#8a6d00", "Yếu": "#b3261e", "Thiếu số": "#8a8a8a"}


def e(x):
    return html.escape("" if x is None else str(x))


def n(x, don_vi="", so_le=None):
    if x is None:
        return "–"
    if isinstance(x, float):
        if so_le is None:
            so_le = 0 if abs(x) >= 100 else (1 if abs(x) >= 10 else 2)
        s = f"{x:,.{so_le}f}"
    else:
        s = f"{x:,}"
    return s.replace(",", "_").replace(".", ",").replace("_", ".") + don_vi


def doi(moi, cu):
    if moi is None or cu is None or cu == 0:
        return None
    return (moi - cu) / cu * 100


def the_doi(moi, cu, nguoc=False):
    d = doi(moi, cu)
    if d is None:
        return '<span class="muted">chưa có kỳ trước</span>'
    tot = d >= 0 if not nguoc else d <= 0
    dau = "+" if d >= 0 else ""
    return f'<span class="{"up" if tot else "down"}">{dau}{n(d, "%", 1)} so kỳ trước</span>'


def bieu_do_cot(nhan, cap_gia_tri, chu_thich, don_vi=""):
    """Cột ngang đôi (hiện tại / so sánh). cap_gia_tri: list (a, b)."""
    if not nhan:
        return ""
    lon_nhat = max([v for ab in cap_gia_tri for v in ab if v] or [1])
    cao_dong = 46
    rong_nhan = 130
    rong_cot = 420
    h = cao_dong * len(nhan) + 30
    dong = []
    for i, (t, (a, b)) in enumerate(zip(nhan, cap_gia_tri)):
        y = i * cao_dong + 6
        dong.append(f'<text x="0" y="{y + 16}" class="lbl">{e(t)}</text>')
        for j, (v, lop) in enumerate(((a, "bar-a"), (b, "bar-b"))):
            yy = y + j * 17
            w = 0 if not v else max(2, v / lon_nhat * rong_cot)
            dong.append(f'<rect x="{rong_nhan}" y="{yy}" width="{w:.1f}" height="13" rx="2" class="{lop}"/>')
            dong.append(f'<text x="{rong_nhan + w + 6:.1f}" y="{yy + 11}" class="val">{n(v, don_vi)}</text>')
    chu = (f'<g transform="translate({rong_nhan},{h - 10})"><rect width="10" height="10" class="bar-a"/>'
           f'<text x="14" y="9" class="val">{e(chu_thich[0])}</text>'
           f'<rect x="150" width="10" height="10" class="bar-b"/><text x="164" y="9" class="val">{e(chu_thich[1])}</text></g>')
    return (f'<svg viewBox="0 0 {rong_nhan + rong_cot + 90} {h}" class="chart" role="img">'
            + "".join(dong) + chu + "</svg>")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    thu_muc = sys.argv[1]
    with open(os.path.join(thu_muc, "chi-so.json"), encoding="utf-8") as f:
        cs = json.load(f)
    nd = {}
    p = os.path.join(thu_muc, "nhan-dinh.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            nd = json.load(f)
    nd_kenh = nd.get("kenh") or {}

    ky = cs.get("ky") or {}
    minh = [k for k in cs["kenh"] if k["cua"] == "minh"]
    dt = [k for k in cs["kenh"] if k["cua"] == "doi_thu"]
    ten_ky = f"{ky.get('tu', '?')} → {ky.get('den', '?')}"

    def ket_luan(k):
        return (nd_kenh.get(k["id"]) or {}).get("ket_luan") or k["danh_gia"]["ket_luan_so_bo"]

    # ---------- HTML ----------
    phan = []
    phan.append(f'<header><p class="eyebrow">Đánh giá kênh social</p><h1>{e(cs.get("doanh_nghiep"))}</h1>'
                f'<p class="muted">Kỳ {e(ten_ky)} · so với kỳ {e(ky.get("ky_truoc_tu", "?"))} → {e(ky.get("ky_truoc_den", "?"))}'
                f' · số lấy ngày {e(cs.get("ngay_lay"))}</p></header>')

    if nd.get("tom_tat"):
        phan.append(f'<section><h2>Tóm tắt</h2><p class="lead">{e(nd["tom_tat"])}</p></section>')

    # Bảng kết luận
    dong = []
    for k in minh:
        dg = k["danh_gia"]
        kl = ket_luan(k)
        dong.append(
            f'<tr><td><b>{e(k["ten_nen_tang"])}</b><div class="muted small">{e(k["ten"])}</div></td>'
            f'<td>{e(dg["ten_vai_tro"])}</td>'
            f'<td><span class="dot" style="background:{MAU_MUC.get(dg["muc_chinh"], "#888")}"></span>{e(dg["muc_chinh"])}</td>'
            f'<td><span class="pill" style="color:{MAU_KET_LUAN.get(kl, "#444")};border-color:{MAU_KET_LUAN.get(kl, "#444")}">{e(kl)}</span></td>'
            f'<td class="small">{e((nd_kenh.get(k["id"]) or {}).get("ly_do") or dg["ly_do_so_bo"])}</td></tr>')
    phan.append('<section><h2>Kết luận từng kênh</h2><div class="tbl"><table><thead><tr><th>Kênh</th><th>Vai trò</th>'
                '<th>Chỉ số chính</th><th>Kết luận</th><th>Lý do</th></tr></thead><tbody>'
                + "".join(dong) + "</tbody></table></div></section>")

    # Biểu đồ tổng
    nhan = [k["ten_nen_tang"] for k in minh]
    phan.append('<section><h2>Phủ sóng: kỳ này và kỳ trước</h2><p class="muted small">TikTok, YouTube tính lượt xem; '
                'các kênh khác tính reach (Group: thành viên hoạt động, Zalo OA: lượt xem bài).</p>'
                + bieu_do_cot(nhan, [(k["chi_so"]["phu_song"], k["chi_so_ky_truoc"].get("phu_song")) for k in minh],
                              ("Kỳ này", "Kỳ trước")) + "</section>")
    if any(k["chi_so"]["lead"] for k in minh):
        th = cs.get("tong_hop") or {}
        phan.append(f'<section><h2>Lead theo kênh</h2><p class="muted small">Tổng {n(th.get("tong_lead"))} lead · '
                    f'chi phí ads {n(th.get("tong_chi_phi_ads"), "đ")} · CPL trung bình {n(th.get("cpl_trung_binh"), "đ")}'
                    + (f' · lead không rõ nguồn {n(th.get("lead_khong_ro_nguon"))}' if th.get("lead_khong_ro_nguon") is not None else "")
                    + "</p>"
                    + bieu_do_cot(nhan, [(k["chi_so"]["lead"], k["chi_so_ky_truoc"].get("lead")) for k in minh],
                                  ("Kỳ này", "Kỳ trước")) + "</section>")

    # Từng kênh
    for k in minh:
        ht, kt, dg = k["chi_so"], k["chi_so_ky_truoc"], k["danh_gia"]
        nk = nd_kenh.get(k["id"]) or {}
        kl = ket_luan(k)
        o = [
            ("Follower", n(ht["follower"]), the_doi(ht["follower"], kt.get("follower"))),
            ("Follower mới", n(ht["follower_moi"]), the_doi(ht["follower_moi"], kt.get("follower_moi"))),
            (ht["ten_phu_song"].capitalize(), n(ht["phu_song"]), the_doi(ht["phu_song"], kt.get("phu_song"))),
            ("Tỷ lệ tương tác", n(ht["er_pct"], "%"), the_doi(ht["er_pct"], kt.get("er_pct"))),
            ("Bài / tuần", n(ht["tan_suat_bai_tuan"]), f'<span class="muted">{n(ht["so_bai"])} bài trong kỳ</span>'),
            ("Lead", n(ht["lead"]), the_doi(ht["lead"], kt.get("lead"))),
        ]
        if ht["cpl"] is not None:
            o.append(("Chi phí / lead", n(ht["cpl"], "đ"), the_doi(ht["cpl"], kt.get("cpl"), nguoc=True)))
        o_html = "".join(f'<div class="tile"><div class="muted small">{e(a)}</div><div class="num">{b}</div><div class="small">{c}</div></div>'
                         for a, b, c in o)
        tc_html = "".join(
            f'<li><b>{e(t["tieu_chi"])}</b> <span style="color:{MAU_MUC[t["muc"]]}">{e(t["muc"])}</span>'
            f'{" · <span class=muted>chỉ số chính</span>" if key in dg["tieu_chi_chinh"] else ""}'
            f'<div class="muted small">{e("; ".join(t["can_cu"]) or "không có số để so")}</div></li>'
            for key, t in dg["tieu_chi"].items() if key in dg["tieu_chi_chinh"] + dg["tieu_chi_phu"])
        top = k["noi_dung"]["top_bai"]
        top_html = ""
        if top:
            top_html = ('<h4>Bài chạy tốt nhất (theo ' + e(k["noi_dung"].get("do_bang")) + ')</h4><div class="tbl"><table><thead><tr><th>Ngày</th><th>Bài</th>'
                        '<th>Định dạng</th><th>Lượt xem</th><th>Tương tác</th></tr></thead><tbody>'
                        + "".join(f'<tr><td>{e(b["ngay"])}</td><td><a href="{e(b["url"])}" target="_blank" rel="noopener">'
                                  f'{e(b["tieu_de"] or b["chu_de"] or "Mở bài")}</a></td><td>{e(b["dinh_dang"])}</td>'
                                  f'<td>{n(b["luot_xem"])}</td><td>{n(b["tuong_tac"])}</td></tr>' for b in top)
                        + "</tbody></table></div>")
            dd = k["noi_dung"]["theo_dinh_dang"]
            if len(dd) > 1:
                top_html += ('<p class="small muted">Theo định dạng (trung bình mỗi bài): '
                             + " · ".join(f'{e(x["nhom"])} {n(x["tb_moi_bai"])} ({x["so_bai"]} bài)' for x in dd) + "</p>")
        viec = nk.get("viec_tiep") or []
        nd_html = ""
        if nk.get("noi_dung_thang"):
            nd_html += f'<p><b>Nội dung thắng:</b> {e(nk["noi_dung_thang"])}</p>'
        if nk.get("doi_tu"):
            nd_html += f'<p class="small muted">Đổi từ kết luận sơ bộ "{e(nk["doi_tu"])}".</p>'
        if viec:
            nd_html += "<p><b>Việc kỳ tới</b></p><ol>" + "".join(f"<li>{e(v)}</li>" for v in viec) + "</ol>"
        thieu = k.get("thieu") or []
        thieu_html = ("" if not thieu else '<p class="small muted">Thiếu: '
                      + "; ".join(f'{e(t.get("chi_so"))} ({e(t.get("ly_do"))})' for t in thieu) + "</p>")
        phan.append(
            f'<section class="kenh"><div class="kenh-head"><div><h2>{e(k["ten_nen_tang"])}</h2>'
            f'<p class="muted small"><a href="{e(k["url"])}" target="_blank" rel="noopener">{e(k["ten"])}</a> · vai trò {e(dg["ten_vai_tro"])}</p></div>'
            f'<span class="pill big" style="color:{MAU_KET_LUAN.get(kl, "#444")};border-color:{MAU_KET_LUAN.get(kl, "#444")}">{e(kl)}</span></div>'
            f'<p>{e(nk.get("ly_do") or dg["ly_do_so_bo"])}</p>'
            f'<div class="tiles">{o_html}</div><h4>Chấm theo tiêu chí</h4><ul class="tc">{tc_html}</ul>'
            f'{top_html}{nd_html}{thieu_html}</section>')

    # Đối thủ
    if dt:
        nts = sorted({k["nen_tang"] for k in dt})
        bang = []
        for nt in nts:
            ds = [k for k in minh if k["nen_tang"] == nt] + [k for k in dt if k["nen_tang"] == nt]
            for k in ds:
                ck = k["chi_so_cong_khai"]
                bang.append(
                    f'<tr class="{"me" if k["cua"] == "minh" else ""}"><td>{e(k["ten_nen_tang"])}</td>'
                    f'<td>{"<b>Mình</b>" if k["cua"] == "minh" else e(k["doi_thu"])}<div class="muted small">{e(k["ten"])}</div></td>'
                    f'<td>{n(k["chi_so"]["follower"])}</td><td>{n(ck.get("tan_suat_bai_tuan"))}</td>'
                    f'<td>{n(ck.get("luot_xem_tb_bai"))}</td><td>{n(ck.get("tuong_tac_tb_bai"))}</td>'
                    f'<td>{n(ck.get("er_cong_khai_pct"), "%")}</td></tr>')
        phan.append('<section><h2>So với đối thủ (số công khai)</h2><p class="muted small">Chỉ dùng số ai cũng xem được '
                    'trên trang (follower, view, like, bình luận, chia sẻ) cho cả mình và đối thủ.</p>'
                    '<div class="tbl"><table><thead><tr><th>Nền tảng</th><th>Kênh</th><th>Follower</th><th>Bài/tuần</th>'
                    '<th>View TB/bài</th><th>Tương tác TB/bài</th><th>ER công khai</th></tr></thead><tbody>'
                    + "".join(bang) + "</tbody></table></div>"
                    + (f'<p>{e(nd["khoang_trong_doi_thu"])}</p>' if nd.get("khoang_trong_doi_thu") else "")
                    + "</section>")

    if nd.get("pheu") or nd.get("uu_tien"):
        s = "<section><h2>Toàn hệ kênh</h2>"
        if nd.get("pheu"):
            s += f'<p>{e(nd["pheu"])}</p>'
        if nd.get("uu_tien"):
            s += "<h4>3 ưu tiên kỳ tới</h4><ol>" + "".join(f"<li>{e(x)}</li>" for x in nd["uu_tien"]) + "</ol>"
        phan.append(s + "</section>")

    # Nguồn
    nguon = []
    for k in cs["kenh"]:
        for g in k.get("nguon") or []:
            nguon.append(f'<li>{e(k["ten_nen_tang"])} · {e(k["doi_thu"] or "Mình")}: {e(g.get("chi_so"))} — '
                         f'{e(g.get("noi_lay"))}, ngày {e(g.get("ngay_lay"))}</li>')
    if nguon:
        phan.append('<section><h2>Nguồn số liệu</h2><ul class="small">' + "".join(nguon) + "</ul></section>")

    css = """
:root{--bg:#fff;--fg:#1d1d1f;--muted:#6b6b70;--line:#e6e6e9;--soft:#f6f6f7;--accent:#6864AE;--up:#1f7a4d;--down:#b3261e}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#151517;--fg:#ededf0;--muted:#a0a0a8;--line:#2c2c31;--soft:#1e1e22;--accent:#a29fe0;--up:#5cc28e;--down:#f08080}}
:root[data-theme="dark"]{--bg:#151517;--fg:#ededf0;--muted:#a0a0a8;--line:#2c2c31;--soft:#1e1e22;--accent:#a29fe0;--up:#5cc28e;--down:#f08080}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:980px;margin:0 auto;padding:32px 16px 64px}h1{font-size:28px;margin:4px 0}h2{font-size:19px;margin:0 0 10px}h4{margin:18px 0 8px;font-size:14px}
.eyebrow{color:var(--accent);font-weight:600;margin:0;font-size:13px;letter-spacing:.02em}.muted{color:var(--muted)}.small{font-size:13px}.lead{font-size:16px}
section{border-top:1px solid var(--line);padding:24px 0}a{color:var(--accent)}
.tbl{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:14px}th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}th{font-weight:600;color:var(--muted);font-size:12px}
tr.me td{background:var(--soft)}.pill{display:inline-block;border:1px solid;border-radius:4px;padding:1px 8px;font-size:13px;font-weight:600;white-space:nowrap}.pill.big{font-size:15px;padding:3px 12px}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px}
.kenh-head{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;margin:14px 0}.tile{background:var(--soft);border-radius:6px;padding:10px 12px}.num{font-size:20px;font-weight:600}
.up{color:var(--up)}.down{color:var(--down)}ul.tc{padding-left:18px}ul.tc li{margin-bottom:6px}
.chart{width:100%;height:auto;max-width:680px}.chart .lbl{font-size:13px;fill:var(--fg)}.chart .val{font-size:11px;fill:var(--muted)}.bar-a{fill:var(--accent)}.bar-b{fill:var(--line)}
"""
    trang = ('<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
             f'<title>Đánh giá kênh</title><style>{css}</style></head><body><main>' + "".join(phan) + "</main></body></html>")
    with open(os.path.join(thu_muc, "bao-cao.html"), "w", encoding="utf-8") as f:
        f.write(trang)

    # ---------- CSV cho Google Sheets ----------
    os.makedirs(os.path.join(thu_muc, "sheets"), exist_ok=True)
    nguon_kenh = lambda k: "; ".join(f'{g.get("noi_lay")} ({g.get("ngay_lay")})' for g in k.get("nguon") or [])
    with open(os.path.join(thu_muc, "sheets", "chi-so-kenh.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Kỳ", "Kênh", "Nền tảng", "Vai trò", "Follower", "Follower mới", "Phủ sóng", "Loại phủ sóng",
                    "Δ phủ sóng %", "Tương tác", "ER %", "Số bài", "Bài/tuần", "Lead", "Lead paid", "Chi phí ads",
                    "CPL", "Chỉ số chính", "Kết luận", "Lý do", "Nguồn", "Duyệt"])
        for k in minh:
            ht, kt, dg = k["chi_so"], k["chi_so_ky_truoc"], k["danh_gia"]
            d = doi(ht["phu_song"], kt.get("phu_song"))
            w.writerow([ten_ky, k["ten"], k["ten_nen_tang"], dg["ten_vai_tro"], ht["follower"], ht["follower_moi"],
                        ht["phu_song"], ht["ten_phu_song"], None if d is None else round(d, 1), ht["tuong_tac"],
                        ht["er_pct"], ht["so_bai"], ht["tan_suat_bai_tuan"], ht["lead"], ht["lead_paid"],
                        ht["chi_phi_ads"], ht["cpl"], dg["muc_chinh"], ket_luan(k),
                        (nd_kenh.get(k["id"]) or {}).get("ly_do") or dg["ly_do_so_bo"], nguon_kenh(k), "Chờ duyệt"])
    with open(os.path.join(thu_muc, "sheets", "top-bai.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Kỳ", "Kênh", "Nền tảng", "Ngày đăng", "Bài", "Link", "Định dạng", "Chủ đề", "Lượt xem", "Tương tác"])
        for k in minh:
            for b in k["noi_dung"]["top_bai"]:
                w.writerow([ten_ky, k["ten"], k["ten_nen_tang"], b["ngay"], b["tieu_de"], b["url"], b["dinh_dang"],
                            b["chu_de"], b["luot_xem"], b["tuong_tac"]])
    with open(os.path.join(thu_muc, "sheets", "doi-thu.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Kỳ", "Nền tảng", "Bên", "Kênh", "Follower", "Bài/tuần", "View TB/bài", "Tương tác TB/bài",
                    "ER công khai %", "Cách tính ER", "Nguồn"])
        for k in minh + dt:
            if k["cua"] == "minh" and not any(x["nen_tang"] == k["nen_tang"] for x in dt):
                continue
            ck = k["chi_so_cong_khai"]
            w.writerow([ten_ky, k["ten_nen_tang"], "Mình" if k["cua"] == "minh" else k["doi_thu"], k["ten"],
                        k["chi_so"]["follower"], ck.get("tan_suat_bai_tuan"), ck.get("luot_xem_tb_bai"),
                        ck.get("tuong_tac_tb_bai"), ck.get("er_cong_khai_pct"), ck.get("cach_tinh_er"), nguon_kenh(k)])
    print(f"Đã ghi {os.path.join(thu_muc, 'bao-cao.html')} và 3 file trong {os.path.join(thu_muc, 'sheets')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
