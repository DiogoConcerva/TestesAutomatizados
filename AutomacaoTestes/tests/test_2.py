from selenium import webdriver

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

URL = 'https://www.saucedemo.com/'


class Test2:
    @pytest.fixture()
    def test_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        yield
        self.driver.quit()

    def test_efetuar_login(self, test_setup):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()

        assert self.driver.current_url != URL, 'Página não modificada'

        products_page = self.driver.find_element(By.CLASS_NAME, 'title').text

        assert products_page == 'PRODUCTS', 'Página não encontrada'

        # Verificar menu
        try:
            self.driver.find_element(By.ID, 'react-burger-menu-btn')
        except NoSuchElementException:
            pytest.fail('Menu não encontrado!')

        # Verificar lista de produtos
        try:
            self.driver.find_element(By.ID, 'inventory_container')
        except NoSuchElementException:
            pytest.fail('Lista de produtos não encontrado!')
            