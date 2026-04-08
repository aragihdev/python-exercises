print("Juntar listas sem repetir elementos")

menu = 1
list_one = []
list_two = []
while menu == 1:
    list_length = int(input("Quantos elementos terá cada lista?"))
    for lista in range(1,3):
        for elemento in range(list_length):
            user_string = input(f"digite o {elemento+1}° elemento da {lista}° lista: ")
            if lista == 1:
                list_one.append(user_string)
            if lista == 2:
                list_two.append(user_string)
    summed_list = list_one[:]
    for elemento in list_two:
        if elemento not in summed_list:
            summed_list.append(elemento)
    print(f"LISTA 1: {list_one}.")
    print(f"LISTA 2: {list_two}.")
    print(f"LISTA SOMADA SEM REPETIÇÕES: {summed_list}.")