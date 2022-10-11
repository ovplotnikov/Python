# программу, удаляющую из текста все слова, содержащие ""абв"".


def main():
    a = input("Введите текст: ")
    b = a.split()
    c = []
    for i in b:
        if 'абв' not in i:
            c.append(i)
    print(c)

main()