print("Sistema de Atendimento Telefônico")

print("1 - Suporte Técnico")
print("2 - Financeiro")
print("3 - Cancelamento")
print("4 - Falar com atendente")

call = str(input("Selecione o serviço que deseja realizar:"))

match call:
    case "1":
        print("Bem vindo ao suporte técnico, qual o seu problema dentre os problema abaixo:")
        print("1 -Problemas com o site")
        print("2 -Problemas para realizar o login")
        print("3 -Recuperar senha")
        print("4 -Não está entre os acima (Falar com atendente)")
        userissue = str(input("Digite o dígito do problema:"))
        match userissue:
            case "1":
                print("FAQ sobre problemas com o site")
            case "2":
                print("FAQ sobre problema com o login")
            case "3":
                print("FAQ sobre problemas para recuperar a senha")
            case "4":
                print("Você está sendo encaminhado à chamada com o atendente...")
    case "2":
        print("Bem vindo ao suporte financeiro, o que deseja realizar?")
        print("1 - Emitir nota fiscal")
        print("2 - Visualizar o arquivo")
        print("3 - Registrar novo arquivo")
        print("4 - Não está entre os acima (Falar com atendente)")
        userissue = str(input("Digite o dígito do problema:"))
        match userissue:
            case "1":
                print("Aba de Emissão de nota fiscal:")
            case "2":
                print("Aba de visualização do arquivo:")
            case "3":
                print("Aba de registro de novos arquivos:")
            case "4":
                print("Você está sendo encaminhado à chamada com o atendente...")
    case "3":
        print("Bem vindo ao suporte para cancelamentos, o que deseja cancelar?")
        print("1 - Cancelamento de linha telefônica")
        print("2 - Cancelamento de email")
        print("3 - Cancelamento de CPF")
        print("4 - Não está entre os acima (Falar com atendente)")
        userissue = str(input("Digite o dígito do problema:"))
        match userissue:
            case "1":
                print("Aba de cancelamento de linha telefônica:")
            case "2":
                print("Aba de cancelamento de email:")
            case "3":
                print("Aba de cancelamento de CPF:")
            case "4":
                print("Você está sendo encaminhado à chamada com o atendente...")
    case "4":
        print("Você está sendo encaminhado à chamada com o atendente...")