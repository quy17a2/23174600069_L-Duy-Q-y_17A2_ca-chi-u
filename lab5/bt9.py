# Nhập hai chuỗi từ người dùng
a1 = input("Nhập chuỗi thứ nhất: ")
a2 = input("Nhập chuỗi thứ hai: ")

# Kiểm tra xem độ dài của hai chuỗi có giống nhau không
if len(a1) == len(a2):
    differences = 0
    # Duyệt qua từng ký tự trong hai chuỗi và kiểm tra xem chúng có khác nhau không
    for i in range(len(a1)):
        if a1[i] != a2[i]:
            differences += 1

    if differences <= 2:
        print("Có thể thay đổi từ chuỗi thứ nhất thành chuỗi thứ hai.")
    else:
        print("Không thể thay đổi từ chuỗi thứ nhất thành chuỗi thứ hai.")
else:
    print("Không thể thay đổi từ chuỗi thứ nhất thành chuỗi thứ hai vì độ dài của hai chuỗi không giống nhau.")
