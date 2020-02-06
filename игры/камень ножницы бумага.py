print("Камень ножницы бумага")
from random import *
b = int(input("Введите число от 1 до 3, 1 - камень, 2 - ножницы, 3 - бумага \n"))
a = randint(1,3)
first = 1
second = 2
third = 3
if b == first and a == third:
    print("Бумага")
    print("Вы проиграли!")
elif b == second and a == third:
    print("Бумага")
    print("Вы выйграли!")
elif b == first and a == second:
    print("Ножницы")
    print("Вы выйграли!")
elif b == third and a == second:
    print("Ножницы")
    print("Вы проиграли!")
elif b == second and a ==first:
    print("Камень")
    print("Вы проиграли!")
elif b == third and a == first:
    print("Бумага")
    print("Вы выйграли!")
elif b == first and a == first:
    print("Камень")
    print("Ничья")
elif b == second and a == second:
    print("Ножницы")
    print("Ничья")
else:
    print("Бумага")
    print("Ничья")
