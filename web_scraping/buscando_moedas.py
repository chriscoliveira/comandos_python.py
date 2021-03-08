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
    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(req.content, 'html.parser')
    itens = soup.find_all('div', class_='coin')
    arquivo = open('resultado.txt', 'a')

    for item in itens:
        # arquivo.write(f'{item.prettify}\n')
        pais = item.find('a', class_='blue-15').text

        try:
            desc = item.find('div', class_='desc').text
        except:
            desc = ''

        try:
            marca = item.find('div', class_='gray-13').text
        except Exception as e:
            marca = ''

        try:
            assunto = item.find('div', class_='dgray-13').next_element
        except Exception as e:
            assunto = ''
        try:
            valor = item.find('a', class_='blue-12').text
        except Exception as e:
            valor = ''
        fotos = []
        krause = item.find('div', class_='gray-11').text
        contador = 0
        for imgs in item.find_all('td', class_='coin-img'):
            for img in imgs.find_all('img'):
                if contador == 0:
                    baixar(img['src'], pais + '_1.jpg')
                    contador += 1
                else:
                    baixar(img['src'], pais + '_2.jpg')
                    contador = 0

        arquivo.write(f'Pais : {pais}\n'
                      f'marca {marca}\n'
                      f'Desc : {desc}\n'
                      f':{assunto}\n'
                      f'valor: {valor}\n'
                      f'Krause {krause}\n\n')
    arquivo.close()


if __name__ == '__main__':
    for i in range(100):
        buscar('https://pt.ucoin.net/gallery/?uid=26638&page=' + str(i))
        print('https://pt.ucoin.net/gallery/?uid=26638&page=' + str(i))
