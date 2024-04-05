even_numbers = []
odd_numbers = []
count = 0

while True:
    try:
        n = int(input('Nhập một số nguyên dương: '))
        if n <= 0:
            print('Vui lòng nhập một số nguyên dương.')
            continue
    except ValueError:
        print('Vui lòng nhập một số hợp lệ.')
        continue

    count += 1
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)

    if sum(even_numbers) + sum(odd_numbers) > 1000:
        break

print(f'a) Các số lẻ đã nhập: {odd_numbers}')
print(f'b) Các số chẵn đã nhập: {even_numbers}')
print(f'c) Tổng số đã nhập: {count}')
