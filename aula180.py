# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w', encoding='utf-8') as arquivo:
    colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas
    )
    escritor.writeheader() # manda escrever o header

    for cliente in lista_clientes:
        escritor.writerow(cliente)

# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['Luiz Otávio', 'Av 1, 22'],
# ]

# with open(CAMINHO_CSV, 'w', encoding='utf-8') as arquivo:
#     # colunas = lista_clientes[0].keys()
#     colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(colunas)

#     for cliente in lista_clientes:
#         print(cliente)
#         escritor.writerow(cliente)
