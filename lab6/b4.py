#a) Dãy Fibonacci

n = int(input("Nhập số lượng số Fibonacci cần tạo: "))
fibonacci_list = [0, 1] if n >= 2 else [0] if n == 1 else []
for i in range(2, n):
    fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
print("Danh sách Fibonacci gồm", n, "số đầu tiên là:")
print(fibonacci_list)
#dãy số nguyên tố
so_nguyen_to = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
print("Danh sách các số nguyên tố nhỏ hơn 100 là:")
print(so_nguyen_to)

