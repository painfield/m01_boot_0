ARTICULO = 0
UNIDADES = 1
PRECIO = 2

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
        print ('\n'+str(num),'no es un número.')
        print ('Solo números!\n')
    return valNum

print ('Factura\n-------')
end = False
lista = []
total = 0
items = 0

while end is False:
    articulo = input('Introduce el artículo:')
    unidades = input('nº de unidades:')
    precio = commaReplace (input('Precio por unidad:'))
    if articulo == '' and unidades == '' and precio == '':
        end = True
    else:
        if articulo != '' and unidades.isdigit() and validate(precio) is True:
            item = []
            item.append(articulo)
            item.append(unidades)
            item.append(precio)
            lista.append(item)
        else:
            print ('\nNo registrado. Debes introducir un artículo, números enteros como unidades y el precio ha de ser numérico.\n')

print ('\n')
for item in lista:
    parcial = float(item[PRECIO]) * int(item[UNIDADES])
    total += parcial
    items += int(item[UNIDADES])
    if int(item[UNIDADES]) > 1:
        print(item[ARTICULO]+'\t'+(item[PRECIO]+'€').rjust(6),'*',item[UNIDADES].rjust(2),'uds. =',(str(round (parcial,2))+'€').rjust(7))
    else:
        print(item[ARTICULO]+'\t'+(item[PRECIO]+'€').rjust(6),'*',item[UNIDADES].rjust(2),' ud. =',(str(round (parcial,2))+'€').rjust(7))
print('----------------------------------\nTotal:\t\t',str(items).rjust(2),'uds. =', (str(round(total,2))+'€').rjust(7))