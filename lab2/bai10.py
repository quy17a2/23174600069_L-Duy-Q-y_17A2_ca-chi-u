
print("Danh sách thể loại phim:")
print("1. Hành động")
print("2. Kinh dị")
print("3. Tình cảm")
print("4. Hài hước")
print("5. Hoạt hình")
lua_chon_the_loai = int(input("Nhập lựa chọn thể loại phim của bạn (1-5): "))
thoi_gian_xem = input("Nhập thời gian muốn xem phim (sáng, trưa, chiều, tối): ")
if lua_chon_the_loai == 1 or lua_chon_the_loai == 4:
    if thoi_gian_xem == "sáng" or thoi_gian_xem == "trưa":
        print("Thời gian chiếu: 8:00 - 11:00")
    elif thoi_gian_xem == "chiều":
        print("Thời gian chiếu: 13:00 - 16:00")
    elif thoi_gian_xem == "tối":
        print("Thời gian chiếu: 19:00 - 22:00")
    else:
        print("Không có suất chiếu")
elif lua_chon_the_loai == 2:
    if thoi_gian_xem == "tối":
        print("Thời gian chiếu: 20:00 - 23:00")
    else:
        print("Không có suất chiếu")
elif lua_chon_the_loai == 3:
    if thoi_gian_xem == "tối":
        print("Thời gian chiếu: 18:00 - 21:00")
    else:
        print("Không có suất chiếu")
elif lua_chon_the_loai == 5:
    if thoi_gian_xem == "sáng" or thoi_gian_xem == "trưa":
        print("Thời gian chiếu: 8:30 - 11:30")
    else:
        print("Không có suất chiếu")
else:
    print("Lựa chọn không hợp lệ")
