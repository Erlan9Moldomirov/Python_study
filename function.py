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