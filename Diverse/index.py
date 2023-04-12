'''
arr = 'Eu sunt beniamin sferciuc!'
print(arr)
save = arr.split()
print(save)

x = 3.25;
print('x = %.2f' % x)

print('This is a number: ' + str(3))

lst = ['huawei', 'apple', 'samsung']

size = int(input("Introduceti dimensiunea vectorului: "))
print("Introduceti elemntele vectorului: ")

arr = [int(input('arr[' + str(i) + '] = ')) for i in range(size)]
print(*arr) # afiseaza vectorul fara paranteze patrate si virgula
'''

# despre matrice in python
#definire matrice
# row = 3
# col = 4
# mat = [0] * row
# for i in range(row):
#     mat[i] = [0] * col

# print(mat)
# for i in range(row):
#     print(*mat[i])

# #alt mod
# mat = [[1 for i in range(row)] for i in range(col)]
# print('Matrice (', row, ' x ', col, '):', sep='')
# for i in range(row):
#     print(*mat[i])

#citirea matricei de la tastatura
# Implementare profa
# declararea matricei si stabilirea numarului de randuri si coloane
# row = 3
# col = 3

# mat = [[1 for i in range(col)] for j in range(row)]
# print(*mat)
# #bucla pentru coloane
# for i in range(row):
#     mat[i] = [int(x) for x in input('Introduceti elementele de pe linia (' + str(i) + '): ').split()]
# # bucla pentru afisare
# for i in range(row):
#     print(*mat[i])

# r = 3
# c = 5

# mat = [7] * r
# print(mat)

# for i in range(r):
#     mat[i] = [7] * c

# print(mat)

# Implementarea mea
# row = int(input('Introduceti numarul de randuri: '))
# col = int(input('Introduceti numarul de coloane: '))

# main_list = []

# for i in range(row):
#     sec_list = []
#     for j in range(col):
#         element = int(input('Introduceti: '))
#         sec_list.append(element)
#     main_list.append(sec_list)

# print(main_list)

# sim_list = []
# size = int(input('Size: '))

# for i in range(size):
#     element = input("Elem. " + str(i) + ': ')
#     sim_list.append(element)

# print(sim_list)

# # Citirea listei de liste de la tastatură
# lista_principala = [list(map(str.strip, input().split())) for _ in range(int(input()))]

# # Afișarea listei de liste citite
# print("Lista de liste introdusa este: ", lista_principala)

# ___________________________________________________________________________________________________________________________________
# Tipuri de formate in Python (formate de siruri)
# # 1. String formatting cu operatorul %
# name = 'Beniamin'
# age = 21
# print('Numele meu este %s si am %d ani!' % (name, age))

# # 2. String formatting cu functia format() 
# print('Numele meu este {} si am {} ani!'.format(name, age))

# # 3. String formatting cu F-string
# print(f'Numele meu este {name} si am {age} ani!')

# # 4. String formatting cu siruri brute
# citat = r'This is a \n string!'
# print(citat)

# # 5. String formatting cu template-uri
# # from string import Template
# # str = Template("Numele meu este ${name} si am ${age} ani!")
# # mess = str.substitute(name = 'Beniamin', age = 21)
# # print(mess)

# # 6. String formatting cu str.format_map() - pentru dictionare
# detalii = {'name': 'Beniamin', 'age': 21}
# print("Numele meu este {name} si am {age} ani!".format_map(detalii))

# # 7. String formatting cu argumente numite
# print('Numele meu este {nume} si am {varsta} ani!'.format(nume = name, varsta = age))

# # 8. String formatting cu operatorul de concatenare
# print('Numele meu este ' + name + ' si am ' + str(age) + ' ani!')

# # 9. String formatting cu metoda join()
# mesaj = 'Numele meu este {0} si am {1} ani!'.format(name, age)
# print(' '.join(mesaj.split()))
# ___________________________________________________________________________________________________________________________________

# Prefixe pentru siruri formate
'''
1. r - prefixul pentru șiruri brute (raw strings) - acesta face ca caracterele speciale să fie ignorate și să fie considerate ca litere obișnuite.
2. u - prefixul pentru șiruri Unicode - acesta indică faptul că șirul trebuie interpretat ca fiind în format Unicode. In Python 3, nu mai este necesar.
3. b - prefixul pentru șiruri bytes - acesta indică faptul că șirul este format din octeți (bytes) și nu din caractere Unicode.
4. f - prefixul pentru șiruri formatate - acesta este utilizat pentru a formata șiruri în funcție de anumite valori.
5. fr
6. br
7. rb
'''

# Tuple/Enumerari
# tup = 1, 2, 3, 4
# tup1 = 6, 7
# tup_main = tup + tup1
# print(tup)
# print(tup_main[-2:])

# Functii:
# Sintaxa: 
# def nume_functie(parametru1, parametru2, ...)
#   bloc de instructiuni
#   return something

# Variabila globala: global <nume_variabila>

# glo_var = 'Python'

# def change_var():
#     '''Aceasta este o variabila globala acum si se va schimba din 'Python' in 'Java'''
#     global glo_var
#     glo_var = 'Java'

# change_var()
# print(glo_var)

# # Afisarea comentariilor din functie
# print(change_var.__doc__)

# # Functii cu un numar variabil de argumente '*'
# def suma(*operanzi):
#     s = 0
#     for x in operanzi:
#         if x == 0:
#             continue
#         s += 1/x
#     return s

# print(suma(1,0,4))

# Utilizarea unei functii din alt modul
# import random
# u = random.randint(1, 10)
# print('Zarul dv.: ', str(u))

# import random as rnd => inlocuieste random cu rnd
# import random as rnd
# pctUser = pctSys = 0

# while input('Arunc zarul? ').upper() == 'DA' or 'YES':
#     u = rnd.randint(1, 6)
#     print("Zarul dv.:", str(u))
#     c = rnd.randint(1, 6)
#     print('Al meu: ' + str(c))
#     if u > c:
#         print('Ati castigat!')
#         pctUser += 1
#     elif u < c:
#         print("Am castigat!")
#         pctSys += 1
#     else:
#         print("Egalitate!")
#     print('Scorul user-system:', pctUser, '-', pctSys)

# Expresii aritmetice post-fixate
#ramas la pagina 74

# import Learn

# if __name__ == '__main__':
#     Learn.something()
#     print('Apelat din index.py')
