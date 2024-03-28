#a) In ra các số nguyên tố từ 100 đến 1000 (kể cả số 1000)
print("Các số nguyên tố từ 100 đến 1000 là:")
for so in range(100, 1001):
    if so > 1:  # Kiểm tra số nguyên tố phải lớn hơn 1
        is_prime = True
        for i in range(2, int(so ** 0.5) + 1):
            if so % i == 0:
                is_prime = False
                break
        if is_prime:
            print(so, end=", ")
#b) In ra các số chính phương từ 1 đến 1000 (kể cả số 1000)
print("Các số chính phương từ 1 đến 1000 là:")
for so in range(1, 1001):
    can_bac_hai = int(so ** 0.5)  
    if can_bac_hai * can_bac_hai == so:  
        print(so, end=", ")
#c) In ra chuỗi Fibonacci sao cho số cuối cùng trong chuỗi nhỏ hơn 100
a, b = 0, 1
print("Chuỗi Fibonacci sao cho số cuối cùng nhỏ hơn 100 là:")
print(a, end=", ")
while b < 100:
    print(b, end=", ")
    a, b = b, a + b
#d)In ra các số hoàn hảo bé hơn 500
print("Các số hoàn hảo bé hơn 500 là:")
for so in range(2, 500):
    tong_uoc = 0
    for i in range(1, so):
        if so % i == 0:
            tong_uoc += i
    if tong_uoc == so:
        print(so, end=", ")
#e) In ra tổng của các số ngũ giác trong đoạn từ 1 đến 200 (kể cả số 200)
tong = 0
for n in range(1, 201):
    so_ngu_giac = n * (3 * n - 1) // 2
    tong += so_ngu_giac

print("Tổng của các số ngũ giác trong đoạn từ 1 đến 200 là:", tong)
