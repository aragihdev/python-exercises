import time

print("Contagem progressiva")

end = int(input("Até que número a contagem deve ir?"))

for contagem in range(1, end, 1):
    print(f"{contagem}")
    time.sleep(.5)