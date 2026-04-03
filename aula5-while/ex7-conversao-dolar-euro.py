print("Conversor de dólares para euros")

while True:
    dolar = float(input("Digite uma quantia em dólares para converter (insira '0' para encerrar):"))
    if dolar == 0:
        break
    euro = float(dolar) * 0.86
    print(f"${dolar} equivalem à €{euro}.")
print("Conversão encerrada.")