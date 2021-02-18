from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = '/home/adming/PycharmProjects/novoselenium/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def abre_link(self, link):
        self.chrome.get(link)

    def fecha_chrome(self):
        sleep(5)
        self.chrome.quit()

    def digita_chamado(self, m_cat1, m_cat2, m_problema):
        try:
            cat1 = self.chrome.find_element_by_id('s2id_fieldCategoria2').click()
            cat1_text = self.chrome.find_element_by_id('s2id_autogen1_search')
            cat1_text.send_keys(m_cat1)
            cat1_text = self.chrome.find_element_by_class_name('select2-result-label').click()
            # fieldCategoria3 select
        except Exception as e:
            print('Erro : equipamento ', e)
        try:
            cat2 = self.chrome.find_element_by_id('s2id_fieldCategoria3').click()
            cat2 = self.chrome.find_element_by_class_name('select2-offscreen')
            cat2.send_keys('Lento')
            '''
            #div_component5d8e82a5136b4 > fieldCategoria3 > option:nth-child(3)
            '''

        except Exception as e:
            print('Erro incidente : ', e)

        # try:
        #     loja = self.chrome.find_element_by_id('s2id_fieldLocalidade').click()
        #     loja_text = self.chrome.find_element_by_id('s2id_autogen3_search')
        #     loja_text.send_keys('CT18 - Jacarei').click()
        #     loja_text = self.chrome.find_element_by_class_name('select2-result-label').click()
        # except Exception as e:
        #     print('Erro localidade: ', e)
        try:
            descricao = self.chrome.find_element_by_id('fieldDescricao')
            descricao.send_keys(f'O PDV {m_problema} esta com pouca memoria livre e precisa ser reiniciado.')
        except Exception as e:
            print('Erro descricao: ', e)


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.abre_link(
        'http://10.131.0.67/qualitor//html/ad/adform/request/viewQForm.php?cryptget=99B100W102x111t114g109s61WNgjv99x100t108W105t110t103x117W97B61xev105t100W108B105g110B103t117s97W61g112s116x45s116W100q99g100x101x109g112x114t101g115s97s61sNz99x100B111B112W101s114W97x100W111B114s102g111W114x109t61Blxjz110W109g117g115x117x97B114B105t111W61t65B68g77s32x81W85s65W76t73t84B79B82v99W100s117x115t117B97s114x105t111x61t97g100W109B113t117t97B108B105B116t111g114A99W100B115t101s110t104s97B61B67x95xcWNs95t99gcgHslBeBdB97WUt99BUx102x99tjxUxNtHscBdxNB98xlt97xdBesNglx99WUs102BcxYWez99x100g115W101W114s118t105s99x111x61gNxiFYsdxiWYsHtUBjxetc&idexterno=N&cdservico=16&idtipoatendimento=S&cdusuario=1&A_nmskin=9&nmusuario=&cdcliente=1&cdcontato=2034&cdchamado=&cdchamadorelacionado=&idloginatendente=&A_nmskin=9')
    chrome.digita_chamado(m_cat1='PDV - CPU', m_cat2='Lento', m_problema='101')
    chrome.fecha_chrome()
