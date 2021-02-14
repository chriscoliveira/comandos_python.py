import csv

with  open('clientes.csv', 'r') as arquivo:
    # leitura dos dados do csv em lista
    # dados = csv.reader(arquivo)
    # next(dados)
    #
    # for dado in dados:
    #     print(dado)

    # leitura dos dados em dicionarios
    # dados = csv.DictReader(arquivo)
    # next(dados)
    # for dado in dados:
    #     print(dado)

    # para acessar os dados fora do while, usando listcomprehension
    dados = [x for x in csv.DictReader(arquivo)]

with open('clientes2.csv', 'w+') as arquivo:
    escreve = csv.writer(arquivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    chaves = list(dados[0].keys())
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
