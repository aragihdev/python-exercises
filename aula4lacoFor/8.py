from statistics import median
somanotas = 0
quantidade = 5

print(f"Calculador de média {quantidade} números")


for i in range(quantidade):
    nota = float(input(f"Digite a {i+1} nota:"))
    somanotas += nota

media = somanotas / quantidade
print(media)