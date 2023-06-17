# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe():
        print('OI :D')


c1 = Classe()
c1.funcao_que_esta_na_classe()
Classe.funcao_que_esta_na_classe()