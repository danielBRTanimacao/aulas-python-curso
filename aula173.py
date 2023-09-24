# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy

import os
import shutil

HOME = os.path.expanduser('~')
PATH_DOWNLOAD = os.path.join(HOME, 'Downloads')
ORIGINAL_FOLDER = os.path.join(PATH_DOWNLOAD, 'exemplo_teste_aula')
NEW_FOLDER = os.path.join(PATH_DOWNLOAD, 'exemplo02')

for root, dirs, files in os.walk(ORIGINAL_FOLDER):
    for file in files:
        print(file)