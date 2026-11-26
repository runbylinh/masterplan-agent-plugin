"""Xuất kết quả ra file .xlsx đúng khuôn Bộ mẫu Marketing Masterplan (templates/bo-mau/bo-mau.json).

Cách chạy:
  python3 xuat_bo_mau.py --liet-ke
  python3 xuat_bo_mau.py <mau> --nam 2026 [--nam-ke-hoach 2027] [--doanh-nghiep "Tên"] [--ket-qua a/ket-qua.json b/ket-qua.json] [-o file.xlsx] [--day-du]

<mau>: danh-gia-hien-trang | nghien-cuu-thi-truong | du-bao-dinh-huong | ke-hoach-tong-the
Không truyền --ket-qua: ra mẫu trống đúng khuôn.
Mỗi phần trong ket-qua.json muốn điền vào mẫu cần khoá "muc_mau": "<Tên tab>/<Tên mục>" (mục không tên: chỉ "<Tên tab>").
Cột khớp theo TÊN cột trong mẫu; cột thừa bị bỏ qua (có cảnh báo). Mục có dòng cố định: khớp theo giá trị cột đầu.
--day-du: thêm cả tab phụ (ví dụ "Kiểm tra tín hiệu") khi chưa có dữ liệu.
"""
import argparse
import json
import os
import sys

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
except ImportError:
    sys.exit("Cần openpyxl: python3 -m pip install openpyxl")

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_MAU = os.path.join(GOC, "templates", "bo-mau", "bo-mau.json")
NHAN = "6864AE"
FILL_TIEU_DE = PatternFill("solid", fgColor="EEEDF7")
FILL_COT = PatternFill("solid", fgColor="F3F3F5")


def chuan(s):
    return " ".join(str(s or "").strip().lower().split())


def thay(s, bien):
    if s is None:
        return None
    for k, v in bien.items():
        s = s.replace("{" + k + "}", str(v))
    return s


def o_text(v):
    if v is None:
        return ""
    if isinstance(v, list):
        return "; ".join(o_text(x) for x in v)
    return v


def doc_du_lieu(ds_file, bien):
    """→ {khoá mục chuẩn hoá: [(cot, dong)]}, nguon_mo_ta"""
    kho, mo_ta = {}, []
    for f in ds_file or []:
        with open(f, encoding="utf-8") as fh:
            kq = json.load(fh)
        mo_ta.append(kq.get("tieu_de") or os.path.basename(os.path.dirname(f)))
        for p in kq.get("phan") or []:
            if not p.get("muc_mau") or not p.get("bang"):
                continue
            kho.setdefault(chuan(thay(p["muc_mau"], bien)), []).append((p["bang"].get("cot") or [], p["bang"].get("dong") or []))
    return kho, mo_ta


