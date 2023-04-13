ListaNotasAlunos= [["Caio",[7,9,8,10]],["Cauã",[9,8,7,4]],["Henrique",[8,6,7,9]],["Davi",[4,6,2,10]],["Miguel",[6,2,5,8]],["Maykon",[9,5,3,6]],["Arthur",[9,6,4,8]],["Guilherme",[9,7,8,9]],["Liz",[9,8,10,9]],["Ian",[10,10,10,10]]]
alunosAprovados = 0
for aluno in ListaNotasAlunos:
    
    media = 0
    media=(sum(aluno[1])/4)
    if media >= 7:
        alunosAprovados = alunosAprovados + 1

print("Alunos Aprovados:",alunosAprovados)

        