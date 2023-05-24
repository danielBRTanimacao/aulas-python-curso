def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


duplica = executa(lambda mu: lambda nu: nu * mu, 2)
print(duplica(2))

print(executa(lambda x, y: x + y, 3, 3))

print(executa(lambda *soma: sum(soma), 3, 4, 5, 6, 5, 1))