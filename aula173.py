# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy

import os
import shutil

HOME = os.path.expanduser('~') #pega home do usuario
PATH_DOWNLOAD = os.path.join(HOME, 'Downloads')
ORIGINAL_FOLDER = os.path.join(PATH_DOWNLOAD, 'exemplo_teste_aula')
NEW_FOLDER = os.path.join(PATH_DOWNLOAD, 'exemplo02')

os.makedirs(NEW_FOLDER, exist_ok=True)

for root, dirs, files in os.walk(ORIGINAL_FOLDER):
    for dir_ in dirs: # cria as subpastas
        new_path_directory = os.path.join(root.replace(
            ORIGINAL_FOLDER, NEW_FOLDER), dir_
        )
        os.makedirs(new_path_directory, exist_ok=True)

    for file in files:
        path_file = os.path.join(root, file)
        new_path_file = os.path.join(root.replace(ORIGINAL_FOLDER, NEW_FOLDER), file)

        shutil.copy(path_file, new_path_file)