def grafico_pizza():
    import matplotlib.pyplot as plt
    import numpy as np

    # valores do grafico
    y = np.array([35, 25, 25, 15])

    # itens do grafico
    labels = ['maças', 'bananas', 'laranjas', 'melancias']

    # espaço entre fatias
    my_explode = [0.1, 0.1, 0.1, 0.1]

    plt.pie(y, labels=labels, explode=my_explode, shadow=True)
    plt.show()


def qrcode():
    import pyqrcode
    import png
    from pyqrcode import QRCode

    # link para o qrcode
    string = 'https://google.com.br'

    # monta o qrcode
    url = pyqrcode.create(string)

    # salva em png
    url.png(r'qr.png', scale=8)


def grafico_barra():
    from matplotlib import pyplot as plt
    import numpy as np

    valores_produto_a = [6, 7, 8, 4, 4]
    valores_produto_b = [3, 12, 3, 4.1, 6]

    # cria o eixo x com uma separacao de 0.25 entre as barras
    x1 = np.arange(len(valores_produto_a))
    x2 = [x + 0.25 for x in x1]

    # plota as barras
    plt.bar(x1, valores_produto_a, width=0.25, label='Produto A', color='deepskyblue')
    plt.bar(x2, valores_produto_b, width=0.25, label='Produto B', color='mediumseagreen')

    # coloca o nome dos meses como label do eixo x
    meses = ['Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    plt.xticks([x + 0.25 for x in range(len(valores_produto_a))], meses)

    # insere a legenda
    plt.legend()

    plt.title("Quantidade de vendas")
    plt.show()


def renderizar_mapas():
    import folium

    # cria o mapa
    mapa = folium.Map(
        location=[-23.29345756433121, -45.95982397299854],
        tiles='Stamen Terrain',  # estilo do mapa
        zoom_start=16
    )

    # adiciona o marcador no mapa
    folium.Marker(
        [-23.29345756433121, -45.95982397299854],
        popup='<i>Casa</i>',
        tooltip='Clique Aqui!'
    ).add_to(mapa)

    # salva html do mapa
    mapa.save(r'./mapa.html')


def pegar_ip_sites():
    import socket as s

    host = 'google.com'
    IP = s.gethostbyname(host)
    print(f'o Ip do site {host} é {IP}')


def criar_executavel():
    # pip install pyinstaller
    # pyinstaller script.py
    pass


def gerador_senhas():
    import random

    lower = 'qwertyuiopasdfghjklçzxcvbnm'
    upper = lower.upper()
    numbers = '0123456789'
    symbels = '!@#$%&*-+/.'

    all = lower + upper + numbers + symbels
    length = 16
    password = ''.join(random.sample(all, length))

    print(password)


def descobrir_operadora_celular():
    import phonenumbers
    from phonenumbers import geocoder, carrier

    telefone = phonenumbers.parse('+5512988092198')

    Carrier = carrier.name_for_number(telefone, 'pt-br')

    regiao = geocoder.description_for_number(telefone, 'pt-br')

    print(f'A operador é {Carrier}, o estado é {regiao}')


def scrap_clima():
    from bs4 import BeautifulSoup
    import requests

    # carrega a pagina
    html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/469/jacarei-sp').content

    # faz o parse no html
    soup = BeautifulSoup(html, 'html.parser')

    # captura os dados
    resumo = soup.find(class_='-gray -line-height-24 _center')
    temMin = soup.find(id='min-temp-1')
    temMax = soup.find(id='max-temp-1')

    print(f'Resumo: {resumo.text}\nMinima de: {temMin}\nMaxima de: {temMax}')


def estrair_zip():
    from zipfile import ZipFile

    filePath = 'arquivo.zip'

    with ZipFile(filePath, 'r') as zip:
        zip.printdir()
        zip.extractall()


def transforma_img_em_cartoon():
    from cv2 import cv2
    import numpy as np

    # carrega img
    img = cv2.imread(r'foto.jpg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    cv2.imshow('Image', img)
    cv2.imshow('edges', edges)
    cv2.imshow('carton', cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def gerar_cod_barra():
    from barcode import EAN13, Code128
    from barcode.writer import ImageWriter

    with open('barcode_code128.png', 'wb') as f:
        Code128('21220JWC11H11', writer=ImageWriter()).write(f)
    with open('barcode_ean13.png', 'wb') as f:
        EAN13('1234567891026', writer=ImageWriter()).write(f)


def criar_diagrama():  # esta com erro
    from diagrams import Cluster, Diagram
    from diagrams.aws.compute import ECS
    from diagrams.aws.database import Elasticache, RDS
    from diagrams.aws.network import ELB, Route53

    with Diagram('Clustered Web Servives.jpg', show=False):
        dns = Route53('dns')
        lb = ELB('lb')
        with Cluster('Services'):
            svc_group = [ECS('web1'), ECS('web2'), ECS('web3')]
        with Cluster('DB Cluster'):
            db_master = RDS('userdb')
            db_master - [RDS('userdb ro')]

        memcached = Elasticache('memcached')

        dns >> lb >> svc_group
        svc_group >> db_master
        svc_group >> memcached


def encurtador_url():  # esta com erro
    import pyshorteners

    url = 'https://www.google.com.br'

    s = pyshorteners.Shortener()

    shortUrl = s.tinyurl.short(url)

    print(f'a URL "{url}" encurtada é {shortUrl}')


def baixar_post_instagram():
    from datetime import datetime
    import instaloader

    # carrega a lob e faz login com a conta
    L = instaloader.Instaloader()
    # L.login('christian.coliveira@gmail.com', '8480151624')

    # carrega todos os posts do perfil
    posts = instaloader.Profile.from_username(L.context, 'pycodebr').get_posts()

    # periodo que deseja baixar os posts
    SINCE = datetime(2020, 1, 16)
    UNTIL = datetime(2021, 7, 18)

    # percorre os posts e baixa apenas os que estao dentro do periodo desejado
    for post in posts:
        if (post.date >= SINCE) and (post.date <= UNTIL):
            print(post.date)
            L.download_post(post, 'insta-posts-downloads')

baixar_post_instagram()