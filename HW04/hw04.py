# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.



import random
import math
import os
import sys

def main():
    k = int(input("Введите степень многочлена: "))
    a = []
    for i in range(k+1):
        a.append(random.randint(0,100))
    print(a)
    with open('hw04.txt', 'w') as f:
        f.write(str(a))
    f.close()

main()