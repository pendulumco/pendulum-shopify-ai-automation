from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.base_helper import BaseHelper


class MetabolicDailyPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.baseHelper = BaseHelper(driver)

    MD_3mo_radio_button = (By.CSS_SELECTOR, 'div[data-product="pendulum-metabolic-daily-membership-90-count"]')
    add_to_cart_button = (By.CSS_SELECTOR, 'button[type="submit"].btn.justify-content-center')
    upsell_modal_close = (By.CLASS_NAME, 'tingle-modal__close')

    def open_home_page(self, url):
        self.driver.get(url)

    def set_3months(self):
        self.baseHelper.click_element(self.MD_3mo_radio_button)

    def click_add_to_cart(self):
        self.baseHelper.click_element(self.add_to_cart_button)

    def click_close_upsell_modal(self):
        self.baseHelper.click_element(self.upsell_modal_close)


