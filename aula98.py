import importlib

import aula98_m

#importlib recarrega o modulo

for i in range(10):
    importlib.reload(aula98_m)
    print(i)
    
print('Cabo')