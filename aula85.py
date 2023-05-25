lista = []
for x in range(3):
    for y in range(2):
        lista.append((x, y))

lista = [
    (x, y) for x in range(3) for y in range(2)
]
print(lista)