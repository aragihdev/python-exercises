print("Adivinhação de número!")
random = hash("random")
sorteio = None

# Aleatorizador caseiro sem usar import random
if random % 5 == 0:
    sorteio = 1
elif random % 7 == 0:
    sorteio = 2
elif random % 9 == 3:
    sorteio = 3
elif (random - 10) % 3:
    sorteio = 4
elif random % 2 == 0:
    sorteio = 5
elif random % 11 == 0:
    sorteio = 6
elif random % 10 in [3, 7]:
    sorteio = 7
elif (random >> 4) & 1:
    sorteio = 8
elif (random * 2) % 15 < 5:
    sorteio = 9
elif not (random % 4 == 0):
    sorteio = 10

chances = 5
for i in range(1,chances+1,1):
    num = int(input("Escolha um número de 1 a 10 (5 chances para acertar):"))
    if num > 10:
        print("O numero deve ser menor que 10!")
        num = int(input("Escolha um número de 1 a 10:"))
    elif num < 1:
        print("O número deve ser maior que 0")
        num = int(input("Escolha um número de 1 a 10:"))
    if num == sorteio:
        print(f"Você acertou o número!!")
        chances = 0
    else:
        print("Número errado... Tente novamente!")
