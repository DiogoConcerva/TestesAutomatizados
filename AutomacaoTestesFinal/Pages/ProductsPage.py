from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class ProductNotFoundException(Exception):
    pass


class ProductsPage(PageObject):

    id_products = 'inventory_container'
    class_products_itens = 'inventory_item_description'
    class_itens = 'inventory_item_name'
    btn_add_to_cart = 'add-to-cart-sauce-labs-bolt-t-shirt'
    btn_remove_to_cart = 'remove-sauce-labs-bolt-t-shirt'
    text_remove_btn = 'REMOVE'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def page_products(self):
        try:
            self.driver.find_element(By.ID, self.id_products)
            return True
        except NoSuchElementException:
            return False

    def find_products(self, product_name):
        list_products = self.driver.find_elements(By.CLASS_NAME, self.class_products_itens)
        for products in list_products:
            name_product = products.find_element(By.CLASS_NAME, self.class_itens).text
            if name_product == product_name:
                products.find_element(By.ID, self.btn_add_to_cart).click()
                if products.find_element(By.ID, self.btn_remove_to_cart).text != self.text_remove_btn:
                    raise Exception(f'Após clicar no ADD TO CART ou botão não mudou para {self.text_remove_btn}!')
                break
        else:
            raise ProductNotFoundException(f'Produto {product_name} não localizado.')
