from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

"""Каждая категория в отдельном классе"""
class Category_komplektuyushhie_dlya_pk_page(Base):

    url = 'https://www.dns-shop.ru/catalog/17aa522a16404e77/komplektuyushhie-dlya-pk/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    subcategories = { 'Основные комплектующие для ПК': '//a[contains(@href,"osnovnye-komplektuyushhie-dlya-pk")]',
               'Устройства расширения': '//a[contains(@href,"ustrojstva-rasshireniya")]',
               'Моддинг и обслуживание': '//a[contains(@href,"modding-i-obsluzhivanie")]',
               'Комплектующие для сервера': '//a[contains(@href,"komplektuyushhie-dlya-servera")]' }

    # Getters

    def get_subcategory(self, subcategory):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.subcategories[subcategory])))

    # Actions

    def subcategory_click(self, subcategory):
        self.get_subcategory(subcategory).click()
        print('Click subcategory "' + subcategory + '" button')