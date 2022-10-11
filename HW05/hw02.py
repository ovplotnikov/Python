# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота. Бот должен выбирать ход случайным образом.



import random
number_of_candies = int(300)
print ("На столе лежит", number_of_candies, "конфет")
player1 = int(0)
player2 = int(0)
while number_of_candies > 0:
    player1 = int(input("Игрок 1, сколько конфет вы хотите взять? "))
    if player1 > 28:
        print("Вы не можете взять больше 28 конфет за ход")
    elif number_of_candies - player1 < 0:
        print("На столе осталось", number_of_candies, "конфет. Вы не можете взять столько конфет")
        continue
    number_of_candies = number_of_candies - player1
    print ("На столе осталось", number_of_candies, "конфет")
    if number_of_candies <= 0:
        print ("Игрок 1 победил")
        break
    player2 = random.randint(1, 28)
    if number_of_candies < 28:
        player2 = number_of_candies
    print ("Игрок 2 взял", player2, "конфет")
    number_of_candies = number_of_candies - player2
    print ("На столе осталось", number_of_candies, "конфет")
    if number_of_candies <= 0:
        print ("Игрок 2 победил")
        break

