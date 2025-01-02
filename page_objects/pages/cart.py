from selenium.webdriver.common.by import By
from helpers.base_helper import BaseHelper

class CartPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.baseHelper = BaseHelper(driver)

    item_qtd = (By.NAME, 'updates[]')
    continue_to_checkout_button = (By.NAME, 'checkout')

    def open_home_page(self, url):
        self.driver.get(url)

    def click_item_qtd(self):
        self.baseHelper.click_element(self.item_qtd)

    def set_item_qtd(self, qtd):
        self.baseHelper.click_element((By.XPATH, f'//option[@value="{qtd}"]'))

    def click_continue_to_checkout(self):
        self.baseHelper.click_element(self.continue_to_checkout_button)