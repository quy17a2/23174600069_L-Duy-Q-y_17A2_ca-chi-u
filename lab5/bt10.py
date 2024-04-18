
chuoi = input("Nhập chuỗi: ")
result_string = ""
for char in chuoi:
    if char != ' ':
        result_string += char
print("Chuỗi sau khi loại bỏ khoảng trắng:", result_string)
