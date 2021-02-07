def commaReplace (num):
    s = list(num)
    for value in range(len(s)):
        if s[value] == ',':
            s[value] = '.'
    num = "".join(s)
    return num

def validate(num):
    valNum = True
    for value in range(len(num)):
        if not num[value].isdigit() and not (num[value] == '.' and (num[value-1].isdigit() or num[value-1] == None) and num[value+1].isdigit()):
            valNum = False
    if valNum == False:
        print ('\n'+num,'no es un número.')
        print ('Solo números!\n')
    return valNum

print ('Cálculo del area de un triángulo\n')
validation = False
while validation is not True:
    b = commaReplace (input('Introduce la base:'))
    h = commaReplace (input('Introduce la altura:'))
    if b != '' and h != '':
        if validate(b) is True and validate(h) is True:
            validation = True
    else:
        print ('\nTienes que introducir valores numéricos.\n')
        
area = round((float(b) * float(h)) / 2, 2)

print('\nEl area es', area)