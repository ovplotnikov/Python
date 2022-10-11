# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


import math
def prime_factors(num):
    while num % 2 == 0:
        print(2,)
        num = num / 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            print(i,)
            
            num = num / i
    if num > 2:
        print(num)


        
    

def main():
    num = int(input("Введите натуральное число: "))
    print ('Простые множители числа', num, ':')
    prime_factors(num)

main()