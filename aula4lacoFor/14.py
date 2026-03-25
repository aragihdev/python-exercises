print("Maior e menor número da lista")
maior = 0
menor = 0

print("Comparador de 5 números:")

meio = float(input("Digite um número:"))

for i in range(0,4,1):
    num = int(input("Digite um número:"))
    if num >= meio:
        maior = num
    if num <= meio:
        menor = num
print(f"O maior dos 5 foi {maior} e o menor foi {menor}.")