from pytest_selenium import driver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.util import timeout
from selenium.webdriver.support import expected_conditions as EC
from helpers.base_helper import BaseHelper


class products_page(object):
    def __init__(self, driver):
        self.driver = driver
        self.baseHelper = BaseHelper(driver)

    button_add_to_cart = (By.XPATH, "//button[text()='Add to cart']")
    button_close_upsell_modal = (By.CLASS_NAME, 'tingle-modal__close')

    def set_radio_data_product(self, product_name):
        dynamic_selector = f'div[data-product="{product_name}"]'
        self.baseHelper.click_element_javascript((By.CSS_SELECTOR, f'{dynamic_selector}'))

    def click_add_to_cart(self):
        self.baseHelper.click_element_javascript(self.button_add_to_cart)

    def click_close_upsell_modal(self):
        self.baseHelper.click_element(self.button_close_upsell_modal)
