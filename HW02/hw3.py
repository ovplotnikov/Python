""" Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму. """

import math
n = int(input('Введите целое положительное число: '))

list_number = list(range(1, n + 1))
for i in list_number:
    list_number[i - 1] = (1 + 1 / i) ** i

print(f'Результат: {list_number}')

result = sum(list_number)

print(f'Сумма: {result}')