import heapq
import ast

# Tips 1: for...else
numbers = [2, 1, 6, 7, 10]
for number in numbers:
    if number % 2 == 1:
        print('Exista cel putin un numar impar!')
        break
else:
    print('Nu exista niciun numar impar!')

# Tips 2: Get elements from a list using variable
my_num = [1, 2, 3, 4, 5]
one, two, three, four, five = my_num
print(one)
print(two)
print(three)

# Tips 3: Get n largest or n smallest elements in a list using the module heapq
scores = [51, 33, 64, 87, 91, 75, 15, 49, 33, 82]
print(heapq.nlargest(3, scores))
print(heapq.nlargest(1, scores))

# Tips 4: Pass values from a list as method arguments
print(my_num)
print(*my_num)


def sum_elem(*arg):
    total = 0
    for i in arg:
        total += i
    return total


print(sum_elem(1, 2, 3, 4, 5))

# Tips 5: Get all the elements in the middle of the list
_, *elements_in_the_middle, _ = [1, 2, 3, 4, 5, 6, 7, 8]
print(elements_in_the_middle)
# or
first, second, *elem_in_the_middle, second_last, last = [1, 2, 3, 4, 5, 6, 7, 8]
print(elem_in_the_middle)

# Tips 6: Assign multiple variables in just one line
one, two, three = 1, 2, 3

# Tips 7: List comprehensions
even_num = [number for number in scores if number % 2 == 0]
print(even_num)
# or
dictionary = {'first_element': 1, 'second_element': 2,
              'third_element': 3, 'fourth_element': 4}
odd_value_elements = {key: num for (key, num) in
                      dictionary.items() if num % 2 == 1}
print(odd_value_elements)

# Tips 8: Repeat strings without looping
string = 'abc'
print(string * 3)

# Tips 9: Compare 3 numbers just like in Math
print(1 < 3 < 6)

# Tips 10: Merge dictionaries in a single readable line
first_dictionary = {'name': 'Fatos', 'location': 'Munich'}
second_dictionary = {'name': 'Drift', 'surname': 'Morina',
                     'location': 'Bavaria, Munich'}
result = first_dictionary | second_dictionary
print(result)


# Tips 11: Convert a string into a list of strings


def string_to_list(string):
    return ast.literal_eval(string)


str_ls = string_to_list('[1, 2, 3, 4, 5]')
print(type(str_ls))


# Tips 12: Avoid “trivial” mistakes by using named parameters
def subtract(a, b):
    return a - b


print((subtract(a=1, b=3)))  # -2
print((subtract(b=3, a=1)))  # -2

# Tips 13: Print multiple values with a custom separator in between each value
print("29", "01", "2022", sep="/")  # 29/01/2022
print("name", "domain.com", sep="@")  # name@domain.com

# Tips 14: You can separate big numbers with the underscore
print(1_000_000_000)

# Tips 15: Reverse slicing
my_string = 'Eu sunt fiul dreptei!'
print(my_string[10:0:-1])
print(my_string[::-1])
print(my_string[:5])
print(my_string[5:])

# Tips 16:  Merge 2 dictionaries quickly
dictionary_one = {"a": 1, "b": 2}
dictionary_two = {"c": 3, "d": 4}
merged = {**dictionary_one, **dictionary_two}
print(merged)

# Tips 17: Find the largest word in a list
my_string = ['aklfhd', 'adsghfadg', 'ladfkh', 'vzvcx']
print(max(my_string, key=len))


# Tips 18: Check whether 2 strings are anagrams using sorted()


def check_if_anagram(first_word, second_word):
    first_word = first_word.lower()
    second_word = second_word.lower()
    return sorted(first_word) == sorted(second_word)


print(check_if_anagram("testinG", "Testing"))  # True
print(check_if_anagram("Here", "Rehe"))  # True
print(check_if_anagram("Know", "Now"))  # False

# Tips 19: Get the value of a character in Unicode
print(ord('A'))

# Tips 20: Swap keys and values of a dictionary
dictionary = {"a": 1, "b": 2, "c": 3}
swap_dic = {value: key for key, value in dictionary.items()}
print(swap_dic)

# Tips 21: Lambda functions can only be in one line
comparison = lambda x: x > 3
print(comparison(4))


# Tips 21: super()
class Parent:
    def __init__(self, city, address):
        self.city = city
        self.address = address


class Child(Parent):
    def __init__(self, city, address, university):
        super().__init__(city, address)
        self.university = university


child = Child('Zürich', 'Rämistrasse 101', 'ETH Zürich')
print(child.university)
print(child.city)
print(child.address)

parent = Parent('Falticeni', 'Slt. Grigoras 5')
print(parent.city)
print(parent.address)

# Tips 22: Find number of space
my_string = 'fdslkf adsf ladsf dslf ads f'
print(my_string.count('\x20'))


# Tips 23: Condition inside the print function


def is_positive(number):
    print("Positive" if number > 0 else "Negative")  # Positive


is_positive(-3)
is_positive(5)

# Tips 24: global
string = 'string'


def do_nothing():
    global string
    string = 'inside a method'


do_nothing()
print(string)

# Tips 24: Count the number of elements in a string or list using Counter from “collections”
from collections import Counter

result = Counter('Banana')
for key, value in result.items():
    print(f'{key} - {value} aparitii')
# or
test_list = ['Banana', 'Apple', 'Banana', 'Ananas', 'Kiwi', 'Apple', 'Apple', 'Banana', 'Kiwi']
result_counter = Counter(test_list)
print(result_counter.most_common())

# Tips 25: Find the most frequent element in a list in just one line
my_list = ['1', 1, 0, 'a', 'b', 2, 'a', 'c', 'a', 1 , 1, 'a']

print(max(set(my_list), key=my_list.count))

# Tips 26: Default keys in dictionary
from collections import defaultdict

my_dictonary = defaultdict(str)
my_dictonary['name'] = "Name"
my_dictonary['surname'] = "Surname"

print(my_dictonary)


# Tips 27: Remove duplicates
ls = [1, 2, 1, 2, 3, 4, 5]
my_set = set(ls)
print(list(my_set))

# Tips 28: setdefault method
print()
import pprint as p
text = 'This is a random text for a test function pprint.'
counts = {}
for word in text.split():
    counts.setdefault(word, 0)
    counts[word] += 1

p.pprint(counts)

dic_ls = list(counts.items())
# list_list = [list(tup) for tup in dic_ls] sau
list_list = map(list, dic_ls)

print(list(list_list))

# Tips 29: Multiple variables
a = [1, 2, 3, 4, 5]
*x, y, z = a
print(x)
print(y)
print(z)

# Tips 30: fractions
from fractions import Fraction

print(float(Fraction(1, 2) + Fraction(4, 1)))


# Tips 31: Functii (*args, *kwargs), valoare impicita
# Argumentele arbitrare sunt adesea scurtate la *args în documentațiile Python. (*)
# Expresia Argumentele cuvintelor cheie este adesea scurtată la kwargs în documentațiile Python. (**)

def average(*args):
    total = 0
    count = 0
    for num in args:
        total += num
        count += 1 # echivalent cu len(args)
    return total/count

print(average(1,2,3,4,5,6,7,8,9,10))

def country(country1, country2, country3):
    return 'This is ' + country2

print(country(country3 = 12, country1 = 23, country2 = 'Olanda'))

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = 'Beniamin', lname = "Refsnes")

# Valoarea implicita 
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Tips 31:
import json

x = '{"name":"John", "age":30, "city":"New York"}'

y = json.loads(x)
print(type(y))

js = json.dumps(y)
print(type(js))

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4))