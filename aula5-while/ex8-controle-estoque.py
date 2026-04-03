print("Controle de estoque")
option = 'ask'
menu = 1
notebook = 0
desktop = 0
celular = 0
while menu == 1:
    option = input("O que deseja fazer (Entrada, Saída, exibição ou sair)?").lower()
    add = 0

    if option == 'entrada':
        print("Seção: Entrada de produtos ~")
        stay = input("Deseja seguir nesta seção? (Y/N)").lower()
        if stay == 'y':
            produto = input("Qual produto deseja adicionar? (notebook, desktop, celular):")
            if produto == 'notebook' or produto == 'desktop' or produto == 'celular':
                add = float(input(f"Digite quantos {produto} deseja adicionar ao estoque:"))
                if produto == 'notebook':
                    if add > 0:
                        notebook += add
                elif produto == 'desktop':
                    if add > 0:
                        desktop += add
                elif produto == 'celular':
                    if add > 0:
                        celular += add
            else:
                print(f"{produto} não um produto válido.")
        else:
            print("Voltando para seção inicial...")
    elif option == 'saida':
        print("Seção: Saída de produtos ~")
        stay = input("Deseja seguir nesta seção? (Y/N)").lower()
        if stay == 'y':
            produto = input("Qual produto deseja dar saída? (notebook, desktop, celular)")
            if produto == 'notebook' or produto == 'desktop' or produto == 'celular':
                saida = float(input(f"Digite quantos {produto} deseja dar saída do estoque:"))
                if produto == 'notebook':
                    if saida > 0:
                        if saida < notebook:
                            notebook -= saida
                elif produto == 'desktop':
                    if saida > 0:
                        if saida < desktop:
                            desktop -= saida
                elif produto == 'celular':
                    if add > 0:
                        if saida < celular:
                            celular -= saida
            else:
                print(f"{produto} não um produto válido.")
        else:
            print("Voltando para seção inicial...")
    elif option == 'exibição':
            print("Seção: Exibição")
            print(f"{notebook} unidades de notebook no estoque.")
            print(f"{desktop} unidades de desktop no estoque.")
            print(f"{celular} unidades de celular no estoque.")
    elif option == 'sair':
        print("Ok! Saindo do menu...")
        menu = 0
    else:
        print("Resposta inválida.")