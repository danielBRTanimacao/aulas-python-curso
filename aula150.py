# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    try:
        print('Abrindo arquivo!')
        file = open(path, mode, encoding='utf-8')
        yield file
    # except Exception as e:
    #     print('Ocorreu o erro', e)
    finally:
        print('fechando arquivo')
        file.close()


with my_open('aula150.txt', 'w') as file:
    file.write('Bababui 1\n')
    file.write('skidibidop 2\n', 2)
    file.write('Bicô secõ 3\n')