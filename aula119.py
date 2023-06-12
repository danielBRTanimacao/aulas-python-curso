import os

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


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer, sair')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comandos = comandos.get(tarefa) if comandos.get(tarefa) is not None else adicionar(tarefa)
    comandos()
    # if tarefa == 'listar':
    #     listar(tarefas)
    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    # elif tarefa == 'clear':
    #     os.system('cls')
    # elif tarefa == 'sair':
    #     break
    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)