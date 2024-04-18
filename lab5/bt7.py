x = input("Nhập chuỗi cần đếm: ")

so_chu_thuong = 0
so_chu_hoa = 0
so_chu_so = 0
so_ky_tu_dac_biet = 0

for char in x:
    if 'a' <= char <= 'z':
        so_chu_thuong += 1
    elif 'A' <= char <= 'Z':
        so_chu_hoa += 1
    elif '0' <= char <= '9':
        so_chu_so += 1
    else:
        so_ky_tu_dac_biet += 1

print("Số lượng chữ thường:", so_chu_thuong)
print("Số lượng chữ hoa:", so_chu_hoa)
print("Số lượng chữ số:", so_chu_so)
print("Số lượng ký tự đặc biệt:", so_ky_tu_dac_biet)
