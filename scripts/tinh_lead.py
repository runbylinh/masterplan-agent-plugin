#!/usr/bin/env python3
"""Tính chỉ số lead & hội thoại từ hoi-thoai.json, dựng bao-cao.html và CSV cho Sheets.

Cách dùng:
    python3 tinh_lead.py <thu-muc-ky> [--cau-hinh duong-dan/cau-hinh.json]
Đọc:  hoi-thoai.json, nhan-dinh.json (không bắt buộc), cau-hinh.json (tìm ngược lên từ thư mục kỳ)
Ghi:  chi-so-lead.json, bao-cao.html, sheets/lead-theo-kenh.csv, sheets/ly-do-khong-chot.csv
"""
import argparse
import json
import os
import statistics
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import html_chung as H  # noqa: E402

TEN_KENH = {"messenger": "Messenger fanpage", "instagram": "Instagram Direct", "zalo_oa": "Zalo OA",
            "zalo_ca_nhan": "Zalo web (cá nhân)", "zalo_web": "Zalo web (cá nhân)", "tiktok": "TikTok tin nhắn",
            "tiktok_shop": "TikTok Shop chat", "shopee": "Shopee chat", "website_chat": "Chat website",
            "lead_form": "Form / landing page"}
TEN_MUC = {"nong": "Nóng", "am": "Ấm", "lanh": "Lạnh", "khong_phu_hop": "Không phù hợp", "khong_ro": "Không rõ"}
TEN_LY_DO = {"gia": "Giá", "thoi_gian_lich": "Thời gian / lịch", "chua_tin": "Chưa đủ tin tưởng",
             "chua_ro_loi_ich": "Chưa rõ lợi ích", "so_sanh_doi_thu": "So sánh đối thủ", "phan_hoi_cham": "Phản hồi chậm",
             "tu_van_chua_toi": "Tư vấn chưa tới", "chua_co_nhu_cau_ngay": "Chưa cần ngay", "khac": "Khác"}
MAU_TOI_THIEU = 20


def tim_cau_hinh(thu_muc):
    d = os.path.abspath(thu_muc)
    for _ in range(4):
        p = os.path.join(d, "cau-hinh.json")
        if os.path.exists(p):
            return p
        d = os.path.dirname(d)
    return None


def ty_le(a, b):
    return None if a is None or not b else round(a / b * 100, 1)


def dem_nhan(theo_nhan, ds_nhan):
    if not theo_nhan:
        return None
    ds = {x.strip().lower() for x in ds_nhan}
    vals = [v for k, v in theo_nhan.items() if k.strip().lower() in ds and isinstance(v, (int, float))]
    return sum(vals) if vals else (0 if theo_nhan else None)


