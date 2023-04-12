# Ex. 1)
'''
x = input("x = ")
y = input("y = ")
print(x, y)
print(x*5, y*3)
print(x + y)
x = float(x)
y = float(y)
print("x = %f, y = %f, x ? y = %d" % (x, y, int(x)**int(y)))
print("%d" % (x/y))
print('%.2f' % (x/y))
x = int(input("x = "))
y = int(input("y = "))
print(x/y)
print(x//y)
'''

# Ex. 2)
'''
a = input("Primul sir: ")
b = input("Al doilea sir: ")
c = input("Al treilea sir: ")
c = c + '.'

print(a, b, c, sep='---')
'''

# Ex. 3)
'''
num = int(input("Introduceti un numar: "))
print(hex(num))
'''

# Ex. 4)
'''
x = int(input("x = "))
y = int(input('y = '))
print(x + y)

if x + y > 0:
    print("Suma este pozitiva!")
else:
    print("Suma este negativa!")
'''

# Ex. 5)
'''
num = int(input('Introduceti un numar oarecare: '))
if num < 100:
    print(hex(num))
else:
    print(oct(num))
'''

# Ex. 6) Ec. de gr. 1 - ax + b = 0
'''
a = int(input("Introduceti coeficientul lui a: "))
b = int(input("Introduceti coeficientul lui b: "))

if a == 0:
    print("Ecuatia nu exista!")
else:
    result = -b/a
    print('Solutia ecuatiei este: ' + str(result))
'''

# Ex. 6)
'''
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a < b < c:
    print("Valorile introduse sunt consecutive!", a, '<', b, '<', c)
else:
    print("Valorile introduse NU sunt consecutive!")
'''

# Ex. 7)
'''
num = int(input('Introduceti un numar intreg: '))
if num > 0:
    print('Numarul introdus este pozitiv!')
elif num == 0:
    print('Numarul introdus este 0!')
else:
    print('Numarul introdus este negativ!')
'''

# Ex. 8)
'''
import math

r = int(input('Introducei un numar real: '))
if r <= 0:
    print("Numarul este mai mic sau egal cu zero si nu poate fi raza unei sfere!")
else:
    aria = 4 * math.pi * r**2
    aria = round(aria, 2)
    print(f'Aria sferei este: {aria}')
    volume = (4/3)*math.pi*r**3
    volume = round(volume, 2)
    print('Volumul sferei este: ' + str(volume))
'''

# Ex. 9)
'''
a = int(input("Introduceti primul numar intreg: "))
b = int(input("Introduceti al doilea numar intreg: "))

print(f"Maximul este: {max(a, b)}")
'''

# Ex. 10)
'''
a = int(input("Introduceti un numar real: "))
x = int(input("Introduceti primul numar din interval: "))
y = int(input("Introduceti al doile numar din interval: "))

if x <= a <= y:
    print(f"Numarul introdus {a} apartine intervalului [{x}, {y}]")
elif x > y:
    print('Acesta nu este un interval!')
else: 
    print("Numarul nu se incadreaza in intervalul dat!")
'''

# Ex. 11) Ec. de gr. 2 - ax^2 + bx + c
'''
import math as m

a = int(input("Introduceti coeficientul lui a: "))
b = int(input("Introduceti coeficientul lui b: "))
c = int(input("Introduceti coeficientul lui c: "))

d = b**2 - 4*a*c

if a == 0:
    print('Ecuatia de gradul doi este posibila daca coeficientul lui a este diferit de 0.')
elif d == 0:
    print(f'x1 = x2 = {-b/2*a}')
elif d < 0:
    print("Solutiile sunt numere complexe.")
elif d > 0:
    x1 = (-b + m.sqrt(d))/2*a
    x2 = (-b - m.sqrt(d))/2*a
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
'''

# Ex. 12) 
'''
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
x = sorted([a, b, c])

print(f'Maximul este: {max(a, b, c)}')
print(f'Minimul este: {min(a, b, c)}')
print(f'Numerele sortate crescator: {x}')
'''

# Ex. 13)
'''
x = int(input("Coordonata x: "))
y = int(input("Coordonata y: "))

if x >= 0 and y >= 0:
    print(f'Coordonatele ({x}, {y}) apartin cadranului 1.')
elif x <= 0 and y >= 0:
    print(f'Coordonatele ({x}, {y}) apartin cadranului 2.')
elif x <= 0 and y <= 0:
    print(f'Coordonatele ({x}, {y}) apartin cadranului 3.')
elif x >= 0 and y <= 0:
    print(f'Coordonatele ({x}, {y}) apartin cadranului 4.')    
'''
