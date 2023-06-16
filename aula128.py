# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_da_classe(cls):
        print('Bababui')

    @classmethod
    def create_50_age(cls, nome):
        return cls(nome, 50)

    @classmethod
    def create_no_name(cls, idade):
        return cls('Anônimo', idade)


p1 = Pessoa('Cleitin do grau', 25)
p2 = Pessoa.create_50_age('Bababui')
p3 = Pessoa.create_no_name(23)
print(p3.nome)
# print(p2.nome, p2.idade)
# print(Pessoa.ano)
# Pessoa.metodo_da_classe()