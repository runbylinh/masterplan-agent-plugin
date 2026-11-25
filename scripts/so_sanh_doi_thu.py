#!/usr/bin/env python3
"""So lần quét đối thủ hiện tại với lần trước, dựng báo cáo HTML và CSV.

Cách dùng:
    python3 so_sanh_doi_thu.py doi-thu/YYYY-MM-DD
Đọc:  quet.json, nhan-dinh.json (không bắt buộc), ../lich-su/*.json (lần quét trước)
Ghi:  thay-doi.json, bao-cao.html, sheets/offer.csv, sheets/ads.csv, sheets/thay-doi.csv,
      ../lich-su/<ngay_quet>.json
"""
import glob
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import html_chung as H  # noqa: E402


def khoa_ads(a):
    return a.get("library_id") or f'{a.get("nen_tang")}|{a.get("link_dich")}|{a.get("thong_diep")}'


def so_sanh(moi, cu):
    """Trả về danh sách thay đổi cho một đối thủ."""
    tdoi = []
    if cu is None:
        return [{"loai": "Lần quét đầu", "chi_tiet": "chưa có lần trước để so"}]
    om = {o.get("ma") or o.get("ten"): o for o in moi.get("offer") or []}
    oc = {o.get("ma") or o.get("ten"): o for o in cu.get("offer") or []}
    for k, o in om.items():
        if k not in oc:
            tdoi.append({"loai": "Offer mới", "chi_tiet": f'{o.get("ten")}: {H.n(o.get("gia_uu_dai") or o.get("gia_niem_yet"), "đ")}'})
        else:
            c = oc[k]
            for tr in ("gia_niem_yet", "gia_uu_dai", "qua_tang", "cam_ket"):
                if o.get(tr) != c.get(tr) and (o.get(tr) or c.get(tr)):
                    tdoi.append({"loai": "Offer đổi", "chi_tiet": f'{o.get("ten")} – {tr}: {c.get(tr)} → {o.get(tr)}'})
    for k, o in oc.items():
        if k not in om:
            tdoi.append({"loai": "Offer không còn thấy", "chi_tiet": o.get("ten")})
    km = {x.get("ma") or x.get("ten"): x for x in moi.get("khuyen_mai") or []}
    kc = {x.get("ma") or x.get("ten"): x for x in cu.get("khuyen_mai") or []}
    for k, x in km.items():
        if k not in kc:
            tdoi.append({"loai": "Khuyến mãi mới", "chi_tiet": f'{x.get("ten")} ({x.get("muc_giam")}, {x.get("tu") or "?"} → {x.get("den") or "?"})'})
    for k, x in kc.items():
        if k not in km:
            tdoi.append({"loai": "Khuyến mãi đã kết thúc / không còn thấy", "chi_tiet": x.get("ten")})
    am = {khoa_ads(a): a for a in moi.get("ads") or [] if a.get("dang_chay", True)}
    ac = {khoa_ads(a): a for a in cu.get("ads") or [] if a.get("dang_chay", True)}
    moi_ads = [a for k, a in am.items() if k not in ac]
    tat_ads = [a for k, a in ac.items() if k not in am]
    if moi_ads:
        tdoi.append({"loai": "Ads mới", "chi_tiet": f'{len(moi_ads)} mẫu: ' + "; ".join((a.get("thong_diep") or "")[:60] for a in moi_ads[:5])})
    if tat_ads:
        tdoi.append({"loai": "Ads đã tắt", "chi_tiet": f'{len(tat_ads)} mẫu: ' + "; ".join((a.get("thong_diep") or "")[:60] for a in tat_ads[:5])})
    cd_moi = {c for k in moi.get("kenh") or [] for c in k.get("chu_de_chu_luc") or []}
    cd_cu = {c for k in cu.get("kenh") or [] for c in k.get("chu_de_chu_luc") or []}
    if cd_moi - cd_cu:
        tdoi.append({"loai": "Chủ đề nội dung mới", "chi_tiet": ", ".join(sorted(cd_moi - cd_cu))})
    if not tdoi:
        tdoi.append({"loai": "Không đổi", "chi_tiet": "không thấy thay đổi offer, khuyến mãi, ads, chủ đề"})
    return tdoi


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    thu_muc = os.path.abspath(sys.argv[1])
    with open(os.path.join(thu_muc, "quet.json"), encoding="utf-8") as f:
        q = json.load(f)
    ngay = q.get("ngay_quet") or os.path.basename(thu_muc)
    lich_su = os.path.join(os.path.dirname(thu_muc), "lich-su")
    os.makedirs(lich_su, exist_ok=True)
    truoc = sorted(p for p in glob.glob(os.path.join(lich_su, "*.json")) if os.path.basename(p)[:-5] < ngay)
    qc = None
    if truoc:
        with open(truoc[-1], encoding="utf-8") as f:
            qc = json.load(f)
    cu_theo_ten = {d["ten"]: d for d in (qc or {}).get("doi_thu") or []}
    nd = {}
    p = os.path.join(thu_muc, "nhan-dinh.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            nd = json.load(f)

    thay_doi = {d["ten"]: so_sanh(d, cu_theo_ten.get(d["ten"]) if qc else None) for d in q.get("doi_thu") or []}
    with open(os.path.join(thu_muc, "thay-doi.json"), "w", encoding="utf-8") as f:
        json.dump({"ngay_quet": ngay, "so_voi": (qc or {}).get("ngay_quet"), "thay_doi": thay_doi}, f, ensure_ascii=False, indent=2)

    phan = []
    if nd.get("tom_tat"):
        phan.append(H.section("Tóm tắt", f'<p class="lead">{H.e(nd["tom_tat"])}</p>'))
    hang = []
    for d in q.get("doi_thu") or []:
        ads_chay = [a for a in d.get("ads") or [] if a.get("dang_chay", True)]
        hang.append([f'<b>{H.e(d["ten"])}</b>', len(d.get("offer") or []), len(d.get("khuyen_mai") or []), len(ads_chay),
                     "<br>".join(f'<span class="tag">{H.e(t["loai"])}</span>{H.e(t["chi_tiet"])}' for t in thay_doi[d["ten"]])])
    phan.append(H.section("Có gì mới" + (f' so với {qc.get("ngay_quet")}' if qc else ""),
                          H.bang(["Đối thủ", "Offer", "Khuyến mãi", "Ads đang chạy", "Thay đổi"], hang, cot_so=(1, 2, 3))))
    # Bảng offer
    oh = []
    for d in q.get("doi_thu") or []:
        for o in d.get("offer") or []:
            oh.append([H.e(d["ten"]), f'<a href="{H.e(o.get("url"))}" target="_blank" rel="noopener">{H.e(o.get("ten"))}</a>',
                       o.get("gia_niem_yet"), o.get("gia_uu_dai"), H.e(o.get("qua_tang")), H.e(o.get("cam_ket"))])
    if oh:
        phan.append(H.section("Offer và giá", H.bang(["Đối thủ", "Sản phẩm / gói", "Giá niêm yết", "Giá ưu đãi", "Quà tặng", "Cam kết"], oh, cot_so=(2, 3))))
    kh = []
    for d in q.get("doi_thu") or []:
        for x in d.get("khuyen_mai") or []:
            kh.append([H.e(d["ten"]), H.e(x.get("ten")), H.e(x.get("muc_giam")), H.e(f'{x.get("tu") or "?"} → {x.get("den") or "?"}'),
                       H.e(x.get("dieu_kien")), H.e(", ".join(x.get("kenh") or []))])
    if kh:
        phan.append(H.section("Khuyến mãi đang chạy", H.bang(["Đối thủ", "Chương trình", "Mức giảm", "Thời gian", "Điều kiện", "Kênh"], kh)))
    ah = []
    for d in q.get("doi_thu") or []:
        for a in d.get("ads") or []:
            if a.get("dang_chay", True):
                ah.append([H.e(d["ten"]), H.e(a.get("nen_tang")), H.e(a.get("bat_dau")), H.e(a.get("dinh_dang")),
                           H.e(a.get("thong_diep")), H.e(a.get("cta")),
                           f'<a href="{H.e(a.get("link_dich"))}" target="_blank" rel="noopener">link</a>' if a.get("link_dich") else "–"])
    if ah:
        phan.append(H.section("Quảng cáo đang chạy", H.bang(["Đối thủ", "Nền tảng", "Bắt đầu", "Định dạng", "Thông điệp", "CTA", "Đích"], ah)))
    for d in q.get("doi_thu") or []:
        s = ""
        for k in d.get("kenh") or []:
            s += (f'<h4>{H.e(k.get("nen_tang"))} · <a href="{H.e(k.get("url"))}" target="_blank" rel="noopener">kênh</a></h4>'
                  f'<p class="small">Follower {H.n(k.get("follower"))} · {H.n(k.get("so_bai_trong_ky"))} bài trong kỳ · '
                  f'chủ đề: {H.e(", ".join(k.get("chu_de_chu_luc") or []) or "–")} · định dạng: {H.e(", ".join(k.get("dinh_dang_chu_luc") or []) or "–")}</p>')
            if k.get("bai_noi_bat"):
                s += H.bang(["Ngày", "Hook", "Lượt xem", "Tương tác"],
                            [[H.e(b.get("ngay")), f'<a href="{H.e(b.get("url"))}" target="_blank" rel="noopener">{H.e(b.get("hook"))}</a>',
                              b.get("luot_xem"), b.get("tuong_tac")] for b in k["bai_noi_bat"]], cot_so=(2, 3))
        if (nd.get("doi_thu") or {}).get(d["ten"]):
            s = f'<p>{H.e(nd["doi_thu"][d["ten"]])}</p>' + s
        if d.get("khong_thay"):
            s += '<p class="small muted">Không thấy: ' + H.e("; ".join(d["khong_thay"])) + "</p>"
        phan.append(H.section(f'Nội dung: {d["ten"]}', s))
    if nd.get("goi_y_cho_minh"):
        phan.append(H.section("Gợi ý cho mình", H.ds(nd["goi_y_cho_minh"])))
    with open(os.path.join(thu_muc, "bao-cao.html"), "w", encoding="utf-8") as f:
        f.write(H.trang("Quét đối thủ", "Quét đối thủ", f"Ngày quét {ngay}",
                        f'Nhìn lại {q.get("khoang_nhin_lai_ngay", "?")} ngày' + (f' · so với lần quét {qc.get("ngay_quet")}' if qc else " · lần quét đầu"), phan))

    H.ghi_csv(os.path.join(thu_muc, "sheets", "offer.csv"),
              ["Ngày quét", "Đối thủ", "Sản phẩm / gói", "Giá niêm yết", "Giá ưu đãi", "Quà tặng", "Cam kết", "Link", "Duyệt"],
              [[ngay, d["ten"], o.get("ten"), o.get("gia_niem_yet"), o.get("gia_uu_dai"), o.get("qua_tang"), o.get("cam_ket"), o.get("url"), "Chờ duyệt"]
               for d in q.get("doi_thu") or [] for o in d.get("offer") or []])
    H.ghi_csv(os.path.join(thu_muc, "sheets", "ads.csv"),
              ["Ngày quét", "Đối thủ", "Nền tảng", "Library ID", "Bắt đầu", "Đang chạy", "Định dạng", "Thông điệp", "CTA", "Link đích"],
              [[ngay, d["ten"], a.get("nen_tang"), a.get("library_id"), a.get("bat_dau"), a.get("dang_chay", True), a.get("dinh_dang"),
                a.get("thong_diep"), a.get("cta"), a.get("link_dich")] for d in q.get("doi_thu") or [] for a in d.get("ads") or []])
    H.ghi_csv(os.path.join(thu_muc, "sheets", "thay-doi.csv"), ["Ngày quét", "So với", "Đối thủ", "Loại", "Chi tiết"],
              [[ngay, (qc or {}).get("ngay_quet"), ten, t["loai"], t["chi_tiet"]] for ten, ds in thay_doi.items() for t in ds])
    shutil.copyfile(os.path.join(thu_muc, "quet.json"), os.path.join(lich_su, f"{ngay}.json"))
    print(f"Đã ghi báo cáo trong {thu_muc}; so với {(qc or {}).get('ngay_quet') or 'không có lần trước'}")
    for ten, ds in thay_doi.items():
        print(f"- {ten}: " + "; ".join(t["loai"] for t in ds))
    return 0


if __name__ == "__main__":
    sys.exit(main())
