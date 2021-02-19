import requests
from bs4 import BeautifulSoup


def search(link):
    pagina = requests.get(link)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    # print(soup)
    return soup


'''
<article class="tec--card tec--card--medium">
    <figure class="tec--card__thumb"><a class="tec--card__thumb__link"
                                        href="https://www.tecmundo.com.br/mercado/211281-o-que-dia-consumidor.htm"
                                        title="Ir para: O que é o Dia do Consumidor?"> <img
            alt="Imagem de: O que é o Dia do Consumidor?"
            class="tec--card__thumb__image lazyload"
            data-src="https://img.ibxk.com.br/2021/02/18/18103824415048.jpg?w=164&amp;h=118&amp;mode=crop&amp;scale=both"
            height="118" width="164"/> </a></figure>
    <div class="tec--card__info"><h3 class="tec--card__title"><a
            class="tec--card__title__link"
            href="https://www.tecmundo.com.br/mercado/211281-o-que-dia-consumidor.htm"> O
        que é o Dia do Consumidor? </a></h3>
        <div class="tec--timestamp tec--timestamp--lg">
            <div class="tec--timestamp__item z--font-semibold">19/2/2021</div>
            <div class="tec--timestamp__item z--min-w-none">
                <div class="z--truncate z-flex-1">há 18 minutos</div>
            </div>
        </div>
    </div>
</article>
'''


def tecmundo(research=None):
    link = 'https://www.tecmundo.com.br/novidades'
    html = search(link)
    materias = html.find_all('article', class_='tec--card--medium')
    print(f'\nNoticias de {link}')
    for materia in materias:
        texto = materia.text

        if research:
            if research.upper() in texto.upper():
                print(f'\t{texto.strip()}')
                continue
        else:
            print(f'\t{texto.strip()}')



if __name__ == '__main__':
    tecmundo()
