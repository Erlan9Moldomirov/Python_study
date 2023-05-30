# a = 16
# b = 30
# c = 15

# while a < 23:
#     print(a)

# while b > c:
#     print(a, ">", b)

# string = "Hello"
# print(len(string))

# for i in string:
#     print(i)

# i = 0
# while i < len(string):
#     print(string[i])
#     i += 1

# count = 0 
# count1 = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         count += 1
#         print(i)
#     else: 
#         count1 += 1
# print(count)
# print(count1)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in my_list: 
#     print(i)

# i = 0 
# while i < len( my_list):
#     print(my_list[i])
#     i += 1

# password = 123456
# count = 3
# Loged_in = False

# while count > 0:
#     user_input = int(input("Введите пароль: "))

#     if user_input == password:
#         Loged_in = True
#         break
#     else: 
#         count -= 1
#         print("Неверный Пароль! Повторите попытку!")
     
# if Loged_in:
#     print("Вход Выполнен")
# else:
#     print("У вас не осталось попыток!")


# sum = 0
# num = int(input("Введите число: "))
# while num != 0:
#     sum += num
#     num = int(input("Введите число: "))
# print("Сумма введенных чисел - ", sum)

# lst = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# for i in lst:
#     if i == 25:
#         break
#     print(i)

# num = 0
# for i in range(1, 6):
#     print(i, num)

# a = 20
# b = 21 
# c = 20
# num = int(input("Введите число: "))
# if a and c == num:
#     print("yes")
# else: 
#     print("ERROR")

# a = 8
# b = 0
# c = 8
# if a == b or a == c or b == c:
#     print('Yes')
# else:
#     print("Error")

# sum = 0 
# for i in range(1, 101):
#     sum += i
# print("Сумма", sum)

# count = 0 
# num = [2, -7, -4]
# for i in num: 
#     if i > 0:
#         count += 1
#         print(i)


# list1 = [3, 5, 2, 1, 4]
# list2 = [4, 2, 6, 8, 1]
# a = list1 + list2
# b = set(a)
# print(b)
# c = list(b)
# print(c)

# list = []

# for i in range (1, 16):
#     list.append(i)

# max_lst = max(list)
# min_lst = min(list)
# print(max_lst + min_lst)

# *****

# m = int(input("Введите номер месяца: "))

# if (m == 1) or (m <= 2) or (m == 12):
#     print("Зима")

# elif (m == 3) or (m <= 5):
#     print("Весна")

# elif (m == 6) or (m <= 8):
#     print("Лето")

# elif (m == 9) or (m<= 11):
#     print("Осень")

# else:
#     print("Вы неправильно ввели месяц!")

# a = ['a', 'e', 'i', 'o', 'u']
# sstr = input("Введите слово:")
# new = sstr.split()

# for i in new:
#     if i[0].lower() in a:
#         print(i)

# r = int(input("Введите радиус: "))
# res = 2 * 3.14 * r
# print(f"Длина окружности: {res}")

