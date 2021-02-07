import screen
import zoo_frontend
from zoo_config import precio, posicion

def abreFichero():
    try:
        fEntradas = open('transacciones.txt', 'r')
        return fEntradas
    except:
        screen.clear()
        screen.Print('\033[6;7;31;107m{:^}\033[0m'.format('Fichero inexistente.'),10)
        return None

def preparaEntradas(numeroEntradas):
    numEntradas = numeroEntradas.split(',')
    entradas = {'bebe':0,'menor':0,'adulto':0,'jubilado':0}
    i = 0
    for tipo in entradas:
        entradas[tipo] = int(numEntradas[i])
        i += 1
    return entradas 

def imprimeDiario(fEntradas,registro):
    totalEntradas = 0
    total = 0
    while registro != '':
        entradas = preparaEntradas(registro)
        for tipo in entradas:
            totalEntradas += entradas[tipo]
            total += entradas[tipo]*precio[tipo]
            zoo_frontend.printEntrada(entradas[tipo],tipo,totalEntradas,total)
        continuar = screen.Input('Pulsa intro para continuar',12)
        totalEntradas = 0
        total = 0
        registro = fEntradas.readline()

def imprimeTotal(fEntradas,registro):
    ent = {'bebe':0,'menor':0,'adulto':0,'jubilado':0}
    totalEntradas = 0
    total = 0
    while registro != '':
        entradas = preparaEntradas(registro)
        for tipo in entradas:
            ent[tipo] += entradas[tipo]
            totalEntradas += entradas[tipo]
            total += entradas[tipo]*precio[tipo]
        registro = fEntradas.readline()
    for tipo in ent:
        zoo_frontend.printEntrada(ent[tipo],tipo,totalEntradas,total)

def main():
    fEntradas = abreFichero()
    if fEntradas is not None:
        zoo_frontend.printScreen()
        registro = fEntradas.readline()
        modo = screen.Input('Quieres los registros diarios (d) o el total (t)? ',12)
        if modo == 'd':
            imprimeDiario(fEntradas,registro)
        if modo == 't':
            imprimeTotal(fEntradas,registro)
    zoo_frontend.terminar()

main()