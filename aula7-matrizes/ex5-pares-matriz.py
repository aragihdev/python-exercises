linhas = 3
colunas = 3
matriz = []
matrizPares = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        UserValue = float(input(f"Digite o valor para [{i}],[{j}]: "))
        if UserValue % 1 == 0:
            UserValue = int(UserValue)
        linha.append(UserValue)
    matriz.append(linha)
print("pares da matriz:")
for linha in matriz:
    for item in linha:
        if item % 2 == 0:
            matrizPares.append(item)
print(matrizPares)