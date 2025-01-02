from selenium.webdriver.common.by import By
from helpers.base_helper import BaseHelper


# page_url = about:blank
class GlucoseControlPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.baseHelper = BaseHelper(driver)

    GC_1mo_radio_button = (By.CSS_SELECTOR, 'div[data-product="pendulum-glucose-control-2-og"]')
    add_to_cart_button = (By.CSS_SELECTOR, 'button[type="submit"].btn.justify-content-center')
    upsell_modal_close = (By.CLASS_NAME, 'tingle-modal__close')

    def open_home_page(self, url):
        self.driver.get(url)

    def set_1month(self):
        self.baseHelper.click_element(self.GC_1mo_radio_button)

    def click_add_to_cart(self):
        self.baseHelper.click_element(self.add_to_cart_button)

    def click_close_upsell_modal(self):
        self.baseHelper.click_element(self.upsell_modal_close)