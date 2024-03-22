
a1 = float(input("Nhập hệ số góc của đường thẳng thứ nhất: "))
b1 = float(input("Nhập hệ số tự do của đường thẳng thứ nhất: "))
a2 = float(input("Nhập hệ số góc của đường thẳng thứ hai: "))
b2 = float(input("Nhập hệ số tự do của đường thẳng thứ hai: "))
if a1 == a2:
    print("Hai đường thẳng là song song")
elif a1 * a2 == -1:
    print("Hai đường thẳng là vuông góc")
else:
    print("Hai đường thẳng cắt nhau")
