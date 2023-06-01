# user = "Erlan"
# password = 12345

# u = input("Введите имя пользователя: ")
# p = int(input("Введите пароль: "))

# if u == user and p == password:
#     print("Добро пожаловать!")
# else:
#     print("Неверный логин или пароль!")

# *****

# user = "Erlan"
# password = "Covacic23"

# u = input("Введите имя пользователя: ")
# p = input("Введите пароль: ")

# if u == user and p == password:
#     print("Добро пожаловать!")
# else:
#     print("Неверный логин или пароль!")

# for i in range(10):
#     print("I love Python")

# *****

# sset = {1, 2, 3, 4, 5, 6}
# sset2 = {1, 2, 3, 7, 8, 9}

# result = sset.difference(sset2)
# result2 = sset2.difference(sset)
# print(result)
# print(result2)

# result3 = sset.intersection(sset2)
# print(result3)

# result5 = sset.intersection_update(sset2)
# print(result5)

# sset.add(7)
# sset.remove(4)
# sset2.remove(2)
# sset.discard(10)
# sset.clear()
# print(sset)
# print(sset2)

# *****

# a = {"apple", "banana", "mango", "avocado"}
# b = {"grape", "apple", "avocado", "peach"}

# print(a)
# print(b)

# a.add("orange")
# print(a)

# b.remove("apple")
# print(b)

# a.discard("avocado")
# a.discard("tomato")
# print(a)

# result3 = a.difference(b)
# print(result3)

# result = a.intersection(b)
# result2 = a.intersection_update(b)
# print(result)
# print(result2)

# *****

# a = {"apple", "banana", "mango", "avocado", "orange"}
# a.add("tomato")
# print(a)
# b = a.pop()
# print(a)
# print(b)

# *****

# info = {
#     'name': "Ali",
#     'age': 35,
#     'fruit': ["banana", "mango"]
# }

# print(info.get('fruit'))
# print(info.keys())
# print(info.values())
# print(info.items())
# print(info)

# *****

# a = {'apple': 10, 'banana': 20}
# b = {'apple': 40, 'mango': 50}
# a.update(b)
# print(a) 

# *****

# menu = {}
# menu['besh_barmak'] = 130
# menu['lagman'] = 125
# menu['plov'] = 150
# menu['drinks'] = ["Coca-Cola", "Fanta", "Sprite"]
# # del menu['plov']
# print(menu)

# *****

# info = {}
# for i in range(3):
#     name = input('Введите имя: ')
#     password = int(input('Введите пароль: '))
#     info[name] = password

# print(info)
# print(info.keys())
# print(info.values())

# *****

# sset = set(dir(set))
# ddict = set(dir(dict))
# result = sset.intersection(ddict)
# print(result)

# *****

# info = {'David': 'pogrammer', 'Jack': 'engineer', 'Max': 'dancer'}

# for k, v in info.items():
#     print(f"Hello {k}, {v} is good profession.")

# *****

# countries = ['Argentina', 'Brasil', 'Urugvay', 'Bolivia', 'Brasil']

# state = set(countries)
# print(state)

# countries = list(state)
# print(countries)

# *****

# suitcase = []
# suitcase.append("shirt")
# suitcase.append("shoes")
# suitcase.append("hat")
# suitcase.append("umbrella")
# suitcase.append("password")
# suitcase.pop()
# print(suitcase)

# *****

# sset = []

# for i in range(10):
#     a = int(input())
#     sset.append(a)
#     res = tuple(sset)

# print(res)

# *****

# sset1 = {1, 'Apple', -23, 'dream', 3.5, 'BLOCK', 0, 'ball', 54}
# sset2 = {-23, 5, 'dream', 3.4, 12, 54}
# sset3 = sset1.intersection(sset2)
# # print(sset3)

# *****

# num =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = (sum(num) / len(num))
# print(res)
# a = max(num)
# b = min(num)
# c = [a, b]
# print(sum(c))