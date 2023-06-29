# Funções decoradoras e decoradores com classes
def my_repr(self): #essa função pode estar fora ou dentro do add_repr
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'classe: {class_name}({class_dict})'
    return class_repr

def add_repr(cls):
    cls.__repr__ = my_repr
    return cls


@add_repr #decorador 'açucar sintatico'
class Team:
    def __init__(self, name):
        self.name = name


@add_repr
class Planet:
    def __init__(self, name):
        self.name = name


@add_repr
class Language:
    def __init__(self, name):
        self.name = name


brasil = Team('Brasil')
portugal = Team('Portugal')

earth = Planet('Terra')
mars = Planet('Marte')

portuguese = Language('Português')
spanish = Language('Espanhol')

print(brasil)
print(earth)
print(portuguese)
