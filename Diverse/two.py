# Vectori

'''
1. Liste - colectie ordonata si mutabila
2. Tuple - colectie ordonata si imutabila
3. Multimi - colectie neordonata si neindexata
4. Dictionare - colectie neordonata, indexata si mutabila
'''

# # despre liste
# arr = [1, 3, 5, 6]
# print(arr);
# print("New line: ")

# for i in range(1, len(arr)):
#     print(arr[i])

# lst = [{1, 2}, 'abc', 2, ['1.1', '2.6']]
# print(lst)

# for i in range(len(lst)):
#     print(lst[i])

# fruit_list = ['apple', 'banana', 'strawberry']
# # Afisarea tuturor elementelor din vectorul de tip lista
# print(fruit_list)
# # Afisarea unui singur element din lista
# print(fruit_list[0])
# # Modificarea unui element din lista
# fruit_list[1] = "mango"
# print(fruit_list)
# # Manipularea listei folosind bucle (for)
# print("After for: ")
# for i in fruit_list:
#     print(i)

# search = 19

# # Cautarea unui element
# main_list = [1, 2, 3, 4, 5, 6, 7, 8]
# if search in main_list:
#     print("2 is in main_list: true")
# else:
#     print("Doesn't exist in main_list: %d" % search)

# # Dimensiunea unei liste
# print("Dimensiunea liste: ", len(main_list))

# # Adaugarea unui element in lista cu append() si insert()
# company_list = ['apple', 'samsung', 'Nokia', 'IBM']
# print('Before append: ', company_list)
# # folosind append
# company_list.append("Huawei")
# print('After append: ', company_list)

# # folosind insert
# company_list.insert(0, "Facebook")
# print("After insert: ", company_list)

# # Stergerea unui element din lista cu remove() si pop()
# # folosind remove
# company_list.remove("apple")
# print(company_list)
# # folosind pop - sterge ultimul element din lista sau cel indicat de index
# company_list.pop()
# print(company_list)

# # Stergerea intregii liste cu del si clear()
# new_company_list = company_list
# print('New: ', new_company_list)

# del company_list
# # print(company_list) - va da eroare pentru ca company_list nu exista

# new_company_list.clear() # va goli lista, dar nu se va comporta ca si del
# print(new_company_list)

# # Copierea unei liste cu copy() si list()
# lst = ['Pavel', 'Petru', 'Ioan']
# new_lst = lst #metoda de copiere
# new_2_lst = lst.copy() #alta metoda de copiere
# print("new_lst: ", new_lst)
# print("new_2_lst: ", new_2_lst)
# my_list = list(new_2_lst)
# print("my_list: ", my_list)

# # Functii folosite si altele: 
# '''
# 1. append() 
# 2. clear()
# 3. copy()
# 4. count()
# 5. extend()
# 6. index()
# 7. insert()
# 8. pop()
# 9. remove()
# 10. reverse()
# 11. sort()
# 12. len()
# '''

# # Inversare elemente din lista
# new_lst.reverse()
# print('Reverse new_list: ', new_lst)

# # Functia count() - Numara acel elemet specificat dintr-o lista
# x = new_lst.count("Petru")
# print('S-a gasit de:', x, 'ori!')

# # functia extend() - lucreaza similar cu functia append sau pop

# thisList = [1, 2, 3]
# thatList = [4, 5, 6]
# thisList.extend(thatList)
# print(thisList)

# # functia index() - returneaza indexul unui element 
# x = thisList.index(6)
# print('Index: ', x)

# # functia sort()
# thisList = [5,3,4,9,8,1,7,5]
# thisList.sort() # --> aceasta va sorta elementele crescator sau alfabetic
# print(thisList)
# thisList.sort(reverse = True) # --> aceasta va sorta elementele descrescator sau incepand de la ultima litera
# print(thisList)

# # Liste (tablori)
# #definire vector, initializare si afisare
# n = 10
# tab = [1] * n
# tab1 = [0 for i in range(n)]
# print(tab)
# print(tab1)

# for i in tab:
#     print(tab[i], end = ' ')
# print()
# # Citirea vectorului de la tastatura
# n = 5
# tab = [int(input('tab[' + str(i) + '] = ')) for i in range(n)]
# for i in range(n):
#     print(tab[i], end=' ');

# # Alte operatiuni
# sir = 'Beniamin Sferiuc, fiul dreptei!'
# tab = [x for x in sir.split()]
# print('TAB: ', tab, end = ' ')

