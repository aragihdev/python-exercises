import time

print("Contagem regressiva orientada")

ini = int(input("Qual número dará inicio a contagem regressiva?"))

for contagem in range(ini, 0, -1):
    print(f"{contagem}")
    time.sleep(.5)