from random import *
i = "да"
while i == "да":
   y = 1000
   print ("Ваш баланс - ", y)
   while y > 0:
      a,d = map(int,input("Выберите ставку и число на которое ставите, от 0 до 99. Забрать выйгрыш - 0 100.\n").split(" "))
      chi = randint(0,99)
      if a > y or a < 0:
          print("Неподходящая ставка.")
      elif a == 0 and d == 100:
         y = 0
      else:
         if chi <= 5:
            print("Выпало зелёное.", chi)
         elif chi % 2 == 0:
            print("Выпало чёрное.", chi)
         else:
            print("Выпало красное.", chi)
         if chi == d:
            y = y + (a * 4)
            print("Ваша ставка умножена в 5 раз! Теперь у вас:", y)
         elif 6 > chi and 6 > d:
            y = y + (a * 3)
            print("Ваша ставка умножена в 4 раза! Теперь у вас:", y)
         elif d % 2 == chi % 2 and d > 5:
            y = y + a
            print("Ваша ставка умножена в 2 раза! Теперь у вас:", y)
         else:
            y = y - a
            print("Вы проиграли, теперь у вас:", y)
         print("================================================================================")
   i = input("Хотите начать заново? \n")
   print("================================================================================")
print("Спасибо за игру, досвидание.")
