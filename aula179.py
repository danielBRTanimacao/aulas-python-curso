# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

PATH_CSV = Path(__file__).parent / 'aula179.csv'

with open(PATH_CSV, 'r', encoding='utf-8') as file:
    reader_ = csv.DictReader(file) #Para ler em formato de dicionario

    for line in reader_:
        print(line['Nome'])

# with open(PATH_CSV, 'r', encoding='utf-8') as file:
#     reader_ = csv.reader(file)

#     for line in reader_:
#         print(line)
