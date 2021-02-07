name = input('Cómo te llamas? ')
try:
    print('Hola,',name)
except:
    print('Hola.')
age = input('Que edad tienes? ')
year = 2020 - int(age)
print('Naciste en',year)