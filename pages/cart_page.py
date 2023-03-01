from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):

    url = 'https://www.dns-shop.ru/cart/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    product_name = '//a[contains(@class,"base-ui-link")]'
    product_price = '//div[@class="price"]/div/span[@class="price__current"]'
    product_code = '//div[@class="cart-items__product-code"]/div'
    order_conditions_product_price = '//span[@class="price__current"]'
    formalization_button = '//button[@id="buy-btn-main"]'

    # Getters

    def get_product_name(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.product_name)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.product_price)))

    def get_product_code(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.product_code)))

    def get_order_conditions_product_price(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.order_conditions_product_price)))

    def get_formalization_button(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.formalization_button)))

    # Actions

    def formalization_button_click(self):
        self.get_formalization_button().click()
        print('Click "Перейти к оформлению" button')

    def get_product_name_text(self):
        product_name_text = self.get_product_name()[0].text
        print('Cart page product name is ' + product_name_text)
        return product_name_text

    def get_product_code_number(self):
        product_code_number = self.get_product_code_number()[0].text
        print('Cart page product number is ' + product_code_number)
        return product_code_number

    def get_product_price_number(self):
        product_price_number = self.get_product_price()[0].text.split(' ')
        price = product_price_number[0] + ' ' + product_price_number[1]
        print('Cart page product widget product price is ' + price)
        return price

    def get_order_conditions_product_price_number(self):
        order_conditions_product_price_number = self.get_order_conditions_product_price().text.split(' ')
        price = order_conditions_product_price_number[0] + ' ' + order_conditions_product_price_number[1]
        print('Cart page order conditions product price is ' + price)
        return price