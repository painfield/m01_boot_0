import math

tupla = ('A','B','C','D','E','F','H','I','J')
indice = 0
while indice < len(tupla):    
    print (indice,'// 3 (cociente) =',indice // 3)
    print (indice,'% 3 (resto =',indice % 3)
    print (indice,'** 3 (potencia =',indice ** 3,'\n')
    if (indice + 1) % 3 == 0:
        print(tupla[indice])
    indice += 1