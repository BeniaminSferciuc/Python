# afisare in consola
# sintaxa
# print(object(s), sep=separator, end=end, file=file, flush=flush)
print("Eu sunt fiul dreptei.", end=' ')
print('Adica Beniamin!')
a = 2
b = 'euro'
print(a, b)

# citirea de la tastatura
# input('prompt)
# prompt - reprezinta un mesaj inainte de input
username = input('Introduceti numele dvs.: ')
print(username)

# Variabile. Tipuri de date
# ! Variabilele nu se declara
# Numar complex
z = 4j
print(type(z))

# Conversii de tip - cast int/float/str(variable)
store = input('Introduceti un numar intreg: ')
c = int(store) + 5
print("Rezultatul este: ", c)

# Operatori aritmetici
'''
+ adunare
- scadere
* inmultire
/ impartire
% restul impartirii
** putere
// Floor division
'''

# Operatori de atribuire
'''
=   x = 5       x = 5
+=  x += 3      x = x + 3
-=  x -= 3      x = x - 3
*=  x *= 3      x = x * 3
/=  x /= 3      x = x / 3
%=  x %= 3      x = x % 3
**= x **= 3     x = x ** 3
//= x //= 3     x = x // 3
&=  x &= 3      x = x & 3
|=  x |= 3      x = x | 3
^=  x ^= 3      x = x ^ 3
>>= x >>= 3     x = x >> 3
<<= x <<= 3     x = x << 3
'''

# Operatori - atrinuirea multipla
a, b = 10, 20
print(a)
print(b)

# Interschimbarea a doua variabile intre ele se poate face
a, b = b, a 
print('a = ', a, 'b = ', b)

# Operatori comparare
'''
==  egal
!=  diferit
>   mai mare
<   mai mic
>=  mare mare sau egal
<=  mai mic sau egal
'''

# Operatori logici
'''
and     returneaza true daca ambele instructiuni sunt adevarate
or      returneaza true daca una din instructiuni este adevarata
not     inverseaza rezultatul
'''

a = 2
b = 2
c = 1
d = 2

if a == d and c == b:
    print("true")
else:
    print("false")

if a == d or c == b:
    print("true")
else:
    print("false")

# Alti operatori: identitate
'''
is          returneaza true daca ambele variabile sunt acelasi obiect
is not      returneaza true daca ambele variabile nu sunt acelasi obiect
'''

x = 2
y = 3

print(x is not y)   #returneaza true
print(x is y)       #returneaza false

# Alti operatori: apartenenta
'''
in          Returns True if a sequence with the specified value is present in the object
not in      Returns True if a sequence with the specified value is not present in the object
'''

# Operatori pe biti
'''
&   AND
|   OR
^   XOR
~   NOT
<<  left shift
>>  right shift
'''

# Despre blocuri (de instructiuni)
# !!! toate instrucțiunile identate la același nivel aparțin aceluiași bloc

# Structuri de control
'''
if ... else 
for
while
'''

# if ... else
'''
Sintaxa
if expression:
    statements
else:
    statements

    sau

if expression1:
    statements
elif expression2:
    statements
elif expression2:
    statements 
else:
    statements
'''

a = 10
b = 10

if a > b:
    print("a este mai mare decat b")
elif a < b:
    print("a este mai mic decat b")
else:
    print("a este egal cu b")

# for

for i in range(5):
    print(i, end=' ')
print(end='\n')
# Funcția range(stop) sau range(start, stop [,step])
for i in range(0, 100, 2):
    print(i, end=' ')
print(end='\n')

for i in range(0, 11):
    if(i % 2 is 0):
        print(i, "is par")
        continue
    else:
        print(i, "is impar")

# while
'''
Sintaxa: while conditie:
            bloc de instructiuni
'''
i = 0;

while i < 10:
    print("Eu sunt fiul dreptei!")
    i += 1  # !Nu exista i++ in python


# Siruri de caractere
a = 'Hello, world!'
# Extragerea unui caracter dintr-un sir
print(a[1]) # --> afiseaza pe 'e' din Hello

for i in range(13):
    print(a[i], end='')

print(end='\n')
# Extragerea unui subsir dintr-un sir
print(a[7:13]) # --> afiseaza 'world' din variabila a

# Eliminarea spatiilor dintr-un sir de la inceput sau de la sfarsit
a = "  Hello, world! "
print(a)            # --> Nu elimina spatiile
print(a.strip())    # --> functia strip() elimina spatiile de inceputul si sfarisitul unui subsir

# Lungimea unui sir
print("Lungimea sirului este: ", len(a)) # --> 16 caractere (cu tot cu spatii)

# Transformarea in minuscule
b = "Beniamin Sferciuc!"
print(b.lower()) # --> result: beniamin sferiuc
# Transformarea in masjuscule
print(b.upper()) # --> result: BENIAMIN SFERCIUC

# Impartirea in subsiruri
print(b.split(' '))

# Formatarea sirurilor
x = 3.25
print("x = %f" % x)

string = "Benjamin Sferciuc"
print("s = %s!" % string)

sir = "n = %d n/2 = %f n/3 = %.3f" % (14, 14/2, 14/3)
print(sir)

# ! Important
print('Hello - ' * 10) # --> multiplica 'Hello -' de 10 ori


