import turtle #también puede ser import 'turtle as tortu' para crear un alias, 'tortu.home()'
              # o 'from turtle import home' para importar solo la función y llamarla 'home()', no 'turtle.home()'
              # dir(turtle) devuelve todas las funciones del módulo
              # help (turtle.función) devuelve info acerca de la función
def turtleTest():
    turtle.home()
    turtle.begin_poly()
    turtle.fd(100)
    turtle.left(20)
    turtle.fd(30)
    turtle.left(60)
    turtle.fd(50)
    turtle.end_poly()

    turtle.down()
    print('expect 0.0 ->',turtle.heading()-90)
    turtle.left(90)
    print('expect 90.0 ->',turtle.heading()-90)
    turtle.left(90)
    print('expect 180.0 ->',turtle.heading()-90)
    turtle.left(90)
    print('expect 270.0 ->',turtle.heading()+360-90)
    turtle.left(90)
    print('expect 0.0 ->',turtle.heading()-90)
    turtle.home()

def circle(radius):
    turtle.home()
    turtle.write(cadena,False,align="center",font=("Arial", 12, "normal"))
    turtle.speed('fastest')
    turtle.up()
    turtle.forward(radius)
    turtle.left(90)
    turtle.down()
    turtle.circle(radius)
    turtle.up()
    turtle.right(90)
    turtle.home()
    turtle.speed('normal')

def move(grados,size):
    turtle.home()
    turtle.setheading(grados)
    turtle.forward(300)
    turtle.dot(size,'blue')
    
    turtle.setheading(0)
    turtle.forward(size+(size/2))
    turtle.write("Digito: "+digito+'*'+str(checked[digito]),False,align="center",font=("Arial", 14, "normal"))
    
    turtle.setheading(0)
    turtle.home()

digitos16 = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
anguloSector = 360/16
cadena = input('Introduce mensaje a enviar: ')
checked = dict()

turtle.hideturtle()
turtle.mode('logo') # orientar disco correctamente con el inicio al Norte
#turtle.speed('fastest')
#turtleTest()
poly = turtle.get_poly()
circle(300)
for caracter in cadena:
    valorHex = hex(ord(caracter))
    for digito in valorHex[2:4]:
        posicionDigito = digitos16.index(digito)
        angulo = posicionDigito * anguloSector
        print ('digito:',digito,'ángulo:',angulo,'º')
        if digito in checked.keys():
            checked[digito] += 1
        else:
            checked[digito] = 1
        tamanyo = checked[digito]*15
        #turtle.pensize(10)
        move (angulo,tamanyo)