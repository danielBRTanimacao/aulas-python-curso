#map - para mapear dados
from functools import partial

def print_iter(iteretor):
    print(*list(iteretor), sep='\n')
    print()


def aum_porcentagem(value, porcentagem):
    res = round(value * porcentagem)
    return f'R${res:.2f}'


aumento_de_porcentagem = partial(aum_porcentagem, porcentagem=1.1)

produtos = [
    {'nome': 'produto 5', 'preco': 10.50},
    {'nome': 'produto 4', 'preco': 12.35},
    {'nome': 'produto 3', 'preco': 2.00},
    {'nome': 'produto 2', 'preco': 100.20},
    {'nome': 'produto 1', 'preco': 22.99},
]

# novos_produtos = [
#     {**p, 'preco': aumento_de_porcentagem(p['preco'])} for p in produtos
# ]
def muda_preco_produto(produto):
    return {**produto, 'preco': aumento_de_porcentagem(produto['preco'])}


novos_produtos = map(muda_preco_produto, produtos)

#print_iter(novos_produtos)
print(
    list(
        map(
            lambda value: value * 2, [1, 2, 3, 4]
            )
        )
)