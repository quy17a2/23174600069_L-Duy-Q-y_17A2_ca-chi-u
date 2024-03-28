tong = 0

for num in range(2000, 4001):
    if num % 7 == 0 and num % 5 != 0:
        tong += num

print("Tổng các số chia hết cho 7 nhưng không chia hết cho 5 trong khoảng từ 2000 đến 4000 là:", tong)
