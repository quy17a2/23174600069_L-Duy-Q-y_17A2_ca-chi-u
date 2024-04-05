#Viết chương trình in ra các số nguyên tố nhỏ hơn 100 
so = 2

while so < 100:
    is_prime = True  

    
    so_chia = 2
    while so_chia <= so ** 0.5:  
        if so % so_chia == 0:
            is_prime = False  
            break
        so_chia += 1
    if is_prime:
        print(so)

    so += 1
#Viết chương trình in ra các số chính phương nhỏ hơn 100 
i = 1
while i * i < 100:
    print(i * i)
    i += 1
#Viết chương trình để in ra tất cả các số Fibonacci nhỏ hơn 1000 
    # Khởi tạo các số Fibonacci ban đầu
fibonacci_1 = 1
fibonacci_2 = 1
print(fibonacci_1)
print(fibonacci_2)
while True:
    fibonacci_tiep = fibonacci_1 + fibonacci_2
    if fibonacci_tiep>= 1000:
        break
    print(fibonacci_tiep)
    fibonacci_1 = fibonacci_2
    fibonacci_2 = fibonacci_tiep

