# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
#print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


# lista = []
# for num in range(0, 10):
#     lista.append(num)
#print(lista)

# lista = [num for num in range(0, 10)]
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
    {'nome': 'p4', 'preco': 22, },
    {'nome': 'p5', 'preco': 55, },
]

#p(novos_produtos)
#lista = [n for n in range(1, 11) if n < 4]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]
p(novos_produtos)
