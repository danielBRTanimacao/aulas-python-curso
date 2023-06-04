#decoradores com parametros
def fab_decoradores(a=None, b=None, c=None): #cria decorador
    def function_fab(func): #decorador
        print('Decorador 1')

        def aninhada(*args, **kwargs): #funcao criada e executada
            print('Parametros do decorador', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return function_fab


@fab_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


decoradora = fab_decoradores()
vezes = decoradora(lambda x, y: x * y)
multiplicado = vezes(3, 4)
somados = soma(23, 2)
print(multiplicado)
print(somados)