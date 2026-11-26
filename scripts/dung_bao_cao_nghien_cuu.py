"""Dựng báo cáo cho các skill nghiên cứu (thương hiệu, review năm, thị trường, dự báo, chiến lược).

Đầu vào: <thu-muc>/ket-qua.json theo references/ket-qua-json.md
Đầu ra:  <thu-muc>/bao-cao.html, <thu-muc>/sheets/<csv>.csv, <thu-muc>/bao-cao.md (chỉ tạo khi chưa có, hoặc --ghi-md)
Kiểm tra: dòng bảng thiếu nguồn/bằng chứng, mục "tin cậy" ngoài Cao/Trung bình/Thấp → in cảnh báo.

Cách chạy: python3 dung_bao_cao_nghien_cuu.py <thu-muc> [--ghi-md]
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import html_chung as H  # noqa: E402

NHAN_LOAI = {
    "thuong-hieu": "Rà soát thương hiệu & phản hồi công khai",
    "review-nam": "Marketing Audit",
    "thi-truong": "Market Research",
    "du-bao": "Dự báo xu hướng tiêu dùng",
    "chien-luoc": "Định hướng chiến lược Marketing",
}
MUC_TOT = {"cao", "đạt", "dữ kiện", "tiếp tục"}
MUC_VUA = {"trung bình", "tín hiệu", "nhận định", "chững lại", "cần bổ sung"}
MUC_XAU = {"thấp", "giả định", "suy giảm", "chưa đủ căn cứ", "chưa đủ cơ sở"}
CSS_THEM = (".tag.tot{border-color:var(--up);color:var(--up)}.tag.xau{border-color:var(--down);color:var(--down)}"
            ".tag.vua{border-color:var(--accent);color:var(--accent)}.callout{background:var(--soft);border-radius:6px;padding:12px 14px;margin:10px 0}")


def o_html(v, nguoc=False):
    if v is None or v == "":
        return '<span class="muted">–</span>'
    if isinstance(v, (int, float)):
        return H.n(v)
    if isinstance(v, list):
        return "<br>".join(o_html(x, nguoc) for x in v)
    s = str(v)
    if s.startswith("http://") or s.startswith("https://"):
        nhan = s.split("//", 1)[1].split("/", 1)[0]
        return f'<a href="{H.e(s)}" target="_blank" rel="noopener">{H.e(nhan)}</a>'
    k = s.strip().lower()
    for tap, lop in ((MUC_TOT, "tot"), (MUC_VUA, "vua"), (MUC_XAU, "xau")):
        if k in tap:
            if nguoc and lop != "vua":
                lop = "xau" if lop == "tot" else "tot"
            return f'<span class="tag {lop}">{H.e(s)}</span>'
    return H.e(s)


def o_text(v):
    if v is None:
        return ""
    if isinstance(v, list):
        return "; ".join(o_text(x) for x in v)
    return str(v)


def kiem_tra(kq):
    canh_bao = []
    for p in kq.get("phan") or []:
        b = p.get("bang")
        if not b:
            continue
        cot = [c.lower() for c in b.get("cot") or []]
        chi_so_nguon = [i for i, c in enumerate(cot) if "nguồn" in c or "bằng chứng" in c or "căn cứ" in c]
        chi_so_tin_cay = [i for i, c in enumerate(cot) if "tin cậy" in c]
        for j, d in enumerate(b.get("dong") or []):
            if len(d) != len(cot):
                canh_bao.append(f'"{p.get("tieu_de")}" dòng {j + 1}: {len(d)} ô nhưng bảng có {len(cot)} cột')
                continue
            if chi_so_nguon and all(not o_text(d[i]).strip() for i in chi_so_nguon):
                canh_bao.append(f'"{p.get("tieu_de")}" dòng {j + 1}: thiếu nguồn/bằng chứng')
            for i in chi_so_tin_cay:
                if o_text(d[i]).strip().lower() not in ("cao", "trung bình", "thấp", ""):
                    canh_bao.append(f'"{p.get("tieu_de")}" dòng {j + 1}: mức tin cậy "{d[i]}" phải là Cao / Trung bình / Thấp')
    return canh_bao


def dung_html(kq):
    loai = kq.get("loai", "")
    phan = []
    if kq.get("tom_tat"):
        phan.append(f'<section><p class="lead">{H.e(kq["tom_tat"])}</p>'
                    + (H.ds(kq.get("diem_chinh")) if kq.get("diem_chinh") else "") + "</section>")
    if kq.get("cau_chot"):
        phan.append(H.section(kq.get("nhan_cau_chot") or "Kết luận", f'<div class="callout lead">{H.e(kq["cau_chot"])}</div>'))
    for p in kq.get("phan") or []:
        nd = "".join(f"<p>{H.e(x)}</p>" for x in p.get("doan") or [])
        b = p.get("bang")
        if b:
            nguoc = ["rủi ro" in str(c).lower() for c in b.get("cot") or []]
            nd += H.bang(b.get("cot") or [], [[o_html(c, nguoc[i] if i < len(nguoc) else False) for i, c in enumerate(d)]
                                              for d in b.get("dong") or []])
        if p.get("ds"):
            nd += H.ds(p["ds"])
        phan.append(H.section(p.get("tieu_de", ""), nd, p.get("ghi_chu")))
    if kq.get("uu_tien"):
        phan.append(H.section(kq.get("nhan_uu_tien") or "Ưu tiên", H.ds(kq["uu_tien"])))
    if kq.get("can_kiem_chung"):
        phan.append(H.section("Điểm cần kiểm chứng", H.ds(kq["can_kiem_chung"])))
    if kq.get("thieu"):
        phan.append(H.section("Thiếu dữ liệu", H.bang(["Mục", "Lý do"], [[H.e(t.get("muc")), H.e(t.get("ly_do"))] for t in kq["thieu"]])))
    if kq.get("nguon"):
        phan.append(H.section("Nguồn", H.bang(["Nguồn", "Đường dẫn", "Ngày"],
                                              [[H.e(x.get("ten")), o_html(x.get("url")), H.e(x.get("ngay"))] for x in kq["nguon"]])))
    doc = H.trang(kq.get("tieu_de", "Báo cáo"), NHAN_LOAI.get(loai, "Agent Masterplan"), kq.get("tieu_de", ""),
                  " · ".join(x for x in [kq.get("doanh_nghiep"), kq.get("pham_vi"), f'lập ngày {kq["ngay"]}' if kq.get("ngay") else ""] if x),
                  phan)
    return doc.replace("</style>", CSS_THEM + "</style>", 1)


def dung_md(kq):
    out = [f'# {kq.get("tieu_de", "Báo cáo")}', ""]
    phu = " · ".join(x for x in [kq.get("doanh_nghiep"), kq.get("pham_vi"), f'lập ngày {kq["ngay"]}' if kq.get("ngay") else ""] if x)
    if phu:
        out += [phu, ""]
    if kq.get("tom_tat"):
        out += ["## Tóm tắt", kq["tom_tat"], ""] + [f"{i}. {x}" for i, x in enumerate(kq.get("diem_chinh") or [], 1)] + [""]
    if kq.get("cau_chot"):
        out += [f'## {kq.get("nhan_cau_chot") or "Kết luận"}', f'> {kq["cau_chot"]}', ""]
    for p in kq.get("phan") or []:
        out += [f'## {p.get("tieu_de", "")}']
        if p.get("ghi_chu"):
            out += [f'_{p["ghi_chu"]}_']
        out += [""] + [x + "\n" for x in p.get("doan") or []]
        b = p.get("bang")
        if b:
            out.append("| " + " | ".join(b.get("cot") or []) + " |")
            out.append("|" + " --- |" * len(b.get("cot") or []))
            for d in b.get("dong") or []:
                out.append("| " + " | ".join(o_text(c).replace("|", "/").replace("\n", " ") for c in d) + " |")
            out.append("")
        out += [f"{i}. {x}" for i, x in enumerate(p.get("ds") or [], 1)] + ([""] if p.get("ds") else [])
    if kq.get("uu_tien"):
        out += [f'## {kq.get("nhan_uu_tien") or "Ưu tiên"}'] + [f"{i}. {x}" for i, x in enumerate(kq["uu_tien"], 1)] + [""]
    if kq.get("can_kiem_chung"):
        out += ["## Điểm cần kiểm chứng"] + [f"- {x}" for x in kq["can_kiem_chung"]] + [""]
    if kq.get("thieu"):
        out += ["## Thiếu dữ liệu"] + [f'- {t.get("muc")}: {t.get("ly_do")}' for t in kq["thieu"]] + [""]
    if kq.get("nguon"):
        out += ["## Nguồn"] + [f'- {x.get("ten")}' + (f' — {x["url"]}' if x.get("url") else "") + (f' ({x["ngay"]})' if x.get("ngay") else "")
                              for x in kq["nguon"]] + [""]
    return "\n".join(out)


def ghi_sheets(thu_muc, kq):
    ds_file = []
    for p in kq.get("phan") or []:
        b = p.get("bang")
        if not b or not p.get("csv"):
            continue
        duong = os.path.join(thu_muc, "sheets", f'{p["csv"]}.csv')
        H.ghi_csv(duong, ["Ngày lập", "Phạm vi"] + list(b.get("cot") or []) + ["Duyệt"],
                  [[kq.get("ngay", ""), kq.get("pham_vi", "")] + [o_text(c) for c in d] + ["Chờ duyệt"] for d in b.get("dong") or []])
        ds_file.append((duong, p.get("tab_sheets") or p["csv"]))
    return ds_file


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    thu_muc = sys.argv[1]
    with open(os.path.join(thu_muc, "ket-qua.json"), encoding="utf-8") as f:
        kq = json.load(f)
    with open(os.path.join(thu_muc, "bao-cao.html"), "w", encoding="utf-8") as f:
        f.write(dung_html(kq))
    md = os.path.join(thu_muc, "bao-cao.md")
    if "--ghi-md" in sys.argv or not os.path.exists(md):
        with open(md, "w", encoding="utf-8") as f:
            f.write(dung_md(kq))
        print("Đã ghi bao-cao.md")
    for duong, tab in ghi_sheets(thu_muc, kq):
        print(f"CSV {os.path.relpath(duong, thu_muc)} → tab Sheets \"{tab}\"")
    cb = kiem_tra(kq)
    for c in cb:
        print("CẢNH BÁO:", c)
    print("Đã ghi bao-cao.html" + (f" · {len(cb)} cảnh báo cần sửa trong ket-qua.json" if cb else " · không có cảnh báo"))


if __name__ == "__main__":
    main()
