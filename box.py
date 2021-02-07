import screen

screen.clear()
screen.position(10,20)
print ('************')
for i in range (1,19):
    screen.position(10,20+i)
    print ('*          *')
screen.position(10,40)
print ('************')

screen.funciones('math')
screen.ayuda('math','pi')
