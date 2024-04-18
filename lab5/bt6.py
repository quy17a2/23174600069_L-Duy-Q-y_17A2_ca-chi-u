
chuoi = input("Nhập chuỗi văn bản: ")
ky_tu_dac_biet = {}
for ky_tu in chuoi:
    if not ky_tu.isalnum():
        if ky_tu in ky_tu_dac_biet:
            ky_tu_dac_biet[ky_tu] += 1
        else:
            ky_tu_dac_biet[ky_tu] = 1
tong_so_ky_tu = len(chuoi)
for ky_tu, so_lan_xuat_hien in ky_tu_dac_biet.items():
    print(f"Ký tự '{ky_tu}' xuất hiện {so_lan_xuat_hien} lần trong chuỗi, tương ứng với {so_lan_xuat_hien/tong_so_ky_tu*100:.2f}%")
