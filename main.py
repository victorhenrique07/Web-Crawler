from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import getpass


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
        sleep(4.5)
        # login script ready to work

        save_login_button = navegador.find_element(
            By.CSS_SELECTOR, "button.sqdOP:nth-child(4)")
        save_login_button.click()
        sleep(3.5)
        turn_off_notifications_button = navegador.find_element(
            By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")
        turn_off_notifications_button.click()


user = getpass.getpass('Enter your Instagram username: ')
passw = getpass.getpass('Enter your Instagram password: ')
rick_login = Crawler(user, passw)
rick_login.join_instagram()
