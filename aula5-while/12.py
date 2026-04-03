print('Sistema de Vendas com Estoque Reduzido')

menu = 'estoque'
#estoque
perfume = 14
creme = 16
kitmaquiagem = 20
#preços
perfumepreco = 129.99
cremepreco = 59.99
kitmaquiagemprco = 189.99

while menu == 'estoque':
    print("Para visualizar o estoque atual digite 'estoque'")
    opcao = input("Qual produto deseja retirar do estoque?").lower().strip()
    match opcao:
        case 'estoque':
            print(f'{perfume} perfumes.')
            print(f'{creme} cremes.')
            print(f'{kitmaquiagem} kits de maquiagem.')
        case 'perfume' | 'perfumes':
            qtd_input = input("Quantos perfumes você deseja retirar do estoque?")
            if qtd_input.isdigit():
                qtd = int(qtd_input)
                if qtd > 0 and qtd <= perfume:
                    perfume -= qtd
                    print(f"{qtd} perfumes foram removidos do estoque! Restam {perfume} perfumes.")
                else:
                    print(f"Quantidade inválida, há apenas {perfume} perfumes no estoque.")
            else:
                print("Quantidade inválida, digite um número inteiro!")
        case 'creme' | 'cremes':
            qtd_input = input("Quantos cremes você deseja retirar do estoque?")
            if qtd_input.isdigit():
                qtd = int(qtd_input)
                if qtd > 0 and qtd <= creme:
                    creme -= qtd
                    print(f"{qtd} cremes foram removidos do estoque! Restam {creme} cremes.")
                else:
                    print(f"Quantidade inválida, há apenas {creme} cremes no estoque.")
            else:
                print("Quantidade inválida, digite um número inteiro!")
        case 'kitmaquiagem' | 'kit de maquiagem' | 'kits de maquiagem' | 'maquiagem' | 'kit':
            qtd_input = input("Quantos kits de maquiagem você deseja retirar do estoque?")
            if qtd_input.isdigit():
                qtd = int(qtd_input)
                if qtd > 0 and qtd <= kitmaquiagem:
                    kitmaquiagem -= qtd
                    print(f"{qtd} kits de maquiagem foram removidos do estoque! Restam {kitmaquiagem} kits de maquiagem.")
                else:
                    print(f"Quantidade inválida, há apenas {kitmaquiagem} kits de maquiagem no estoque.")
            else:
                print("Quantidade inválida, digite um número inteiro!")
        case _:
            print('Produto inválido...')