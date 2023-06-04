# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# decoradores são "Syntax sugar" açúcar sintatico

def cria_func(func): #função decoradora
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna


@cria_func
def invertedor(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string!')


invertida = invertedor('123')
print(invertida)