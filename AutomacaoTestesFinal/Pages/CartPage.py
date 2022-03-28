from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class CartPage(PageObject):

    class_number_buy = 'shopping_cart_link'
    URL_CART = 'https://www.saucedemo.com/cart.html'
    URL_CHECKOUT = 'https://www.saucedemo.com/checkout-step-one.html'
    URL_OVERVIEW = 'https://www.saucedemo.com/checkout-step-two.html'
    URL_COMPLETE = 'https://www.saucedemo.com/checkout-complete.html'
    class_item = 'cart_item'
    class_name_product = 'inventory_item_name'
    btn_checkout = 'checkout'
    btn_continue = 'continue'
    class_msg_error = 'error-message-container'
    text_error = 'Error: First Name is required'
    id_first_name = 'first-name'
    first_name = 'Diogo'
    id_last_name = 'last-name'
    last_name = 'Concerva'
    id_zip_code = 'postal-code'
    zip_code = '12345678'
    class_quantity_product = 'cart_quantity'
    id_finish = 'finish'

    def __init__(self, driver):
        super(CartPage, self).__init__(driver=driver)

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, self.class_number_buy).click()
        return self.driver.current_url == self.URL_CART

    def number_cart(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_number_buy).text

    def check_item_selected(self, product_name):
        item = self.driver.find_elements(By.CLASS_NAME, self.class_item)
        for product in item:
            if product.find_element(By.CLASS_NAME, self.class_name_product).text == product_name:
                return True
        else:
            return False

    def click_btn_checkout(self):
        self.driver.find_element(By.ID, self.btn_checkout).click()
        return self.driver.current_url == self.URL_CHECKOUT

    def click_btn_continue(self):
        self.driver.find_element(By.ID, self.btn_continue).click()
        msg_error = self.driver.find_element(By.CLASS_NAME, self.class_msg_error).text
        if msg_error == self.text_error:
            return True
        else:
            return False

    def information(self):
        self.driver.find_element(By.ID, self.id_first_name).send_keys(self.first_name)
        self.driver.find_element(By.ID, self.id_last_name).send_keys(self.last_name)
        self.driver.find_element(By.ID, self.id_zip_code).send_keys(self.zip_code)
        self.driver.find_element(By.ID, self.btn_continue).click()
        return self.driver.current_url == self.URL_OVERVIEW

    def check_information(self, product_name):
        if self.driver.find_element(By.CLASS_NAME, self.class_name_product).text == product_name \
                and self.driver.find_element(By.CLASS_NAME, self.class_quantity_product).text == '1':
            self.driver.find_element(By.ID, self.id_finish).click()
            if self.driver.current_url == self.URL_COMPLETE:
                return True
            else:
                return False
