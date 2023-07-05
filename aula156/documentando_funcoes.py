"""Este e um modulo de exemplo :)

Este módulo contem funções e exemplos de documentação de funções.
A função soma você já conhece bastante 
"""

variable_1 = 1

def soma(x: int | float, y: int | float) -> int | float:
    """
    Soma x e y

    Este módulo contem funções e exemplos de documentação de funções.
    A função soma você já conhece bastante 

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int ou float
    """
    return x + y


def multiplica(x: int | float, y: int | float, z: int | float | None = None) -> int | float:
    """Multiplica x, y ou/e z

    Multiplica x e y. Se z for enviado, multiplica x, y e z.
    """
    if z == None:
        return x * y
    return x * y * z


variable_2 = 2
variable_3 = 3
variable_4 = 4
