#!/usr/bin/env python3
"""Tính chỉ số và kết luận sơ bộ cho từng kênh từ so-lieu.json.

Cách dùng:
    python3 tinh_chi_so.py <thu-muc-ky>/so-lieu.json [--nguong duong-dan/nguong.json]
Ghi ra chi-so.json cùng thư mục. Khung chấm điểm: references/khung-danh-gia.md.
"""
import argparse
import json
import os
import statistics
import sys
from datetime import date

PLUGIN_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEN_TANG_DUNG_VIEW = {"tiktok", "youtube"}
MUC_DIEM = {"Tốt": 2, "Trung bình": 1, "Yếu": 0}
TEN_NEN_TANG = {
    "facebook_page": "Facebook Page", "facebook_group": "Facebook Group", "tiktok": "TikTok",
    "instagram": "Instagram", "threads": "Threads", "youtube": "YouTube", "zalo_oa": "Zalo OA",
}
TEN_VAI_TRO = {"nhan_biet": "Nhận biết", "tuong_tac": "Tương tác", "chuyen_doi": "Chuyển đổi"}


def so(x):
    return x if isinstance(x, (int, float)) and not isinstance(x, bool) else None


def chia(a, b):
    a, b = so(a), so(b)
    if a is None or b is None or b == 0:
        return None
    return a / b


def phan_tram_doi(moi, cu):
    r = chia(so(moi) - so(cu) if so(moi) is not None and so(cu) is not None else None, cu)
    return None if r is None else round(r * 100, 1)


def tuong_tac_bai(b):
    vals = [so(b.get(k)) for k in ("thich", "binh_luan", "chia_se", "luu")]
    vals = [v for v in vals if v is not None]
    return sum(vals) if vals else None


def tinh_so_tuan(tu, den):
    try:
        d = (date.fromisoformat(den) - date.fromisoformat(tu)).days + 1
        return max(d / 7.0, 1 / 7.0)
    except (TypeError, ValueError):
        return None


def chi_so_ky(k, nen_tang, ky_so_lieu, bai, so_tuan):
    """Chỉ số cho một kỳ (hiện tại hoặc kỳ trước)."""
    s = dict(ky_so_lieu or {})
    if so(s.get("tuong_tac")) is None and bai:
        tt = [tuong_tac_bai(b) for b in bai]
        tt = [t for t in tt if t is not None]
        s["tuong_tac"] = sum(tt) if tt else None
    if so(s.get("so_bai")) is None and bai:
        s["so_bai"] = len(bai)
    if so(s.get("luot_xem")) is None and so(s.get("reach")) is None and bai:
        # Không có tổng ở trang quản trị: cộng lượt xem từng bài (ghi rõ trong "thieu" của so-lieu.json)
        v = [so(b.get("luot_xem")) for b in bai if so(b.get("luot_xem")) is not None]
        s["luot_xem"] = sum(v) if v else None
    if nen_tang in NEN_TANG_DUNG_VIEW:
        mau = so(s.get("luot_xem")) if so(s.get("luot_xem")) is not None else so(s.get("reach"))
        ten_mau = "lượt xem" if so(s.get("luot_xem")) is not None else "reach"
    else:
        mau = so(s.get("reach")) if so(s.get("reach")) is not None else so(s.get("luot_xem"))
        ten_mau = "reach" if so(s.get("reach")) is not None else "lượt xem"
    dau_ky = so(s.get("follower_dau_ky"))
    if dau_ky is None and so(s.get("follower")) is not None and so(s.get("follower_moi")) is not None:
        dau_ky = s["follower"] - s["follower_moi"]
    lead = so(s.get("lead"))
    lead_paid = so(s.get("lead_paid")) or 0
    lead_organic = None if lead is None else max(lead - lead_paid, 0)
    er = chia(s.get("tuong_tac"), mau)
    tl_follower = chia(s.get("follower_moi"), dau_ky)
    cpl = chia(s.get("chi_phi_ads"), lead_paid) if lead_paid else None
    l1000 = chia(lead_organic, mau)
    return {
        "follower": so(s.get("follower")),
        "follower_moi": so(s.get("follower_moi")),
        "tang_truong_follower_pct": None if tl_follower is None else round(tl_follower * 100, 2),
        "phu_song": mau,
        "ten_phu_song": ten_mau,
        "tuong_tac": so(s.get("tuong_tac")),
        "er_pct": None if er is None else round(er * 100, 2),
        "so_bai": so(s.get("so_bai")),
        "tan_suat_bai_tuan": None if so(s.get("so_bai")) is None or not so_tuan else round(s["so_bai"] / so_tuan, 2),
        "lead": lead,
        "lead_paid": lead_paid if lead is not None else so(s.get("lead_paid")),
        "lead_organic": lead_organic,
        "chi_phi_ads": so(s.get("chi_phi_ads")),
        "cpl": None if cpl is None else round(cpl),
        "lead_tren_1000_phu_song": None if l1000 is None else round(l1000 * 1000, 2),
    }


