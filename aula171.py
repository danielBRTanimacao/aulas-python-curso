# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).

import os
from itertools import count

caminho = os.path.join(
    'C:/', 'Users', 'danie', 'OneDrive', 'Área de Trabalho', 
    'vs estudo', 'testes_projetos_python', 'EXEMPLOS AULA 170'
)
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print(' ', the_counter, 'Dir:', dir_)
    
    for files_ in files:
        print(' ', the_counter, 'FILE:', files_)

    # APAGA TUDO DA PASTA
    # os.unlink(caminho)