# Variáveis livres + nonlocal (locals, globals)

# def fora(x):
#     a = x
#     def dentro():
#         return a
    

#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(8)
# print(dentro1())
# print(dentro2())
def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final


    return interna


c = concatenar('a')
print(c('b'))