# Problema dos parâmetros mutáveis em funções Python

def add_client(name, lista=None):
    if lista == None:
        lista = []
    lista.append(name)
    return lista


client1 = add_client('Gabriel')
add_client('Bababui', client1)
add_client('Bico Seco', client1)

client2 = add_client('Bahianinho')
add_client("Baihano", client2)
client2.append('piru')

print(client1)
print(client2)