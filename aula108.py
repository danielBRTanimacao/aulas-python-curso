# count é um iterador sem fim (itertools)
from itertools import count

c1 = count()
r1 = range(10)

print('c1', hasattr(c1, '__iter__'))

for i in c1:
    if i >= 10:
        break
    print(i)