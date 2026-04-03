print("Soma de algarismos")

numerotext = input("Digite um número com 3 algarismos: ")
soma = 0

for digito in (numerotext):
    soma += int(digito)

print(f"O resultado da soma entre os algarismos de {numerotext} é {soma}")