def phan_tich_mau(mau):
    if not mau:
        return None
    nm = len(mau)
    muc = Counter(m.get("muc") or "khong_ro" for m in mau)
    tt = Counter(m.get("trang_thai") or "khong_ro" for m in mau)
    ly_do = Counter(m.get("ly_do_khong_chot") for m in mau if m.get("ly_do_khong_chot"))
    ph = [m["phan_hoi_dau_phut"] for m in mau if isinstance(m.get("phan_hoi_dau_phut"), (int, float))]
    cau_hoi = Counter(c.strip().lower() for m in mau for c in (m.get("cau_hoi") or []) if c and c.strip())
    theo_nguon = {}
    for ng in sorted({m.get("nguon") or "khong_ro" for m in mau}):
        g = [m for m in mau if (m.get("nguon") or "khong_ro") == ng]
        theo_nguon[ng] = {"so": len(g), "ty_le_chot_pct": ty_le(sum(1 for m in g if m.get("trang_thai") == "chot"), len(g)),
                          "ty_le_nong_pct": ty_le(sum(1 for m in g if m.get("muc") == "nong"), len(g))}
    theo_toc_do = []
    if len(ph) >= MAU_TOI_THIEU:
        for ten, lo, hi in (("≤ 15 phút", 0, 15), ("15–60 phút", 15.0001, 60), ("> 60 phút", 60.0001, 10 ** 9)):
            g = [m for m in mau if isinstance(m.get("phan_hoi_dau_phut"), (int, float)) and lo <= m["phan_hoi_dau_phut"] <= hi]
            if g:
                theo_toc_do.append({"nhom": ten, "so": len(g),
                                    "ty_le_chot_pct": ty_le(sum(1 for m in g if m.get("trang_thai") == "chot"), len(g))})
    return {
        "co_mau": nm,
        "du_mau": nm >= MAU_TOI_THIEU,
        "muc": {k: {"so": v, "pct": ty_le(v, nm)} for k, v in muc.items()},
        "trang_thai": {k: {"so": v, "pct": ty_le(v, nm)} for k, v in tt.items()},
        "ty_le_chot_mau_pct": ty_le(tt.get("chot", 0), nm),
        "phan_hoi_trung_vi_phut": round(statistics.median(ph), 1) if ph else None,
        "ly_do_khong_chot": [{"ly_do": k, "ten": TEN_LY_DO.get(k, k), "so": v} for k, v in ly_do.most_common()],
        "cau_hoi_hay_gap": [{"cau_hoi": k, "so": v} for k, v in cau_hoi.most_common(10)],
        "theo_nguon": theo_nguon,
        "theo_toc_do_phan_hoi": theo_toc_do,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("thu_muc")
    ap.add_argument("--cau-hinh")
    a = ap.parse_args()
    with open(os.path.join(a.thu_muc, "hoi-thoai.json"), encoding="utf-8") as f:
        ht = json.load(f)
    ch_path = a.cau_hinh or tim_cau_hinh(a.thu_muc)
    ch = {}
    if ch_path:
        with open(ch_path, encoding="utf-8") as f:
            ch = json.load(f)
    hop = ch.get("hop_thu") or {}
    nhan_chot = hop.get("nhan_chot") or ["Đã chốt"]
    nhan_kpp = hop.get("nhan_khong_phu_hop") or []
    nd = {}
    p = os.path.join(a.thu_muc, "nhan-dinh.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            nd = json.load(f)

    mau_all = ht.get("mau") or []
    kenh_ra = []
    for k in ht.get("tong_theo_kenh") or []:
        hi, kt = k.get("hien_tai") or {}, k.get("ky_truoc") or {}
        chot_nhan = dem_nhan(hi.get("theo_nhan"), nhan_chot)
        chot_nhan_kt = dem_nhan(kt.get("theo_nhan"), nhan_chot)
        kpp = dem_nhan(hi.get("theo_nhan"), nhan_kpp) if nhan_kpp else None
        so_ht = hi.get("hoi_thoai")
        mau = [m for m in mau_all if m.get("kenh") == k["kenh"]]
        kenh_ra.append({
            "kenh": k["kenh"], "ten": k.get("ten") or TEN_KENH.get(k["kenh"], k["kenh"]),
            "hoi_thoai": so_ht, "hoi_thoai_ky_truoc": kt.get("hoi_thoai"),
            "tu_quang_cao": hi.get("tu_quang_cao"), "tu_nguoi_la": hi.get("tu_nguoi_la"), "chua_tra_loi": hi.get("chua_tra_loi"),
            "ty_le_phan_hoi_pct": hi.get("ty_le_phan_hoi_pct"), "phan_hoi_tb_phut": hi.get("phan_hoi_tb_phut"),
            "lead_form": hi.get("lead_form"),
            "chot_theo_nhan": chot_nhan, "ty_le_chot_nhan_pct": ty_le(chot_nhan, so_ht),
            "ty_le_chot_nhan_ky_truoc_pct": ty_le(chot_nhan_kt, kt.get("hoi_thoai")),
            "khong_phu_hop_theo_nhan": kpp, "ty_le_khong_phu_hop_pct": ty_le(kpp, so_ht),
            "don": hi.get("don"), "don_ky_truoc": kt.get("don"), "doanh_thu": hi.get("doanh_thu"),
            "ty_le_chot_don_pct": ty_le(hi.get("don"), so_ht),
            "mau": phan_tich_mau(mau),
            "nguon": k.get("nguon") or [], "thieu": k.get("thieu") or [],
        })

    tong_ht = sum(k["hoi_thoai"] or 0 for k in kenh_ra)
    tong_chot = sum(k["chot_theo_nhan"] or 0 for k in kenh_ra) if any(k["chot_theo_nhan"] is not None for k in kenh_ra) else None
    tong_don = sum(k["don"] or 0 for k in kenh_ra) if any(k["don"] is not None for k in kenh_ra) else None
    ra = {"doanh_nghiep": ht.get("doanh_nghiep"), "ky": ht.get("ky"), "ngay_lay": ht.get("ngay_lay"),
          "nhan_chot": nhan_chot, "kenh": kenh_ra, "toan_bo_mau": phan_tich_mau(mau_all),
          "tong": {"hoi_thoai": tong_ht, "chot_theo_nhan": tong_chot, "ty_le_chot_nhan_pct": ty_le(tong_chot, tong_ht),
                   "don": tong_don, "ty_le_chot_don_pct": ty_le(tong_don, tong_ht)}}
    with open(os.path.join(a.thu_muc, "chi-so-lead.json"), "w", encoding="utf-8") as f:
        json.dump(ra, f, ensure_ascii=False, indent=2)

    # ---------- HTML ----------
    ky = ht.get("ky") or {}
    t = ra["tong"]
    tm = ra["toan_bo_mau"] or {}
    phan = []
    if nd.get("tom_tat"):
        phan.append(H.section("Tóm tắt", f'<p class="lead">{H.e(nd["tom_tat"])}</p>'))
    phan.append(H.section("Tổng quan", H.tiles([
        ("Hội thoại", H.n(t["hoi_thoai"]), H.the_doi(t["hoi_thoai"], sum(k["hoi_thoai_ky_truoc"] or 0 for k in kenh_ra) or None)),
        ("Chốt theo nhãn", H.n(t["chot_theo_nhan"]), f'tỷ lệ {H.n(t["ty_le_chot_nhan_pct"], "%")}'),
        ("Đơn (file/CRM)", H.n(t["don"]), f'tỷ lệ {H.n(t["ty_le_chot_don_pct"], "%")}'),
        ("Chốt trong mẫu đọc", H.n(tm.get("ty_le_chot_mau_pct"), "%"), f'{H.n(tm.get("co_mau"))} hội thoại đã đọc'),
        ("Phản hồi đầu (trung vị)", H.n(tm.get("phan_hoi_trung_vi_phut"), " phút"), "từ mẫu đọc"),
    ])))
    hang = []
    for k in kenh_ra:
        m = k["mau"] or {}
        nong = ((m.get("muc") or {}).get("nong") or {}).get("pct")
        hang.append([f'<b>{H.e(k["ten"])}</b>', k["hoi_thoai"], H.the_doi(k["hoi_thoai"], k["hoi_thoai_ky_truoc"]),
                     H.n(k["tu_quang_cao"]) + (f' <span class="muted small">· người lạ {H.n(k["tu_nguoi_la"])}</span>' if k.get("tu_nguoi_la") is not None else ""),
                     H.n(k["ty_le_chot_nhan_pct"], "%"), H.n(k["ty_le_chot_don_pct"], "%"),
                     H.n(m.get("ty_le_chot_mau_pct"), "%") + (f' <span class="muted small">(n={m["co_mau"]})</span>' if m else ""),
                     H.n(nong, "%"), H.n(k["phan_hoi_tb_phut"] if k["phan_hoi_tb_phut"] is not None else m.get("phan_hoi_trung_vi_phut"), " ph")])
    phan.append(H.section("Theo kênh", H.bang(["Kênh", "Hội thoại", "So kỳ trước", "Từ quảng cáo", "Chốt (nhãn)",
                                               "Chốt (đơn)", "Chốt (mẫu)", "Lead nóng", "Phản hồi"], hang, cot_so=(1, 3, 4, 5, 6, 7, 8)),
                          "Ba cách tính tỷ lệ chốt: theo nhãn team gắn, theo file đơn/CRM, theo mẫu agent đọc chat. "
                          f"Mẫu dưới {MAU_TOI_THIEU} hội thoại chỉ để tham khảo."))
    phan.append(H.section("Hội thoại theo kênh", H.cot_ngang([k["ten"] for k in kenh_ra], [k["hoi_thoai"] for k in kenh_ra],
                                                            gia_tri_b=[k["hoi_thoai_ky_truoc"] for k in kenh_ra],
                                                            chu_thich=("Kỳ này", "Kỳ trước"))))
    if tm:
        muc = tm.get("muc") or {}
        phan.append(H.section("Chất lượng lead (mẫu đọc)", H.cot_ngang(
            [TEN_MUC.get(x, x) for x in ("nong", "am", "lanh", "khong_phu_hop", "khong_ro") if x in muc],
            [muc[x]["pct"] for x in ("nong", "am", "lanh", "khong_phu_hop", "khong_ro") if x in muc], "%")
            + (H.bang(["Nguồn", "Số hội thoại", "Tỷ lệ chốt", "Tỷ lệ lead nóng"],
                      [[H.e({"quang_cao": "Quảng cáo", "tu_nhien": "Tự nhiên"}.get(k, "Không rõ")), v["so"],
                        H.n(v["ty_le_chot_pct"], "%"), H.n(v["ty_le_nong_pct"], "%")] for k, v in tm["theo_nguon"].items()],
                      cot_so=(1, 2, 3)) if tm.get("theo_nguon") else "")))
        if tm.get("ly_do_khong_chot"):
            phan.append(H.section("Lý do không chốt", H.cot_ngang([x["ten"] for x in tm["ly_do_khong_chot"]],
                                                                  [x["so"] for x in tm["ly_do_khong_chot"]])))
        if tm.get("theo_toc_do_phan_hoi"):
            phan.append(H.section("Tốc độ phản hồi và tỷ lệ chốt", H.bang(
                ["Phản hồi đầu", "Số hội thoại", "Tỷ lệ chốt"],
                [[x["nhom"], x["so"], H.n(x["ty_le_chot_pct"], "%")] for x in tm["theo_toc_do_phan_hoi"]], cot_so=(1, 2))))
        if tm.get("cau_hoi_hay_gap"):
            phan.append(H.section("Câu hỏi khách hay hỏi", H.bang(["Câu hỏi", "Số lần"],
                                                                 [[H.e(x["cau_hoi"]), x["so"]] for x in tm["cau_hoi_hay_gap"]], cot_so=(1,))))
    if nd.get("diem_nghen") or nd.get("kich_ban_tot") or nd.get("uu_tien"):
        s = ""
        if nd.get("diem_nghen"):
            s += f'<p><b>Điểm nghẽn:</b> {H.e(nd["diem_nghen"])}</p>'
        if nd.get("kich_ban_tot"):
            s += f'<p><b>Cách tư vấn chốt tốt:</b> {H.e(nd["kich_ban_tot"])}</p>'
        if nd.get("uu_tien"):
            s += "<h4>Ưu tiên</h4>" + H.ds(nd["uu_tien"])
        phan.append(H.section("Nhận định", s))
    nguon = [f'<li>{H.e(k["ten"])}: {H.e(g.get("chi_so"))} — {H.e(g.get("noi_lay"))}, {H.e(g.get("ngay_lay"))}</li>'
             for k in kenh_ra for g in k["nguon"]]
    thieu = [f'<li>{H.e(k["ten"])}: {H.e(g.get("chi_so"))} ({H.e(g.get("ly_do"))})</li>' for k in kenh_ra for g in k["thieu"]]
    if nguon or thieu:
        phan.append(H.section("Nguồn và phần thiếu", '<ul class="small">' + "".join(nguon + thieu) + "</ul>"))
    with open(os.path.join(a.thu_muc, "bao-cao.html"), "w", encoding="utf-8") as f:
        f.write(H.trang("Lead và hội thoại", "Lead & hội thoại", ht.get("doanh_nghiep") or "",
                        f'Kỳ {ky.get("tu")} → {ky.get("den")} · so với {ky.get("ky_truoc_tu")} → {ky.get("ky_truoc_den")}', phan))

    ten_ky = f'{ky.get("tu")} → {ky.get("den")}'
    H.ghi_csv(os.path.join(a.thu_muc, "sheets", "lead-theo-kenh.csv"),
              ["Kỳ", "Kênh", "Hội thoại", "Hội thoại kỳ trước", "Từ quảng cáo", "Từ người lạ (Zalo)", "Chưa trả lời", "Chốt theo nhãn",
               "Tỷ lệ chốt nhãn %", "Đơn", "Tỷ lệ chốt đơn %", "Doanh thu", "Cỡ mẫu đọc", "Tỷ lệ chốt mẫu %",
               "Lead nóng % (mẫu)", "Phản hồi TB (phút)", "Duyệt"],
              [[ten_ky, k["ten"], k["hoi_thoai"], k["hoi_thoai_ky_truoc"], k["tu_quang_cao"], k.get("tu_nguoi_la"), k["chua_tra_loi"],
                k["chot_theo_nhan"], k["ty_le_chot_nhan_pct"], k["don"], k["ty_le_chot_don_pct"], k["doanh_thu"],
                (k["mau"] or {}).get("co_mau"), (k["mau"] or {}).get("ty_le_chot_mau_pct"),
                (((k["mau"] or {}).get("muc") or {}).get("nong") or {}).get("pct"),
                k["phan_hoi_tb_phut"] if k["phan_hoi_tb_phut"] is not None else (k["mau"] or {}).get("phan_hoi_trung_vi_phut"),
                "Chờ duyệt"] for k in kenh_ra])
    H.ghi_csv(os.path.join(a.thu_muc, "sheets", "ly-do-khong-chot.csv"), ["Kỳ", "Lý do", "Số hội thoại"],
              [[ten_ky, x["ten"], x["so"]] for x in (tm.get("ly_do_khong_chot") or [])])
    print(f"Đã ghi chi-so-lead.json, bao-cao.html, sheets/ trong {a.thu_muc}")
    for k in kenh_ra:
        print(f'- {k["ten"]}: {H.n(k["hoi_thoai"])} hội thoại, chốt theo nhãn {H.n(k["ty_le_chot_nhan_pct"], "%")}, '
              f'chốt theo đơn {H.n(k["ty_le_chot_don_pct"], "%")}')
    return 0


if __name__ == "__main__":
    sys.exit(main())
