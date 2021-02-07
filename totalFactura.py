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

print ('Factura\n')
end = False
art = []
uds = []
prc = []
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
            art.append(articulo)
            uds.append(unidades)
            prc.append(precio)
        else:
            print ('\nNo registrado. Debes introducir un artículo, números enteros como unidades y el precio ha de ser numérico.\n')

for articulo,unidades,precio in zip(art,uds,prc):
    parcial = float(precio) * int(unidades)
    total += parcial
    items += int(unidades)
    if int(unidades) > 1:
        print(articulo+'\t'+(precio+'€').rjust(6),'*',unidades.rjust(2),'uds. =',(str(round (parcial,2))+'€').rjust(7))
    else:
        print(articulo+'\t'+(precio+'€').rjust(6),'*',unidades.rjust(2),' ud. =',(str(round (parcial,2))+'€').rjust(7))
print('----------------------------------\nTotal:\t\t',str(items).rjust(2),'uds. =', (str(round(total,2))+'€').rjust(7))