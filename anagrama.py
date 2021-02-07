import sys
def biblioCaracter(palabra):
    prohibido = (' ',',','.',';',':','-','_')
    cuenta = {}
    for caracter in palabra:
        if caracter not in prohibido:
            caracter = caracter.lower()
            if caracter in cuenta: #también -> cuenta.get(caracter) != None
                cuenta[caracter] += 1 # también -> cuenta.update({caracter:int(numLetra)+1})
            else:
                cuenta[caracter] = 1
    return cuenta
            
def isAnagram(p1,p2):
    cuenta1 = biblioCaracter(p1)
    cuenta2 = biblioCaracter(p2)
    for letra,reps in cuenta1.items():
        if letra not in cuenta2.keys() or reps != cuenta2[letra]:
            return False
    return True

if __name__ == '__main__':
    valid = False
    trigger_input = True
    if len(sys.argv) != 1:
        if len(sys.argv) == 3:
            palabra1 = sys.argv[1]
            palabra2 = sys.argv[2]
            trigger_input = False
        else:
            print('\nDebes incluir exactamente 2 argumentos\n')
            
    while valid is False:
        if trigger_input == True:
            palabra1 = input('Introduce una palabra: ')
            palabra2 = input('Introduce otra palabra: ')
        if palabra1.isalpha() and palabra1 != '' and palabra2.isalpha() and palabra2 != '' and len(palabra1) == len(palabra2):
            valid = True
        else:
            print ('\nEscribe palabras con el mismo número de letras y sin espacios.\n')
            trigger_input = True
            
    if isAnagram(palabra1,palabra2) is True:
        print ('\033[1;37;42m'+palabra1,'\033[0;37;42my\033[1;37;42m',palabra2,'\033[0;37;42mson anagramas.\033[0m')
    else:
        print ('\033[1;37;41m'+palabra1,'y',palabra2,'no son anagramas.\033[0m')
