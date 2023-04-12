# Important functions in Python

'''
1. abs()	          Returns the absolute value of a number
2. all()	          Returns True if all items in an iterable object are true
3. any()	          Returns True if any item in an iterable object is true
4. ascii()	        Returns a readable version of an object. Replaces none-ascii characters with escape character
5. bin()            Returns the binary version of a number
6. bool()	          Returns the boolean value of the specified object
7. bytearray()	    Returns an array of bytes
8. bytes()	        Returns a bytes object
9. callable()	      Returns True if the specified object is callable, otherwise False
10. chr()	          Returns a character from the specified Unicode code.
11. classmethod()   Converts a method into a class method
12. compile()	      Returns the specified source as an object, ready to be executed
13. complex()	      Returns a complex number
14. delattr()	      Deletes the specified attribute (property or method) from the specified object
15. dict()	        Returns a dictionary (Array)
16. dir()	          Returns a list of the specified object's properties and methods
17. divmod()	      Returns the quotient and the remainder when argument1 is divided by argument2
18. enumerate()	    Takes a collection (e.g. a tuple) and returns it as an enumerate object
19. eval()	        Evaluates and executes an expression
20. exec()	        Executes the specified code (or object)
21. filter()	      Use a filter function to exclude items in an iterable object
22. float()	        Returns a floating point number
23. format()	      Formats a specified value
24. frozenset()	    Returns a frozenset object
25. getattr()	      Returns the value of the specified attribute (property or method)
26. globals()	      Returns the current global symbol table as a dictionary
27. hasattr()	      Returns True if the specified object has the specified 28. attribute (property/method)
29. hash()	        Returns the hash value of a specified object
30. help()	        Executes the built-in help system
31. hex()	          Converts a number into a hexadecimal value
32. id()	          Returns the id of an object
33. input()	        Allowing user input
34. int()	          Returns an integer number
35. isinstance()    Returns True if a specified object is an instance of a specified object
36. issubclass()    Returns True if a specified class is a subclass of a specified object
37. iter()	        Returns an iterator object
38. len()	          Returns the length of an object
39. list()	        Returns a list
40. locals()	      Returns an updated dictionary of the current local symbol table
41. map()	          Returns the specified iterator with the specified function applied to each item
42. max()	          Returns the largest item in an iterable
43. memoryview()    Returns a memory view object
44. min()	          Returns the smallest item in an iterable
45. next()	        Returns the next item in an iterable
46. object()	      Returns a new object
47. oct()	          Converts a number into an octal
48. open()	        Opens a file and returns a file object
49. ord()	          Convert an integer representing the Unicode of the specified character
50. pow()	          Returns the value of x to the power of y
51. print()	        Prints to the standard output device
52. property()	    Gets, sets, deletes a property
53. range()	        Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
54. repr()	        Returns a readable version of an object
55. reversed()	    Returns a reversed iterator
56. round()	        Rounds a numbers
57. set()	          Returns a new set object
58. setattr()	      Sets an attribute (property/method) of an object
59. slice()	        Returns a slice object
60. sorted()	      Returns a sorted list
61. staticmethod()  Converts a method into a static method
62. str()	          Returns a string object
63. sum()	          Sums the items of an iterator
64. super()	        Returns an object that represents the parent class
65. tuple()	        Returns a tuple
66. type()	        Returns the type of an object
67. vars()	        Returns the __dict__ property of an object
68. zip()	          Returns an iterator, from two or more iterators
'''
'''
# 1. abs(value)
num = -23.4;
print(f'abs({num}) = {abs(num)}')

# 2. all(iterable)
all_list = [2, 1, 1]
print(f'all({all_list}) = {all(all_list)}')

# 3. any(iterable)
any_list = [0, 0, 1]
print(f'any({any_list}) = {any(any_list)}')

# 4. ascii(object)
string = "aă"
print(f'ascii(aă) = {ascii(string)}')

# 5. bin(value) - from binary
print(f"bin(255) = {bin(255).strip('0b')}")

# 6. bool(object)
print(f'bool(183) = {bool(183)}')

# 7. bytearray(x, encoding, error)
print(f'bytearray(4) = {bytearray(4)}')

# 8. bytes(x, encoding, error)
print(f'bytes(4) = {bytes(4)}')

# 9. callable(object)
def num():
    a = 5
print(f'callable(num) = {callable(num)}')

# 10. chr(value)
print(f'chr(65) = {chr(65)}')

# 11. classmethod()

# 12. compile(source, filname, mode, flag, dont_inherit, optimize)
x = compile('print(55)', 'test', 'eval')
exec(x)

# 13. complex(real, imaginary)
print(f'complex(2, 8) = {complex(2, 8)}')

# 14. delattr(object, attribute)
class Person:
    name = 'Beniamin'
    age ='21'
    county = 'Romania'

delattr(Person, 'age')

# 15. dict(keyword arguments)
print(dict(name = 'Beniamin', age ='21', county = 'Romania'))

# 16. dir(object)
# print(dir(Person))

# 17. divmod(dividend, divisor)
print(f'divmod(19, 3) = {divmod(19, 3)}')

# 18. enumerate(iterable, start)
my_list = ['Apple', 'Samsung', 'Huawei']
y = enumerate(my_list, 10)
print(list(y))

# 19. eval(expression, globals, locals)
x = 'print(55)'
eval(x)

# 20. exec(expression, globals, locals)
x = 'name = "John"\nprint(name)'
exec(x)

# 21. filter(function, iterable)
ages = [13,9,28,5,7,3,18]

def small(x):
    if x < 10:
        return True
    
chids = filter(small, ages)
for i in chids:
    print(i , end=', ')

# 22. float(value)
print(float(3))

# 23. format(value, format***)
print(format(34, 'b'))

# 24. frozenset()
ages = [13,9,28,5,7,3,18]
x = frozenset(ages)

# 25. getattr(iterable)
class Person:
    name = 'Beniamin'
    age ='21'
    county = 'Romania'

print(getattr(Person, 'age'))

# 26. globals()
x = globals()
# print(x)

# 27. hasattr(iterable)
print(hasattr(Person, 'age'))

# 28. hash()

# 29. help()

# 30. hex(value)
print(hex(15))

# 31. id()
a = 3.2
print(id(a))

# 32. input()

#@ 33. int(value, base)
print(int(a))

# 34. isinstance(object, type)
print(isinstance(a, int))

# 35. issubclass(object, subclass)
class myAge:
  age = 36

class myObj(myAge):
  name = "John"
  age = myAge

x = issubclass(myObj, myAge)
print(x)

# 36. iter(object, sentinel) and next(iterable, default)
x = iter([1,23,3])
print(next(x))
print(next(x))
print(next(x))
print(next(x, '10') )

# 37. len()
x = [1,2,3,4]
print(len(x))

# 38. list(iterable)
a = "apple"
b = 'samsung'
c = 'huawei'

my_list = list((a,b,c))
print(my_list)

# 38. locals()
x = locals() 
# print(x["__file__"])

# 39. map(function, iterables)
def my_len(n):
   return len(n)

x = map(my_len, my_list)
print(list(x))

# 40. max(n1, n2, n3, ...) or max(iterable)
arr = [9,13,2,87,5,32,4]
print(max(arr))

# 41. memoryview(object)
p = memoryview(b"Hello")
print(p)
print(p[0])

# 42. min(n1, n2, n3, ...) or min(iterable)
print(min(arr))

# 43. object()
x = object()
print(type(x))

# 44. oct(int)
print(oct(123))

# 45. open(file, mode) mode: 'r', 'a', 'w', 'x', 't', 'b'
f = open("readme.txt", 'r')
print(f.read())

# 46. ord(character)
print(ord('a'))
'''
# 47. pow(base, exponent, [modulus])
print(pow(2, 3, 3)) # same as: ((2*2*2)%5) 

