import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class LoginPage(PageObject):

    URL = 'https://www.saucedemo.com/'
    id_btn_login = 'login-button'
    class_msg_login_error = 'error-message-container'
    text_msg_error = 'Epic sadface: Username is required'
    id_menu = 'react-burger-menu-btn'
    product_page = 'title'
    products = 'PRODUCTS'
    list_product = 'inventory_container'

    def __init__(self):
        super(LoginPage, self).__init__()
        self.driver.get(self.URL)

    def click_btn_login(self):
        self.driver.find_element(By.ID, self.id_btn_login).click()

    def new_page(self):
        return self.driver.current_url != self.URL

    def login_msg_error(self):
        msg_error = self.driver.find_element(By.CLASS_NAME, self.class_msg_login_error).text
        return msg_error == self.text_msg_error

    def efetuar_login(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')

    def page_product(self):
        products_page = self.driver.find_element(By.CLASS_NAME, self.product_page).text
        return products_page == self.products

    def verificar_menu(self):
        try:
            self.driver.find_element(By.ID, self.id_menu)
        except NoSuchElementException:
            pytest.fail('Menu não encontrado')

    def verificar_list_product(self):
        try:
            self.driver.find_element(By.ID, self.list_product)
        except NoSuchElementException:
            pytest.fail('Lista de produtos não encontrado!')
