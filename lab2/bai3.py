
so_nguyen = int(input("Nhập một số nguyên có ba chữ số: "))
so_hang_tram = so_nguyen // 100
so_hang_chuc = (so_nguyen // 10) % 10
so_hang_don_vi = so_nguyen % 10
doc_so_0_den_19 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                   "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

doc_hang_chuc = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
if so_hang_tram != 0:
    print(doc_so_0_den_19[so_hang_tram], "hundred", end=" ")

if so_hang_chuc == 1:
    print(doc_so_0_den_19[so_nguyen % 100], end=" ")
else:
    print(doc_hang_chuc[so_hang_chuc], end=" ")
if so_hang_chuc != 1:
    print(doc_so_0_den_19[so_hang_don_vi])
