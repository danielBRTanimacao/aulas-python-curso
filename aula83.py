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

dados_totais = {
    **pessoa,
    **dados_pessoa,
    'nome2': 'Piru'
}

def mostrar_args(*args, **kwargs):
    print(f'Não nomeados {args}')
    for keys, valor in kwargs.items():
        print(keys, valor)


#mostrar_args(**dados_totais)
#print(dados_totais)

#(a1, a2), b = pessoa.items() 
#print(a1, b)

#for value in pessoa.items():
#    print(value[0])
    
dados = {
    'n1': 'bubu',
    'n2': 'bobo',
    'n3': 'bibi',
    'n4': 'cucu',
    'n5': 'gogogo'
}

mostrar_args(**dados)