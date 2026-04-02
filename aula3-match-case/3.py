print("Sistema de Login Simples")

login = str(input("Digite o login da conta:")).lower()

match login:
    case "admin":
        senha = str(input("Digite a senha da conta:"))
        match senha:
            case "admin":
                print("Login realizado com sucesso, acesso total liberado.")
            case _:
                print("Senha Incorreta")
    case "professor":
        senha = str(input("Digite a senha da conta:"))
        match senha:
            case "123":
                print("Login realizado com sucesso, acesso ao ambiente acadêmico liberado.")
            case _:
                print("Senha Incorreta")
    case "aluno":
        senha = str(input("Digite a senha da conta:"))
        match senha:
            case "123":
                print("Login realizado com sucesso, acesso ao ambiente de estudos liberado.")
            case _:
                print("Senha Incorreta")