print("Aplicador de desconto")
produto = float(input("Digite o preço do produto desejado:"))

if produto >= 101:
    desconto = produto * 0.90
    print(f"O produto está com desconto, custará R${desconto}")
else:
    print(f"O produto não está em desconto, custará R${produto}")