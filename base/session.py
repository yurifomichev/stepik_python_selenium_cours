from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Session():
    def create_session(self, webdriver_path, url):
        options = Options()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(executable_path=webdriver_path,
                                  options=options)
        driver.get(url)
        driver.maximize_window()
        return driver