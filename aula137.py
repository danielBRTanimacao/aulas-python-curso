# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0

print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

supra = Carro('Supra')
toyota = Fabricante('Toyota')
motor_potente = Motor('seis cilindros em linha com 340 cv')
supra.fabricante = toyota
supra.motor = motor_potente

print(f'Nome: {supra.nome} Fabricante: {supra.fabricante.nome} Motor: {supra.motor.nome}')

uno = Carro('Uno')
fiat = Fabricante('Fiat')
uno.fabricante = fiat
uno.motor = motor_1_0

print(f'Nome: {uno.nome} Fabricante: {uno.fabricante.nome} Motor: {uno.motor.nome}')