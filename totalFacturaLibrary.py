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
            item = dict()
            item['articulo'] = articulo
            item['unidades'] = unidades
            item['precio'] = precio
            lista.append(item)
        else:
            print ('\nNo registrado. Debes introducir un artículo, números enteros como unidades y el precio ha de ser numérico.\n')

for item in lista:
    parcial = float(item['precio']) * int(item['unidades'])
    total += parcial
    items += int(item['unidades'])
    if int(item['unidades']) > 1:
        txt_ud = 'uds. ='
    else:
        txt_ud = ' ud. ='
    print(item.get('articulo')+'\t'+(item.get('precio')+'€').rjust(6),'*',item.get('unidades').rjust(2),txt_ud,'{:.2f}€'.rjust(8).format(parcial))
print('----------------------------------\nTotal:\t\t',str(items).rjust(2),'uds. = {:.2f}€'.rjust(8).format(total))