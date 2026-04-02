print("Simulação caixa eletrônico")
usuario = input("Digite o login:")
senha = input("Digite a senha:")
print(f"Olá {usuario}, você entrou com sucesso, seu saldo é de R$4.800,00")
op = int(input("Qual operação deseja realizar? (Saque = 1, Depósito = 2)"))
saldo = float(4800.00)

if op == 1:
    saque = float(input("Quanto deseja sacar?"))
    if saldo > saque:
        print(f"Saque realizado com sucesso! Saldo atual: R${saldo - saque}")
    else:
        print("Saldo insuficiente.")
elif op == 2:
    deposito = float(input("Quanto deseja depositar?"))
    print(f"Depósito realizado com sucesso! Saldo atual: R${saldo + deposito}.")
else:
    print("Opção inválida")