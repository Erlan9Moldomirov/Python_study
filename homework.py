# Problem 

# num1 = 17391
# num2 = 546
# num3 = 934
# a = num1 % 17
# b = num2 % 17
# c = num3 % 17
# print(a, b, c)
# if a < b < c:
#     print(f"Остаток числа {num1} меньше остатка числа {num2}, который меньше остатка числа {num3}")
# elif a > b > c:
#     print(f"Остаток числа {num1} больше остатка числа {num2}, который больше остатка числа {num3}")
# elif a == b == c:
#     print(f"Остаток всех трех чисел равен")

# *****

# Problem 16

# x = 13

# if x ** 2 > 172:
#     print(f"Квадрат числа {x} равен {x ** 2}, что больше числа 172")

# elif x ** 2 < 172:
#     print(f"Квадрат числа {x} равен {x ** 2}, что меньше числа 172")
#     print(x ** 2 ** 2)

# ******

# Problem 14

# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# c = int(input("Введите число: "))

# if a < b < c:
#     print(f"Самое большее число {c}, а самое меньшее число {a}")
# elif a > b > c:
#     print(f"Самое большее число {a}, а самое меньшее число {c}")
# elif a < b > c and a < c:
#     print(f"Самое большее число {b}, а самое меньшее число {a}")
# elif a < b > c and a > c:
#     print(f"Самое большее число {b}, а самое меньшее число {c}")
# elif a > b < c and a < c:
#     print(f"Самое большее число {c}, а самое меньшее число {b}")
# elif a > b < c and a > c:
#     print(f"Самое большее число {a}, а самое меньшее число {b}")
# elif a == b == c:
#     print(f"Все числа равны")
# elif a == b > c:
#     print(f"y")
# elif a == b < c:
#     print(f"u")
# elif a == c > b:
#     print(f"i")
# else:
#     print(f"o")

# *****

# Problem 

# num = int(input("Введите число: "))
# if num < 0:
#     print("Вы ввели отрицательное число")
# else:
#     print("Ошибка! Вы ввели неправильное число!")

# *****

# "Знаки зодиака"

# d = int(input("Введите день вашего рождения: "))
# m = int(input("Введите месяц вашего рождения: "))
# year = int(input("Введите год вашего рождения: "))

# if (d >= 21 and d <= 30 and m == 3) or (m == 4 and d >= 1 and d <= 20):
#     print("Ваш знак зодиака - Овен")
# elif (d >= 21 and d<= 31 and m == 4) or (m == 5 and d >= 1 and d <= 21):
#     print("Ваш знак зодиака - Телец")
# elif (d >= 22 and d<= 30 and m == 5) or (m == 6 and d >= 1 and d <= 21):
#     print("Ваш знак зодиака - Близнецы")
# elif (d >= 22 and d<= 30 and m == 6) or (m == 7 and d >= 1 and d <= 22):
#     print("Ваш знак зодиака - Рак")
# elif (d >= 23 and d<= 31 and m == 7) or (m == 8 and d >= 1 and d <= 21):
#     print("Ваш знак зодиака - Лев")
# elif (d >= 22 and d<= 31 and m == 8) or (m == 9 and d >= 1 and d <= 23):
#     print("Ваш знак зодиака - Дева")
# elif (d >= 24 and d<= 30 and m == 9) or (m == 10 and d >= 1 and d <= 23):
#     print("Ваш знак зодиака - Весы")
# elif (d >= 24 and d<= 31 and m ==10) or (m == 11 and d >= 1 and d <= 22):
#     print("Ваш знак зодиака - Скорпион")
# elif (d >= 23 and d<= 30 and m == 11) or (m == 12 and d >= 1 and d <= 22):
#     print("Ваш знак зодиака - Стрелец")
# elif (d >= 23 and d<= 31 and m == 12) or (m == 1 and d >= 1 and d <= 20):
#     print("Ваш знак зодиака - Козерог")
# elif (d >= 21 and d<= 31 and m == 1) or (m == 2 and d >= 1 and d <= 19):
#     print("Ваш знак зодиака - Водолей")
# elif (d >= 20 and d<= 28 and m == 2) or (m == 3 and d >= 1 and d <= 20):
#     print("Ваш знак зодиака - Рыбы")

# if (year - 2000) % 12 == 0:
#     print("Ваш лунный знак зодиака - Дракон")
# elif (year - 2000) % 12 == 1:
#     print("Ваш лунный знак зодиака - Змея")
# elif (year - 2000) % 12 == 2:
#     print("Ваш лунный знак зодиака - Лошадь")
# elif (year - 2000) % 12 == 3:
#     print("Ваш лунный знак зодиака - Овца")
# elif (year - 2000) % 12 == 4:
#     print("Ваш лунный знак зодиака - Обезьяна")
# elif (year - 2000) % 12 == 5:
#     print("Ваш лунный знак зодиака - Петух")
# elif (year - 2000) % 12 == 6:
#     print("Ваш лунный знак зодиака - Собака")
# elif (year - 2000) % 12 == 7:
#     print("Ваш лунный знак зодиака - Свинья")
# elif (year - 2000) % 12 == 8:
#     print("Ваш лунный знак зодиака - Крыса")
# elif (year - 2000) % 12 == 9:
#     print("Ваш лунный знак зодиака - Бык")
# elif (year - 2000) % 12 == 10:
#     print("Ваш лунный знак зодиака - Тигр")
# else:
#     print("Ваш лунный знак зодиака - Кролик")

# *****

# from random import shuffle

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]

# shuffle(names)

# total = 13  
# num = 4  

# team_size = total // num  
# remainder = total % num  

# teams = [] 

# start = 0

# for i in range(num):
#     end = start + team_size 

#     if i < remainder:
#         end += 1 

#     team = names[start:end]
#     teams.append(team) 

#     start = end 

# for i, team in enumerate(teams):
#     print(f"Команда {i+1}: {', '.join(team)}")

# import datetime
# currenttime = datetime.datetime.now()
# print(f"Текущее время: {currenttime}")

# NUMBERS = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]

# for i in range(len(NUMBERS) - 1):
#     num1 = NUMBERS[i]
#     num2 = NUMBERS[i + 1]
#     sum = num1 + num2
#     print(f"Сумма чисел {num1} и {num2}: {sum}")

# from time import sleep
# for i in range(10):
#     print(i)
#     sleep(5)

# from time import sleep
# password = 123456
# count = 3
# logged_in = False

# while count > 0 and not logged_in:
#     count_less = count
#     while count_less > 0:
#         user_input = int(input("Введите пароль: "))

#         if user_input == password:
#             logged_in = True
#             break
#         else: 
#             count_less -= 1
#             print("Неверный Пароль! Повторите попытку!")
#             if count > 0:
#                 print(f"У вас осталось {count_less} попытки")
            
#     if logged_in:
#         print("Вход Выполнен")
#     else:
#         print("У вас не осталось попыток!")
#         sleep(5)
