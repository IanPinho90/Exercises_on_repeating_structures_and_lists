numeros = [1,2,3,4,5]
Media = 0
tempSoma = 0
for i in range(len(numeros)):
    tempSoma += numeros[i]
Media = tempSoma / len(numeros)
print("Soma:",tempSoma)
print("Média:",Media)