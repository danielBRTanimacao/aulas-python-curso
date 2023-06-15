# __dict__ e vars para atributos de instancia
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.name = nome
        self.age = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.age
    

dados = {'nome': 'bababui', 'idade': 19}
p1 = Pessoa(**dados)
# p1.__dict__['coisa'] = 'qualquer'
print(p1.__dict__)
print(p1.name)
# print(vars(p1))