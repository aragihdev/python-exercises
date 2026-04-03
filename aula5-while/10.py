print("Controle de votação")
bonoro = 0
lule = 0
aidt = 0
davi = 0
gabriel = 0
joaquim = 0
presidentecheck = 0
prefeitocheck = 0
menu = 'votacao'
print("Para ver os candidatos disponíveis digite 'ajuda'.")
while menu == 'votacao':
    choice = input("Qual cargo deseja votar (presidente, prefeito):").lower()
    if choice == 'presidente' and presidentecheck == 0:
        voto = input("Para qual presidente deseja votar?")
        if voto == 'ajuda':
            print("Bonoro - 022")
            print("Lule - 013")
            print("Aí dento - 069")
        elif voto != 'ajuda' and presidentecheck == 0:
            if voto == '022':
                confirm = input("Deseja votar em Bonoro? (S/N):").lower()
                if confirm == 's':
                    print("Voto validado")
                    bonoro += 1
                    presidentecheck +=1
                elif confirm == 'n':
                    print("Voto cancelado")
                else:
                    print("Resposta inválida")
            if voto == '013':
                confirm = input("Deseja votar em Lule? (S/N):").lower()
                if confirm == 's':
                    print("Voto validado")
                    bonoro += 1
                    presidentecheck +=1
                elif confirm == 'n':
                    print("Voto cancelado")
                else:
                    print("Resposta inválida")
            if voto == '069':
                confirm = input("Deseja votar em Aí dento? (S/N):").lower()
                if confirm == 's':
                    print("Voto validado")
                    bonoro += 1
                    presidentecheck +=1
                elif confirm == 'n':
                    print("Voto cancelado")
                else:
                    print("Resposta inválida")
        else:
            print("Resposta inválida")
    elif presidentecheck != 0:
        print("Você não pode votar duas vezes para o mesmo cargo!")
    if choice == 'prefeito' and prefeitocheck == 0:
        voto = input("Para qual prefeito deseja votar?")
        if voto == 'ajuda':
            print("Davi - 073")
            print("Gabriel - 090")
            print("Joaquim - 101")
        elif voto != 'ajuda' and prefeitocheck == 0:
            if voto == '073':
                confirm = input("Deseja votar em Davi para prefeito? (S/N):").lower()
                if confirm == 's':
                    print("Voto validado")
                    davi += 1
                    presidentecheck +=1
                elif confirm == 'n':
                    print("Voto cancelado")
                else:
                    print("Resposta inválida")
            if voto == '090':
                confirm = input("Deseja votar em Gabriel para prefeito? (S/N):").lower()
                if confirm == 's':
                    print("Voto validado")
                    gabriel += 1
                    presidentecheck +=1
                elif confirm == 'n':
                    print("Voto cancelado")
                else:
                    print("Resposta inválida")
            if voto == '101':
                confirm = input("Deseja votar em Joaquim para prefeito? (S/N):").lower()
                if confirm == 's':
                    print("Voto validado")
                    joaquim += 1
                    presidentecheck +=1
                elif confirm == 'n':
                    print("Voto cancelado")
                else:
                    print("Resposta inválida")
        else:
            print("Resposta inválida")
    elif prefeitocheck != 0:
        print("Você não pode votar duas vezes para o mesmo cargo!")