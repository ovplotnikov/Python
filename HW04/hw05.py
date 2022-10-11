# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()


def main():
    a = read_file('hw05a.txt')
    b = read_file('hw05b.txt')
    c = []
    for i in range(len(a)):
        c.append(int(a[i]) + int(b[i]))
    print(c)
    with open('hw05.txt', 'w') as f:
        f.write(str(c))
    f.close()


main()