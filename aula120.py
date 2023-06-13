# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


pessoa1 = Pessoa('baba', 'bui')
pessoa2 = Pessoa('cleitin', 'do grau')
# pessoa1.nome = 'baba'
# pessoa1.sobrenome = 'bui'

print(pessoa1.nome)
print(pessoa2.sobrenome)