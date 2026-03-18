import time

print("Contagem personalizada")

ini = int(input("Qual número dará inicio a contagem?"))
end = int(input("Qual número será o último da contagem?"))
pas = int(input("Qual será o passo da contagem?"))

for contagem in range(ini, end, pas):
    print(f"{contagem}")
    time.sleep(.5)