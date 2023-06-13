# is_nice = 9 > 10
# state = "nice" if is_nice else "not nice"
# print(state)

# nice = True
# personality = ("добрая", "вредная")[nice]
# print("Кошка", personality)

# num = int(input())
# num_type = "четный" if num % 2 == 0 else "нечетный"
# num_type = ("нечетный", "четный") [num % 2 == 0]
# print(num_type)

# def palindrom(x):
#     if len(x) <= 1:
#         return True
#     if x[0] != x[-1]:
#         return False
#     return palindrom(x[1:-1])
# print(palindrom("loyal"))

# def rec(w):
#     if len(w) == 1 or len(w) == 2:
#         return w
#     return w[0] + "(" +rec(w[1:-1]) + ")" + w[-1]

# w = input()
# print(rec(w))

# def summ(*args):
#     return sum(args)
# print(summ(1, 6, 3))

# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# info(name = "Erlan", age = 25)

# def my_func_1():
#     def nested_func_1():
#         print("In my_func_1.")
#         nested_func_2()

#     def nested_func_2():
#         print("In nested_func_1.")
#         nested_func_3()

#     def nested_func_3():
#         print("In nested_func_2.")
#         nested_func_4()

#     def nested_func_4():

# def my_func_1():
#     def nested_func_1():
#         print("In my_func_1.")
#         nested_func_2()

#     def nested_func_2():
#         print("In nested_func_1.")
#         nested_func_3()

#     def nested_func_3():
#         print("In nested_func_2.")
#         nested_func_4()

#     def nested_func_4():
#         print("In nested_func_3.")

#     nested_func_1()

# my_func_1()
#         print("In nested_func_3.")

#     nested_func_1()

# my_func_1()
            
# def search_substr(subst, st):
#     if subst.lower() in st.lower():
#         return "Есть контакт!"
    
#     else:
#         return "Мимо!"

# print(search_substr("one","one piece"))
# print(search_substr("666", "Germa66"))


# def biggest_dict(**kwargs):
#     global my_dict
#     my_dict.update(kwargs)
# my_dict = {'first_one': 'we can do it'}
# print(my_dict)
# biggest_dict(second_one = "we_are")
# print(my_dict)

# list1 = [5, 10, 15, 20, 25, 50, 20]
# inum = list1.index(20)
# list1[inum] = 200
# print(list1)

# aList = [1, 2, 3, 4, 5, 6, 7]
# bList =[]

# for i in aList:
#     bList.append(i**2)
# print(bList)

# list = [5, 20, 15, 20, 25, 50, 20]

# def removeValue(sampleList, val):
#    return [value for value in sampleList if value != val]
# resList = removeValue(list, 20)
# print(resList)

# letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# clean_let = ''
# for i in letters:
#     if i.islower():
#         clean_let += i
# print(clean_let)

# numbers = [1, 2, 3, 4, 5, 1, 2, 3]
# num = list(set(numbers))
# num.sort
# print(num)

# # new_fun

import random

def random_num(a):
    num1 = random.randint(20, 30)
    num2 = random.randint(1, 20)
    if a == "+":
        print(num1 + num2)
    elif a == "-":
        print(num1 - num2)
    elif a == "*":
        print(num1 * num2)
    elif a == "/":
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print("Нельзя делить на 0")
    else:
        print("Error")
    print(f"Первое число - {num1}, второе число - {num2}")   

    

a = input()
random_num(a)



