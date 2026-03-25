print("Fatorial de um número")

num = int(input("Digite um número para saber seu fatorial:"))
fatorial = num

for i in range(num-1, 1, -1):
    fatorial *= int(i)

print(f"O fatorial de {num} é {fatorial}.")