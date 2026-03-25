print("Identificador de números personalizado")
positive = 0
negative = 0
neutral = 0

for i in range(0,10,1):
    num = float(input("Digite qualquer número (pode ser negativo):"))
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        neutral += 1
print(f"{positive} foram positivos, {negative} foram negativos e {neutral} foram iguais a 0.")
