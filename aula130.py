# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:

    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        # setter
        self.password = password
    
    @classmethod
    def creator_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('LOG:', msg)


# c1 = Connection()
c1 = Connection.creator_with_auth('Bababui', '123')
# c1.set_user('Bababui')
# c1.set_password(123)
Connection.log('Essa e a mensagem de log Bababui')
print(c1.user)
print(c1.password)