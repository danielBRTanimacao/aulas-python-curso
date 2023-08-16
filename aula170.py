# os.listdir para navegar em caminhos
#C:\Users\danie\OneDrive\Área de Trabalho\vs estudo\testes_projetos_python\EXEMPLOS AULA 170
# caminho = r'C:\\Users\\danie\\OneDrive\\Área de Trabalho\\vs estudo\\testes_projetos_python\\EXEMPLOS AULA 170'
import os

caminho = os.path.join('C:/', 'Users', 'danie', 'OneDrive', 'Área de Trabalho', 
                       'vs estudo', 'testes_projetos_python', 'EXEMPLOS AULA 170'
)
# print(caminho)
for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for itens in os.listdir(caminho_completo_pasta):
        print(' ', itens)