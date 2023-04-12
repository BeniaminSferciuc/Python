# Dictionare in Python

# Ex. 1)
opt = '''
1. Incarcare informatii despre studenti de la tastatura
2. Afisare studenti
3. Afisare note
4. Afisarea studenti si notele obtinute
5. Cautare student dupa nume
6. Afisare studenti promovati
7. Info autor
8. Termina program
'''

dict_name = {}
dict_note = {}

while(True):
    print(opt)
    option = int(input("Introduceti o optiune: "))
    match(option):
        case 1:
            nr = int(input('Introduceti numarul de studenti: '))
            for i in range(nr):
                data = input('Student %d: ' % (i + 1)).split(',')
                ID = int(data[0])
                name = data[1]
                note = [int(nota) for nota in data[2].split()]
                dict_name[ID] = name
                dict_note[ID] = note
        case 2:
            ids = 'ID'
            print(f'{ids:<10} Nume Student')
            for i, value in dict_name.items():
                print(f'{i:<10} {value}')
        case 3:
            std = 'ID stud'
            print(f'{std:<10} Note')
            for i, note in dict_note.items():
                print(f'{i:<10} {note}')
        case 4:
            std = 'ID'
            nume_std = 'Nume student'
            print(f'{std:<10} {nume_std:<20} Note')
            for key in dict_name:
                print(f'{key:<10} {dict_name[key]:<20} {dict_note[key]}')
        case 5:
            search__student = input('Numele studentului: ')
            aux = 0
            for key in dict_name:
                if search__student == dict_name[key]:
                    print('-'*40)
                    print(f'{key:<10} {dict_name[key]:<20} {dict_note[key]}')
                    aux = 1
            if aux == 0:
                print('Numele nu exista!')
        case 6:
            # Afisare studenti promovati >=5
            print(f'ID\t\tNume student\t\tMedia')
            print('-'*45)
            dict_avr = {}
            for key in dict_note:
                suma = sum(dict_note[key])
                length = len(dict_note[key])
                average = suma/length
                if average >= 5:
                    print("{}\t\t{}\t\t{:.2f}".format(key, dict_name[key], average))
                    # print(f'{key}\t\t{dict_name[key]}\t\t{round(average, 2)}')
        case 7:
            print(f'Autor: Beniamin Sferciuc!')
        case 8:
            exit('Sfarsit!')
        case _:
            print('Ati introdus o optiune indisponibila!')

# End