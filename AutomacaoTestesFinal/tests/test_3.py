from time import sleep

import pytest

from Pages.LoginPage import LoginPage
from Pages.MenuPage import MenuPage


class Test3:

    @pytest.fixture
    def test_setup(self):
        self.logar_page = LoginPage()

        yield
        self.logar_page.close_page()

    def test_logout_application(self, test_setup):
        self.logar_page.logar_site()
        self.menu_page = MenuPage(self.logar_page.driver)
        self.menu_page.open_menu()

        assert self.menu_page.menu_display(), 'O menu não foi exibido'

        self.menu_page.logout_site()

        assert self.logar_page.home_page(), 'Página não encontrada'
