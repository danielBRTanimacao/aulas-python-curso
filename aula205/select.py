import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "2"'
) # * Seleciona tudo

row = cursor.fetchone()
print(row)

# for row in cursor.fetchall():
#     _id, name, weight = row
#     print(_id, name, weight)

cursor.close()
connection.close()
