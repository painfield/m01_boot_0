import turtle

def cuadrado(lado):
    TMNT.forward(lado/2)
    TMNT.left(90)
    TMNT.forward(lado/2)
    TMNT.left(90)
    TMNT.forward(lado)
    TMNT.left(90)
    TMNT.forward(lado)
    TMNT.left(90)
    TMNT.forward(lado)
    TMNT.left(90)
    TMNT.forward(lado/2)
    TMNT.left(90)
    TMNT.forward(lado/2)
    TMNT.left(90)
    return lado*lado

TMNT = turtle.Turtle()

sum = 0
for i in range(1,43):
    sum += i
    area01 = cuadrado(sum)
    print ('loop =',i)
    print ('lado =',sum)
    print ('area =',area01)
    TMNT.left(90)
    i += 1

for i in range(1,43):
    sum -= i*2
    area01 = cuadrado(sum)
    print ('loop =',i)
    print ('lado =',sum)
    print ('area =',area01)
    TMNT.left(90)
    i += 1

num=int(input('Cuantos cuadrados? '))
paso = int(input('Paso? '))
for i in range(num):
    lado = i * paso
    #lado = int(input('lado '+str(i+1)+': '))
    area = cuadrado(lado)
    print ('loop =',i)
    print ('lado =,'lado)
    print ('area =',area)
    TMNT.left(90)