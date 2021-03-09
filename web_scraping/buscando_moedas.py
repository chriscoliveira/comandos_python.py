# -*- coding: utf-8 -*-
from unidecode import unidecode
import requests
from bs4 import BeautifulSoup


def baixar(url, nome):
    with open('fotos/' + nome, 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print
            response

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


def buscar(url):
    colecao = []
    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(req.content, 'html.parser')
    itens = soup.find_all('div', class_='coin')
    arquivo = open('resultado.csv', 'w')

    for item in itens:
        link = item.find('a', class_='blue-15')
        arquivo.write(str(buscar_info('https://pt.ucoin.net/' + link['href'])) + '\n')

    arquivo.close()


def buscar_info(url):
    colecao = []
    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(req.content, 'html.parser')
    linhas = soup.find_all('table', {'class': 'coin-info'})
    infos = []
    pais = '-'
    ano = '-'
    krause = '-'
    valor = '-'
    moeda = '-'
    tipo = 'Moeda'
    qualidade = '-'
    material = '-'
    diametro = '-'
    detalhe = '-'
    anverso = '-'
    reverso = '-'
    datacadastro = '-'
    file = open('bancoMoedas.txt', 'a+')
    for linha in linhas:
        itens = linha.findAll('tr')
        for item in itens:
            campo = str(item.findAll('th')).replace('<th>', '').replace('</th>', '').replace('[', '').replace(']', '') \
                .replace('<th class="nowrap">', '').replace('(', '').replace(')', '')
            campo = unidecode(campo.upper())
            info = str(item.findAll('td')).replace('<td>', '').replace('</td>', '').replace('[', '').replace(']', '') \
                .replace('<span class="lgray-11">', '').replace('</span>', '').replace('\xa0', ' ') \
                .replace('<td class="gray-11" style="text-align:right"><b>', '').replace('</b>', '') \
                .replace('<b class="blue-11">', '')
            info = unidecode(info.upper())

            if campo == 'PAIS':
                pais = info
            elif campo == 'ANO':
                ano = info
            elif campo == 'NUMERO KRAUSE':
                krause = info
            elif campo == 'DENOMINACAO':
                valor = info
            elif campo == 'COMPOSICAO':
                material = info
            elif campo == 'DIAMETRO MM':
                diametro = info + 'MM'
            elif campo == 'ANVERSO':
                anverso = info
            elif campo == 'REVERSO':
                reverso = info
            elif campo == 'PERIODO':
                detalhe += 'PEDIODO ' + info + ' - '
            elif campo == 'TIPO DE MOEDA':
                detalhe += 'CIRCULACAO ' + info + ' - '
            elif campo == 'SOBERANO':
                detalhe += 'SOBERANO ' + info + ' - '
            elif campo == 'TIPO DE BORDO':
                detalhe += 'BORDA ' + info + ' - '
            elif campo == 'ALINHAMENTO':
                detalhe += 'ALINHAMENTO ' + info + ' - '
            elif campo == 'PESO (GR)':
                detalhe += 'PESO ' + info + 'GR - '
            elif campo == 'ESPESSURA (MM)':
                detalhe += 'ESPESSURA ' + info + 'MM '

    file.write(
        f"INSERT INTO Colecao (pais, ano, krause, valor, moeda, tipo, qualidade, material, diametro, detalhe, "
        f"anverso, reverso) VALUES ('{pais}', {ano}, '{krause}', '{valor}', '{moeda}', '{tipo}', '{qualidade}',"
        f" '{material}', '{diametro}', '{detalhe}', '{anverso}', '{reverso}');\n"
    )
    file.close()
    return infos


if __name__ == '__main__':
    # buscar('https://pt.ucoin.net/gallery/?uid=26638&page=0')
    buscar_info('https://pt.ucoin.net//coin/spain-1-peseta-1997/?ucid=40433543')
    for i in range(100):
        buscar('https://pt.ucoin.net/gallery/?uid=26638&page=' + str(i))
        print('https://pt.ucoin.net/gallery/?uid=26638&page=' + str(i))
