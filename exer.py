# def bank(a, years):
#     per = 0.10 #10-процентная ставка
#     sum = a * (1 + per) ** years #формула 
#     return int(sum)

# a = int(input("Введите сумму вклада: "))
# years = int(input("введите срок: "))

# result = bank(a, years)
# print(f"Итоговая сумма на счету пользователя: {result} рублей")

# def is_valid_date(day, month, year):

#     if year < 1 or year > 9999:
#         return False

#     if month < 1 or month > 12:
#         return False
    
#     if day < 1:
#         return False

#     if month == 2:
#         if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#             if day > 29:
#                 return False
#         elif day > 28:
#             return False
#     elif month in [4, 6, 9, 11]:
#         if day > 30:
#             return False
#     else:  # Остальные месяцы
#         if day > 31:
#             return False

#     return True

# day = int(input())
# month = int(input())
# year = int(input())

# if is_valid_date(day, month, year):
#     print("Действительная дата")
# else:
#     print("Недействительная дата")

# def XOR_cipher(message, key):
#         encrypted_message = ""
#         for char in message:
#             encrypted_char = chr(ord(char) ^ key)
#             encrypted_message += encrypted_char
#         return encrypted_message


# def XOR_uncipher(encrypted_message, key):
#     decrypted_message = ""
#     for char in encrypted_message:
#         decrypted_char = chr(ord(char) ^ key)
#         decrypted_message += decrypted_char
#     return decrypted_message

# message = input()
# key = int(input())

# encrypted_message = XOR_cipher(message, key)
# print("Зашифрованное сообщение:", encrypted_message)

# decrypted_message = XOR_uncipher(encrypted_message, key)
# print("Расшифрованное сообщение:", decrypted_message)