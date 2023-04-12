# List Methods 
'''
1. append()	- Adds an element at the end of the list
2. clear() -  Removes all the elements from the list
3. copy()  -  Returns a copy of the list
4. count()	- Returns the number of elements with the specified value
5. extend()	- Add the elements of a list (or any iterable), to the end of the current list
5. index() -  Returns the index of the first element with the specified value
6. insert()	- Adds an element at the specified position
7. pop()  -   Removes the element at the specified position
8. remove()	- Removes the first item with the specified value
9. reverse() -Reverses the order of the list
10. sort()  - Sorts the list
'''

my_list = ['Valentin', 'Beniamin', 'Ramona', 'Sara', 'Rebeca']

print(*my_list, sep=', ')
my_list.append('Gabriel')
print(*my_list, sep=', ')
new_list = my_list.copy()
print(*new_list, sep=', ')
print(my_list.count('Sara'))

rest_list = ['Catalin', 'Florin', 'Estera']
my_list.extend(rest_list)
print(*my_list, sep=', ')

print(my_list.index('Catalin'))

my_list.insert(0, 'Maria')
my_list.insert(len(my_list), 'Constantin')
print(my_list)

my_list.pop(10)
print(my_list)

my_list.remove('Maria')
print(my_list)

my_list.reverse()
print(my_list)

my_list.sort(reverse=True)
print(my_list)