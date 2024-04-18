# Nhận đầu vào từ người dùng
numbers = input("Nhập vào một danh sách các số, cách nhau bởi dấu cách: ")
numbers = [float(x) for x in numbers.split()]
gtln = numbers[0]
gtnn = numbers[0]
for num in numbers:

    if num > gtln:
        gtln = num
    
    if num < gtnn:
        gtnn = num
print("Giá trị lớn nhất là:", gtln)
print("Giá trị nhỏ nhất là:", gtnn)
