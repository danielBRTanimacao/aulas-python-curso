# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso e Protegido!'
        self.__private = 'Isso e PRIVADO!'
    
    def metodo_public(self):
        print(self.__private)
        return 'Metodo publico kkkkk'
    
    def _metodo_protected(self):
        self.__metodo_private()
        return 'Metodo protegido'
    
    def __metodo_private(self):
        return 'PRIVADO!'


f = Foo()
# print(f._protected)
# print(f.public)
print(f.metodo_public())
# print(f._Foo__metodo_private())