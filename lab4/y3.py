# Initialize the number and the count of digits
so = int(input("nhập vào một số nguyên: "))
tong = 0
while so != 0:
    digit = so % 10
    tong += 1
    so //= 10
print("số lượng chữ số:  " + str(tong))