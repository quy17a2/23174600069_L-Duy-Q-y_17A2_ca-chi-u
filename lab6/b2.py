
n = int(input("Nhập vào số phần tử của mảng: "))
arr = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(so)
print("Các số nguyên tố trong mảng là:")
for so in arr:
    la_so_nguyen_to = True
    if so <= 1:
        la_so_nguyen_to = False
    else:
        for i in range(2, int(so**0.5) + 1):
            if so % i == 0:
                la_so_nguyen_to = False
                break
    if la_so_nguyen_to:
        print(so)

print("Các số hoàn hảo trong mảng là:")
for so in arr:
    la_so_hoan_hao = False
    if so > 1:
        tong_uoc = 1
        for i in range(2, int(so**0.5) + 1):
            if so % i == 0:
                tong_uoc += i
                if i != so // i:
                    tong_uoc += so // i
        if tong_uoc == so:
            la_so_hoan_hao = True
    if la_so_hoan_hao:
        print(so)
