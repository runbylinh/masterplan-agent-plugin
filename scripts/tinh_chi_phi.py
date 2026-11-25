#!/usr/bin/env python3
"""Tổng hợp chi phí quảng cáo từ chi-phi.json, dựng bao-cao.html và CSV.

Cách dùng:
    python3 tinh_chi_phi.py chi-phi-ads/<kỳ>
Đọc:  chi-phi.json, nhan-dinh.json (không bắt buộc)
Ghi:  chi-so-chi-phi.json, bao-cao.html, sheets/theo-thang.csv, sheets/chien-dich.csv, sheets/ngan-sach.csv
"""
import json
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import html_chung as H  # noqa: E402

TEN_NT = {"meta": "Meta", "tiktok": "TikTok"}
TEN_MT = {"nhan_biet": "Nhận biết", "tuong_tac": "Tương tác", "luot_xem_video": "Lượt xem video", "tin_nhan": "Tin nhắn",
          "lead": "Lead", "chuyen_doi": "Chuyển đổi", "luot_truy_cap": "Lượt truy cập", "khac": "Khác"}


def so(x):
    return x if isinstance(x, (int, float)) and not isinstance(x, bool) else 0


def chia(a, b):
    return None if not a or not b else a / b


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    tm = sys.argv[1]
    with open(os.path.join(tm, "chi-phi.json"), encoding="utf-8") as f:
        cp = json.load(f)
    nd = {}
    p = os.path.join(tm, "nhan-dinh.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            nd = json.load(f)

    cd = cp.get("chien_dich") or []
    thang = sorted({c["thang"] for c in cd} | {n["thang"] for n in cp.get("ngan_sach") or []})
    nen_tang = sorted({c["nen_tang"] for c in cd})
    ma_tran = defaultdict(float)
    for c in cd:
        ma_tran[(c["thang"], c["nen_tang"])] += so(c.get("chi_phi"))
    theo_thang = [{"thang": t, **{nt: ma_tran.get((t, nt)) or 0 for nt in nen_tang},
                   "tong": sum(ma_tran.get((t, nt)) or 0 for nt in nen_tang)} for t in thang]
    tong = sum(x["tong"] for x in theo_thang)

    mt = defaultdict(lambda: {"chi_phi": 0, "ket_qua": 0, "loai": set()})
    for c in cd:
        k = (c["nen_tang"], c.get("muc_tieu") or "khac")
        mt[k]["chi_phi"] += so(c.get("chi_phi"))
        mt[k]["ket_qua"] += so(c.get("ket_qua"))
        if c.get("loai_ket_qua"):
            mt[k]["loai"].add(c["loai_ket_qua"])
    theo_muc_tieu = sorted([{"nen_tang": k[0], "muc_tieu": k[1], "chi_phi": v["chi_phi"],
                             "ty_trong_pct": round(v["chi_phi"] / tong * 100, 1) if tong else None,
                             "ket_qua": v["ket_qua"], "loai_ket_qua": ", ".join(sorted(v["loai"])),
                             "chi_phi_ket_qua": None if not chia(v["chi_phi"], v["ket_qua"]) else round(v["chi_phi"] / v["ket_qua"])}
                            for k, v in mt.items()], key=lambda x: x["chi_phi"], reverse=True)

    gom_cd = defaultdict(lambda: {"chi_phi": 0, "ket_qua": 0, "nen_tang": None, "muc_tieu": None, "loai_ket_qua": None})
    for c in cd:
        g = gom_cd[c["chien_dich"]]
        g["chi_phi"] += so(c.get("chi_phi"))
        g["ket_qua"] += so(c.get("ket_qua"))
        g["nen_tang"], g["muc_tieu"], g["loai_ket_qua"] = c["nen_tang"], c.get("muc_tieu"), c.get("loai_ket_qua")
    ds_cd = []
    for ten, g in gom_cd.items():
        cpk = chia(g["chi_phi"], g["ket_qua"])
        ds_cd.append({"chien_dich": ten, **g, "chi_phi_ket_qua": None if cpk is None else round(cpk)})
    # so với trung bình cùng mục tiêu để tìm chiến dịch tốn mà kém
    for x in ds_cd:
        tb = next((m["chi_phi_ket_qua"] for m in theo_muc_tieu if m["nen_tang"] == x["nen_tang"] and m["muc_tieu"] == (x["muc_tieu"] or "khac")), None)
        x["so_tb_muc_tieu"] = None if not tb or x["chi_phi_ket_qua"] is None else round(x["chi_phi_ket_qua"] / tb, 2)
    ds_cd.sort(key=lambda x: x["chi_phi"], reverse=True)
    ton_kem = [x for x in ds_cd if (x["so_tb_muc_tieu"] or 0) >= 1.3 or (x["ket_qua"] == 0 and x["chi_phi"] > 0)][:5]
    tot = sorted([x for x in ds_cd if x["so_tb_muc_tieu"] is not None and x["chi_phi"] >= tong * 0.02], key=lambda x: x["so_tb_muc_tieu"])[:5]

    ns = defaultdict(lambda: {"ke_hoach": None, "thuc_chi": None})
    for n in cp.get("ngan_sach") or []:
        g = ns[n["thang"]]
        for tr in ("ke_hoach", "thuc_chi"):
            if isinstance(n.get(tr), (int, float)):
                g[tr] = (g[tr] or 0) + n[tr]
    ngan_sach = [{"thang": t, "ke_hoach": ns[t]["ke_hoach"], "thuc_chi_file": ns[t]["thuc_chi"],
                  "chi_tren_nen_tang": next((x["tong"] for x in theo_thang if x["thang"] == t), None),
                  "lech_pct": None if not ns[t]["ke_hoach"] else round(((ns[t]["thuc_chi"] if ns[t]["thuc_chi"] is not None else next((x["tong"] for x in theo_thang if x["thang"] == t), 0)) - ns[t]["ke_hoach"]) / ns[t]["ke_hoach"] * 100, 1)}
                 for t in thang if t in ns]

    kq = defaultdict(lambda: {"lead": None, "don": None, "doanh_thu": None})
    for r in cp.get("ket_qua_kinh_doanh") or []:
        g = kq[r["nen_tang"]]
        for tr in ("lead", "don", "doanh_thu"):
            if isinstance(r.get(tr), (int, float)):
                g[tr] = (g[tr] or 0) + r[tr]
    hieu_qua = []
    for nt in nen_tang:
        chi = sum(x[nt] for x in theo_thang)
        g = kq.get(nt) or {}
        hieu_qua.append({"nen_tang": nt, "chi_phi": chi, "lead": g.get("lead"), "don": g.get("don"), "doanh_thu": g.get("doanh_thu"),
                         "cpl": None if not chia(chi, g.get("lead")) else round(chi / g["lead"]),
                         "chi_phi_don": None if not chia(chi, g.get("don")) else round(chi / g["don"]),
                         "roas": None if not chia(g.get("doanh_thu"), chi) else round(g["doanh_thu"] / chi, 2)})

    ra = {"doanh_nghiep": cp.get("doanh_nghiep"), "ky": cp.get("ky"), "da_gom_vat": cp.get("da_gom_vat"), "tong_chi_phi": tong,
          "theo_thang": theo_thang, "theo_muc_tieu": theo_muc_tieu, "chien_dich": ds_cd, "ton_ma_kem": ton_kem, "hieu_qua_tot": tot,
          "ngan_sach": ngan_sach, "hieu_qua": hieu_qua, "nguon": cp.get("nguon") or [], "thieu": cp.get("thieu") or []}
    with open(os.path.join(tm, "chi-so-chi-phi.json"), "w", encoding="utf-8") as f:
        json.dump(ra, f, ensure_ascii=False, indent=2)

    # HTML
    ky = cp.get("ky") or {}
    phan = []
    if nd.get("tom_tat"):
        phan.append(H.section("Tóm tắt", f'<p class="lead">{H.e(nd["tom_tat"])}</p>'))
    o = [("Tổng chi trên nền tảng", H.n(tong, "đ"), "đã gồm VAT" if cp.get("da_gom_vat") else "chưa gồm VAT")]
    o += [(TEN_NT.get(h["nen_tang"], h["nen_tang"]), H.n(h["chi_phi"], "đ"),
           (f'ROAS {H.n(h["roas"])}' if h["roas"] else (f'CPL {H.n(h["cpl"], "đ")}' if h["cpl"] else ""))) for h in hieu_qua]
    phan.append(H.section("Tổng quan", H.tiles(o)))
    phan.append(H.section("Chi theo tháng", H.cot_ngang([x["thang"] for x in theo_thang], [x["tong"] for x in theo_thang], "đ")
                          + H.bang(["Tháng"] + [TEN_NT.get(nt, nt) for nt in nen_tang] + ["Tổng"],
                                   [[x["thang"]] + [round(x[nt]) for nt in nen_tang] + [round(x["tong"])] for x in theo_thang],
                                   cot_so=tuple(range(1, len(nen_tang) + 2)))
                          + (f'<p>{H.e(nd["phan_bo"])}</p>' if nd.get("phan_bo") else "")))
    phan.append(H.section("Theo mục tiêu", H.bang(["Nền tảng", "Mục tiêu", "Chi phí", "Tỷ trọng", "Kết quả", "Loại kết quả", "Chi phí / kết quả"],
                                                   [[TEN_NT.get(m["nen_tang"], m["nen_tang"]), TEN_MT.get(m["muc_tieu"], m["muc_tieu"]), round(m["chi_phi"]),
                                                     H.n(m["ty_trong_pct"], "%"), m["ket_qua"], H.e(m["loai_ket_qua"]), H.n(m["chi_phi_ket_qua"], "đ")]
                                                    for m in theo_muc_tieu], cot_so=(2, 3, 4, 6))))
    if ngan_sach:
        phan.append(H.section("Kế hoạch và thực chi", H.bang(["Tháng", "Kế hoạch", "Thực chi (file)", "Chi trên nền tảng", "Lệch kế hoạch"],
                                                             [[x["thang"], x["ke_hoach"], x["thuc_chi_file"], x["chi_tren_nen_tang"],
                                                               H.n(x["lech_pct"], "%")] for x in ngan_sach], cot_so=(1, 2, 3, 4))
                              + (f'<p>{H.e(nd["lech_ngan_sach"])}</p>' if nd.get("lech_ngan_sach") else ""),
                              "Thực chi trong file có thể khác số trên nền tảng do VAT, phí thanh toán, đại lý."))
    if any(h["lead"] or h["don"] or h["doanh_thu"] for h in hieu_qua):
        phan.append(H.section("Hiệu quả kinh doanh", H.bang(["Nền tảng", "Chi phí", "Lead", "CPL", "Đơn", "Chi phí / đơn", "Doanh thu", "ROAS"],
                                                            [[TEN_NT.get(h["nen_tang"], h["nen_tang"]), round(h["chi_phi"]), h["lead"], h["cpl"], h["don"],
                                                              h["chi_phi_don"], h["doanh_thu"], H.n(h["roas"])] for h in hieu_qua], cot_so=(1, 2, 3, 4, 5, 6, 7))
                              + (f'<p>{H.e(nd["hieu_qua"])}</p>' if nd.get("hieu_qua") else "")))
    def bang_cd(ds):
        return H.bang(["Chiến dịch", "Nền tảng", "Mục tiêu", "Chi phí", "Kết quả", "Chi phí / kết quả", "So TB cùng mục tiêu"],
                      [[H.e(x["chien_dich"]), TEN_NT.get(x["nen_tang"], x["nen_tang"]), TEN_MT.get(x["muc_tieu"], x["muc_tieu"]), round(x["chi_phi"]),
                        x["ket_qua"], H.n(x["chi_phi_ket_qua"], "đ"), H.n(x["so_tb_muc_tieu"], "×")] for x in ds], cot_so=(3, 4, 5, 6))
    if ton_kem:
        phan.append(H.section("Tốn nhiều mà kém", bang_cd(ton_kem), "Chi phí/kết quả từ 1,3 lần trung bình cùng mục tiêu, hoặc có chi mà không có kết quả."))
    if tot:
        phan.append(H.section("Hiệu quả nhất", bang_cd(tot)))
    if nd.get("uu_tien"):
        phan.append(H.section("Đầu vào cho kế hoạch", H.ds(nd["uu_tien"])))
    nguon = [f'<li>{H.e(g.get("muc"))} — {H.e(g.get("noi_lay"))}, {H.e(g.get("ngay_lay"))}</li>' for g in ra["nguon"]]
    thieu = [f'<li>Thiếu: {H.e(g.get("muc"))} ({H.e(g.get("ly_do"))})</li>' for g in ra["thieu"]]
    if nguon or thieu:
        phan.append(H.section("Nguồn và phần thiếu", '<ul class="small">' + "".join(nguon + thieu) + "</ul>"))
    with open(os.path.join(tm, "bao-cao.html"), "w", encoding="utf-8") as f:
        f.write(H.trang("Chi phí quảng cáo", "Chi phí quảng cáo", cp.get("doanh_nghiep") or "", f'Kỳ {ky.get("tu")} → {ky.get("den")}', phan))

    H.ghi_csv(os.path.join(tm, "sheets", "theo-thang.csv"), ["Tháng"] + [TEN_NT.get(nt, nt) for nt in nen_tang] + ["Tổng", "Duyệt"],
              [[x["thang"]] + [round(x[nt]) for nt in nen_tang] + [round(x["tong"]), "Chờ duyệt"] for x in theo_thang])
    H.ghi_csv(os.path.join(tm, "sheets", "chien-dich.csv"), ["Kỳ", "Chiến dịch", "Nền tảng", "Mục tiêu", "Chi phí", "Kết quả", "Loại kết quả", "Chi phí/kết quả", "So TB mục tiêu"],
              [[f'{ky.get("tu")} → {ky.get("den")}', x["chien_dich"], x["nen_tang"], x["muc_tieu"], round(x["chi_phi"]), x["ket_qua"], x["loai_ket_qua"],
                x["chi_phi_ket_qua"], x["so_tb_muc_tieu"]] for x in ds_cd])
    H.ghi_csv(os.path.join(tm, "sheets", "ngan-sach.csv"), ["Tháng", "Kế hoạch", "Thực chi (file)", "Chi trên nền tảng", "Lệch %"],
              [[x["thang"], x["ke_hoach"], x["thuc_chi_file"], x["chi_tren_nen_tang"], x["lech_pct"]] for x in ngan_sach])
    print(f"Đã ghi chi-so-chi-phi.json, bao-cao.html, sheets/ trong {tm}")
    print(f"Tổng chi {round(tong):,}đ qua {len(thang)} tháng, {len(ds_cd)} chiến dịch, {len(ton_kem)} chiến dịch tốn mà kém")
    return 0


if __name__ == "__main__":
    sys.exit(main())
