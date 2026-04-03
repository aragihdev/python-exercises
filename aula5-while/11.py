print("Simulador de Caixa Registradora")
menu = 'caixa'
loopcheck = 0
total = 0
cafepreco = 24.99
suspiropreco = 9.99
paomilhopreco = 13.99
cafe = 0
suspiro = 0
paomilho = 0
print("Opções de produto:")
print("Café de alpino - R$24,99")
print("Suspiro - R$9,99")
print("Pão de milho - R$13,99")
print("")
print("Para ver o carrinho digite 'carrinho' e 'caixa' para encerrar a compra.")
while menu == 'caixa':
    produto = input("Qual produto deseja comprar?").lower().strip()
    match produto:
        case 'café de alpino' | 'cafe de alpino' | 'cafe' | 'alpino' | 'cafe alpino' | 'café alpino' :
            qtd = int(input("Quantos cafés de alpino deseja adquirir?"))
            if qtd > 0 and qtd == 1:
                total += (cafepreco * qtd)
                cafe += qtd
                print(f"{qtd} café de alpino adicionado ao carrinho.")
            elif qtd > 1:
                total += (cafepreco * qtd)
                cafe += qtd
                print(f"{qtd} cafés de alpino adicionados ao carrinho.")
            else:
                print("Quantidade inválida, tente novamente.")
        case 'suspiro':
            qtd = int(input("Quantos suspiros deseja adquirir?"))
            if qtd > 0 and qtd == 1:
                total += (suspiropreco * qtd)
                suspiro += qtd
                print(f"{qtd} suspiro adicionado ao carrinho.")
            elif qtd > 1:
                total += (suspiropreco * qtd)
                suspiro += qtd
                print(f"{qtd} suspiros adicionados ao carrinho.")
            else:
                print("Quantidade inválida, tente novamente.")
        case 'pão de milho' | 'pao de milho' | 'pão' | 'pao':
            qtd = int(input("Quantos pães de milho deseja adquirir?"))
            if qtd > 0 and qtd == 1:
                total += (paomilhopreco * qtd)
                paomilho += qtd
                print(f"{qtd} pão de milho adicionado ao carrinho.")
            elif qtd > 1:
                total += (paomilhopreco * qtd)
                paomilho += qtd
                print(f"{qtd} pães de milho adicionados ao carrinho.")
            else:
                print("Quantidade inválida, tente novamente.")
        case 'carrinho':
            print(f"Café de alpino - {cafe} (R${cafe * cafepreco})")
            print(f"Suspiro - {suspiro} (R${suspiro * suspiropreco})")
            print(f"Pão de milho - {paomilho} (R${paomilho * paomilhopreco})")
            print("para remover algum produto digite 'remover'.")
        case 'remover':
            remove = input('Qual produto deseja remover do carrinho?')
            match remove:
                case 'café de alpino' | 'cafe de alpino' | 'cafe' | 'alpino' | 'cafe alpino' | 'café alpino':
                    qtd = int(input(f"Quantos cafés deseja remover do carrinho?"))
                    if qtd > 0 and qtd < cafe and qtd == 1:
                        print(f"{qtd} café de alpino removido do carrinho")
                        total -= (cafepreco * qtd)
                        cafe -= qtd
                    elif qtd > 0 and qtd < cafe:
                        print(f"{qtd} cafés de alpino removidos do carrinho")
                        total -= (cafepreco * qtd)
                        cafe -= qtd
                case 'suspiro':
                    qtd = int(input(f"Quantos suspiros deseja remover do carrinho?"))
                    if qtd > 0 and qtd < suspiro and qtd == 1:
                        print(f"{qtd} suspiro removido do carrinho")
                        total -= (suspiropreco * qtd)
                        suspiro -= qtd
                    elif qtd > 0 and qtd < suspiro:
                        print(f"{qtd} suspiros removidos do carrinho")
                        total -= (suspiropreco * qtd)
                        suspiro -= qtd
                case 'pão de milho' | 'pao de milho' | 'pão' | 'pao':
                    qtd = int(input(f"Quantos pães de milho deseja remover do carrinho?"))
                    if qtd > 0 and qtd < paomilho and qtd == 1:
                        print(f"{qtd} pão de milho removido do carrinho")
                        total -= (paomilhopreco * qtd)
                        paomilho -= qtd
                    elif qtd > 0 and qtd < paomilho:
                        print(f"{qtd} pães de milho removidos do carrinho")
                        total -= (paomilhopreco * qtd)
                        paomilho -= qtd
        case 'caixa':
            menu = 'final'
        case _:
            print('Opção inválida, tente novamente.')
while menu == 'final' and loopcheck == 0:
    print(f"Café de alpino - {cafe}")
    print(f"Suspiro - {suspiro}")
    print(f"Pão de milho - {paomilho}")
    print(f"Total da compra R${total}")
    loopcheck += 1