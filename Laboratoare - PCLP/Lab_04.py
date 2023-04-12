# Ex. 1)
'''
print("1.\tCitire")
print("2.\tAfisare")
print("3.\tAfisare nr cuvinte")
print("4.\tInlocuire X cu Y")
print("5.\tFormare sir cu majuscule")
print("6.\tNr de vocale")
print("7.\tEliminare caractere speciale")
print("8.\tStart index")
print("0.\tExit")

while True:
    try:
        optiune = int(input("Introduceti o optiune: "))
        match optiune:
            case 1:
                string = input("Introduceti un sir de caractere: ")
            case 2:
                print(string)
            case 3:
                list_of_items = list(string.split())
                for i in list_of_items:
                    print(f"{i} - {len(i)} caractere")
            case 4:
                X = input("Introduceti un caracter: ")
                Y = input("Introduceti un caracter: ")
                
                new_string = string.replace(X, Y)
                print(new_string)                
            case 5:
                upper_string = ''
                for letter in string:
                    if letter.isupper():
                        upper_string = upper_string + letter
                print(upper_string)           
            case 6:
                vowel = ['a', 'e','i','o', 'u']
                string.lower()
                for i in vowel:
                    count = 0
                    for j in string:
                        if i == j:
                            count += 1
                    print(f"{i} - {count} vowel")    
            case 7:
                el_string = ''
                for i in string:
                    if i.isalnum():
                        el_string += i
                print(el_string)           
            case 8:
                start = int(input("Introduceti un index: "))
                print(string[start:])
            case 9:
                exit(-1)
            case _:
                print("Comanda gresita! Incercati din nou!")
    except(ValueError):
        print("Ati introdus o optiune gresita!")

'''
# Ex. 2)
'''
sir1 = input("Introuceti sirul 1: ")
sir2 = input("Introuceti sirul 2: ")

count = len(sir1)
this_count = 0
for i in sir1:
    if i in sir2:
        this_count += 1
    
if count == this_count:
    print("Sirurile sunt echilibrate!")
else:
    print("Sirurile nu sunt echilibrate!")
'''

# Ex. 3)
'''
sir = input("Introuceti sirul: ")
subsir = input("Introuceti subsirul: ")

new__sir = sir
new__subsir =subsir


if subsir.lower() in sir.lower():
    print(f"Subsirul a fost gasit: {new__subsir}")
else:
    print("Subsirul nu a fost gasit!")
'''

# Ex. 4)
'''
my_string = input('Introduceti un sir de caractere: ')
vowel = 'aeiouAEIOU'
dbl = ''
for i in my_string:
    if i in vowel:
        dbl += i * 2
    else:
        dbl += i

print(dbl)
'''

# Ex. 5)
'''
my_string = input('Introduceti un sir de caractere: ')
n = int(input('Introduceti dimensiunea: '))
my_string.strip()
my_word = list(my_string.split())

for i in my_word:
    if len(i) == n:
        print(i)
'''

# Ex. 6)
'''
my_string = input('Introduceti un sir de caractere: ')

new_string = ''
for i in my_string:
    if i.isalnum() or i.isspace():
        new_string += i

print(new_string)
'''

# Ex. 7)
'''
my_string = input('Introduceti un sir de caractere: ')
my_list = my_string.split()
my_list.sort()
for i in my_list:
    print(i)
'''

# Ex. 8)
my_string = input('Introduceti un sir de caractere: ')
my_list = my_string.split()
new_str = ''
for i in my_list:
    new_str += str(i[::-1]) + ' '
print(new_str)

# End