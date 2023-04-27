numeros = [1,2,3,4,5]
tempNumber = 0
for i in range(len(numeros)):
    if numeros[i] > tempNumber:
        tempNumber = numeros[i]
print(tempNumber)