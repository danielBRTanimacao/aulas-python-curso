# json.dump e json.load com arquivos
import json
import os

FILE_NAME = 'aula177.json'
PATH_ABSOLUT_FILE = os.path.abspath(
    os.path.join( 
        os.path.dirname(__file__),
        FILE_NAME
    )
)

movie = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(PATH_ABSOLUT_FILE, 'w') as file:
    json.dump(movie, file, ensure_ascii=False, indent=2)

with open(PATH_ABSOLUT_FILE, 'r') as file:
    movie_do_json = json.load(file)
    print(movie_do_json)
