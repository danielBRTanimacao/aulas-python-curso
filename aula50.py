"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
nomes_lista = ['Daniel', 'Bababui', 'Cleitin_doGrau']
nomes_lista.append('jose')

indices = range(len(nomes_lista))

for c in indices:               #type tipo de var
    print(c, nomes_lista[c], type(nomes_lista[c]))