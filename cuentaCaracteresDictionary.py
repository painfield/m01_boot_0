texto = 'En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor.'\
'Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lantejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda.'\
'El resto della concluían sayo de velarte, calzas de velludo para las fiestas, con sus pantuflos de lo mesmo, y los días de entresemana se honraba con su vellorí de lo más fino.'\
'Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la podadera.'\
'Frisaba la edad de nuestro hidalgo con los cincuenta años; era de complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo de la caza.'\
'Quieren decir que tenía el sobrenombre de Quijada, o Quesada, que en esto hay alguna diferencia en los autores que deste caso escriben; aunque por conjeturas verosímiles se deja entender que se llamaba Quijana.'\
'Pero esto importa poco a nuestro cuento: basta que en la narración dél no se salga un punto de la verdad.'
cuenta = {}
for caracter in texto:
    if caracter != ' ' and caracter != ',' and caracter != '.' and caracter != ';' and caracter != ':':
        caracter = caracter.lower()
        if caracter in cuenta: #también -> cuenta.get(caracter) != None
            cuenta[caracter] += 1 # también -> cuenta.update({caracter:int(numLetra)+1})
        else:
            cuenta[caracter] = 1

print ('\033[1;37;40m')
print (texto)
#for key, value in cuenta.items():
#    print('Hay',value,'instancias de',key)

print ('\nOrdenado\n')
ordList = dict()
done = []
i = 0
while i < len(cuenta):
    top = 0
    last = ''
    for key, value in cuenta.items():
        if key not in done:
            if value > top:
                top = value
                last = key
    done.append(last)
    if last not in ordList:
        ordList[last] = top
    i += 1
for key, value in ordList.items():
    print('Hay',value,'instancias de',key)