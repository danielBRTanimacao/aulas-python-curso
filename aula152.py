# Funções decoradoras e decoradores com metodos

def my_repr(self): #essa função pode estar fora ou dentro do add_repr
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'classe: {class_name}({class_dict})'
    return class_repr

def add_repr(cls):
    cls.__repr__ = my_repr
    return cls


def my_planet(method):
    def internal(self, *args, **kwargs): #decorador
        result = method(self, *args, **kwargs)

        if 'Terra' in result:
            return 'Você esta em casa!'
        return result
    return internal


@add_repr #decorador 'açucar sintatico'
class Team:
    def __init__(self, name):
        self.name = name


@add_repr
class Planet:
    def __init__(self, name):
        self.name = name
    
    @my_planet
    def say_name(self): #decorador
        return f'O planeta e {self.name}'


brasil = Team('Brasil')
portugal = Team('Portugal')

earth = Planet('Terra')
mars = Planet('Marte')

print(brasil)
print(earth)

print(earth.say_name())
print(mars.say_name())

