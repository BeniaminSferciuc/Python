# import math

# print("Hello, Python!")
# print(int(15/2))

# x = pow(3,3)
# print(x)

# y = abs(-65)
# print(y)

# x = -23

# if x < 0:
#     x = -x
# else:
#     x = x

# print("Absolut value: " + str(x))

# print(math.sin(3.14159))
# print("Sin pi: %.10f" % math.sin(3.14159))
# print(math.factorial(5))
# print(math.radians(math.sin(45)))

# x = 3
# y = 4

# rez = x is y
# print(rez)
# rez = x is not y
# print(rez)

# str = 'THIS IS A STRING'
# x = str.lower()
# print(x)

# x = input("Introduceti numele dvs.: ")
# print("Numele introdus este: " + x) 

# a = "Hello,"
# b = "Python!"
# print(a + b)
# print(a, b)

# print(b[-1]) #acceseaza ultimul caracter din sir

# print ("'You must be the change you wish to see in the world' - Gandhi")
# print ('"You must be the change you wish to see in the world" - Gandhi')

# print ("\"You must be the change you wish to see in the world\"")
# print("Benjamin! " * 10)
# print("that" in "this is it")

# string = "10"
# print(int(string))
# str = "Hello Brother!"
# print(str[0:10:2])

# s = "Hello!"
# ss = "lo"
# print(s.find(ss))
# print(s.lower())
# print(s.upper())

# print(s.islower())

# s = "Hello, Python!"
# ss = "Beniamin"
# print(s.replace("Python", ss))

# newS = s.split(',')
# print(newS[0])

# myList1 = ['first', 'secound', 'third', 'fourth', 'fifth']
# myList2 = myList1
# print(myList1)
# print(myList2)

# myList3 = myList1[0:3]
# print(myList3)
# myList4 = myList1[-3]
# print(myList4)

# myList5 = range(9)
# print(myList5[7])

# mylist = []
# print(mylist)

# mylist.append("This is putted in mylist with append function")
# print(mylist)

# mylist.append("After first append!")
# print(mylist)

# for var in range(1, 10):
#     print(var)

# i = 0;
# while i < 10:
#     print(i)
#     i += 1

# myList = ['first', 'secound', 'third', 'fourth']
# for x in range(len(myList)):
#     print("This is myList[x]: ", myList[x])
    
# i = 0
# A = [1, 2, 3, 4, 2, 6]
# B = [5, 6, 7, 8]
# C = []

# for x, y in zip(A, B):
#     C.append(x + y)

# print(C)

# size_A = len(A)
# size_B = len(B)

# if size_A > size_B:
#     C.append(A[size_B : size_A + 1])

# print(C)

# x = ['apple', 'samsung', 'huawei', 'IBM', 'Facebook']
# y = ['first', 'secound', 'third']
# ap = []

# for za, zb  in zip(x, y):
#     ap.append(za + ' ' + zb)

# print(*ap)

# x.pop(0)
# print(x)

# myList = [12, 34, 89, 32, 90, 23, 67, 12, 64]
# del myList[2]
# print(myList)
# del myList[1:5]
# print(myList)


# count = 0;
# sir = ["apple", 'apple', 'banana', 'kiwi', 'apple', 'mango']
# for i in range(len(sir)):
#     if 'apple' is sir[i]:
#         count = count + 1
    
# print("S-au gasit:", count)

# for i in range(count):
#     sir.remove("apple")

# print(sir)

# print(', '.join(sir))

# lis = [1, 11, 111]
# print(lis)

# print(str(lis).strip('[]'))

# myStr = ', '.join(str(i) for i in lis)
# print(myStr)

# myList = ['Python', 'C++', 'Java']
# myList.insert(1, 'Javascript')
# print(myList)

# print(', '.join(str(i) for i in myList))

# myList.reverse()
# print(myList)

# myList = [3,7,1,8,2,6]
# myList.sort()
# print(myList)

# # Crearea unui dictionar
# myDictionary = {'key-1': 'element-1', 'key-2': 'element-2', 'key-3': 'element-3', 'key-4': 'element-4', 'key-5': 'element-5'}

