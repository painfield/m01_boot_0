import screen
import zoo_frontend
from zoo_config import precio, posicion

def registroEntradas():
    edad = None
    entradas = {'bebe':0,'menor':0,'adulto':0,'jubilado':0}
    totalEntradas = 0
    total = 0
    
    zoo_frontend.printScreen()
    
    while edad != '':
        edad = zoo_frontend.pedirEdad()
        if edad is not None and edad is not '':    
            if edad > 0 and edad <= 2:
                tipo = 'bebe'
            elif edad <= 12:
                tipo = 'menor'
            elif edad >= 65:
                tipo = 'jubilado'
            else:
                tipo = 'adulto'
            totalEntradas += 1
            entradas[tipo] += 1
            total += precio[tipo]
            zoo_frontend.printEntrada(entradas[tipo],tipo,totalEntradas,total)
    return entradas

def guardaFichero(entradas):
    fEntradas = open('transacciones.txt', 'a+')
    transaccion = '{},{},{},{}\n'.format(entradas['bebe'],entradas['menor'],entradas['adulto'],entradas['jubilado'])
    fEntradas.write(transaccion)
    fEntradas.close()
    
def main():
    entradas = registroEntradas()
    guardaFichero(entradas)    
    zoo_frontend.terminar()
    
main()