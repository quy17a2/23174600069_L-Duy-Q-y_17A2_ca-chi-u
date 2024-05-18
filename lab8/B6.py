#1
def laSoLe(x):
    return x % 2 != 0
danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ket_qua = list(filter(laSoLe, danh_sach))
print("Các số lẻ trong danh sách là:", ket_qua)
#2
def loc_cac_so_chan(numbers):
    return filter(lambda x: x % 2 == 0, numbers)
so_nguyen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cac_so_chan = list(loc_cac_so_chan(so_nguyen))
print(cac_so_chan)
#3
def cube(x):
    return x**3

numbers = [1, 2, 3, 4, 5]
cubes = list(map(cube, numbers))
print(cubes)
#4
def cube(x):
    return x**3

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
cubes = list(map(cube, even_numbers))
print(cubes)
#5
def binh_phuong(x):
    return x**2

so_nguyen = [1, 2, 3, 4, 5]
so_le = filter(lambda x: x % 2 != 0, so_nguyen)
binh_phuong_cua_so_le = list(map(binh_phuong, so_le))
print(binh_phuong_cua_so_le)
