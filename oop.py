# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     name = "Erlan"
#     age = 25

#     def info(self):
#         print(f"My name is {self.name}, I am {self.age} years old")

# person = Person("Erlan", 25)
# person.info()


# import math
# class Math():
#     def __init__(self, a):
#         self.a = a

#     def perimetr(self):
#         return self.a * 4
    
#     def squar(self):
#         return self.a ** 2
    
#     def diagonal(self):
#         res = (self.a ** 2 + self.a ** 2)
#         res2 = math.sqrt(res)
#         return res2
    
# matth = Math(3)
# print(matth.perimetr())
# print(matth.squar())
# print(matth.diagonal())

# class Rectangle():
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def get_area(self):
#         area = self.a * self.b
#         return f"Площадь првямопугольника равна {area}"
    
# rectangle = Rectangle(5, 4)
# print(rectangle.get_area())

# class Cars():
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def get_info(self):
#         return f"Марка автомобиля:{self.brand}, модель: {self.model} "
    
# car = Cars("TOYOTA", "RAV4")
# print(car.get_info())
# car2 = Cars("Daewoo", "Matiz")
# print(car2.get_info())

# class Circle():
    
#     def __init__(self, radius):
#         self.radius = radius
    
#     def get_circumference(self):
#         C = 2 * 3.14 * self.radius
#         return C
    
#     def get_area(self):
#         A = 3.14 * self.radius ** 2
#         return A
# circle = Circle(4)
# print(circle.get_circumference())
# print(circle.get_area())

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.baa = []

#     def student_baa(self, num):
#         self.baa.append(num)

#     def student_info(self):
#         if len(self.baa) > 0:
#             return sum(self.baa) / len(self.baa)
#         else:
#             return 0

# student = Student("Bayel")
# student.student_baa(5)
# student.student_baa(5)
# student.student_baa(5)
# student.student_baa(5)
# student.student_baa(5)
# print(student.student_info())


# class Bank:
#     def init(self, name, money=0):
#         self.name = name
#         self.money = money
        
#     def plus(self, amount):
#         self.money += amount
        
#     def minus(self, amount):
#         if self.money >= amount:
#             self.money -= amount
#         else:
#             print(f"Недостаточно средств")     
    
#     def get_money(self):
#         print(f"Name - {self.name}, money - {self.money}")   
        
# bank = Bank()  
# bank.plus(500)
# bank.plus(500)
# bank.minus(1040)
# bank.get_money()

# class Bus:
#     def __init__(self, name):
#         self.name = name
    
#     def driving(self):
#         print(f"The {self.name} is driving")

# class Car(Bus):
#     def hunk(self):
#         print("Beep, beep!")

# car = Car("Maybach")
# car.driving()
# car.hunk()

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_info(self):
#         print(f"Name - {self.name}")
#         print(f"Salary - {self.salary}")
    
# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department
    
#     def display_info(self):
#         super().display_info()
#         print(f"Department - {self.department}")

# emp = Employee("John", 4000)
# manager = Manager("Jack", 5000, "Sale")
# emp.display_info()
# print("-------------")
# manager.display_info()

# class Animal:
#     def sound(self):
#         pass

# class Cat(Animal):
#     def sound(self):
#         print("Мяу-мяу")

# class Dog(Animal):
#     def sound(self):
#         print("Гав-гав")

# def make_sound(animal):
#     animal.sound()

# dog = Dog()
# cat = Cat()

# make_sound(dog)
# make_sound(cat)

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         pass

# class Cat(Animal):
#     def sound(self):
#         return "Мяу-мяу"

# class Dog(Animal):
#     def sound(self):
#         return "Гав-гав"

# dog = Dog("Боря")
# cat = Cat("Муря")

# print(dog.name, dog.sound())
# print(cat.name, cat.sound())

# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def display_info(self):
#         print(f"Имя студента: {self.name}") 
#         print(f"Возраст студента: {self.age}")
#         print(f"Номер студента: {self.student_id}")  

# student = Student("Иван", 20, 12345)
# student.display_info()

# class Horse():
#     isHorse = True

# class Donkey():
#     isDonkey = True

# class Mule(Horse, Donkey):
#     pass

# mule = Mule()
# print(mule.isHorse)
# print(mule.isDonkey)

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Meow")

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Bark")

# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()

# from math import pi
# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         pass

#     def fact(self):
#         return "I am a two-dimensional shape."

#     def __str__(self):
#         return self.name

# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Square")
#         self.length = length

#     def area(self):
#         return self.length**2

#     def fact(self):
#         return "Squares have each angle equal to 90 degrees."

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius

#     def area(self):
#         return pi*self.radius**2

# a = Square(4)
# b = Circle(7)
# print(b)
# print(b.fact())
# print(a.fact())
# print(b.area())