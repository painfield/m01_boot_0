def mayusc(palabra):
    PALABRA = ''
    for letra in palabra:
        codigo = ord(letra)
        print (letra,'-',codigo)
        if codigo >= 97 and codigo <=122:
            codigoM = codigo - 32
            letraM = chr(codigoM)
            PALABRA = PALABRA + letraM
    return PALABRA

def lista():
    for codigo in range(32,128):
        print(codigo,'-',chr(codigo),end='\t')

while True:
    txt = input('\nIntroduce una palabra (list para tabla ASCII): ')
    if txt == 'list':
        lista()
    else:
        TXT = mayusc(txt)
        print ('upper:',txt.upper())
        print ('mi función mayusc:',TXT)
        print ('lower:',TXT.lower())
