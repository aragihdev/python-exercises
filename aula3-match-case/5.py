print("Tradutor de cores para inglês")

color = str(input("Diga uma cor que deseja saber a tradução:")).lower()

match color:
    case "vermelho":
        language = str(input("Para qual língua deseja traduzir? (inglês, francês, alemão)")).lower()
        match language:
            case "ingles" | "inglês":
                print("Vermelho em inglês é Red.")
            case "frances" | "francês":
                print("Vermelho em francês é Rouge")
            case "alemao" | "alemão":
                print("Vermelho em alemão é Rot")
    case "azul":
        language = str(input("Para qual língua deseja traduzir? (inglês, francês, alemão)")).lower()
        match language:
            case "ingles" | "inglês":
                print("Vermelho em inglês é Red.")
            case "frances" | "francês":
                print("Vermelho em francês é Bleu")
            case "alemao" | "alemão":
                print("Vermelho em alemão é Blau")
    case "amarelo":
        language = str(input("Para qual língua deseja traduzir? (inglês, francês, alemão)")).lower()
        match language:
            case "ingles" | "inglês":
                print("Vermelho em inglês é Red.")
            case "frances" | "francês":
                print("Vermelho em francês é Jaune")
            case "alemao" | "alemão":
                print("Vermelho em alemão é Gelb")
    case "verde":
        language = str(input("Para qual língua deseja traduzir? (inglês, francês, alemão)")).lower()
        match language:
            case "ingles" | "inglês":
                print("Vermelho em inglês é Red.")
            case "frances" | "francês":
                print("Vermelho em francês é Vert")
            case "alemao" | "alemão":
                print("Vermelho em alemão é Grün")
    case "roxo":
        language = str(input("Para qual língua deseja traduzir? (inglês, francês, alemão)")).lower()
        match language:
            case "ingles" | "inglês":
                print("Vermelho em inglês é Red.")
            case "frances" | "francês":
                print("Vermelho em francês é Violet")
            case "alemao" | "alemão":
                print("Vermelho em alemão é Lila")