# Escopo da classe e de metodos da classe
class Animal:
    def __init__(self, nome):
        self.nome = nome


    def comendo(self, alimento):
        return f'O {self.nome} esta comendo {alimento}!'
    
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


cavalo = Animal('cavalo')
print(cavalo.executar('maçâ'))