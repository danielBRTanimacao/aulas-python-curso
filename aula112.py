def print_iter(iteretor):
    print(*list(iteretor), sep='\n')
    print()


produtos = [
    {'nome': 'produto 5', 'preco': 10.50},
    {'nome': 'produto 4', 'preco': 12.35},
    {'nome': 'produto 3', 'preco': 2.00},
    {'nome': 'produto 2', 'preco': 100.20},
    {'nome': 'produto 1', 'preco': 22.99},
]
#novos_produtos = [prod for prod in produtos if prod['preco'] >= 15]
novos_produtos = filter(lambda product: product['preco'] > 10, produtos)

print_iter(novos_produtos)
