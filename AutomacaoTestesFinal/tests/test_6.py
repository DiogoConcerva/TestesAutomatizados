import pytest
from Pages.CartPage import CartPage
from Pages.LoginPage import LoginPage
from Pages.ProductsPage import ProductsPage


class Test6:

    @pytest.fixture
    def test_setup(self):
        self.login_page = LoginPage()
        self.add_cart = ProductsPage(self.login_page.driver)
        self.display_cart = CartPage(self.login_page.driver)

        yield
        self.login_page.close_page()

    def test_buy_success(self, test_setup):
        product_name = 'Sauce Labs Bolt T-Shirt'
        self.login_page.logar_site()
        assert self.add_cart.page_products(), 'Página de produtos não encontrada'
        self.add_cart.find_products(product_name)
        assert self.display_cart.open_cart(), 'Página do carrinho não encontrada'
        assert self.display_cart.number_cart() == '1', 'O valor adicionado ao carrinho está incorreto'
        assert self.display_cart.check_item_selected(product_name), 'Produto diferente do escolhido'
        assert self.display_cart.click_btn_checkout(), 'Página de checkout não encontrada'

        assert self.display_cart.information(), 'Página para finalizar pedido não encontrada'

        assert self.display_cart.check_information(product_name), 'Compra não finalizada'
