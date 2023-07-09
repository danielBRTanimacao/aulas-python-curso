import abc


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO R${valor:.2f})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é R${self.saldo:.2f} {msg}')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attr}'


class ContaPoupanca(Conta):
    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f})')
            return self.saldo

        print('Não foi possivel sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO R${valor:.2f})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f})')
            return self.saldo

        print('Não foi possivel sacar o valor desejado')
        print(f'Seu limite e de R${-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO R${valor:.2f})')
        return self.saldo

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attr}'


if __name__ == '__main__':
    # conta_poupanca1 = ContaPoupanca(123, 333)
    # conta_poupanca1.sacar(13)
    # conta_poupanca1.depositar(10)
    # print('####')
    conta_corrente2 = ContaCorrente(123, 333, 0, 100)
    conta_corrente2.sacar(13)
    conta_corrente2.sacar(89)
