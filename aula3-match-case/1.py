print("Conversor de moedas diversas para BRL")

while True:
    currency = str(input("Qual a moeda do valor que você tem (USD, EUR, GBP)")).lower()
    value = float(input("Qual o valor que deve ser convertido?"))

    USDBR = value * 5
    EURBR = value * 6
    GBPBR = value * 7

    match currency:
        case "usd":
            print(f"Seus {currency}{value} em reais são R${USDBR}")
        case "eur":
            print(f"Seus {currency}{value} em reais são R${EURBR}")
        case "gbp":
            print(f"Seus {currency}{value} em reais são R${GBPBR}")