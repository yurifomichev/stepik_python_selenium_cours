from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    url = 'https://www.dns-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    # Locators_head buttons
    user_menu = '//div[@class="user-menu"]'
    cart_button = '//div[@class="cart-button"]'
    wishlist_link = '//a[@class="wishlist-link-counter"]'
    compare_link = '//a[@class="compare-link-counter"]'
    user_menu_login_button = '//button[@class="base-ui-button-v2_medium base-ui-button-v2_brand base-ui-button-v2_ico-none base-ui-button-v2"]'
    # Locators_login/register modal window
    login_with_password_button = '//div[@class="block-other-login-methods__password-button"]'
    phone_or_email_textbox = '//input[@autocomplete="username"]'
    password_textbox = '//input[@autocomplete="current-password"]'
    login_window_login_button = '//button[@class="base-ui-button-v2_big base-ui-button-v2_brand base-ui-button-v2_ico-none base-ui-button-v2"]'
    rc_container = '//iframe[@title="reCAPTCHA"]'
    # Locators_catalog
    catalog = { 'Бытовая техника':'//a[contains(@href,"bytovaya-texnika")]', 'Красота и здоровье':'//a[contains(@href,"krasota-i-zdorove")]', 'Смартфоны и фототехника':'//a[contains(@href,"smartfony-i-fototexnika")]',
                'ТВ, консоли и аудио':'//a[contains(@href,"tv-konsoli-i-audio")]', 'ПК, ноутбуки, периферия':'//a[contains(@href,"pk-noutbuki-periferiya")]', 'Комплектующие для ПК':'//a[contains(@href,"komplektuyushhie-dlya-pk")]',
                'Офис и мебель':'//a[contains(@href,"ofis-i-mebel")]', 'Сетевое оборудование':'//a[contains(@href,"setevoe-oborudovanie")]', 'Отдых и развлечения':'//a[contains(@href,"otdyx-i-razvlecheniya")]',
                'Инструмент и стройка':'//a[contains(@href,"instrument-i-strojka")]', 'Садовая техника':'//a[contains(@href,"sadovaya-texnika")]', 'Дом, декор и посуда':'//a[contains(@href,"dom-dekor-i-posuda")]',
                'Автотовары':'//a[contains(@href,"avtotovary")]', 'Аксессуары и услуги':'//a[contains(@href,"aksessuary-i-uslugi")]', 'Уцененные товары':'//a[contains(@href,"markdown")]', }

    # Getters

    def get_user_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_menu)))
    def get_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))
    def get_wishlist_link(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.wishlist_link)))
    def get_compare_link(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.compare_link)))
    def get_user_menu_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_menu_login_button)))
    def get_login_with_password_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_with_password_button)))
    def get_phone_or_email_textbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.phone_or_email_textbox)))
    def get_password_textbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password_textbox)))
    def get_login_window_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_window_login_button)))
    def get_rc_container(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.rc_container)))
    def get_catalog_category(self, catalog_category):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog[catalog_category])))

    # Actions

    def user_menu_move_mouse(self):
        ActionChains(self.driver).move_to_element(self.get_user_menu()).perform()
        print('Move mouse to user menu')
    def user_menu_login_button_click(self):
        self.get_user_menu_login_button().click()
        print('Click user menu login button')
    def login_with_password_button_click(self):
        self.get_login_with_password_button().click()
        print('Click login with password button')
    def phone_or_email_textbox_input(self, phone_or_email):
        self.get_phone_or_email_textbox().send_keys(phone_or_email)
        print('Input "' + phone_or_email + '" in phone or email textbox')
    def password_textbox_input(self, password):
        self.get_password_textbox().send_keys(password)
        print('Input "' + password + '" in password textbox')
    def login_window_login_button_click(self):
        self.get_login_window_login_button().click()
        print('Click login window login button')
    def catalog_category_click(self, catalog_category):
        self.get_catalog_category(catalog_category).click()
        print('Click catalog category "' + catalog_category + '" button')