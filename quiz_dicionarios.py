perguntas = {
    'Pergunta 1': {
        'pergunta': '2+2?',
        'respostas': {'a': '0', 'b': '2', 'c': '3', 'd': '4'},
        'resposta_certa': 'd'
    },
    'Pergunta 2': {
        'pergunta': '2+1?',
        'respostas': {'a': '1', 'b': '2', 'c': '3', 'd': '4'},
        'resposta_certa': 'c'
    },
    'Pergunta 3': {
        'pergunta': '2+2?',
        'respostas': {'a': '0', 'b': '2', 'c': '3', 'd': '4'},
        'resposta_certa': 'd'
    },
    'Pergunta 4': {
        'pergunta': '2+1?',
        'respostas': {'a': '1', 'b': '2', 'c': '3', 'd': '4'},
        'resposta_certa': 'c'
    },
    'Pergunta 5': {
        'pergunta': '2+2?',
        'respostas': {'a': '0', 'b': '2', 'c': '3', 'd': '4'},
        'resposta_certa': 'd'
    },
    'Pergunta 6': {
        'pergunta': '2+1?',
        'respostas': {'a': '1', 'b': '2', 'c': '3', 'd': '4'},
        'resposta_certa': 'c'
    }
}
acertos = 0
for pergunta_key, pergunta_value in perguntas.items():
    print(f'\n{pergunta_key}: {pergunta_value["pergunta"]}\nRespostas')
    for resposta_key, resposta_value in pergunta_value['respostas'].items():
        print(f'\t{resposta_key}) {resposta_value}')

    resposta_usuario = input("Qual a resposta correta? ")
    if resposta_usuario == pergunta_value['resposta_certa']:
        print('Resposta Correta!')
        acertos += 1
    else:
        print('Resposta incorreta')

qtde_perguntas = len(perguntas)
porcentagem_acertos = acertos / qtde_perguntas * 100

print(f'Voce acertou {acertos} respostas, {porcentagem_acertos:}% das perguntas feitas')
