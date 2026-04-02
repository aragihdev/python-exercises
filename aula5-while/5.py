print("Simulador de caixa eletrônico")

saldo = 2500
while saldo != 0:
    print(f"Saldo atual: R${saldo}")
    saque = float(input("Digite um valor para sacar:"))
    if saque < 2500 and saque > 0:
        saldo -= saque
    else:
        print("Saque inválido.")
print("Caixa fechado.")