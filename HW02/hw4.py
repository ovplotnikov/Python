""" Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число. """

import random


def main():
    N = 10
    result = 1
    list = [random.randint(-N, N) for i in range(N)]
    print(list)
    with open('file.txt', 'r') as f:
        for line in f:
            for i in line.split():
                result = result * list[int(i)]
    print("Произведение элементов на указанных позициях: ", result)


main()
