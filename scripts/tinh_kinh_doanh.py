#!/usr/bin/env python3
"""Phân tích số kinh doanh từ du-lieu.json, dựng bao-cao.html và CSV.

Cách dùng:
    python3 tinh_kinh_doanh.py kinh-doanh/<kỳ>
Đọc:  du-lieu.json, nhan-dinh.json (không bắt buộc)
Ghi:  chi-so-kd.json, bao-cao.html, sheets/theo-thang.csv, sheets/theo-san-pham.csv, sheets/theo-kenh.csv, sheets/kpi.csv
"""
import json
import os
import statistics
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import html_chung as H  # noqa: E402


def so(x):
    return x if isinstance(x, (int, float)) and not isinstance(x, bool) else None


def cong(a, b):
    return b if a is None else (a if b is None else a + b)


def thang_truoc_nam(t):
    y, m = t.split("-")
    return f"{int(y) - 1}-{m}"


def quy(t):
    y, m = t.split("-")
    return f"{y}-Q{(int(m) - 1) // 3 + 1}"


def gom(dong, khoa):
    g = defaultdict(lambda: {"doanh_thu": None, "don": None, "loi_nhuan_gop": None})
    for d in dong:
        k = d.get(khoa) or "(chưa rõ)"
        for tr in ("doanh_thu", "don", "loi_nhuan_gop"):
            g[k][tr] = cong(g[k][tr], so(d.get(tr)))
    return g


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    tm = sys.argv[1]
    with open(os.path.join(tm, "du-lieu.json"), encoding="utf-8") as f:
        dl = json.load(f)
    nd = {}
    p = os.path.join(tm, "nhan-dinh.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            nd = json.load(f)

    tt = sorted(dl.get("theo_thang") or [], key=lambda x: x["thang"])
    theo = {x["thang"]: x for x in tt}
    ky = dl.get("ky") or {}
    trong_ky = [x for x in tt if (not ky.get("tu") or x["thang"] >= ky["tu"]) and (not ky.get("den") or x["thang"] <= ky["den"])]

    thang_ra = []
    truoc = None
    for x in trong_ky:
        dt, don = so(x.get("doanh_thu")), so(x.get("don"))
        cung_ky = theo.get(thang_truoc_nam(x["thang"]))
        km, kc = so(x.get("khach_moi")), so(x.get("khach_cu"))
        thang_ra.append({
            "thang": x["thang"], "doanh_thu": dt, "don": don,
            "gia_tri_don_tb": round(dt / don) if dt is not None and don else None,
            "so_thang_truoc_pct": None if truoc is None else (lambda d: None if d is None else round(d, 1))(H.doi(dt, so(truoc.get("doanh_thu")))),
            "so_cung_ky_pct": None if not cung_ky else (lambda d: None if d is None else round(d, 1))(H.doi(dt, so(cung_ky.get("doanh_thu")))),
            "khach_moi": km, "khach_cu": kc,
            "ty_le_mua_lai_pct": round(kc / (km + kc) * 100, 1) if km is not None and kc is not None and (km + kc) else None,
            "chi_phi_marketing": so(x.get("chi_phi_marketing")),
        })
        truoc = x
    co_dt = [t for t in thang_ra if t["doanh_thu"] is not None]
    tong_dt = sum(t["doanh_thu"] for t in co_dt) if co_dt else None
    tong_don = sum(t["don"] for t in thang_ra if t["don"] is not None) if any(t["don"] is not None for t in thang_ra) else None
    tb = statistics.mean(t["doanh_thu"] for t in co_dt) if co_dt else None
    mua_vu = [{"thang": t["thang"], "chi_so_mua_vu": round(t["doanh_thu"] / tb * 100)} for t in co_dt] if tb else []

    def loc(ds):
        return [d for d in ds if (not ky.get("tu") or d.get("thang", "") >= ky["tu"]) and (not ky.get("den") or d.get("thang", "") <= ky["den"])]

    sp = gom(loc(dl.get("theo_san_pham") or []), "san_pham")
    tong_sp = sum(v["doanh_thu"] or 0 for v in sp.values()) or None
    sp_ra = sorted([{"san_pham": k, **v, "ty_trong_pct": None if not tong_sp or v["doanh_thu"] is None else round(v["doanh_thu"] / tong_sp * 100, 1),
                     "bien_lai_gop_pct": None if not v["doanh_thu"] or v["loi_nhuan_gop"] is None else round(v["loi_nhuan_gop"] / v["doanh_thu"] * 100, 1)}
                    for k, v in sp.items()], key=lambda x: x["doanh_thu"] or 0, reverse=True)
    luy_ke = 0
    for x in sp_ra:
        luy_ke += x["ty_trong_pct"] or 0
        x["nhom_80"] = luy_ke - (x["ty_trong_pct"] or 0) < 80
    # xu hướng sản phẩm: nửa sau kỳ so nửa đầu
    ds_thang = sorted({d["thang"] for d in loc(dl.get("theo_san_pham") or []) if d.get("thang")})
    if len(ds_thang) >= 4:
        giua = ds_thang[len(ds_thang) // 2]
        for x in sp_ra:
            dau = sum(so(d.get("doanh_thu")) or 0 for d in dl["theo_san_pham"] if d.get("san_pham") == x["san_pham"] and ds_thang[0] <= d["thang"] < giua)
            sau = sum(so(d.get("doanh_thu")) or 0 for d in dl["theo_san_pham"] if d.get("san_pham") == x["san_pham"] and giua <= d["thang"] <= ds_thang[-1])
            x["xu_huong_pct"] = None if not dau else round((sau - dau) / dau * 100, 1)
    kn = gom(loc(dl.get("theo_kenh") or []), "kenh")
    tong_kn = sum(v["doanh_thu"] or 0 for v in kn.values()) or None
    kn_ra = sorted([{"kenh": k, **v, "ty_trong_pct": None if not tong_kn or v["doanh_thu"] is None else round(v["doanh_thu"] / tong_kn * 100, 1)}
                    for k, v in kn.items()], key=lambda x: x["doanh_thu"] or 0, reverse=True)

    kpi_ra = []
    for m in dl.get("muc_tieu") or []:
        k = m.get("ky", "")
        if "-Q" in k:
            ds = [t for t in thang_ra if quy(t["thang"]) == k]
        elif len(k) == 4:
            ds = [t for t in thang_ra if t["thang"].startswith(k)]
        else:
            ds = [t for t in thang_ra if t["thang"] == k]
        thuc_dt = sum(t["doanh_thu"] or 0 for t in ds) if ds else None
        thuc_don = sum(t["don"] or 0 for t in ds) if ds else None
        kpi_ra.append({"ky": k, "muc_tieu_doanh_thu": so(m.get("doanh_thu")), "thuc_te_doanh_thu": thuc_dt,
                       "dat_doanh_thu_pct": None if not so(m.get("doanh_thu")) or thuc_dt is None else round(thuc_dt / m["doanh_thu"] * 100, 1),
                       "muc_tieu_don": so(m.get("don")), "thuc_te_don": thuc_don,
                       "dat_don_pct": None if not so(m.get("don")) or thuc_don is None else round(thuc_don / m["don"] * 100, 1),
                       "so_thang_co_so": len(ds)})

    ra = {"doanh_nghiep": dl.get("doanh_nghiep"), "ky": ky, "tong_doanh_thu": tong_dt, "tong_don": tong_don,
          "gia_tri_don_tb": round(tong_dt / tong_don) if tong_dt and tong_don else None,
          "theo_thang": thang_ra, "mua_vu": mua_vu, "theo_san_pham": sp_ra, "theo_kenh": kn_ra, "kpi": kpi_ra,
          "nguon": dl.get("nguon") or [], "thieu": dl.get("thieu") or []}
    with open(os.path.join(tm, "chi-so-kd.json"), "w", encoding="utf-8") as f:
        json.dump(ra, f, ensure_ascii=False, indent=2)

    # HTML
    phan = []
    if nd.get("tom_tat"):
        phan.append(H.section("Tóm tắt", f'<p class="lead">{H.e(nd["tom_tat"])}</p>'))
    o = [("Doanh thu", H.n(tong_dt, "đ"), f"{len(co_dt)} tháng có số"), ("Đơn", H.n(tong_don), ""),
         ("Giá trị đơn TB", H.n(ra["gia_tri_don_tb"], "đ"), "")]
    if co_dt:
        cao = max(co_dt, key=lambda t: t["doanh_thu"])
        thap = min(co_dt, key=lambda t: t["doanh_thu"])
        o += [("Tháng cao nhất", H.e(cao["thang"]), H.n(cao["doanh_thu"], "đ")), ("Tháng thấp nhất", H.e(thap["thang"]), H.n(thap["doanh_thu"], "đ"))]
    phan.append(H.section("Tổng quan", H.tiles(o)))
    if thang_ra:
        phan.append(H.section("Doanh thu theo tháng", H.cot_ngang([t["thang"] for t in thang_ra], [t["doanh_thu"] for t in thang_ra], "đ")
                              + H.bang(["Tháng", "Doanh thu", "Đơn", "Giá trị đơn TB", "So tháng trước", "So cùng kỳ", "Mua lại"],
                                       [[t["thang"], t["doanh_thu"], t["don"], t["gia_tri_don_tb"], H.n(t["so_thang_truoc_pct"], "%"),
                                         H.n(t["so_cung_ky_pct"], "%"), H.n(t["ty_le_mua_lai_pct"], "%")] for t in thang_ra], cot_so=(1, 2, 3, 4, 5, 6))
                              + (f'<p>{H.e(nd["mua_vu"])}</p>' if nd.get("mua_vu") else "")))
    if sp_ra:
        phan.append(H.section("Theo sản phẩm", H.cot_ngang([x["san_pham"] for x in sp_ra[:12]], [x["ty_trong_pct"] for x in sp_ra[:12]], "%")
                              + H.bang(["Sản phẩm", "Doanh thu", "Đơn", "Tỷ trọng", "Biên lãi gộp", "Xu hướng nửa sau kỳ", "Nhóm 80%"],
                                       [[H.e(x["san_pham"]), x["doanh_thu"], x["don"], H.n(x["ty_trong_pct"], "%"), H.n(x["bien_lai_gop_pct"], "%"),
                                         H.n(x.get("xu_huong_pct"), "%"), "có" if x["nhom_80"] else ""] for x in sp_ra], cot_so=(1, 2, 3, 4, 5))
                              + (f'<p>{H.e(nd["san_pham"])}</p>' if nd.get("san_pham") else ""),
                              "Nhóm 80%: các sản phẩm cộng lại tạo khoảng 80% doanh thu."))
    if kn_ra:
        phan.append(H.section("Theo kênh / nguồn khách", H.cot_ngang([x["kenh"] for x in kn_ra], [x["ty_trong_pct"] for x in kn_ra], "%")
                              + H.bang(["Kênh", "Doanh thu", "Đơn", "Tỷ trọng"],
                                       [[H.e(x["kenh"]), x["doanh_thu"], x["don"], H.n(x["ty_trong_pct"], "%")] for x in kn_ra], cot_so=(1, 2, 3))
                              + (f'<p>{H.e(nd["kenh"])}</p>' if nd.get("kenh") else "")))
    if kpi_ra:
        phan.append(H.section("So mục tiêu", H.bang(["Kỳ", "Mục tiêu doanh thu", "Thực tế", "Đạt", "Mục tiêu đơn", "Thực tế đơn", "Đạt"],
                                                     [[x["ky"], x["muc_tieu_doanh_thu"], x["thuc_te_doanh_thu"], H.n(x["dat_doanh_thu_pct"], "%"),
                                                       x["muc_tieu_don"], x["thuc_te_don"], H.n(x["dat_don_pct"], "%")] for x in kpi_ra], cot_so=(1, 2, 3, 4, 5, 6))
                              + (f'<p>{H.e(nd["kpi"])}</p>' if nd.get("kpi") else "")))
    if nd.get("uu_tien"):
        phan.append(H.section("Hệ quả cho marketing", H.ds(nd["uu_tien"])))
    nguon = [f'<li>{H.e(g.get("file"))} · {H.e(g.get("noi"))} · sheet {H.e(g.get("sheet"))} · sửa {H.e(g.get("ngay_sua"))} → {H.e(g.get("dung_cho"))}</li>' for g in ra["nguon"]]
    thieu = [f'<li>Thiếu: {H.e(g.get("muc"))} ({H.e(g.get("ly_do"))})</li>' for g in ra["thieu"]]
    if nguon or thieu:
        phan.append(H.section("Nguồn và phần thiếu", '<ul class="small">' + "".join(nguon + thieu) + "</ul>"))
    with open(os.path.join(tm, "bao-cao.html"), "w", encoding="utf-8") as f:
        f.write(H.trang("Báo cáo kinh doanh", "Phân tích kinh doanh", dl.get("doanh_nghiep") or "", f'Kỳ {ky.get("tu")} → {ky.get("den")}', phan))

    H.ghi_csv(os.path.join(tm, "sheets", "theo-thang.csv"), ["Tháng", "Doanh thu", "Đơn", "Giá trị đơn TB", "So tháng trước %", "So cùng kỳ %", "Khách mới", "Khách cũ", "Mua lại %", "Duyệt"],
              [[t["thang"], t["doanh_thu"], t["don"], t["gia_tri_don_tb"], t["so_thang_truoc_pct"], t["so_cung_ky_pct"], t["khach_moi"], t["khach_cu"], t["ty_le_mua_lai_pct"], "Chờ duyệt"] for t in thang_ra])
    H.ghi_csv(os.path.join(tm, "sheets", "theo-san-pham.csv"), ["Kỳ", "Sản phẩm", "Doanh thu", "Đơn", "Tỷ trọng %", "Biên lãi gộp %", "Xu hướng %", "Nhóm 80%"],
              [[f'{ky.get("tu")} → {ky.get("den")}', x["san_pham"], x["doanh_thu"], x["don"], x["ty_trong_pct"], x["bien_lai_gop_pct"], x.get("xu_huong_pct"), x["nhom_80"]] for x in sp_ra])
    H.ghi_csv(os.path.join(tm, "sheets", "theo-kenh.csv"), ["Kỳ", "Kênh", "Doanh thu", "Đơn", "Tỷ trọng %"],
              [[f'{ky.get("tu")} → {ky.get("den")}', x["kenh"], x["doanh_thu"], x["don"], x["ty_trong_pct"]] for x in kn_ra])
    H.ghi_csv(os.path.join(tm, "sheets", "kpi.csv"), ["Kỳ", "MT doanh thu", "Thực tế", "Đạt %", "MT đơn", "Thực tế đơn", "Đạt %"],
              [[x["ky"], x["muc_tieu_doanh_thu"], x["thuc_te_doanh_thu"], x["dat_doanh_thu_pct"], x["muc_tieu_don"], x["thuc_te_don"], x["dat_don_pct"]] for x in kpi_ra])
    print(f"Đã ghi chi-so-kd.json, bao-cao.html, sheets/ trong {tm}")
    print(f"Doanh thu {tong_dt}, đơn {tong_don}, {len(sp_ra)} sản phẩm, {len(kn_ra)} kênh, {len(kpi_ra)} mốc KPI")
    return 0


if __name__ == "__main__":
    sys.exit(main())
