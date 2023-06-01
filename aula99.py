#import aula99_package
#import aula99_package.modulo #2
#from aula99_package import modulo #1
from aula99_package.modulo import soma_modulo #3
from aula99_package.modulo import * #3

#print(modulo.soma_modulo(1, 99)) #1
#print(aula99_package.modulo.soma_modulo(10))#2
print(soma_modulo(12, 3)) #3
print(variavel)