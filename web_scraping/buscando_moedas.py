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


def buscar(url, pagina):
    colecao = []
    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(req.content, 'html.parser')
    itens = soup.find_all('div', class_='coin')
    arquivo = open('resultado.csv', 'w')

    for item in itens:
        link = item.find('a', class_='blue-15')
        arquivo.write(str(buscar_info('https://pt.ucoin.net/' + link['href'], pagina)) + '\n')

    arquivo.close()


def buscar_info(url, pagina):
    colecao = []
    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(req.content, 'html.parser')

    linhas = soup.find_all('div', {'class': 'centerCol'})
    infos = []
    pais = ' '
    ano = ' '
    krause = ' '
    valor = ' '
    moeda = ' '
    tipo = 'Moeda'
    qualidade = ' '
    material = ' '
    diametro = ' '
    detalhe = ' '
    anverso = ' '
    reverso = ' '
    datacadastro = ' '
    variacao = ' '
    file = open(str(pagina) + '_ucoin.txt', 'a+')
    for linha in linhas:
        itens = linha.findAll('tr')
        try:
            variacao = str(linha.findAll('h4')).replace('<h4>', '').replace('</h4>', '').replace('"', '').replace('[',
                                                                                                                  '').replace(
                ']', '').upper()
        except :
            variacao = 'VERIFICAR ERROR'
        venda = str(linha.find_all('a', {'class': 'right'})).replace(
            '[<a class="gray-12 right pricewj" href="#price">Preço: € <span>', '').replace('</span></a>]', '').replace('[','').replace(']','')

        if not venda == '':
            venda = round(float(venda) * 6.74, 2)
        for item in itens:
            campo = str(item.findAll('th')).replace('<th>', '').replace('</th>', '').replace('[', '').replace(']', '') \
                .replace('<th class="nowrap">', '').replace('(', '').replace(')', '')
            campo = unidecode(campo.upper())
            info = str(item.findAll('td')).replace('<td>', '').replace('</td>', '').replace('[', '').replace(']', '') \
                .replace('<span class="lgray-11">', '').replace('</span>', '').replace('\xa0', ' ') \
                .replace('<td class="gray-11" style="text-align:right"><b>', '').replace('</b>', '') \
                .replace('<b class="blue-11">', '').replace(
                '<SPAN CLASS="LTR" STYLE="FONT-FAMILY: DC;FONT-SIZE: 13PX;">', '')
            info = unidecode(info.upper())

            if campo == 'PAIS':
                pais = info
            elif campo == 'ANO':
                ano = info
            elif campo == 'NUMERO KRAUSE':
                krause = info
            elif campo == 'DENOMINACAO':
                value = info.split()
                valor = value[0]
                moeda = str(value[1:]).replace("'", '').replace(',', '').replace('[', '').replace(']', '')
            elif campo == 'COMPOSICAO':
                material = info
            elif campo == 'DIAMETRO MM':
                diametro = info + 'MM'
            elif campo == 'ANVERSO':
                anverso = info
            elif campo == 'REVERSO':
                reverso = info
            elif campo == 'PERIODO':
                detalhe += info + ' - '
            elif campo == 'TIPO DE MOEDA':
                detalhe += 'CIRCULACAO ' + info + ' - '
            elif campo == 'SOBERANO':
                detalhe += 'SOBERANO ' + info + ' - '
            elif campo == 'TIPO DE BORDO':
                detalhe += 'BORDA ' + info + ' - '
            elif campo == 'ALINHAMENTO':
                detalhe += 'ALINHAMENTO ' + info + ' - '
            elif campo == 'PESO GR':
                detalhe += 'PESO ' + info + 'GR - '
            elif campo == 'ESPESSURA MM':
                detalhe += 'ESPESSURA ' + info + 'MM '
    print(pais, venda,variacao)
    file.write(
        f"INSERT INTO Colecao (pais,ano,krause,valor,moeda,tipo,qualidade,material,diametro,detalhe,anverso,reverso,"
        f"datacadastro) VALUES ('{pais.capitalize()}', {ano}, '{krause}', '{valor}', '{moeda}', '{tipo}', "
        f"'{qualidade}', '{material}', '{diametro}', '{variacao.encode('utf8')} {detalhe}', '{anverso}', '{reverso}', '{venda}');\n"
    )

    file.close()
    return infos


if __name__ == '__main__':
    # buscar('https://pt.ucoin.net/gallery/?uid=26638&page=0')
    # buscar_info('https://pt.ucoin.net/coin/france-1-franc-1944/?ucid=34241015',3)
    #
    for i in range(110):
        print(i)
        if i > 99 and i < 109:
            buscar('https://pt.ucoin.net/gallery/?uid=26638&page=' + str(i), i)
            print(str(i)+'-')
