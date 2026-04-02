adminlogin = "admin"
adminsenha = "admin"

print("Sistema de login")
usuario = str(input("Digite o login:"))

if usuario == adminlogin:
    senha = str(input("Digite a senha:"))
    if senha == adminsenha:
        print("Você entrou com sucesso.")
    else:
        print("Senha incorreta.")
else:
    print("Login incorreto")
