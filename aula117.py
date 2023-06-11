import json

# pessoa = {
#     'nome': 'Bico',
#     'sobrenome': 'Seco',
#     'endereco': [
#         {'rua': 'Rua bababui', 'numero': 23},
#         {'rua': 'Rua pirilampo', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numero_preferido': (1, 2, 3, 4, 5, 6),
#     'dev': False,
#     'nada': None,
# }

# with open('aula117.json', 'w', encoding='utf-8') as arquivo:
#     json.dump(pessoa, arquivo, indent=2)

with open('aula117.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)