# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os

import dotenv
import pymysql

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)
with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE_TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
        # CUIDADO ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
        connection.commit() # so para lembrar
        
        # COMEÇA A MANIPULAR DADOS A PARTIR DAQUI

        with connection.cursor as cursor:
            cursor.execute(
                f'INSERT TO {TABLE_NAME} '
                '(name, age) VALUES ("Cururu", 20) '
            )
        connection.commit()

    