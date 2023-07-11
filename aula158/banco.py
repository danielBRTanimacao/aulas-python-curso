import contas
import pessoas


class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None, 
            clientes: list[pessoas.Pessoa] | None = None,
            contas: list[contas.Conta] | None = None
        ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
    
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False        

    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False        

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attr}'


if __name__ == '__main__':
    cliente_1 = pessoas.Cliente('Bababui', 69)
    conta_corrente_1 = contas.ContaCorrente(123, 321, 0, 100)
    cliente_1.conta = conta_corrente_1

    cliente_2 = pessoas.Cliente('Bico seco', 26)
    conta_poupanca_1 = contas.ContaPoupanca(321, 123, 0)
    cliente_2.conta = conta_poupanca_1

    banco = Banco()
    banco.clientes.extend([cliente_1, cliente_2])
    banco.contas.extend([conta_corrente_1, conta_poupanca_1])
    banco.agencias.extend([123, 321])

    print(banco.autenticar(cliente_1, conta_corrente_1))

    print(banco)