# 48. print(object, sep=separator, end=end, file=file, flush=flush)

# 49. property()

# 50. range(start, stop, step)
x = range(3, 20, 2)
for n in x:
  print(n)

# 51. repr()

# 52. reversed(sequence)
alph = ["a", "b", "c", "d"]
rev = reversed(alph)
print(list(rev))

# 53. round(number, digits)
print(round(3.1324, 2))
print(round(5.23))

# 54. set(iterable)
x = set(('apple', 'banana', 'cherry'))
print(x)

# 55. setattr(object, attribute, value)
class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)
x = getattr(Person, 'age')
print(x)

# 56. slice(start, end, step)
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])

# 57. sorted(iterable, key=key, reverse=reverse)
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a, reverse=True)
print(x)

# 58. staticmethod()

# 59. str(object, encoding=encoding, errors=errors)
print(str(3.5))

# 60. sum(iterable, start)
a = (1, 2, 3, 4, 5)
print(sum(a))

# 61. super()

# 62. tuple(iterable)
x = tuple(('apple', 'banana', 'cherry'))
print(x)

# 63. type(object, bases, dict)
print(type(x))

# 64. vars(object)
class Person:
  name = "John"
  age = 36
  country = "norway"

# x = vars(Person)

print(x)

# 64. zip(iterator1, iterator2, iterator3, ...)
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(list(x))