# # iterarea prin dictionar
# for i in myDictionary:
#     print('key: ' + i + ", " + 'element: ' + myDictionary[i])

# # Stergerea unui element dintr-un dictionar
# del myDictionary['key-2'] 
# print(myDictionary)

# # Adaugarea unui element intr-un dictionar
# myDictionary["key-6"] = "element-6"
# print(myDictionary)

# # Pentru a afisa un element din dictionar
# print(myDictionary['key-1'])

# integerDictionary = {10: 'C++', 20: 'Java'}
# print(integerDictionary[20] + " si " + integerDictionary[10])

# emptyDictionary = {}
# print(emptyDictionary)

# emptyDictionary['India'] = 'Delhi'
# print(emptyDictionary)

# emptyDictionary['Romania'] = 'Bucuresti'
# print(emptyDictionary)

# # Actualizarea elementelor existente intr-un dictionar
# firstDictionary = {'Course-1': 'C', 'Course-2': 'C++', 'Course-3': 'Python', 'Course-4': 'HTML5', 'Course-5': 'CSS3'}
# secoundDictionary = {'Course-1': 'Javascript', 'Course-6': 'SQL'}

# print(firstDictionary)
# firstDictionary.update(secoundDictionary)
# print(firstDictionary)

# store_size = len(firstDictionary)
# print(store_size)

# print('Original:', firstDictionary)
# print('Items:', firstDictionary.items())

# print(firstDictionary.values())
# print(firstDictionary.keys())

# print(firstDictionary.__contains__('Course-7'))

# Despre tuple

# from filecmp import cmp

# myTuplu = 1, 2, 3, 4
# print(myTuplu[1])

# # Tuple gol
# emptyTuple = ()
# print(emptyTuple)

# t = 1, 2, 3, 4, 5
# print(t)
# t = t + (7,)
# print(t)

# # Concatenarea a doua tuple in alt tuplu cu operatorul +
# t1 = (1,2,3)
# print(t1)
# t2 = 4,5
# t3 = t1 + t2
# print(t3)

# # Stergerea unui tuplu
# del (t3)

# t = 1,2 
# print(t * 5)

# t = (1, 2, 3, 6, 7, 8)
# r = 2 in t
# w = 5 in t
# print(r, w)

# # afiseaza valoara maxima si minima
# print(max(t))
# print(min(t))

# print(True and False)
# print(True or False)
# print(not True)

# x = int(input())
# print('Se afla in intervalul [0, 100]:', (x > 0) and (x < 100))

# Mini program (bank account)
# amount = 1000
# print('Aveti suma de:   1000$')
# withdraw = int(input('Introduceti suma pe care doriti sa o scoateti: '))
# if withdraw > amount:
#     print('Bani insuficienti!')
# else:
#     print('Bani sunt pe drum!')
#     amount = amount - withdraw
# print('Noul dvs. sold: ' + str(amount) + '$')

# # Mini program cu intervalele zilei
# time = 1301

# if (time >= 600) and (time < 1200):
#     print("Morning!")
# elif time == 1200:
#     print('Noon!')
# elif (time > 1200) and (time <= 1700):
#     print('Afternoon!')
# elif (time > 1700) and (time <= 2000):
#     print('Evening!')
# elif ((time > 2000) and (time <= 2400)) or ((time >= 0) and (time < 600)):
#     print('Night!')
# else:
#     print('Invalid time')

# # Alternativa prin imbricarea declaratiilor if-else
# if (time >= 600) and (time < 1200):
# 	print ("Morning");
# else:
# 	if (time == 1200):
# 		print ("Noon");
# 	else:
# 		if (time > 1200) and (time <= 1700):
# 			print ("Afternoon");
# 		else:
# 			if (time > 1700) and (time <= 2000):
# 				print ("Evening");
# 			else:
# 				if ((time > 2000) and (time < 2400)) or ((time >= 0) and (time < 600)):
# 					print ("Night");
# 				else:
# 					print ("Invalid time!");

