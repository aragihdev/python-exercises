print("Controle de estoque")
option = 'ask'
while option == 'ask':
    option = input("O que deseja fazer (Entrada, Saída, exibição)?").lower()
notebook = 0
desktop = 0
monitor = 0
stay = 'a'

while option == 'entrada':
    print("Seção: Entrada de produtos ~")
    stay = input("Deseja continuar nesta seção? (Y/N)").lower()
    if stay == 'n':
        option = 'ask'
    if stay != 'y':
        print(f"{stay} não é uma opção válida.")
    produto = input("Qual produto deseja adicionar? (notebook, desktop, monitor")
    add = float(input(f"Digite quantos {produto} deseja adicionar ao estoque:"))
    if produto == 'notebook':
        if add > 0:
            notebook += add
    elif produto == 'desktop':
        if add > 0:
            desktop += add
    elif produto == 'monitor':
        if add > 0:
            monitor += add
    else:
        print(f"{produto} não um produto válido.")
while option == 'saida':
    print("Seção: Saída de produtos ~")
    produto = input("Qual produto deseja dar saída? (notebook, desktop, monitor")
    saida = float(input(f"Digite quantos {produto} deseja dar saída do estoque:"))
while option == 'exibição':
    print("Seção: Exibição")
    print(f"")