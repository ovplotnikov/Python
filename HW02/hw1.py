""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. """

def float_transform(number):
    number = float(input('Введите вещественное число: '))
    number = abs(number)
    if number >= 1:
        number = int(number)
    else:
        number = str(number)
        number = number.replace('.', '')
        number = int(number)
    return number


def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    print('Сумма цифр =', sum)


sum_of_digits(float_transform(0))


