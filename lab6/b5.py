# Nhập dữ liệu từ người dùng
numbers = input("Nhập vào một danh sách các số nguyên, cách nhau bằng dấu cách: ")

# Chuyển đổi chuỗi đầu vào thành một danh sách các số nguyên
numbers = [int(x) for x in numbers.split()]

# Kiểm tra xem danh sách có tạo thành dãy số học không
if len(numbers) < 3:
    print("Danh sách không tạo thành dãy số học.")
else:
    diff = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] - numbers[i-1] != diff:
            print("Danh sách không tạo thành dãy số học.")
            break
    else:
        print("Danh sách tạo thành dãy số học với công sai cố định là", diff)
        print("Danh sách là:", numbers)
