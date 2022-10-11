# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах input.txt и output.txt.
# Входные данные - произвольная строка, состоящая из символов латинского алфавита.
# Выходные данные - строка, состоящая из пар вида "символ-число", где символ - это символ
# из входной строки, а число - это количество повторений этого символа во входной строке.
# Например, строка "aaabbbcc" должна преобразоваться в строку "a3b3c2".
# При сжатии строки не должно быть пробелов.


def rle_encode(string):
    """Encode string using RLE algorithm."""
    encoded = ""
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            encoded += string[i] + str(count)
            count = 1
    encoded += string[-1] + str(count)
    return encoded


def rle_decode(string):
    """Decode string using RLE algorithm."""
    decoded = ""
    for i in range(0, len(string), 2):
        decoded += string[i] * int(string[i + 1])
    return decoded


def main():
    """Run script."""
    with open("input.txt", "r") as input_file:
        string = input_file.read()
    encoded = rle_encode(string)
    with open("output.txt", "w") as output_file:
        output_file.write(encoded)





main()