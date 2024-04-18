
chuoi_van_ban = input("Nhập chuỗi văn bản: ")
tu_can_tim_kiem = input("Nhập từ cần tìm kiếm: ")
vi_tri = chuoi_van_ban.find(tu_can_tim_kiem)
print(f"Vị trí của từ '{tu_can_tim_kiem}' trong chuỗi là: {vi_tri}")
so_lan_xuat_hien = chuoi_van_ban.count(tu_can_tim_kiem)
print(f"Từ '{tu_can_tim_kiem}' xuất hiện {so_lan_xuat_hien} lần trong chuỗi")
tu_nhieu_nhat = max(set(chuoi_van_ban.split()), key=chuoi_van_ban.split().count)
print(f"Từ xuất hiện nhiều nhất trong chuỗi là '{tu_nhieu_nhat}'")
