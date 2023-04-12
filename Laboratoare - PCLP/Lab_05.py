# Ex. 1)
import sys
from termcolor import colored, cprint
import functions_lab5 as fun
'''
while True:
    print(fun.display_options())
    option = input('Introduceti o optiune: ')
    option = option.upper()
    match option:
        case 'A': 
            n = int(input("Introduceti numarul de elemente: "))
            while n <= 0 or n > 20:
                print(colored("Introduceti numarul de elemente: ", 'red', attrs=['reverse', 'blink']))
                n = int(input())
            a = int(input('Introduceti intervalul minim: '))
            b = int(input('Introduceti intervalul maxim: '))
            if a > b:
                a, b = b, a
            arr = fun.option_A(n, a, b)
        case 'B':
            print(*arr)
        case 'C':
            fun.option_C(arr)
        case 'D':
            max = max(arr)
            print(f'Maximul este {max} si indexul este {arr.index(max)}')
        case 'E':
            x = int(input('Introduceti pozita: '))
            fun.option_E(arr, x)
        case 'F':
            fun.rm_elem(arr)
        case 'G':
            print('Hello, I am Beniamin!')
        case 'H':
            exit("Sfarsit!")
        case 'I':
            import os
            os.system('cls')
        case _:
            print("Ati introdus o comanda inexistenta!")
'''

# Ex. 2) Operatii asuprea unei matrice
import functions_lab5 as myFunction

print(myFunction.display_opt())

while True:
    while True:
        try:
            option = int(input("Introduceti o optiune: "))
            break
        except ValueError:
                print('Introduceti numai numere!')
    match(option):
        case 1:
            name = input("Numiti matricea: ")
            row = int(input("Introduceti numarul de randuri: "))
            col = int(input("Introduceti numarul de coloane: "))
            matrice = myFunction.create_matrice(row, col)
        case 2:
            print(f'Matricea {name}:')
            myFunction.display_mat(matrice)
        case 3:
            print(f'Elementele maxime de pe linii: ')
            max_elem_l = myFunction.max_elem_line(matrice)
            print(max_elem_l)
        case 4:
            print(f'Elementele maxime de pe coloane: ')
            max_elem_c = myFunction.max_elem_col(matrice)
            print(max_elem_c)
        case 5:
            print(f'Matricea {name} transpusa:')
            for i in myFunction.transpose(matrice):
                print(*i)
        case 6:
            print('Introduceti noua linie: ')
            new_line = myFunction.create_line(col)
            new_mat_l = myFunction.add_line(matrice, new_line)
            myFunction.display_mat(new_mat_l)
        case 7:
            print('Introduceti noua coloana:')
            new_mat_c = myFunction.add_col(matrice)
            myFunction.display_mat(new_mat_c)
        case 8:
            line = int(input('Ce linie doriti sa stergeti? Introduceti: '))
            del_row = myFunction.del_line(matrice, line)
            myFunction.display_mat(del_row)
        case 9:
            nr_col = int(input('Ce coloana doriti sa stergeti? Introduceti: '))
            del_col = myFunction.del_col(matrice, nr_col)
            myFunction.display_mat(del_col)
        case 10:
            print(f'Matricea {name} liniarizata este: ')
            myFunction.inline(matrice)
        case 11:
            exit("End.")
        case _:
            print("Ati introdus o optiune gresita!")

# End