import os
import json

def listar(tarefas):
    print()
    if not tarefas:
        print("Nenhuma tarefa listada!")
        return
    
    print("Tarefas:")
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_desfazer):
    print()
    if not tarefas:
        print("Nenhuma tarefa para ser desfeita!")
        return
    
    tarefa = tarefas.pop()
    print(f'a tarefa {tarefa} foi removida!')
    tarefas_desfazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_desfazer):
    print()
    if not tarefas_desfazer:
        print("Nenhuma tarefa para refazer!")
        return
    
    tarefa = tarefas_desfazer.pop()
    print(f'a tarefa {tarefa} foi adicionado!')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print("Você não digitou nenhuma tarefa!")
        return
    tarefas.append(tarefa)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer, clear, ler')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comandos = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comandos()
    salvar(tarefas, CAMINHO_ARQUIVO)
