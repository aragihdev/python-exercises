print("Números impares e pares")
ini = int(input("Escolha o primeiro número da contagem:"))
end = int(input("Escolha o último número da contagem:"))

for i in range(ini,end+1,1):
    par = int(i) % 2
    if par == 0:
        print(f"o número {i} é par!")
    else:
        print(f"o número {i} é impar!")