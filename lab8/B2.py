def giai_thua(n):
    """Tính giai thừa của một số n."""
    if n == 0 or n == 1:
        return 1
    ket_qua = 1
    for i in range(2, n + 1):
        ket_qua *= i
    return ket_qua

def hoan_vi(n, r):
    """Tính số hoán vị của n phần tử lấy r phần tử mỗi lần: P(n, r)."""
    return giai_thua(n) // giai_thua(n - r)

def to_hop(n, r):
    """Tính số tổ hợp của n phần tử lấy r phần tử mỗi lần: C(n, r)."""
    return hoan_vi(n, r) // giai_thua(r)
n = 10
r = 5
print(f"Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần là: P({n}, {r}) = {hoan_vi(n, r)}")
print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần là: C({n}, {r}) = {to_hop(n, r)}")
