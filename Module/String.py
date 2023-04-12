# String Methods
#-------------------------------------------------------
'''
Metode utile:
1. capitalize() | casefold() | swapcase() | title() | lower() | upper()
3. center()
4. count()
5. startswith() and endswith()
6. index() or find()
7. isalnum()
8. isalpha()
9. isdigit() and isnumeric()
10. isidentifier()
11. islower() and isupper()
12. isspace()
13. istitle() 
14. join()
15. ljust() and rjust()
16. lstrip() and rstrip() and strip()
17. replace()
18. partition()
19. split() and rsplit()
20. splitlines()
21. zfill()
'''
#-------------------------------------------------------
'''
# 1. capitalize()
my_string = 'beniamin sferciuc'
print('capitalize: ' + my_string.capitalize())

# 2. casefold()
case_string = 'Beniamin Sferciuc Este Fiul Dreptei.'
print('casefold: ' + case_string.casefold())

# 3. center(length, character)
print('center: ' + my_string.center(50, '*'))

# 4. count(value, start, end)
print('count: ' + str(my_string.count('i')))

# 5. decode

# 6. encode(ecoding = default UTF-8, errors = 'backslashreplace', 'ignore', 'namereplace', 'strict', 'replace', 'xmlcharrefereplace') 
print('encode: ' + str(my_string.encode(encoding = 'UTF-8'), errors = 'namereplace'))

# 7. endswith(value, start_position, end_position)
print('endswith: ' + str(my_string.endswith('sferciuc')))

# 8. expandtabs(tabsize)
my_new_string = 'Beniamin\tSferciuc!'
print('expandtabs: ' + my_new_string.expandtabs(10))

# 9. find(value, start, end)
print('find:', my_string.find('sferciuc'))

# 10. format(value1, value2...)
age = 21
name = 'Dr. Drift'

text = "My name is {0}, I'm {1}.".format('John', 36)
print(text)

# 11. format_map()

# 12. index(value, start, end) like find() like rindex()

# 13. isalnum()
print(my_string.isalnum())

# 14. isalpha()
print(my_string.isalpha())

# 15. isascii()
print(my_string.isascii())

# 16. isdecimal()
print(my_string.isdecimal())

# 17. isdigit()
print(my_string.isdigit())

# 18. isidentifier()
print(my_string.isidentifier())

# 19. islower()
print(my_string.islower())

# 20. isnumeric()
print(my_string.isnumeric())

# 21. isprintable()
print(my_string.isprintable())

# 22. isspace()
print(my_string.isspace())

# 23. istitle()
print(my_string.istitle())

# 24. isupper()
print(my_string.isupper())

# 24. separator.join(iterable)
array = ['John', 'Peter', 'Vicky']
print('-'.join(array))

# 25. ljust(lenght, caracter) # same as rjust
x = 'BMW'
print(x.ljust(20, '-'))

# 26. lower()
print(x.lower())

# 27. lstrip(characters) same rstrip()
y = '****Beniamin****'
print(y.lstrip('*'))

# 28. maketrans(x, y, z)
txt = 'Beniamin Sferciuc!'
mytable = str.maketrans("S", "C")
print(txt.translate(mytable))

# 29. partition(value) and rpartition()
text = 'Eu sunt fiul dreptei!'
print(text.partition('dreptei!'))

# 30. replace(old new, count)
print(text.replace('fiul', 'omul' , 1))

# 31. rfing(value, start, end)
string = "Mi casa, su casa. casa in casa."
print(string.rfind('casa'))

# 31. rsplit(separator, maxsplit) same split() and lsplit()
print(string.rsplit(',', 1))

# 32. splitlines(optinal_True)
my_text = 'This is a random\ntext used\n for a test function call splitlines()'
print(my_text.splitlines())

# 33. startwith(value)
print(my_text.startswith('This'))

# 34. swapcase()
random_text = 'AbCdEfGhIjKlM'
print(random_text.swapcase())

# 35. title()
simple_text = 'introducere in javascript'
print(simple_text.title())

# 36. translate()
my_dict = {83: 80}
txt = "Hello Sam!"
print(txt.translate(my_dict))

# 37. upper()
print(simple_text.upper())

# 38. zfill()
print('5000'.zfill(10))
'''