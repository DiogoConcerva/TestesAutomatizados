from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class LoginPage(PageObject):
    URL = 'https://www.saucedemo.com/'
    username = 'user-name'
    usarname_site = 'standard_user'
    password = 'password'
    password_site = 'secret_sauce'
    btn_login = 'login-button'

    def __init__(self):
        super(LoginPage, self).__init__()
        self.driver.get(self.URL)

    def logar_site(self):
        self.driver.find_element(By.ID, self.username).send_keys(self.usarname_site)
        self.driver.find_element(By.ID, self.password).send_keys(self.password_site)
        self.driver.find_element(By.ID, self.btn_login).click()

    def home_page(self):
        return self.driver.current_url == self.URL
