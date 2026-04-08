print("Verificador de nomes")

menu = 1
while menu == 1:
    nomes = ["vicenzo", "joaquim", "rafael", "gabriel", "davi", "henrique"]

    guess = input("Tente adivinhar o nome:")

    if guess in nomes:
        print("Acertou.")
        menu = 0
    else:
        print("Errou, tente novamente...")
print("fim.")