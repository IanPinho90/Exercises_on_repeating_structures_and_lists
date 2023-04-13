Vetor1 = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]
Vetor2 = [[9],[8],[7],[6],[5],[4],[3],[2],[1],[0]]
Vetor3 = [[9],[0],[8],[1],[7],[2],[6],[3],[5],[4]]
Vetor4= []

for elemento in range(0, 10):
    Vetor4.append(Vetor1[elemento])
    Vetor4.append(Vetor2[elemento])
    Vetor4.append(Vetor3[elemento])

print(Vetor4)