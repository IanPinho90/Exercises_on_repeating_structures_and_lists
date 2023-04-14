print("Insira uma nota de 0-10:")
parada=False


while parada==False:
    nota=input()
    if nota >= "0" and nota <= "10":
        print("Valor inserido válido.")
        parada=True
    else:
        print("Valor inserido inválido, tente novamente.")




