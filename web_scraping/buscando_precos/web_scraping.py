import requests
from bs4 import BeautifulSoup
import urllib.request


def search(link):
    pagina = requests.get(link)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    # print(soup)
    return soup


def tiny_url(url):
    api_url = 'https://tinyurl.com/api-create.php?url='
    tinyurl = urllib.request.urlopen(api_url + url).read()
    return tinyurl.decode('utf-8')


def retorna_materias(link, tag_bloco, tag_titulo, tag_link=None, tag_horario=None, research=None):
    pagina = requests.get(link)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    arquivo = open('resultado.txt', 'w')

    arquivo.write(
        f'\nNotícias de {link.replace("https://", "").replace(".com", "").replace("www.", "").replace(".br", "").replace("/", "")}\n')

    for materia in soup.select(tag_bloco):
        try:
            texto = materia.select_one(tag_titulo).text
            link = materia.select_one('a').get('href')

            # verifica se existe a tag de horario da materia
            if tag_horario:
                horario = materia.select_one(tag_horario)
                horario = horario.text.replace("há", "")
            else:
                horario = ''
        except Exception as e:
            texto = ''

        if research:
            if research.upper() in texto.upper():
                # arquivo.write(f'{horario} - {texto.strip()} \n\n')
                arquivo.write(f'{horario} - {texto.strip()} {tiny_url(link)}\n\n')

        else:
            # arquivo.write(f'{horario} - {texto.strip()} {tiny_url(link)}\n\n')
            if not horario == None:
                arquivo.write(f'{horario} - {texto.strip()} {tiny_url(link)}\n\n')

    arquivo.close()


if __name__ == '__main__':
    # tecmundo
    valor = None
    retorna_materias(link='https://www.tecmundo.com.br/novidades', tag_bloco='.tec--card--medium',
                     tag_titulo='.tec--card__title__link', tag_horario='.z-flex-1', research=valor)