print("Encontrar o máximo")

compare = 0
while True:
    numero = input("Digite um número para comparar aos próximos (digite 'sair' para encerrar):")
    if str(numero) == "sair":
        break
    elif float(numero) > compare:
        compare = float(numero)
    elif compare == 0:
        compare = float(numero)
    print(f"O maior número é até agora foi {compare}")
print("Comparação finalizada")
