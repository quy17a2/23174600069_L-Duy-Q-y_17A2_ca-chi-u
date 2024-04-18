
n = input("Nhập chuỗi có độ dài hơn 10 ký tự: ")
if len(n) > 10:
    substring = n[1:8]
    print("Chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8:", substring)
else:
    print("Chuỗi không có độ dài hơn 10 ký tự.")



input_string = input("Nhập chuỗi có độ dài hơn 10 ký tự: ")


if len(input_string) > 10:
    # b) Trích ra chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5
    sub_string_b = input_string[4:9]
    print("b) Chuỗi ký tự con từ vị trí thứ 5 gồm 5 ký tự:", sub_string_b)

    # c) Trích ra chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự
    sub_string_c = input_string[-3:]
    print("c) Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:", sub_string_c)

    # d) Chuyển đổi các ký tự trong chuỗi thành chữ thường
    lowercase_string = input_string.lower()
    print("d) Chuỗi chữ thường:", lowercase_string)

    # e) Chuyển đổi các ký tự trong chuỗi thành chữ hoa
    uppercase_string = input_string.upper()
    print("e) Chuỗi chữ hoa:", uppercase_string)

    # f) Đảo ngược chuỗi ký tự
    reversed_string = input_string[::-1]
    print("f) Chuỗi ký tự đảo ngược:", reversed_string)
else:
    print("Chuỗi không có độ dài hơn 10 ký tự.")
