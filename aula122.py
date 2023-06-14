# Entendendo o self em classes python
# Classe - molde geralmente sem dados 
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar varias instâncias
# Na classe o self e a propria instãncia

class Carro:
    def __init__(self, nome):
        self.nome = nome


    def acelerar(self):
        print(f'O carro {self.nome} está acelerando...')


opala = Carro('Opala')
chevrolet = Carro('Chevete')

Carro.acelerar(opala)
print(opala.nome)
chevrolet.acelerar()