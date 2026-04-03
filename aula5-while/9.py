print("Simulação de sensor de dados")

invalid = 0
while invalid < 3:
    num = float(input("Digite um valor:"))
    if num < 0 or num > 100:
        print(f"Dado invalido (restam {2 - invalid} erros).")
        invalid += 1
    else:
        print("Dado armazenado.")
if invalid == 3:
    print("Erros máximos alcançados, sistema finalizado.")