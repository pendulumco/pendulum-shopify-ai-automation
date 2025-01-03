from selenium.webdriver.common.by import By
from helpers.base_helper import BaseHelper

class CartPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.baseHelper = BaseHelper(driver)

    item_qtd = (By.CLASS_NAME, 'quantity-selector')
    continue_to_checkout_button = (By.NAME, 'checkout')

    def open_home_page(self, url):
        self.driver.get(url)

    def set_item_qtd(self, qtd):
        self.baseHelper.select_option_by_value('[name="updates[]"', qtd)

    def click_continue_to_checkout(self):
        self.baseHelper.click_element_javascript(self.continue_to_checkout_button)