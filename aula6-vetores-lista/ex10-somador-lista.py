print("Somador de lista")

user_num = 1
num_list = []
while user_num != 0:
    user_num = float(input("Digite um número para ser somado ao próximo (digite '0' para encerrar): "))
    num_list.append(user_num)
    print(f"{user_num} adicionado à contagem! Atualmente a soma resulta em: {sum(num_list)}.")
print(f"Soma encerrada!")
print(f"Números digitados: {num_list}.")