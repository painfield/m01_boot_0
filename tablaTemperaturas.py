def CtoF(temp):
    f = round((temp * 9/5) + 32,2)
    return f

def FtoC(temp):
    c = round((temp - 32) * 5/9,2)
    return c

def listaTemp(sistema,limite,paso):
    for temp in range(0,limite,paso):
        if sistema == 'C':
            txt_orig = 'ºC'
            txt_conv = 'ºF'
            temp_conv = CtoF(temp)
        else:
            txt_orig = 'ºF'
            txt_conv = 'ºC'
            temp_conv = FtoC(temp)
        print ((str(temp)+txt_orig).rjust(len(str(temp))),(str(temp_conv)+txt_conv).rjust(len(str(temp_conv))))

validacion = False
while True: #validacion is False
    sistema = input('Introduce C/F: ').upper()
    if sistema == 'C':
        limite = 100
        paso = 10
        listaTemp(sistema,limite,paso)
        validacion = True
    if sistema == 'F':
        limite = 230
        paso = 40
        listaTemp(sistema,limite,paso)
        validacion = True