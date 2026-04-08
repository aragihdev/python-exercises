print("Reordenagem de números")

menu = 1
num_list = []
while menu == 1:
    user_number = float(input("Digite um número (digite '0' para encerrar): "))
    num_list.append(user_number)
    if user_number == 0:
        num_list.remove(0)
        for numero_atual in num_list[:]:
            if numero_atual % 1 == 0:
                num_list.remove(numero_atual)
                num_list.append(int(numero_atual))
        num_list.sort()
        print(f"Número em ordem crescente: {num_list}.")
        num_list.sort(reverse=True)
        print(f"Número em ordem decrescente: {num_list}.")