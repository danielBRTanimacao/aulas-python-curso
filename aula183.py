# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula183texto.txt'

locale.setlocale(locale.LC_ALL, '')

def converter_para_brl(numero: float) -> str:
    brl = 'R$' + locale.currency(numero, symbol=False, grouping=True)
    return brl


data = datetime(2023, 11, 14)
dados = dict(
    nome='João',
    valor=converter_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    tefelone='+55 (00) 000-0000'
)

class MyTemplate(string.Template) :
    delimitar = '%'


with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    template = MyTemplate(texto)
    print(template.substitute(dados))