print("Identificador de múltiplos")

num = int(input("Digite um número qualquer:"))
contm3 = 0
contm5 = 0

for i in range(1, num+1, 1):
    mult3 = int(i) % 3
    mult5 = int(i) % 5
    if mult3 == 0:
        if mult5 == 0:
            print(f"O número {i} é múltiplo de 3 e de 5 ao mesmo tempo!")
            contm3 += 1
            contm5 += 1
        else:
            print(f"O número {i} é múltiplo de 3.")
            contm3 += 1
    elif mult5 == 0:
        if mult3 == 0:
            print(f"O número {i} é múltiplo de 3 e de 5 ao mesmo tempo!")
            contm5 += 1
            contm3 += 1
        else:
            print(f"O número {i} é múltiplo de 5.")
            contm5 += 1
print(f"Entre 1 e {num} existem {contm3} múltiplos de 3 e {contm5} múltiplos de 5.")