def ghi_muc(ws, r, muc, du_lieu, bien, canh_bao, ten_tab):
    cot = muc["cot"]
    ten = thay(muc.get("ten"), bien)
    if ten:
        ws.cell(r, 1, ten).font = Font(bold=True, color=NHAN, size=12)
        for c in range(1, len(cot) + 1):
            ws.cell(r, c).fill = FILL_TIEU_DE
        r += 1
    for i, t in enumerate(cot, 1):
        o = ws.cell(r, i, t)
        o.font = Font(bold=True)
        o.fill = FILL_COT
        o.alignment = Alignment(wrap_text=True, vertical="top")
    r += 1
    # gom dòng dữ liệu theo tên cột mẫu
    dong_dl = []
    ten_cot = [chuan(c) for c in cot]
    for cot_dl, ds in du_lieu:
        cdl = [chuan(c) for c in cot_dl]
        thua = [cot_dl[i] for i, c in enumerate(cdl) if c not in ten_cot]
        if thua:
            canh_bao.append(f"{ten_tab}/{ten or '-'}: cột chỉ có trong báo cáo, không đưa vào mẫu: {', '.join(thua)}")
        for d in ds:
            m = {cdl[i]: o_text(v) for i, v in enumerate(d) if i < len(cdl)}
            dong_dl.append([m.get(c, "") for c in ten_cot])
    co_dinh = [thay(x, bien) for x in muc.get("dong_co_dinh") or []]
    gia_tri = muc.get("gia_tri_co_dinh") or []
    hang = []
    if co_dinh:
        con_lai = list(dong_dl)
        for j, nhan in enumerate(co_dinh):
            khop = next((d for d in con_lai if chuan(d[0]) == chuan(nhan)), None)
            if khop:
                con_lai.remove(khop)
                hang.append([nhan] + khop[1:])
            else:
                gt = [thay(x, bien) for x in (gia_tri[j] if j < len(gia_tri) else [])]
                hang.append([nhan] + gt + [""] * (len(cot) - 1 - len(gt)))
        hang += con_lai
        hang += [[""] * len(cot) for _ in range(muc.get("dong_trong", 0))] if not dong_dl else []
    else:
        hang = dong_dl + [[""] * len(cot) for _ in range(max(muc.get("dong_trong", 3) - len(dong_dl), 2 if dong_dl else 0))]
    for d in hang:
        for i, v in enumerate(d, 1):
            o = ws.cell(r, i, v if v != "" else None)
            o.alignment = Alignment(wrap_text=True, vertical="top")
            if "(đồng)" in cot[i - 1]:
                o.number_format = "#,##0"
        r += 1
    return r + 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mau", nargs="?")
    ap.add_argument("--liet-ke", action="store_true")
    ap.add_argument("--nam", type=int)
    ap.add_argument("--nam-ke-hoach", type=int)
    ap.add_argument("--doanh-nghiep", default="")
    ap.add_argument("--ket-qua", nargs="*")
    ap.add_argument("-o", "--ra")
    ap.add_argument("--day-du", action="store_true")
    a = ap.parse_args()
    with open(FILE_MAU, encoding="utf-8") as f:
        bo = json.load(f)["files"]
    if a.liet_ke or not a.mau:
        for k, v in bo.items():
            print(f'{k:24s} {v["ten_file"]}  · tab: {", ".join(t["ten"] for t in v["tabs"])}  · skill: {", ".join(v["skill"]) or "(sau)"}')
        return
    if a.mau not in bo:
        sys.exit(f"Không có mẫu '{a.mau}'. Dùng --liet-ke.")
    if not a.nam:
        sys.exit("Cần --nam (năm review).")
    bien = {"nam": a.nam, "nam_ke_hoach": a.nam_ke_hoach or a.nam + 1}
    mau = bo[a.mau]
    kho, mo_ta = doc_du_lieu(a.ket_qua, bien)
    canh_bao, da_dung = [], set()
    wb = Workbook()
    wb.remove(wb.active)
    for tab in mau["tabs"]:
        khoa_tab = [chuan(tab["ten"] + ("/" + thay(m["ten"], bien) if m.get("ten") else "")) for m in tab["muc"]]
        if tab.get("phu") and not a.day_du and not any(k in kho for k in khoa_tab):
            continue
        ws = wb.create_sheet(tab["ten"][:31])
        so_cot = max(len(m["cot"]) for m in tab["muc"])
        ws.cell(1, 1, thay(tab["tieu_de"], bien)).font = Font(bold=True, size=15, color=NHAN)
        phu = " · ".join(x for x in [a.doanh_nghiep, "; ".join(mo_ta) if mo_ta else "mẫu trống",
                                      "Agent Masterplan điền, trạng thái: Chờ duyệt" if mo_ta else ""] if x)
        ws.cell(2, 1, phu).font = Font(italic=True, color="6B6B70")
        r = 4
        for m, k in zip(tab["muc"], khoa_tab):
            da_dung.add(k)
            r = ghi_muc(ws, r, m, kho.get(k, []), bien, canh_bao, tab["ten"])
        for c in range(1, so_cot + 1):
            ws.column_dimensions[get_column_letter(c)].width = 30
        ws.freeze_panes = "A4"
    for k in kho:
        if k not in da_dung:
            canh_bao.append(f'muc_mau "{k}" không khớp mục nào trong mẫu {a.mau}')
    ra = a.ra or (thay(mau["ten_file"], bien).replace("Mẫu ", "", 1) + (f" — {a.doanh_nghiep}" if a.doanh_nghiep else "") + ".xlsx")
    wb.save(ra)
    for c in canh_bao:
        print("CẢNH BÁO:", c)
    print(f"Đã ghi {ra}")


if __name__ == "__main__":
    main()
