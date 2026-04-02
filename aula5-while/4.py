print("Conversão de temperatura")

while True:
    celsius = (input("Digite uma temperatura em celsius para converter (apenas números):"))
    if celsius == str("sair"):
        break
    fahrenheit = (float(celsius) * 1.8) + 32
    print(f'{celsius}°C convertidos para Fahrenheit equivalem à {fahrenheit}°F. Para encerrar digite "sair".')
print("Conversão finalizada.")