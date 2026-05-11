linhas = 0
colunas = 0
matriz= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
diagMatriz= []
revDiagMatriz = []
for linha in matriz:
    linhas += 1
for coluna in matriz:
    colunas += 1
#DIAGONAL PRINCIPAL
if linhas == colunas:
    for i in range(0,linhas,1):
        diagMatriz.append(matriz[i][i])
#DIAGONAL REVERSA
if linhas == colunas:
    for i in range(0, linhas, 1):
        indiceColuna = (linhas-1) - i
        revDiagMatriz.append(matriz[i][indiceColuna])
print(diagMatriz)
print(revDiagMatriz)