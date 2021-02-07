import anagrama

valid = False
while valid is False:
    palabra1 = input('Introduce una palabra: ')
    palabra2 = input('Introduce otra palabra: ')
    if palabra1.isalpha() and palabra1 != '' and palabra2.isalpha() and palabra2 != '' and len(palabra1) == len(palabra2):
        valid = True
    else:
        print ('\nEscribe palabras con el mismo número de letras y sin espacios.\n')

if anagrama.isAnagram(palabra1,palabra2) is True:
    print ('\033[1;37;42m'+palabra1,'y',palabra2,'son anagramas\033[0m.')
else:
    print ('\033[1;37;41m'+palabra1,'y',palabra2,'no son anagramas\033[0m.')