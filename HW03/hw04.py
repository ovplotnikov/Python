# Напишите программу, которая будет преобразовывать десятичное число в двоичное

def dec2bin(dec):
    bin = ""
    while dec > 0:
        bin = str(dec % 2) + bin
        dec = dec // 2
    return bin

def main():
    print ('Введите десятичное число')
    dec = int(input())
    print('Число в двоичном формате:', dec2bin(dec))


main()