# cuv = []
# for x in ['a', 'e', 'c']:
#     for y in ['a', 'b', 'c']:
#         if x != y:
#             cuv.append(x + y)
# print(cuv)

# print('Hello, Python! '\
#       'Hello, World! '\
#         'Hello, Benjamin!')

# Construirea unei matrice (lista de liste)
# row = 4
# col = 5

# mat = [10] * row
# print(mat)
# for i in range(0, row):
#     mat[i] = [10] * col

# print(mat)

# # Afisare matrice cu for
# for i in range(row):
#     print(*mat[i], end='\n')

# # Alt mod de a defini o matrice - se va specifica prima data col
# mat2 = [[10 for i in range(col)] for j in range(row)]
# for i in range(row):
#     print(mat2[i], end='\n')

# # Citire vector de la tastatura
# n = int(input('n = '))
# lista = []
# for i in range(n):
#         lista.append(int(input()))

# print(lista)

# # Alt mod de citire - se citesc numere pana se intalneste enter
# l = []
# citit = input("Introdu: ")
# while citit != '':
#     l.append(citit)
#     citit = input('Introdu: ')

# print(l)

# ___________________________________________________________________________________________________________________________________
# Tuple / Enumerari

#functii utile:
'''
1. len(tuple)
2. cmp(tuple1, tuple2)
3. max(tuple)
4. min(tuple)
5. tuple(list)
'''

# tuple = 1,2,3,4,5,6,7
# print(tuple[5:])

# # ___________________________________________________________________________________________________________________________________
# # Dictionare in Python
# dic = {1: 'Luni', 2: 'Marti'}
# print(dic)
# newdic = dic.copy()
# print(newdic)

# Operatii cu fisiere text
    #deschiderea unui fisier
    # sintaxa: <file_object> = open(<file_name>, [<mod>])
'''
Moduri      Description
1. 'r'      Reading
2. 'w'      Writing
3. 'x'      Exclusive creation
4. 'a'      Appending at the end of the file
5. 't'      Text mode
6. 'b'      Binary mode
7. '+'      Open a file for updating (reading and writing)
'''

# Citirea informatiilor din fisier
'''
Metode                      Descriere
1. read(size = -1)          Citeste size octeti din fizier. Daca nu este specificat sau e -1, atunci se va citi intregul fisier
2. readline(size = -1)      Citeste size octeti de pe o singura linie
3. readlines()              Se citesc liniile din fisier si se memoreaza intr-o lista
'''

# file = open('readme.txt', 'r') #deschide fisierul si il salveaza in variabila file
# lst = list(file)
# while True:
#     linie = file.readline() #Citeste fiecare linie in parte
#     if len(linie) == 0:
#         break
#     print(linie, end = '')
# file.close()    #inchide fisierul

# print(lst)

# # Afisarea numarului inregistrarilor
# for i in range(len(lst)):
#     print(str(i + 1) + ':\t\t' + lst[i], end = '')

# Enumerari
# file = open('readme.txt', 'r')
# lst = list(file)
# print(lst)
# file.close()

# for i, linie in enumerate(lst):
#     print(i + 1, ':\t\t', linie, end = '', sep = '')
# print()
# new_list = list(enumerate(lst, 1))
# print(new_list)

# with open() as ...
# sintaxa: with open(nume_fisier, mod) as f:
#                   <bloc de intructiuni>
# ! functia close() este apelata automat cand se iese din blocul with
# with open('readme.txt', 'rt') as file:
#     linii = file.readlines()

# print(linii)
# print()
# #
# for l in linii:
#     print(l, end = '')
# # echivalent cu cea de sus
# for l in linii:
#     print(l.rstrip())

# Aplicatie:
with open('student.txt', 'rt') as f:
    lines = f.readlines()

n = media = 0
print('Nume', '\tPrenume', '\tNota', sep = '\t')
print('-' * 36)
for linie in lines:
    campuri = linie.split()
    nota = int(campuri[2])
    n, media = n + 1, media + nota
    print(campuri[0], campuri[1], '', nota, sep = '\t')
print()
print('Media celor', n, 'studenti este %.2f' % (media/n))

lst = 'Eu sunt Beniamin Sferciuc, fiul dreptei!'
new_lst = lst.split()
print(new_lst)

# Alte functii alternative la print si input
# import sys
# sys.stdout.write('Hello, Python!')

# import pprint
# pprint.pprint("This is pprint world!")

# import getpass
# password = getpass.getpass("Introduceti parola: ")
# print(password)

#ramas la 89