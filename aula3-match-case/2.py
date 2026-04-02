print("Calculador de área de formas geométricas")

while True:
    forma = str(input("Qual a forma que você quer a área?")).lower()

    match forma:
        case "quadrado":
            qdr = float(input("Quanto tem um dos lados deste quadrado em centímetros?"))
            print(f"A área do quadrado é {qdr * 2}cm")
        case "retangulo" | "retângulo":
            ret1 = float(input("Quanto tem a base do retângulo em centímetros?"))
            ret2 = float(input("Quanto de altura tem o retângulo em centímetros?"))
            print(f"A área do retângulo é {ret1 * ret2}cm")
        case "triangulo" | "triângulo":
            tri1 = float(input("Quanto tem a base do triângulo em centímetros?"))
            tri2 = float(input("Quanto de altura tem o triângulo em centímetros?"))
            print(f"A área do triângulo é {(tri1 * tri2) / 2}cm")
        case _:
            print("Essa não é uma forma geométrica válida")