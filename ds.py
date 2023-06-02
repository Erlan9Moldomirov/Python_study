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
    
# import math
# def sqr(a):
#     p = a * 4 
#     s = a * 2
#     d = 2*a**2
#     d2 = math.sqrt(d)
#     print(f"Периметр - {p}. Площадь - {s}. Диагональ - {round(d2, 1)}")

# a = int(input())
# sqr(a)


import os
import shutil

def image():
    im1 = input("Введите путь первой картинки: ")
    im2 = input("Введите путь второй картинки: ")

    if os.path.exists(im1) and os.path.exists(im2):
        shutil.copyfile(im1, im2)
    else:
        if not os.path.exists(im1):
            print(f"Файл {im1} не найден")
        if not os.path.exists(im2):
            print(f"Файл {im2} не найден")

image()
