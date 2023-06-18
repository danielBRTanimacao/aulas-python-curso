# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯
class Caneta:
    def __init__(self, cor):
        # self.cor_tinta = cor
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('PROPERTY!')
        return self._cor

    @cor.setter
    def cor(self, value):
        # if value == 'Vermelho':
        #     raise ValueError('Não aceito esse valor kk')
        self._cor = value

    @property
    def color_tamp(self):
        return self._cor_tampa
    
    @color_tamp.setter
    def color_tamp(self, value):
        self._cor_tampa = value


caneta = Caneta('Azul')
caneta.cor = 'Red'
caneta.color_tamp = 'Blue'
# getter -> obter um valor
print(caneta.cor)
print(caneta.color_tamp)