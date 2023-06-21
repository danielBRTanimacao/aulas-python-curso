# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.adress = []

    def inserir_adress(self, rua, numero):
        self.adress.append(Adress(rua, numero))
    
    def inserir_adress_externo(self, adress):
        self.adress.append(adress)

    def listar_adress(self):
        for adress in self.adress:
            print(adress.rua, adress.numero)

    def __dell__(self):
        print('Apagando', self.nome)


class Adress:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __dell__(self):
        print('Apagando', self.rua, self.numero)


cliente1 = Cliente('Bababui')
cliente1.inserir_adress('Cururu', 98)
cliente1.inserir_adress('Piru B', 89)
adress_externo = Adress('Skibididop', 13)
cliente1.inserir_adress_externo(adress_externo)
# print(cliente1.adress[0].rua)
cliente1.listar_adress()

del cliente1

print('================================= Codigo finalizado =================================')