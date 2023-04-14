Parada=False
print("Insira seu nome de usuário:")
userName=input()
print ("Usuário é:",userName)
print("Insira sua senha:")
senha=input()
while Parada==False:
    if senha==userName:
        print("Senha não pode ser igual o nome.")
        print("Insira sua senha:")
        senha=input()
    else:
        print("Conta criada com sucesso.")
        Parada=True
