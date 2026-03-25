print("Identificador de números primos")

num = int(input("Digite um número qualquer para saber se é primo:"))
primo = 0
for i in range(2,num, 1):
    if num % int(i) == 0:
        primo = 1

if primo == 1:
    print(f"{num} não é primo!")
else:
    print(f"{num} é primo!")