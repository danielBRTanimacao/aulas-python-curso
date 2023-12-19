import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - CREATE READ   UPDATE DELETE
# SQL -  INSERT SELECT UPDATE DELETE

# CUIDADO: Fazendo DELETE sem WHERE
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# Delete mais cuidadoso
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,' #primary key
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores
# CUIDADO: com sql injection NÃO PRECISA MAIS DE CUIDADO
sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES '
    '(:nome, :peso)' # Agora ele sabe que os valores estão separados
)
# connection.execute(sql, ["Bico Seco", 1]) Execute, executa uma unica coisa e executemany varias coisas
# connection.executemany(
#     sql, (
#         ("Bico Seco", 1), ("Cururu Pidão", 4)
#     )
# ) 
connection.execute(sql, {'nome': "Silas Mahoraga", 'peso': 10})
connection.executemany(
    sql, (
        {'nome': "Silas Mahoraga", 'peso': 10},
        {'nome': "Akasa", 'peso': 12},
        {'nome': "Pidão", 'peso': 2},
        {'nome': "Cleitin do Grau", 'peso': 6}
    )
)
connection.commit()

cursor.close()
connection.close()

if __name__ == '__main__':
    print(sql)