print("Deletador de repetidos")

menu = 1
num_list = []
num_list_unique = []
while menu == 1:
    user_number = int(input("Digite um número inteiro (digite '0' para encerrar): "))
    num_list.append(user_number)
    if user_number == 0:
        num_list.remove(0)
        for numero_atual in num_list:
            if numero_atual not in num_list_unique:
                num_list_unique.append(numero_atual)
        print(f"Lista original: {num_list}.")
        print(f"Lista única: {num_list_unique}.")