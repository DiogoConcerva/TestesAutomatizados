from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    URL = 'https://www.saucedemo.com/'
    id_btn_login = 'login-button'
    class_msg_login_error = 'error-message-container'
    text_msg_error = 'Epic sadface: Username is required'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)

    def click_btn_login(self):
        self.driver.find_element(By.ID, self.id_btn_login).click()

    def is_login_page(self):
        return self.driver.current_url == self.URL

    def login_msg_error(self):
        msg_error = self.driver.find_element(By.CLASS_NAME, self.class_msg_login_error).text
        return msg_error == self.text_msg_error

    def close(self):
        self.driver.quit()
