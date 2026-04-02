print("Controle de estoque")
option = 'ask'
menu = 1
while menu == 1:
    while option == 'ask':
        option = input("O que deseja fazer (Entrada, Saída, exibição)?").lower()
    notebook = 0
    desktop = 0
    monitor = 0
    add = 0

    if option == 'entrada':
        print("Seção: Entrada de produtos ~")
        stay = input("Deseja seguir nesta seção? (Y/N)").lower()
        if stay == 'y':
            pass
        else:
            continue
        produto = input("Qual produto deseja adicionar? (notebook, desktop, monitor):")
        add = float(input(f"Digite quantos {produto} deseja adicionar ao estoque:"))
        if produto == 'notebook':
            if add > 0:
                notebook += add
                add = 0
        elif produto == 'desktop':
            if add > 0:
                desktop += add
                add = 0
        elif produto == 'monitor':
            if add > 0:
                monitor += add
                add = 0
        else:
            print(f"{produto} não um produto válido.")
    elif option == 'saida':
        print("Seção: Saída de produtos ~")
        produto = input("Qual produto deseja dar saída? (notebook, desktop, monitor")
        saida = float(input(f"Digite quantos {produto} deseja dar saída do estoque:"))
        if produto == 'notebook':
            if saida > 0:
                if saida < notebook:
                    notebook -= add
        elif produto == 'desktop':
            if saida > 0:
                if saida < desktop:
                    desktop -= add
        elif produto == 'monitor':
            if add > 0:
                if saida < monitor:
                    monitor += add
        else:
            print(f"{produto} não um produto válido.")
    elif option == 'exibição':
            print("Seção: Exibição")
            print(f"{notebook} unidades de notebook no estoque.")
            print(f"{desktop} unidades de desktop no estoque.")
            print(f"{monitor} unidades de monitor no estoque.")