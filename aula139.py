# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('Esse e o upper')
#         return super().upper()


# string = MinhaString('Bababui')
# print(string.upper())

class A:
    atributo_a = 'value A'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'value B'

    def __init__(self, atributo, another):
        super().__init__(atributo)
        self.another = another

    def metodo(self):
        print('B')

    
class C(B):
    atributo_c = 'value C'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def metodo(self):
        super().metodo() #vai ver o B
        super(B, self).metodo() # A
        # A.metodo(self)
        print('C')


c1 = C('Skibididop')
print(c1.atributo)
# print(c1.atributo_a)
# print(c1.atributo_b)
# print(c1.atributo_c)
# c1.metodo()