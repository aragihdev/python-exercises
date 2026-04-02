print("Calculadora simples")

num1 = float(input("Qual o primeiro número da operação?"))
num2 = float(input("Qual o segundo número da operação"))
operation = str(input("Qual operação deseja realizar entre eles?"))

soma = num1 + num2
subt = num1 - num2
mult = num1 * num2
divi = num1 / num2

match operation:
    case "adição" | "adicao" | "+" | "soma" | "somar" | "adicionar":
        print(f"A soma de {num1} e {num2} é {soma}")
    case "subtração" | "subtracao" | "-" | "menos":
        print(f"A subtração de {num1} e {num2} é {subt}")
    case "multiplicação" | "multiplicacao" | "*" | "x" | "vezes":
        print(f"A multiplicação entre {num1} e {num2} é {mult}")
    case "divisão" | "divisao" | "/" | "dividir":
        print(f"A divisão entre {num1} e {num2} é {divi}")