from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# page_url = about:blank
class CartPage(object):
    def __init__(self, driver):
        self.driver = driver

    item_qtd = (By.NAME, 'updates[]')
    continue_to_checkout_button = (By.NAME, 'checkout')

    def open_home_page(self, url):
        self.driver.get(url)

    def click_item_qtd(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.item_qtd)
        ).click()

    def set_item_qtd(self, qtd):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//option[@value="{qtd}"]'))
        ).click()

    def click_continue_to_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_to_checkout_button)
        ).click()
