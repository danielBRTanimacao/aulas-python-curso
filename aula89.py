# dir, hasattr e getattr em Python

string = 'Bababui'
metodo = 'lower'

if hasattr(string, metodo):
    print(f'Existe {metodo}')
    print(getattr(string, metodo)())
else:
    print('Não existe esse metodo')