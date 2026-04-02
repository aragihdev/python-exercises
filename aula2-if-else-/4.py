print("Calculadora")
n1 = float(input("Digite um número:"))
n2 = float(input("Digite o segundo:"))
operation = str(input("O que quer fazer com eles? (somar, subtrair, dividir ou multiplicar):"))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

if operation == "somar":
    print(f"A soma de {n1} e {n2} é {soma}")
elif operation == "subtrair":
    print(f"A subtração de {n1} e {n2} é {sub}")
elif operation == "multiplicar":
    print(f"A multiplicação de {n1} e {n2} é {mult}")
elif operation == "dividir":
    print(f"A divisão de {n1} e {n2} é {div}.")