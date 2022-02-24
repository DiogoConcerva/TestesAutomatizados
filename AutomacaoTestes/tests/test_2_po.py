import pytest

from Pages.LoginPage2 import LoginPage


class Test2:

    @pytest.fixture
    def test_setup(self):
        self.login_page = LoginPage()

        yield
        self.login_page.close()

    def test_efetuar_login(self, test_setup):
        self.login_page.efetuar_login()
        self.login_page.click_btn_login()

        assert self.login_page.new_page(), 'Página não modificada'

        assert self.login_page.page_product(), 'Página não encontrada'

        self.login_page.verificar_menu()

        self.login_page.verificar_list_product()
