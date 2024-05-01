#6.1
m, n = map(int, input("Nhập số hàng (m) và số cột (n) của ma trận: ").split())
ma_tran = []

for i in range(m):
    hang = list(map(int, input(f"Nhập các phần tử của hàng {i+1}: ").split()))
    ma_tran.append(hang)
tong = 0
for i in range(m):
    for j in range(n):
        tong += ma_tran[i][j]

print("Tổng của ma trận là:", tong)
p, q = map(int, input("Nhập số hàng (p) và số cột (q) của ma trận thứ hai: ").split())
ma_tran2 = []

for i in range(p):
    hang = list(map(int, input(f"Nhập các phần tử của hàng {i+1}: ").split()))
    ma_tran2.append(hang)

if n != p:
    print("Không thể tính tích của hai ma trận này.")
else:
    ket_qua = [[0] * q for _ in range(m)]
    for i in range(m):
        for j in range(q):
            for k in range(n):
                ket_qua[i][j] += ma_tran[i][k] * ma_tran2[k][j]

    print("Tích của hai ma trận là:")
    for hang in ket_qua:
        print(hang)
chuyen_vi = [[0] * m for _ in range(n)]
for i in range(m):
    for j in range(n):
        chuyen_vi[j][i] = ma_tran[i][j]

print("Ma trận chuyển vị là:")
for hang in chuyen_vi:
    print(hang)
