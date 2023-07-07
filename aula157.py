# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
import enum

# Directions = enum.Enum('Directions', ['ESQUERDA', 'DIREITA']) #const
# Esse tipo Directions ja funciona e o programa percebi o seu tipo
# print(Directions.ESQUERDA, Directions(1), Directions['ESQUERDA'])
# print(Directions(1).name, Directions.ESQUERDA.value)

class Directions(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    CIMA = enum.auto()

def mover(direction: Directions):
    if not isinstance(direction, Directions):
        raise ValueError('Direção não encontrada')
    print(f'Movendo para a direção {direction.name.lower()}')


mover(Directions.ESQUERDA)
mover(Directions.DIREITA)
mover(Directions.CIMA)
#mover('lado')
