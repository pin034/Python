from random import *
q = "Да"
while q == "Да":
   sl = input("Введите сложность. \nЛёгкая. Средняя. Сложная.\n")
   if sl == "Лёгкая":
      a1,a2,hp2 = 15,25,125
   elif sl == "Средняя":
      a1,a2,hp2 = 17,25,150
   else:
      a1,a2,hp2 = 20,30,155
   if sl in "Лёгкая" or sl in "Средняя" or sl in "Сложная":
        hp1,y1,ny = 150,"0",1
        while y1 != "Закончить" and hp2 > 0 and hp1 > 0:
            print("Ваше HP - ", hp1 ,". НР противника - ", hp2)
            if ny%2==1:
               yk2 = randint(0,2)
               y1 = str(input("Сейчас ваш ход. Введите сторону куда хотите ударить.\n"))
               if yk2 == 1:
                   yk2 = "Влево"
               else:
                   yk2 = "Вправо"
               if y1 == yk2:
                  print("Противник укланился",yk2)
                  yr = randint(20,30)
                  hp2-=yr
                  print("Вы попали по противнику, и нанисли ему ",yr)
               elif y1=="Влево" or y1=="Вправо":
                  print("Противник укланился",yk2)
                  print("Противник уклонился, вы не нанесли уме урона.")
               elif y1!="Закончить":
                  print("Вы написали что-то не то.")
               ny+=1
            else:
               yk2 = randint(0,2)
               y1 = str(input("Ход противника. Введите сторону куда хотите увернуться.\n"))
               if yk2 == 1:
                   yk2 = "Влево"
               else:
                   yk2 = "Вправо"
               if y1 == yk2:
                  print("Противник ударил",yk2)
                  yr = randint(a1,a2)
                  hp1-=yr
                  print("Противник попал по вам и нанёс вам",yr)
               elif y1=="Влево" or y1=="Вправо":
                  print("Противник укланился",yk2)
                  print("Вы уклонились, противник не нанесли по вам урона.")
               elif y1!="Закончить":
                  print("Вы написали что-то не то.")
               ny-=1
        if hp2 < 0:
            print("Вы выйграли!")
        else:
            print("ВЫ проиграли.")
   else:
      print("Вы написали что-то не то.")
   q = input("Хотите начать заново? Да или нет\n")
