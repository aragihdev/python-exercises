print("Calculadora IMC")
peso = float(input("Digite seu peso em quilos:"))
altura = float(input("Digite sua altura em metros:"))
altura2 = altura * altura
imc = peso / altura2

if imc <= 18.5:
    print(f"Sua classificação é: Abaixo do peso ({imc}).")
elif imc < 24.9:
    print(f"Sua classificação é: Peso normal ({imc}).")
elif imc < 29.9:
    print(f"Sua classificação é: Sobrepeso ({imc}).")
elif imc < 39.9:
    print(f"Sua classificação é: Obesidade ({imc}).")
else:
    print(f"Cuidado, sua classificação é Obesidade grave! ({imc})")