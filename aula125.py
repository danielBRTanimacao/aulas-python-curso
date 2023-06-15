# Atributos de classe
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.name = nome
        self.age = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.age
    

p1 = Pessoa('Bababui', 10)
p2 = Pessoa('Sikibididop', 19)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())