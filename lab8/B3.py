def cubesum(n):
    """Trả về tổng các lập phương của các chữ số riêng lẻ của số n."""
    sum_cubes = 0
    while n > 0:
        digit = n % 10
        sum_cubes += digit ** 3
        n //= 10
    return sum_cubes

def isArmstrong(n):
    """Kiểm tra xem một số n có phải là số Armstrong hay không."""
    return n == cubesum(n)

def PrintArmstrong():
    """In ra tất cả các số Armstrong từ 1 đến 999."""
    for i in range(1, 1000):
        if isArmstrong(i):
            print(i)
print("Các số Armstrong từ 1 đến 999 là:")
PrintArmstrong()
n = 153
if isArmstrong(n):
    print(f"{n} là số Armstrong.")
else:
    print(f"{n} không phải là số Armstrong.")
