# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(value=0, maximo=10):
    while True:
        yield value
        value += 1

        if value > maximo:
            return


gen = generator(6, 7)
print(next(gen))
for num in gen:
    print(num)