#Ordem dos decoradores
def parametro_decorador(nome): 
    def decorador(func): 
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs): 
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador


@parametro_decorador(nome='segundo')
@parametro_decorador(nome='primeiro')
def soma(x, y):
    return x + y


somados = soma(23, 2)
print(somados)