print("Avaliador de alunos")

menu = 1
studnames = []
studgrades = []
studgradesapproved = []
studnamessapproved = []
studgradesfailed = []
studnamesfailed = []
while menu == 1:
    user_students = int(input("Quantos alunos deseja avaliar? "))
    if user_students > 0:
        for i in range(0,user_students):
            user_studname = input(f"Digite o nome do {i+1}° aluno: ")
            studnames.append(user_studname)
            while True:
                user_studgrade = float(input(f"Digite a nota do {user_studname}: "))
                if user_studgrade < 11 and user_studgrade >= 0:
                    studgrades.append(user_studgrade)
                    break
                else:
                    print(f"Nota do {user_studname} inválida! Deve ser entre 0 e 10.")
    elif user_students < 1:
        print("Número de alunos inválido! Tente novamente...")
    print(f"Alunos: {studnames}")
    print(f"Notas: {studgrades}")
    for estudante_atual in range(len(studgrades)):
        if studgrades[estudante_atual] > 5.9:
            studgradesapproved.append(studgrades[estudante_atual])
            studnamessapproved.append(studnames[estudante_atual])
        elif studgrades[estudante_atual] < 6:
            studgradesfailed.append(studgrades[estudante_atual])
            studnamesfailed.append(studnames[estudante_atual])
    #print(f"Aluno aprovados: {studnamessapproved}.")
    #print(f"Notas respectivas: {studgradesapproved}.")
    #print(f"Aluno reprovados: {studnamesfailed}.")
    #print(f"Notas respectivas: {studgradesfailed}")
    print("")
    print("APROVADOS")
    print("")
    for i in range(len(studgradesapproved)):
        print(f"{studnamessapproved[i]} com média {studgradesapproved[i]}")
    print("")
    print("REPROVADOS")
    print("")
    for i in range(len(studgradesfailed)):
        print(f"{studnamesfailed[i]} com média {studgradesfailed[i]}")
    print("")