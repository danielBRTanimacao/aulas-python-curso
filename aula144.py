# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print("E-mail: Enviando...", self.mensagem)
        return True
    

class NotificacaoSms(Notificacao):
    def enviar(self) -> bool:
        print("SMS: Enviando...", self.mensagem)
        return False


def notificar(notificar: Notificacao):
    notificar_enviar = notificar.enviar()

    if notificar_enviar:
        print('A notificação foi enviada')
    else:
        print('A notificação não foi enviada')
    

notificacao_email = NotificacaoEmail('Enviou essa bomba kkk')
notificar(notificacao_email)

notificar(NotificacaoSms('Olha a mensagem kkk'))