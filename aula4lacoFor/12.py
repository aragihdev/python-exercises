print("Tabuada personalizada")

num = int(input("Digite um número para saber sua tabuada:"))

for i in range(0,11,1):
    multi = int(i) % 3
    multi2 = num % 3
    if multi or multi2 == 0:
        print(f"{num} x {i} = {num*int(i)} e é múltiplo de três!")
    else:
        print(f"{num} x {i} = {num*int(i)}")