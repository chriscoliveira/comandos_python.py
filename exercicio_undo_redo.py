'''
adicionar tarefa
listar tarefa
desfazer
refazer
'''
tarefa = []
refazer_tarefa = []

def do_add(todo,value):
    todo.append(value)
    print('#'*80) 
    print(f'\n\t->Tarefa: {todo[-1]} adicionado\n')
def do_ls(todo):
    print('#'*80) 
    print(f'\n\t->Tarefas cadastradas: {todo}\n')
    
def do_undo(todo,undo):
    if todo:
        undo.append(todo[-1])
        todo.pop()
        print('#'*80) 
        print(f'\n\t->Desfazendo ultima modificacao: {todo}\n')
    else:
        print('#'*80) 
        print(f'Nao há mais alteracoes para desfazer...\n')
    
def do_redo(todo,redo):
    if redo:
        todo.append(redo[-1])
        redo.pop()
        print('#'*80) 
        print(f'\n\t->Refazendo ultima modificacao: {todo}')
    else:
        print('#'*80) 
        print(f'\n\tNao há mais alteracoes para refazer...\n')
    

while True:
    acao = input('\nO que deseja fazer? add ls undo redo\n: ')
    
    if acao == 'add':
        do_add(tarefa,input('Digite a tarefa: '))
        continue
    if acao == 'ls':
        do_ls(tarefa)
        continue
    if acao == 'undo':
        do_undo(tarefa,refazer_tarefa)
        continue
    if acao == 'redo':
        do_redo(tarefa,refazer_tarefa)
        continue
        