# Mai multe despre bucle
# for a in range(0, 5):
#     print(a)
# else:
#     print(6)
    
# print()
# myList = [8, 9, 1, 4, 5, 2]
# for i in myList:
#     print(i)

bigList = [[1, 3, 6], [8, 2], [0, 4, 7, 10], [1, 5, 2], [6]]
# for i in bigList:
# 	for j in i:
# 		print(j)

# print()
# i = 0
# while i < 5:
#     print(i)
#     i = i + 1
    
# print('After:')
# i = 0
# j = 0
# while i < len(bigList):
# 	while j < len(bigList[i]):
# 		print(bigList[i][j])
# 		j = j + 1
# 	i = i + 1
	
        
# name = 'Beniamin'
# for i in name:
# 	if not i.islower():
# 		continue
# 	print(i, end='')

# print()
# for i in name:
# 	if i == 'i':
# 		break	
# 	print(i, end='')
# print()

# x = 100
# print(hex(x).strip('0x'))
# print(oct(x).strip('0o'))
# print(bin(x).strip('0b'))

# tab = [10] * 10
# tab = [i for i in range(0, 10)]
# print(tab)

# size = int(input('Introduceti numarul de elemente din vector: '))
# arr = [int(input('arr[' + str(i) + '] = ')) for i in range(0, size)]
# print(arr)

# str = 'Eu sunt Beniamin Sferciuc si sunt fiul maniei drepte!'
# strArr = [x for x in str.split()]
# print(strArr)

# row = int(input("Introdu nr. de randuri: "))
# col = int(input("Introdu nr. de coloane: "))

# mat = [[0 for j in range(row)] for i in range(col)]
# for i in range(col):
#     mat[i] = [int(x) for x in input("Introduceti elementele de pe linia: " + str(i) + ': ').split()]

# print(mat)

# Sintaxa simpla si speciala pentru if-else
# x = 10
# condition = False
# x = 1 if condition else 0
# print(x)

# # Metoda utila de aplicat la numerele mari
# num1 = 1_000_000_000
# num2 = 1_000_000

# total = num1 + num2
# print(f'{total: ,}')

# # functia enumerate face codul sa fie mai curat
# myList = ['C/C++', 'HTML5', 'CSS3', 'JS', 'Python']
# for index, name in enumerate(myList, start = 1):
#     print(index, name)

# # list comprehensive + functia sorted()
# index = [i*i for i in range(0, 10)] 
# sort_list = sorted(index, reverse=True)
# print(*sort_list)

# # functia set() elimina duplicatele
# list = [3,7,4,7,8,3,4,7]
# unique_list = set(list)
# print(unique_list)

# imprima cuvintele cheie folosite de python
# import keyword
# print(keyword.kwlist)

# print(isinstance('hello', str))
# print('foobar')

# print()
# lst = [4,3,2,1]
# print(lst.reverse())
# print(lst[::-1]) #inverseaza ordinea

# Funtii in Python
'''Definirea unei funtii simple: '''
'''
def functionName(parameter1, parameter2):
    algorithm statements
    ...
    return someData
'''
# Ex: functie cu return
# def add(a1, a2):
#     c = a1 + a2
#     return c 

# a = int(input())
# b = int(input())
# c = add(a,b)
# print(c)

# # functie fara return
# def add(a, b):
#     return a + b

# print(add(a, b))

# # Trecerea unei functii ca parametru
# print(add(20, add(10, 20)))

# n = int(input())
# for i in range(1, n+1):
# 	if i%2 == 0:
# 		print(i, end=' ')
# 	else:
# 		print(2*i, end=' ')

# Argumente implicite
# def add(a = 0, b = 0): return a+b
# print(add(10,10))
# print(add()) # va return 0, fara ca python sa arunce o eroare in cazul in care nu se dau parametrii

# # Alias pentru functii
# suma = add
# print(suma(10,1))

