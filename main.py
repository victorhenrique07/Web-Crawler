from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


class Crawler:
    def __init__(self, username, password):
        self.username = user
        self.password = passw
        self.navegador = webdriver.Firefox(executable_path='./geckodriver')
        sleep(1)

    def join_instagram(self):
        navegador = self.navegador
        navegador.get('https://www.instagram.com/')
        sleep(2)
        username_input_website = navegador.find_elements_by_name('username')
        username_input_website[0].send_keys(self.username)
        password_input_website = navegador.find_elements_by_name('password')
        password_input_website[0].send_keys(self.password)
        password_input_website[0].send_keys(Keys.ENTER)
        


user = input('Enter your Instagram username: ')
passw = input('Enter your Instagram password: ')
rick_login = Crawler(user, passw)
rick_login.join_instagram()
