# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(lista1, lista2): SOLUÇÃO 1
#     interval_max = min((len(lista1)), len(lista2))
#     return [(lista1[indice], lista2[indice]) for indice in range(interval_max)]
#
#
# print(zipper(lista1, lista2))

#print(list(zip(lista1, lista2))) SOLUÇÃO 2

from itertools import zip_longest #SOLUÇÃO 3

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip_longest(lista1, lista2, fillvalue='Sem cidade')))