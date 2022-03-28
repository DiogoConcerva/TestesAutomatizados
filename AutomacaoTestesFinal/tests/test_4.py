import pytest
from Pages.CartPage import CartPage
from Pages.LoginPage import LoginPage
from Pages.ProductsPage import ProductsPage


class Test4:

    @pytest.fixture
    def test_setup(self):
        self.logar_page = LoginPage()

        yield
        self.logar_page.close_page()

    def test_add_product_cart(self, test_setup):
        product_name = 'Sauce Labs Bolt T-Shirt'
        self.logar_page.logar_site()
        self.add_cart = ProductsPage(self.logar_page.driver)

        assert self.add_cart.page_products(), 'Pagina de produtos não encontrada!'
        self.add_cart.find_products(product_name)

        self.display_cart = CartPage(self.logar_page.driver)
        assert self.display_cart.number_cart() == '1', 'O valor adicionado ao carrinho está incorreto'
        assert self.display_cart.open_cart(), 'Página de carrinho não encontrada!'
        assert self.display_cart.check_item_selected(product_name), 'Produto não encontrado no carrinho'
