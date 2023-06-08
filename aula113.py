# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]
# def func_reduce(acumulador, produto):
#     return acumulador + produto['preco']


total = reduce(lambda acumulador, produtos: acumulador + produtos['preco'], produtos, 0)
#print(sum(p['preco'] for p in produtos))
print(total)