import time
print("Removedor de números negativos")

menu = 1
num_list = []
while menu == 1:
    user_number = int(input("Digite um número inteiro: "))
    num_list.append(user_number)
    if user_number == 0:
        for numero_atual in num_list[:]:
            if numero_atual < 0:
                num_list.remove(numero_atual)
        num_list.remove(0)
        print(num_list)