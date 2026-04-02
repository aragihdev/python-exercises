print("Classificação de notas")
nota = int(input("Digite a nota para avaliação:"))

if nota <= 59:
    print("Nota F")
elif nota <= 69:
    print("Nota D")
elif nota <= 79:
    print("Nota C")
elif nota <= 89:
    print("Nota B")
elif nota <= 100:
    print("Nota A")
else:
    print("Nota incorreta (maior que o possível).")