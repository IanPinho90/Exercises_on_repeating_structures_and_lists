print("Insira a quantidade de habitantes do pais com maior população:")
popChina=int(input())
print("Insira a quantidade de habitantes do pais com menor população:")
popJapao=int(input())
print("Insira a taxa de crescimento em 1.x da população menor.")
taxaCrescimentoA = float(input())
print("Insira a taxa de crescimento em 1.x da população maior.")
taxaCrescimentoB = float(input())
anos=[]
parada=False
while parada==False:
    
    anoJapao=popJapao*taxaCrescimentoA
    
    anoChina=popChina*taxaCrescimentoB
    popJapao=anoJapao
    popChina=anoChina
    anos.append(1)
    if popChina<popJapao:
        parada=True
print ("Ano(s):", len (anos))