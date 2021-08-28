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
            By.CSS_SELECTOR, "button.aOOlW:nth-child(2)")
        turn_off_notifications_button.click()

    def click_first_post(self):
        # class of button to copy link: wp06b
        navegador = self.navegador
        first_post = navegador.find_element(
            By.CSS_SELECTOR, 'article._8Rm4L:nth-child(1) > div:nth-child(2) > button:nth-child(1)')
        first_post.click()
        copy_link = navegador.find_element(By.CSS_SELECTOR, "button.aOOlW:nth-child(5)")
        copy_link.click()


user = getpass.getpass(prompt='Enter your Instagram username: ', stream=None)
passw = getpass.getpass(prompt='Enter your Instagram password: ', stream=None)
rick_login = Crawler(user, passw)
rick_login.join_instagram()
rick_login.click_first_post()
