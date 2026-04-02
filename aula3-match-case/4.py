print("Listador de descontos")

produto = str(input("Qual produto você deseja comprar?")).lower()

match produto:
    case "eletronico" | "eletrônicos":
        value = float(input("Qual o valor desse eletrônico em reais?"))
        print(f"Este eletrônico está com 35% de desconto e irá custar R${value * 0.65}")
    case "roupas":
        value = float(input("Qual o valor das roupas em reais?"))
        print(f"As roupas estão com 13% de desconto e irá custar R${value * 0.87}")
    case "alimentos":
        value = float(input("Qual o valor dos alimentos em reais?"))
        print(f"Os alimentos estão com 20% de desconto e irá custar R${value * 0.80}")
    case "moveis" | "móveis":
        value = float(input("Qual o valor das roupas em reais?"))
        print(f"As roupas estão com 45% de desconto e irá custar R${value * 0.55}")