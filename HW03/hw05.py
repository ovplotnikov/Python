# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def main():
    n = int(input("Введите число N: "))
    fib_negative_numbers = [fib(i) for i in range(n+1)]
    for i in range(len(fib_negative_numbers)):
        if i%2 == 0:
            fib_negative_numbers[i] = -fib_negative_numbers[i]
        
    fib_numbers = [fib(i) for i in range(n+1)]
    fib_negative_numbers.reverse ()
    fib_negative_numbers.remove(0)
    nega_fib = [*fib_negative_numbers, *fib_numbers]
    print('Числа негафибоначчи: ', nega_fib)



main()