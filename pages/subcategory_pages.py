from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

"""Каждая субкатегория в отдельном классе"""
class Subcategory_osnovnye_komplektuyushhie_dlya_pk_page(Base):

    url = 'https://www.dns-shop.ru/catalog/17aa522a16404e77/komplektuyushhie-dlya-pk/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    subcategories = { 'Процессоры': '//a[contains(@href,"processory")]',
                      'Материнские платы': '//a[contains(@href,"materinskie-platy")]',
                      'Видеокарты': '//a[contains(@href,"videokarty")]',
                      'Оперативная память': '//a[contains(@href,"operativnaya-pamyat")]',
                      'Корпуса': '//a[contains(@href,"korpusa")]',
                      'Блоки питания': '//a[contains(@href,"bloki-pitaniya")]',
                      'Охлаждение компьютера': '//a[contains(@href,"oxlazhdenie-kompyutera")]',
                      'Твердотельные накопители': '//a[contains(@href,"tverdotelnye-nakopiteli")]',
                      'Жесткие диски': '//a[contains(@href,"zhestkie-diski")]',
                      'Мониторы': '//a[contains(@href,"monitory")]',}

    # Getters

    def get_subcategory(self, subcategory):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.subcategories[subcategory])))

    # Actions

    def subcategory_click(self, subcategory):
        self.get_subcategory(subcategory).click()
        print('Click subcategory "' + subcategory + '" button')
