from base.session import Session
from pages.main_page import *

def test_login(set_group):
    driver = Session().create_session(webdriver_path='C:\\PycharmProjects\\lessons_selenium\\chromedriver.exe',
                                      url='https://www.dns-shop.ru/')
    """Test data"""
    email = 'cabome5150@wireps.com'
    password = 'y+9W*J6d@FG%'
    """Pages class instance"""
    main_page = Main_page(driver)
    """Test"""
    main_page.user_menu_move_mouse()
    main_page.user_menu_login_button_click()
    main_page.login_with_password_button_click()
    main_page.phone_or_email_textbox_input(email)
    main_page.password_textbox_input(password)
    main_page.login_window_login_button_click()
    main_page.get_rc_container()
    print('Login successfull, we got reCAPTCHA!')
    driver.close()
