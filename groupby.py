from itertools import groupby, tee

alunos = [
    {'nome':'Luiz','nota':'A'},
    {'nome':'Leticia','nota':'E'},
    {'nome':'Fabricio','nota':'B'},
    {'nome':'Mary','nota':'B'},
    {'nome':'Joao','nota':'A'},
    {'nome':'Joana','nota':'C'},
    {'nome':'Patricia','nota':'B'},
    {'nome':'Patricia','nota':'B'},
    {'nome':'Patricia','nota':'B'},
    {'nome':'Patricia','nota':'B'},
    {'nome':'Patricia','nota':'B'},
    {'nome':'Andre','nota':'C'},
    {'nome':'Eduardo','nota':'D'},
    {'nome':'Anderson','nota':'A'},
    {'nome':'Anderson','nota':'A'},
    {'nome':'Anderson','nota':'A'},
    {'nome':'Anderson','nota':'A'},
    {'nome':'Anderson','nota':'A'},
    {'nome':'Anderson','nota':'A'},
    {'nome':'Anderson','nota':'A'},
    {'nome':'Anderson','nota':'A'},
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento,valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'Nota: {agrupamento}')
    quantidade = len(list(va1))
    for aluno in va2:
        print(f'\t{aluno}')

    print(f'\t{quantidade} de alunos tiraram nota {agrupamento}')
