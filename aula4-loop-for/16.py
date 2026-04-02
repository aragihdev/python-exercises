print("Identificador de múltiplos")

num = int(input("Digite um número qualquer:"))
contm3 = 0
contm5 = 0

for i in range(1, num+1, 1):
    mult3 = int(i) % 3
    mult5 = int(i) % 5
    if mult3 == 0:
        contm3 += 1
        if mult5 == 0:
            contm5 += 1
    elif mult5 == 0:
        contm5 += 1
        if mult3 == 0:
            contm3 += 1
print(f"Entre 1 e {num} existem {contm3} múltiplos de 3 e {contm5} múltiplos de 5.")