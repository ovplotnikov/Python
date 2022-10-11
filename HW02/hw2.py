""" Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. """

import math


number = int(input('Введите целое положительное число: '))
list_number = list(range(1, number + 1))
""" print(list_number) """

result_list = list()
for i in list_number:
    result_list.append(math.factorial(i))


print(f'Результат: {result_list}')
