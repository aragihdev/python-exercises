print("Diferenciador - pares e impares")
menu = 1
numbers_even = []
numbers_odds = []

while menu == 1:
    for i in range (10,0,-1):
        user_number = int(input(f"Digite o {i}° número inteiro da lista:"))
        if user_number % 2 == 0:
            numbers_even.append(user_number)
        else:
            numbers_odds.append(user_number)
    print(f"Pares = {numbers_even}.")
    print(f"Ímpares = {numbers_odds}.")
