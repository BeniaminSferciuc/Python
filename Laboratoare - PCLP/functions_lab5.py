import random

# Aceasta functie afiseaza toate optiunile disponibile
def display_opt():
    options = \
'''
1\tCitire matrice de la tastatura (pe linii)
2\tAfisare matrice
3\tCreare si afisare lista de elemente maxime de pe linii
4\tCreare si afisare lista de elemente maxime de pe coloane
5\tAfisare matrice transpusa
6\tAdauga linie
7\tAdauga coloana
8\tSterge linie
9\tSterge coloana
10\tLiniarizare matrice (creare si afisare vector rezultat)
'''
    return options

# Aceasta functie creaza o matrice
def create_matrice(row, col):
    matrice = []
    while True:
        try:
            for i in range(row):
                rand = []
                for j in range(col):
                    rand.append(int(input('[' + str(i) + '][' + str(j) + '] = ')))
                matrice.append(rand)
            break
        except ValueError:
            print('Introduceti un numar!')
    return matrice

# Aceasta functie afiseaza o matrice
def display_mat(mat):
    for i in mat:
        print(*i)

# Aceasta functie returneaza o lista cu elementele maxime de pe linii
def max_elem_line(mat):
    max_list = []
    for i in mat:
        max_list.append(max(i))
    return max_list

# Aceasta functie returneaza o lista cu elementele maxime de pe coloane
def max_elem_col(mat):
    max_list = []
    transpose_mat = list(zip(*mat))
    for i in transpose_mat:
        max_list.append(max(i))
    return max_list

# Aceasta functie returneaza o matrice transpusa
def transpose(mat):
    mat_traspose = list(zip(*mat))
    return mat_traspose

# Creaza inca o linie de elemente 
def create_line(col):
    new_line = [int(input('Elementul ' + str(i + 1) + ' : ')) for i in range(col)]
    return new_line

# Adauga o linie la o matrice existenta
def add_line(mat, new_line):
    mat.append(new_line)
    return mat

# Adauga o coloana la o matrice existenta
def add_col(mat):
    print('Adaugati o coloana noua!')
    for i in mat:
        x = int(input('Introduceti elementul: '))
        i.append(x)
    return mat

# Aceasta functie sterge o linie din matrice:
def del_line(mat, line):
    mat.pop(line - 1)
    return mat

# Aceasta functie sterge o coloana din matrice:
def del_col(mat, col):
    for i in mat:
        i.pop(col - 1)
    return mat
    
# Aceasta functie afiseaza elementele unei liste de liste intr-o singura lista si cu virgula intre ele
def inline(mat):    
    my_list = []
    for i in mat:
        my_list.extend(i) 
    print(*my_list, sep=', ')

#_______________________________________________________
# Aici Ex. 1)
# Afiseaza optiunile disponibile
def display_options():
    str = \
'''
    A.\tGenerare vector de n-elemente
    B.\tAfisare vector generat
    C.\tAfisare elemente > decat media aritmetica a elementelor vectorului
    D.\tDeterminare valoare maximă şi pozitia aceasteia în tablou.
    E.\tDeplasare elemente cu x-pozitii; x-citit de la tastatura
    F.\tEliminare elemente care nu apartin intervalului [a,b]
    G.\tInfo autor
    H.\texit
'''
    return str

# Generare vector de n-elemente
def option_A(n, a, b):
    arr = []
    for i in range(1, n + 1):
        arr.append(random.randrange(a, b))
    return arr

# Afisare elemente > decat media aritmetica a elementelor vectorului
def option_C(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    sum = sum/len(arr)
    new_arr = []
    print(sum)
    for j in range(0, len(arr)):
        if(arr[j] > sum):
            print(arr[j])

# Deplasare elemente cu x-pozitii; x-citit de la tastatura
def option_E(arr, nr):
    print(arr[nr:] + arr[: nr])    

def rm_elem(arr):
    a = int(input())
    b = int(input())
    new_list = []
    for i in arr:
        if i in range(a, b) or i in range(b, a):
            new_list.append(i)
    print(new_list)