# Definirea unei clase
'''
class Apolo:
    destination = 'Moon'
    def fly(self):
        print('Spaceship flying...')
    def get_destination(self):
        print('Destination is: ' + self.destination)

# Crearea obiectelor
firstObject = Apolo()
secondObject = Apolo()

firstObject.destination = 'Mars'
firstObject.get_destination()

secondObject.get_destination()
'''

# Exercitiu cu clase, propria clasa
'''
class Me:
    name = 'Beniamin T. Sferciuc'
    age = 21
    sex = 'Masculine'
    def aboutMe(self):
        print("My name is: " + self.name + \
            ', I am ' + str(self.age) + \
            ' years old and my sex is ' + \
            self.sex)

firstObj = Me()
firstObj.aboutMe()

class Example:
    def function(self, parameter1):
        self.age = parameter1
        self.name = input("Introduceti numele: ")
        print(f'Numele: {self.name} si varsta: {self.age} ani!')

age = input('Introduceti varsta: ')
description = Example()
description.function(age)
print(description.name)

description.function("Python is COOL!")
print(description.age)
'''

# About __new__
# class Example:
#     def __new__(self):
#         return 'Python'

# obj = Example()
# print(type(obj))

# # About __init__
# class Example:
#     def __init__(self, value1, value2):
#         self.myvar1 = value1
#         self.myvar2 = value2
#         print(self.myvar1)
#         print(self.myvar2)

# myObj = Example('Python', 'Javascript')

# Distrugerea unui obiect
# class Example:
#     def __init__(self):
#         print("Object created!")
#     def __del__(self):
#         print("Object destroyed!")

# myObj = Example()
# print(myObj)
# del myObj
# print(myObj)

# Mostenire
'''
class Parent:
    # class variable
    a = 10
    b = 100
    # some class methods
    def doThis(self):
        print('Parent - doThis')
    def doThat(self):
        print('Parent - doThat')
    
class Child(Parent): #specificand numele altei clase in paranteze, specificam mostenirea
    # child class variable
    x = 1000
    y = -1
    # some child class method
    def doWhat(self):
        print('Child - doWhat')
    def doNotDoThat(self):
        print('Child - doNotDoThat')

obj_1 = Child()
obj_1.doThis()
'''
'''
class Human:
    hands = 2
    legs = 2
    def talk(self):
        print("You talk to much!")

class Brain(Human):
    cell = 100000000
    def thinking(self):
        total_members = Human.hands + Human.legs 
        return total_members

segment = Brain()
segment.talk()
total = segment.thinking()
print(total)
'''
'''
# Modificator de acces: protected
class Employee:
    def __init__(self, name, sal):
        self._name = name
        self._sal = sal

emp = Employee("Captain America", 1000)
print(emp._sal)
print(emp._name)

class Child(Employee):
    def task(self):
        print(f'the best avengers!')

Child_emp = Child("Captain America", 1000)
Child_emp.task()
print(Child_emp._name)
'''

# Modificatori de acces: Private

# Modificator de acces: protected
'''
class Employee:
    def __init__(self, name, sal):
        self._name = name
        self._sal = sal

emp = Employee("Captain America", 1000)
print(emp.__sal) # double underscore
print(emp.__name)

class Child(Employee):
    def task(self):
        print(f'the best avengers!')

Child_emp = Child("Captain America", 1000)
Child_emp.task()
print(Child_emp.__name)
>>> eroare
'''
'''
# define parent class Company
class Company:
    # constructor
    def __init__(self, name, proj):
        self.name = name      # name(name of company) is public
        self._proj = proj     # proj(current project) is protected
    
    # public function to show the details
    def show(self):
        print("The code of the company is = ", self.ccode)

# define child class Emp
class Emp(Company):
    # constructor
    def __init__(self, eName, sal, cName, proj):
        # calling parent class constructor
        Company.__init__(self, cName, proj)
        self.name = eName   # public member variable
        self.__sal = sal    # private member variable
    
    # public function to show salary details
    def show_sal(self):
        print("The salary of", self.name, "is", self.__sal,)

# creating instance of Company class
c = Company("Stark Industries", "Mark 4")
# creating instance of Employee class
e = Emp("Steve", 9999999, c.name, c._proj)

print("Welcome to", c.name)
print("Here", e.name, "is working on", e._proj)

# only the instance itself can change the __sal variable
# and to show the value we have created a public function show_sal()
print(e.show_sal())
'''

