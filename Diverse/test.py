# # import random
# # mat = []
# # for i in range(3):
# #     rand = []
# #     for j in range(3):
# #         rand.append(random.randrange(0, 10))
# #     mat.append(rand)

# # print(mat)

# # for i in mat:
# #     x = int(input('Nr: '))
# #     i.append(x)

# # print(mat)


# # my_list = [1, 2, 3]
# # my_string = ''.join(map(str, my_list))
# # print(my_string)


# # import itertools as i
# # list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # new_list = list(i.chain(*list_of_lists))
# # print(new_list)

# my_string = 'Beniamin'
# new_string = ''
# for i in my_string:
#     new_string += i + '-'

# print(new_string.rstrip('-'))

# # sau 

# my_string = 'Beniamin'
# sep = '-'
# print(sep.join(my_string))

# test = [1,9,3,2,8,5,6,2,2]
# print(max(set(test), key = test.count))

# lista = ['abc', 'xy', 'lmnop', 'z']
# maxim = max(lista, key=len)
# print(maxim)

# x, y = input('dati numarul de linii si de coloane: ').split()

# mat = []
# for i in range(int(x)):
#     rand = input(f'Linia {i}: ').split()
#     mat.append(rand)

# print(mat)
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}  

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

thisdict["year"] = "2000"
print(thisdict)

thisdict.update({'model': 'Focus'})
print(thisdict)

for key in thisdict:
    print(thisdict[key])


a, b = 200, 300
if a > b:
    pass
"""

import re

my_str = 'lorem ipsum dolor sit, amet consectetur adipisicing elit. molestiae, sint architecto officia laudantium delectus voluptatibus fugit ut in, quae sequi quaerat possimus aspernatur doloremque, error quibusdam rerum cumque porro fugiat!'

print(my_str.title())

# import camelcase as c

# camel = c.CamelCase()
# print(camel.hump(my_str))


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
    
      
