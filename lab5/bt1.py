
so_thap_phan = int(input("Nhập số nguyên dương (số thập phân): "))
so_nhi_phan = ""
while so_thap_phan > 0:
    du = so_thap_phan % 2
    so_nhi_phan = str(du) + so_nhi_phan
    so_thap_phan = so_thap_phan // 2
print("Số nhị phân tương ứng là:", so_nhi_phan)


