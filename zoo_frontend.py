import screen
from zoo_config import precio, posicion

def printScreen():
    screen.clear()
    screen.Print('Bebe....:    -',4,5) # linea,columna
    screen.Print('Menor...:    -',5,5)
    screen.Print('Adulto..:    -',6,5)
    screen.Print('Jubilado:    -',7,5)
    screen.Print('\033[7mTotal...:    -  \033[0m',9,5)
    
def pedirEdad():
    edad = screen.Input('\033[4mIntroduce la edad (vacío para terminar):\033[0m ',1)
    if edad.isdigit() is True:
        edad = int(edad)
        return edad
    elif edad != '':
        screen.Print('\033[6;7;31;107m{:^}\033[0m'.format('La edad debe ser un número entero positivo.'),25)
        #screen.Format(26,'reverse') no funciona, como si no lo pillara al no estar junto con la cadena
        #screen.Print('La edad debe ser un número entero positivo.')
        #screen.Format('reset')
    else:
        return ''

def printEntrada(entradas,tipo,totalEntradas,total):
    screen.Print('{:>3}'.format(entradas),posicion[tipo][0],posicion[tipo][1])
    screen.Print('{:>5}€'.format(entradas*precio[tipo]),posicion[tipo][0],posicion[tipo][2])
    screen.Print('\033[7m{:>3}\033[0m'.format(totalEntradas),9,14)
    screen.Print('\033[7m{:>5}€\033[0m'.format(total),9,20)
    screen.lineDel(25)
    
def terminar():
    screen.lineDel(25)
    screen.position(12)