notas = (5,4,3,6,8,9,5,4)
sum = 0
print ('index nota suma')
for i in range (len(notas)):
    sum += notas[i]
    print (i,'   ',notas[i],'  ', sum)
media = sum/len(notas)

print ('\nTotal / Items = media\n',sum,'  /',len(notas),'    =',media)