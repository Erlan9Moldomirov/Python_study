# import os
# import shutil

# def register():
#     login = input("Введите логин: ")
#     password = input("Введите пароль: ")
#     photo_path = input("Введитие путь до фото: ")
    
#     if os.path.exists(photo_path):
#         _,photo_split = os.path.splitext(photo_path)
#         valid_photo_split = ['.jpeg', '.jpg', '.png']
        
#         if photo_split.lower() in valid_photo_split:
#             photo = f"registred_foto/{login}{photo_split}"   
            
#             shutil.copyfile(photo_path, photo)
            
#             with open("database.txt", 'a') as file:
#                 file.write(f"{login}:{password}:{photo}\n")
#             print("Регистрация успешна завершена")
        
#         else:
#             print("Неподдерживаемое расширение фотографии. Регистрация отменена")
#     else:
#         print("Фото не найдено. Регистрация отменена")        
        
# os.makedirs('registred_foto', exist_ok=True)

# register()

#******

# def arithmetic():
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число:"))
#     operator = input("Введите тип арифметического оператора: ")
#     if operator == "+":
#         return num1 + num2
    
#     elif operator == "-":
#         return num1 - num2
    
#     elif operator == "*":
#         return num1 * num2
    
#     elif operator == "/":
#         return num1 / num2
    
#     else:
#         print("Неизвестная операция!")

# print(arithmetic())

#******

# import math
# def sqr(a):
#     p = a * 4 
#     s = a * 2
#     d = 2*a**2
#     d2 = math.sqrt(d)
#     print(f"Периметр - {p}. Площадь - {s}. Диагональ - {round(d2, 1)}")

# a = int(input())
# sqr(a)

#******

# import os
# import shutil

# def image():
#     im1 = input("Введите путь первой картинки: ")
#     im2 = input("Введите путь второй картинки: ")

#     if os.path.exists(im1) and os.path.exists(im2):
#         shutil.copyfile(im1, im2)
#     else:
#         if not os.path.exists(im1):
#             print(f"Файл {im1} не найден")
#         if not os.path.exists(im2):
#             print(f"Файл {im2} не найден")

# image()

#******

# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# num = int(input())
# if is_prime(num):
#     print(num, "является простым числом")
# else:
#     print(num, "не является простым числом")

#******

# def get_keys_and_values(dictionary):
#     keys = tuple(dictionary.keys())
#     values = tuple(dictionary.values())
#     return keys, values

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# result_keys, result_values = get_keys_and_values(my_dict)

# print("Keys:", result_keys)
# print("Values:", result_values)

#******

# def print_text_lines():
#     text = input("Введите текст: ")
#     count = int(input("Введите количество строк: "))
#     for _ in range(count):
#         print(text)

# print_text_lines()

#******

# def generate_fibonacci():
#     fibonacci_sequence = [1, 1] 

#     while len(fibonacci_sequence) < 10:
#         next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
#         fibonacci_sequence.append(next_number)

#     return fibonacci_sequence

# fibonacci_numbers = generate_fibonacci()
# print(fibonacci_numbers)

#******

# def addition(a, b):
#     return a + b

# def subtraction(a, b):
#     return a - b

# def perform_operations(a, b):
#     result_addition = addition(a, b)
#     result_subtraction = subtraction(a, b)
#     return result_addition, result_subtraction

# num1 = 10
# num2 = 5

# result_add, result_sub = perform_operations(num1, num2)
# print("Результат сложения:", result_add)
# print("Результат вычитания:", result_sub)


