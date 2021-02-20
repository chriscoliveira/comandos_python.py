import requests
from bs4 import BeautifulSoup


def search(link):
    pagina = requests.get(link)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    # print(soup)
    return soup


def retorna_materias(link, tag_bloco, tag_titulo, tag_link=None, tag_horario=None, research=None):
    pagina = requests.get(link)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    arquivo = open('resultado.txt', 'w')
    # html
    # arquivo.write(f'<br><table><tr><td colspan="2"><h2>Notícias de {link}</td></tr>')
    arquivo.write(f'Notícias de {link}\n')
    contador_txt = 1000
    gasto_txt = 0
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
            texto = 'Falha ao ler o texto'

        if research:
            if research.upper() in texto.upper():
                # arquivo.write(f'<tr><td>{horario}</td><td>- {texto} <a href="{link}">...</a></td></tr>')
                arquivo.write(f'{horario} - {texto} {link}\n\n')

        else:
            # arquivo.write(
            #     f'<tr><td>{horario}</td><td>- {texto} <a href="{link}">...</a></td></tr>')
            arquivo.write(f'{horario} - {texto} {link}\n\n')
    # arquivohtml.write('</table>')
    arquivo.close()


if __name__ == '__main__':
    # arquivo = open('resultado.html', 'w')

    # tecmundo
    valor = None
    retorna_materias(link='https://www.tecmundo.com.br/novidades', tag_bloco='.tec--card--medium',
                     tag_titulo='.tec--card__title__link', tag_horario='.z-flex-1', research=valor)
    # # tudocelular
    # retorna_materias(link='https://www.tudocelular.com/', tag_bloco='.newlist_normal',
    #                  tag_titulo='.title_new', tag_horario='em',research=valor)
    #
    # # olhardigital
    # retorna_materias(link='https://olhardigital.com.br/', tag_bloco='article',
    # tag_titulo='.title', tag_horario=None,research=valor)
    #
    # # uol
    # retorna_materias(link='https://noticias.uol.com.br/', tag_bloco='.thumbnails-item',
    #                  tag_titulo='.thumb-title', tag_horario=None, research=valor)
