import time
from selenium.webdriver.common.by import By

class Base():
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        current_url = self.driver.current_url
        print('Current page url: ' + current_url)
        return current_url

    """Метод для скролла страницы если элемент не найден, потому что существующие методы на сайте dns не сработали"""
    def scroll_to_element(self, locator):
        elem = None
        height = 0
        while elem == None and height < 2000:
            try:
                self.driver.execute_script("window.scrollBy(0,5)", "");
                height += 5
                elem = self.driver.find_element(By.XPATH, locator)
            except:
                self.driver.execute_script("window.scrollBy(0,5)", "");
                height += 5
        while elem == None and height > 0:
            try:
                self.driver.execute_script("window.scrollBy(0,-5)", "");
                height -= 5
                elem = self.driver.find_element(By.XPATH, locator)
            except:
                self.driver.execute_script("window.scrollBy(0,-5)", "");
                height -= 5
        return elem