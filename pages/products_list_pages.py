import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Products_list_videokarty_page(Base):

    url = 'https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)

    # Locators
    # Locators-filters

    filter_consult_wrap = '//div[@class="left-filters__consult-wrap"]'
    filter_consult_avatar = '//div[@class="question__avatar_zh0"]'
    filter_expanders = { 'Наличие в магазинах':'//span[@class="ui-collapse__link-text"][text()="Наличие в магазинах"]',
                       'Цена': '//span[@class="ui-collapse__link-text"][text()="Цена"]',
                       'Акция': '//span[@class="ui-collapse__link-text"][text()="Акция"]',
                       'Производитель': '//span[@class="ui-collapse__link-text"][text()="Производитель"]',
                       'Графический процессор': '//span[@class="ui-collapse__link-text"][text()="Графический процессор"]',
                       'Для игрового компьютера': '//span[@class="ui-collapse__link-text"][text()="Для игрового компьютера"]',
                       'Объем видеопамяти (ГБ)': '//span[@class="ui-collapse__link-text"][text()="Объем видеопамяти (ГБ)"]',
                       'Производитель графического процессора': '//span[@class="ui-collapse__link-text"][text()="Производитель графического процессора"]',
                       'Тип памяти': '//span[@class="ui-collapse__link-text"][text()="Тип памяти"]',
                       'Интерфейс подключения': '//span[@class="ui-collapse__link-text"][text()="Интерфейс подключения"]',
                       'Разрядность шины памяти (бит)': '//span[@class="ui-collapse__link-text"][text()="Разрядность шины памяти (бит)"]',
                       'Тип и количество установленных вентиляторов': '//span[@class="ui-collapse__link-text"][text()="Тип и количество установленных вентиляторов"]',
                       'Профессиональная видеокарта': '//span[@class="ui-collapse__link-text"][text()="Профессиональная видеокарта"]',
                       'Количество подключаемых одновременно мониторов': '//span[@class="ui-collapse__link-text"][text()="Количество подключаемых одновременно мониторов"]',
                       'LHR': '//span[@class="ui-collapse__link-text"][text()="LHR"]' }
    filter_search_textbox = { 'Производитель':'//div[@data-id="brand"]/div/div/div[@class="ui-input-search ui-input-search_list"]/input',
                              'Графический процессор': '//div[@data-id="f[mv]"]/div/div/div[@class="ui-input-search ui-input-search_list"]/input',
                              'Объем видеопамяти(ГБ)':'//div[@data-id="f[mx]"]/div/div/div[@class="ui-input-search ui-input-search_list"]/input' }
    filter_stock_checkbox = '//div[@data-id="stock"]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_rating_ckeckbox = '//div[@data-id="rating"]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_price_ckeckbox = '//div[@data-id="price"]/div/div/div[contains(@class,"ui-checkbox-group")]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_action_ckeckbox = '//div[@data-id="action"]/div/div/div[contains(@class,"ui-checkbox-group")]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_brand_ckeckbox = '//div[@data-id="brand"]/div/div/div[contains(@class,"ui-checkbox-group")]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_review_ckeckbox = '//div[@data-id="review"]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_reliable_models_checkbox = '//div[@data-id="rely"]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_graphics_processor_ckeckbox = '//div[@data-id="f[mv]"]/div/div/div[contains(@class,"ui-checkbox-group")]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_for_gaming_PC_ckeckbox = '//div[@data-id="f[p36]"]/div/div/div[contains(@class,"ui-checkbox-group")]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_videomemory_ckeckbox = '//div[@data-id="f[mx]"]/div/div/div[contains(@class,"ui-checkbox-group")]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_graphics_processor_producer_ckeckbox = '//div[@data-id="f[19n]"]/div/div/div[contains(@class,"ui-checkbox-group")]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_memory_type_ckeckbox = '//div[@data-id="f[mz]"]/div/div/div[contains(@class,"ui-checkbox-group")]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_connection_interface_ckeckbox = '//div[@data-id="f[yg49]"]/div/div/div[contains(@class,"ui-checkbox-group")]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_bus_radiobutton = '//div[@data-id="fr[vf]"]/div/div/div[contains(@class,"ui-radio ui-radio_list")]/label[contains(@class,"ui-radio")]/span[starts-with(text(),"replacement")]'
    filter_fan_ckeckbox = '//div[@data-id="f[pgy]"]/div/div/div[contains(@class,"ui-checkbox-group")]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_professional_videocard_ckeckbox = '//div[@data-id="f[pkx]"]/div/div/div[contains(@class,"ui-checkbox-group")]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_monitor_ckeckbox = '//div[@data-id="f[yg48]"]/div/div/div[contains(@class,"ui-checkbox-group")]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_LHR_checkbox = '//div[@data-id="f[suxy]"]/div/div/div[contains(@class,"ui-checkbox-group")]/label[contains(@class,"ui-checkbox")]/span[starts-with(text(),"replacement")]'
    filter_submit_button = '//button[@data-role="filters-submit"]'

    #Locators-products

    product_widget = '//div[@data-id="product"]'
    product_name = '//a[starts-with(@class,"catalog-product")]/span'
    product_price = '//div[@class="product-buy__price"]'
    product_buy_button = '//button[starts-with(@class,"button-ui buy")]'
    product_buy_certain_product_button = '//div[@data-code="replacement"]/div[starts-with(@class,"product-buy")]/button[starts-with(@class,"button-ui buy")]'

    #Locators-top_bar

    cart_badge = '//span[@class="cart-link-counter__badge"]'
    cart_price = '//span[@class="buttons__link-price cart-link-counter__price"]'

    # Getters

    def get_filter_consult_avatar(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.filter_consult_avatar)))

    def get_filter_expander(self, expander):
        return self.scroll_to_element(self.filter_expanders[expander])

    def get_filter_search_textbox(self, group):
        return self.scroll_to_element(self.filter_search_textbox[group])

    def get_filter_stock_checkbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_stock_checkbox.replace('replacement', checkbox_name))

    def get_filter_rating_ckeckbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_rating_ckeckbox.replace('replacement', checkbox_name))

    def get_filter_price_ckeckbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_price_ckeckbox.replace('replacement', checkbox_name))

    def get_filter_action_ckeckbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_action_ckeckbox.replace('replacement', checkbox_name))

    def get_filter_brand_ckeckbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_brand_ckeckbox.replace('replacement', checkbox_name))

    def get_filter_review_ckeckbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_review_ckeckbox.replace('replacement', checkbox_name))

    def get_filter_reliable_models_checkbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_reliable_models_checkbox.replace('replacement', checkbox_name))

    def get_filter_graphics_processor_ckeckbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_graphics_processor_ckeckbox.replace('replacement', checkbox_name))

    def get_filter_for_gaming_PC_ckeckbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_for_gaming_PC_ckeckbox.replace('replacement', checkbox_name))

    def get_filter_videomemory_ckeckbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_videomemory_ckeckbox.replace('replacement', checkbox_name))

    def get_filter_graphics_processor_producer_ckeckbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_graphics_processor_producer_ckeckbox.replace('replacement', checkbox_name))

    def get_filter_memory_type_ckeckbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_memory_type_ckeckbox.replace('replacement', checkbox_name))

    def get_filter_connection_interface_ckeckbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_connection_interface_ckeckbox.replace('replacement', checkbox_name))

    def get_filter_bus_radiobutton(self, radiobutton_name):
        return self.scroll_to_element(self.filter_bus_radiobutton.replace('replacement', radiobutton_name))

    def get_filter_fan_ckeckbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_fan_ckeckbox.replace('replacement', checkbox_name))

    def get_filter_professional_videocard_ckeckbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_professional_videocard_ckeckbox.replace('replacement', checkbox_name))

    def get_filter_monitor_ckeckbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_monitor_ckeckbox.replace('replacement', checkbox_name))

    def get_filter_LHR_checkbox(self, checkbox_name):
        return self.scroll_to_element(self.filter_LHR_checkbox.replace('replacement', checkbox_name))

    def get_filter_submit_button(self):
        return self.scroll_to_element(self.filter_submit_button)

    def get_product_buy_product_button(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.product_buy_button)))

    def get_product_name(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.product_name)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.product_price)))

    def get_product_buy_certain_product_button(self, product_id):
        return self.scroll_to_element(self.product_buy_certain_product_button.replace('replacement', product_id))

    def get_cart_badge(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.cart_badge)))

    def get_cart_price(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.cart_price)))

    # Actions

    def filter_expander_click(self, expander):
        self.get_filter_expander(expander).click()
        time.sleep(0.5)
        print('Click filter "' + expander + '" expander')

    def filter_search_textbox_input(self, group, text):
        self.get_filter_search_textbox(group).send_keys(text)
        print('Input text "' + text + '" in filter "Поиск" textbox in "' + group + '" group')

    def filter_stock_checkbox_click(self, checkbox_name):
        self.get_filter_stock_checkbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_rating_ckeckbox_click(self, checkbox_name):
        self.get_filter_rating_ckeckbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_price_ckeckbox_click(self, checkbox_name):
        self.get_filter_price_ckeckbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_action_ckeckbox_click(self, checkbox_name):
        self.get_filter_action_ckeckbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_brand_ckeckbox_click(self, checkbox_name):
        self.get_filter_brand_ckeckbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_review_ckeckbox_click(self, checkbox_name):
        self.get_filter_review_ckeckbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_reliable_models_checkbox_click(self, checkbox_name):
        self.get_filter_reliable_models_checkbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_graphics_processor_ckeckbox_click(self, checkbox_name):
        self.get_filter_graphics_processor_ckeckbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_for_gaming_PC_ckeckbox_click(self, checkbox_name):
        self.get_filter_for_gaming_PC_ckeckbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_videomemory_ckeckbox_click(self, checkbox_name):
        self.get_filter_videomemory_ckeckbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_graphics_processor_producer_ckeckbox_click(self, checkbox_name):
        self.get_filter_graphics_processor_producer_ckeckbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_memory_type_ckeckbox_click(self, checkbox_name):
        self.get_filter_memory_type_ckeckbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_connection_interface_ckeckbox_click(self, checkbox_name):
        self.get_filter_connection_interface_ckeckbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_bus_radiobutton_click(self, radiobutton_name):
        self.get_filter_bus_radiobutton(radiobutton_name).click()
        print('Click filter "' + radiobutton_name + '" checkbox')

    def filter_fan_ckeckbox_click(self, checkbox_name):
        self.get_filter_fan_ckeckbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_professional_videocard_ckeckbox_click(self, checkbox_name):
        self.get_filter_professional_videocard_ckeckbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_monitor_ckeckbox_click(self, checkbox_name):
        self.get_filter_monitor_ckeckbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_LHR_checkbox_click(self, checkbox_name):
        self.get_filter_LHR_checkbox(checkbox_name).click()
        print('Click filter "' + checkbox_name + '" checkbox')

    def filter_submit_button_click(self):
        self.get_filter_submit_button().click()
        print('Click filter submit button')

    def get_product_name_text(self):
        product_name_text = self.get_product_name()[0].text
        print('Products list page product name is ' + product_name_text)
        return product_name_text

    def get_product_price_text(self):
        product_price_text = self.get_product_price()[0].text
        print('Products list page product price is ' + product_price_text)
        return product_price_text

    def product_buy_product_button_click(self):
        self.get_product_buy_product_button()[0].click()
        print('Click buy product button')

    def product_buy_certain_product_button_click(self, product_id):
        self.get_product_buy_certain_product_button(product_id).click()
        print('Click buy product with id "' + product_id + '" button')