import requests
from bs4 import BeautifulSoup

url_tudocelular = 'https://www.tudocelular.com/'
response_tudocelular = requests.get(url_tudocelular)
html_tudocelular = BeautifulSoup(response_tudocelular.text, 'html.parser')

def exibeMateriasTudoCelular(assunto=None):
    for materia in html_tudocelular.select('.newlist_normal'):
        titulo = materia.select_one('.title_new')
        # print(titulo)
        titulo1 = titulo.text
        titulo1 = titulo1.strip()
        descricao = materia.select_one('.toplabel')
        comentarios = materia.select_one('.comment-gray')
        hora = materia.select_one('em')
        link = materia.select_one('a')
        if assunto:
            if descricao.text == assunto:
                print(f'{descricao.text}\t- {titulo1} - {hora.text} - {link.attrs["href"]}')
        else:
            print(f'{descricao.text}\t- {titulo1} - {hora.text} - {link.attrs["href"]}')

url_olhardigital = 'https://olhardigital.com.br/'
response_olhardigital = requests.get(url_olhardigital)
html_olhardigital = BeautifulSoup(response_olhardigital.text, 'html.parser')

def exibeMateriasOlharDigital(assunto=None):
    for materia in html_olhardigital.select('article'):
        # print(materia)
        titulo = materia.select_one('.title')

        link = materia.select_one('a')
        print(f'{titulo.text} - {link.attrs["href"]}')

# row justify-content-center


assuntos_tudocelular = ['Tech','Android','Software','Segurança','Lançamentos','Curiosidade','Xiaomi']
for i in assuntos_tudocelular:
    exibeMateriasTudoCelular(i)
print('#'*80)
print('\nUltimas do Tudo celular\n')
exibeMateriasTudoCelular()
print('#'*80)
print('\nUltimas do Olhar Digital\n')
exibeMateriasOlharDigital()

