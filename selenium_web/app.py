from selenium import webdriver
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessa(self,site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_singin(self):
        try:
            btn_singin = self.chrome.find_element_by_link_text('Sign in')
            btn_singin.click()
        except Exception as e:
            print('Erro ao clicar: '+e)

    def fazer_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')
            input_login.send_keys('chriscoliveira')
            input_password.send_keys('H4a9YeyBXNYQzkd')
            sleep(2)
            btn_login.click()
        except Exception as e:
            print('Erro ao fazer login: ' + e)

if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com')
    chrome.clica_singin()
    chrome.fazer_login()
    sleep(30)

    chrome.sair()