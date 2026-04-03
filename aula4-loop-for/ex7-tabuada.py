print("Tabuada")

num = int(input("De qual número você deseja saber a tabuada?"))

print(f"A tabuada de {num} é:")
for contagem in range(1, 11, 1):
    print(f"{num} x {contagem} = {num * contagem}")
