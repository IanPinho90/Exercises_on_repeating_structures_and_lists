parada=False
print("Digite seu nome:")
nome=(input())
while parada==False:
    if len(nome) <=3: #SACANAGEM
        print("nome pequeno demais, tente denovo.")
        print("Digite seu nome:")
        nome=input()
    else:
        parada=True
while parada==True:
    print("Digite sua idade:")
    idade=int(input())
    if idade<=0 or idade>=150:
        print("idade inválida.")
    else:
        parada=False
while parada==False:
    print("Digite seu salário:")
    salario=int(input())
    if salario<=0:
        print("Valor inválida.")
    else:
        parada=True
while parada==True:
    print("Digite seu sexo, 'f' ou 'm'")
    sexo= input()
    if sexo == "f" or sexo == "m" :
        parada = False
    else:
        print ("Sexo inválido")
while parada==False:
    print("Digite seu estado civil, 's' 'c' 'v' 'd'")
    estado= input()
    if estado == "s" or estado == "c" or estado == "v" or estado == "d":
        print("Parabéns, cadastro completo.")
        parada = True
    else:
        print ("Estado civil inválido")

