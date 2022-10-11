# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def main():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    reverse_list1 = list(reversed(list1))
    len_list1 = int((len(list1))/2)
    print(len_list1)
    list3 = list1[:len_list1]
    for i in range(len(list3)):
        list3[i] = list1[i] * reverse_list1[i]
    print('list1:', list1)
    print('list3:', list3)


main()