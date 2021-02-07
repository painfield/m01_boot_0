lock = True # Se desbloquea al introducir dos enteros
while lock is True:
    num1 = input('Introduce un número: ')
    num2 = input('Introduce otro número: ')
    if num1.is_integer() is True and num2.is_integer() is True:
        lock = False
    else:
        print ('\n\n\nSolo números enteros.\n\n') 
        
num1 = int(num1)/10
num2 = int(num2)/10
suma = round(num1 + num2, 2)
resta = round(num1 - num2, 2)
mult = round(num1 * num2, 2)
div = round(num1 / num2, 2)

print('\n')
print(num1, ' + ', num2, ' = ', suma)
print(num1, ' - ', num2, ' = ', resta)
print(num1, ' * ', num2, ' = ', mult)
print(num1, ' / ', num2, ' = ', div)