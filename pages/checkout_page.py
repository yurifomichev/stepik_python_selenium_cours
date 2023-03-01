from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Checkout_page(Base):

    url = 'https://www.dns-shop.ru/checkout/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    products_count = '//div[@class="base-checkout-products__info_hLg"]'
    products_price = '//div[@class="base-checkout-products__price_tDJ"]'

    # Getters

    def get_products_count(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.products_count)))

    def get_products_price(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.products_price)))

    # Actions

    def get_products_count_number(self):
        products_count_number = self.get_products_count().text.split(' ')[1]
        print('Checkout page products count is ' + products_count_number)
        return products_count_number

    def get_products_price_number(self):
        products_price_number = self.get_products_price().text.split(' ')
        price = products_price_number[1] + ' ' + products_price_number[2]
        print('Checkout page products price is ' + price)
        return price