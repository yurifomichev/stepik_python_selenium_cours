from base.session import Session
from pages.category_pages import *
from pages.main_page import *
from pages.subcategory_pages import *
from pages.products_list_pages import *
from pages.cart_page import *
from pages.checkout_page import *

def test_buy_videocard_product(set_up):
    driver = Session().create_session(webdriver_path='C:\\PycharmProjects\\lessons_selenium\\chromedriver.exe',
                                      url='https://www.dns-shop.ru/')
    """Test data"""
    request_url = 'https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/?stock=now&rating=1&review=1&price=49001-270999&action=vygodnyekomplekty&brand=gigabyte&f[p36]=b2oy&f[mx]=2fi&f[19n]=c0k&f[mz]=el42z&f[yg49]=1iaekr&fr[vf]=193-256&f[pgy]=bjwp&f[pkx]=bom1&f[yg48]=1iaekh'
    """Pages class instance"""
    base = Base(driver)
    main_page = Main_page(driver)
    products_list_page = Products_list_videokarty_page(driver)
    cart_page = Cart_page(driver)
    checkout_page = Checkout_page(driver)
    """Test"""
    main_page.catalog_category_click('Комплектующие для ПК')
    Category_komplektuyushhie_dlya_pk_page(driver).subcategory_click('Основные комплектующие для ПК')
    Subcategory_osnovnye_komplektuyushhie_dlya_pk_page(driver).subcategory_click('Видеокарты')
    ActionChains(driver).move_to_element(driver.find_element(By.XPATH, products_list_page.filter_consult_wrap)).perform()
    try:
        products_list_page.get_filter_consult_avatar()
        print('Consult wrap is visible, continue test')
    except:
        print('Consult wrap is not visible, continue test')
    """Check needed filter checkboxes"""
    products_list_page.filter_stock_checkbox_click('Под заказ: сегодня')
    products_list_page.filter_stock_checkbox_click('Под заказ: завтра')
    products_list_page.filter_stock_checkbox_click('Под заказ: позже')
    products_list_page.filter_rating_ckeckbox_click('Рейтинг 4')
    products_list_page.filter_review_ckeckbox_click('Есть обзор')
    products_list_page.filter_price_ckeckbox_click('49 001 ₽ и более')
    products_list_page.filter_action_ckeckbox_click('Выгодные комплекты')
    products_list_page.filter_search_textbox_input('Производитель', 'gigabyte')
    products_list_page.filter_brand_ckeckbox_click('GIGABYTE')
    products_list_page.filter_expander_click('Для игрового компьютера')
    products_list_page.filter_for_gaming_PC_ckeckbox_click('есть')
    products_list_page.filter_expander_click('Объем видеопамяти (ГБ)')
    products_list_page.filter_videomemory_ckeckbox_click('8 ГБ')
    products_list_page.filter_expander_click('Производитель графического процессора')
    products_list_page.filter_graphics_processor_producer_ckeckbox_click('NVIDIA')
    products_list_page.filter_expander_click('Тип памяти')
    products_list_page.filter_memory_type_ckeckbox_click('GDDR6')
    products_list_page.filter_expander_click('Интерфейс подключения')
    products_list_page.filter_connection_interface_ckeckbox_click('PCI-E 4.0')
    products_list_page.filter_expander_click('Разрядность шины памяти (бит)')
    products_list_page.filter_bus_radiobutton_click('193 - 256')
    products_list_page.filter_expander_click('Тип и количество установленных вентиляторов')
    products_list_page.filter_fan_ckeckbox_click('3 осевых')
    products_list_page.filter_expander_click('Профессиональная видеокарта')
    products_list_page.filter_professional_videocard_ckeckbox_click('нет')
    products_list_page.filter_expander_click('Количество подключаемых одновременно мониторов')
    products_list_page.filter_monitor_ckeckbox_click('4')
    products_list_page.filter_submit_button_click()
    """Check url with all filters"""
    if base.get_current_url() == request_url:
        print('Current url matches request PASSED')
    else:
        print('Current url matches request FAILED')
    driver.execute_script("window.scrollBy(0,-3000)", "");
    time.sleep(1)
    """Check name and price of product on products list, cart and checkout pages"""
    product_list_product_name = products_list_page.get_product_name_text()
    price_label = products_list_page.get_product_price_text().split(' ')
    product_list_product_price = price_label[0] + ' ' + price_label[1]
    products_list_page.product_buy_product_button_click()
    if products_list_page.get_cart_badge().text == '1':
        print('Products count on cart badge is correct PASSED')
    else:
        print('Products count on cart badge is correct FAILED')
    if products_list_page.get_cart_price().text == product_list_product_price:
        print('Products price on cart icon is correct PASSED')
    else:
        print('Products price on cart icon is correct FAILED')
    products_list_page.get_cart_badge().click()

    assert base.get_current_url() == cart_page.url
    print('Go to cart page PASSED')

    assert product_list_product_name.__contains__(product_list_product_name)
    print('Cart page product name = products list product name PASSED')

    assert cart_page.get_product_price_number() == product_list_product_price
    print('Cart page product price = products list product price PASSED')

    assert cart_page.get_order_conditions_product_price_number() == product_list_product_price
    print('Cart page order conditions section product price = products list product price PASSED')

    cart_page.formalization_button_click()

    assert base.get_current_url() == checkout_page.url
    print('Go to checkout page PASSED')

    assert checkout_page.get_products_count_number() == '1'
    print('Checkout page products count is correct PASSED')

    assert checkout_page.get_products_price_number() == product_list_product_price
    print('Checkout page products price = products list product price PASSED')

    time.sleep(1)
    print('Test PASSED')
    driver.close()