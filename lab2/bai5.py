
gia_ve_mot_nguoi = 120000
so_luong_nguoi = int(input("Nhập số lượng người: "))
tong_tien = so_luong_nguoi * gia_ve_mot_nguoi
if 2 <= so_luong_nguoi <= 4:
    giam_gia = tong_tien * 0.05
    tong_tien -= giam_gia
print("Tổng số tiền phải trả là:", tong_tien, "đồng")
