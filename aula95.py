# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def no_zero(value):
    if value == 0:
        raise ZeroDivisionError('Você tentou dividir por zero!')
    return True


def deve_ser_int_float(value):
    tipo_v = type(value)
    if not isinstance(value, (float, int)):
        raise TypeError(f'"{value}" Deve ser Int ou Float\n"{tipo_v.__name__}" enviado')


def divide(num, divi):
    deve_ser_int_float(num)
    deve_ser_int_float(divi)
    no_zero(divi)
    return num / divi


# n = int(input('1 Numero: '))
# n2 = int(input('2 Numero: '))
print(divide(3, '0'))