# import os
# print(os.getcwd())

# import sys
# print(sys.platform)

# from random import random, randrange, choice, sample, randint

# num = randrange(0, 100)
# print(num)

# a = ['(G)I-DLE', 'STAYC', 'DREMCATCHER', 'TWICE', 'PINK FANTASY', 'CLC', '4MINUTE']
# print(choice(a))
# print(sample(a, 4))

# rand_num = randint(0, 10)
# user = int(input("Введите цифру: "))
# if user == rand_num:
#     print("Вы угадали!")
# elif user != rand_num:
#     print("Вы не угадали!")
# else:
#     print("Введите число от 0 до 10!")

# count = 3
# while count > 0:
#     rand_num = randint(0, 10)
#     user = int(input("Введите цифру: "))
#     if user > 10:
#         print("Введите число от 0 до 10!")
#     elif user == rand_num:
#         print("Вы угадали!")
#         break
#     elif user != rand_num:
#         print("Вы не угадали!")
#         count -= 1
#         print(rand_num)

# import time
# password = 123456
# count = 3 
# loged_in = False



# while count > 0:
#     user = int(input())
#     if user == password:
#         loged_in = True
#         break
#     else:
#         count -= 1
#         print("Неверный пароль.Повторите попытку")
# if loged_in:
#     print("Вход выполнен") 
# else:
#     print("У вас не осталось попыток")
#     time.sleep(10)

# import math
# print(math.ceil(4.3))
# print(math.floor(4.3))
# print(math.factorial(5))
# print(math.sqrt(16))
# num = int(input())
# print(math.sin(num))

# from main import a
# print(a)

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# from random import sample
# print(sample(names, 4))

# import sys
# print(sys.platform)

# import os
# import random
# import string

# desktop_path = os.path.expanduser("~/Рабочий стол")
# directory_path = os.path.join(desktop_path, "my_directory")

# if not os.path.exists(directory_path):
#     os.makedirs(directory_path)
    
# for i in range(5):
#     random_file = "".join(random.choices(string.ascii_letters, k=8)) + '.txt'
#     file_path = os.path.join(directory_path, random_file)
    
# with open(file_path, 'w') as file:
#     file.write("Это рандомный файл")

# from random import randrange
# num = randrange(6, 12)
# if num % 2 == 0:
#     print(num)

# num = randrange(5, 100)
# if num % 5 == 0:
#     print(num)

