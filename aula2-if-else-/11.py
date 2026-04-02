print("Categorizador de jogadores")
idade = int(input("Qual sua idade?"))

if idade <= 15:
    print("Você não tem a idade mínima para ser categorizado (16 anos).")
elif idade <= 20:
    print("Sua categoria é: Juvenil!")
elif idade <= 34:
    print("Sua categoria é: Adulto!")
else:
    print("Sua categoria é: Veterano!")