from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class MenuPage(PageObject):

    class_open_menu = 'bm-item-list'
    btn_menu = 'react-burger-menu-btn'
    btn_logout = 'logout_sidebar_link'

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)

    def open_menu(self):
        self.driver.find_element(By.ID, self.btn_menu).click()

    def menu_display(self):
        try:
            self.driver.find_element(By.CLASS_NAME, self.class_open_menu)
            return True
        except NoSuchElementException:
            return False

    def logout_site(self):
        self.driver.find_element(By.ID, self.btn_logout).click()
