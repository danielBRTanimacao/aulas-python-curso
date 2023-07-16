# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html
from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self.__next_index = 0
    
    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1
    
    def __len__(self) -> int:
        return self._index
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, value):
        self._data[index] = value
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__next_index >= self._index:
            self.__next_index = 0
            raise StopIteration
        value = self._data[self.__next_index]
        self.__next_index += 1
        return value


if __name__ == '__main__':
    list_ = MyList()
    list_.append('Bababui', 'skibididop')
    list_.append('Bico seco')
    # print(list_[0])
    # print(len(list_))
    for item in list_:
        print(item)
    print('---------')
    for item in list_:
        print(item)