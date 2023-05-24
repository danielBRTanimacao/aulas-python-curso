# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

(a1, a2), b = pessoa.items() 
print(a1, b)

for value in pessoa.items():
    print(value[0])
    