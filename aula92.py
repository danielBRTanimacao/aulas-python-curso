#Yild from
def gen1():
    yield 1
    yield 2
    yield 3
    yield 4
    print('Acabou GEN1')


def gen2(gen1):
    yield from gen1()
    yield 5
    yield 6
    yield 7
    yield 8
    print('Acabou GEN2')


def gen3():
    yield 9
    yield 10
    print('Acabou GEN3')


g1 = gen2(gen1)
g2 = gen2(gen3)
for num in g1:
    print(num)
for num in g2:
    print(num)