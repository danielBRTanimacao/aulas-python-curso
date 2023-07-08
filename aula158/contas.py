import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abc.abstractmethod
    def sacar(self, valor): ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO R${valor:.2f})')

    def detalhes(self, msg=''):
        print(f'O seu saldo é R${self.saldo:.2f} {msg}')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f})')
            return self.saldo
        
        print('Não foi possivel sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO R${valor:.2f})')

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f})')
            return self.saldo
        
        print('Não foi possivel sacar o valor desejado')
        print(f'Seu limite e de R${-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO R${valor:.2f})')


if __name__ == '__main__':
    conta_poupanca1 = ContaPoupanca(123, 333)
    conta_poupanca1.sacar(13)
    conta_poupanca1.depositar(10)
    print('####')
    conta_corrente2 = ContaCorrente(123, 333, limite=100)
    conta_corrente2.sacar(13)
    conta_corrente2.sacar(89)
