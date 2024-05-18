def timUocSoChinh(n):
    """Tìm các ước số chính của số n."""
    uoc_so_chinh = []
    for i in range(1, n):
        if n % i == 0:
            uoc_so_chinh.append(i)
    return uoc_so_chinh

def tongUocSoChinh(n):
    """Tính tổng của các ước số chính của số n."""
    uoc_so_chinh = timUocSoChinh(n)
    tong_uoc_so = sum(uoc_so_chinh)
    return tong_uoc_so

def la_so_amicable(a, b):
    """Kiểm tra xem hai số a và b có phải là cặp số amicable hay không."""
    return tongUocSoChinh(a) == b and tongUocSoChinh(b) == a

def inUocSoChinhVaKiemTraAmicable(a, b):
    """In ra các ước số chính của hai số và kiểm tra xem chúng có phải là cặp số amicable hay không."""
    print(f"Các ước số chính của {a} là: {timUocSoChinh(a)}")
    print(f"Các ước số chính của {b} là: {timUocSoChinh(b)}")
    if la_so_amicable(a, b):
        print(f"{a} và {b} là cặp số amicable.")
    else:
        print(f"{a} và {b} không phải là cặp số amicable.")

a = 300
b = 400
inUocSoChinhVaKiemTraAmicable(a, b)
