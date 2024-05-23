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


n = 100
print(f"Các ước số chính của {n} là: {timUocSoChinh(n)}")
print(f"Tổng các ước số chính của {n} là: {tongUocSoChinh(n)}")