#Suprascrierea metodei
#parent class
# class Parent:
#     # some random function
#     def anything(self):
#         print('Function defined in parent class!')
        
# # child class
# class Child(Parent):
#     # empty class definition
#     def anything(self):
#         print('Function defined in child class!')


# obj1 = Parent()
# obj1.anything()
# obj2 = Child()
# obj2.anything()

# class Square:
#     side = 5
#     def calculate_area(self):
#         return self.side**2
    
# class Triangle:
#     base = 5
#     height = 4
#     def calculate_area(self):
#         return 0.5 * self.base * self.height

# sq = Square()
# tr = Triangle()

# # Polimorfism cu bucle
# # for obj in (sq, tr):
# #     print(obj.calculate_area())

# # Polimorfism cu functii
# def find_area_of_shape(obj):
#     print(obj.calculate_area())

# find_area_of_shape(sq)
# find_area_of_shape(tr)

# Metode statice folosind staticmethod()
# class Shape:
#     var = 1000
#     def info(msg):
#         print(msg)
#         print("Alte info!")

# # Shape.info = staticmethod(Shape.info)
# # Shape.info("Welcome to Shape class!")
# print(Shape.var) 

# Metode statice folosind @staticmethod
# class Shape:
#     @staticmethod
#     def info(msg):
#         print(msg)

# Shape.info("Mesajul pe care dorim sa-l afisam!")

# Supraincarcarea operatorilor
# class Complex:
#     def __init__(self, r, i):
#         self.real = r
#         self.imag = i

#     def __add__(self, sec):
#         r = self.real + sec.real
#         i = self.imag + sec.imag
#         return complex(r, i)
    
#     def __str__(self):
#         return str(self.real) + ' + ' + str(self.imag) + 'i'

# c1 = Complex(5,3)
# c2 = Complex(5,2)
# print("Sum = ", c1 + c2)


# try:
#     a = 10
#     b = 0
#     print(a/b)
# except:
#     print("Impartirea la 0 nu exista!")


# with open('readme.txt', 'a') as file:
#     file.writelines("Hello, Python!")

# try:
#     print(1/'asf')
# except(ZeroDivisionError, ValueError, TypeError):
#     print("Erorr")
# finally:
#     print('End of program!')
# print("This will ...")

# raise ZeroDivisionError

# deschiderea fisierului in modul de citire text
# myFile = open("readme.txt", 'r')

# citirea unei singure linii din fisier
# linie = myFile.readline()
# print(linie)

# citirea tuturor liniilor din fisier cu readline()
# for line in myFile:
#     print(line, end = '')

# citirea toturor liniilor cu readlines()
# content = myFile.readlines()
# print(content)

# abordare echivalenta cu cea de sus
# content = []
# for line in myFile:
#     content.append(line)

# print(content)
# myFile.close()
# ____________________________________________________________________________________________________________________
# scrierea in fisier

# with open('readme.txt', 'a') as f:
#     # content = "This is a line of text write of Python form a program to a extern file with open() function!"
#     # f.write(content)
#     content = ["Python 3.x\n", "Hello, World. I am learning Python"]
#     f.writelines(content)
# ____________________________________________________________________________________________________________________
# pozitia indicatorului

# with open('readme.txt', 'r+') as file:
#     file.seek(5)
#     print(file.tell())
#     content = file.read()
#     print(content)
# ____________________________________________________________________________________________________________________
# copiati un fisier in altul

# file1 = open('readme.txt', 'r')
# file2 = open('copyFile.txt', 'w')

# l = file1.readline()
# while l:
#     file2.write(l)
#     l = file1.readline()

# file1.close()
# file2.close()
# ____________________________________________________________________________________________________________________
# despre __name__ si __main__ variabile speciale
# def something():
#     print("This function is in Learn.py")

