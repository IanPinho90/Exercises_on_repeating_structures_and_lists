altura = []
idade = []

for i in range (5):
    print("Insira sua Altura:")
    altura.append(float(input()))
    print("Insira sua idade:")
    idade.append(int(input()))

altura.reverse()
idade.reverse()

print (altura)
print (idade)

