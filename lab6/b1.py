
n = int(input("Nhập vào số phần tử của mảng: "))
arr = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(so)
tong_chan = 0
tong_le = 0
for so in arr:
    if so % 2 == 0:
        tong_chan += so
    else:
        tong_le += so
print("Tổng các số chẵn trong mảng là:", tong_chan)
print("Tổng các số lẻ trong mảng là:", tong_le)
