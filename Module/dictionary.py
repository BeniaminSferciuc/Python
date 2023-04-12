# Dictionary Methods

'''
1. clear()          Removes all the elements from the dictionary
2. copy()	        Returns a copy of the dictionary
3. fromkeys()	    Returns a dictionary with the specified keys and value
4. get()	        Returns the value of the specified key
5. items()     	    Returns a list containing a tuple for each key value pair
6. keys()	        Returns a list containing the dictionary's keys
7. pop()	        Removes the element with the specified key
8. popitem()	    Removes the last inserted key-value pair
9. setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
10. update()	    Updates the dictionary with the specified key-value pairs
11. values()	    Returns a list of all the values in the dictionary
'''

# 1. clear()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# car.clear()
print(car)

# 2. copy()
new_car = car.copy()
print(new_car)

# 3. fromkeys()
y = 0
thisdict = dict.fromkeys(new_car, y)
print(thisdict)

# 4. get(keyname, value)
x = car.get('model')
print(x) 

# 5. items()
x = car.items()
print(x)

# 6. keys()
x = car.keys()
print(x)

# 7. pop(keyname, defaultvalue)
x = car.pop('model') 
print(x)
print(car)

# 8. popitem()
car.popitem()
print(car)

# 9. setdefault(keyname, value)
x = car.setdefault('model', 'Bronco')
print(car)

# 10. update(iterable)
car.update({'color': "white"})
print(car)

# 11. values()
print(car.values())