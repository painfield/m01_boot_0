num = ''
numPrim = True
valid = False

while valid == False:
    num = input('Introduce un número entero: ')
    if num.isdigit() and num !='0' and num !='1':
        valid = True
        for i in range(2,int(num)):
            if (int(num)%i == 0):
                numPrim = False
if numPrim == True:
    print(num,'es primo')
else:
    print(num,'no es primo')