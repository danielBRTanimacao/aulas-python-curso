import sys
#Generator expression, Iterables e Iterators em python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #__iter__ e __next__
#print(next(iterator))
lista = [n for n in range(1001)]
generator = (n for n in range(1001))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
