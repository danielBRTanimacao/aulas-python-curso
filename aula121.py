# Metodos em instancia de classe Python
# Hard Code - algo escrito diretamente no codigo
class Carro:
    def __init__(self, nome):
        self.nome = nome


    def acelerar(self):
        print(f'O carro {self.nome} está acelerando...')


opala = Carro('Opala')
chevrolet = Carro('Chevete')

print(opala.nome)
chevrolet.acelerar()