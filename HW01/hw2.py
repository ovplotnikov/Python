""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. """


def main():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(
                    f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} = {not(x or y or z)} = {not(x) and not(y) and not(z)}')


main()
