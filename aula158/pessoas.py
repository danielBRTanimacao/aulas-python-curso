import contas


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attr}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.ContaCorrente | None = None


if __name__ == '__main__':
    cliente1 = Cliente('Bababui', 23)
    cliente1.conta = contas.ContaCorrente(112, 123, 100, 100)
    print(cliente1)
    print(cliente1.conta)
