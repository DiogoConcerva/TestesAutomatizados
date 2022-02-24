import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.saucedemo.com/'


class Test1:
    @pytest.fixture()
    def test_setup(self):
        # Abrir o Chrome
        self.driver = webdriver.Chrome()

        # Acessar a URL
        self.driver.get(URL)

        # Fechar browser
        yield
        self.driver.quit()

    def test_click_login(self, test_setup):
        # Encontrar o botão
        self.driver.find_element(By.ID, 'login-button').click()

        # Verificar se a página permanece a mesma
        assert self.driver.current_url == URL, 'Página não encontrada'

        # Encontrar a mensagem de erro
        msg_erro = self.driver.find_element(By.CLASS_NAME, 'error-message-container').text

        # Verificar o texto da mensagem de erro
        assert msg_erro == 'Epic sadface: Username is required', 'Mensagem de erro incorreta'
