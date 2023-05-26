# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def falsy(value):
    return 'falsy' if not value else 'truthy'


print(f"{'Teste'}", falsy('Teste'))
print(f"{dicionario=}", falsy(dicionario))
print(f"{conjunto=}", falsy(conjunto))
print(f"{tupla=}", falsy(tupla))
print(f"{string=}", falsy(string))
print(f"{inteiro=}", falsy(inteiro))
print(f"{flutuante=}", falsy(flutuante))
print(f"{nada=}", falsy(nada))
print(f"{falso=}", falsy(falso))
print(f"{intervalo=}", falsy(intervalo))