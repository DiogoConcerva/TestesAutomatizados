import pytest

from Pages.CartPage import CartPage
from Pages.LoginPage import LoginPage
from Pages.ProductsPage import ProductsPage


class Test5:
    @pytest.fixture
    def test_setup(self):
        self.login_page = LoginPage()
        self.add_cart = ProductsPage(self.login_page.driver)
        self.display_cart = CartPage(self.login_page.driver)


        yield
        self.login_page.close_page()

    def test_error_message_invalid_information(self, test_setup):
        product_name = 'Sauce Labs Bolt T-Shirt'
        self.login_page.logar_site()
        assert self.add_cart.page_products(), 'Página de produtos não encontrada'
        self.add_cart.find_products(product_name)

        assert self.display_cart.number_cart() == '1', 'O valor adicionado ao carrinho está incorreto'
        self.display_cart.open_cart()

        assert self.display_cart.click_btn_checkout(), 'Página de checkout não encontrada'

        assert self.display_cart.click_btn_continue(), 'Mensagem de erro não localizada'

