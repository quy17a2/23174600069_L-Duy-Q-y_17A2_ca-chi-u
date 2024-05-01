kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Tính tổng số tiền cho từng loại hoa quả
hoa_don = {}

for mat_hang in kho:
    so_luong = kho[mat_hang]
    don_gia = gia_tien[mat_hang]
    tong_tien = so_luong * don_gia
    hoa_don[mat_hang] = {
        "so_luong": so_luong,
        "don_gia": don_gia,
        "tong_tien": tong_tien
    }

# In ra hóa đơn
print("Hóa đơn mua hàng:")
for mat_hang, thong_tin in hoa_don.items():
    print(f"Mặt hàng: {mat_hang}, Số lượng: {thong_tin['so_luong']}, Đơn giá: {thong_tin['don_gia']}, Tổng tiền: {thong_tin['tong_tien']}")

# Tính tổng số tiền cần thanh toán
tong_tien_can_thanh_toan = sum(thong_tin['tong_tien'] for thong_tin in hoa_don.values())
print(f"Tổng tiền cần thanh toán: {tong_tien_can_thanh_toan}")
