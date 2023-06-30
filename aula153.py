# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, name):
        print(name ,'está chamando o telefone', self.phone)
        return 'Bababui kk'
    

call1 = CallMe('00 00-00000')
call1('Daniel')
print(call1('Bico seco'))