print("Soma de números pares e ímpares")

num = int(input("Digite um número:"))
print("Contagem de números ímpares até o escolhido:")
for i in range(0,num,1):
    impcheck = i % 2
    if impcheck != 0:
        print(f"{i}")

print("Contagem de números pares até o escolhido:")
for i in range(0,num+1,2):
    print(f"{i}")