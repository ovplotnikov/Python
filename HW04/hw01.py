# Вычислить число π заданным количество знаков после запятой

from math import factorial
from decimal import Decimal, getcontext

getcontext().prec=100

def calc(n):
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)
    k = 0
    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)                                   
    pi = pi * Decimal(12)/Decimal(640320**(1.5))
    pi = 1/pi
    return pi

def main():
    n = int(input("Введите количество знаков после запятой: "))
    print(round(calc(n),n))

main()

