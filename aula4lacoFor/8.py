from statistics import median

print("Calculador de média 5 números")
somanotas = 0
quantidade = 5

for i in range(quantidade):
    nota = float(input(f"Digite a {i+1} nota:"))
    somanotas += nota

media = somanotas / quantidade
print(media)