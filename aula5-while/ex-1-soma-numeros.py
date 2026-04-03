print("Soma de números")

stop = 1
contagem = 0
while stop != 0:
    num = float(input("Digite o número que desejar somar:"))
    contagem += num
    print(f"Atualmente a soma está em {contagem}")
    if num == 0:
        stop = 0
print("Contagem finalizada!")