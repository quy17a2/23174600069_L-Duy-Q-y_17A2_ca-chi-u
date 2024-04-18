
chuoi1 = input("Nhập chuỗi ký tự thứ nhất: ")
chuoi2 = input("Nhập chuỗi ký tự thứ hai: ")
do_dai_chuoi1 = len(chuoi1)
do_dai_chuoi2 = len(chuoi2)
chuoi_ket_qua = ""
do_dai_lon_nhat = max(do_dai_chuoi1, do_dai_chuoi2)
for i in range(do_dai_lon_nhat):
    if i < do_dai_chuoi1:
        chuoi_ket_qua += chuoi1[i]
    if i < do_dai_chuoi2:
        chuoi_ket_qua += "-" + chuoi2[i]
print("Chuỗi kết quả sau khi trộn hai chuỗi là:", chuoi_ket_qua)
