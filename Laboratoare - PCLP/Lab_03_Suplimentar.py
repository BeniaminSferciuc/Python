# Ex.1)
'''
def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def combinator(n, m):
    result = factorial(n)/(factorial(m) * factorial((n - m)))
    return result

n = 10
m = 5

result = combinator(n, m)
print(result)
'''

# Ex. 2)
'''
def convert_bin(n):
    result = ''
    while n > 0:
        result = result + str(n % 2)
        n //= 2
    return result

bin = convert_bin(15)
print(bin[::-1])
'''

# Ex. 3)


# a) Patrate perfecte
'''
from math import isqrt
def find_all_square(a, b):
    result = []
    if a > b:
        for i in range(b, a + 1):
            if isqrt(i)**2 == i:
                result.append(i)
    else:
        for i in range(a, b + 1):
            if isqrt(i)**2 == i:
                result.append(i)
    return result
                
# b) Numere prime


from sympy import isprime

def prime(n, m):
    my_prime = []
    if n > m:
        for i in range(m, n + 1):
            if isprime(i):
                my_prime.append(i)
    else:
        for i in range(n, m + 1):
            if isprime(i):
                my_prime.append(i)
    return my_prime

# c) numere care se divid cu n si m
def interval(n, m):
    n_list = []
    m_list = []

    for i in range(1000, 10000):
        if i % n == 0:
            n_list.append(i)
        if i % m == 0:
            m_list.append(i)
        result = n_list + m_list
    return result

# d) c.m.m.d.c - algoritmul euclid
def cmmdc(n, m):
    if n % m == 0:
        print(f'{m} este cel mai mare divizor comun')
    else:
        r = n % m          
        while r > 0:
            n = m     
            m = r       
            r = n % m   
    return m

# alternativ 
# from math import gcd
# print(gcd(24, 12))

print("1.\tCitire + afisare")
print("2.\tPatrate perfecte")
print("3.\tNumere prime")
print("4.\tNumere divizibile")
print("5.\tCmmdc")
print("6.\tExit")

import sys
while True:
    choice = int(input("Alegeti: "))
    match choice:
        case 1:
            n = int(input('n = '))
            m = int(input('m = '))
            print(f'Numerele introduse sunt: {n}, {m}')
        case 2:
            print(find_all_square(n, m))
        case 3:
            print(prime(n, m))
        case 4:
            print(interval(n, m))
        case 5: 
            print(cmmdc(n, m))
        case 6:
            sys.exit("Sfarsit!")
'''

# Ex. 4)
'''
n = int(input('Introduceti un numar din intervalul [20, 50): '))
while n < 20 or n >= 50:
    n = int(input('Introduceti un numar din intervalul [20, 50): '))

S1 = 0
S2 = 0

for i in range(1, n):
    if i % 2 == 0:
        S2 = S2 - i
    else:
        S1 = S1 + i

print(f'Total: {S1 + S2}')
'''

# Ex. 5)
'''
x = input("Introduceti un numar integ: ")
rez = list(x)
print(max(rez))
'''

# Ex. 6)
'''
n = input("Introduceti un numar integ: ")
my_digits_str = list(n)

my_digits = [int(digit) for digit in my_digits_str]

par = 0
c_par = 0
impar = 1
c_impar = 0

for i in range(len(my_digits)):
    if my_digits[i] % 2 == 0:
        par += my_digits[i]
        c_par += 1
    else:
        impar *= my_digits[i]
        c_impar += 1

total_par = par/c_par
total_par = round(total_par, 2)

print(f'Media aritmetica a numerelor pare este {total_par}')
print(f'Produsul numerelor impare este {round(impar/c_impar, 2)}')
'''

# Ex. 7)
'''
n = int(input("Introduceti un numar integ: "))
div = []
for i in range(1, n + 1):
    if n % i == 0:
        div.append(i)

div.pop()

if sum(div) == n:
    print("Este numar perfect!")
else:
    print('Nu este numar perfect')
'''

# Ex. 8)
'''
n = int(input("Introduceti un numar natural nenul: "))
suma = 0
produs = 1

for i in range(1, n+1):
    produs *= i
    suma += produs

print("Suma este:", suma)
'''
# Ex. 9)

n = int(input("Introduceti un numar natural nenul: "))
suma = 0
produs = 1

for i in range(1, n+1):
    produs *= i
    termen = 1/produs
    suma += termen

print("Suma este:", suma)

