# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)
from typing import Any


def my_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.__repr__ = my_repr

        if 'say' not in cls.__dict__ or not callable(cls.__dict__['say']):
            raise NotImplementedError('Implementa o metodo "say"!')

        return cls
    
    def __call__(self, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        print(instance.__dict__)

        if 'name' not in instance.__dict__:
            raise NotImplementedError('Implemente o atributo "name"!')

        return instance

    
class Person(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('Meu NEW')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print('Meu INIT')
        self.name = name
    
    def say(self):
        print('Falando...')


person1 = Person('Bababui')
print(person1)
