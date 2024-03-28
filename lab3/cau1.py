while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break
    else:
        print("Số bạn nhập không hợp lệ. Vui lòng nhập lại.")

# Tính tổng a
tong_a = 0
for i in range(1, n + 1):
    tong_a += i

# Tính tổng b
tong_b = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        tong_b += j

# Tính tổng c
tong_c = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        tong_c += j * (i - j + 1)

# Tính tổng d
tong_d = 0
for i in range(1, n + 1):
    temp = 0
    for j in range(1, i + 1):
        temp += j
    if i % 2 == 0:
        tong_d -= temp
    else:
        tong_d += temp

print("a) Số nguyên từ 1 đến n:", tong_a)
print("b) Số tam giác:", tong_b)
print("c) Số hình thang:", tong_c)
print("d) Số hiệp phương trình:", tong_d)
