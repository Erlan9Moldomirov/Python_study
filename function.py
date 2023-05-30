# a = [True, True, False, True]
# print(any(a))
# print(all(a))
 
# a = -5
# print(abs(a))

# lst = [1, 2, 3, 4, 5]
# print(min(lst))
# print(max(lst))
# print(list(reversed(lst)))

# num = 3.1445643345
# print(round(num, 3))

# loan = float(input('Введите сумму займа: '))
# percent = 3.47
# total = loan * (percent / 100)
# if loan >= 50000:
#     print(round(total, 2))
# else:
#     print('Введите сумму выше пятидесяти тысяч!')

# setm = set()
# for i in range(5):
#     i = int(input('Введите число: '))
#     setm.add(i)
# print(min(setm))

# try:
#     a = int(input())
#     b = int(input())
#     print(a / b)
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     print(10 + '10')
# except TypeError:
#     print("Нельзя сложить из числа и строки")

# values = ['a', 'b', (4, 5), 'c']

# convertibility = []
# for item in values:
#     try:
#         set(item)
#         convertibility.append(True)
#     except TypeError:
#         convertibility.append(False)

# can_convert = all(convertibility)
# print("Можно ли конвертировать values в SET?", can_convert)

# user_input = input("Введите Python функцию: ")

# try:
#     result = eval(user_input)
#     print("Результат выполнения функции", result)
# except NameError:
#     print("В Python такой фунции нет!")

# try:
#     my_list =[1, 2, 3]
#     print(my_list[6])
# except IndexError:
#     print("Такого индекса нет")

# while True:
#     try:
#         num1 = int(input())
#         a = input()
#         num2 = int(input())
#         if a == '+':
#             print(num1 + num2)
#         elif a == "-":
#             print(num1 - num2)
#         elif a == '/':
#             try: 
#                 print(num1 / num2)
#             except ZeroDivisionError:
#                 print("Нельзя делить на ноль!")
#             finally:
#                 print('YES')
#         elif a == '*':
#             print(num1 * num2)
#         elif a == '**':
#             print(num1 ** num2)
#         else:
#             print("Error")
#     except ValueError :
#         print("Введите число!")

# dict_ = {'name': 'join', 'lastname': 'Snow', 12 : 'age'}
# try:
#     for i in dict_.keys():
#         dict_ = i + 'abc'
#         print(dict_)
# except TypeError:
#     print("Нельзя сложить число в строку!")

# def num_summ():
#     a = 13
#     b = 8
#     print(a + b)
# num_summ()

# def num_summ(a, b):
#     print(a + b)

# a = 13
# b = 8
# result = num_summ(13, 8)

# my_list = [1, 'Mario', 3.5]

# def length():
#     result = 0
#     for i in my_list:
#         result += 1
#     print(f"Список состоит из  {result} элементов")

# length()

# def split_and_reversed(lst):
#     middle = len(lst) // 2

#     left_half = lst[:middle][::-1]
#     right_half = lst[middle:][::-1]

#     reversed_list = left_half + right_half

#     return reversed_list

# list_1 = ['name', 'age', '1', '19']
# modifided_list = split_and_reversed(list_1)

# print("Оригинальный лист", list_1)
# print("Измененный лист", modifided_list)

# def chat_bot():
#     while True:
#         word = input()
#         if type(word) != str(word):
#             print('Введите слово!')
#         elif word == "":
#             print("Как классно когда ты молчишь. Продолжай в том же духе")
#         elif '?' in word:
#             print("Конечно!")
#         elif word.upper() == word:
#             print("Успокойся!")
#         else:
#             print("Ну и что")

# chat_bot()

# def sum(a, b):
#     return a + b

# def min(a, b):
#     return a - b

# def ret(a, b):
#     c = sum(a, b)
#     d = min(a, b)
#     return c, d

# a = 15
# b = 10
# e = ret(a, b)
# print(e)

# def create_file(f):
#     with open(f, 'w') as file:
#         file.write("Hello, World")
    
# file_name = input()

# result = create_file
# result(file_name)

# import random

# def gen_number():
#     code = "0444"
#     number = code

#     for i in range(6):
#         digit = random.choice(['1', '4', '5', '7', '9', '0'])
#         number += digit 
#     return number 
# phone_number = gen_number() 
# print("Сгенерированный номер", phone_number)