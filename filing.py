# file = open("new.txt", "r")
# file.write("Hello, World\n")
# file.write("Hi")
# s = file.read()
# print(s)
# file.close()

# login = input("Введите ваш логин: ")
# password = int(input())

# with open("users.txt", "a", encoding="utf-8") as file:
#     file.write(f"Ваш логин - {login}, Ваш пароль {password}")

#******

# try:
#     with open("new.txt", "r") as file:
#         s = file.read()
#         print(s)
#         file.close()
# except FileNotFoundError:
#     print("Файл не найден")

#******

# try:
#     with open("users.txt", "r", encoding= "utf-8") as file:
#         text = file.read()

#         if "w" in text:
#             print("Да, в тексте есть w")
#         else:
#             print("Нет, в тексте нет w")

# except FileNotFoundError:
#     print("Файл не найден")

# file_name = "users.txt"
# with open(file_name, "w") as file:
#     text = file.write("too much extentions in the world")

# with open(file_name ,"r") as file:
#     text = file.read()

#******

# t_words =[]
# for word in text.split():
#     if "t" in word.lower():
#         t_words.append(word)

# for word in t_words:
#     print(word)

#******

# numbers = [19, 3, 24, 5, 7]
# file_name="users.txt"
# with open(file_name, "w") as file:
#     for number in numbers:
#         file.write(str(number)+ "\n")
# max_number = float ("-inf")
# min_number = float ("inf")
# with open(file_name, "r")as file:
#     for i in file:
#         number = int(i.strip())
#         max_number = max(max_number, number)
#         min_number = min(min_number, number)
# output_file = "result.txt"
# with open(output_file, "w") as file:
#     file.write("максимальное число:" + str (max_number) + " ")
#     file.write("минимальное число:" + str (min_number))
# print("максимальное и минимальное число записаны в файл", output_file)