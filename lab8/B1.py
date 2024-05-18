def la_so_nguyen_to(n):
    """Kiểm tra một số có phải là số nguyên tố không."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def in_so_nguyen_to_sinh_doi(gioi_han):
    """In ra các cặp số nguyên tố sinh đôi nhỏ hơn giới hạn."""
    for i in range(3, gioi_han - 2, 2):  # Duyệt qua các số lẻ từ 3 đến giới hạn-3
        if la_so_nguyen_to(i) and la_so_nguyen_to(i + 2):
            print(f"({i}, {i + 2})")
in_so_nguyen_to_sinh_doi(1000)