# if __name__ == '__main__':
#     something()
#     print('Apelat din Learn.py')
# else:
#     print('Learn.py este importat din alte fisiere')
# ____________________________________________________________________________________________________________________
# despre __iter__(), iter(), __next__(), next()

# cars = ['Audi', 'Mercedes', 'VW', 'BMW', 'Jaguar', 'Tesla', 'Ford']
# # cars_iter = iter(cars)
# cars_iter = cars.__iter__()

# print(next(cars_iter))
# print(next(cars_iter))
# print(cars_iter.__next__())
# print(cars_iter.__next__())
# print(cars_iter.__next__())
# print(cars_iter.__next__())
# print(cars_iter.__next__())
# ____________________________________________________________________________________________________________________
# for - functionalitate

# cars = ['Audi', 'Mercedes', 'VW', 'BMW', 'Jaguar', 'Tesla', 'Ford']
# iter_obj = iter(cars)

# while True: # eroarea va fi StopIteration
#     try:
#         element = next(iter_obj)
#         print(element)
#     except:
#         break


# index = cars.__iter__()
# ____________________________________________________________________________________________________________________
# Exemplu:
# class Counting:
#     def __init__(self, limit):
#         self.limit = limit
    
#     # implementing the __iter__ method
#     def __iter__(self):
#         self.current = 0
#         return self
    
#     # implementing the __next__ method
#     def __next__(self): 
#         if self.current < self.limit:
#             self.current += 1
#             return self.current
#         else:
#             raise StopIteration
            
# if __name__=='__main__':
#   # create object of Counting class
#   counting = Counting(20)
  
#   # use for loop on it
#   for x in counting:
#     print(x)
# ____________________________________________________________________________________________________________________
# despre yield cuvantul cheie

# def counter():
#     x = 0
#     while x < 5:
#         yield x
#         x += 1

# print(counter())
# for i in counter():
#     print(i)
# ____________________________________________________________________________________________________________________
# inversare sir cu yield
# def reverse(string):
#     length = len(string)
#     for i in range(length - 1, -1, -1):
#         yield string[i]

# for j in reverse("Beniamin"):
#     print(j)

# functii imbricate si variabile non-locale
# def outer(message):
#     text = message
#     def inner():
#         print(text)
#     return inner
# func = outer("Hello, I am Python!")
# func()

# # alt mod
# def suma_1(n):
#     def suma_2(m):
#         return m + n
#     return suma_2

# first_func = suma_1(5)
# first_result_func = first_func(5)
# print(first_result_func)

# decoratori in Python

# def myDecor(func):
#     def wrapper():
#         print("Modified function")
#         func()
#     return wrapper

# def myfunc():
#     print('Hello!!')

# # decorating the myfunc function
# decorated_myfunc = myDecor(myfunc)

# # calling the decorated version
# decorated_myfunc()

# sau
# using the decorator function
# @myDecor
# def myfunc():
#     print('Hello!!')

# # Calling myfunc()
# myfunc()

# ____________________________________________________________________________________________________________________
# decorator cu argumente

# def myDecor(func):
#     def myfunc(*args, **kwargs):
#         print("Hello, ")
#         func(*args, **kwargs)
#     return myfunc

# @myDecor
# def another_func(msg):
#     print(msg)

# another_func("hello, python!")
# ____________________________________________________________________________________________________________________
# despre assert
# def percentage(marks):
#     for m in marks:
#         assert m > 0, 'Nu introduceti in lista numere negative!'
#     return (sum(marks)/len(marks)) # media

# num = [90, 93, 99, 89, -20]
# print(percentage(num))

# import copy

# l1=[1,3,[9,4],6,8]
# l2 = copy.deepcopy(l1) #Making a deep copy

# print('List 1 = ', l1)
# print('List 2 = ', l2)

# print('Performing change in list 2')
# l1[2][0] = 5

# print('List 1 = ',l1)
# print('List 2 = ',l2)

# print('Hello - ' * 5, end='')

# import time

# timp = time.asctime(time.localtime(time.time()))
# print(timp)

# import calendar

# cal = calendar.month(2023, 3)
# print(cal)

