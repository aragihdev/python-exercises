print("Jogo da velha")
def jogoDaVelha():
    for i in range(0,len(plano)):
        print(plano[i])
plano = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
jogoDaVelha()
timesPlayed = 0
gameRunning = 1
while gameRunning == 1:
    for i in range(0,9):
        SuaVez = 1
        while SuaVez == 1:
            while True:
                user1Linha = int(input("Em qual linha deseja fazer o X? (1,2,3) "))
                if user1Linha < 4 and user1Linha >= 1:
                    break
                else:
                    print("Número inválido")
            while True:
                user1Coluna = int(input("Em qual coluna deseja fazer o X? (1,2,3) "))
                if user1Coluna < 4 and user1Coluna >= 1:
                    break
                else:
                    print("Número inválido")
            if plano[user1Linha -1][user1Coluna -1] == "X" or plano[user1Linha -1][user1Coluna -1] == "O":
                print("Posição inválida, tente novamente")
            else:
                plano[user1Linha -1][user1Coluna -1] = "X"
                break
                SuaVez = 0
        jogoDaVelha()
        timesPlayed += 1
        # horizontal
        if plano[0][0] == plano[0][1] == plano[0][2] and plano[0][0] != "-":
            gameRunning = 0
        if plano[1][0] == plano[1][1] == plano[1][2] and plano[1][0] != "-":
            gameRunning = 0
        if plano[2][0] == plano[2][1] == plano[2][2] and plano[2][0] != "-":
            gameRunning = 0
        # vertical
        if plano[0][0] == plano[1][0] == plano[2][0] and plano[0][0] != "-":
            gameRunning = 0
        if plano[0][1] == plano[1][1] == plano[2][1] and plano[0][1] != "-":
            gameRunning = 0
        if plano[0][2] == plano[1][2] == plano[2][2] and plano[0][2] != "-":
            gameRunning = 0
        # diagonal
        if plano[0][0] == plano[1][1] == plano[2][2] and plano[0][0] != "-":
            gameRunning = 0
        if plano[0][2] == plano[1][1] == plano[2][0] and plano[0][2] != "-":
            gameRunning = 0
        # vitoria
        if gameRunning == 0 or timesPlayed == 9:
            print("Jogo finalizado.")
            break
        SuaVez = 1
        while SuaVez == 1:
            while True:
                user2Linha = int(input("Em qual linha deseja fazer o O? (1,2,3) "))
                if user2Linha < 4 and user2Linha >= 1:
                    break
                else:
                    print("Número inválido")
            while True:
                user2Coluna = int(input("Em qual coluna deseja fazer o O? (1,2,3) "))
                if user2Coluna < 4 and user2Coluna >= 1:
                    break
                else:
                    print("Número inválido")
            if plano[user2Linha -1][user2Coluna -1] == "X" or plano[user2Linha -1][user2Coluna -1] == "O":
                print("Posição inválida, tente novamente")
            else:
                plano[user2Linha -1][user2Coluna -1] = "O"
                break
                SuaVez = 0
        jogoDaVelha()
        timesPlayed += 1
        # horizontal
        if plano[0][0] == plano[0][1] == plano[0][2] and plano[0][0] != "-":
            gameRunning = 0
        if plano[1][0] == plano[1][1] == plano[1][2] and plano[1][0] != "-":
            gameRunning = 0
        if plano[2][0] == plano[2][1] == plano[2][2] and plano[2][0] != "-":
            gameRunning = 0
        # vertical
        if plano[0][0] == plano[1][0] == plano[2][0] and plano[0][0] != "-":
            gameRunning = 0
        if plano[0][1] == plano[1][1] == plano[2][1] and plano[0][1] != "-":
            gameRunning = 0
        if plano[0][2] == plano[1][2] == plano[2][2] and plano[0][2] != "-":
            gameRunning = 0
        # diagonal
        if plano[0][0] == plano[1][1] == plano[2][2] and plano[0][0] != "-":
            gameRunning = 0
        if plano[0][2] == plano[1][1] == plano[2][0] and plano[0][2] != "-":
            gameRunning = 0
        # vitoria
        if gameRunning == 0 or timesPlayed == 9:
            print("Jogo finalizado.")
            break