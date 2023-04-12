# Ex. 1)
'''
n = int(input('Introduceti o valoare pentru n: '))
for i in range(n):
    print(i, end=' ')
'''

# Ex. 2)
'''
# a)
n = int(input('Introduceti o valoare pentru n: '))
for i in range(n):
    print(n - i, end=' ')
print()

# b)
for i in range(1, n + 1, 2):
    print(i, end=' ')
print()

# c)
import math
print(f'Factorialul: {math.factorial(n)}')

# d)
x = int(input("Introduceti un numar: "))
sum = 0
for i in range(1, n + 1):
    if i % x == 0:
        sum += i
print(sum)
'''

# Ex. 3)
'''
num = int(input("Introduceti un numar natural: "))
aux = num
sum = 0

while num > 0:
    last = num % 10
    sum += last
    num = num // 10

print(f'Suma cifrelor numarului {aux} = {int(sum)}')
'''

# Ex. 4)
'''
for i in range(7):
    print('*' * i)
for i in range(6):
    print('*' * (5 - i) )
'''

# Ex. 5) 
'''
x = input("Introduceti un numar oarecare: ")
n = input("Introduceti numarul de termeni: ")
sum = 0
result = ''

for i in range(1, (int(n) + 1)):
    sum = sum + int(x*i)
    result = result + x * i + ' + '

result = result.rstrip('+ ')
print(f'{result} = {sum}')
'''

# Ex. 6) 
'''
num = int(input("x = "))
sum = 0

while num != 0:
    sum += num
    num = int(input("x = ")) 

print(f'Suma numerelor introduse este: {sum}')
'''

# Ex. 7)
'''
x = input('Introduceti un numar oarecare: ')
print(x[::-1])
'''

# Ex. 8)
'''
x = 1
while x <= 10:
    print(f'3*{x}^2-7*{x}-10 = {3*(x**2) - 7*x - 10}')
    x += 1
'''

# Ex. 9)
'''
while True:
    option = input("Introduceti o optiune: ").upper()
    match option:
        case 'C':
            x = int(input("Introduceti un numar intreg: "))
            y = int(input("Introduceti un numar intreg: "))
        case '+':
            print(x + y)
        case '-':
            print(x - y)
        case '*':
            print(x * y)
        case '/':
            print(x / y)
        case 'X':
            exit("EndofSoftware!")
'''