def chi_so_cong_khai(bai, follower):
    """Chỉ số tính được từ số công khai từng bài, dùng để so với đối thủ."""
    if not bai:
        return {"er_cong_khai_pct": None, "luot_xem_tb_bai": None, "tuong_tac_tb_bai": None, "cach_tinh_er": None}
    views = [so(b.get("luot_xem")) for b in bai]
    tts = [tuong_tac_bai(b) for b in bai]
    cap = [(t, v) for t, v in zip(tts, views) if t is not None and v]
    tt_hop_le = [t for t in tts if t is not None]
    v_hop_le = [v for v in views if v is not None]
    if len(cap) >= max(3, len(bai) // 2):
        er = statistics.mean(t / v for t, v in cap) * 100
        cach = "tương tác / lượt xem mỗi bài"
    elif tt_hop_le and so(follower):
        er = statistics.mean(tt_hop_le) / follower * 100
        cach = "tương tác trung bình mỗi bài / follower"
    else:
        er, cach = None, None
    return {
        "er_cong_khai_pct": None if er is None else round(er, 2),
        "luot_xem_tb_bai": round(statistics.mean(v_hop_le)) if v_hop_le else None,
        "tuong_tac_tb_bai": round(statistics.mean(tt_hop_le)) if tt_hop_le else None,
        "cach_tinh_er": cach,
    }


def phan_tich_noi_dung(bai, nen_tang):
    if not bai:
        return {"top_bai": [], "theo_dinh_dang": [], "theo_chu_de": []}
    dung_view = nen_tang in NEN_TANG_DUNG_VIEW and any(so(b.get("luot_xem")) for b in bai)

    def diem(b):
        if dung_view:
            return so(b.get("luot_xem")) or 0
        return tuong_tac_bai(b) or 0

    sap = sorted(bai, key=diem, reverse=True)
    top = []
    for b in sap[:5]:
        top.append({
            "url": b.get("url"), "ngay": b.get("ngay"), "dinh_dang": b.get("dinh_dang"),
            "chu_de": b.get("chu_de"), "tieu_de": b.get("tieu_de"),
            "luot_xem": so(b.get("luot_xem")), "reach": so(b.get("reach")),
            "tuong_tac": tuong_tac_bai(b),
        })

    def nhom(truong):
        g = {}
        for b in bai:
            khoa = (b.get(truong) or "").strip() or "(chưa gắn)"
            g.setdefault(khoa, []).append(diem(b))
        ra = [{"nhom": k, "so_bai": len(v), "tb_moi_bai": round(statistics.mean(v))} for k, v in g.items()]
        return sorted(ra, key=lambda x: x["tb_moi_bai"], reverse=True)

    return {
        "do_bang": "lượt xem" if dung_view else "tương tác",
        "top_bai": top,
        "theo_dinh_dang": nhom("dinh_dang"),
        "theo_chu_de": nhom("chu_de"),
    }


# ---------- chấm điểm ----------

def muc_theo_doi(pct, ng, dao_nguoc=False):
    if pct is None:
        return None
    if dao_nguoc:
        pct = -pct
    if pct >= ng["tot_tu"]:
        return "Tốt"
    if pct < ng["yeu_duoi"]:
        return "Yếu"
    return "Trung bình"


def muc_theo_ty_le(ty_le, tot_tu, yeu_duoi):
    if ty_le is None:
        return None
    if ty_le >= tot_tu:
        return "Tốt"
    if ty_le < yeu_duoi:
        return "Yếu"
    return "Trung bình"


def gop(ten, cac_moc):
    """cac_moc: list (muc, can_cu). Trả về đánh giá tiêu chí."""
    co = [(m, c) for m, c in cac_moc if m is not None]
    if not co:
        return {"tieu_chi": ten, "muc": "Thiếu số", "diem": None, "can_cu": [c for _, c in cac_moc if c]}
    d = statistics.mean(MUC_DIEM[m] for m, _ in co)
    muc = "Tốt" if d >= 1.5 else ("Yếu" if d < 0.75 else "Trung bình")
    return {"tieu_chi": ten, "muc": muc, "diem": round(d, 2), "can_cu": [f"{c} → {m}" for m, c in co]}


def fmt(x, don_vi=""):
    if x is None:
        return "không có số"
    if isinstance(x, float):
        return f"{x:,.2f}{don_vi}".replace(",", ".")
    return f"{x:,}{don_vi}".replace(",", ".")


def danh_gia_kenh(k, ng, trung_vi_dt, cpl_tb):
    nt = k["nen_tang"]
    ht, kt, ck = k["chi_so"], k["chi_so_ky_truoc"], k["chi_so_cong_khai"]
    dt = trung_vi_dt.get(nt) or {}
    ng_ky = ng["so_voi_ky_truoc"]
    ng_dt = ng["so_voi_doi_thu"]

    def so_dt(gia_tri, ten_dt):
        tv = dt.get(ten_dt)
        r = chia(gia_tri, tv)
        if r is None:
            return (None, None)
        return (muc_theo_ty_le(r, ng_dt["tot_tu"], ng_dt["yeu_duoi"]),
                f"bằng {r:.0%} trung vị đối thủ ({fmt(gia_tri)} so với {fmt(tv)})")

    tc = {}
    # Phủ sóng
    d = phan_tram_doi(ht["phu_song"], kt.get("phu_song"))
    ten_bai = "luot_xem_tb_bai" if nt in NEN_TANG_DUNG_VIEW else "tuong_tac_tb_bai"
    tc["phu_song"] = gop("Phủ sóng (" + ht["ten_phu_song"] + ")", [
        (muc_theo_doi(d, ng_ky), None if d is None else f"{ht['ten_phu_song']} {fmt(d, '%')} so kỳ trước"),
        so_dt(ck.get(ten_bai), ten_bai),
    ])
    # Tăng trưởng follower
    d = phan_tram_doi(ht["follower_moi"], kt.get("follower_moi"))
    tc["tang_truong_follower"] = gop("Tăng trưởng follower", [
        (muc_theo_doi(d, ng_ky), None if d is None else f"follower mới {fmt(d, '%')} so kỳ trước"),
    ])
    # Tỷ lệ tương tác
    d = phan_tram_doi(ht["er_pct"], kt.get("er_pct"))
    nge = ng["ty_le_tuong_tac"].get(nt)
    tc["ty_le_tuong_tac"] = gop("Tỷ lệ tương tác", [
        (muc_theo_doi(d, ng_ky), None if d is None else f"ER {fmt(ht['er_pct'], '%')}, {fmt(d, '%')} so kỳ trước"),
        (muc_theo_ty_le(ht["er_pct"], nge["tot_tu"], nge["yeu_duoi"]) if nge else None,
         None if ht["er_pct"] is None or not nge else f"ER {fmt(ht['er_pct'], '%')} so ngưỡng ngành {nge['yeu_duoi']}–{nge['tot_tu']}%"),
        so_dt(ck.get("er_cong_khai_pct"), "er_cong_khai_pct"),
    ])
    # Tần suất
    toi_thieu = ng["tan_suat_toi_thieu_bai_tuan"].get(nt)
    ts = ht["tan_suat_bai_tuan"]
    tc["tan_suat"] = gop("Tần suất đăng", [
        (muc_theo_ty_le(chia(ts, toi_thieu), 1.0, 0.5) if toi_thieu else None,
         None if ts is None or not toi_thieu else f"{fmt(ts)} bài/tuần, tối thiểu {toi_thieu}"),
        so_dt(ts, "tan_suat_bai_tuan"),
    ])
    # Lead
    d = phan_tram_doi(ht["lead"], kt.get("lead"))
    tc["lead"] = gop("Lead", [
        (muc_theo_doi(d, ng_ky), None if d is None else f"lead {fmt(ht['lead'])}, {fmt(d, '%')} so kỳ trước"),
    ])
    d = phan_tram_doi(ht["cpl"], kt.get("cpl"))
    r = chia(ht["cpl"], cpl_tb)
    tc["cpl"] = gop("Chi phí / lead", [
        (muc_theo_doi(d, ng_ky, dao_nguoc=True), None if d is None else f"CPL {fmt(ht['cpl'])}đ, {fmt(d, '%')} so kỳ trước"),
        (None if r is None else ("Tốt" if r <= ng["cpl_tot_neu_duoi_trung_binh_tai_khoan"] else
                                 "Yếu" if r > ng["cpl_yeu_neu_tren_trung_binh_tai_khoan"] else "Trung bình"),
         None if r is None else f"CPL bằng {r:.0%} trung bình các kênh ({fmt(round(cpl_tb))}đ)"),
    ])
    d = phan_tram_doi(ht["lead_tren_1000_phu_song"], kt.get("lead_tren_1000_phu_song"))
    tc["lead_tren_1000"] = gop("Lead / 1.000 " + ht["ten_phu_song"], [
        (muc_theo_doi(d, ng_ky), None if d is None else f"{fmt(ht['lead_tren_1000_phu_song'])} lead/1.000, {fmt(d, '%')} so kỳ trước"),
    ])

    vai_tro = k.get("vai_tro") or "nhan_biet"
    if vai_tro == "chuyen_doi":
        chinh, phu = ["lead", "cpl", "lead_tren_1000"], ["ty_le_tuong_tac", "phu_song", "tan_suat"]
    elif vai_tro == "tuong_tac":
        chinh, phu = ["ty_le_tuong_tac"], ["phu_song", "tan_suat", "tang_truong_follower"]
    else:
        chinh, phu = ["phu_song", "tang_truong_follower"], ["ty_le_tuong_tac", "tan_suat"]

    diem_chinh = [tc[x]["diem"] for x in chinh if tc[x]["diem"] is not None]
    muc_phu = [tc[x]["muc"] for x in phu if tc[x]["diem"] is not None]
    if diem_chinh:
        dc = statistics.mean(diem_chinh)
        muc_chinh = "Tốt" if dc >= 1.5 else ("Yếu" if dc < 0.75 else "Trung bình")
    else:
        muc_chinh = "Thiếu số"

    so_bai = ht["so_bai"]
    if muc_chinh == "Thiếu số" or (so_bai is not None and so_bai < ng["it_bai_chua_du_du_lieu"]):
        kl = "Chưa đủ dữ liệu"
        ly = "thiếu chỉ số chính" if muc_chinh == "Thiếu số" else f"chỉ có {so_bai} bài trong kỳ"
    elif muc_chinh == "Tốt" and "Yếu" not in muc_phu:
        kl, ly = "Đẩy mạnh", "chỉ số chính Tốt, không chỉ số phụ nào Yếu"
    elif muc_chinh in ("Tốt", "Trung bình"):
        yeu = [tc[x]["tieu_chi"] for x in phu if tc[x]["muc"] == "Yếu"]
        kl = "Giữ"
        ly = f"chỉ số chính {muc_chinh}" + (f", yếu ở: {', '.join(yeu)}" if yeu else "")
    elif any(m in ("Tốt", "Trung bình") for m in muc_phu):
        kl, ly = "Tối ưu", "chỉ số chính Yếu nhưng còn chỉ số phụ khá"
    else:
        kl, ly = "Bỏ / tạm dừng", "chỉ số chính Yếu, không còn chỉ số nào khá"

    return {
        "vai_tro": vai_tro,
        "ten_vai_tro": TEN_VAI_TRO.get(vai_tro, vai_tro),
        "tieu_chi_chinh": chinh,
        "tieu_chi_phu": phu,
        "tieu_chi": tc,
        "muc_chinh": muc_chinh,
        "ket_luan_so_bo": kl,
        "ly_do_so_bo": ly,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("so_lieu")
    ap.add_argument("--nguong", default=os.path.join(PLUGIN_ROOT, "references", "nguong.json"))
    a = ap.parse_args()

    with open(a.so_lieu, encoding="utf-8") as f:
        sl = json.load(f)
    with open(a.nguong, encoding="utf-8") as f:
        ng = json.load(f)

    ky = sl.get("ky") or {}
    so_tuan = tinh_so_tuan(ky.get("tu"), ky.get("den"))
    so_tuan_truoc = tinh_so_tuan(ky.get("ky_truoc_tu"), ky.get("ky_truoc_den")) or so_tuan

    kenh_ra = []
    for k in sl.get("kenh", []):
        nt = k.get("nen_tang")
        bai = k.get("bai") or []
        ht = chi_so_ky(k, nt, k.get("hien_tai"), bai, so_tuan)
        kt = chi_so_ky(k, nt, k.get("ky_truoc"), [], so_tuan_truoc) if k.get("ky_truoc") else {}
        ck = chi_so_cong_khai(bai, ht["follower"])
        ck["tan_suat_bai_tuan"] = ht["tan_suat_bai_tuan"]
        kenh_ra.append({
            "id": k.get("id"), "nen_tang": nt, "ten_nen_tang": TEN_NEN_TANG.get(nt, nt),
            "ten": k.get("ten"), "url": k.get("url"), "cua": k.get("cua", "minh"),
            "doi_thu": k.get("doi_thu"), "vai_tro": k.get("vai_tro"),
            "chi_so": ht, "chi_so_ky_truoc": kt, "chi_so_cong_khai": ck,
            "noi_dung": phan_tich_noi_dung(bai, nt),
            "nguon": k.get("nguon") or [], "thieu": k.get("thieu") or [], "ghi_chu": k.get("ghi_chu") or "",
        })

    # Trung vị đối thủ theo nền tảng (chỉ số công khai)
    trung_vi = {}
    for nt in {k["nen_tang"] for k in kenh_ra if k["cua"] == "doi_thu"}:
        ds = [k for k in kenh_ra if k["cua"] == "doi_thu" and k["nen_tang"] == nt]
        tv = {"so_kenh": len(ds)}
        for truong in ("er_cong_khai_pct", "luot_xem_tb_bai", "tuong_tac_tb_bai", "tan_suat_bai_tuan"):
            v = [k["chi_so_cong_khai"].get(truong) for k in ds if k["chi_so_cong_khai"].get(truong) is not None]
            tv[truong] = round(statistics.median(v), 2) if v else None
        v = [k["chi_so"]["follower"] for k in ds if k["chi_so"]["follower"] is not None]
        tv["follower"] = round(statistics.median(v)) if v else None
        trung_vi[nt] = tv

    minh = [k for k in kenh_ra if k["cua"] == "minh"]
    tong_cp = sum(k["chi_so"]["chi_phi_ads"] or 0 for k in minh)
    tong_lp = sum(k["chi_so"]["lead_paid"] or 0 for k in minh)
    cpl_tb = chia(tong_cp, tong_lp)
    for k in minh:
        k["danh_gia"] = danh_gia_kenh(k, ng, trung_vi, cpl_tb)

    tong_lead = sum(k["chi_so"]["lead"] or 0 for k in minh)
    ra = {
        "doanh_nghiep": sl.get("doanh_nghiep"),
        "ky": ky,
        "so_tuan": None if so_tuan is None else round(so_tuan, 1),
        "ngay_lay": sl.get("ngay_lay"),
        "kenh": kenh_ra,
        "trung_vi_doi_thu": trung_vi,
        "tong_hop": {
            "tong_lead": tong_lead,
            "lead_khong_ro_nguon": so(sl.get("lead_khong_ro_nguon")),
            "tong_chi_phi_ads": tong_cp,
            "cpl_trung_binh": None if cpl_tb is None else round(cpl_tb),
            "phan_bo_lead": [
                {"id": k["id"], "ten_nen_tang": k["ten_nen_tang"], "lead": k["chi_so"]["lead"],
                 "ty_trong_pct": None if not tong_lead or k["chi_so"]["lead"] is None else round(k["chi_so"]["lead"] / tong_lead * 100, 1)}
                for k in minh
            ],
            "ket_luan": {kl: [k["id"] for k in minh if k["danh_gia"]["ket_luan_so_bo"] == kl]
                         for kl in ("Đẩy mạnh", "Giữ", "Tối ưu", "Bỏ / tạm dừng", "Chưa đủ dữ liệu")},
        },
    }
    out = os.path.join(os.path.dirname(os.path.abspath(a.so_lieu)), "chi-so.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(ra, f, ensure_ascii=False, indent=2)
    print(f"Đã ghi {out}")
    for k in minh:
        dg = k["danh_gia"]
        print(f"- {k['ten_nen_tang']} ({dg['ten_vai_tro']}): chính {dg['muc_chinh']} → {dg['ket_luan_so_bo']} ({dg['ly_do_so_bo']})")


if __name__ == "__main__":
    sys.exit(main())
