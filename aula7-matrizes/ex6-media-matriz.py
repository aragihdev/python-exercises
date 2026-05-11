linhas = 3
colunas = 3
somaMatriz = 0
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        UserValue = float(input(f"Digite o valor para [{i}],[{j}]: "))
        if UserValue % 1 == 0:
            UserValue = int(UserValue)
        linha.append(UserValue)
    matriz.append(linha)
print("Matriz resultante:")
for linha in matriz:
    print(linha)
print("Soma da matriz:")
for linha in matriz:
    for item in linha:
        somaMatriz += item
print(somaMatriz / (len(matriz) * len(matriz)))