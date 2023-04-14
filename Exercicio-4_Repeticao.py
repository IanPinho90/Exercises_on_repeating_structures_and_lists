popChina=200000
popJapao=80000
anos=[]
while popChina>popJapao:
    anoJapao=popJapao*1.03
    anoChina=popChina*1.015
    popJapao=anoJapao
    popChina=anoChina
    anos.append(1)
print ("Ano(s):", len (anos))



