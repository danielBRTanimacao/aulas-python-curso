# Classes decoradoras (Decorator class)
class Multiply:
    def __init__(self, function_):
        self.func = function_
        self._z = 10
    
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result


@Multiply
def soma(x, y):
    return x + y


two_plus_two = soma(2, 2)
print(two_plus_two)