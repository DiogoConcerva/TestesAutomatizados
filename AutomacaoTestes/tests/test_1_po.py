import pytest
from Pages.LoginPage1 import LoginPage


class Test1:
    @pytest.fixture
    def test_setup(self):
        self.login_page = LoginPage()

        yield
        self.login_page.close()

    def test_click_login(self, test_setup):
        self.login_page.click_btn_login()
        assert self.login_page.is_login_page(), 'Página de login não encontrada'

        assert self.login_page.login_msg_error(), 'Mensagem de erro incorreta'
