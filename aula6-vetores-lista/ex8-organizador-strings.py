print("Organizador de nomes")

menu = 1
nomes = []
while menu == 1:
    for i in range (5,0,-1):
        user_addname = input(f"Digite o {i}° nome da lista:")
        nomes.append(user_addname)
    nomes.sort()
    print(nomes)