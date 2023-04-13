Vetor1 = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]
Vetor2 = [[9],[8],[7],[6],[5],[4],[3],[2],[1],[0]]

Vetor3= []

for elemento in range(0, 10):
    Vetor3.append(Vetor1[elemento])
    Vetor3.append(Vetor2[elemento])

print("Taboada do 9:",Vetor3)