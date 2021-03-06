from selenium import webdriver


class PageObject:
    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()

    def close(self):
        self.driver.quit()
